"""Exploratory associations, not estimates of the causal effects of sequencing."""
from pathlib import Path
import sys, os, json, warnings

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / 'python-deps'))
os.environ.setdefault('MPLCONFIGDIR', str(BASE / 'mpl-cache'))
import numpy as np
import pandas as pd
import statsmodels.api as sm
import patsy

RAW = BASE / 'raw'
OUT = BASE
OUT.mkdir(exist_ok=True)
CODE_MAP = {'TAW':'TWN', 'SIN':'SGP', 'ROM':'ROU', 'ZAR':'COD', 'UAE':'ARE'}
ASIA = ['KOR','TWN','SGP','JPN','CHN','MYS','IDN','THA','PHL','IND','VNM','PAK','LKA','MMR']
warnings.filterwarnings('ignore', category=UnicodeWarning)

dc = ['country_name','wbcode','year','y','dem','demCGV','demBMR','region',
      'gdppercapitaconstant2000us','secenr','mortnew','lp_bl','ls_bl','lh_bl']
d = pd.read_stata(RAW/'ddcg_replication/replication_files_ddcg/DDCGdata_final.dta',
                  columns=dc, convert_categoricals=False)
d['iso'] = d.wbcode.replace(CODE_MAP)
d['year'] = d.year.astype(int)
d['log_gdp_ddcg'] = d.y / 100  # The supplied y variable is 100 * log GDP.
c = pd.read_stata(RAW/'state_capacity_v1/StateCapacityDataset_v1.dta', convert_categoricals=False)
c['iso'] = c.iso3.replace(CODE_MAP)
c['year'] = c.year.astype(int)
m = pd.read_stata(RAW/'maddison2023.dta', convert_categoricals=False)
m['iso'] = m.countrycode.replace(CODE_MAP)
m['year'] = m.year.astype(int)
m = m.loc[m.year.ge(1950)].copy()
m['log_gdp_mpd'] = np.log(m.gdppc.where(m.gdppc.gt(0)))
for frame in (d,c,m):
    assert not frame.duplicated(['iso','year']).any(), 'Duplicate country-year key'

pd.DataFrame([
    {'source':'DDCG','original':k,'harmonized':v} for k,v in CODE_MAP.items()
]).to_csv(OUT/'country_code_crosswalk.csv',index=False)
pd.DataFrame({'ddcg_without_capacity':sorted(set(d.iso)-set(c.iso))}).to_csv(OUT/'unmatched_ddcg_countries.csv',index=False)
pd.DataFrame({'capacity_without_ddcg':sorted(set(c.iso)-set(d.iso))}).to_csv(OUT/'unmatched_capacity_countries.csv',index=False)

merged = d.merge(c[['iso','year','Capacity','Capacity_sd','v2clrspct','WBregion']],
                 on=['iso','year'], how='left', validate='one_to_one')
merged = merged.merge(m[['iso','year','gdppc','log_gdp_mpd']],
                      on=['iso','year'],how='left',validate='one_to_one')
merged.to_csv(OUT/'country_year_panel.csv',index=False)
di = d.set_index(['iso','year'])
mi = m.set_index(['iso','year'])
ci = c.set_index(['iso','year'])

def value(frame, iso, year, col):
    try:
        val = frame.loc[(iso,year),col]
        return float(val) if pd.notna(val) else np.nan
    except KeyError:
        return np.nan

def annual_growth(iso, start, horizon, source):
    frame,col = (di,'log_gdp_ddcg') if source=='ddcg' else (mi,'log_gdp_mpd')
    a,b = value(frame,iso,start,col),value(frame,iso,start+horizon,col)
    return (b-a)*100/horizon

def mean_pre(iso, t, col):
    # CZE denotes Czechoslovakia before 1993 in HS, but Czech Republic in DDCG.
    # Do not silently assign the predecessor's capacity to the successor country.
    if iso == 'CZE' and t-5 < 1993:
        return np.nan
    vals = [value(ci,iso,y,col) for y in range(t-5,t)]
    return float(np.mean(vals)) if np.isfinite(vals).all() else np.nan

def pre_distribution(t, col='Capacity'):
    window = c.loc[c.year.between(t-5,t-1)].groupby('iso')[col].agg(['mean','count'])
    return window.loc[window['count'].eq(5),'mean'].dropna()

