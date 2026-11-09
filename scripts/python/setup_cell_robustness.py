# === CELLA DI SETUP per le sezioni 12-15 (UQND + robustness) ===
# Esegui questa cella UNA VOLTA dopo aver caricato il dataset M in memoria.
# Crea gli alias e le serie necessarie alle celle successive.

import numpy as np
import pandas as pd

# --- 1. Crea alias r_main (= r del paper, lordo aggiustato) ---
if 'r_main' not in M.columns:
    if 'r' in M.columns:
        M['r_main'] = M['r']
    else:
        # Ricostruisci se manca (formula del paper)
        M['K_cur'] = M['OKND'] * (M['PIGT']/100)
        M['r_main'] = M['UQGD'] / (M['K_cur'] + M['UWCD'])
    print(f"  r_main creato. Range: {M['r_main'].dropna().index.min()}-{M['r_main'].dropna().index.max()}")

# --- 2. Crea omega se manca (quota salari aggiustata) ---
if 'omega' not in M.columns:
    M['omega'] = M['ALCD0'] / 100
    print(f"  omega creato")

# --- 3. Scarica UQND e crea r_NETTO/r_NETTO_strict se mancano ---
if 'UQND' not in M.columns:
    print("  Scarico UQND da AMECO...")
    uqnd = ameco_fetch('UQND', 'ITA.1.0.0.0.UQND')
    M['UQND'] = uqnd
    M['r_NETTO'] = M['UQND'] / (M['K_cur'] + M['UWCD'])
    M['r_NETTO_strict'] = M['UQND'] / M['K_cur']
    M['ammort_share'] = 1 - M['UQND']/M['UQGD']
    print(f"  UQND, r_NETTO, r_NETTO_strict creati")

# --- 4. Crea r_prime, r_gross se mancano ---
if 'r_prime' not in M.columns:
    M['r_prime'] = M['UQGD'] / M['K_cur']
if 'r_gross' not in M.columns and 'UOGD' in M.columns:
    M['r_gross'] = M['UOGD'] / M['K_cur']

# --- 5. Scarica REER (XUNRQ) per ADF/KPSS - codice corretto in DBnomics ---
if 'REER' not in M.columns:
    print("  Scarico REER (XUNRQ-4 ITA.3.0.30.437.XUNRQ, base 2020=100)...")
    try:
        reer = ameco_fetch('XUNRQ-4', 'ITA.3.0.30.437.XUNRQ')
        M['REER'] = reer
        print(f"  REER creato. Range: {M['REER'].dropna().index.min()}-{M['REER'].dropna().index.max()}")
    except Exception as e:
        print(f"  Avviso REER: {e}")

# --- 6. Crea IK se manca ---
if 'IK' not in M.columns:
    if 'UIGT' not in M.columns:
        print("  Scarico UIGT...")
        M['UIGT'] = ameco_fetch('UIGT', 'ITA.1.0.0.0.UIGT')
    M['IK'] = M['UIGT'] / M['OKND']
    print(f"  IK creato")

# --- 7. Crea CA_Y se manca ---
if 'CA_Y' not in M.columns:
    if 'UBCA' not in M.columns:
        M['UBCA'] = ameco_fetch('UBCA', 'ITA.1.0.0.0.UBCA')
    M['CA_Y'] = M['UBCA'] / M['UVGD']
    print(f"  CA_Y creato")

# --- 8. Crea q_proxy (composizione organica K/W) ---
if 'q_proxy' not in M.columns:
    M['q_proxy'] = M['OKND'] / M['UWCD']
    print(f"  q_proxy creato")

# --- Verifica finale ---
required = ['r_main', 'omega', 'r_prime', 'r_gross', 'r_NETTO', 'r_NETTO_strict', 
            'REER', 'IK', 'CA_Y', 'q_proxy']
missing = [c for c in required if c not in M.columns]
if missing:
    print(f"\n  ATTENZIONE: colonne ancora mancanti: {missing}")
else:
    print(f"\n  Setup OK. Tutte le {len(required)} colonne presenti in M.")
    print(f"  Range dataset: {M.index.min()}-{M.index.max()}, T={len(M)}")
