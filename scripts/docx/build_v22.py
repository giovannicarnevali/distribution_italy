import re, html, sys
path=sys.argv[1]; xml=open(path).read(); n0=xml.count('<w:p ')
def esc(s): return html.escape(s, quote=False).replace("'", "&apos;")
RPR='<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>'
RPRB=RPR.replace('<w:sz w:val="24"/>','<w:b/><w:sz w:val="24"/>')
PPR='<w:pPr><w:spacing w:after="120" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/>'+RPR+'</w:pPr>'
def para(text, lead=None):
    r=(f'<w:r>{RPRB}<w:t xml:space="preserve">{esc(lead)}</w:t></w:r>' if lead else '')+f'<w:r>{RPR}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'
    return f'<w:p w:rsidR="007372E6" w:rsidRPr="00A97429" w:rsidRDefault="003C27D6" w:rsidP="00A97429">{PPR}{r}</w:p>'
def heading(text,lvl=2):
    return f'<w:p w:rsidR="007372E6" w:rsidRPr="00A97429" w:rsidRDefault="003C27D6" w:rsidP="00A97429"><w:pPr><w:pStyle w:val="Heading{lvl}"/><w:spacing w:line="360" w:lineRule="auto"/></w:pPr><w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>'
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
def rep(old,new,count=1):
    global xml
    o=esc(old); c=xml.count(o)
    if c!=count:
        o2=html.escape(old,quote=False); c2=xml.count(o2)
        if c2!=count:
            o3=old.replace('&','&amp;').replace('&amp;amp;','&amp;'); c3=xml.count(o3); assert c3==count,(old[:70],c,c2,c3); o=o3
        else: o=o2
    xml=xml.replace(o,esc(new))
def para_span(start_text,end_text):
    """ritorna (a,b): inizio del <w:p> che contiene start_text, fine del </w:p> che contiene end_text"""
    i=xml.find(esc(start_text)); assert i>0,start_text
    a=xml.rfind('<w:p ',0,i)
    j=xml.find(esc(end_text),a); assert j>0,end_text
    b=xml.find('</w:p>',j)+6
    return a,b

# ============ 1. §4.2bis: heading + primi paragrafi ============
rep("4.2bis Crescita endogena, R&amp;D e upgrade produttivo perduto".replace("&amp;","&"),
    "4.2bis R&D, produttività e distribuzione: perché non usiamo la TFP")
rep("Un elemento cruciale del declino italiano 1970–2024 è la stagnazione della crescita della produttività totale dei fattori (TFP), che riflette l'assenza di un upgrade significativo della specializzazione produttiva.",
    "Un elemento cruciale del declino italiano 1970–2024 è il rallentamento della produttività del lavoro, che riflette l'assenza di un upgrade significativo della specializzazione produttiva. Questa sezione documenta i fatti che non dipendono da come si misura la produttività (la spesa in R&D, la composizione dell'export) e spiega perché il paper non utilizza la produttività totale dei fattori come misura del progresso tecnico.")
rep("suggerisce che la TFP è endogenamente determinata dall'investimento pubblico e privato in ricerca e sviluppo (R&D/GDP).",
    "suggerisce che la crescita della produttività è endogenamente determinata dall'investimento pubblico e privato in ricerca e sviluppo (R&D/GDP); questa letteratura la misura come TFP, con i problemi discussi sotto.")
rep("La TFP italiana, calcolata dal residuo di Solow su dati AMECO, è crollata da +0.8% p.a. negli anni Ottanta a praticamente zero post-2000. ",
    "La produttività del lavoro (valore aggiunto reale per occupato, AMECO) rallenta dal 3,1% l'anno degli anni Settanta all'1,8 degli Ottanta, allo 0,8 del 1993-2007 e allo 0,1 del 2014-24. ")
rep("Questa stagnazione della TFP coesiste","Questa stagnazione coesiste")

