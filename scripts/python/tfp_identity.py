import pandas as pd, numpy as np, sys
pd.set_option('display.width',200)
df=pd.read_csv(sys.argv[1],index_col=0).loc[1960:2024]
Y=df['OVGD']; P=df['PVGD']/100; L=df['NETD']; K=df['OKND']          # K a prezzi 2020 (stessa base di OVGD)
Yn=df['UVGD']; W=df['UWCD']; OGS=df['UOGD']; T=df['UTVN']
# quota lavoro aggiustata per autonomi, a costo dei fattori (base ALCD0, come nel paper)
omega_adj = (df['ALCD0']/100*Yn)/(Yn-T)
# fattori: Y a costo fattori reale
Yfc = (Yn-T)/P
w = omega_adj*Yfc/L                 # "salario" reale aggiustato per occupato (costo fattori)
r = (1-omega_adj)*Yfc/K             # saggio di profitto su K reale (stessa deflazione -> identità esatta)
g=lambda s: np.log(s).diff()
sh = (omega_adj+omega_adj.shift(1))/2   # Tornqvist
solow = g(Yfc) - sh*g(L) - (1-sh)*g(K)             # "TFP" = residuo di Solow
ident = sh*g(w) + (1-sh)*g(r)                       # lato distributivo dell'identità
print("max |residuo di Solow − (ω ŵ + (1−ω) r̂)| =", round((solow-ident).abs().max(),10), " <- identità esatta")
per={'1961-69':(1961,1969),'1970-79':(1970,1979),'1980-92':(1980,1992),'1993-2007':(1993,2007),'2008-13':(2008,2013),'2014-24':(2014,2024),'1996-2019':(1996,2019)}
rows=[]
for lab,(a,b) in per.items():
    sl=slice(a,b)
    rows.append({'periodo':lab,'g_Y':100*g(Yfc).loc[sl].mean(),'g_L':100*g(L).loc[sl].mean(),'g_K':100*g(K).loc[sl].mean(),
                 'TFP (Solow)':100*solow.loc[sl].mean(),'ω·ŵ':100*(sh*g(w)).loc[sl].mean(),'(1−ω)·r̂':100*((1-sh)*g(r)).loc[sl].mean(),
                 'ŵ reale':100*g(w).loc[sl].mean(),'r̂':100*g(r).loc[sl].mean(),'ω media':100*omega_adj.loc[sl].mean()})
t=pd.DataFrame(rows).set_index('periodo').round(2); print(t.to_string())
t.to_csv(sys.argv[2])
# produttività del lavoro reale vs nominale (capacità di valorizzazione), per occupato e per ora
LPr = Y/L; LPn = Yn/L
H=df['NLHT']; LPr_h=Y/H; LPn_h=Yn/H
rows=[]
for lab,(a,b) in per.items():
    sl=slice(a,b); rows.append({'periodo':lab,'LP reale/occ':100*g(LPr).loc[sl].mean(),'LP nominale/occ':100*g(LPn).loc[sl].mean(),
        'LP reale/ora':100*g(LPr_h).loc[sl].mean(),'LP nominale/ora':100*g(LPn_h).loc[sl].mean(),'deflatore PIL':100*g(P).loc[sl].mean(),'Δω (pp/anno)':100*omega_adj.diff().loc[sl].mean()})
t2=pd.DataFrame(rows).set_index('periodo').round(2); print("\n",t2.to_string()); t2.to_csv(sys.argv[3])
