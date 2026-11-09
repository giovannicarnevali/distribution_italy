"""Scarica da UN Comtrade (API v1) gli export verso il mondo per prodotto SITC a 3 cifre.
SITC Rev.3 per gli anni <= 2006, Rev.4 dal 2007 (classificazione in cui i paesi UE riportano).
Uso: python fetch_comtrade.py <SUBSCRIPTION_KEY> <out.csv>
"""
import sys, time, requests, pandas as pd

KEY, OUT = sys.argv[1], sys.argv[2]
H = {"Ocp-Apim-Subscription-Key": KEY}
REPORTERS = {"381": "ITA", "251": "FRA", "276": "DEU", "724": "ESP", "620": "PRT", "752": "SWE"}
YEARS = range(1995, 2024)

rows = []
for code, iso in REPORTERS.items():
    for yr in YEARS:
        cl = "S3" if yr <= 2006 else "S4"
        p = dict(reporterCode=code, period=str(yr), partnerCode="0", flowCode="X", cmdCode="AG3",
                 motCode="0", customsCode="C00", partner2Code="0")
        for attempt in range(5):
            r = requests.get(f"https://comtradeapi.un.org/data/v1/get/C/A/{cl}", params=p, headers=H, timeout=120)
            if r.status_code == 429:
                time.sleep(3); continue
            break
        j = r.json()
        for d in j.get("data", []):
            rows.append(dict(iso=iso, year=yr, cl=cl, sitc3=d["cmdCode"], value_usd=d["primaryValue"]))
        print(iso, yr, cl, len(j.get("data", [])), j.get("error", ""), flush=True)
        time.sleep(1.1)

pd.DataFrame(rows).to_csv(OUT, index=False)
print("saved", OUT, len(rows))
