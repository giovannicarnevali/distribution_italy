"""Scarica i dati grezzi del paper, UN FILE PER OGNI DATASET, in data/raw/<fonte>/.
Fonti: AMECO (via DBnomics), OCSE Economic Outlook (via DBnomics), Eurostat (API SDMX).
UN Comtrade è scaricato da fetch_comtrade.py (serve una chiave); World Bank e PWT sono file già in data/raw/.
Uso: python scripts/python/fetch_raw.py            (dalla radice del repository)
"""
import os, time, requests, pandas as pd

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "raw")
def out(src, name): d = os.path.join(ROOT, src); os.makedirs(d, exist_ok=True); return os.path.join(d, name)

def dbn(provider, dataset, series):
    j = requests.get(f"https://api.db.nomics.world/v22/series/{provider}/{dataset}/{series}?observations=1", timeout=90).json()
    s = j["series"]["docs"][0]
    df = pd.DataFrame({"period": s["period"], "value": s["value"]})
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df.insert(0, "series_code", f"{provider}/{dataset}/{series}"); df.insert(1, "series_name", s.get("series_name", ""))
    return df

# ---------------- AMECO, Italia: una serie per file ----------------
AMECO_ITA = {
    # conti nazionali e distribuzione
    "UVGD": "1.0.0.0", "OVGD": "1.1.0.0", "PVGD": "3.1.0.0", "UWCD": "1.0.0.0", "UOGD": "1.0.0.0", "UQGD": "1.0.0.0", "UQND": "1.0.0.0",
    "UTVN": "1.0.0.0", "UTSG": "1.0.0.0", "ALCD0": "1.0.0.0", "NWTD": "1.0.0.0", "NETD": "1.0.0.0", "NETN": "1.0.0.0", "NLHT": "1.0.0.0",
    # capitale e investimenti
    "OKND": "1.0.0.0", "OIGT": "1.1.0.0", "UIGT": "1.0.0.0", "UIGG": "1.0.0.0", "PIGT": "3.1.0.0",
    # estero e finanza pubblica
    "UBCA": "1.0.0.0", "UBGS": "1.0.0.0", "UBLA": "1.0.0.0", "UXGS": "1.0.0.0", "UMGS": "1.0.0.0", "UBLG": "1.0.0.0", "UBLGI": "1.0.0.0",
    "UDGG": "1.0.0.0", "USGP": "1.0.0.0",
    # competitività e lavoro
    "XUNRQ": "3.0.30.415", "QLCD": "3.1.0.0", "ZUTN": "1.0.0.0",
}
for code, suf in AMECO_ITA.items():
    try:
        # OVGD/PVGD/OIGT/PIGT/QLCD hanno suffissi diversi a seconda del codice; prova il suffisso dato, poi il generico
        for s in (suf, "1.0.0.0", "1.1.0.0", "3.1.0.0"):
            try:
                df = dbn("AMECO", code, f"ITA.{s}.{code}"); break
            except Exception: df = None
        if df is None: print("AMECO manca", code); continue
        df.to_csv(out("ameco", f"AMECO_{code}_ITA.csv"), index=False); print("AMECO", code, len(df))
    except Exception as e: print("AMECO errore", code, e)
    time.sleep(0.3)

# ---------------- AMECO, pannello 14 paesi per lo SCM: una serie per file ----------------
C14 = ["ITA", "ESP", "FRA", "BEL", "NLD", "AUT", "PRT", "FIN", "GRC", "DEU", "IRL", "DNK", "SWE", "GBR"]
for code, suf in {"ALCD0": "1.0.0.0", "XUNRQ": "3.0.30.415", "ZUTN": "1.0.0.0"}.items():
    frames = []
    for c in C14:
        try:
            d = dbn("AMECO", code, f"{c}.{suf}.{code}"); d.insert(0, "iso", c); frames.append(d)
        except Exception as e: print("AMECO panel manca", code, c)
        time.sleep(0.3)
    pd.concat(frames).to_csv(out("ameco", f"AMECO_{code}_panel14.csv"), index=False); print("AMECO panel", code)

# ---------------- OCSE Economic Outlook, Italia: una serie per file ----------------
for code in ["NLGQ", "NLGXQ", "TYB", "TYH", "SSRG", "SRATIO"]:
    try:
        df = dbn("OECD", "EO", f"ITA.{code}.A"); df.to_csv(out("oecd_eo", f"OECD_EO_{code}_ITA.csv"), index=False); print("OECD EO", code, len(df))
    except Exception as e: print("OECD EO errore", code, e)
    time.sleep(0.5)

# ---------------- Eurostat: conti per settore istituzionale (B9) e nama_10_a64 per l'Italia ----------------
EUROSTAT = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
def eurostat(dataset, key, name):
    r = requests.get(f"{EUROSTAT}/{dataset}/{key}", params={"format": "SDMX-CSV", "compressed": "false"}, timeout=180)
    if r.status_code != 200: print("Eurostat", dataset, r.status_code, r.text[:120]); return
    open(out("eurostat", name), "w", encoding="utf8").write(r.text); print("Eurostat", name, r.text.count("\n"), "righe")
eurostat("nasa_10_nf_tr", "A.CP_MEUR.PAID.B9.S1+S11+S12+S13+S14+S15+S14_S15+S2.IT", "ESTAT_nasa_10_nf_tr_B9_IT.csv")
eurostat("nama_10_a64", "A.CP_MEUR.A+A01+B-E+C+D+F+G+G-I+H+H49+I+J+J61+K+L+M_N+O-Q+R-U+TOTAL.D1+B1G.IT", "ESTAT_nama_10_a64_D1_B1G_IT.csv")
eurostat("nama_10_a64_p5", "A.CP_MEUR...P51G.IT", "ESTAT_nama_10_a64_p5_P51G_IT.csv")
print("fatto")
