"""Audit time windows, data joins, source integrity and reported calculations."""
from pathlib import Path
import sys, os, json, hashlib, csv
BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / 'python-deps'))
os.environ.setdefault('MPLCONFIGDIR', str(BASE / 'mpl-cache'))
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

R = BASE
checks = []
def check(name, condition, detail=''):
    assert condition, name
    checks.append({'check':name,'passed':True,'detail':detail})

main = pd.read_csv(R/'main_transition_sample.csv')
events = pd.read_csv(R/'all_observed_transitions.csv')
models = pd.read_csv(R/'model_results.csv')
models = pd.concat([models,pd.read_csv(R/'wdi_diagnostic_models.csv')],ignore_index=True)
summary = json.loads((R/'summary.json').read_text())
d = pd.read_stata(BASE/'raw/ddcg_replication/replication_files_ddcg/DDCGdata_final.dta',convert_categoricals=False)
c = pd.read_stata(BASE/'raw/state_capacity_v1/StateCapacityDataset_v1.dta',convert_categoricals=False)
m = pd.read_stata(BASE/'raw/maddison2023.dta',convert_categoricals=False)
cross = {'TAW':'TWN','SIN':'SGP','ROM':'ROU','ZAR':'COD','UAE':'ARE'}
d['iso'] = d.wbcode.replace(cross)
c['iso'] = c.iso3.replace(cross)
m['iso'] = m.countrycode.replace(cross)
check('Unique country-year keys in all three sources', all(not f.duplicated(['iso','year']).any() for f in [d,c,m]))
check('Main cohort has 57 unique countries',len(main)==main.iso.nunique()==57)
check('Czech predecessor mismatch excluded','CZE' not in set(main.iso))
check('Taiwan GDP absent from primary cohort; no invented Singapore transition', 'TWN' not in set(main.iso) and 'SGP' not in set(events.iso))
for row in main.itertuples():
    t=int(row.transition_year)
    demo=d.loc[d.iso.eq(row.iso)].set_index('year')
    cap=c.loc[c.iso.eq(row.iso)].set_index('year')
    assert (demo.loc[list(range(t-5,t)),'dem']==0).all()
    assert demo.loc[t,'dem']==1
    assert np.isclose(cap.loc[list(range(t-5,t)),'Capacity'].mean(),row.capacity_pre5,rtol=1e-6)
    # DDCG stores 100*ln(GDP), so dividing the difference by 10 yields annual log percentage points.
    growth=(float(demo.loc[t+9,'y'])-float(demo.loc[t-1,'y']))/10
    assert np.isclose(growth,row.growth10_ddcg,atol=1e-5)
check('All 57 pre-capacity, five-year regime and exact ten-year outcome windows checked',True)
kor=main.set_index('iso').loc['KOR']
check('Korea 1987 to 1997 ten-year growth',np.isclose(kor.growth10_ddcg,6.430015563964844))
twn=m.loc[m.iso.eq('TWN')].set_index('year')
twn20=100*np.log(float(twn.loc[2011,'gdppc'])/float(twn.loc[1991,'gdppc']))/20
check('Taiwan 1991 to 2011 twenty-year growth independently calculated',np.isclose(twn20,4.114868048155804))

# Independent closed-form OLS and HC3 calculation for the primary model.
X=np.column_stack([np.ones(len(main)),main.cap_z,main.log_gdp0_ddcg,main.t_center])
y=main.growth10_ddcg.to_numpy()
b=np.linalg.lstsq(X,y,rcond=None)[0]
inv=np.linalg.inv(X.T@X)
h=np.einsum('ij,jk,ik->i',X,inv,X)
e=y-X@b
cov=inv@(X.T@(((e/(1-h))**2)[:,None]*X))@inv
primary=models.loc[models.model.eq('transition_income_year')].iloc[0]
check('Primary coefficient and HC3 standard error independently reproduced',np.isclose(b[1],primary.estimate) and np.isclose(np.sqrt(cov[1,1]),primary.se))

same_a=pd.read_csv(R/'source_common_ddcg_rows.csv')
same_b=pd.read_csv(R/'transition_mpd_same_sample_rows.csv')
check('GDP-source comparison uses identical 55 countries',len(same_a)==len(same_b)==55 and set(same_a.iso)==set(same_b.iso))
w20=pd.read_csv(R/'wdi20_common_mpd_rows.csv')
m20=pd.read_csv(R/'mpd20_common_wdi_rows.csv')
check('Current WDI and MPD twenty-year comparison uses identical 57 countries',len(w20)==len(m20)==57 and set(w20.iso)==set(m20.iso))
wraw=json.loads((BASE/'raw/wdi_real_gdppc.json').read_text())
wlookup={(r['countryiso3code'],int(r['date'])):r['value'] for r in wraw[1]}
kor_wdi20=100*np.log(wlookup['KOR',2007]/wlookup['KOR',1987])/20
check('Current WDI Korea twenty-year growth independently calculated',np.isclose(kor_wdi20,float(w20.set_index('iso').loc['KOR','observed'])))
with open(BASE/'raw/mpd_GDPpc.csv') as f:
    excel_rows=list(csv.reader(f))
