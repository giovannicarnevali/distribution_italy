# Dati

Regola: **un file per ogni dataset scaricato**, in `raw/<fonte>/`, mai modificato a mano. Tutto ciò che è calcolato sta in `derived/` con lo script che lo genera. I file in `preliminary/` sono serie illustrative delle versioni preliminari del paper: non sono dati reali e non vanno citati come fonte.

## raw/ameco/ — AMECO (DG ECFIN), vintage Autumn Forecast 2025, via DBnomics (`https://api.db.nomics.world/v22/series/AMECO/<CODE>/ITA.<suffisso>.<CODE>`), scaricati il 9/11/2026 con `scripts/python/fetch_raw.py`

Un file per serie, Italia 1960-2027 (2025-27 sono previsioni): `AMECO_<CODE>_ITA.csv` con colonne `series_code, series_name, period, value`.

| File | Serie | Uso nel paper |
|---|---|---|
| ALCD0 | quota salari aggiustata, % PIL a costo dei fattori | ω (tutto il paper) |
| UVGD, OVGD, PVGD | PIL a prezzi correnti, a prezzi 2020, deflatore | denominatori, LP, identità TFP |
| UWCD, UOGD, UQGD, UQND | redditi da lavoro dipendente; surplus lordo; surplus lordo e netto aggiustati per gli autonomi | r, r_gross, r_NETTO, Kalecki |
| UTVN, UTSG | imposte indirette nette; contributi sociali effettivi | identità TFP a costo dei fattori; gradino IRAP 1998 |
| NWTD, NETD, NETN, NLHT | dipendenti, occupati totali e nazionali, ore lavorate | LP, ŵ, β del Goodwin (NLHT), Sylos Labini |
| OKND, OIGT, PIGT, UIGT, UIGG | stock netto di capitale a prezzi 2020; investimenti reali e correnti; deflatore investimenti; investimenti pubblici | K_corrente, I/K, q, effetto Ricardo, Kalecki |
| UBCA, UBGS, UBLA, UXGS, UMGS | partite correnti; bilancia beni e servizi; net lending nazione; export; import | CA/Y, X/Y, saldi settoriali |
| UBLG, UBLGI, UDGG, USGP | net lending AP; interessi; debito lordo AP; risparmio privato | Kalecki (D), debito/PIL, proxy saldi |
| XUNRQ, QLCD, ZUTN | REER su CLUP (37 paesi), CLUP reale, disoccupazione | REER, SCM predictors |
| `AMECO_ALCD0_panel14.csv`, `AMECO_XUNRQ_panel14.csv`, `AMECO_ZUTN_panel14.csv` | stesse serie per ITA ESP FRA BEL NLD AUT PRT FIN GRC DEU IRL DNK SWE GBR | Synthetic Control (§8.6) |

## raw/oecd_eo/ — OCSE Economic Outlook (database EO), via DBnomics (`OECD/EO/ITA.<CODE>.A`), 9/11/2026

`OECD_EO_<CODE>_ITA.csv`: NLGQ (net lending AP, % PIL), NLGXQ (net lending primario), TYB (imposte dirette sulle imprese, euro), TYH (imposte dirette sulle famiglie), SSRG (contributi sociali ricevuti dalle AP), SRATIO (tasso di risparmio netto delle famiglie). Usati per innestare la serie del deficit 1970-94 su AMECO e per T_π e S_w nell'equazione di Kalecki (§4.3). Valori in euro, non in miliardi.

## raw/eurostat/ — Eurostat, API SDMX 2.1 (`https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/<dataset>/<key>?format=SDMX-CSV`)

| File | Dataset e filtro | Data | Uso |
|---|---|---|---|
| `ESTAT_nama_10_a64_D1_B1G_IT.csv` | nama_10_a64, A.CP_MEUR.<branche>.D1+B1G.IT | 9/11/2026 | wage share per branca D1/B1G (§6bis.3-6bis.5) |
| `ESTAT_nama_10_a64_D1_B1G_IT_wide_2026-04.csv` | stesso dataset, formato wide, scaricato ad aprile 2026 | 04/2026 | versione usata nelle prime stime Eurostat |
| `ESTAT_nama_10_a64_FULL_all_countries_2026-04.csv.gz` | nama_10_a64 completo, tutti i paesi (36 MB) — **file troncato** (il download di aprile si è interrotto: leggibile solo in parte) | 04/2026 | era usato per il confronto multi-paese del §6bis; da riscaricare se serve |
| `ESTAT_nama_10_a64_p5_P51G_IT.csv` | nama_10_a64_p5, A.CP_MEUR.<tutte le branche>.<asset10>.P51G.IT | 9/11/2026 | investimenti fissi lordi per branca (investment rate privatizzate, verifica di giugno) |
| `ESTAT_nama_10_a64_B1G_CLV10_IT.csv` | nama_10_a64, A.CLV10_MEUR.<branche>.B1G.IT | 10/11/2026 | valore aggiunto in volume per branca (Tabella 6bis.1) |
| `ESTAT_nama_10_a64_D29X39_IT.csv` | nama_10_a64, A.CP_MEUR.C+D+H+J61+K+TOTAL.D29X39.IT | 10/11/2026 | altre imposte meno contributi alla produzione, per il surplus operativo lordo per identità (Tabella 6bis.1) |
| `ESTAT_nama_10_a64_B2A3N_IT.csv` | nama_10_a64, A.CP_MEUR.D.B2A3N.IT | 10/11/2026 | surplus netto energia (controllo) |
| `ESTAT_nasa_10_nf_tr_B9_IT.csv` | nasa_10_nf_tr, A.CP_MEUR.PAID.B9.S1+S11+S12+S13+S14+S15+S14_S15+S2.IT | 9/11/2026 | saldi settoriali Cripps-Godley 1995-2024 (§7.3, Tabelle 7.1-7.2) |

