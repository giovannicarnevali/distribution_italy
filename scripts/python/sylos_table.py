import pandas as pd, numpy as np, sys, statsmodels.api as sm
df=pd.read_csv(sys.argv[1],index_col=0).loc[1960:2024]
g=lambda s: np.log(s).diff()
gLP=g(df['OVGD']/df['NETD']); gY=g(df['OVGD']); gL=g(df['NETD'])
ric=g((df['UWCD']/df['NWTD'])/(df['PIGT']/100))
X=pd.DataFrame({'gY':gY,'ric_l1':ric.shift(1)})
rows=[]
for lab,a,b in [("1961-2024",1961,2024),("1961-1992",1961,1992),("1993-2024",1993,2024),("1993-2007",1993,2007)]:
    d=pd.concat([gLP.rename('gLP'),gL.rename('gL'),X],axis=1).loc[a:b].dropna()
    m=sm.OLS(d['gLP'],sm.add_constant(d[['gY','ric_l1']])).fit(cov_type='HAC',cov_kwds={'maxlags':3})
    mL=sm.OLS(d['gL'],sm.add_constant(d[['gY','ric_l1']])).fit(cov_type='HAC',cov_kwds={'maxlags':3})
    rows.append({'campione':lab,'n':len(d),'b_Y (prod.)':m.params['gY'],'se':m.bse['gY'],'c_Ricardo':m.params['ric_l1'],'se_c':m.bse['ric_l1'],'p_c':m.pvalues['ric_l1'],
                 'elast. occup.':mL.params['gY'],'se_L':mL.bse['gY'],'R2':m.rsquared})
t=pd.DataFrame(rows).set_index('campione').round(3); print(t.to_string()); t.to_csv(sys.argv[2])