# ============ 2. sposta regressione R&D-TFP in appendice A.7, inserisci blocco identità ============
a,b=para_span("Verifica empirica con dati reali (panel 13 paesi OECD, 1996–2022).","Una specifica ARDL-PMG (Pesaran-Shin 1999)")
moved=xml[a:b]
rows=[["Periodo","\"TFP\" (residuo di Solow)","= ω·ŵ","+ (1−ω)·r̂","ŵ reale","r̂","ω media"],
      ["1970-79","2,36","2,51","−0,16","3,63","−0,50","69,4"],
      ["1980-92","0,47","0,48","−0,01","0,73","−0,05","65,6"],
      ["1993-2007","0,10","0,00","0,10","0,00","0,27","60,0"],
      ["2008-13","−1,30","−0,32","−0,98","−0,52","−2,52","61,3"],
      ["2014-24","0,46","−0,16","0,62","−0,27","1,55","59,6"],
      ["1996-2019","−0,31","−0,09","−0,22","−0,14","−0,55","60,3"]]
ident = heading("La TFP come identità distributiva",3) \
+ para("La misura standard del progresso tecnico, la produttività totale dei fattori, è il residuo di Solow: la parte della crescita del prodotto non spiegata dalla crescita ponderata di lavoro e capitale. La critica di Cambridge alla funzione di produzione aggregata (Robinson 1953; Sraffa 1960; Pasinetti 1959; Garegnani 1970; Harcourt 1972) ha una conseguenza empirica precisa, formalizzata da Shaikh (1974), Rymes (1971) e Felipe e McCombie (2014, 2020): poiché i dati di contabilità nazionale soddisfano per costruzione l'identità Y ≡ wL + rK (prodotto uguale a monte salari più profitti), la crescita del residuo di Solow è anch'essa un'identità, TFP̂ ≡ ω·ŵ + (1−ω)·r̂, cioè la media ponderata della crescita del salario reale e del saggio di profitto, con pesi pari alle quote distributive. Non misura la tecnologia: misura la distribuzione. Nelle parole di Halevi (2025), la funzione di produzione aggregata «non riesce nemmeno a qualificarsi come errata poiché è semplicemente vuota: non ha contenuto empirico falsificabile, perché è tautologica».") \
+ para("La tabella verifica l'identità sui dati del paper. Il residuo di Solow è calcolato su AMECO con valore aggiunto a costo dei fattori in termini reali, occupati totali (NETD), stock netto di capitale a prezzi 2020 (OKND), quota lavoro aggiustata per gli autonomi (ALCD0) e pesi di Törnqvist; il lato distributivo usa il salario reale aggiustato per occupato e il saggio di profitto sul capitale reale, con la stessa deflazione. Lo scarto massimo fra le due colonne su 64 anni è dell'ordine di 10⁻⁵, l'approssimazione discreta dell'identità continua. Medie annue in punti percentuali.") \
+ table(rows,[1100,1500,1000,1200,1000,900,1000]) \
+ note("Note: elaborazione su AMECO (Autumn Forecast 2025), Italia. ω = quota lavoro aggiustata a costo dei fattori; ŵ = crescita del salario reale aggiustato per occupato; r̂ = crescita del saggio di profitto lordo sul capitale netto reale. Per confronto, Penn World Table 10.0 (rtfpna, che usa ore e capitale umano) dà −0,63 per il 1996-2019: stesso segno, stessa lettura.") \
+ para("La lettura è immediata. Negli anni Settanta la \"TFP\" cresce del 2,4% l'anno perché il salario reale cresce del 3,6%; dal 1993 al 2007 è ferma perché il salario reale aggiustato per occupato è esattamente fermo (0,00) e il saggio di profitto cresce poco; nel 2008-13 crolla perché crolla il saggio di profitto; il \"recupero di produttività\" del 2014-24 è interamente recupero del saggio di profitto (+1,55% l'anno) con salari reali in calo. Il rallentamento della produttività italiana misurato con la TFP è la stagnazione salariale, per identità. Per questo il paper non presenta la TFP come risultato: sarebbe un conteggio doppio dei risultati distributivi dei capitoli 3, 5 e 6 (compressione di ω, dinamica di r). Ne segue anche che una regressione della crescita della TFP sull'intensità di R&D — che una versione precedente del paper riportava fra i risultati principali, e che è ora in Appendice A.7 come esercizio nella grammatica mainstream — regredisce l'R&D su una combinazione di crescita dei salari reali e dei profitti: il \"residuo italiano\" di quella regressione dice che in Italia i salari sono cresciuti meno di quanto il suo R&D avrebbe previsto, che è un'altra cosa da un deficit tecnologico.") \
+ para("Una seconda cautela, di Pasinetti (1959, 1981) e ripresa in Gaddi, Garbellini e Oro (2025), riguarda la stessa produttività del lavoro in termini di valore aggiunto reale: il valore aggiunto reale ha un referente fisico solo in un'economia a un bene, e a livello settoriale, con doppia deflazione e cambiamento strutturale, misura la capacità di valorizzazione del settore verticalmente integrato, non un volume. Il paper usa quindi la produttività del lavoro reale (OVGD/NETD) solo come indice descrittivo aggregato per l'Italia nel tempo, non come misura dell'efficienza fisica, e ne affida la spiegazione all'equazione di produttività di Sylos Labini in §6.3, che non richiede una funzione di produzione.")
xml = xml[:a] + ident + xml[b:]

