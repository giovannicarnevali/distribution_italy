import re, html, sys, pandas as pd
path=sys.argv[1]; xml=open(path,encoding='utf8').read(); n0=xml.count('<w:p ')
def esc(s): return html.escape(s, quote=False).replace("'", "&apos;")
RPR='<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>'
RPRB=RPR.replace('<w:sz w:val="24"/>','<w:b/><w:sz w:val="24"/>')
PPR='<w:pPr><w:spacing w:after="120" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/>'+RPR+'</w:pPr>'
def para(text, lead=None):
    r=(f'<w:r>{RPRB}<w:t xml:space="preserve">{esc(lead)}</w:t></w:r>' if lead else '')+f'<w:r>{RPR}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'
    return f'<w:p w:rsidR="007372E6" w:rsidRPr="00A97429" w:rsidRDefault="003C27D6" w:rsidP="00A97429">{PPR}{r}</w:p>'
def table(rows,widths,sz=18):
    B='<w:tblBorders>'+''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="auto"/>' for s in ['top','left','bottom','right','insideH','insideV'])+'</w:tblBorders>'
    t=f'<w:tbl><w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/>{B}</w:tblPr><w:tblGrid>'+''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)+'</w:tblGrid>'
    for i,row in enumerate(rows):
        t+='<w:tr>'
        for j,c in enumerate(row):
            rp='<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'+('<w:b/>' if i==0 else '')+f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr>'
            t+=f'<w:tc><w:tcPr><w:tcW w:w="{widths[j]}" w:type="dxa"/></w:tcPr><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="{"left" if j==0 else "center"}"/></w:pPr><w:r>{rp}<w:t xml:space="preserve">{esc(str(c))}</w:t></w:r></w:p></w:tc>'
        t+='</w:tr>'
    return t+'</w:tbl>'
def note(text):
    R=RPR.replace('24','20')
    return f'<w:p w:rsidR="007372E6" w:rsidRPr="00A97429" w:rsidRDefault="003C27D6" w:rsidP="00A97429"><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/>{R}</w:pPr><w:r>{R}<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>'
def find(old,count=1):
    for o in (esc(old), html.escape(old,quote=False), old.replace('&','&amp;').replace('&amp;amp;','&amp;'), old):
        if xml.count(o)==count: return o
    raise AssertionError((old[:80], xml.count(esc(old))))
def rep(old,new,count=1):
    global xml
    o=find(old,count); xml=xml.replace(o,esc(new))
def para_bounds(text):
    i=xml.find(find(text)); a=xml.rfind('<w:p ',0,i); b=xml.find('</w:p>',i)+6; return a,b
def del_para(text):
    global xml
    a,b=para_bounds(text); xml=xml[:a]+xml[b:]
def del_para_range(start,end):
    global xml
    a,_=para_bounds(start); _,b=para_bounds(end); assert b>a; xml=xml[:a]+xml[b:]
def del_row(text):
    global xml
    i=xml.find(find(text)); a=xml.rfind('<w:tr',0,i); b=xml.find('</w:tr>',i)+7; xml=xml[:a]+xml[b:]

def set_para(anchor,new,lead=None):
    """sostituisce tutti i run del paragrafo che contiene anchor con (lead in grassetto +) new, conservando pPr e rPr del primo run"""
    global xml
    a,b=para_bounds(anchor); p=xml[a:b]
    m=re.search(r'<w:pPr>.*?</w:pPr>',p,flags=re.S); ppr=m.group(0) if m else ''
    mr=re.search(r'<w:r>(<w:rPr>.*?</w:rPr>)?',p,flags=re.S); rpr=(mr.group(1) or RPR) if mr else RPR
    rpr=re.sub(r'<w:b/>|<w:bCs/>|<w:i/>|<w:iCs/>','',rpr)
    rprb=rpr.replace('<w:rPr>','<w:rPr><w:b/>')
    head=re.match(r'<w:p [^>]*>',p).group(0)
    body=(f'<w:r>{rprb}<w:t xml:space="preserve">{esc(lead)}</w:t></w:r>' if lead else '')+f'<w:r>{rpr}<w:t xml:space="preserve">{esc(new)}</w:t></w:r>'
    xml=xml[:a]+head+ppr+body+'</w:p>'+xml[b:]

def insert_after_para(text,new):
    global xml
    _,b=para_bounds(text); xml=xml[:b]+new+xml[b:]
def insert_before_para(text,new):
    global xml
    a,_=para_bounds(text); xml=xml[:a]+new+xml[a:]

# ===================== A. ARRIGHI (opzione B di luglio) =====================
rep("Sylos Labini (vincolo esterno e competitività), Arrighi (cicli egemoni), Aglietta","Sylos Labini (vincolo esterno e competitività), Aglietta")
rep("Sylos Labini (external constraint and competitiveness), Arrighi (hegemonic cycles), Aglietta","Sylos Labini (external constraint and competitiveness), Aglietta")
rep("Tabella 1.1 — Le cinque fasi del declino italiano nella cornice Aglietta-Arrighi-Goodwin-Luxemburg-Godley.","Tabella 1.1 — Le cinque fasi del declino italiano nella cornice Aglietta-Goodwin-Luxemburg-Godley.")
rep("nel quadro analitico più generale Aglietta-Arrighi-Goodwin-Luxemburg-Godley sviluppato","nel quadro analitico più generale Aglietta-Goodwin-Luxemburg-Godley sviluppato")
del_para_range("Arrighi: cicli sistemici di accumulazione e finanziarizzazione","Per la nostra analisi specifica dell'Italia 1980-2024, le categorie arrighiane utili sono due.")
del_row("Arrighi (cicli sistemici)")
rep("Tabella 1.2 — Cornice teorica integrata Aglietta-Arrighi-Goodwin-Luxemburg-Godley. Aglietta fornisce le categorie analitiche generali a livello nazionale; Arrighi aggiunge la dimensione di lungo periodo e geopolitica (cicli sistemici secolari, finanziarizzazione come autunno egemonico). Marx",
    "Tabella 1.2 — Cornice teorica integrata Aglietta-Goodwin-Luxemburg-Godley. Aglietta fornisce le categorie analitiche generali a livello nazionale. Marx")