mozi=excel_rows[2].index('MOZ')
moz_excel={int(r[0]):float(r[mozi]) for r in excel_rows[3:] if r[0] in ['1993','2003']}
moz_stata=m.loc[m.iso.eq('MOZ')].set_index('year')
check('Surprising Mozambique MPD values match official Stata and Excel releases',all(np.isclose(v,float(moz_stata.loc[y,'gdppc'])) for y,v in moz_excel.items()))
for entry in json.loads((BASE/'raw/manifest.json').read_text()):
    path=BASE/'raw'/entry['file']
    check('SHA256 '+entry['file'],hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'])
(R/'validation.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False))

selected = [
 ('transition_income_year','Primary: 10 years, DDCG GDP'),
 ('wdi10_primary_cohort','Primary cohort: current WDI GDP, 10 years'),
 ('wdi20_common_mpd','Common sample: current WDI GDP, 20 years'),
 ('mpd20_common_wdi','Common sample: Maddison GDP, 20 years'),
 ('wdi20_common_prior_growth','Current WDI, 20 years + prior growth'),
]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(14,6.7))
fig.subplots_adjust(left=.35,right=.76,top=.79,bottom=.32)
for i,(key,label) in enumerate(selected):
    row=models.loc[models.model.eq(key)].iloc[0]
    color='#176d79' if i<2 else '#595d79'
    ax.errorbar(row.estimate,4-i,xerr=[[row.estimate-row.ci_low],[row.ci_high-row.estimate]],fmt='o',color=color,capsize=4,linewidth=2,markersize=7)
    ax.text(1.05,4-i,f'{row.estimate:+.2f}  [{row.ci_low:+.2f}, {row.ci_high:+.2f}]',transform=ax.get_yaxis_transform(),va='center',ha='left',fontsize=10)
ax.set_yticks(range(5),[f'{label}  (n={int(models.loc[models.model.eq(key),"n"].iloc[0])})' for key,label in selected[::-1]])
ax.tick_params(axis='y',length=0,pad=15)
ax.axvline(0,color='#808080',linestyle='--',linewidth=1)
ax.set_xlim(-1,2.7);ax.set_ylim(-.6,4.6)
ax.set_xticks([-1,0,1,2]);ax.grid(axis='x',alpha=.12)
ax.set_xlabel('Annualized log GDP per capita growth: percentage-point difference\nassociated with one SD higher pre-transition state capacity',labelpad=13)
fig.text(.035,.945,'Does state capacity before democratization predict later growth?',fontsize=17,fontweight='bold',color='#19313d')
fig.text(.035,.892,'A clearer positive association over 20 years; this does not establish a required political sequence.',fontsize=11.5,color='#4d5960')
fig.text(.035,.155,'Dots: adjusted associations. Lines: 95% HC3 intervals. All rows adjust for initial income and transition year.',fontsize=10,color='#4d5960')
fig.text(.035,.11,'One SD = 0.694 capacity units in the fixed 71-transition reference cohort. Sample coverage differs as labeled.',fontsize=10,color='#4d5960')
fig.text(.035,.065,'Sources: Hanson & Sigman v1; DDCG; World Bank WDI (July 2026); Maddison Project 2023. See sources.md.',fontsize=10,color='#4d5960')
fig.text(.035,.02,'Exploratory analysis, 20 September 2026. These estimates do not identify effects of authoritarianism or institutional sequencing.',fontsize=10,color='#793b29')
fig.savefig(R/'capacity_growth.png',dpi=170,facecolor='white')
fig.savefig(R/'capacity_growth.svg',facecolor='white')
plt.close(fig)
print(json.dumps({'validation_checks_passed':len(checks),'main_n':len(main),'figure':str(R/'capacity_growth.png')}))
print(pd.read_csv(R/'gdp_source_comparison.csv').assign(abs_diff=lambda x:x.growth_difference.abs()).nlargest(6,'abs_diff')[['iso','country','growth10_ddcg','growth10_mpd','growth_difference']].to_string(index=False))