# ============ 3. Appendice A.7 prima di Bibliografia ============
i=xml.find('Bibliografia essenziale'); pb=xml.rfind('<w:p ',0,i)
a7 = heading("A.7 Regressione cross-country R&D–TFP (esercizio riportato per confronto)",2) \
+ para("Avvertenza. Il materiale che segue era, in una versione precedente del paper, parte di §4.2bis e uno dei risultati principali. È conservato in appendice per trasparenza e per confronto con la letteratura che lo usa, ma non entra nei risultati del paper, per la ragione esposta in §4.2bis: la crescita della TFP è identicamente ω·ŵ + (1−ω)·r̂ (Felipe e McCombie 2014, 2020), quindi la regressione stima un'associazione fra R&D e una combinazione di crescita dei salari reali e dei profitti, non fra R&D e progresso tecnico. I fatti descrittivi sull'intensità di R&D e sulla composizione dell'export, che non dipendono da questa misura, restano in §4.2bis e §5bis.","") \
+ moved
xml = xml[:pb] + a7 + xml[pb:]

# ============ 4. §6.3: numeri + nuova 6.3.1 Sylos Labini ============
rep("Nei dati AMECO che utilizziamo, g_LP medio del decennio 1996-2007 è 0.21% annuo, contro 2.96% del decennio 1970-79 e 1.70% del decennio 1980-89.",
    "Nei dati AMECO che utilizziamo (valore aggiunto reale per occupato, vintage Autumn Forecast 2025), g_LP medio del 1996-2007 è 0,3% annuo, contro 3,1% del decennio 1970-79 e 1,8% del decennio 1980-89.")
srows=[["Campione","n","Coeff. su g_Y (produttività)","Elasticità occupazione/prodotto","Effetto Ricardo (ŵ − p̂_I)₋₁","R²"],
       ["1961-2024","63","0,84 (0,04)","0,16 (0,04)","+0,15 (0,04), p<0,001","0,88"],
       ["1961-1992","31","0,93 (0,08)","0,07 (0,08)","+0,13 (0,03), p<0,001","0,89"],
       ["1993-2024","32","0,75 (0,04)","0,25 (0,04)","−0,07 (0,09), p=0,47","0,81"],
       ["1993-2007","15","0,57 (0,30)","0,43 (0,30)","+0,18 (0,09), p=0,054","0,24"]]