del_para("Lettura arrighiana: la fase 5 italiana come autunno locale.")
del_para("Va sottolineata però una differenza specifica del caso italiano rispetto al modello arrighiano puro:")
rep("Combinando i risultati nella cornice Aglietta-Arrighi-Goodwin, emerge","Combinando i risultati nella cornice Aglietta-Goodwin, emerge")
rep("8.4 Coerenza con la cornice Aglietta–Arrighi–Goodwin–Luxemburg–Godley","8.4 Coerenza con la cornice Aglietta–Goodwin–Luxemburg–Godley")
rep("evidenza compatibile con la cornice Aglietta-Arrighi-Goodwin-Luxemburg-Godley","evidenza compatibile con la cornice Aglietta-Goodwin-Luxemburg-Godley")
rep("Lettura arrighiana di lungo periodo. ","Lettura di lungo periodo (lente storico-narrativa, non econometrica). ")
del_para("Arrighi, G. (2007). ")

# ===================== B. CORREZIONI DEL RAMO DI LUGLIO =====================
rep("Di Martino e Vasta (2010, curatori di ","Di Martino e Vasta (2017, curatori di ")
rep("Di Martino e Vasta (curatori, 2010, Ricchi per caso)","Di Martino e Vasta (curatori, 2017, Ricchi per caso)")
rep("Di Martino, P., & Vasta, M. (Eds.) (2010). ","Di Martino, P., & Vasta, M. (a cura di) (2017). ")
rep("5bis. Lock-in nella specializzazione produttiva: il test di Martin-Vasta","5bis. Lock-in nella specializzazione produttiva: il test di Di Martino-Vasta")
rep("5bis.1 La narrativa di Martin-Vasta","5bis.1 La narrativa di Di Martino-Vasta")
rep("il libro di Valeria Martin e Giovanni Vasta, ","il volume curato da Paolo Di Martino e Michelangelo Vasta (2017), ")
rep("Ricchi per caso. Gattopardi e modernizzazione nel capitalismo italiano","Ricchi per caso. La parabola dello sviluppo economico italiano")
rep("Martin-Vasta definisce questo fenomeno come 'lock-in'","Di Martino e Vasta definiscono questo fenomeno come 'lock-in'")
rep("La storia delle privatizzazioni di Modiano e Onado (2009, ","La storia delle privatizzazioni di Modiano e Onado (2023, ")
rep("Illusioni perdute. Le privatizzazioni tra promesse e realtà","Illusioni perdute. Banche, imprese, classe dirigente in Italia dopo le privatizzazioni",3)
rep("La ricerca storica di Modiano e Onado (2009, ","La ricerca storica di Modiano e Onado (2023, ")
rep("Il libro di Francesco Modiano e Mario Onado, ","Il libro di Pietro Modiano e Marco Onado, ")
rep(" (2009), racconta la storia delle privatizzazioni"," (2023), racconta la storia delle privatizzazioni")
rep("Modiano, F., & Onado, M. (2009). ","Modiano, P., & Onado, M. (2023). ")
rep("con Garibaldo e Mortágua (2018, ","con Garibaldo e Mortágua (2019, ")
rep("Bellofiore-Garibaldo-Mortágua (2018)","Bellofiore-Garibaldo-Mortágua (2019)")
rep("Mortágua, M. (201). ","Mortágua, M. (2019). ")
rep("media ~1.0% del PIL (vs. 2.5% della Svezia, 2.2% della Germania, 1.3% della Spagna nel 2024).","media intorno all'1% del PIL, 1,4% nel 2023 (contro 3,6% della Svezia, 3,1% della Germania, 1,5% della Spagna; World Bank GB.XPD.RSDV.GD.ZS).")
rep("il saggio di profitto recupera dal 7.7% del 1992 al 9.4% del 1995, ma il recupero non avviene via produttività (g_LP cala dal 2.9% al 0.2% in vent'anni)","il saggio di profitto recupera dall'8,1% del 1992 al 9,4% del 1995, ma il recupero non avviene via produttività (g_LP cala dal 2,0% del 1986-95 allo 0,3 del 1996-2007)")
rep("Il saggio di profitto recupera (7.7% → 9.4% tra 1992 e 1995)","Il saggio di profitto recupera (8,1% → 9,4% tra 1992 e 1995)")
rep("accordo del 23 luglio 1993 (Ciampi–Giugni) che abolisce di fatto la scala mobile e instaura un regime di concertazione salariale","cessazione della scala mobile con il protocollo del 31 luglio 1992 e accordo del 23 luglio 1993 (Ciampi–Giugni) che instaura un regime di concertazione salariale")
rep("viene firmato l'accordo Ciampi-Giugni che istituisce il regime di concertazione sociale ancorato all'inflazione programmata, abolendo di fatto la scala mobile (legge 38/1986 era già stata modificata, ma il 1993 chiude la transizione).",
    "viene firmato l'accordo Ciampi-Giugni che istituisce il regime di concertazione sociale ancorato all'inflazione programmata e dà un nuovo assetto alla contrattazione, dopo che il protocollo del 31 luglio 1992 aveva già posto fine alla scala mobile.")

# ===================== C. ABSTRACT: Chow 13/24, SCM framing, high-tech =====================
rep("(11 su 21 test di Chow sopravvivono)","(13 su 24 test di Chow con errori HAC sopravvivono)")
rep("(11 of 21 Chow tests survive)","(13 of 24 HAC Chow tests survive)")
rep("evidenza compatibile con un effetto negativo di Maastricht sulla quota salari italiana: gap medio post-1992 = −3,51 punti percentuali (in-space placebo p=0,125), indicazione causale suggestiva ma non conclusiva.",
    "evidenza compatibile con una divergenza negativa della quota salari italiana nel regime di convergenza post-1992: gap medio rispetto al sintetico = −3,51 punti percentuali (in-space placebo p=0,125), indicazione suggestiva ma non conclusiva, che si indebolisce allargando il donor pool alla Grecia (gap −2,5, p=0,22).")
rep("evidence compatible with a negative effect of Maastricht on the Italian wage share: average post-1992 gap = −3.51 percentage points (in-space placebo p=0.125), suggestive but not conclusive causal indication.",
    "evidence compatible with a negative divergence of the Italian wage share in the post-1992 convergence regime: average gap relative to the synthetic = −3.51 percentage points (in-space placebo p=0.125), suggestive but not conclusive, and weaker when Greece is added to the donor pool (gap −2.5, p=0.22).")