transitions=[]
for iso,g in d.groupby('iso'):
    g=g.sort_values('year')
    dates=g.loc[g.dem.eq(1) & g.dem.shift(1).eq(0) & g.year.diff().eq(1),'year'].tolist()
    eligible_count=0
    for t in dates:
        pre_dem=[value(di,iso,y,'dem') for y in range(t-5,t)]
        pre_ok=t>=1965 and np.isfinite(pre_dem).all() and all(v==0 for v in pre_dem)
        if pre_ok: eligible_count+=1
        cap=mean_pre(iso,t,'Capacity')
        peers=pre_distribution(t)
        base=t-1
        row={
          'iso':iso,'country':g.country_name.iloc[0],'region':g.region.iloc[0],
          'transition_year':t,'baseline_year':base,'five_nondem_years':pre_ok,
          'first_eligible_transition':bool(pre_ok and eligible_count==1),
          'capacity_pre5':cap,'capacity_posterior_sd_pre5':mean_pre(iso,t,'Capacity_sd'),
          'administration_pre5':mean_pre(iso,t,'v2clrspct'),
          'capacity_world_percentile':100*(peers<=cap).mean() if np.isfinite(cap) else np.nan,
          'capacity_above_world_median':float(cap>=peers.median()) if np.isfinite(cap) else np.nan,
          'log_gdp0_ddcg':value(di,iso,base,'log_gdp_ddcg'),
          'log_gdp0_mpd':value(mi,iso,base,'log_gdp_mpd'),
          'pre_growth10_ddcg':annual_growth(iso,base-10,10,'ddcg'),
          'pre_growth10_mpd':annual_growth(iso,base-10,10,'mpd'),
        }
        for source in ['ddcg','mpd']:
            for h in [10,20]:
                row[f'growth{h}_{source}']=annual_growth(iso,base,h,source)
        deaths0=value(di,iso,base,'mortnew');deaths10=value(di,iso,base+10,'mortnew')
        row['mortality_change10']=deaths10-deaths0
        vals=[value(mi,iso,y,'log_gdp_mpd') for y in range(base,base+11)]
        row['negative_growth_years10_mpd']=int((np.diff(vals)<0).sum()) if np.isfinite(vals).all() else np.nan
        row['main_eligible']=bool(row['first_eligible_transition'] and np.isfinite(cap) and np.isfinite(row['growth10_ddcg']))
        reasons=[]
        if not pre_ok:reasons.append('no five consecutive observed pre-transition non-democratic years')
        elif not row['first_eligible_transition']:reasons.append('later eligible transition')
        if not np.isfinite(cap):
            reasons.append('predecessor/successor boundary mismatch: Czechoslovakia/Czech Republic' if iso=='CZE' and t-5<1993 else 'incomplete pre-transition capacity')
        if not np.isfinite(row['growth10_ddcg']):reasons.append('missing ten-year DDCG GDP endpoint')
        row['main_exclusion_reason']='; '.join(reasons)
        transitions.append(row)
tall=pd.DataFrame(transitions)
eligible=tall.loc[tall.first_eligible_transition & tall.capacity_pre5.notna()].copy()
normalization={}
for col,z in [('capacity_pre5','cap_z'),('administration_pre5','admin_z')]:
    mu,sd=eligible[col].mean(),eligible[col].std(ddof=1)
    tall[z]=(tall[col]-mu)/sd
    normalization[z]={'mean':mu,'sd':sd,'reference':'all first eligible transitions with complete pre-capacity, before GDP selection'}
tall['t_center']=tall.transition_year-1985
tall.to_csv(OUT/'all_observed_transitions.csv',index=False)
main=tall.loc[tall.main_eligible].copy()
main.to_csv(OUT/'main_transition_sample.csv',index=False)

results=[]
fitted={}
def fit(name,frame,formula,terms=('cap_z',),cluster=False):
    y,x=patsy.dmatrices(formula,frame,return_type='dataframe')
    rank=np.linalg.matrix_rank(x.to_numpy())
    assert rank==x.shape[1], f'{name}: rank deficient design'
    groups=frame.loc[x.index,'iso']
    if cluster:
        res=sm.OLS(y,x).fit(cov_type='cluster',cov_kwds={'groups':groups,'use_correction':True},use_t=True)
    else:
        res=sm.OLS(y,x).fit(cov_type='HC3',use_t=True)
    for term in terms:
        ci_=res.conf_int().loc[term]
        results.append({'model':name,'formula':formula,'term':term,'estimate':res.params[term],
          'se':res.bse[term],'ci_low':ci_.iloc[0],'ci_high':ci_.iloc[1],'p':res.pvalues[term],
          'n':int(res.nobs),'countries':int(groups.nunique()),'covariance':'country-clustered' if cluster else 'HC3',
          'r2':res.rsquared,'df_resid':res.df_resid})
    fitted[name]=(res,frame.loc[x.index].copy())
    pd.DataFrame({'iso':groups,'observed':y.iloc[:,0],'fitted':res.fittedvalues,'residual':res.resid}).to_csv(OUT/(name+'_rows.csv'),index=False)
    return res