sylos = heading("6.3.1 L'equazione di produttività di Sylos Labini",3) \
+ para("Il quadro teorico del paper contiene già la spiegazione del puzzle, ma in forma discorsiva. Sylos Labini (1984, 1993) la scrisse come equazione: la crescita della produttività del lavoro dipende dalla crescita della domanda (effetto Smith, che è la legge di Kaldor-Verdoorn: Verdoorn 1949, Kaldor 1966) e dalla crescita del salario rispetto al prezzo dei beni d'investimento (effetto Ricardo: salari che crescono più delle macchine inducono meccanizzazione). È un'equazione cambridgiana nel senso di Kaldor, non usa funzioni di produzione, e inverte la freccia causale della vulgata contestata in Gaddi, Garbellini e Oro (2025): non «la produttività è ferma, quindi i salari vanno moderati», ma «i salari sono fermi, quindi la produttività è ferma». La stimiamo su AMECO 1961-2024, g_LP = a + b·g_Y + c·(ŵ − p̂_I)₋₁, con g_LP crescita del valore aggiunto reale per occupato, g_Y crescita del PIL reale, ŵ crescita della retribuzione nominale per dipendente, p̂_I crescita del deflatore degli investimenti, errori HAC (Newey-West, 3 ritardi). Poiché g_LP = g_Y − g_L, la regressione della produttività sul prodotto ha una componente meccanica (Rowthorn 1975); riportiamo perciò anche l'elasticità dell'occupazione al prodotto, 1 − b, che è la forma pulita della legge di Verdoorn.") \
+ table(srows,[1100,500,1700,1800,2100,700]) \
+ note("Note: elaborazione su AMECO (Autumn Forecast 2025), Italia. Errori standard HAC fra parentesi. L'elasticità dell'occupazione è stimata direttamente regredendo g_L sugli stessi regressori. Medie di periodo dei regressori: g_Y 3,7 (1970-79), 2,1 (1980-92), 1,5 (1993-2007), −1,5 (2008-13), 1,0 (2014-24); (ŵ − p̂_I) 2,0; 1,1; 0,3; −0,5; 0,2.") \
+ para("Due fatti stilizzati. Primo, dopo il 1993 la crescita diventa labour-intensive: l'elasticità dell'occupazione al prodotto passa da 0,07 (1961-92) a 0,25 (1993-2024) e a 0,43 nel 1993-2007, gli anni del pacchetto Treu e della legge Biagi; a parità di crescita del prodotto, una quota maggiore si traduce in occupazione a bassa produttività e una minore in produttività. È la tesi di Saltari e Travaglini (2009), con un numero. Secondo, l'effetto Ricardo, forte e significativo fino al 1992 (+0,13, p<0,001), scompare dopo: il coefficiente diventa nullo e, soprattutto, la variabile stessa si azzera, perché il salario relativo al prezzo dei beni d'investimento, che cresceva del 2% l'anno negli anni Settanta, cresce dello 0,3 nel 1993-2007 e dello 0,2 nel 2014-24. Senza pressione salariale non c'è incentivo a meccanizzare. Nel sotto-periodo 1993-2007 il coefficiente resta positivo ma al margine della significatività (p=0,054, n=15): il canale non è morto, è fermo per mancanza di input.") \
+ para("Questa è, in un'equazione, l'interpretazione avanzata sopra: la compressione salariale del regime post-Maastricht non è la risposta a una produttività ferma, ne è una causa. Il risultato è coerente con l'identità di §4.2bis, con il modello di Goodwin di §8.1, in cui α (la crescita della produttività) non è un parametro esogeno ma dipende da ω, e con la riformulazione di §6bis.6: un capitalismo che realizza profitti senza accumulare non ha bisogno di produttività, e un regime salariale che non preme sulle imprese non la produce.")
i=xml.find('6bis. Privatizzazioni, quota salari e quasi-rendite'); pb=xml.rfind('<w:p ',0,i)
xml = xml[:pb] + sylos + xml[pb:]