rep("apply the Synthetic Control Method to estimate the effect of Maastricht-1992 on the wage share","apply the Synthetic Control Method to estimate the divergence of the Italian wage share after 1992 from a counterfactual built on other European countries")
rep("è la più bassa tra i paesi OCSE avanzati, inferiore alla Spagna e nettamente al di sotto di Francia, Germania, Svezia e Corea.","è fra le più basse tra i paesi OCSE avanzati, pari a quella della Spagna e nettamente al di sotto di Francia, Germania, Svezia e Corea; su dati UN Comtrade classificati con la tassonomia di Lall, la quota low-tech dell'export manifatturiero italiano resta doppia rispetto a Germania e Francia.")
rep("is the lowest among advanced OECD economies, below Spain and well below France, Germany, Sweden, and Korea.","is among the lowest in advanced OECD economies, on a par with Spain and well below France, Germany, Sweden, and Korea; on UN Comtrade data classified with Lall's taxonomy, the low-tech share of Italian manufactured exports remains twice that of Germany and France.")
rep("le serie chiave del paper (r, ω, I/K, REER) risultano compatibili con un processo I(1)","le serie chiave del paper (ω, I/K, REER) risultano compatibili con un processo I(1), r è un caso borderline I(0)/I(1),")
rep("(effetto Maastricht + globalizzazione)","(regime post-Maastricht + globalizzazione)")

# ===================== D. §1.1 e fase 1 (B2, C1, C9, C21) =====================
rep("la quota salari ω = W/Y sale fino al 64% del PIL, comprimendo","la quota salari aggiustata ω (ALCD0) sale fino al 67% nel 1975, comprimendo")
rep("in cui spiaccano due break strutturali: la fine degli anni Settanta (in paritcolare dall’anmalisi emerge il 1979 come anno sparitacque)  rappresenta","in cui spiccano due break strutturali: la fine degli anni Settanta (in particolare dall'analisi emerge il 1979 come anno spartiacque) rappresenta")
rep("il referendum sul divorzio (1974) e l'aborto (1981)","i referendum sul divorzio (1974) e sull'aborto (1981)")
rep("Anche q (composizione tecnica) sale di +12% nel decennio (5.9 → 6.6)","Anche q (composizione tecnica) sale dell'11% tra il 1970 e il 1975 (5,9 → 6,6) e del 15% nell'intero decennio (6,8 nel 1979)")
rep("(imperialismo della domanda).. Le grandi crisi","(imperialismo della domanda). Le grandi crisi")
rep("le crisi degli anni Settanta sono primariamente di manifestazioni di sovraccumulazione","le crisi degli anni Settanta sono primariamente manifestazioni di sovraccumulazione")
rep("Il capitolo 2 descrive dati e metodi. I capitoli 3-7 affrontano le cinque fasi nell'ordine cronologico, presentando le evidenze empiriche per ciascuna.","Il capitolo 2 descrive dati e metodi. I capitoli 3-7 affrontano le cinque fasi nell'ordine cronologico, presentando le evidenze empiriche per ciascuna; due capitoli di approfondimento, 5bis (specializzazione produttiva) e 6bis (privatizzazioni), testano le narrative di Di Martino-Vasta e di Modiano-Onado.")

# ===================== E. §4 fase 2: REER, debito, riallineamenti, cross-ref =====================
rep("I dati confermano il pattern Sylos: la svalutazione del REER (-13% tra 1979 e 1985) coincide cronometricamente con il recupero del saggio di profitto (da 7.7% nel 1979 a 7.7% nel 1985, con valori intermedi vicini all'8%). Negli stessi anni la quota salari ω scende da 65.5% a 61.9% — primo indizio della pressione discendente che si consolida solo dopo il 1992.",
    "I dati qualificano il pattern Sylos. Le svalutazioni nominali nello SME non si traducono in un deprezzamento reale: il REER basato sul costo del lavoro per unità di prodotto (AMECO XUNRQ) si apprezza del 29% tra il 1979 e il 1985 (da 80,6 a 104,1), perché il differenziale d'inflazione più che compensa i riallineamenti. Il saggio di profitto cala dall'8,0% del 1979 al 7,0% del 1983 e recupera all'8,75% del 1989: il recupero coincide non con una svalutazione reale, che non c'è, ma con la discesa di ω dal 64,2% del 1983 al 58,5% del 1989, dopo il decreto di San Valentino del 1984 — primo indizio della pressione distributiva che si consolida dopo il 1992. Nella fase 2 il canale di Sylos Labini opera dunque come svalutazione nominale che accomoda l'inflazione e protegge i margini, non come guadagno di competitività reale.")
rep("Il rapporto debito/PIL passa dal 56.8% del 1980 al 95.7% del 1990 (+38.9 punti).","Il rapporto debito/PIL passa dal 54,3% del 1980 al 91,4% del 1990 (+37 punti; AMECO UDGG/UVGD).")
rep("Tra il 1981 e il 1987 si verificano 7 riallineamenti della lira (ottobre 1981, giugno 1982, marzo 1983, luglio 1985, aprile 1986, gennaio 1987), per una svalutazione cumulata","Tra il 1981 e il 1987 si verificano 7 riallineamenti della lira (marzo e ottobre 1981, giugno 1982, marzo 1983, luglio 1985, aprile 1986, gennaio 1987), seguiti nel gennaio 1990 dal passaggio alla banda stretta con riduzione della parità centrale, per una svalutazione cumulata")
rep("(riallineamenti del 1981, 1982, 1983, 1985, 1986, 1990)","(riallineamenti del 1981, 1982, 1983, 1985, 1986 e 1987, poi la riduzione della parità centrale del 1990)")
rep("(Capitolo 8 dettagliato; qui i risultati salienti)","(§2.3 e §5.5 per il dettaglio; qui i risultati salienti)")

