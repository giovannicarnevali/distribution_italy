# Smontaggio della v23b e piano di revisione a pezzi

Riferimento: `paper/working_paper_v24_RENDITE.pdf` (104 pp). Le pagine della tabella sono quelle della v23b: dal §6bis in poi scalano di circa 2 pagine nella v24.

Quattro destinazioni tematiche (non cronologiche — i pivot 1979-80, 1992-93, 2008-14 sono la tesi e devono stare nello stesso testo):

- **A — Paper madre**: periodizzazione e regimi del conflitto distributivo 1970-2024.
- **B — Privatizzazioni e quasi-rendite**: §6bis intero, risultato negativo del DiD, Torrini/Modiano-Onado.
- **C — Produttività, TFP e specializzazione**: critica cambridgiana, Sylos Labini, Comtrade/Lall, World Bank, A.7.
- **D — Export-led 2.0 e saldi settoriali**: Luxemburg, Cripps-Godley, 2014-24; da completare con il modello.

Legenda della colonna **Lavoro**: R = riscrivere nel tuo stile; N = verificare i numeri contro `data/`; E = passaggio econometrico/metodologico da interrogare; F = fonti e citazioni da verificare; T = tagliare o spostare. Il **pezzo** è l'unità di revisione: una seduta ciascuno, in ordine.

## 1. Tabella di smontaggio

