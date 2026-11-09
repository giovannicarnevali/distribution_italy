# CLAUDE.md — distribution_italy

Working paper "Le lotte di classe in Italia. Fasi del declino italiano 1980–2024" di Giovanni Battista Carnevali.

All'apertura leggi, in quest'ordine: `docs/CONTEXT.md` (tesi, risultati, decisioni chiuse), `docs/HANDOFF.md` (versione corrente, pendenti), `docs/COLLABORATION.md` (ruoli e triage). Il tuo ruolo è tecnico-editoriale: calcoli, dati, editing del DOCX, triage delle review esterne, aggiornamento dei file in `docs/`. Le decisioni teoriche e il filtro critico sono dell'autore; le correzioni fondate si applicano senza chiedere conferma passo per passo; nessuna citazione viene aggiunta senza fonte verificata.

Prima di lavorare sul paper verifica MD5 e pagine della versione in `paper/` contro `docs/HANDOFF.md`. Ogni nuova versione: suffisso parlante, PDF, MD5, aggiornamento di `docs/HANDOFF.md`. Dati e script di replica vanno in `data/` e `scripts/`, non solo nei messaggi. Il notebook finale è `notebooks/Marx_Schumpeter_Italia_v12_robustness.ipynb`; le versioni precedenti sono archivio, non fonte dei numeri correnti.

Toolchain DOCX in questo ambiente: `unzip` → `python3 /mnt/skills/public/docx/scripts/merge_runs.py` → edit di `word/document.xml` → `zip -X` → `validate.py --original` → `soffice --convert-to pdf` → `pdftotext` per verificare che le sostituzioni siano avvenute. `pip install statsmodels` in ogni nuovo container. AMECO via DBnomics è raggiungibile.

Commit e push solo su richiesta dell'autore.