# ============ 5. propagazione ============
rep("(5) Una regressione cross-sectional su 13 paesi OCSE avanzati (1996–2019) mostra un'associazione tra intensità di R&D e crescita della TFP pari a +0,44 punti percentuali di TFP growth per 1 punto percentuale di R&D/PIL (R²=0,69; p=0,0004), senza interpretazione causale stringente dato il numero ridotto di paesi e il rischio di omitted variables. L'Italia sottoperforma questa relazione di −0,42 punti percentuali annui anche controllando per il basso livello di R&D e registra la flessione della TFP più marcata del campione (−13,1% nel 1995–2019; unica altra in calo è la Spagna, ma con intensità inferiore: −5,8%). La quota di export",
    "(5) Il paper non usa la produttività totale dei fattori come misura del progresso tecnico: seguendo la critica di Cambridge (Pasinetti; Felipe e McCombie), mostriamo sui dati AMECO che la crescita del residuo di Solow è identicamente ω·ŵ + (1−ω)·r̂, e che la \"stagnazione della TFP\" italiana dal 1993 è la stagnazione del salario reale (0,00% l'anno nel 1993-2007) per identità, mentre il suo recupero post-2014 è interamente recupero del saggio di profitto. Il puzzle della produttività è spiegato con l'equazione di Sylos Labini: dopo il 1992 l'effetto Ricardo (salari rispetto al prezzo dei beni d'investimento) scompare e l'elasticità dell'occupazione al prodotto sale da 0,07 a 0,25, cioè la crescita diventa labour-intensive. La compressione salariale non è la risposta alla produttività ferma: ne è una causa. La quota di export")
rep("(5) A cross-sectional regression on 13 advanced OECD countries (1996–2019) shows an association between R&D intensity and TFP growth equal to +0.44 percentage points of TFP growth per 1 percentage point of R&D/GDP (R²=0.69; p=0.0004), without strict causal interpretation given the limited number of countries and the risk of omitted variables. Italy underperforms this relationship by −0.42 percentage points per year even controlling for low R&D, and registers the steepest TFP decline in the sample (−13.1% over 1995–2019; the only other country in decline is Spain, but at a lower intensity: −5.8%). The Italian high-tech export share",
    "(5) The paper does not use total factor productivity as a measure of technical progress: following the Cambridge critique (Pasinetti; Felipe and McCombie), we show on AMECO data that Solow-residual growth is identically ω·ŵ + (1−ω)·r̂, and that the Italian \"TFP stagnation\" since 1993 is real-wage stagnation (0.00% per year in 1993-2007) by identity, while its post-2014 recovery is entirely a recovery of the profit rate. The productivity puzzle is explained with Sylos Labini's productivity equation: after 1992 the Ricardo effect (wages relative to the price of investment goods) disappears and the employment elasticity to output rises from 0.07 to 0.25, i.e. growth becomes labour-intensive. Wage compression is not the response to stagnant productivity: it is one of its causes. The Italian high-tech export share")
rep("Penn World Tables 10.0 (TFP), World Bank (R&D, high-tech export)","World Bank (R&D, high-tech export)")
rep("Penn World Tables 10.0 (TFP), World Bank (R&D, high-tech exports)","World Bank (R&D, high-tech exports)")
rep("infine, stimiamo una regressione cross-country della crescita della TFP sull'intensità di R&D per documentare l'anomalia italiana.",
    "infine, verifichiamo sui dati AMECO l'identità distributiva della TFP e stimiamo l'equazione di produttività di Sylos Labini.")
rep("Finally, we estimate a cross-country regression of TFP growth on R&D intensity to document the Italian anomaly.",
    "Finally, we verify on AMECO data the distributive identity of TFP and estimate Sylos Labini's productivity equation.")
rep("La TFP nei settori low-tech italiani stagna, mentre in altri paesi cresce anche nei settori low-tech (per effetto di esternalità e tecnologie trasversali)",
    "La produttività del lavoro nei settori low-tech italiani stagna, mentre in altri paesi cresce anche nei settori low-tech (per effetto di esternalità e tecnologie trasversali)")
rep("L'elasticità export-TFP è bassa per l'Italia, specialmente nel low-tech (debole connessione tra produttività e export competitività)",
    "L'elasticità export-produttività è bassa per l'Italia, specialmente nel low-tech (debole connessione tra produttività e export competitività)")
rep("Il costo unitario del lavoro cala, ma la TFP non aumenta, per cui la competitività export rimane fragile",
    "Il costo unitario del lavoro cala, ma la produttività del lavoro non aumenta, per cui la competitività export rimane fragile")