| Pezzo | Sezioni (pp.) | Va in | Lavoro | Numeri da verificare (file in `data/`) | Domande econometriche da farmi | Fonti da verificare |
|---|---|---|---|---|---|---|
| 1 | Abstract IT/EN (1-7) | A (riscrivere alla fine, per ultimo) | R N | tutti i numeri dei 5 risultati: F=27, 13/24, ρ −0,545 [−0,714; −0,366], −16,54 pp / +2,3 pp, −3,51 e −2,5 (Grecia), identità TFP, Sylos 0,07→0,25, 8,1% high-tech | nessuna: deve solo coincidere con il corpo | — |
| 2 | §1.1 mappa delle fasi, Tabella 1.1 (8-10) | A | R N | ω 67% 1975, r 9,4→7,3, 8,1→9,4, debito 54→91 | perché 5 fasi narrative e 3 regimi distributivi: la risposta è in §8, ma va anticipata qui | Modiano-Onado 2023, Di Martino-Vasta 2017 (cit.) |
| 3 | §1.1bis Graziani (10-14) | A | R F | — | — | Graziani 1998; Bellofiore 2012a/b; Bellofiore-Garibaldo-Mortágua 2019; Brancaccio (5 voci); Saraceno (3); Mortágua in-text |
| 4 | §1.2 paradigmi teorici, Tabella 1.2 (14-19) | A (tagliare: le parti Luxemburg/Cripps-Godley passano a D) | R T | α−β 2,32 / −0,58 | Goodwin: β = ore lavorate NLHT, perché e con quale effetto sulla stima; Okishio; cosa resta di Aglietta dopo la rimozione di Arrighi | Aglietta 1976; Goodwin 1967; Gandolfo 2005 vs 2010 (C25); Luxemburg; Godley-Cripps 1983; Godley-Lavoie 2007 |
| 5 | §1.3-1.4 domande e struttura (19-20) | A | R | — | — | — |
| 6 | §2 dati e metodi (21-28) | A (il paragrafo sui metodi va sfoltito: Markov-switching e VECM in appendice) | R E | definizioni di r, ω, q, I/K, LP (Tabella A.1 e `data/raw/ameco`) | r = UQGD/(K+UWCD): perché il capitale variabile al denominatore; K_corrente = OKND·PIGT; UQGD vs UOGD; PELT vs Bai-Perron; trimming 0,15; HAC Newey-West a 3 ritardi; Holm vs Benjamini-Hochberg | Killick et al. 2012; Bai-Perron 1998/2003; Andrews 1993; Zeileis et al. 2002; Cameron et al. 2008 |
| 7 | §3 fase 1 1970-79 (29-35) | A | R N E F | Tabella 3.1 (α, β, α−β 2,325), Tabella 3.2/3.2bis (robustezza r: −2,10/−2,50; +1,18/+1,28; +1,03/+1,00; ρ −0,28/−0,27), ω 62,7→67,2, q 5,9→6,6→6,8 | stima dei parametri Goodwin su sub-sample (medie di tassi di crescita: è una stima o una calibrazione?); bootstrap CI delle correlazioni (quante repliche, a blocchi?) | Salvati 1981 **(voce mancante)**, Romagnoli 1980 **(mancante)**, Modigliani-Padoa Schioppa 1978, Tarantelli 1978, Sylos Labini 1972, Okishio 1961 |
| 8 | §4.1-4.2 fase 2 1980-87 (36-37) | A | **R** N F | **§4.2 riscritta in v23**: REER 80,6→104,1 (+29%), r 8,0→7,0→8,75, ω 64,2→58,5; debito 54,3→91,4; sette riallineamenti (C10, marzo 1981 aggiunto, 1990 parità centrale) | Quandt-Andrews 1986 per r e 1982 per REER: come leggere break che non coincidono con la narrativa | **De Cecco "keynesismo criminale" (voce mancante)**; date dei riallineamenti SME su fonte Banca d'Italia |
| 9 | §4.2bis TFP come identità (37-41) | **C** (in A resta un rinvio di 10 righe) | R E | Tabella identità (7 periodi; `derived/tfp_identity_table.csv`); LP 3,1/1,8/0,8/0,1; PWT −0,63 | l'identità TFP̂ ≡ ω·ŵ + (1−ω)·r̂: perché vale esattamente con pesi Törnqvist; cosa cambia a costo dei fattori; perché PWT dà −0,63 e noi −0,31 (ore, capitale umano) | Felipe-McCombie 2014/2020; Shaikh 1974; Rymes 1971; Pasinetti 1959/1981; Garegnani 1970; Harcourt 1972; Robinson 1953; Sraffa 1960; Halevi 2025; Gaddi-Garbellini-Oro 2025 (tutte scritte da Claude: controllare pagine) |
| 10 | §4.3 Kalecki (41-43) | A | R N E | Tabella 13 colonne (`derived/kalecki_*`): I/P 0,48→0,34, risparmio famiglie 22→11→4, deficit 6,7→10,4 | come è costruito D (innesto OCSE EO su AMECO 1995), T_π = TYB, perché C_π − S_w non è separabile; verifica che la tabella chiuda; unità (euro vs miliardi) | Kalecki 1971; OECD EO 2025 |
| 11 | §5.1-5.4 fase 3 e regime change (43-47) | A | R N F | scala mobile 31/7/1992, Ciampi-Giugni 23/7/1993, Maastricht in vigore 1/11/1993; ω 58,8→53,8; r 8,06→9,36; REER 112→83 | — | Salvati 2000; Ciocca 2007 |
| 12 | §5.5 Bai-Perron e Chow (47-50) | A | **R** N E | **§5.5(a) riscritta in v23**: break per 7 serie (`derived/bai_perron_two_specs.csv`); Tabella 5.2 Chow; 11 Holm / 17 BH standard; 13/24 HAC; IRAP δ 2,25/2,34/3,15 → 1994 | perché due specificazioni (intercetta+trend vs sola intercetta) danno 4 e 2 break; convenzione sulla data (ultimo anno del segmento); Holm su 21 vs 24 test; cosa significa "BIC non confrontabile tra serie" | Holm 1979 |
| 13 | §5.7 non-stazionarietà (50-51) | A | R E | ADF/KPSS (`derived/r_unit_root_full.csv`), PO Pu 4,82 / Pz 12,45, Johansen 21,95 vs 19,96 e 14,28 vs 15,67, β −0,30/−0,34, ρ(Δ) −0,74 | r borderline I(0)/I(1): conseguenze; perché la regressione in differenze è "prudenziale"; cosa perde (la relazione di livello) | Johansen 1991; Pesaran-Shin 1999; Pesaran-Shin-Smith 2001; Pfaff 2008 |
| 14 | §5bis lock-in (51-55) | **C** | **R** N F | **§5bis.2 riscritta in v23 su Comtrade**: Tabella 5bis.1 (`derived/lall_periods.csv`); World Bank 8,12 / 8,13 / 6,18 / 25,06 / 16,53 / 15,76 / 33,85 | tassonomia di Lall: cosa classifica e cosa no (prodotti, non imprese); perché quote sull'export manifatturiero e non RCA; Rev.3→Rev.4 | **Di Martino-Vasta 2017: verificare che le tesi attribuite (monopsonio distrettuale, trappola) siano nel volume, con pagine**; Lall 2000; Bagnasco 1977; Becattini 1979; Brusco 1986; Sforzi 1990 |
| 15 | §6.1-6.2 fase 4 (56-57) | A | R N | ω 58,8→53,8→51,4 (minimo 2000); r 8,06→9,74; LP 0,3 vs 2,0; X/Y 18,5→27,2 | — | — |
| 16 | §6.3-6.3.1 produttività e Sylos (57-60) | **C** (in A resta la tabella Sylos con 10 righe) | R N E F | Tabella Sylos 4 campioni (`derived/sylos_table.csv`); p 1993-2007 = 0,07 (t, 11 gdl); elasticità 0,07→0,25→0,43 | effetto Smith/Verdoorn vs effetto Ricardo; critica di Rowthorn e perché riportiamo 1−b; HAC(3) con n=15; endogeneità di g_Y | Sylos Labini 1984/1993; Verdoorn 1949 (pagine); Kaldor 1966; Rowthorn 1975; Pellegrino-Zingales 2017; Bugamelli et al. 2018; Saltari-Travaglini 2009 |
| 17 | §6bis.1-6bis.2 narrativa e Torrini (v24: 60-61) | **B** | **R** F | citazioni di Torrini con pagine (`docs/torrini_estratti.md`) | — | Modiano-Onado 2023 (citazioni testuali: pagine); Torrini 2005 pp. 3, 26, 28-30, 32, 34; Torrini 2016 p. 20 |
| 18 | §6bis.3-6bis.4 verifica ex post e "perché non un DiD" (v24: 61-63) | **B** | **R** N E | Tabella 6bis.1 (`derived/privatizzate_surplus_investimenti.csv`): energia 60→78 / 169→73; finanza 40→57 / 25→15; telecom 73→80→74 / 49→32→77; manifatt. 49→45 / 39→55; totale 39 | definizioni (B1G−D1)/B1G e P51G/(B1G−D1); perché H e non H49; caveat ciclo combinato ed energia 2022-24; perché il DiD era inadatto (quota salari = salari o rendita) | Callaway-Sant'Anna 2021; Goodman-Bacon 2021; de Chaisemartin-D'Haultfœuille 2020 (citati solo in 6bis.4) |
| 19 | §6bis.5 riformulazione (v24: 63-64) | **B** (sintesi di 15 righe in A, §8.2) | **R** | rinvii a Kalecki 0,48→0,34, break I/K 1992/2006/2015, Tabella 6bis.1 | la formulazione "innesto" è dell'autore (10/11): riscriverla nel suo stile | Bhaduri-Marglin 1990; Stockhammer 2004 |
| 20 | §7.1-7.2 storia 2008-24 (66-68) | A (sfoltire) / D | R N F | debito 119→135; CA/Y −3,2→+1,0→+1,8; spread 575 intraday; EUR/USD 1,33→1,11→1,13; interessi 5,4→3,4 | — | Blanchard-Leigh 2013; Saraceno 2017/2018/2020 |
| 21 | §7.3 Luxemburg e saldi settoriali, Tabelle 7.1-7.2, Figure 7.1-7.2 (68-71) | **D** (in A resta la Tabella 7.2 e 20 righe) | R N E | B9 per settore (`raw/eurostat/ESTAT_nasa_10_nf_tr_B9_IT.csv`): +6,51% vs proxy +2,29%; Figura 7.2 copertura 1960/1995; Movimprese (Figura 7.1) | identità Cripps-Godley: cosa dimostra e cosa no; perché la proxy AMECO (USGP−UIGT) sottostima; Movimprese: fonte e perimetro | Steindl 1952; Chen-Karabarbounis-Neiman 2017; Krippner 2005; Schneider-Buehn 2012 |
| 22 | §8.1 Goodwin come lente (72-74) | A | R E | α−β +2,32 / −0,58; autovalori; "regime sella" | Hopf per analogia, non dimostrata: dirlo una volta sola; cosa significa che α dipende da ω (rinvio a Sylos) | Gandolfo |
| 23 | §8.2-8.5 sintesi, pivot, contro-evidenze, Tabella 8.2 (74-78) | A | **R** | coerenza con §5.5 riscritta (riga Bai-Perron della Tabella 8.2) | il 1979 come break "politico-sindacale" che i dati vedono su q, I/K, REER ma non su ω: come formularlo | — |
| 24 | §8.6-8.6.1 SCM (78-82) | A | R N E | pesi 43,1/22,4/28,0/6,6 (notebook) vs 43,8/22,6/27,5/6,1 (replica); gap −3,51/−3,53; media 98-01 −5,4; p 0,125; LOO [−3,89; −3,26]; **Grecia: −2,48, RMSPE 1,64, rank 2/9, p 0,222** (`derived/scm_greece_results.csv`) | come sono scelti i pesi (distanza nei predictors standardizzati, non RMSPE annidato): dirlo; perché con 8-9 unità il placebo in-space ha poca risoluzione; perché la Grecia peggiora il fit; cosa direbbe un gsynth | Abadie-Gardeazabal 2003; Abadie-Diamond-Hainmueller 2010/2015; Xu 2017; Arkhangelsky et al. 2021 |
| 25 | §9.1-9.2 limiti e robustezza, Tabella 9.1 (82-88) | A (riscrivere dopo tutto il resto) | R N | ogni riga della Tabella 9.1 deve coincidere con il corpo | — | — |
| 26 | §9.3 ricerca futura, nota metodologica (88-90) | A | R | — | — | — |
| 27 | A.6 VECM bivariato, A.3-A.4 VECM a 8 variabili (91, 103-105) | A appendice (valutare se tenere A.4) | T E | Tabella A.4.1 vs §5.7 (riconciliate in v23); rango 5 asintotico | il VECM a 8 variabili con T=60 è un esercizio: tenerlo in appendice o in un file del repo? | Osterwald-Lenum 1992; Reinsel-Ahn 1992; Cheung-Lai 1993 |
| 28 | A.7 regressione R&D–TFP (92-93) | **C** appendice | T | +0,30/0,35 robustness WGI **ancora stimati**: eseguire o togliere | — | Coe-Helpman 1995; Romer 1990; Aghion-Howitt 1992; Gemmell et al. 2016 |
| 29 | Bibliografia (94-100) | tutti | **F** | — | — | 100 voci: 39 scritte da Claude senza cataloghi (16 in v22 + 23 in v23); verificare ciascuna su catalogo editoriale/DOI; 3 citate senza voce (Salvati 1981, Romagnoli 1980, De Cecco) |
| 30 | A.1-A.2, A.5 (101-102, 106) | A appendice | N | Tabella A.1 (26 serie) vs `data/raw/ameco/`; Tabella A.2 anni narrativi | — | — |

