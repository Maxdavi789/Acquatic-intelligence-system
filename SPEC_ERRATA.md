# Spec Errata

Registro delle modifiche e aggiunte alla specifica DOPO il congelamento, come
richiesto dalla spec v1.1 (sezione 16 - Registro versioni) e dalla nota di
processo: "Dopo il congelamento ogni modifica va tracciata in SPEC_ERRATA.md".

Questo file NON e' la specifica: la specifica congelata vive in `spec.txt`.
Qui si annotano baseline, delta e correzioni successive, con data e task ID.

## 2026-07-13 - Baseline: congelamento spec v1.1

- Stato: la specifica di riferimento passa alla versione v1.1 (datata
  02/07/2026), che sostituisce il vecchio `spec.txt` (generazione v0).
- La sostituzione fisica del contenuto di `spec.txt` con la v1.1 e' eseguita
  nel task T01 di questa sessione (vedi breakdown_tasks_v1).
- Il vecchio `spec.txt` resta recuperabile dalla history Git (commit precedenti
  a T01).

### Delta principali v0 (vecchio spec.txt) -> v1.1

1. Symmetry Score bilaterale: RIMOSSO dal perimetro MVP (decisione DA-01 = A).
   Contraddice il vincolo di vista laterale (arto lontano occluso). La funzione
   `calculate_symmetry_score` resta nel codice come airbag NON collegato
   (vedi task T05), riattivabile in v2 con cambio protocollo di ripresa.
2. Obiettivo riformulato in modo onesto (DA-03): il PoC valida la logica
   software e algoritmica, NON la validita' biomeccanica sportiva in acqua.
   Rimosso ogni claim di "equivalenza a laboratorio professionale".
3. Input MP4 dichiarato percorso PRIMARIO; webcam declassata a best-effort
   sperimentale (DA-02), per i limiti di Streamlit sul rendering real-time.
4. Fluidity Score: costante K=50 dichiarata euristica; il punteggio e' un
   indice relativo, non una misura assoluta (DA-04).
5. Contesto strategico aggiunto: il PoC e' la leva per un pitch di
   finanziamento; formalizzato il sandbox di validazione controllato
   (spec v1.1 sezione 3.4) e il criterio di ripetibilita' demo (sezione 1.2).
6. Stack precisato: MediaPipe API legacy con versione PINNATA (DA-06);
   Python 3.11; matplotlib solo se necessario (DA-07); niente SQLite, solo CSV.
7. Contraddizioni interne del vecchio testo (Symmetry "max" vs "media",
   overclaiming): rese irrilevanti perche' la metrica e' fuori scope MVP.

### Delta ambientali rispetto alla spec

- Python di riferimento: la spec fissa 3.11; l'ambiente locale attuale ha sul
  PATH Python 3.12.10. Scelta operativa: venv su 3.12 con fallback a 3.11 se
  MediaPipe legacy risulta incompatibile (vedi incidents.md 2026-07-13).

## Errata successivi

### 2026-07-14 - Hardening riproducibilita' ambiente UI (audit pre-presentazione)

- La spec richiede esplicitamente il pin di MediaPipe (DA-06); l'audit finale
  ha rilevato che le altre due dipendenze applicative dirette, `streamlit` e
  `pandas`, erano ancora flottanti in `requirements.txt`.
- Per rendere ripetibile anche la dashboard/export sulla baseline realmente
  validata vengono fissate le versioni installate e testate:
  `streamlit==1.59.1` e `pandas==3.0.3`.
- Nessuna modifica funzionale o architetturale: il pin documenta l'ambiente con
  cui sono passati suite 23/23, smoke test Streamlit e pipeline ufficiale.
- Corretto inoltre il default di `scripts/analyze_video.py`: ora usa il video
  ufficiale versionato `test_videos/profilo_test.mp4`, non il vecchio file
  provvisorio locale e gitignored.

### 2026-07-14 - Deroga T34/T35 (DA-05, DA-08): video ufficiale da footage con licenza libera

- Contesto: la registrazione in proprio del video di riferimento nel sandbox
  fisico (T34/T35) non e' realizzabile per l'MVP. La spec prevede gia'
  l'alternativa in DA-05 ("dataset open ... con licenza chiara").
- Decisione (approvata dall'utente): il video ufficiale di riferimento e'
  la clip stock Pexels 37264420 ("Workout warm up arm stretch routine
  outdoors"), variante HD 720x1280 25fps, adottata come
  `test_videos/profilo_test.mp4` e VERSIONATA nella repo (1,9 MB).
  - Fonte: https://www.pexels.com/video/workout-warm-up-arm-stretch-routine-outdoors-37264420/
  - File: https://videos.pexels.com/video-files/37264420/15786510_720_1280_25fps.mp4
  - SHA256: 2102C40B880F6BF5EC3AA04EBC22F769F1A628A4942E042D7AEAD4E1BBF5CD83
  - Licenza: Pexels License (uso libero anche commerciale, attribuzione non
    richiesta). Watermark assenti.
- Motivazione tecnica: soggetto singolo in piedi, prevalentemente di
  profilo, camera fissa, luce uniforme, mulinelli RITMICI del braccio
  (10 cicli in 7 s): esercita tutti i KPI, incluso il Fluidity Score che
  con il provvisorio restava 0 (<3 picchi). Validazione: 175/175 frame con
  posa, 10 bracciate, Fluidity 93,1, angoli [58,49; 179,92].
- Conseguenze sulla spec congelata:
  - Il "sandbox di validazione controllato" (sez. 3.4) per l'MVP e'
    soddisfatto dalle condizioni controllate della clip (camera fissa,
    sfondo uniforme, luce costante), non da un allestimento proprio.
    L'allestimento fisico resta nella roadmap della fase finanziata.
  - La simulazione e' in piedi (mulinello tipo dorso), opzione gia'
    prevista dalla spec (sez. 14.2), non prona su panca.
  - La demo (sez. 1.2) resta: elaborazione LIVE del video ufficiale nella
    dashboard, ripetibile con KPI identici (riproducibilita' T33), con
    eventuale momento webcam live best-effort (RF-014) da decidere.
- Il precedente `profilo_provvisorio.mp4` (terzi, non licenziato) resta
  NON tracciato e viene declassato a materiale di sviluppo storico.

### 2026-07-13 - Correzione DA-06 / T02: runtime MediaPipe legacy

- `mediapipe==0.10.35` importa su Python 3.12 ma non distribuisce l'API legacy
  `mp.solutions` usata da `vision_tracker.py`; il semplice import check iniziale
  non esercitava la funzionalita' richiesta.
- Il pin funzionante e' corretto a `mediapipe==0.10.21`, ultima versione
  verificata in questo progetto con `mp.solutions.pose` su Python 3.12.10.
- Per rendere riproducibile la combinazione verificata sono fissati anche
  `opencv-contrib-python==4.11.0.86`, `numpy==1.26.4` e
  `protobuf==4.25.9`.
- `opencv-python` non e' piu' una dipendenza diretta: il pacchetto contrib
  include l'intero namespace `cv2` e MediaPipe lo richiede. Installare entrambi
  nello stesso ambiente puo' produrre sovrascritture non deterministiche.
- Nessun cambio architetturale: resta in uso MediaPipe Pose legacy come da spec;
  questa errata corregge soltanto il set di dipendenze della decisione DA-06.
