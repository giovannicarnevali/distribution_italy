"""Settori privatizzati vs manifatturiero, Italia 1995-2024 (Eurostat nama_10_a64 e nama_10_a64_p5), Tabella 6bis.1.
Surplus operativo lordo e reddito misto per branca ottenuto per identità dei conti: B2A3G = B1G - D1 - D29X39
(Eurostat non pubblica B2A3G a livello A64; D29X39 = altre imposte meno contributi alla produzione).
Indicatori per periodo (somme di periodo): quota del surplus sul VA = B2A3G/B1G; tasso di investimento = P51G/B1G;
investimenti fissi lordi in rapporto al surplus = P51G/B2A3G (NON una quota di profitti reinvestita: flussi lordi,
gli investimenti possono essere finanziati con debito, il surplus non coincide con gli utili); crescita del VA in volume
(CLV10) e del deflatore implicito del VA. Le branche sono intere (D, J61, K, H): non coincidono con le imprese privatizzate.
Uso: python scripts/python/privatizzate_surplus.py   (dalla radice del repository)
"""
import pandas as pd, numpy as np
d=pd.read_csv('data/raw/eurostat/ESTAT_nama_10_a64_D1_B1G_IT.csv'); d=d[d.unit=='CP_MEUR']
tx=pd.read_csv('data/raw/eurostat/ESTAT_nama_10_a64_D29X39_IT.csv')
p=pd.read_csv('data/raw/eurostat/ESTAT_nama_10_a64_p5_P51G_IT.csv'); p=p[(p.unit=='CP_MEUR')&(p.asset10=='N11G')]
clv=pd.read_csv('data/raw/eurostat/ESTAT_nama_10_a64_B1G_CLV10_IT.csv')
W=lambda df,item: df[df.na_item==item].pivot(index='TIME_PERIOD',columns='nace_r2',values='OBS_VALUE')
B1G,D1,I,R,TX=W(d,'B1G'),W(d,'D1'),W(p,'P51G'),W(clv,'B1G'),W(tx,'D29X39')
PER={'1995-2000':(1995,2000),'2001-07':(2001,2007),'2008-13':(2008,2013),'2014-24':(2014,2024)}
rows=[]
for b,lab in {'D':'Energia','J61':'Telecom','K':'Finanza','H':'Trasporti (H)','C':'Manifatt.','TOTAL':'Totale'}.items():
    SUR=B1G[b]-D1[b]-TX[b]
    for per,(a,z) in PER.items():
        s=slice(a,z)
        rows.append(dict(branca=lab,periodo=per,quota_surplus=SUR.loc[s].sum()/B1G[b].loc[s].sum()*100,
            sussidi_netti_su_VA=-TX[b].loc[s].sum()/B1G[b].loc[s].sum()*100,
            tasso_inv=I[b].loc[s].sum()/B1G[b].loc[s].sum()*100, inv_su_surplus=I[b].loc[s].sum()/SUR.loc[s].sum()*100,
            crescita_VA_reale=(np.log(R[b].loc[z]/R[b].loc[a])/(z-a)*100) if b in R.columns else np.nan,
            deflatore_VA=(np.log((B1G[b]/R[b]).loc[z]/(B1G[b]/R[b]).loc[a])/(z-a)*100) if b in R.columns else np.nan,
            quota_VA_totale=B1G[b].loc[s].sum()/B1G['TOTAL'].loc[s].sum()*100))
t=pd.DataFrame(rows).round(1); t.to_csv('data/derived/privatizzate_surplus_investimenti.csv',index=False)
for k in ['quota_surplus','sussidi_netti_su_VA','tasso_inv','inv_su_surplus','crescita_VA_reale','deflatore_VA','quota_VA_totale']:
    print('\n==',k); print(t.pivot(index='branca',columns='periodo',values=k).loc[['Energia','Telecom','Finanza','Trasporti (H)','Manifatt.','Totale']].to_string())
