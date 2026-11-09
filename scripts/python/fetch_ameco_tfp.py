import requests, pandas as pd, sys
out=sys.argv[1]
codes={'OVGD':'ITA.1.1.0.0.OVGD','UVGD':'ITA.1.0.0.0.UVGD','PVGD':'ITA.3.1.0.0.PVGD','PIGT':'ITA.3.1.0.0.PIGT',
       'NETD':'ITA.1.0.0.0.NETD','NLHT':'ITA.1.0.0.0.NLHT','OKND':'ITA.1.0.0.0.OKND','UWCD':'ITA.1.0.0.0.UWCD',
       'UOGD':'ITA.1.0.0.0.UOGD','UQGD':'ITA.1.0.0.0.UQGD','UTVN':'ITA.1.0.0.0.UTVN','ALCD0':'ITA.1.0.0.0.ALCD0',
       'OIGT':'ITA.1.1.0.0.OIGT','NWTD':'ITA.1.0.0.0.NWTD'}
d={}
for k,c in codes.items():
    r=requests.get(f"https://api.db.nomics.world/v22/series/AMECO/{k}/{c}?observations=1",timeout=30)
    docs=r.json().get('series',{}).get('docs',[]) if r.status_code==200 else []
    if not docs: print("MISSING",k,r.status_code); continue
    doc=docs[0]; s=pd.to_numeric(pd.Series(doc['value'],index=[int(p[:4]) for p in doc['period']]),errors='coerce')
    d[k]=s; print(k, s.dropna().index.min(), s.dropna().index.max(), doc.get('series_name','')[:60])
pd.DataFrame(d).loc[1960:2024].to_csv(out)
