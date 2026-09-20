"""Post-publication diagnostic review; not a confirmatory analysis or causal claim.
Checks specified before this run: reproduce WDI20 headline; examine every
single-country omission; compare 10/20 horizons on identical rows; inspect
region/cohort controls and primary/secondary sample differences.
"""
import json,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent
import pandas as pd
import statsmodels.formula.api as smf
R=BASE
d=pd.read_csv(R/'wdi_mpd_common20_sample.csv')
main=pd.read_csv(R/'main_transition_sample.csv')
def fit(frame,formula):
    r=smf.ols(formula,frame).fit(cov_type='HC3',use_t=True)
    ci=r.conf_int().loc['cap_z']
    return {'n':int(r.nobs),'estimate':float(r.params['cap_z']),'ci':[float(ci.iloc[0]),float(ci.iloc[1])],'p':float(r.pvalues['cap_z'])}
formula='growth20_wdi ~ cap_z + log_gdp0_wdi + t_center'
result={'status':'post-result diagnostic review; exploratory','headline_reproduced':fit(d,formula)}
loo=[]
for iso in d.iso:
    row=fit(d[d.iso!=iso],formula);row['excluded']=iso;loo.append(row)
result['leave_one_out']={'estimate_min':min(loo,key=lambda x:x['estimate']),'estimate_max':max(loo,key=lambda x:x['estimate']),'intervals_include_zero':sum(x['ci'][0]<=0<=x['ci'][1] for x in loo),'runs':len(loo)}
paired=d.dropna(subset=['growth10_wdi','growth20_wdi','cap_z','log_gdp0_wdi','t_center']).copy()
paired['growth20_minus_growth10']=paired.growth20_wdi-paired.growth10_wdi
result['same_sample_horizons']={k:fit(paired,f'{y} ~ cap_z + log_gdp0_wdi + t_center') for k,y in [('ten','growth10_wdi'),('twenty','growth20_wdi'),('difference','growth20_minus_growth10')]}
result['twenty_with_region']=fit(d,formula+' + C(region)')
d['transition_decade']=(d.transition_year//10*10).astype(int)
result['twenty_with_decade_instead_of_linear_year']=fit(d,'growth20_wdi ~ cap_z + log_gdp0_wdi + C(transition_decade)')
result['cohort_difference']={'overlap':len(set(main.iso)&set(d.iso)),'primary_only':sorted(set(main.iso)-set(d.iso)),'twenty_common_only':sorted(set(d.iso)-set(main.iso))}
result['all_single_country_omissions']=loo
result['input_sha256']={name:hashlib.sha256((R/name).read_bytes()).hexdigest() for name in ['wdi_mpd_common20_sample.csv','main_transition_sample.csv']}
Path(__file__).with_name('rigor_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'all_single_country_omissions'},indent=2))