## 2. Ordine consigliato delle sedute

1. **Pezzi 6, 12, 13, 24** (metodi, Bai-Perron, non-stazionarietà, SCM): sono il cuore econometrico di A e il punto su cui un referee ti attacca per primo. Qui le domande da farmi sono le più importanti.
2. **Pezzi 7, 8, 10, 11, 15** (le fasi): numeri e narrativa, nel tuo stile.
3. **Pezzi 9, 14, 16** (il blocco C): decidi se restano in A in forma ridotta o escono.
4. **Pezzi 17, 18, 19** (il blocco B): idem, con la decisione su Torrini.
5. **Pezzi 20, 21** (D).
6. **Pezzi 2, 4, 22, 23, 25, 1** (introduzione, sintesi, limiti, abstract): per ultimi, perché dipendono da tutto il resto.
7. **Pezzo 29** (bibliografia): trasversale, una voce alla volta man mano che rileggi la sezione che la cita.

## 3. Cosa duplicare se i quattro paper diventano davvero quattro

- Dati e periodizzazione (Tabella 1.1 e §2.2): in ogni paper, in forma di una pagina + rinvio al paper madre.
- `data/` e `scripts/` restano un repository unico; ogni paper cita il tag di versione.
- Resta orfana solo la parte Markov-switching di §5.4 e A.3: o entra in A come robustezza del pivot 1993-94, o va in un file del repo.

## 4. Come usare questo file

Una seduta = un pezzo. Per ogni pezzo: (i) rileggi; (ii) riscrivi nel tuo stile i paragrafi che non ti suonano; (iii) apri il CSV indicato e controlla i numeri; (iv) fammi le domande della colonna E, una alla volta, e pretendi la risposta sui dati, non a parole; (v) verifica le voci F e segna ✔ qui accanto. Quando un pezzo è chiuso, lo marchi qui e io propago le modifiche al DOCX e a HANDOFF.