# ===================== F. §5.5: Bai-Perron riconciliato; meta-linguaggio =====================
set_para("Vero Bai-Perron con BIC.","Con regressione segmentata su intercetta e trend (2 parametri per segmento), trimming 0,15 e massimo 5 break, il BIC seleziona 4 break per ω (1970, 1983, 1997, 2008), 4 per r (1970, 1983, 2000, 2011), 2 per CA/Y (1992, 2011), 4 per il REER (1972, 1981, 1992, 2008) e 3 per X/Y (1976, 1992, 2008). L'implementazione Python (programmazione dinamica, script bai_perron.py nel repository) replica esattamente strucchange per ω, r e CA/Y; per I/K e q il numero di break selezionato è sensibile ai dettagli di implementazione (4-5). Con la sola intercetta (mean shift, 1 parametro per segmento) il BIC è più parsimonioso e seleziona per ω due soli break, 1984 e 1993: esattamente i due pivot della periodizzazione. Il Bai-Perron è dunque più prudente del PELT nel numero di break, ma non lo contraddice: la selezione endogena conferma la cesura 1992-94 per ω, CA/Y, REER e X/Y e quella del 1983-84 per ω e r (accordo di San Valentino), e colloca il primo break al 1970-72 piuttosto che al 1979.",lead="Risultato (a) — Bai-Perron con BIC. ")
rep("La periodizzazione narrativa non è selezionata endogenamente dal vero Bai-Perron","La selezione endogena colloca il primo break al 1970-72 (autunno caldo), non al 1979; i pivot 1983-84 e 1992-94 sono confermati, il 1979 no")
rep("Una critica esterna sollevata in fase di peer review (ChatGPT) ha correttamente osservato che la Tabella 5.2 contiene","La Tabella 5.2 contiene")
rep("Una revisione metodologica esterna ha sollevato un punto importante: alcune serie","Un punto metodologico importante: alcune serie")
rep("I risultati ADF + KPSS confermano il sospetto di non-stazionarietà: r, ω, I/K e log(REER) risultano compatibili con un processo I(1);","I risultati ADF + KPSS confermano il sospetto di non-stazionarietà: ω, I/K e log(REER) risultano compatibili con un processo I(1); r è un caso borderline (ADF −2,81 contro valore critico −2,89; KPSS non rigetta la stazionarietà) e per prudenza è trattato come I(1) nelle specificazioni in differenze;")

# ===================== G. §5bis.2: dati Comtrade reali (Lall) =====================
per=pd.read_csv(sys.argv[2])
P=lambda iso,p,c: f"{per[(per.iso==iso)&(per.period==p)][c].iloc[0]:.1f}".replace('.',',')
names={'ITA':'Italia','DEU':'Germania','FRA':'Francia','ESP':'Spagna','PRT':'Portogallo','SWE':'Svezia'}
rows=[["Paese","Low-tech 1995-99","Low-tech 2015-23","Medium-tech 1995-99","Medium-tech 2015-23","High-tech 1995-99","High-tech 2015-23","Risorse nat. 2015-23"]]
for iso in ['ITA','DEU','FRA','ESP','PRT','SWE']:
    rows.append([names[iso],P(iso,'1995-99','low'),P(iso,'2015-23','low'),P(iso,'1995-99','medium'),P(iso,'2015-23','medium'),P(iso,'1995-99','high'),P(iso,'2015-23','high'),P(iso,'2015-23','resource')])
rep("Testiamo la tesi di Martin-Vasta misurando l'evoluzione della specializzazione export italiana per livelli tecnologici (low, medium, high-tech) dal 1995 al 2024, e confrontandola con paesi europei comparabili (Francia, Spagna, Germania). Se la tesi di lock-in è corretta, ci aspettiamo:",
    "Testiamo la tesi di Di Martino-Vasta misurando l'evoluzione della composizione tecnologica dell'export manifatturiero italiano dal 1995 al 2023 e confrontandola con Francia, Germania, Spagna, Portogallo e Svezia. Se la tesi del lock-in è corretta, ci aspettiamo che la quota low-tech italiana resti strutturalmente superiore a quella dei grandi paesi manifatturieri europei e che la quota high-tech non converga.")