Il file `nama_10_a64__custom_…csv` scaricato dall'autore dal Data Browser (stesso contenuto di D1/B1G) è sul suo PC.

## raw/worldbank/ — World Bank API (`https://api.worldbank.org/v2/country/<ISO>/indicator/<IND>?format=json`), aprile 2026

Un file JSON per paese e indicatore: `rd_<ISO>.json` = GB.XPD.RSDV.GD.ZS (R&D/PIL, 13 paesi); `gdp_<ISO>.json` = NY.GDP.PCAP.KD (PIL pro capite, 5 paesi); `trade_ht_<ISO>.json` e `wb_hightech_ita.json` = TX.VAL.TECH.MF.ZS (high-tech export % manifatturiero, 15 paesi). Usati in §4.2bis, §5bis.3, A.7.

## raw/pwt/ — Penn World Table 10.0 e 10.01 (Groningen, `https://www.rug.nl/ggdc/productivity/pwt/`), file Excel originali, aprile 2026

`pwt100.xlsx` (rtfpna, rgdpna, emp, avh, hc per 13 paesi OCSE 1996-2019) usato solo per confronto in §4.2bis e A.7.

## raw/comtrade/ — UN Comtrade, API v1 (`https://comtradeapi.un.org/data/v1/get/C/A/<S3|S4>`), 9/11/2026, `scripts/python/fetch_comtrade.py` (richiede chiave gratuita)

Un file per paese: `COMTRADE_X_SITC3_<ISO>_1995_2023.csv` — export verso il mondo (partner 0), flusso X, SITC Rev. 3 a 3 cifre fino al 2006 e Rev. 4 dal 2007 (colonna `cl`), valori in USD correnti. Paesi: ITA FRA DEU ESP PRT SWE. Nota: Comtrade usa il codice 381 per l'Italia.

## derived/ — file calcolati (script tra parentesi)

ameco_tfp.csv (fetch_ameco_tfp.py: 14 serie AMECO in un file, input di tfp_identity.py e sylos_table.py) · tfp_identity_table.csv, lp_real_nominal.csv (tfp_identity.py) · sylos_table.csv, sylos_means.csv (sylos_table.py) · kalecki_data_full.csv, kalecki_decomposition_robust.csv, kalecki_table_robust.csv, kalecki_table_v21.csv (notebook, §4.3) · omega_irap_corrected.csv, bai_perron_irap_check.csv (§5.5 IRAP) · bai_perron_series7.csv, bai_perron_two_specs.csv (bai_perron.py) · r_unit_root_full.csv, r_breakpoints.csv, r_results.csv (working_paper_robustness.R, sul PC dell'autore) · ameco_scm_panel.csv, scm_greece_results.csv, scm_simple_gap_*.csv, scm_leave_one_out.csv (scm_greece.py; notebook) · did_eurostat_REAL.csv (da nama_10_a64 D1/B1G; input di did_callaway_santanna.R), did_real_dataset.csv, did_real_results.csv · lall_shares.csv, lall_periods.csv (lall_classify.py sui file Comtrade) · privatizzate_surplus_investimenti.csv (privatizzate_surplus.py: Tabella 6bis.1) · wb_rd_panel.csv, wb_hightech_panel.csv, pwt_panel.csv, cross_section_rd_tfp.csv, cross_section_results.csv, panel_fe_full.csv, country_specific_rd_elasticity.csv (A.7) · eurostat_wage_share_panel_6countries.csv (§6bis confronto paesi) · specializzazione: vedi preliminary.

## preliminary/ — NON DATI REALI

`did_eurostat_sectors_SIMULATO.csv`, `did_privatizzazioni_SIMULATO.csv` (DiD preliminare, §6bis.2), `specializzazione_lockin_SIMULATO.csv` (vecchia §5bis.2, sostituita dai dati Comtrade). Conservati solo per tracciabilità.
