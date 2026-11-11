import re, html, sys
p=sys.argv[1]; x=open(p,encoding='utf8').read()
def esc(s): return html.escape(s, quote=False).replace("'", "&apos;")
def rep(old,new,n=1):
    global x
    for o in (esc(old), html.escape(old,quote=False), old):
        if x.count(o)==n: x=x.replace(o,esc(new)); return
    raise AssertionError((old[:70], x.count(esc(old))))
rep("è rimasta inferiore a quella della Spagna e della Francia","è rimasta inferiore a quella della Francia e della Germania e in linea con quella della Spagna (Tabella 5bis.1)")
rep("Prima di Modiano e Onado, e con gli strumenti della contabilità settoriale, Torrini (2005) aveva già documentato il meccanismo.","Prima di Modiano e Onado, e con gli strumenti della contabilità settoriale, Torrini (2005) aveva già documentato il meccanismo (le citazioni che seguono sono dall'edizione italiana, Banca d'Italia, Temi di discussione n. 551, a cui si riferiscono i numeri di pagina; il lavoro è uscito anche come CEP Discussion Paper n. 671 della LSE, con impaginazione diversa).")
rep("dei 17 test significativi al 5% sui p-value raw,","dei 17 test significativi al 5% sui p-value raw (p < 0,05 in senso stretto; X/Y-1992, con p = 0,05, è escluso),")
rep("agroalimentare, metalli: dal 14,6 al 18,7%).","agroalimentare, metalli: dal 14,5 al 18,7%, per differenza dalla Tabella 5bis.1).")
rep("e pari a quello del Portogallo (28,1)","e prossimo a quello del Portogallo (28,1)")
rep("il Portogallo resta sotto (6,18%). Ovvero:","il Portogallo resta sotto (6,18%). I livelli non sono confrontabili con quelli della Tabella 5bis.1 (Italia 13,0% high-tech su Comtrade/Lall): la tassonomia di Lall include fra i prodotti high-tech voci — apparecchiature elettriche, strumenti, parte dei macchinari — che la definizione World Bank/OCSE, basata sull'intensità di ricerca dei prodotti, esclude; le graduatorie fra paesi sono invece coerenti nei due indicatori. Ovvero:")
rep("In G. Carnevali et al., ","In G. Carnevali, G. Cucignatto, L. Esposito, M. Gaddi, N. Garbellini, J. Halevi, R. Lampa, G. Oro & P. Polidori, ",2)
rep("Modiano-Onado concludono che ","Modiano e Onado concludono, con le parole già citate in §4.2bis, che ")
rep("transizioni progresssive","transizioni progressive")
rep("Questi effetti sono persistenti (durare per 20+ anni)","Questi effetti sono persistenti (della durata di oltre vent'anni)")
rep("Questo è il risultato robust principale:","Questo è il principale risultato di robustezza:")
rep("Synthetic Control Method, Difference-in-Differences, PELT","Synthetic Control Method, PELT",2)
# ===================== separatore decimale =====================
paras=list(re.finditer(r'<w:p[ >].*?</w:p>',x,flags=re.S))
def ptext(s): return html.unescape(''.join(re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>',s,flags=re.S)))
T=[ptext(m.group(0)) for m in paras]
i_en0=[i for i,t in enumerate(T) if t.startswith('Abstract (English)')][0]; i_en1=[i for i,t in enumerate(T) if t.startswith('JEL codes')][0]
EXCL=re.compile(r'(Tabella|Tabelle|Figura|Figure|Fig\.|Appendice|Sezione|sezione|Capitolo|capitolo|par\.|Python|Table|Rev\.|Industria|Industry|export-led|versione|version|statsmodels|linearmodels|SciPy|scipy|pandas|numpy|ruptures)\s*$|§\s*$|[A-Za-z_]$')
num=re.compile(r'(?<![\w.,])(\d+)\.(\d+)(?![\w.])')
count=0; skipped=[]
def conv(txt):
    global count
    out=[]; last=0
    for m in num.finditer(txt):
        a,b=m.group(1),m.group(2); pre=txt[:m.start()]
        if EXCL.search(pre[-16:]) or (len(b)==3 and b=='000' and len(a)>=2):
            skipped.append(txt[max(0,m.start()-25):m.end()+5]); continue
        out.append(txt[last:m.start()]); out.append(a+','+b); last=m.end(); count+=1
    out.append(txt[last:]); return ''.join(out)
pieces=[]; last=0
for i,m in enumerate(paras):
    s=m.group(0)
    if i_en0<=i<=i_en1 or '<w:pStyle w:val="Heading' in s or 'http' in s or 'db.nomics' in s or 'github' in s.lower(): continue
    s2=re.sub(r'(<w:t(?: [^>]*)?>)(.*?)(</w:t>)',lambda mt: mt.group(1)+esc(conv(html.unescape(mt.group(2))))+mt.group(3),s,flags=re.S)
    if s2!=s: pieces.append(x[last:m.start()]); pieces.append(s2); last=m.end()
pieces.append(x[last:]); x=''.join(pieces)
open(p,'w',encoding='utf8').write(x)
print('conversioni',count,'| esclusi',len(skipped)); print('\n'.join(sorted(set(skipped))))