rep("TFP che NON aumenta nei settori privatizzati (fallimento dell'upgrade tecnologico promesso)",
    "Produttività del lavoro che NON aumenta nei settori privatizzati (fallimento dell'upgrade tecnologico promesso)")
rep("TFP (assenza di upgrade): ","Produttività (assenza di upgrade): ")
rep("La TFP nei settori privatizzati post-1992 è 0.0143, sostanzialmente analoga a quella pre-1992 (0.0131, Δ +0.0012 ≈ 0%). Nel complesso delle economie sviluppate, la TFP dei settori privatizzati cresce tipicamente di 0.3-0.5 punti percentuali al decennio. L'assenza di aumento di TFP italiano è coerente con la diagnosi di Modiano-Onado di un upgrade promesso e mancato.",
    "la versione preliminare usava una misura settoriale di TFP calcolata sui dati simulati; alla luce di §4.2bis quella misura non è utilizzata nella versione finale. Il punto sostantivo — l'assenza di upgrade produttivo nei settori privatizzati — è ripreso con i dati Eurostat reali in §6bis.3 e con l'equazione di produttività in §6.3.1.")
rep("e la coerenza con il dato sul mark-up e con la stagnazione TFP rendono il risultato","e la coerenza con il dato sul mark-up e con la stagnazione della produttività del lavoro rendono il risultato")
rep("Il residuo negativo dell'Italia nella regressione R&D-TFP di §4.2bis, che sopravvive ai controlli per qualità istituzionale e capitale umano, è la manifestazione aggregata di questo meccanismo di composizione.",
    "La scomparsa dell'effetto Ricardo nell'equazione di produttività di Sylos Labini dopo il 1992 (§6.3.1) — salari che non crescono rispetto al prezzo dei beni d'investimento e produttività che non risponde — è la manifestazione aggregata di questo meccanismo di composizione.")
rep("o alla regressione cross-country R&D-TFP (§4.2bis):","o all'equazione di produttività di Sylos Labini (§6.3.1):")
rep("R&D → TFP cross-country","Produttività: identità della TFP ed equazione di Sylos Labini")
rep("Solido (dati World Bank + PWT 10.0)","Solido (identità contabile su AMECO; equazione stimata 1961-2024)")
rep("Cross-section 13 paesi OECD: associazione +0.44 pp di TFP growth per pp di R&D/PIL </w:t><w:lastRenderedPageBreak/><w:t>(R²=0.69, p=0.0004; non interpretata causalmente per N piccolo + omitted variables). Italia subperforma di −0.42 pp/anno",
    "TFP̂ ≡ ω·ŵ + (1−ω)·r̂ verificata sui dati del paper (scarto 10⁻⁵): la \"TFP\" ferma dal 1993 è il salario reale fermo (0,00). Sylos Labini: effetto Ricardo +0,13 (p<0,001) fino al 1992, nullo dopo; elasticità occupazione/prodotto da 0,07 a 0,25. La regressione R&D→TFP è in Appendice A.7, non fra i risultati")
rep("Italia anomala in TFP","Italia: basso R&D e specializzazione low-tech")
rep("Solido (dati PWT 10.0)","Solido (dati World Bank, OECD MSTI)")
rep("Italia ha il calo TFP più marcato del campione 1995–2019 (−13.1%). Spagna è l'altro paese in calo (−5.8%). Tutti gli altri 11 paesi crescono o stagnano",
    "R&D/PIL fermo intorno all'1% dal 1980; quota di export high-tech la più bassa fra i paesi OCSE avanzati (8,1% nel 2015-22). Fatti descrittivi indipendenti dalla misura della produttività")

# ============ 6. bibliografia ============
def bibp(main, ital, tail):
    L='<w:lang w:val="en-US"/>'
    R=f'<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/>{L}</w:rPr>'
    RI=R.replace('<w:sz','<w:i/><w:iCs/><w:sz')
    return (f'<w:p w:rsidR="007372E6" w:rsidRPr="00202A01" w:rsidRDefault="003C27D6" w:rsidP="00A97429"><w:pPr><w:spacing w:after="120" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/>{R}</w:pPr>'
            f'<w:r>{R}<w:t xml:space="preserve">{esc(main)}</w:t></w:r><w:r>{RI}<w:t xml:space="preserve">{esc(ital)}</w:t></w:r><w:r>{R}<w:t xml:space="preserve">{esc(tail)}</w:t></w:r></w:p>')
