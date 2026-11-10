"""Settori privatizzati vs manifatturiero, Italia 1995-2024 (Eurostat nama_10_a64 e nama_10_a64_p5):
quota profitti = (B1G-D1)/B1G; tasso di investimento = P51G/B1G; surplus reinvestito = P51G/(B1G-D1);
crescita reale del valore aggiunto (CLV10). Serve a confrontare l'attesa di Torrini (2005, p. 32: espansione dei
settori privatizzati) con la tesi di Modiano-Onado (2023: rendite non reinvestite). H49 non ha P51G: si usa H.
Uso: python scripts/python/privatizzate_surplus.py   (dalla radice del repository) -> data/derived/privatizzate_surplus_investimenti.csv
"""
import pandas as pd, numpy as np
d=pd.read_csv('data/raw/eurostat/ESTAT_nama_10_a64_D1_B1G_IT.csv'); d=d[d.unit=='CP_MEUR']
p=pd.read_csv('data/raw/eurostat/ESTAT_nama_10_a64_p5_P51G_IT.csv'); p=p[(p.unit=='CP_MEUR')&(p.asset10=='N11G')]
clv=pd.read_csv('data/raw/eurostat/ESTAT_nama_10_a64_B1G_CLV10_IT.csv')
W=lambda df,item: df[df.na_item==item].pivot(index='TIME_PERIOD',columns='nace_r2',values='OBS_VALUE')
B1G,D1,I,R=W(d,'B1G'),W(d,'D1'),W(p,'P51G'),W(clv,'B1G')
br={'D':'Energia','J61':'Telecom','H':'Trasporti (H)','K':'Finanza','C':'Manifatt.','TOTAL':'Totale'}
PER={'1995-2000':(1995,2000),'2001-07':(2001,2007),'2008-13':(2008,2013),'2014-24':(2014,2024)}
rows=[]
for b,lab_b in br.items():
    sur=B1G[b]-D1[b]
    for lab,(a,z) in PER.items():
        s=slice(a,z)
        rows.append(dict(branca=lab_b,periodo=lab,quota_profitti=sur.loc[s].sum()/B1G[b].loc[s].sum()*100,
            tasso_inv=I[b].loc[s].sum()/B1G[b].loc[s].sum()*100, inv_su_surplus=I[b].loc[s].sum()/sur.loc[s].sum()*100,
            crescita_VA_reale=(np.log(R[b].loc[z]/R[b].loc[a])/(z-a)*100) if b in R.columns else np.nan,
            quota_VA_totale=B1G[b].loc[s].sum()/B1G['TOTAL'].loc[s].sum()*100))
t=pd.DataFrame(rows).round(1); t.to_csv('data/derived/privatizzate_surplus_investimenti.csv',index=False)
for k in ['quota_profitti','tasso_inv','inv_su_surplus','crescita_VA_reale','quota_VA_totale']:
    print('\n==',k); print(t.pivot(index='branca',columns='periodo',values=k).loc[list(br.values())].to_string())