del_para_range("Italia rimane bloccata in low-tech (specializzazione bassa) mentre Francia/Spagna/Germania transitano verso high-tech","L'elasticità export-produttività è bassa per l'Italia, specialmente nel low-tech")
set_para("I dati sull'export specialization sono costruiti da UN Comtrade","I dati sono gli export verso il mondo per prodotto a 3 cifre SITC (Rev. 3 fino al 2006, Rev. 4 dal 2007), scaricati da UN Comtrade (API v1, novembre 2026) per i sei paesi, 1995-2023 (script fetch_comtrade.py e lall_classify.py nel repository). La classificazione tecnologica è la tassonomia di Lall (2000), definita sui codici SITC a 3 cifre: prodotti primari, manufatti basati su risorse naturali, low-tech (tessile-abbigliamento-calzature e altri), medium-tech (automotive, processo, meccanica), high-tech (elettronica-elettrotecnica e altri). I codici introdotti da Rev. 3 e Rev. 4 sono assegnati per analogia alla voce di origine (elenco nello script); la quota non classificata è dello 0,03% dell'export. Le quote sono calcolate sull'export manifatturiero (esclusi prodotti primari e altre transazioni), non come vantaggio comparato rivelato: il confronto riguarda la composizione interna dell'export, non la competitività relativa al mondo. Una versione precedente di questa sezione usava serie illustrative, non dati Comtrade: sono state sostituite.",lead="Fonti dati e metodologia. ")
a,_=para_bounds("La Figura 5bis.1 mostra l'evoluzione della specializzazione export per paese e tech level."); _,b=para_bounds("Figura 5bis.1: Specializzazione export e lock-in nella tecnologia (1995-2024)")
xml=xml[:a]+table(rows,[1300,1050,1050,1150,1150,1050,1050,1100])+note("Tabella 5bis.1 — Composizione tecnologica dell'export manifatturiero, quote percentuali, medie di periodo. Fonte: UN Comtrade, export verso il mondo, SITC Rev. 3/4 a 3 cifre; classificazione di Lall (2000). La colonna \"Risorse nat.\" è la quota dei manufatti basati su risorse naturali (agroalimentare trasformato, metalli, raffinazione); low + medium + high + risorse = 100.")+xml[b:]
rep("I risultati sono coerenti con Martin-Vasta:","I risultati, nella Tabella 5bis.1, sono coerenti con la tesi del lock-in ma la qualificano.")
set_para("Italia 1995→2024: Low-tech",f"L'Italia riduce la quota low-tech dal {P('ITA','1995-99','low')}% (1995-99) al {P('ITA','2015-23','low')}% (2015-23), ma resta a un livello doppio rispetto a Germania ({P('DEU','2015-23','low')}) e Francia ({P('FRA','2015-23','low')}) e pari a quello del Portogallo; la quota high-tech sale dal {P('ITA','1995-99','high')} al {P('ITA','2015-23','high')}%, la più bassa del gruppo dopo il Portogallo e appena sopra la Spagna ({P('ESP','2015-23','high')}); la quota medium-tech, dove sta la meccanica strumentale, è ferma al 41% per tutto il periodo, contro il 49 della Germania. La convergenza verso l'high-tech è modesta (+2,5 punti in venticinque anni, contro +4,9 della Germania) e la riduzione del low-tech non si traduce in upgrade ma in un aumento della componente basata su risorse naturali (agroalimentare, metalli: dal {P('ITA','1995-99','resource')} al {P('ITA','2015-23','resource')}%).")
del_para_range("Francia 1995→2024: Low-tech −4.4%","Germania 1995→2024: Low-tech −3.1%")
set_para("La composizione dell'export italiano mostra una persistenza","La composizione dell'export italiano mostra quindi una persistenza della specializzazione low-tech relativamente maggiore rispetto a Francia, Germania e Spagna e una crescita contenuta della componente high-tech, coerente con la tesi del lock-in di Di Martino-Vasta. Si tratta di evidenza descrittiva sulla composizione: la lenta convergenza potrebbe riflettere fattori non osservati (specializzazione iniziale, dimensione media delle imprese, accesso al credito, domanda mondiale per i prodotti italiani), e un'analisi a livello di settore o distretto rafforzerebbe l'identificazione. La tassonomia di Lall classifica i prodotti, non le imprese: la meccanica strumentale italiana è medium-tech per costruzione, e la sua forza relativa (§5bis.3) non emerge da questo indicatore.")
rep("Martin-Vasta","Di Martino-Vasta",1)
rep("I dati sono inequivocabili: l'Italia ha la quota high-tech export più bassa tra i paesi OECD avanzati.","I dati sono netti: l'Italia ha una delle quote high-tech export più basse tra i paesi OCSE avanzati.")
rep("Persino la Spagna, partita nel 2007 al 5.61% (sotto Italia che era al 6.73%), supera Italia nel 2015–2022 con 8.13%.","La Spagna, partita nel 2007 al 5,61% (sotto l'Italia, 6,73%), raggiunge l'Italia nel 2015–2022 (8,13 contro 8,12%); il Portogallo resta sotto (6,18%).")
rep("Italia 8.1% di high-tech export su manifatturiero (2015–22), il livello più basso tra paesi OECD avanzati. Spagna ha superato Italia","Italia 8,1% di high-tech export su manifatturiero (2015–22), fra i livelli più bassi tra i paesi OCSE avanzati, pari alla Spagna; su Comtrade/Lall la quota low-tech resta doppia rispetto a Germania e Francia")

# ===================== H. §6: produttività, picco/minimo, §6.3.1 p-value =====================
rep("con picco al 51.4% nel 2000.","con minimo al 51,4% nel 2000.")
rep("La produttività del lavoro cresce solo dello 0.2% medio annuo nel decennio 1996-2007, contro un 2.9% del decennio precedente.","La produttività del lavoro cresce solo dello 0,3% medio annuo nel 1996-2007, contro il 2,0% del decennio precedente (1986-95) e il 3,1 degli anni Settanta.")
rep("+0,18 (0,09), p=0,054","+0,18 (0,09), p=0,07")
rep("al margine della significatività (p=0,054, n=15)","al margine della significatività (p=0,07 con la distribuzione t a 11 gradi di libertà, n=15)")

# ===================== I. §6bis: Ferrovie, ipotesi, T=30, dataset, t-stat, refusi =====================
rep("Le privatizzazioni (Telecom Italia 1997, ENEL 1999, Ferrovie Italiane 2000+) erano ideate","Le privatizzazioni e le trasformazioni societarie (Telecom Italia 1997, ENEL 1999; Ferrovie dello Stato, società per azioni dal 1992 ma a capitale interamente pubblico) erano ideate")
rep("ma NON hanno investito significativamente in innovazione tecnologica, e hanno compresso i salari della manodopera occupata.","ma NON hanno investito significativamente in innovazione tecnologica e — questa è l'ipotesi che il DiD di §6bis.2-6bis.5 sottopone a verifica e che §6bis.6 riformula — avrebbero compresso i salari della manodopera occupata.")
rep("nei settori privatizzati (Telecom, Energia, Ferrovie) con un gruppo di controllo","nei settori privatizzati o trasformati in società per azioni (Telecom, Energia, Ferrovie) con un gruppo di controllo")
rep("= −2.16 pp. La Figura 6bis.1(A) mostra visivamente il divergement post-1992","= −2,17 pp. La Figura 6bis.1(A) mostra visivamente la divergenza post-1992")
rep("Sample: 1995–2024 (T=29), Italia, 7 settori (3 trattati + 4 controllo).","Sample: 1995–2024 (T=30), Italia, 7 settori (3 trattati + 4 controllo); 209 osservazioni settore-anno (una mancante). Il dataset è did_eurostat_REAL.csv nel repository ed è il file letto dallo script R did_callaway_santanna.R.")
rep(" Trasporti terrestri (Ferrovie dello Stato, trasformazione 2001+)."," Trasporti terrestri (Ferrovie dello Stato: trasformazione in società per azioni e separazione rete-servizio 2000-2001, senza cessione della proprietà pubblica; per questa branca il \"trattamento\" è corporatizzazione e apertura regolatoria, non privatizzazione).")
rep("Il t-stat osservato di −4.31 cade al di fuori","Il t-stat osservato (−4,82 nella specificazione aggregata) cade al di fuori")

