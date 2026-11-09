# HANDOFF — stato corrente

Aggiornato: 9 novembre 2026 (v23b, dopo la review ChatGPT/Kimi sulla v23). Si legge dopo `CONTEXT.md`. Contiene solo ciò che cambia: versione, ultime modifiche, pendenti, prompt di apertura.

## 1. Versione corrente

| | |
|---|---|
| File | `paper/working_paper_v23b_REVIEWED.docx` / `.pdf` |
| Pagine | 106 |
| MD5 | docx `b582170b5c228387b5cd8bbad6821cc7` · pdf `50906b29733541d7eea5acac42522889` |
| Base | v23_REVIEWED (106 pp, MD5 docx `4aea79aa20fc7d18814f6235de566a43`) e v22 (MD5 `c6070a8e…`), in `paper/archive/` |
| Repository | `https://github.com/giovannicarnevali/distribution_italy` — **reso pubblico dall'autore il 9/11** per farlo leggere ai reviewer; il paper in bozza è quindi scaricabile da chiunque |

Storia: v17 triangolazione → v18 replica R → v19 peer review → v20 Kalecki + IRAP → v21_REFEREE2 → v22 TFP/Cambridge → **v23 REVIEWED** (fusione del ramo di luglio + review ChatGPT e Kimi sulla v22).

## 2a. Cosa ha fatto la v23b (review ChatGPT/Kimi sulla v23)

Applicati: formulazioni Comtrade coerenti con la Tabella 5bis.1 (quasi doppia vs Germania, +50% vs Francia; high-tech terza più bassa dopo Portogallo e Spagna) in abstract IT/EN, §5bis.2, tabella 9.1; titoli SCM senza "causalità" (§8.6, tabella 9.1); ATT Callaway-Sant'Anna in punti percentuali ovunque (+2,3 pp [+0,3; +4,3]; TWFE staggered −15,1 pp); Figura 7.2 con copertura dichiarata (estero e nazionale 1960-2024, privato dal 1995); β del Goodwin = ore lavorate totali (NLHT) in definizioni e tabelle 3.1/8.1 (verificato sul notebook v9, cella 23); avvertenza in apertura di §6bis.2; Minsky come riferimento via Bellofiore-Halevi 2011; rinumerazione: Figura 5bis.2→5bis.1, 9.1→8.2, 8.7→8.3, 4.2bis.1→A.7.1, Tabella 9.2→9.1. Verificato: α−β = 2,325 non arrotondato (Tabella A.2), quindi 2,32 è corretto (Kimi C14 chiuso). Non applicati (fonti da autore): De Cecco "keynesismo criminale", Salvati 1981, Romagnoli 1980.

## 2. Cosa ha fatto la v23

Risposta alle due review esterne della v22 (ChatGPT, 10 rilievi; Kimi, 52 rilievi) e fusione del ramo di luglio. Tutto verificato sui dati prima di scrivere.

**Esecuzioni nuove**
1. **SCM con la Grecia eseguito davvero** (`scripts/python/scm_greece.py`): il risultato è negativo (gap −2,5, p = 0,222, fit peggiore). §8.6.1 riscritta come risultato negativo; abstract IT/EN e tabella 9.2 aggiornati. I numeri di comodo (−3,4, p 0,10) sono spariti.
2. **Bai-Perron riconciliato** (`scripts/python/bai_perron.py`): Python replica R per ω, r, CA/Y; il "0 break" di §5.5 era falso ed è stato rimosso; aggiunta la specificazione a sola intercetta (ω: 1984, 1993). Tabella 8.2 armonizzata.
3. **§5bis.2 con dati UN Comtrade reali** (`fetch_comtrade.py`, `lall_classify.py`, tassonomia di Lall 2000, 6 paesi 1995-2023): nuova Tabella 5bis.1; figura e bullet su dati simulati eliminati; dichiarato nel testo che la versione precedente usava serie illustrative.
4. **§4.2 fase 2 corretta**: il REER si apprezza del 29% nel 1979-85 (non "−13%"); il recupero di r negli Ottanta passa per la discesa di ω dopo il 1984, non per il cambio reale. È una riformulazione sostantiva del canale Sylos per la fase 2: **l'autore deve rileggerla**.
5. Debito/PIL riallineato ad AMECO; CA/Y 2013-14; EUR/USD; spread 2011 intraday.

**Fusione del ramo di luglio**: Di Martino-Vasta (2017, Paolo e Michelangelo) ovunque; Modiano-Onado (2023, Pietro e Marco, sottotitolo corretto); Mortágua 2019; R&D Svezia/Germania/Spagna 2023; r 1992 8,1; scala mobile al protocollo 31/7/1992 in §1.1 e §5.1; UQND e UTSG in Tabella A.1; 23 voci bibliografiche aggiunte e bibliografia riordinata.

**Arrighi, opzione B applicata**: via da abstract, §1.2 (blocco di 6 paragrafi), tabelle 1.1-1.2, §7.3 (2 paragrafi), titoli 8.2/8.4, §9.1; resta la lettura di lungo periodo in §8.3 con Arrighi 1994 in bibliografia.

**Meccanici**: abstract 13/24; "divergenza nel regime di convergenza" al posto di "effetto Maastricht" (abstract IT/EN, §1.1bis, §8.6); ω fino al 67%; 1996-2007 0,3% ovunque; minimo (non picco) 51,4; Ferrovie non privatizzate (§6bis.1, 6bis.3); §6bis.1 come ipotesi sottoposta a test; T=30 e dataset dichiarato; t-stat −4,82; p Sylos 1993-2007 = 0,07 (t a 11 gdl); refusi C1-C9, C11-C12, C16-C17, C20-C23; meta-linguaggio di peer review rimosso dal corpo; acknowledgments riscritti (Kimi incluso, repository citato); A.4.1 riconciliata con §5.7 (r borderline); A.5 aggiornata; Osterwald-Lenum.

