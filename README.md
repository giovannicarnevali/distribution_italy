# distribution_italy

**Le lotte di classe in Italia. Fasi del declino italiano 1980–2024**
Working paper di Giovanni Battista Carnevali. Versione corrente: **v24e_RENDITE** (11 novembre 2026, 106 pagine).

Lettura econometrica del declino italiano come sequenza di regimi di conflitto distributivo (profit squeeze fordista 1970-79; restaurazione istituzionale post-Maastricht 1992-2007; finanziarizzazione ed export-led 2008-2024), in un quadro Marx-Goodwin-Sylos Labini-Aglietta-Godley-Graziani-Bellofiore. Dati AMECO 1960-2024, Eurostat NACE A64 1995-2024, OCSE EO/MSTI, World Bank. Metodi: PELT, Quandt-Andrews, Chow narrativi HAC + Holm-Bonferroni, Bai-Perron (strucchange e replica Python), Synthetic Control (con estensione alla Grecia), DiD staggered (TWFE + Callaway-Sant'Anna), cointegrazione/VECM, decomposizione di Kalecki, identità distributiva della TFP (Felipe-McCombie), equazione di produttività di Sylos Labini, composizione tecnologica dell'export (UN Comtrade, tassonomia di Lall).

## Struttura del repository

```
README.md                 questo file
CLAUDE.md                 istruzioni per Claude (Code / chat) all'apertura del repo
docs/
  ISTRUZIONI_PROGETTO_CHATGPT.md   istruzioni da incollare nel progetto ChatGPT (valide anche per Kimi/DeepSeek)
  CONTEXT.md              conoscenza stabile del progetto: tesi, struttura, risultati, dati, decisioni chiuse
  HANDOFF.md              stato corrente, pendenti, prompt di apertura (si aggiorna a ogni sessione)
  SMONTAGGIO.md           tabella di smontaggio in 4 paper tematici e piano di revisione a pezzi (30 sedute)
  COLLABORATION.md        protocollo multi-LLM: ruoli, formato delle review, triage
paper/
  working_paper_v24e_RENDITE.docx / .pdf
  archive/                          versioni precedenti (v22-v24d)
data/
  README.md                         catalogo di ogni file: fonte, URL, data di download, uso nel paper
  raw/ameco/ (34 file)              una serie AMECO per file, via DBnomics
  raw/oecd_eo/ (6 file)             una serie OCSE Economic Outlook per file
  raw/eurostat/ (5 file)            nama_10_a64 D1/B1G, nama_10_a64_p5 P51G, nasa_10_nf_tr B9, dump completo nama_10_a64
  raw/worldbank/ (33 file)          un JSON per paese e indicatore (R&D, PIL pro capite, high-tech export)
  raw/pwt/                          Penn World Table 10.0/10.01 originali
  raw/comtrade/ (6 file)            export SITC3 per paese, UN Comtrade
  derived/                          tutto ciò che è calcolato, con lo script che lo genera (vedi data/README.md)
  preliminary/*_SIMULATO.csv        serie illustrative delle versioni preliminari: NON dati reali
scripts/
  python/fetch_raw.py               scarica TUTTI i dati grezzi AMECO/OCSE/Eurostat, un file per dataset, in data/raw/
  python/fetch_ameco_tfp.py         scarica le 14 serie AMECO dell'identità TFP in un unico file derived
  python/tfp_identity.py            identità distributiva della TFP (pesi Törnqvist)
  python/sylos_table.py             equazione di Sylos Labini, OLS HAC(3)
  python/scm_greece.py              Synthetic Control baseline + Grecia, placebo in-space, leave-one-out
  python/bai_perron.py              Bai-Perron (DP, BIC) con specificazione 'mean' e 'trend'
  python/fetch_comtrade.py          scarica export SITC3 da UN Comtrade (serve chiave gratuita)
  python/lall_classify.py           tassonomia di Lall e quote per periodo
  python/privatizzate_surplus.py    surplus operativo lordo (B1G−D1−D29X39), investimenti/surplus, VA reale e deflatore per branca (Tabella 6bis.1)
  python/setup_cell_robustness.py
  R/did_callaway_santanna.R         DiD staggered (pacchetto did), event-study
  R/working_paper_robustness.R      Phillips-Ouliaris, Johansen, Bai-Perron  [sul PC dell'autore, da caricare]
  docx/build_v22.py … build_v24.py   modifiche testuali applicate a ogni versione del DOCX (tracciabilità)
notebooks/
  Marx_Schumpeter_Italia_v12_robustness.ipynb   notebook finale (le versioni v2-v11 restano sul PC dell'autore)
```

## Replicare

```bash
pip install pandas numpy scipy statsmodels requests
python scripts/python/fetch_raw.py              # → data/raw/{ameco,oecd_eo,eurostat}/ (un file per dataset)
python scripts/python/fetch_ameco_tfp.py        # → data/derived/derived/ameco_tfp.csv
python scripts/python/tfp_identity.py           # → data/derived/tfp_identity_table.csv, lp_real_nominal.csv
python scripts/python/sylos_table.py            # → data/derived/sylos_table.csv, sylos_means.csv
python scripts/python/scm_greece.py data/derived/ameco_scm_panel.csv data/derived/scm_out   # ~3 min
python scripts/python/bai_perron.py data/derived/bai_perron_series7.csv
python scripts/python/fetch_comtrade.py <CHIAVE_COMTRADE> data/raw/comtrade/comtrade_sitc3_raw.csv   # poi un file per paese   # ~4 min, 174 chiamate
python scripts/python/lall_classify.py "data/raw/comtrade/COMTRADE_X_SITC3_*.csv" data/derived/lall
Rscript scripts/R/did_callaway_santanna.R       # dalla radice del repo; richiede did, lmtest, sandwich; legge data/derived/did_eurostat_REAL.csv
```

AMECO: vintage Autumn Forecast 2025 via `https://api.db.nomics.world/v22/series/AMECO/<CODICE>/ITA.1.0.0.0.<CODICE>`. Eurostat: `nama_10_a64` (GEO=IT, unit=CP_MEUR, na_item=D1,B1G). I risultati cross-software Python/R sono "sostanzialmente coincidenti, con differenze solo di arrotondamento".

## Convenzioni

- Ogni versione del paper ha suffisso parlante (`v22_TFP_CAMBRIDGE`) e MD5 registrato in `docs/HANDOFF.md`; chi recensisce dichiara quale versione ha letto.
- Le decisioni teoriche e di filtro critico sono dell'autore. Gli LLM (Claude, ChatGPT, Kimi, DeepSeek) hanno ruoli definiti in `docs/COLLABORATION.md`.
- Repository pubblico dal 9/11/2026 per consentire la lettura ai reviewer. Licenza e DOI (Zenodo) da definire alla pubblicazione.