# ===================== J. §7: spread, cambio, CA/Y, debito =====================
rep("Lo spread BTP-Bund collassa dai 575 pb del 2011 a circa 100-150 pb","Lo spread BTP-Bund collassa dai 575 pb del picco intraday del novembre 2011 a circa 100-150 pb")
rep("Il cambio EUR/USD scende da 1.40 nel 2014 a 1.05 nel 2017, e si stabilizza intorno a 1.10-1.20 nel periodo successivo.","Il cambio EUR/USD scende da 1,33 (media 2014) a 1,11 (2015) e 1,13 (2017), oscilla intorno a 1,10-1,20 fino al 2021 e scende sotto la parità nel 2022.")
rep("riporta CA/Y in avanzo dal -3% del 2010 al +2% del 2013,","riporta CA/Y in avanzo dal −3,2% del 2010 al +1,0% del 2013 e +1,8% del 2014,")
rep("Il rapporto debito/PIL passa dal 116% del 2010 al 132% del 2014.","Il rapporto debito/PIL passa dal 119% del 2010 al 135% del 2014 (AMECO UDGG/UVGD).")

# ===================== K. §8.6 SCM: meta-linguaggio, media 98-01, Grecia reale =====================
rep("Tuttavia, come sottolineato correttamente in peer review, la significatività di un break","Tuttavia la significatività di un break")
rep("Picco 1998-2001: −5.52 pp.","Media 1998-2001: −5,4 pp.")
rep("Robustezza al leave-one-out (peer review correction). ","Robustezza al leave-one-out. ")
rep("Una critica metodologica sollevata in peer review è che lo SCM","Una critica metodologica naturale è che lo SCM")
a,_=para_bounds("Una raccomandazione della peer review esterna riguarda l'allargamento del donor pool dello SCM"); _,b=para_bounds("L'interpretazione sostantiva è invariata.")
new861 = para("Un'estensione naturale riguarda l'allargamento del donor pool dello SCM oltre i sette donor originari (otto unità con l'Italia). Con n = 8 unità il p-value minimo ottenibile dal placebo in-space è 1/8 = 0,125, indipendentemente dalla magnitudine del gap stimato: la non-significatività del risultato riflette in parte la dimensione del campione. L'allargamento è però delicato, perché i candidati naturali sono pochi: i paesi dell'Est Europa entrano in UE nel 2004 e non possono fungere da controlli per uno shock 1992; Stati Uniti, Giappone, Canada e Australia hanno traiettorie distributive eterogenee rispetto al cluster europeo continentale. Tra i paesi europei con dati AMECO comparabili dal 1960 il candidato più informativo è la Grecia, che entra nello SME nel 1998 e nell'euro nel 2001. Replicando lo SCM con la stessa specificazione e otto donor (i sette originari più la Grecia; script scm_greece.py nel repository), il risultato peggiora: il fit pre-trattamento si deteriora (RMSPE 1,64 contro 1,10), perché l'ottimizzatore assegna alla Grecia un peso del 16% e al Portogallo del 19%, due paesi con traiettorie della quota salari idiosincratiche; il gap medio post-1992 scende a −2,5 punti percentuali (−4,7 nel 1998-2001); e nel placebo in-space l'Italia non è più l'unità con il rapporto RMSPE post/pre più alto, superata dalla Spagna: rank 2/9, p-value one-sided 0,222. Il leave-one-out sul pool allargato dà gap nell'intervallo [−3,5; −2,5]; escludendo la Grecia si torna al risultato baseline. La replica della specificazione baseline con lo stesso codice riproduce i pesi (Spagna 43,8%, Francia 22,6%, Austria 27,5%, Finlandia 6,1%), il gap (−3,53) e il p-value (0,125) del paragrafo precedente.") \
 + para("L'interpretazione sostantiva ne esce indebolita, non rafforzata, e va dichiarata come tale: la divergenza della quota salari italiana post-1992 rispetto al sintetico è robusta alla composizione del pool originario (leave-one-out) ma non all'aggiunta di un donor strutturalmente diverso, e con nove unità il placebo in-space non la distingue dal rumore. L'evidenza resta \"suggestiva ma non conclusiva\", con l'accento sul secondo termine. Una soluzione metodologicamente più ambiziosa sarebbe il Generalized Synthetic Control di Xu (2017) o lo Synthetic Difference-in-Differences di Arkhangelsky et al. (2021), che combinano SCM e DiD e tipicamente producono inferenza più potente con donor pool piccoli; la loro applicazione è lasciata a ricerca futura.")
xml=xml[:a]+new861+xml[b:]
rep("(a) estensione del donor pool con Grecia e paesi dell'Est Europa entrati in UE post-2004;","(a) estensione del donor pool ai paesi dell'Est Europa entrati in UE post-2004, con trattamento del 2004 come secondo shock;")
rep("per verificare se l'effetto Maastricht è coerente attraverso variabili distributive diverse","per verificare se la divergenza è coerente attraverso variabili distributive diverse")
rep(" e coerente con: (i) i break Chow del 1992 sopravvissuti a Holm-Bonferroni; (ii) il DiD privatizzazioni con wild cluster bootstrap p=0.022 (§6bis.3); (iii) la robustezza leave-one-out dimostrata sopra. Il peso della tesi distributiva-istituzionale poggia su questi tre risultati combinati, non sullo SCM da solo."," ma non all'allargamento del donor pool alla Grecia (§8.6.1), ed è coerente con: (i) i break Chow del 1992 sopravvissuti a Holm-Bonferroni; (ii) la decomposizione di Kalecki e l'equazione di Sylos Labini, che documentano lo stesso cambio di regime distributivo dopo il 1992-93. Il DiD sulle privatizzazioni, declassato in §6bis.5, non è più fra i sostegni. Il peso della tesi distributiva-istituzionale poggia su questi risultati combinati, non sullo SCM da solo.")
rep("Robustness con controlli aggiuntivi (peer review correction). ","Robustness con controlli aggiuntivi. ")
rep("Una raccomandazione della peer review esterna è di testare","Un'estensione naturale è testare")

