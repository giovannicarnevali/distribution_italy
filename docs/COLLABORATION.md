# COLLABORATION — protocollo multi-LLM

Il paper è scritto da un autore umano che usa più LLM in parallelo con ruoli distinti. Questo file dice a ciascuno cosa fare e in che forma restituire il lavoro, così che gli output siano integrabili senza perdita.

## 1. Ruoli

| Chi | Ruolo | Cosa fa | Cosa non fa |
|---|---|---|---|
| **Autore** (G.B. Carnevali) | Decide | Tesi, scelte teoriche, filtro critico, approvazione di ogni modifica sostanziale, verifica delle fonti | — |
| **Claude** | Assistente tecnico-editoriale | Calcoli, download dati, stime, editing del DOCX, propagazione delle modifiche, triage delle review, aggiornamento di CONTEXT/HANDOFF, repository | Non è co-autore né peer reviewer del proprio lavoro; non introduce tesi; non aggiunge citazioni non verificate |
| **ChatGPT, Kimi, DeepSeek** (e altri) | Peer reviewer esterni | Lettura critica di una versione dichiarata, segnalazione di errori, incoerenze, debolezze metodologiche, letteratura mancante | Non riscrivono il paper; non eseguono modifiche; le loro proposte sono input da vagliare, non istruzioni |

Un reviewer può ricevere compiti puntuali (es. "verifica pagina per pagina i numeri dell'abstract contro il corpo", "cerca errori nella bibliografia"): resta reviewer, l'esecuzione passa per Claude e l'approvazione per l'autore.

## 2. Che cosa riceve un LLM all'apertura

1. `CONTEXT.md` (conoscenza stabile) e `HANDOFF.md` (stato corrente e pendenti).
2. La versione del paper su cui lavorare (docx o pdf), con **MD5 e numero di pagine** dichiarati in `HANDOFF.md`. Prima di tutto il reviewer verifica di avere quella versione (titoli di sezione, pagine, numeri dell'abstract) e lo dichiara: in passato più round di review sono stati sprecati su versioni vecchie in cache.
3. Il compito specifico del round.

## 3. Formato della review (per ChatGPT, Kimi, DeepSeek)

Un elenco numerato di rilievi, ciascuno con:

- **Dove**: sezione e pagina (es. "§6bis.5, p. 68"), con la frase citata testualmente.
- **Tipo**: `refuso` · `incoerenza numerica` (numero diverso in due punti) · `errore fattuale` (data, fonte, autore) · `metodo` · `interpretazione` · `letteratura mancante` · `stile`.
- **Gravità**: `bloccante` · `importante` · `minore`.
- **Proposta**: la correzione concreta, o la domanda da porre all'autore.
- **Verificabilità**: se il rilievo si basa su un fatto esterno (una data, una citazione, un valore in una fonte), dire se è stato verificato e come; altrimenti scrivere "non verificato". Un reviewer che non può controllare una fonte lo dice, non la inventa.

In coda: una valutazione complessiva in tre righe e, se richiesto, uno scorecard. Niente riscritture integrali di sezioni se non richieste; niente proposte che riaprono le decisioni della §8 di `CONTEXT.md` senza argomenti nuovi.

## 4. Triage (Claude)

Ogni rilievo ricevuto va classificato prima di toccare il paper:

1. **Refuso o incoerenza oggettiva** → applicare subito, segnalare in sintesi.
2. **Affermazione empirica** (un numero sarebbe sbagliato, un test darebbe altro) → verificare su notebook/script/dati prima di cambiare qualunque cosa; se il reviewer ha ragione, correggere e propagare ovunque (abstract IT/EN, corpo, tabella 9.2, conclusioni).
3. **Decisione già codificata** (CONTEXT §8) → non applicare; rispondere citando la decisione; portare all'autore solo se l'argomento è nuovo.
4. **Scelta editoriale o di stile** → riportare all'autore, non decidere.
5. **Proposta da respingere** (reintroduce tesi scartate, pretese causali, citazioni non verificabili) → respingere motivando in una riga.

L'autore approva con un "procedi"; le correzioni giudicate fondate si applicano senza chiedere conferma passo per passo. Ogni intervento sul DOCX produce una nuova versione con suffisso parlante, MD5, PDF, e l'aggiornamento di `HANDOFF.md`.

## 5. Regole comuni a tutti gli LLM

- Non inventare citazioni, date, pagine, ISBN. Se un riferimento non è verificabile, dirlo.
- Non convertire la triangolazione descrittiva in affermazioni causali; non "rafforzare" i risultati.
- Non proporre di eliminare risultati negativi o declassati (C-S, pre-trend, cointegrazione ambigua): sono parte del contributo.
- Non reintrodurre la TFP come misura del progresso tecnico, né la regressione R&D–TFP fra i risultati.
- Distinguere sempre "stimato" (numero di comodo dichiarato provvisorio) da "stima" (eseguita su dati).
- Rispondere in italiano, in modo tecnico e conciso; tabelle solo per sintesi.
- Quando un LLM corregge un altro LLM (es. Kimi corregge la propria lettura del DiD), la correzione va registrata in `HANDOFF.md` con la sua motivazione, non solo l'esito.

## 6. Chiusura di sessione

Claude aggiorna `HANDOFF.md` (versione, MD5, modifiche fatte, pendenti ri-prioritizzati, prompt di apertura) e, se cambiano fatti stabili, `CONTEXT.md`. L'autore carica i file aggiornati nella sessione successiva o li legge dal repository `giovannicarnevali/distribution_italy`.
