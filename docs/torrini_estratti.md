# Torrini: estratti con pagina (per il pezzo 19 dello smontaggio)

Pagine = numerazione stampata nel documento. File: Temi di discussione n. 551 (giugno 2005), "Quota dei profitti e redditività del capitale in Italia: un tentativo di interpretazione"; Questioni di Economia e Finanza n. 318 (marzo 2016), "Labour, profit and housing rent shares in Italian GDP: long-run trends and recent patterns".

## Torrini 2005 — a sostegno della tesi Modiano-Onado (rendita trasferita, non ridotta)
- p. 3 (sommario): le privatizzazioni "hanno determinato un'accelerazione nella produttività totale dei fattori e il contenimento del costo del lavoro, senza tuttavia ridurre significativamente il potere di mercato delle imprese coinvolte".
- p. 29: "poiché le privatizzazioni sono state mosse soprattutto dall'esigenza dello Stato di ridurre il debito, le preoccupazioni per la tutela della concorrenza e per la regolamentazione dei monopoli naturali […] sembrano aver giocato un ruolo di secondo piano (Banca d'Italia, 2000). I guadagni di efficienza si sarebbero quindi tradotti principalmente in un ampliamento dei margini piuttosto che in una riduzione dei prezzi."
- p. 30: privatizzazioni e ristrutturazione "non si siano tradotti in una riduzione del potere di mercato, determinando una redistribuzione delle rendite dai salari ai profitti".
- p. 31: il caso italiano "sembra confermare l'ipotesi teorica avanzata da Blanchard (2000), che vede nella redistribuzione di rendite la causa più probabile dell'innalzamento della quota del capitale negli anni '90".
- p. 34 (conclusioni): "Il passaggio dal pubblico al privato […] uniti a una liberalizzazione ancora parziale, hanno accresciuto l'efficienza senza ridurre il potere di mercato delle imprese privatizzate, con conseguente aumento della redditività."
- pp. 28-29 (evidenza settoriale, Tavv. 5-8): energia, trasporti-comunicazioni e finanza "sono gli unici [settori] in cui il rendimento del capitale si è accresciuto" nel 1989-2001; gli unici con TFP in accelerazione rispetto al 1980-89; costo del lavoro cresciuto "meno che negli altri settori e in misura inferiore all'indice dei prezzi al consumo".
- p. 26 (Fig. 9): "Lo spread tra rendimento e costo d'uso [del capitale] è pertanto aumentato considerevolmente nel privato al netto manifatturiero".

## Torrini 2005 — ordine causale (compressione salariale generale prima, rendita settoriale dopo)
- pp. 27-28: accordi del 1992 "raggiunti durante una delle recessioni più severe del dopoguerra", con il consolidamento del debito che impediva allo Stato di sostenere l'occupazione; occupazione privata −4,6% "per la prima volta in 30 anni"; moratoria del secondo livello che "rese non automatica la redistribuzione degli incrementi di produttività, favorendo così la crescita della quota del capitale".
- p. 28: gli accordi "non possono, tuttavia, spiegare, da sole, le accentuate differenze […]. Al contrario, le privatizzazioni e la ristrutturazione delle imprese pubbliche, per la loro concentrazione in alcuni settori specifici, possono ampiamente dar conto di tali differenze".

## Torrini 2005 — ciò che NON sostiene (da dichiarare)
- p. 32: i settori privatizzati "sembrano invece godere di favorevoli andamenti della redditività relativa, tali da stimolarne l'espansione, sempre che le condizioni istituzionali favoriscano la crescita e l'entrata di nuovi operatori e non permettano il consolidarsi di posizioni di monopolio". Attesa condizionale di espansione: nessuna evidenza sul reinvestimento.
- La misura dell'"efficienza" è la TFP (§4.2bis del paper): citare i fatti fisici (occupazione, costo del lavoro, capitale/prodotto), non la misura.

## Torrini 2016 — conferma e limiti temporali
- p. 20: dal 1995 la quota del lavoro nei settori regolati (RS: energia, trasporti, comunicazioni, finanza) cala di 8 punti, "consistent with a shift in rents from labour to capital (Bassanetti et al., 2010; Torrini, 2005a, 2005b; Azmat et al., 2012) and a rise in the required return to capital following privatization and stock market listing of the main companies"; "Since 2001 the labour share has levelled off at the low levels […] for RS".
- p. 31: "rent reallocation has been much greater in RS" (Bassanetti et al. 2010, 2014); dal 1995 i mark-up nel resto dell'economia si comprimono.

## Verifica ex post sui dati Eurostat 1995-2024 (`scripts/python/privatizzate_surplus.py`, `data/derived/privatizzate_surplus_investimenti.csv`)
Quota profitti (B1G−D1)/B1G, surplus reinvestito P51G/(B1G−D1), crescita reale del VA (% annuo), per periodo 1995-2000 / 2001-07 / 2008-13 / 2014-24:
- Energia (D): quota profitti 59,6 → 71,1 → 74,9 → 78,4; surplus reinvestito 169 → 155 → 115 → 73; VA reale +0,2 / −1,7 / −4,3 / −0,8.
- Telecom (J61): 73,2 → 80,3 → 78,3 → 73,9; 49 → 32 → 39 → 77; VA reale +9,6 / +5,2 / −0,9 / +1,7; quota sul VA totale 1,4 (1995) → 1,9 (2001-07) → 0,8 (2024).
- Finanza (K): 40,5 → 53,0 → 54,4 → 57,4; 25 → 15 → 12 → 15; VA reale +1,5 / +2,7 / +0,9 / −1,0.
- Trasporti (H): 45,1 → 51,5 → 50,3 → 48,4; 74 → 75 → 66 → 63.
- Manifatturiero (C): 48,7 → 46,7 → 42,2 → 45,1; **39 → 47 → 54 → 55**; VA reale +0,9 / +1,1 / −2,9 / +1,2.
- Totale: 58,0 → 58,3 → 56,1 → 55,8; 39 → 41 → 39 → 39.
Lettura: nei settori privatizzati la quota profitti sale e la quota di surplus reinvestita scende (energia e finanza nettamente; telecom fino al 2013, poi investimenti in fibra con rendita evaporata); l'espansione attesa da Torrini non c'è (energia e finanza si contraggono in termini reali; telecom cresce fino al 2007 poi dimezza il suo peso). Il manifatturiero fa l'opposto: quota profitti in calo e surplus reinvestito in aumento. Caveat: in Energia il tasso di investimento 1995-2007 sopra il 100% del VA riflette il ciclo dei cicli combinati; il calo post-2008 è anche fine di quel ciclo; la quota profitti 2022-24 è gonfiata dai prezzi dell'energia.
