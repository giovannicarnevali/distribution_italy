# CONTEXT — conoscenza stabile del progetto

Da leggere per intero prima di qualunque intervento sul paper. Contiene ciò che non cambia da una sessione all'altra: tesi, struttura, risultati con i numeri, fonti, convenzioni, decisioni chiuse. Lo stato corrente e i pendenti sono in `HANDOFF.md`; i ruoli degli LLM in `COLLABORATION.md`.

**Storia dei rami (9/11/2026).** Da giugno a novembre il paper ha vissuto in due rami non fusi: uno (luglio, chat parallela) con 44 correzioni meccaniche e un §6bis che usava Torrini come validazione esterna; l'altro (questa linea: v20 Kalecki/IRAP → v21 → v22 TFP/Cambridge) con §6bis riscritto su Callaway-Sant'Anna e quasi-rendite. Le review di ChatGPT e Kimi sulla v22 hanno fatto emergere i sintomi (citazioni mai corrette). La **v23** fonde i due rami: le correzioni di luglio sono state riapplicate dall'elenco, il §6bis è quello della linea v22. Le decisioni di luglio su Torrini/TFP ed Energia sono superate (vedi §8).

## 1. Il lavoro

- **Autore unico**: Giovanni Battista Carnevali. Economista; co-autore di *Tornare alla pianificazione. Politiche industriali dopo la globalizzazione* (Carnevali, Cucignatto, Esposito, Gaddi, Garbellini, Halevi, Lampa, Oro, Polidori; Punto Rosso 2025), da cui il paper riprende la critica cambridgiana alla funzione di produzione (cap. 1 Gaddi-Garbellini-Oro; cap. 11 Halevi).
- **Titolo**: *Le lotte di classe in Italia. Fasi del declino italiano 1980–2024*. Lingua: italiano (abstract anche in inglese).
- **Natura**: working paper, lettura storica quantitativa fondata sulla **convergenza di metodi multipli** (triangolazione), non dimostrazione causale univoca. Questo framing è una scelta deliberata e va difeso, non "rafforzato" con pretese causali.
- **Stato**: in peer review simulata (ChatGPT, Kimi, DeepSeek), verdetto "Accept with minor revisions"; destinazione da decidere (Stato e Mercato, IEJ, Moneta e Credito, collana working paper).

## 2. Tesi

Il declino italiano è una sequenza di **tre regimi di conflitto distributivo**, mediati da istituzioni salariali, vincoli macroeconomici e finanziarizzazione:

1. **1970–1979, profit squeeze fordista**: piena occupazione e forza sindacale; ω (quota salari aggiustata) sale fino al 67%, r (saggio di profitto lordo aggiustato) crolla. Meccanismo Goodwin attivo.
2. **1980–1992, compromesso al ribasso** (fasi 2-3 del paper): recupero dei profitti via leve eterodosse — svalutazioni nello SME, disavanzo pubblico (per tre quarti interessi sul debito), imprese pubbliche. Stallo del conflitto redistributivo che prelude alla rotta del 1992. 1979-80 è break politico-sindacale (fine dell'area di governo PCI, ingresso nello SME, marcia dei 40.000).
3. **1992–2007, restaurazione istituzionale**: fine della scala mobile (protocollo 31 luglio 1992), Ciampi-Giugni (23 luglio 1993, nuovo assetto contrattuale), Maastricht (firmato 1992, in vigore 1° novembre 1993), privatizzazioni. Compressione salariale strutturale, recupero di r **non reinvestito**: quasi-rendite (Modiano-Onado 2023; Torrini 2005, 2016), meccanismo Goodwin spento, crescita labour-intensive, produttività ferma.
4. **2008–2024, finanziarizzazione ed export-led 2.0**: crisi 2008-13 e cura Monti ammazzano la domanda interna; dal 2014 S>I, corporate saving glut, surplus estero (mai oltre due punti di PIL), recuperi ciclici di ω ma r in caduta per insufficiente reinvestimento. Pattern Luxemburg.

Fil rouge interpretativo (parole dell'autore): meccanismo fordista → piena occupazione e lotte → crisi di accumulazione; compromesso keynesiano al ribasso anni Ottanta; break 1992 (il deficit fa saltare la lira nella banda larga, salta la scala mobile, salta il compromesso); nuovo regime 1994-2007 in cui i profitti si mangiano i salari ma non vengono reinvestiti in crescita bensì in quasi-rendite; 2008-19 crisi dei debiti sovrani, Monti, export-led.

Riferimenti teorici: Marx, Goodwin (1967), Sylos Labini (1972, 1984, 1993), Aglietta e la regolazione, Godley (saldi settoriali), Graziani (cornice storica, §1.1bis), Bellofiore, Kalecki (equazione dei profitti), Luxemburg (realizzazione esterna), Bhaduri-Marglin 1990 e Stockhammer 2004 (profitti senza investimenti), Pasinetti / Felipe-McCombie / Shaikh (critica della funzione di produzione). Arrighi: solo lente storico-narrativa in §8.2-8.4, fuori dalla bibliografia come meccanismo.

## 3. Struttura del paper (v22)

Abstract IT/EN · 1 Introduzione e tesi (1.1 cinque fasi; 1.1bis Graziani; 1.2 paradigmi; 1.3 domande; 1.4 struttura) · 2 Dati e metodi (2.1 fonti; 2.2 variabili; 2.3 metodi) · 3 Fase 1 1970-79 (3.4 robustezza di r a definizioni alternative) · 4 Fase 2 1980-87 (4.2bis R&D, produttività e distribuzione: perché non usiamo la TFP; 4.3 equazione dei profitti di Kalecki) · 5 Fase 3 1987-92 e regime change (5.2 break 1992-94; 5.3 pivot in prospettiva comparata; 5.4 puzzle di politica economica; 5.5 Bai-Perron e Chow narrativi, controllo IRAP; 5.7 non-stazionarietà, cointegrazione, differenze) · 5bis Lock-in nella specializzazione (Di Martino-Vasta; 5bis.2 UN Comtrade con tassonomia di Lall, Tabella 5bis.1; 5bis.3 World Bank high-tech export) · 6 Fase 4 1995-2007 (6.3 puzzle della produttività; 6.3.1 equazione di Sylos Labini) · 6bis Privatizzazioni, rendite e investimenti (6bis.2 Torrini; 6bis.3 verifica ex post Eurostat, Tabella 6bis.1; 6bis.4 perché non un DiD; 6bis.5 riformulazione) · 7 Crisi 2008-14 e fase 5 2014-24 (7.3 pattern Luxemburg) · 8 Sintesi: tre regimi (8.1 Goodwin come lente; 8.5 contro-evidenze; 8.6 SCM; 8.6.1 donor pool allargato alla Grecia: risultato negativo) · 9 Limiti, robustezza (tabella 9.1 "rivedibilità dei risultati"), ricerca futura · A.6 VECM (r, ω) esplorativo · A.7 regressione cross-country R&D–TFP (solo per confronto) · Bibliografia · Appendice metodologica A.1-A.5.

## 4. Variabili (AMECO, Italia)

- ω = ALCD0/100 (quota salari aggiustata per gli autonomi; l'Italia ha ~23% di autonomi vs 14% UE, l'aggiustamento è sostanziale).
- r = UQGD / (K_corrente + UWCD), K_corrente = OKND × PIGT/100. Varianti: r′, r_NETTO = UQND/(K+UWCD), r_NETTO_strict = UQND/K, r_gross (non aggiustato: la correlazione con ω non regge).
- q = K_corrente/UWCD; I/K = UIGT/K_corrente; LP = OVGD/NETD; REER XUNRQ; ULC reale QLCD; CA/Y = UBCA/UVGD; X/Y = UXGS/UVGD.
- Saldi settoriali Cripps-Godley da Eurostat nasa_10_nf_tr (B9 per S11+S12+S14+S15, S13, S1), 1995-2024.
- Kalecki: P − T_π = I + D + (X−M) + C_π − S_w, con D = net borrowing delle AP (OCSE EO NLGQ/NLGXQ 1970-94 innestato su AMECO UBLG/UBLGI dal 1995), T_π = OCSE TYB (in euro, dividere per 1e9), risparmio netto famiglie OCSE SRATIO. Identità PIL = UWCD+UOGD+UTVN esatta dal 1995, entro 1 pp dal 1970; anni Sessanta esclusi.
- Identità TFP: Y a costo dei fattori = (UVGD − UTVN)/PVGD; ω aggiustata al costo dei fattori; w = ω·Y/L, r = (1−ω)·Y/K; residuo di Solow con pesi Törnqvist; scarto numerico massimo 2,9e-5.
- Sylos Labini: g_LP = a + b·g_Y + c·(ŵ − p̂_I)₋₁, con ŵ = crescita UWCD/NWTD, p̂_I = crescita PIGT; OLS HAC(3); elasticità occupazione/prodotto = 1 − b, riportata per rispondere a Rowthorn (1975).

## 5. Risultati principali (numeri da preservare)

Nel modello di Goodwin β è la crescita delle ore lavorate totali (AMECO NLHT), usata come proxy della forza lavoro; α−β = 2,325 nel 1970-80 (2,32 arrotondato). L'ATT di Callaway-Sant'Anna va sempre espresso in punti percentuali (+2,3 pp), come il TWFE.

| Risultato | Valore |
|---|---|
| Break ω 1992-93 (Chow narrativo) | F = 27, sopravvive Holm-Bonferroni |
| Chow narrativi HAC Newey-West + Holm | **13 su 24** significativi (versione standard preliminare: 11/21) — 13/24 è la cifra canonica |
| Bai-Perron (intercetta + trend, BIC, h=0,15, max 5) | ω 1970, 1983, 1997, 2008 (il terzo → **1994** con correzione IRAP, δ = 2,25/2,34/3,15 pp); r 1970, 1983, 2000, 2011; CA/Y 1992, 2011; REER 1972, 1981, 1992, 2008; X/Y 1976, 1992, 2008. Python (`bai_perron.py`) = R strucchange per ω, r, CA/Y. **Sola intercetta**: ω 1984, 1993. Il vecchio "0 break per tutte le variabili" (§5.5 fino alla v22) era un residuo errato, rimosso |
| ρ(r, ω) 1992-2024 | −0,545 [−0,714; −0,366]; r_NETTO −0,276 [−0,524; −0,067]; r_gross −0,205 (IC include 0) |
| Δr = α + β·Δω (HAC) | β = −0,30 (1992-2024, p<0,001); −0,34 (1961-2024); ρ(Δr,Δω) = −0,74 |
| Non-stazionarietà | r, ω, I/K, REER compatibili con I(1); r borderline I(0)/I(1) (ADF p=0,057, KPSS non rigetta) — trattato a parte; cointegrazione r-ω non univoca (Phillips-Ouliaris non rigetta; Johansen ambiguo trace vs max-eigen) |
| SCM Maastricht su ω | gap medio post-1992 −3,51 pp; in-space placebo p = 0,125; leave-one-out [−3,89; −3,26]; "divergenza nel regime di convergenza post-1992", suggestivo non conclusivo |
| SCM donor pool + Grecia (§8.6.1, eseguito in v23) | gap −2,48; RMSPE pre 1,64 (peggiora); pesi ESP 42,6 / PRT 19,4 / FIN 22,1 / GRC 16,0; Italia rank 2/9 (superata dalla Spagna), **p = 0,222**; LOO [−3,53; −2,48]. Replica baseline con lo stesso codice: pesi 43,8/22,6/27,5/6,1, gap −3,53, p 0,125 |
| Privatizzazioni (Eurostat per branca 1995-2024, v24) | quota profitti / surplus reinvestito / VA reale per periodo: energia 60→78 / 169→73 / in calo; finanza 40→57 / 25→15; telecom 73→80→74 / 49→32→77, peso sul VA 1,9→0,8; trasporti 45→52→48 / 74→63; **manifatturiero 49→45 / 39→55**; totale 58→56 / 39→39. Attesa di Torrini (espansione) non realizzata; Modiano-Onado confermata |
| DiD privatizzazioni (fino alla v23b, eliminato in v24) | TWFE −16,54 pp vs Callaway-Sant'Anna +2,3 pp [+0,3; +4,3], pre-trend non piatti: non identificato; e la quota salari per branca non distingue salari compressi da rendita. Resta solo in 6bis.4 come esercizio scartato; codice nel repo |
| Kalecki | investimento privato/surplus operativo lordo 0,48 (anni Settanta) → 0,34 (post-1993); risparmio netto famiglie 22% → 11% → 4%; fonte esterna di realizzazione: deficit pubblico anni Ottanta, riduzione del risparmio delle famiglie dal 1993, estero dal 2014 |
| Identità TFP (medie annue %) | 1970-79: 2,36 = 2,51 + (−0,16) [ŵ 3,63; r̂ −0,50; ω 69,4] · 1980-92: 0,47 = 0,48 − 0,01 · **1993-2007: 0,10 = 0,00 + 0,10** [ŵ 0,00; r̂ 0,27] · 2008-13: −1,30 = −0,32 − 0,98 · 2014-24: 0,46 = −0,16 + 0,62 [ŵ −0,27; r̂ 1,55] · 1996-2019: −0,31 (PWT: −0,63) |
| LP reale (medie annue %) | 1970-79 3,1; 1980-89 1,8; 1993-2007 0,8; 2008-24 0,1. LP nominale per occupato 1993-2007 +3,7 (deflatore 2,9) |
| Sylos Labini | 1961-2024 (n=63): b_Y 0,84 (0,04), Ricardo +0,149 (0,041) p<0,001, elast. occ. 0,16, R² 0,88 · 1961-92: 0,93, **+0,126 p<0,001**, 0,07 · 1993-2024: 0,745, −0,067 p=0,47, **0,255** · 1993-2007 (n=15): 0,57, +0,178 p=0,054, 0,43, R² 0,24. Medie (ŵ−p̂_I): 2,0 / 1,1 / 0,3 / −0,5 / 0,2 |
| R&D e specializzazione | R&D/PIL 1,4% nel 2023 (Svezia 3,6, Germania 3,1, Spagna 1,5; World Bank); high-tech export 8,1% del manifatturiero 2015-22 (World Bank), fra i più bassi OCSE, pari alla Spagna (8,13), sopra il Portogallo (6,2). **Comtrade/Lall (v23)**: low-tech Italia 33,5% (1995-99) → 26,9% (2015-23) contro DEU 13,7, FRA 17,1, PRT 28,1; high-tech 10,5 → 13,0 (DEU 18,1→23,0; ESP 12,8; PRT 9,0); medium-tech fermo 41 (DEU 49); risorse naturali 14,6 → 18,7 |
| Fase 2 (§4.2, corretto in v23) | REER (XUNRQ) **si apprezza** del 29% 1979-85 (80,6 → 104,1): le svalutazioni nominali SME non diventano deprezzamento reale. r 8,0 (1979) → 7,0 (1983) → 8,75 (1989); ω 64,2 (1983) → 58,5 (1989). Il recupero di r negli Ottanta passa per ω, non per il cambio reale |
| Debito/PIL (AMECO UDGG/UVGD) | 54,3 (1980), 91,4 (1990), 118,8 (2010), 134,8 (2014) |
| LP reale, finestre canoniche | 1970-79 3,1; 1980-89 1,8; 1986-95 2,0; 1993-2007 0,8; 1996-2007 0,3; 2014-24 0,1 |

Lettura: ciò che la letteratura mainstream chiama "stagnazione della TFP" post-1993 è, per identità, la stagnazione del salario reale, e il suo "recupero" post-2014 è solo r̂ — il paper lo mostra per smontare la misura, non la adotta. La spiegazione positiva della produttività ferma è nell'equazione di Sylos Labini: dopo il 1992 l'effetto Ricardo scompare e la crescita diventa labour-intensive; **la compressione salariale non è la risposta alla produttività ferma, ne è una causa**.

## 6. Fonti e strumenti

- **AMECO** via DBnomics (`https://api.db.nomics.world/v22/series/AMECO/<CODE>/ITA.1.0.0.0.<CODE>`), vintage Autumn Forecast 2025. Interfaccia ufficiale: `https://dashboard.tech.ec.europa.eu/qs_digit_dashboard_mt/public/sense/app/667e9fba-eea7-4d17-abf0-ef20f6994336`.
- **Eurostat**: `nama_10_a64` (D1, B1G; floor 1995 — vincolo strutturale, non colmabile), `nama_10_a64_p5` (P51G), `nasa_10_nf_tr` (B9).
- **OCSE**: Economic Outlook (NLGQ, NLGXQ, TYB, SRATIO), MSTI (GERD/GDP, BERD).
- **World Bank**: R&D/GDP (GB.XPD.RSDV.GD.ZS), high-tech export share (TX.VAL.TECH.MF.ZS). **PWT 10.0**: solo come confronto in §4.2bis/A.7.
- **UN Comtrade** (API v1, chiave gratuita comtradedeveloper.un.org): export verso il mondo, SITC Rev.3 (≤2006) / Rev.4 (≥2007) a 3 cifre, 6 paesi 1995-2023; tassonomia di Lall (2000) in `lall_classify.py`. Comtrade usa 381 per l'Italia; 1 chiamata/secondo.
- **Software**: Python (pandas, statsmodels; `pip install statsmodels` necessario in ogni nuovo container), R 4.6 (did, urca, strucchange, lmtest, vars, sandwich). Replica cross-software: dire sempre "risultati sostanzialmente coincidenti, con differenze solo di arrotondamento".
- **Editing DOCX** (Claude): `unzip` → `merge_runs.py` → modifica di `word/document.xml` → `zip -X` → `validate.py --original` → `soffice --convert-to pdf`. Controllo di integrità: conteggio paragrafi e validazione OOXML. Verificare sempre MD5 e numero di pagine della versione su cui si lavora: più volte sono circolate versioni vecchie in cache.

## 7. Convenzioni terminologiche

- "Bai-Perron strucchange su modelli lineari con trend segmentato"; break "robustamente rilevati entro le specificazioni in livelli".
- "Batteria standard di test per serie storiche non stazionarie" (mai "Reinsel-Ahn").
- "Rapporto investimento privato/surplus" (mai "tasso di reinvestimento").
- SCM: "divergenza nel regime di convergenza post-1992" (mai "effetto Maastricht" secco).
- Scala mobile cessata con il protocollo del 31 luglio 1992; Ciampi-Giugni 1993 = nuovo assetto contrattuale; Maastricht in vigore 1° novembre 1993.
- R&D→produttività: fatto descrittivo e ipotesi, non "canale bloccato" dimostrato.
- Torrini documenta estrazione di rendita **con** guadagni di TFP: la quasi-rendita spiega la destinazione dei guadagni di efficienza (ai profitti anziché a salari o prezzi), non la loro assenza. Modiano-Onado (2023) è la fonte per profitti-su/investimenti-giù/finanziarizzazione, in particolare per la grande impresa privata post-1982 (§5.5), oltre che per le privatizzate (§6bis).
- Il paper **non usa la TFP** come misura del progresso tecnico (critica di Cambridge): la TFP compare solo in §4.2bis (perché non la usiamo), tabella 9.2 e A.7.

## 8. Decisioni chiuse — non ri-litigare

1. Arrighi fuori da §1.2 e §7.3 e dalla bibliografia; "arrighiano/a" preservato solo in §8.2-8.4 come lente storica (Opzione B).
2. 13/24 Chow HAC + Holm è la cifra canonica; 11/21 è la versione standard preliminare, citabile solo come tale.
3. r è borderline I(0)/I(1), distinto da ω e I/K.
4. UQGD (aggiustato per autonomi) è la baseline di r; r_gross è variante.
5. §6bis (v24): **il DiD è eliminato**. La tesi Modiano-Onado nei termini dell'autore: non privatizzazione → compressione salariale, ma rendita che si innesta su salari già compressi (1992-93, generale, precede le cessioni) e che, con concorrenza incompleta, rafforza un rent-seeking già forte e non viene reinvestita: strada di non-sviluppo. Prova: Tabella 6bis.1 (profitti ↑ e surplus reinvestito ↓ nei privatizzati, opposto nel manifatturiero) + Torrini per la rendita trasferita non ridotta. Il DiD non era identificabile (dati dal 1995, rottura 1992-93 su tutti) e concettualmente inadatto (quota salari per branca = salari compressi o VA gonfiato dalla rendita, indistinguibili). Non reintrodurlo.
6. **Torrini.** Entra in 6bis.2 con citazioni e pagine (`docs/torrini_estratti.md`): rendita trasferita non ridotta (pp. 3, 29, 30, 34), concentrazione settoriale (pp. 28-29), ordine causale (pp. 27-28), attesa condizionale di espansione (p. 32) smentita dai dati 1995-2024. La sua "TFP accelerata" non si usa come misura (§4.2bis): si citano i fatti fisici. Torrini 2016 p. 20: rendita 1995-2001 poi stabilizzazione.
7. VECM ridotto in A.6 con avvertenza forte; VECM a 8 variabili in A.4 solo per tracciabilità.
8. TFP sostituita da identità distributiva + Sylos Labini (v22); la regressione cross-country R&D–TFP sopravvive solo in A.7 "per confronto".
9. "Produttività nominale/capacità di valorizzazione" del libro Punto Rosso **non** importata (nel paper è deflatore + 1/ω, ridondante con l'identità).
10. Framing complessivo: triangolazione descrittiva, non causalità.
11. Arrighi: opzione B applicata in v23 (via da abstract, §1.2, tabelle 1.1-1.2, §7.3, titoli 8.2/8.4; resta la "lettura di lungo periodo" in §8.3 con Arrighi 1994 in bibliografia, 2007 rimosso).
12. §5bis.2 usa dati Comtrade reali con tassonomia di Lall; le serie illustrative sono in `data/preliminary/` con suffisso `_SIMULATO` e non vanno più citate come fonte.
13. §8.6.1 riporta il risultato negativo dello SCM con la Grecia; non si sostituisce con numeri più favorevoli né si rimuove.

## 9. Trappole note

- **Citazioni inventate dagli LLM**: in versioni passate erano comparsi autori inesistenti ("Valeria Martin e Giovanni Vasta") e anni sbagliati. Di Martino e Vasta (2017, non 2010), Modiano e Onado (2023, Il Mulino, Pietro e Marco), Torrini (2005 Temi di discussione 551, anche *Politica Economica* 21(1); 2016 Questioni di Economia e Finanza 318). **Nessun LLM aggiunge o corregge una voce bibliografica senza fonte verificata; in dubbio, lo segnala all'autore.** Le 16 voci aggiunte in v22 (Felipe-McCombie 2014/2020, Gaddi-Garbellini-Oro 2025, Garegnani 1970, Halevi 2025, Harcourt 1972, Kaldor 1966, Pasinetti 1959/1981, Robinson 1953, Rowthorn 1975, Rymes 1971, Shaikh 1974, Sraffa 1960, Sylos Labini 1984/1993, Verdoorn 1949) e le 23 aggiunte in v23 (Abadie ×3, Aghion-Howitt, Arkhangelsky et al., Bugamelli et al. 2018, Callaway-Sant'Anna, Cheung-Lai, Ciocca 2007, de Chaisemartin-D'Haultfœuille, Godley-Cripps 1983, Goodman-Bacon, Lall 2000, Modigliani-Padoa Schioppa 1978, Osterwald-Lenum 1992, Pfaff 2008, Romer 1990, Salvati 2000, Saltari-Travaglini 2009, Sun-Abraham, Sylos Labini 1972, Tarantelli 1978, Xu 2017) sono scritte da Claude senza accesso ai cataloghi: l'autore le verifica una per una. Restano citate nel testo senza voce: Salvati (1981), Romagnoli (1980) — fonti non identificate con certezza, da fornire o eliminare.
- **Dati simulati presentati come reali**: fino alla v22 §5bis.2 dichiarava UN Comtrade ma usava serie lineari di comodo (Kimi A7); §6bis.2 usa ancora il DiD preliminare su dati aggregati/simulati, dichiarato come tale. Prima di citare un CSV, verificare che non sia in `data/preliminary/`.
- Dal v24 l'investment rate per branca è un risultato del paper (Tabella 6bis.1): energia P51G/B1G 101→110→86→57%.
- Numeri "stimati" residui: robustness R&D con WGI/capitale umano (+0,30/0,35) in A.7 — dichiarati provvisori. Lo SCM con la Grecia è stato eseguito (v23).
- Fino alla v22 §4.2 affermava una "svalutazione del REER −13% 1979-85": il dato AMECO dice +29%. Controllare sempre i numeri di cambio reale contro XUNRQ.
- Fino alla v22 §5.5 diceva che il BIC seleziona 0 break per tutte le variabili, contro §2.3/§5.7 (4 break per ω): residuo di un'implementazione precedente. Rimosso in v23.
- In §6bis coesistono la versione preliminare (TWFE su dati simulati/aggregati) e quella su Eurostat reale: è dichiarato, non è un errore da "correggere" cancellando una delle due.
- Le cifre "ω cala di X pp" in §5.2/§8 vanno lette al netto di 1,5-2 pp di riclassificazione IRAP.
- Stringhe spezzate in più run XML: le sostituzioni nel docx vanno verificate sul testo estratto (pdftotext), non date per riuscite.
