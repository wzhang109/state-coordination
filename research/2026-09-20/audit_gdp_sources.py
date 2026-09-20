"""Late, explicitly logged source diagnostics using current World Bank GDP."""
from pathlib import Path
import sys,json
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'python-deps'))
import pandas as pd
import numpy as np
import statsmodels.api as sm
import patsy
R=BASE
raw=json.loads((BASE/'raw/wdi_real_gdppc.json').read_text())
assert raw[0]['pages']==1
w=pd.DataFrame([{'iso':v['countryiso3code'],'year':int(v['date']),'gdppc':v['value']} for v in raw[1] if v['countryiso3code']])
assert not w.duplicated(['iso','year']).any()
w['log_gdppc']=np.log(w.gdppc.where(w.gdppc.gt(0)))
wi=w.set_index(['iso','year'])
def logval(iso,year):
    try:return float(wi.loc[(iso,year),'log_gdppc'])
    except KeyError:return np.nan

e=pd.read_csv(R/'all_observed_transitions.csv')
e=e.loc[e.first_eligible_transition & e.capacity_pre5.notna()].copy()
for idx,row in e.iterrows():
    t=int(row.transition_year)-1
    b=logval(row.iso,t)
    e.loc[idx,'log_gdp0_wdi']=b
    e.loc[idx,'pre_growth10_wdi']=100*(b-logval(row.iso,t-10))/10
    for h in [10,20]:e.loc[idx,f'growth{h}_wdi']=100*(logval(row.iso,t+h)-b)/h
main=e.loc[e.main_eligible].copy()
common10=main.dropna(subset=['growth10_wdi','log_gdp0_wdi','growth10_mpd','log_gdp0_mpd'])
common20=e.dropna(subset=['growth20_wdi','log_gdp0_wdi','growth20_mpd','log_gdp0_mpd'])
results=[]
def fit(name,frame,formula):
    y,x=patsy.dmatrices(formula,frame,return_type='dataframe')
    assert np.linalg.matrix_rank(x.to_numpy())==x.shape[1]
    res=sm.OLS(y,x).fit(cov_type='HC3',use_t=True)
    low,high=res.conf_int().loc['cap_z']
    results.append({'model':name,'formula':formula,'term':'cap_z','estimate':res.params['cap_z'],'se':res.bse['cap_z'],'ci_low':low,'ci_high':high,'p':res.pvalues['cap_z'],'n':int(res.nobs),'countries':int(frame.loc[x.index,'iso'].nunique()),'covariance':'HC3','r2':res.rsquared})
    pd.DataFrame({'iso':frame.loc[x.index,'iso'],'observed':y.iloc[:,0],'fitted':res.fittedvalues}).to_csv(R/(name+'_rows.csv'),index=False)
fit('wdi10_primary_cohort',main,'growth10_wdi ~ cap_z + log_gdp0_wdi + t_center')
fit('wdi10_primary_prior_growth',main,'growth10_wdi ~ cap_z + log_gdp0_wdi + t_center + pre_growth10_wdi')
fit('wdi10_common_mpd',common10,'growth10_wdi ~ cap_z + log_gdp0_wdi + t_center')
fit('mpd10_common_wdi',common10,'growth10_mpd ~ cap_z + log_gdp0_mpd + t_center')
fit('wdi20_common_mpd',common20,'growth20_wdi ~ cap_z + log_gdp0_wdi + t_center')
fit('mpd20_common_wdi',common20,'growth20_mpd ~ cap_z + log_gdp0_mpd + t_center')
fit('wdi20_common_prior_growth',common20,'growth20_wdi ~ cap_z + log_gdp0_wdi + t_center + pre_growth10_wdi')
fit('wdi20_without_korea_taiwan',common20.loc[~common20.iso.isin(['KOR','TWN'])],'growth20_wdi ~ cap_z + log_gdp0_wdi + t_center')
pd.DataFrame(results).to_csv(R/'wdi_diagnostic_models.csv',index=False)
e.to_csv(R/'transitions_with_wdi.csv',index=False)
common20.to_csv(R/'wdi_mpd_common20_sample.csv',index=False)
audit={'wdi_api_metadata':raw[0],'common10_n':len(common10),'common20_n':len(common20),
       'interpretation':'Post-result GDP-source diagnostic, not a confirmatory test or causal estimate.'}
(R/'wdi_audit_summary.json').write_text(json.dumps(audit,indent=2))
print(pd.DataFrame(results)[['model','estimate','ci_low','ci_high','n']].to_string(index=False))
print(e.loc[e.iso.isin(['KOR','TWN','MOZ','IDN','PHL']),['iso','transition_year','growth10_wdi','growth20_wdi','growth10_mpd','growth20_mpd']].to_string(index=False))