**Repository**: script DiD ora legge `data/did_eurostat_REAL.csv`; i tre CSV simulati spostati in `data/preliminary/` con suffisso `_SIMULATO`; nuovi dati e script in `data/` e `scripts/python/`.

## 3. Pendenti, in ordine di priorità

**Metodo di lavoro deciso dall'autore il 9/11**: revisione a pezzi secondo `docs/SMONTAGGIO.md` (30 pezzi, 4 destinazioni tematiche A/B/C/D), con rilettura integrale, riscrittura nel suo stile, verifica dei numeri sui CSV, interrogazione di ogni passaggio econometrico e verifica di ogni voce bibliografica. Nessuna sottomissione prima della fine del percorso.


| # | Pendente | Chi | Note |
|---|---|---|---|
| 1 | **Rilettura delle parti riscritte in v23**: §4.2 (REER/fase 2), §5.5(a), §5bis.2, §8.6.1, §6bis.1 | Autore | Sono riformulazioni, non refusi |
| 2 | **Verifica bibliografica integrale**: 16 voci v22 + 23 voci v23 scritte da Claude senza cataloghi; citati nel testo senza voce: Salvati (1981), Romagnoli (1980), De Cecco ("keynesismo criminale", §5) — fornire estremi o togliere; Gandolfo 2005 vs 2010 (Kimi C25) | Autore | Kimi ha verificato: Di Martino-Vasta 2017, Modiano-Onado 2023, Mortágua 2019, Modigliani-Padoa Schioppa 1978, Brancaccio-De Cristofaro 2025 |
| 3 | Verificare che le tesi attribuite a Di Martino-Vasta in §5bis.1 (monopsonio distrettuale, trappola salari compressi) siano nel volume | Autore | Kimi A1 |
| 4 | Riallineamenti SME: la lista del 1981-87 ora include marzo 1981 e il 1990 è trattato come riduzione della parità centrale; **segno e date da verificare su fonte** (Kimi C10) | Autore | Banca d'Italia, Bollettino 1992 |
| 5 | ~~Numerazione figure/tabelle~~ fatta in v23b; restano gli stili heading di §2.1-2.2 (Kimi C19) | Claude | Minore |
| 6 | Periodizzazione: Tabella 1.1 fase 4 "1995-2007" vs tabelle analitiche 1993-2007; 1987 in due fasi; 2008-13 senza fase (Kimi C15) | Autore decide | Scelta sostantiva |
| 7 | ~~α−β 2,32 vs 2,31~~ chiuso: valore non arrotondato 2,325 | — | — |
| 8 | §6bis.2 (DiD preliminare su dati simulati/aggregati) coesiste con 6bis.3-6bis.5 su Eurostat reale: dichiarato, ma valutare se eliminarlo | Autore | Kimi non lo ha contestato; semplificherebbe |
| 9 | Round di review sulla v23b (MD5 `b582170b…`) solo se l'autore lo ritiene utile: i round su v22 e v23 hanno già coperto numeri, fonti, coerenza | Reviewer | — |
| 10 | Paragrafo qualitativo grandi imprese (SIP/Telecom, Pirelli, Ferruzzi, FIAT, IRI): 4-5 fatti con date dall'autore | Autore | Proposta Kimi di giugno |
| 11 | Formalizzazione delle fasi (saldi settoriali + ciclo elettorale 1980-92; Lotka-Volterra profitti/quasi-rendite 1994-2007) | Autore | Idee dell'autore, non nel paper |
| 12 | Visibilità del repository (pubblico dal 9/11): decidere se tornare privato dopo le review | Autore | — |
| 13 | Zenodo/DOI, cover letter, sede | Autore | Bassa |

## 4. File sul PC dell'autore

Cartella `C:\Users\an_om\Documents\Claude\files08062026\`: `working_paper_data.csv`, `working_paper_robustness.R` (Phillips-Ouliaris, Johansen, Bai-Perron strucchange; non nel repo), `did_callaway_santanna.R`, `did_eurostat_sectors.csv` (= il file reale, rinominato), `did_event_study.png`, `did_results_CS.csv`, `did_att_gt.csv`, notebook v2-v11. R 4.6.0 con did, urca, strucchange, lmtest, vars, sandwich. Chiave Comtrade: rigenerarla dal portale (quella usata il 9/11 è passata in chat).

## 5. Prompt di apertura

**Per Claude (nuova chat)**
> Leggi docs/CONTEXT.md, docs/HANDOFF.md e docs/COLLABORATION.md nel repository distribution_italy. Lavoriamo su `paper/working_paper_v23b_REVIEWED.docx` (MD5 b582170b…, 106 pp): verifica di avere questa versione. Pendenti aperti in HANDOFF §3. Oggi: [compito].

**Per un reviewer (ChatGPT, Kimi, DeepSeek)**
> Sei peer reviewer esterno di questo working paper. Leggi prima docs/CONTEXT.md (§7 convenzioni, §8 decisioni chiuse, §9 trappole) e docs/COLLABORATION.md §3 per il formato. Il file è `paper/working_paper_v23b_REVIEWED.pdf`, 106 pagine, MD5 del docx b582170b5c228387b5cd8bbad6821cc7: conferma la versione citando il titolo di §8.6.1 e il secondo risultato dell'abstract. Compito: [es. verificare che le correzioni elencate in HANDOFF §2 siano state applicate e non abbiano introdotto nuove incoerenze; rileggere §4.2, §5.5, §5bis.2, §8.6.1]. Non riscrivere, non riaprire le decisioni chiuse senza argomenti nuovi, segnala ciò che non puoi verificare.