fit('transition_raw',main,'growth10_ddcg ~ cap_z')
fit('transition_income_year',main,'growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center')
fit('transition_prior_growth',main,'growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center + pre_growth10_ddcg')
fit('transition_region',main,'growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center + C(region)')
fit('transition_admin',main,'growth10_ddcg ~ admin_z + log_gdp0_ddcg + t_center',terms=('admin_z',))
fit('transition_without_korea_taiwan',main.loc[~main.iso.isin(['KOR','TWN'])],'growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center')
fit('transition_mpd_same_sample',main,'growth10_mpd ~ cap_z + log_gdp0_mpd + t_center')
fit('transition_mpd20_same_sample',main,'growth20_mpd ~ cap_z + log_gdp0_mpd + t_center')
extended=tall.loc[tall.first_eligible_transition & tall.capacity_pre5.notna()].copy()
fit('transition_mpd_extended',extended,'growth10_mpd ~ cap_z + log_gdp0_mpd + t_center')
fit('transition_mpd20_extended',extended,'growth20_mpd ~ cap_z + log_gdp0_mpd + t_center')
fit('transition_ddcg20',main,'growth20_ddcg ~ cap_z + log_gdp0_ddcg + t_center')
repeated=tall.loc[tall.five_nondem_years & tall.capacity_pre5.notna()].copy()
fit('transition_repeated',repeated,'growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center',cluster=True)
fit('transition_mpd_negative_years',extended,'negative_growth_years10_mpd ~ cap_z + log_gdp0_mpd + t_center')

# Common-sample specifications distinguish covariate changes from sample changes.
common=main.dropna(subset=['pre_growth10_ddcg','log_gdp0_ddcg','cap_z'])
fit('transition_common_income_year',common,'growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center')

# Added after the first run because GDP-source sensitivity remained unresolved.
# Hold rows fixed, then separately swap the outcome and baseline income series.
source_common=main.dropna(subset=['growth10_mpd','log_gdp0_mpd'])
fit('source_common_ddcg',source_common,'growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center')
fit('source_common_mpd_outcome_only',source_common,'growth10_mpd ~ cap_z + log_gdp0_ddcg + t_center')
fit('source_common_mpd_income_only',source_common,'growth10_ddcg ~ cap_z + log_gdp0_mpd + t_center')
fit('mpd20_prior_growth',extended,'growth20_mpd ~ cap_z + log_gdp0_mpd + t_center + pre_growth10_mpd')
fit('mpd20_without_korea_taiwan',extended.loc[~extended.iso.isin(['KOR','TWN'])],
    'growth20_mpd ~ cap_z + log_gdp0_mpd + t_center')
fit('mpd20_admin',extended,'growth20_mpd ~ admin_z + log_gdp0_mpd + t_center',terms=('admin_z',))
source_common[['iso','country','transition_year','growth10_ddcg','growth10_mpd',
               'log_gdp0_ddcg','log_gdp0_mpd']].assign(
    growth_difference=lambda x:x.growth10_mpd-x.growth10_ddcg
).to_csv(OUT/'gdp_source_comparison.csv',index=False)

loo=[]
for iso in main.iso.unique():
    sample=main.loc[main.iso.ne(iso)]
    y,x=patsy.dmatrices('growth10_ddcg ~ cap_z + log_gdp0_ddcg + t_center',sample,return_type='dataframe')
    r=sm.OLS(y,x).fit(cov_type='HC3',use_t=True)
    lo,hi=r.conf_int().loc['cap_z']
    loo.append({'excluded':iso,'estimate':r.params['cap_z'],'ci_low':lo,'ci_high':hi})
pd.DataFrame(loo).to_csv(OUT/'leave_one_country_out.csv',index=False)

# Broad panel: capacity before each decade and democracy at its starting year.
panel=[]
for iso,g in d.groupby('iso'):
    for yr in [1970,1980,1990,2000]:
        cap=mean_pre(iso,yr,'Capacity')
        if not np.isfinite(cap):continue
        panel.append({'iso':iso,'year':yr,'country':g.country_name.iloc[0],
            'capacity_pre5':cap,'dem':value(di,iso,yr,'dem'),
            'log_gdp0':value(di,iso,yr,'log_gdp_ddcg'),
            'growth10':annual_growth(iso,yr,10,'ddcg')})
panel=pd.DataFrame(panel).dropna(subset=['growth10','dem','log_gdp0','capacity_pre5'])
panel['cap_z']=(panel.capacity_pre5-panel.capacity_pre5.mean())/panel.capacity_pre5.std(ddof=1)
panel.to_csv(OUT/'decade_panel.csv',index=False)
fit('panel_cohort',panel,'growth10 ~ cap_z * dem + log_gdp0 + C(year)',terms=('cap_z','dem','cap_z:dem'),cluster=True)
fit('panel_country_cohort',panel,'growth10 ~ cap_z * dem + log_gdp0 + C(year) + C(iso)',terms=('cap_z','dem','cap_z:dem'),cluster=True)

