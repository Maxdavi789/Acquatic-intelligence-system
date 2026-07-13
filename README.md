# Acquatic Intelligence System

Proof of Concept locale per un AI Swimming Motion Analyzer a secco.

## Obiettivo

Il progetto valida a costo zero una pipeline offline di Computer Vision che
analizza un video laterale di movimenti natatori simulati a secco. MediaPipe
fornisce i landmark corporei; il motore deterministico calcola angolo del
gomito, conteggio delle bracciate e regolarita' del ritmo.

Il PoC dimostra la fattibilita' software e algoritmica. Non dimostra validita'
biomeccanica in acqua e non equivale a un sistema professionale da laboratorio.
La specifica di riferimento e' [`spec.txt`](spec.txt), versione 1.1 congelata.

## Input e output MVP

- Input primario: file MP4 laterale (profilo 90 gradi).
- Input secondario: webcam, modalita' sperimentale/best-effort.
- Output previsto: video annotato, angolo gomito live, bracciate totali,
  Fluidity Score, grafico Y del polso ed export CSV della sessione.
- Esecuzione: interamente locale, senza API o servizi a pagamento.

## Stack

- Python 3.11 come riferimento di specifica; ambiente locale validato anche con
  Python 3.12.10.
- OpenCV contrib `4.11.0.86` (include il namespace `cv2` completo).
- MediaPipe Pose legacy, pinnato a `mediapipe==0.10.21`.
- Streamlit.
- NumPy `1.26.4`, protobuf `4.25.9` e Pandas.
- CSV locale per l'export delle sessioni.

`matplotlib` non e' una dipendenza diretta del progetto: viene installato
transitivamente da MediaPipe. I grafici della dashboard useranno
`st.line_chart`.

## Stato

Aggiornato al 2026-07-13.

- M0/T01-T06: completata. T03 e' stata validata sul video dryland provvisorio:
  448/448 frame con posa, arto selezionato affidabile nel 100% dei frame e
  chiusura `q` pulita. La webcam best-effort e' stata tentata ma su questa
  macchina non e' presente alcuna camera (INC-010).
- M1/T07-T12: completata; suite sintetica corrente 23/23 verde, inclusa la
  regressione sul gate spalla stretto di T10.
- M2/T13-T14: completata. `analyze_frame` e' collegata ai landmark reali dallo
  script CLI `scripts/analyze_video.py`: sul video provvisorio 448/448 frame
  con posa, angolo in [4,40; 179,92] e conteggio finale 2.
- M3/T15-T22: completata. La dashboard Streamlit ha selettore input (MP4
  primario, webcam sperimentale), video annotato con scheletro e angolo del
  gomito live, KPI reali (bracciate totali e Fluidity Score), grafico
  dell'onda Y del polso popolato durante l'elaborazione e risultati che
  sopravvivono ai rerun dell'interfaccia. Sul video provvisorio: conteggio
  finale 2, coerente con le bracciate visibili.
- M4/T23-T25: completata. Il pulsante "Termina Sessione ed Esporta Dati"
  aggrega timestamp, bracciate totali, Fluidity Score e angolo medio/max in
  un DataFrame con preview e lo accoda a `data/sessions.csv` (header alla
  prima scrittura, append mai distruttivo). Verifica privacy passata: in
  `data/` restano solo metriche aggregate anonime, nessun frame o video.
- M5/T26-T29: completata. Robustezza verificata: occlusioni senza picchi
  spuri ne' crash (limite documentato INC-011: possibile sottostima dopo
  occlusioni prolungate, mai sovrastima), errori di sorgente gestiti con
  messaggi leggibili, anteprima webcam sperimentale a durata limitata con
  degrado documentato, risorse rilasciate anche su stop a meta'.
- M6/T30-T33: completata. Sul video ufficiale: conteggio manuale 10 vs
  automatico 10 (differenza 0) e riproducibilita' bit-identica tra run.
- M7/T34-T36: completata in deroga DA-05 (dettagli in SPEC_ERRATA.md):
  il video ufficiale e' una clip stock con licenza Pexels, versionata come
  `test_videos/profilo_test.mp4`. Validazione completa: 175/175 frame con
  posa, 10 bracciate ritmiche, Fluidity Score 93,1, export CSV verificato.
- M8: da iniziare (README finale, screenshot, slide pitch, rehearsal).

La prossima task in ordine e' T37 (modulo M8): revisione finale del README.

Lo stato task per task e' in [`breakdown_status.md`](breakdown_status.md).

## Avvio e validazione

```powershell
.\venv\Scripts\python.exe scripts\test_metrics.py
.\venv\Scripts\python.exe vision_tracker.py --source <clip>.mp4
.\venv\Scripts\python.exe scripts\analyze_video.py --source <clip>.mp4
```

Lo scaffold della dashboard e' avviabile con:

```powershell
.\venv\Scripts\python.exe -m streamlit run app.py
```

I test formali di validazione sul video provvisorio sono documentati in
`incidents.md` e `breakdown_status.md` (modulo M6); la validazione finale
avverra' sul video ufficiale del sandbox (T35-T36).

Il video ufficiale di riferimento e' `test_videos/profilo_test.mp4` (clip con
licenza Pexels, fonte e hash in `SPEC_ERRATA.md`), versionato nella repo: dopo
il clone la demo funziona subito. Il vecchio campione provvisorio
`profilo_provvisorio.mp4` (terzi, non licenziato) resta solo locale e non
tracciato.

## Struttura principale

```text
.
+-- app.py
+-- vision_tracker.py
+-- metrics_engine.py
+-- scripts/test_metrics.py
+-- scripts/analyze_video.py
+-- requirements.txt
+-- spec.txt
+-- SPEC_ERRATA.md
+-- data/
+-- test_videos/
+-- breakdown_status.md
+-- prompt_log.md
+-- incidents.md
+-- HANDOFF.md
```

## Privacy e disclaimer

I frame e i video non vengono persistiti dall'MVP; vengono salvate solo
metriche aggregate nel CSV locale. Eventuali persone riprese devono essere
consenzienti e i video di terzi richiedono una licenza/base d'uso adeguata.

**Questo progetto non e' un dispositivo medico e non fornisce consigli clinici
o di prevenzione degli infortuni.**

## Governance operativa

- `breakdown_status.md`: avanzamento rispetto alle task T01-T41.
- `prompt_log.md`: iterazioni, richieste, azioni ed esiti.
- `incidents.md`: incidenti reali, impatto, mitigazioni e stato.
- `SPEC_ERRATA.md`: modifiche successive al congelamento della specifica.

Questo e' un aggiornamento intermedio di coerenza. La revisione conclusiva del
README resta prevista nel task T37, dopo la validazione end-to-end.