# ===================== L. §9 e appendici: refusi, A.4.1, A.5, Johansen-Osterwald =====================
rep("Le firmazioni quantitative (es. coefficiente +27.1 su CA/Y) non sono attendibili","Le stime quantitative (es. coefficiente +27.1 su CA/Y) non sono attendibili")
rep("la storia raccontata nel paper è anni '70, recupero post-1992 via ω↓) è ","la storia raccontata nel paper (caduta di r negli anni '70, recupero post-1992 via ω↓) è ")
rep("una rejezione marginale che","un rigetto marginale che")
rep("Per il REER il jump più grande è in 1967 (fine Bretton Woods)","Per il REER il jump più grande è nel 1967 (svalutazione della sterlina)")
rep("Tabella A.4.1 — Test di radice unitaria Augmented Dickey-Fuller (ADF) con selezione lag automatica via AIC. La maggior parte delle variabili appare integrata di ordine 1: log r, log REER, CA/Y e g_LP risultano stazionarie sui livelli al 5%, ma la giustificazione del VECM si fonda sulla potenziale presenza di cointegrazione tra le componenti I(1) restanti.",
    "Tabella A.4.1 — Test ADF con selezione lag via AIC sulle trasformazioni logaritmiche usate nel VECM esteso a 8 variabili. Questi risultati valgono per quelle trasformazioni e per quel modello esplorativo; la tabella di riferimento del paper sulle proprietà di integrazione delle serie in livelli (ADF e KPSS, replicati in R con urca) è in §5.7: r è borderline I(0)/I(1) (ADF −2,81 contro valore critico −2,89; KPSS non rigetta), ω, I/K e il REER sono I(1), CA/Y è I(0). La stazionarietà di log r e log REER al 5% qui riportata riflette la trasformazione e la specificazione, ed è la ragione per cui il paper tratta r come caso borderline e adotta la regressione in differenze come specificazione prudenziale.")
rep("I valori critici qui riportati sono quelli asintotici di Johansen-Osterwald (1995).","I valori critici qui riportati sono quelli asintotici di Osterwald-Lenum (1992).")
rep("Tutti i risultati del paper sono replicabili tramite due notebook Jupyter Python (Marx_Schumpeter_Italia_v9.ipynb e Marx_Schumpeter_Italia_competitivita.ipynb) sviluppati nel periodo aprile 2026 con: Python 3.12, statsmodels 0.14.6, linearmodels 7.0, ruptures, pandas, numpy, scipy, matplotlib.",
    "Tutti i risultati del paper sono replicabili tramite il notebook Jupyter Python Marx_Schumpeter_Italia_v12_robustness.ipynb (versione finale; le versioni precedenti sono archivio), gli script Python del repository (identità TFP, Sylos Labini, Bai-Perron, SCM con Grecia, Comtrade/Lall) e gli script R (did_callaway_santanna.R; working_paper_robustness.R per Phillips-Ouliaris, Johansen e Bai-Perron), sviluppati fra aprile e novembre 2026 con: Python 3.12-3.13, statsmodels 0.14, linearmodels, ruptures, pandas, numpy, scipy, matplotlib; R 4.6.0 con strucchange, urca, vars, lmtest, sandwich, did.")

# ===================== M. Acknowledgments =====================
rep("L'autore ha utilizzato modelli linguistici di grandi dimensioni (Claude di Anthropic, ChatGPT di OpenAI, DeepSeek) come assistenti","L'autore ha utilizzato modelli linguistici di grandi dimensioni (Claude di Anthropic, ChatGPT di OpenAI, Kimi di Moonshot, DeepSeek) come assistenti")
rep("ChatGPT (OpenAI) e DeepSeek sono stati utilizzati come revisori critici simulati per identificare le debolezze metodologiche del paper preliminare. Le loro critiche sono state recepite nelle revisioni v2 e v3 (vero Bai-Perron via R/strucchange, abbandono del CE1 spurious, sostituzione della proxy (S-I)_priv con saldi settoriali Eurostat veri, attenuazione della causalità).",
    "ChatGPT (OpenAI), Kimi (Moonshot) e DeepSeek sono stati utilizzati come revisori critici simulati, in round successivi, per identificare debolezze metodologiche, incoerenze numeriche ed errori di attribuzione bibliografica. Le critiche accolte hanno portato, fra l'altro, al Bai-Perron via R/strucchange, all'abbandono del CE1 spurio, alla sostituzione della proxy (S-I)_priv con i saldi settoriali Eurostat, all'attenuazione del linguaggio causale, allo stimatore di Callaway-Sant'Anna, alla sostituzione dei dati illustrativi di §5bis.2 con dati UN Comtrade e all'esecuzione effettiva dello SCM con la Grecia. Alcune voci bibliografiche di versioni precedenti erano state generate dai modelli in modo errato: sono state verificate e corrette sui cataloghi editoriali.")
rep("Il codice e i dati per la replica completa del paper (notebook Jupyter Python + script R) sono disponibili su richiesta all'autore. Una versione successiva del paper migrerà su un repository pubblico (Zenodo, GitHub) per garantire piena replicabilità.",
    "Il codice e i dati per la replica del paper (notebook Jupyter Python, script Python e R, CSV) sono nel repository GitHub giovannicarnevali/distribution_italy; il deposito su Zenodo con DOI accompagnerà la versione sottoposta.")

# ===================== N. Tabella A.1: due righe mancanti =====================
i=xml.find('ITA.1.0.0.0.NETN'); ra=xml.rfind('<w:tr',0,i); rb=xml.find('</w:tr>',i)+7; row=xml[ra:rb]
def mkrow(code,desc,unit):
    r=row.replace('>NETN<',f'>{code}<').replace('>Occupati totali<',f'>{esc(desc)}<').replace('ITA.1.0.0.0.NETN',f'ITA.1.0.0.0.{code}')
    r=re.sub(r'(<w:t>)1000(</w:t>)',r'\g<1>'+unit+r'\2',r,count=1); return r
xml=xml[:rb]+mkrow('UQND','Surplus operativo netto aggiustato per gli autonomi (per r_NETTO, §3.4)','Mrd EUR')+mkrow('UTSG','Contributi sociali effettivi: gradino IRAP 1998 (§5.5)','Mrd EUR')+xml[rb:]