pd.DataFrame(results).to_csv(OUT/'model_results.csv',index=False)
main.groupby('capacity_above_world_median').agg(n=('iso','size'),
  mean_growth10=('growth10_ddcg','mean'),median_growth10=('growth10_ddcg','median'),
  mean_initial_income_log=('log_gdp0_ddcg','mean')).to_csv(OUT/'descriptive_capacity_groups.csv')

asian=[]
for iso in ASIA:
    dg=d.loc[d.iso.eq(iso)].sort_values('year')
    ts=tall.loc[tall.iso.eq(iso) & tall.first_eligible_transition]
    row={'iso':iso,'country':dg.country_name.iloc[0] if len(dg) else iso,
         'DDCG_dem_1960':value(di,iso,1960,'dem'),'DDCG_dem_2010':value(di,iso,2010,'dem'),
         'qualifying_transition':int(ts.transition_year.iloc[0]) if len(ts) else np.nan,
         'capacity_1960':value(ci,iso,1960,'Capacity'),'capacity_2010':value(ci,iso,2010,'Capacity'),
         'mpd_gdppc_1960':value(mi,iso,1960,'gdppc'),'mpd_gdppc_2022':value(mi,iso,2022,'gdppc')}
    if len(ts):
        for col in ['capacity_world_percentile','growth10_ddcg','growth10_mpd','growth20_mpd','pre_growth10_ddcg','main_eligible']:
            row[col]=ts.iloc[0][col]
    row['gdppc_ratio_2022_1960']=row['mpd_gdppc_2022']/row['mpd_gdppc_1960']
    asian.append(row)
pd.DataFrame(asian).to_csv(OUT/'asian_cases.csv',index=False)

# Internal check of previously saved patent counts. No upstream query was rerun.
source_snapshot='wzhang109-state-coordination-0346cc0'
pat=pd.read_csv(BASE/'input_patent_counts_1990_2010.csv')
wide=pat.pivot(index='filing_year',columns='sector',values='patent_count')
wide['auto_to_textile_ratio']=wide.automobiles/wide.textiles
wide.to_csv(OUT/'existing_patent_counts_internal_check.csv')
pat_summary=[]
for sector in ['automobiles','textiles']:
    for start,end in [(1990,2000),(2001,2010),(1990,2010)]:
        pat_summary.append({'sector':sector,'start':start,'end':end,'start_count':wide.loc[start,sector],
          'end_count':wide.loc[end,sector],'cagr_percent':100*((wide.loc[end,sector]/wide.loc[start,sector])**(1/(end-start))-1)})
pd.DataFrame(pat_summary).to_csv(OUT/'existing_patent_growth_internal_check.csv',index=False)

summary={
 'capacity_raw_country_codes':int(c.iso.nunique()),
 'capacity_codes_with_nonmissing_estimates':int(c.loc[c.Capacity.notna(),'iso'].nunique()),
 'capacity_named_entities_with_nonmissing_estimates':int(c.loc[c.Capacity.notna(),'country'].nunique()),
 'capacity_rows_with_nonmissing_estimates':int(c.Capacity.notna().sum()),
 'capacity_country_years':len(c),'democracy_countries':int(d.iso.nunique()),
 'observed_transitions':len(tall),'eligible_first_transitions_pre_gdp':int(tall.first_eligible_transition.sum()),
 'first_transitions_complete_capacity':len(eligible),'main_countries':len(main),
 'main_transition_year_min':int(main.transition_year.min()),'main_transition_year_max':int(main.transition_year.max()),
 'panel_countries':int(panel.iso.nunique()),'panel_country_decades':len(panel),
 'normalization':normalization,'loo_range':[min(x['estimate']for x in loo),max(x['estimate']for x in loo)],
 'source_commit_folder':source_snapshot,'software':{'python':sys.version,'numpy':np.__version__,'pandas':pd.__version__,'statsmodels':sm.__version__},
 'notes':['No regression identifies a causal effect of authoritarianism, Legalism or sequencing.',
          'DDCG y is 100*log GDP. Results use percentage points of annualized log GDP growth.',
          'Main outcomes span t-1 to t+9: exactly ten years; 20-year outcomes span t-1 to t+19.',
          'Main sample includes subsequent regime reversals; no conditioning on democratic survival.',
          'SER is not remapped to SRB because Serbia-Montenegro and Serbia have different boundaries.',
          'Pre-1993 CZE capacity is Czechoslovakia, not Czech Republic; mixed predecessor/successor capacity windows excluded.',
          'First eligible transition means first observed transition after >=5 nondemocratic years, not first transition in national history.']
}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False))
print(json.dumps(summary,indent=2,ensure_ascii=False))
print(pd.DataFrame(results)[['model','term','estimate','ci_low','ci_high','n','countries']].to_string(index=False))
print(pd.DataFrame(asian).to_string(index=False))
