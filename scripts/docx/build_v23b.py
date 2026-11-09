import re, html, sys
path=sys.argv[1]; xml=open(path,encoding='utf8').read(); n0=xml.count('<w:p ')
def esc(s): return html.escape(s, quote=False).replace("'", "&apos;")
def find(old,count=1):
    for o in (esc(old), html.escape(old,quote=False), old.replace('&','&amp;').replace('&amp;amp;','&amp;'), old):
        if xml.count(o)==count: return o
    raise AssertionError((old[:80], xml.count(esc(old))))
def rep(old,new,count=1):
    global xml
    o=find(old,count); xml=xml.replace(o,esc(new))

# A1 Comtrade: formulazioni coerenti con la tabella
rep("la quota low-tech dell'export manifatturiero italiano resta doppia rispetto a Germania e Francia.","la quota low-tech dell'export manifatturiero italiano resta quasi doppia rispetto alla Germania e superiore di oltre la metà a quella francese.")
rep("the low-tech share of Italian manufactured exports remains twice that of Germany and France.","the low-tech share of Italian manufactured exports remains almost twice Germany's and more than half again France's.")
rep("ma resta a un livello doppio rispetto a Germania (13,7) e Francia (17,1) e pari a quello del Portogallo; la quota high-tech sale dal 10,5 al 13,0%, la più bassa del gruppo dopo il Portogallo e appena sopra la Spagna (12,8);",
    "ma resta a un livello quasi doppio rispetto alla Germania (13,7), superiore di oltre la metà a quello della Francia (17,1) e pari a quello del Portogallo (28,1); la quota high-tech sale dal 10,5 al 13,0%, la terza più bassa del gruppo dopo Portogallo (9,0) e Spagna (12,8);")
rep("su Comtrade/Lall la quota low-tech resta doppia rispetto a Germania e Francia","su Comtrade/Lall la quota low-tech resta quasi doppia rispetto alla Germania e superiore di oltre la metà a quella francese")

# A2 titoli SCM
rep("8.6 Causalità di Maastricht-1992: Synthetic Control Method","8.6 La divergenza post-1992 della quota salari: Synthetic Control Method")
rep("Causalità del 1992-93 come pivot","Divergenza post-1992 della quota salari (SCM)")

# A3 Minsky via Bellofiore
rep("(riprendendo Minsky)","(riprendendo Minsky; il riferimento qui è la lettura di Bellofiore e Halevi 2011)")

# A4 unità dell'ATT Callaway-Sant'Anna
rep("dà un ATT di segno opposto (+0,023, IC 95% [+0,003; +0,043]) con pre-trend non piatti","dà un ATT di segno opposto (+2,3 punti percentuali, IC 95% [+0,3; +4,3]) con pre-trend non piatti")
rep("yields an ATT of opposite sign (+0.023, 95% CI [+0.003; +0.043]) with non-flat pre-trends","yields an ATT of opposite sign (+2.3 percentage points, 95% CI [+0.3; +4.3]) with non-flat pre-trends")
rep("L'ATT medio post-trattamento è +0,023 (errore standard 0,010, intervallo al 95% [+0,003; +0,043]) contro −0,151 del TWFE sugli stessi dati; le aggregazioni per coorte (+0,018, non significativa) e dinamica (+0,031) danno lo stesso segno.",
    "L'ATT medio post-trattamento è +0,023, cioè +2,3 punti percentuali di quota salari (errore standard 0,010, intervallo al 95% [+0,3; +4,3] punti) contro −15,1 punti del TWFE staggered sugli stessi dati; le aggregazioni per coorte (+1,8 punti, non significativa) e dinamica (+3,1 punti) danno lo stesso segno.")
rep("un calo a t = 0 (−0,024, significativo) è seguito da un rimbalzo positivo a t = +1 (+0,038) e oltre.","un calo a t = 0 (−2,4 punti, significativo) è seguito da un rimbalzo positivo a t = +1 (+3,8 punti) e oltre.")
rep("TWFE −16.54 pp ma Callaway-Sant'Anna +0.023 con pre-trend non piatti","TWFE −16,54 pp ma Callaway-Sant'Anna +2,3 pp con pre-trend non piatti")
rep("Callaway-Sant'Anna = +0.023 [+0.003; +0.043], pre-trend non piatti","Callaway-Sant'Anna = +2,3 pp [+0,3; +4,3], pre-trend non piatti")

# A5 Figura 7.2: copertura delle serie
rep("Figura 7.2 — Saldi settoriali Italia 1960-2024 (% di PIL): (S-I) settore privato (blu), CA/Y settore estero (rosso), (S-I) nazionale = net lending B9_S1/Y (verde tratteggiato).",
    "Figura 7.2 — Saldi settoriali Italia (% di PIL): CA/Y settore estero (rosso) e net lending nazionale B9_S1/Y (verde tratteggiato), AMECO UBCA e UBLA, 1960-2024; (S-I) settore privato (blu) dal 1995, anno da cui sono disponibili i conti per settore istituzionale (Eurostat nasa_10_nf_tr, cfr. §2.2); prima del 1995 il saldo privato non è mostrato.")
rep("La Figura 7.2 mostra l'evoluzione dei tre saldi nel periodo 1960-2024.","La Figura 7.2 mostra l'evoluzione dei saldi: estero e nazionale dal 1960, privato dal 1995.")

# A6 beta = ore lavorate
rep("α = produttività del lavoro, β = crescita forza lavoro, γ e ρ parametri della curva di Phillips. Il sistema produce orbite chiuse","α = produttività del lavoro, β = crescita dell'input di lavoro (nelle stime, ore lavorate totali, AMECO NLHT, come proxy della forza lavoro), γ e ρ parametri della curva di Phillips. Il sistema produce orbite chiuse")
rep("α = produttività del lavoro, β = crescita forza lavoro, γ e ρ parametri della curva di Phillips lineare.","α = produttività del lavoro, β = crescita dell'input di lavoro (ore lavorate totali, AMECO NLHT), γ e ρ parametri della curva di Phillips lineare.")
rep("β (forza lavoro)","β (ore lavorate, proxy forza lavoro)",2)

# A8 §6bis.2: avvertenza in apertura
rep("Testiamo la tesi di Modiano-Onado usando un Difference-in-Differences (DiD) semplice:","Questa sezione riporta l'esercizio preliminare, condotto su dati settoriali aggregati e in parte simulati prima dell'accesso ai dati Eurostat NACE A64: i suoi numeri sono illustrativi e sono superati dalle stime di §6bis.3-6bis.5, che restano le uniche su dati reali. Testiamo la tesi di Modiano-Onado usando un Difference-in-Differences (DiD) semplice:")

# B numerazione figure/tabelle
rep("Figura 5bis.2 — High-technology export share","Figura 5bis.1 — High-technology export share")
rep("Figura 9.1 — Synthetic Control Method per ω italiana.","Figura 8.2 — Synthetic Control Method per ω italiana.")
rep("Figura 8.7 — SCM leave-one-out.","Figura 8.3 — SCM leave-one-out.")
rep("Figura 4.2bis.1 — R&D investment e TFP growth","Figura A.7.1 — R&D investment e TFP growth")
rep("Tabella 9.2 — Sintesi della rivedibilità","Tabella 9.1 — Sintesi della rivedibilità")

open(path,'w',encoding='utf8').write(xml)
print("paragrafi", n0, "->", xml.count('<w:p '))