# ===================== O. Bibliografia: voci mancanti (verificate) + Sraffa in ordine =====================
NEW=[
"Abadie, A., & Gardeazabal, J. (2003). The economic costs of conflict: A case study of the Basque Country. American Economic Review, 93(1), 113-132.",
"Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies: Estimating the effect of California's tobacco control program. Journal of the American Statistical Association, 105(490), 493-505.",
"Abadie, A., Diamond, A., & Hainmueller, J. (2015). Comparative politics and the synthetic control method. American Journal of Political Science, 59(2), 495-510.",
"Aghion, P., & Howitt, P. (1992). A model of growth through creative destruction. Econometrica, 60(2), 323-351.",
"Arkhangelsky, D., Athey, S., Hirshberg, D. A., Imbens, G. W., & Wager, S. (2021). Synthetic difference-in-differences. American Economic Review, 111(12), 4088-4118.",
"Bugamelli, M., Lotti, F., Amici, M., Ciapanna, E., Colonna, F., D'Amuri, F., Giacomelli, S., Linarello, A., Manaresi, F., Palumbo, G., Scoccianti, F., & Sette, E. (2018). Productivity growth in Italy: A tale of a slow-motion change. Banca d'Italia, Questioni di Economia e Finanza, n. 422.",
"Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. Journal of Econometrics, 225(2), 200-230.",
"Cheung, Y.-W., & Lai, K. S. (1993). Finite-sample sizes of Johansen's likelihood ratio tests for cointegration. Oxford Bulletin of Economics and Statistics, 55(3), 313-328.",
"Ciocca, P. (2007). Ricchi per sempre? Una storia economica d'Italia (1796-2005). Torino: Bollati Boringhieri.",
"de Chaisemartin, C., & D'Haultfœuille, X. (2020). Two-way fixed effects estimators with heterogeneous treatment effects. American Economic Review, 110(9), 2964-2996.",
"Godley, W., & Cripps, F. (1983). Macroeconomics. Oxford: Oxford University Press.",
"Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. Journal of Econometrics, 225(2), 254-277.",
"Lall, S. (2000). The technological structure and performance of developing country manufactured exports, 1985-98. Oxford Development Studies, 28(3), 337-369.",
"Modigliani, F., & Padoa-Schioppa, T. (1978). The Management of an Open Economy with \"100% Plus\" Wage Indexation. Essays in International Finance, n. 130. Princeton: Princeton University, International Finance Section.",
"Osterwald-Lenum, M. (1992). A note with quantiles of the asymptotic distribution of the maximum likelihood cointegration rank test statistics. Oxford Bulletin of Economics and Statistics, 54(3), 461-472.",
"Pfaff, B. (2008). Analysis of Integrated and Cointegrated Time Series with R (2nd ed.). New York: Springer.",
"Romer, P. M. (1990). Endogenous technological change. Journal of Political Economy, 98(5), S71-S102.",
"Salvati, M. (2000). Occasioni mancate. Economia e politica in Italia dagli anni '60 a oggi. Roma-Bari: Laterza.",
"Saltari, E., & Travaglini, G. (2009). Le radici del declino economico. Occupazione e produttività in Italia nell'ultimo decennio. Torino: UTET.",
"Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. Journal of Econometrics, 225(2), 175-199.",
"Sylos Labini, P. (1972). Sindacati, inflazione e produttività. Roma-Bari: Laterza.",
"Tarantelli, E. (1978). Il ruolo economico del sindacato: il caso italiano. Roma-Bari: Laterza.",
"Xu, Y. (2017). Generalized synthetic control method: Causal inference with interactive fixed effects models. Political Analysis, 25(1), 57-76.",
]
# Sraffa: sposta prima della prima voce Sylos Labini
sa,sb=para_bounds("Sraffa, P. (1960)."); sraffa=xml[sa:sb]; xml=xml[:sa]+xml[sb:]
def bib_entries():
    i0=xml.find(find("Bibliografia essenziale")); i1=xml.find(find("Appendice metodologica"),i0)
    out=[]
    for m in re.finditer(r'<w:p [^>]*>.*?</w:p>',xml[i0:i1],flags=re.S):
        t=''.join(re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>',m.group(0),flags=re.S))
        if re.match(r"[A-Za-zÀ-ÿ'’\-]+, [A-Z]",html.unescape(t)) or t.startswith('de Chaisemartin'): out.append((i0+m.start(),html.unescape(t)))
    return out
def key(t): return re.sub(r'^(de |van )','',t).lower()
def insert_bib(entry):
    global xml
    ents=bib_entries()
    pos=None
    for p,t in ents:
        if key(t)>key(entry): pos=p; break
    if pos is None: pos=ents[-1][0]+len(re.match(r'<w:p [^>]*>.*?</w:p>',xml[ents[-1][0]:],flags=re.S).group(0))
    xml=xml[:pos]+para(entry)+xml[pos:]
insert_bib_sraffa=None
for e in NEW: insert_bib(e)
# reinserisci Sraffa nella posizione alfabetica
ents=bib_entries(); pos=[p for p,t in ents if key(t)>key("Sraffa, P.")][0]; xml=xml[:pos]+sraffa+xml[pos:]
rep("leave-one-out range stabile [−3.89, −3.26] pp; evidenza causale suggestiva non conclusiva)","leave-one-out range stabile [−3.89, −3.26] pp; con la Grecia nel donor pool gap −2,5 e p=0,22; evidenza suggestiva non conclusiva)")
rep("8.6.1 Donor pool allargato (Grecia post-1981)","8.6.1 Donor pool allargato alla Grecia: un risultato negativo")

# ===================== P. Riordino alfabetico della bibliografia =====================
i0=xml.find(find("Bibliografia essenziale")); i0=xml.find('</w:p>',i0)+6
i1=xml.find(find("Appendice metodologica")); i1=xml.rfind('<w:p ',0,i1)
block=xml[i0:i1]; ps=re.findall(r'<w:p [^>]*>.*?</w:p>|<w:p>.*?</w:p>',block,flags=re.S)
assert ''.join(ps)==block.strip() or len(''.join(ps))>len(block)*0.98, (len(''.join(ps)),len(block))
def ptxt(p): return html.unescape(''.join(re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>',p,flags=re.S)))
ents=[p for p in ps if ptxt(p).strip()]
def k(p):
    t=ptxt(p).strip(); t=re.sub(r'^(de |van |von )','',t,flags=re.I); return t.lower()
ents.sort(key=k)
xml=xml[:i0]+''.join(ents)+xml[i1:]

open(path,'w',encoding='utf8').write(xml)
print("paragrafi", n0, "->", xml.count('<w:p '))