def ins_before(marker,block):
    global xml
    i=xml.find(esc(marker)); 
    if i<0: i=xml.find(html.escape(marker,quote=False))
    assert i>0,marker; p=xml.rfind('<w:p ',0,i); xml=xml[:p]+block+xml[p:]
ins_before("Gandolfo, G. (2005)", bibp("Felipe, J., & McCombie, J. S. L. (2014). The aggregate production function: 'not even wrong'. ","Review of Political Economy"," 26(1), 60-84.")
                                 + bibp("Felipe, J., & McCombie, J. S. L. (2020). The illusions of calculating total factor productivity and testing growth models: from Cobb-Douglas to Solow and Romer. ","Journal of Post Keynesian Economics"," 43(3), 470-513.")
                                 + bibp("Gaddi, M., Garbellini, N., & Oro, G. (2025). Produttività e competitività: una critica dei concetti dominanti. In G. Carnevali et al., ","Tornare alla pianificazione. Politiche industriali dopo la globalizzazione"," (pp. 3-23). Milano: Edizioni Punto Rosso.")
                                 + bibp("Garegnani, P. (1970). Heterogeneous capital, the production function and the theory of distribution. ","Review of Economic Studies"," 37(3), 407-436."))
ins_before("Hamilton, J. D. (1989)", bibp("Halevi, J. (2025). Osservazioni conclusive. In G. Carnevali et al., ","Tornare alla pianificazione. Politiche industriali dopo la globalizzazione"," (pp. 173-186). Milano: Edizioni Punto Rosso.")
                                  + bibp("Harcourt, G. C. (1972). ","Some Cambridge Controversies in the Theory of Capital",". Cambridge: Cambridge University Press."))
ins_before("Killick, R., Fearnhead, P.", bibp("Kaldor, N. (1966). ","Causes of the Slow Rate of Economic Growth of the United Kingdom",". Cambridge: Cambridge University Press."))
ins_before("Pellegrino, B., &amp; Zingales, L. (2017)".replace("&amp;","&"), bibp("Pasinetti, L. L. (1959). On concepts and measures of changes in productivity. ","Review of Economics and Statistics"," 41(3), 270-286.")
                                  + bibp("Pasinetti, L. L. (1981). ","Structural Change and Economic Growth",". Cambridge: Cambridge University Press."))
ins_before("Saraceno, F. (2017)", bibp("Robinson, J. (1953). The production function and the theory of capital. ","Review of Economic Studies"," 21(2), 81-106.")
                                + bibp("Rowthorn, R. E. (1975). What remains of Kaldor's law? ","Economic Journal"," 85(337), 10-19.")
                                + bibp("Rymes, T. K. (1971). ","On Concepts of Capital and Technical Change",". Cambridge: Cambridge University Press."))
ins_before("Sforzi, F. (1990)", bibp("Shaikh, A. (1974). Laws of production and laws of algebra: the humbug production function. ","Review of Economics and Statistics"," 56(1), 115-120."))
ins_before("Torrini, R. (2005)", bibp("Sraffa, P. (1960). ","Produzione di merci a mezzo di merci",". Torino: Einaudi.")
                               + bibp("Sylos Labini, P. (1984). ","Le forze dello sviluppo e del declino",". Roma-Bari: Laterza.")
                               + bibp("Sylos Labini, P. (1993). ","Progresso tecnico e sviluppo ciclico",". Roma-Bari: Laterza."))
ins_before("Zeileis, A., Leisch, F.", bibp("Verdoorn, P. J. (1949). Fattori che regolano lo sviluppo della produttività del lavoro. ","L'Industria"," 1, 3-10."))

open(path,'w').write(xml); print("paragrafi:",n0,"->",xml.count('<w:p '))
