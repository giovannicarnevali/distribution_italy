# HANDOFF — stato corrente

Aggiornato: 9 novembre 2026. Si legge dopo `CONTEXT.md`. Contiene solo ciò che cambia: versione, ultime modifiche, pendenti, prompt di apertura.

## 1. Versione corrente

| | |
|---|---|
| File | `working_paper_v22_TFP_CAMBRIDGE.docx` / `.pdf` |
| Pagine | 105 |
| MD5 | docx `c6070a8e329a43ef73f8cec37f993721` · pdf `dd3a28b00ea7e4a9c991e6d372a7c80c` |
| Base | v21_REFEREE2 (102 pp, MD5 `728fbe8b7e7f35e04107a568a06cb8f6`) |
| Repository | `https://github.com/giovannicarnevali/distribution_italy` (privato; popolato il 9/11 con paper v22, dati, script, notebook v12 e docs/) |

Storia recente: v17 triangolazione (§5.7) → v18 replica R → v19 peer review (A VECM in A.6; B §6bis.5 C-S + script R; C SCM con Grecia; D robustness R&D; E §5.5 doppio break) → v20 Kalecki + IRAP → v21 dieci correzioni ChatGPT → **v22 TFP/Cambridge**.

## 2. Cosa ha fatto la v22

Revisione della parte sulla TFP alla luce di *Tornare alla pianificazione* (critica di Pasinetti e di Cambridge alla funzione di produzione):

1. §4.2bis riscritta: "perché non usiamo la TFP"; nuova sottosezione "La TFP come identità distributiva" con tabella TFP̂ ≡ ω·ŵ + (1−ω)·r̂ su sette periodi (p. 40) e cautela pasinettiana.
2. Regressione cross-country R&D→TFP (con figura) spostata in **Appendice A.7** "per confronto", con avvertenza.
3. Nuova **§6.3.1 "L'equazione di produttività di Sylos Labini"** (p. 60): tabella su quattro campioni, elasticità dell'occupazione, scomparsa dell'effetto Ricardo post-1992.
4. Propagazione: abstract IT/EN (quinto risultato riscritto; "Penn World Tables (TFP)" tolta dalle fonti), §1.1bis, §5bis (tabella e 5bis.3), §6bis.2/6bis.3/6bis.6, §8.1, tabella 9.2 (due righe). Numeri di §6.3 allineati alla vintage AMECO Autumn 2025.
5. Sedici voci bibliografiche aggiunte (elenco in CONTEXT §9) — **da verificare**.
6. Non importata la "produttività nominale" del libro (decisione chiusa, CONTEXT §8.9).

File di replica prodotti: `ameco_tfp.csv`, `tfp_identity_table.csv`, `lp_real_nominal.csv`, `sylos_table.csv`, `sylos_means.csv`, `fetch_ameco_tfp.py`, `tfp_identity.py`, `sylos_table.py`.

## 3. Pendenti, in ordine di priorità

| # | Pendente | Chi | Note |
|---|---|---|---|
| 1 | **Abstract IT/EN dicono ancora "11 su 21 test di Chow sopravvivono"** mentre la cifra canonica è 13/24 HAC (CONTEXT §8.2); §5.7 e §9.2 sono coerenti, l'abstract no | Claude | Rilevato il 9/11 preparando questo file; correzione meccanica, non ancora applicata |
| 2 | Verifica delle 16 voci bibliografiche aggiunte in v22 | Autore (o reviewer con accesso a fonti) | Titoli/pagine scritti a memoria |
| 3 | Rilettura di §4.2bis, §6.3.1, A.7 e coerenza con il libro Punto Rosso co-firmato dall'autore | Autore | In particolare: il sottoperiodo Sylos 1993-2007 ha n=15, R²=0,24, presentato come "canale fermo per mancanza di input" |
| 4 | Revisione "referee 2" pagina per pagina della v22 (numeri abstract vs corpo, date, fonti) | ChatGPT o Kimi | Formato in COLLABORATION §3; dichiarare MD5 letto |
| 5 | ~~Caricare paper, dati, script, docs nel repository~~ fatto il 9/11 (commit iniziale con notebook v12) | — | `working_paper_robustness.R` e i notebook v2-v11 restano sul PC dell'autore |
| 6 | Verifica residua di voci bibliografiche LLM-generated: Brancaccio-De Cristofaro 2025, voci Bellofiore complete | Autore | Di Martino-Vasta e Modiano-Onado già chiuse |
| 7 | Numeri "stimati" ancora nel testo: SCM con Grecia (−3,4, §8.6.1), robustness R&D (+0,30/0,35) | Autore decide | Eseguire davvero le stime o lasciarli dichiarati provvisori |
| 8 | Paragrafo qualitativo sulle grandi imprese scomparse (SIP/Telecom, Pirelli, Ferruzzi, FIAT, IRI): servono 4-5 fatti con date forniti dall'autore | Autore | Proposta Kimi; gli LLM sbagliano le date d'impresa |
| 9 | Cifre "ω cala di X pp" in §5.2 e §8 da rileggere al netto di 1,5-2 pp IRAP | Claude | Dopo decisione dell'autore su come trattarle |
| 10 | Test settoriale profit share (B2G/B1G) vs investment rate (P51G/B1G) su Eurostat per le branche privatizzate | rinviato | Non risolve l'identificazione (CONTEXT §8.5); eventuale in revisione successiva |
| 11 | Formalizzazione delle fasi (modello saldi settoriali + ciclo elettorale per il 1980-92; Lotka-Volterra "profitti che si mangiano i salari senza reinvestimento" per il 1994-2007) | Autore | Idee dell'autore, non ancora nel paper; da discutere se entrano in questo paper o in uno successivo |
| 12 | Zenodo/DOI, cover letter, scelta della sede | Autore | Bassa priorità |

## 4. File sul PC dell'autore

Cartella `C:\Users\an_om\Documents\Claude\files08062026\`: `working_paper_data.csv` (1960-2024, 17 colonne), `working_paper_robustness.R` (Phillips-Ouliaris, Johansen, Bai-Perron; eseguito), `did_callaway_santanna.R` (eseguito), `did_eurostat_sectors.csv` (= `did_eurostat_REAL.csv` rinominato; Eurostat NACE A64 reale), `did_event_study.png`, `did_results_CS.csv`, `did_att_gt.csv`. R 4.6.0 con did, urca, strucchange, lmtest, vars, sandwich.

## 5. Prompt di apertura

**Per Claude (nuova chat)**
> Leggi CONTEXT.md, HANDOFF.md e COLLABORATION.md. Lavoriamo su `working_paper_v22_TFP_CAMBRIDGE.docx` (MD5 c6070a8e…, 105 pp): verifica di avere questa versione. Il primo pendente è la correzione 11/21 → 13/24 nell'abstract. Poi [compito del giorno].

**Per un reviewer (ChatGPT, Kimi, DeepSeek)**
> Sei peer reviewer esterno di questo working paper. Leggi prima CONTEXT.md (in particolare §7 convenzioni, §8 decisioni chiuse, §9 trappole) e COLLABORATION.md §3 per il formato. Il file da leggere è `working_paper_v22_TFP_CAMBRIDGE.pdf`, 105 pagine: conferma di avere questa versione citando il titolo di §6.3.1 e il quinto risultato dell'abstract. Compito: [es. revisione pagina per pagina delle sezioni nuove §4.2bis, §6.3.1, A.7 e della loro coerenza con abstract, §8 e tabella 9.2]. Non riscrivere, non proporre riaperture delle decisioni chiuse senza argomenti nuovi, segnala ciò che non puoi verificare.
