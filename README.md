# distribution_italy

**Le lotte di classe in Italia. Fasi del declino italiano 1980–2024**
Working paper di Giovanni Battista Carnevali. Versione corrente: **v23_REVIEWED** (9 novembre 2026, 106 pagine).

Lettura econometrica del declino italiano come sequenza di regimi di conflitto distributivo (profit squeeze fordista 1970-79; restaurazione istituzionale post-Maastricht 1992-2007; finanziarizzazione ed export-led 2008-2024), in un quadro Marx-Goodwin-Sylos Labini-Aglietta-Godley-Graziani-Bellofiore. Dati AMECO 1960-2024, Eurostat NACE A64 1995-2024, OCSE EO/MSTI, World Bank. Metodi: PELT, Quandt-Andrews, Chow narrativi HAC + Holm-Bonferroni, Bai-Perron (strucchange e replica Python), Synthetic Control (con estensione alla Grecia), DiD staggered (TWFE + Callaway-Sant'Anna), cointegrazione/VECM, decomposizione di Kalecki, identità distributiva della TFP (Felipe-McCombie), equazione di produttività di Sylos Labini, composizione tecnologica dell'export (UN Comtrade, tassonomia di Lall).

## Struttura del repository

```
README.md                 questo file
CLAUDE.md                 istruzioni per Claude (Code / chat) all'apertura del repo
docs/
  ISTRUZIONI_PROGETTO_CHATGPT.md   istruzioni da incollare nel progetto ChatGPT (valide anche per Kimi/DeepSeek)
  CONTEXT.md              conoscenza stabile del progetto: tesi, struttura, risultati, dati, decisioni chiuse
  HANDOFF.md              stato corrente, pendenti, prompt di apertura (si aggiorna a ogni sessione)
  COLLABORATION.md        protocollo multi-LLM: ruoli, formato delle review, triage
paper/
  working_paper_v23_REVIEWED.docx / .pdf
  archive/                          versioni precedenti (v22)
data/
  ameco_tfp.csv                     AMECO (DBnomics) 1960-2024: OVGD UVGD PVGD PIGT NETD NLHT OKND UWCD UOGD UQGD UTVN ALCD0 OIGT NWTD
  kalecki_data_full.csv             serie per l'equazione dei profitti (AMECO + OCSE EO)
  kalecki_decomposition_robust.csv  decomposizione per periodi, con imposte indirette
  omega_irap_corrected.csv          ω con correzione approssimativa IRAP 1998 (3 varianti)
  bai_perron_irap_check.csv         break Bai-Perron su ω originale e corretta
  did_eurostat_REAL.csv             Eurostat nama_10_a64 IT, D1/B1G, 7 branche, 1995-2024 (209 oss.) — il file letto dallo script R
  ameco_scm_panel.csv               ALCD0, XUNRQ, ZUTN per 14 paesi 1960-2024 (SCM)
  scm_greece_results.csv, scm_simple_gap_*.csv   SCM baseline e con Grecia (§8.6, §8.6.1)
  bai_perron_series7.csv, bai_perron_two_specs.csv   7 serie e break BIC per le due specificazioni (§5.5)
  comtrade_sitc3_raw.csv            UN Comtrade, export SITC 3 cifre, 6 paesi 1995-2023
  lall_shares.csv, lall_periods.csv quote tecnologiche (Lall 2000), per anno e per periodo (Tabella 5bis.1)
  preliminary/*_SIMULATO.csv        dataset illustrativi delle versioni preliminari: NON sono dati reali, conservati solo per tracciabilità
  tfp_identity_table.csv            TFP ≡ ω·ŵ + (1−ω)·r̂ per periodi
  lp_real_nominal.csv               produttività reale vs nominale
  sylos_table.csv, sylos_means.csv  equazione di Sylos Labini, 4 campioni
  r_unit_root_full.csv, r_breakpoints.csv, r_results.csv   output R (urca, strucchange)
  scm_leave_one_out.csv, specializzazione_lockin.csv
scripts/
  python/fetch_ameco_tfp.py         scarica AMECO via DBnomics
  python/tfp_identity.py            identità distributiva della TFP (pesi Törnqvist)
  python/sylos_table.py             equazione di Sylos Labini, OLS HAC(3)
  python/scm_greece.py              Synthetic Control baseline + Grecia, placebo in-space, leave-one-out
  python/bai_perron.py              Bai-Perron (DP, BIC) con specificazione 'mean' e 'trend'
  python/fetch_comtrade.py          scarica export SITC3 da UN Comtrade (serve chiave gratuita)
  python/lall_classify.py           tassonomia di Lall e quote per periodo
  python/setup_cell_robustness.py
  R/did_callaway_santanna.R         DiD staggered (pacchetto did), event-study
  R/working_paper_robustness.R      Phillips-Ouliaris, Johansen, Bai-Perron  [sul PC dell'autore]
notebooks/
  Marx_Schumpeter_Italia_v12_robustness.ipynb   notebook finale (le versioni v2-v11 restano sul PC dell'autore)
```

## Replicare

```bash
pip install pandas numpy statsmodels requests
python scripts/python/fetch_ameco_tfp.py        # → data/ameco_tfp.csv
python scripts/python/tfp_identity.py           # → data/tfp_identity_table.csv, lp_real_nominal.csv
python scripts/python/sylos_table.py            # → data/sylos_table.csv, sylos_means.csv
python scripts/python/scm_greece.py data/ameco_scm_panel.csv data/scm_out   # ~3 min
python scripts/python/bai_perron.py data/bai_perron_series7.csv
python scripts/python/fetch_comtrade.py <CHIAVE_COMTRADE> data/comtrade_sitc3_raw.csv   # ~4 min, 174 chiamate
python scripts/python/lall_classify.py data/comtrade_sitc3_raw.csv data/lall
Rscript scripts/R/did_callaway_santanna.R       # dalla radice del repo; richiede did, lmtest, sandwich; legge data/did_eurostat_REAL.csv
```

AMECO: vintage Autumn Forecast 2025 via `https://api.db.nomics.world/v22/series/AMECO/<CODICE>/ITA.1.0.0.0.<CODICE>`. Eurostat: `nama_10_a64` (GEO=IT, unit=CP_MEUR, na_item=D1,B1G). I risultati cross-software Python/R sono "sostanzialmente coincidenti, con differenze solo di arrotondamento".

## Convenzioni

- Ogni versione del paper ha suffisso parlante (`v22_TFP_CAMBRIDGE`) e MD5 registrato in `docs/HANDOFF.md`; chi recensisce dichiara quale versione ha letto.
- Le decisioni teoriche e di filtro critico sono dell'autore. Gli LLM (Claude, ChatGPT, Kimi, DeepSeek) hanno ruoli definiti in `docs/COLLABORATION.md`.
- Repository pubblico dal 9/11/2026 per consentire la lettura ai reviewer. Licenza e DOI (Zenodo) da definire alla pubblicazione.
