Script che hanno prodotto le versioni v22, v23 e v23b del DOCX a partire dalla versione precedente (modifica diretta di `word/document.xml`).
Pipeline: `unzip` → `merge_runs.py` → `python build_vXX.py u/word/document.xml [...]` → `zip -X` → validazione OOXML → `soffice --convert-to pdf`.
Servono solo per tracciare esattamente quali frasi sono state cambiate in ogni versione; non vanno rieseguiti.
