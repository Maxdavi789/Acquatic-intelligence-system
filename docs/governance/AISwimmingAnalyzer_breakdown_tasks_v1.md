# Breakdown Task — AI Swimming Motion Analyzer (PoC a secco)

**Autore:** Filippo Moruzzi (supporto metodologico) — per lo studente proprietario del progetto
**Progetto:** AI Swimming Motion Analyzer — repo `Acquatic Intelligence System`
**Versione spec di riferimento:** v1.1 — **congelare prima di iniziare M1** (T01 mette la spec congelata in `spec.txt`)
**Repository:** https://github.com/Maxdavi789/Acquatic-intelligence-system
**Data:** 02/07/2026
**Corso:** AI Projects Development — ITS ICT Academy Roma — Docente Melanie Trucco

---

## Scopo del documento

Scomposizione del lavoro **residuo** di build dell'MVP in task atomiche con dipendenze esplicite, criterio di "fatto" (DoD) e stima tempo. Ogni task ha un ID univoco (`TNN`) citabile in commit, `incidents.md` e `prompt_log.md`.

**Stato di partenza reale (repo al 28/05/2026):** FASE 0 completata, FASE 1 (`vision_tracker.py`) e FASE 2 (`metrics_engine.py`) **implementate ma non allineate alla spec v1.1** (scritte contro la vecchia `spec.txt`). `app.py` è vuoto (FASE 3 non iniziata). FASE 4 non iniziata.

Il breakdown quindi **non ricrea** la base: M0 la riconcilia con le decisioni della spec (simmetria fuori MVP, MP4 primario, pin MediaPipe, obiettivo onesto), poi costruisce ciò che manca.

---

## Riepilogo per fase (vista alto livello)

| Modulo | Descrizione | Task ID | Stima cumulativa | Fase spec |
|---|---|---|---|---|
| M0 | Allineamento base esistente ↔ spec v1.1 | T01–T06 | ~1h 40min | FASE 0/1 (revisione) |
| M1 | Hardening motore metriche `metrics_engine.py` | T07–T12 | ~2h 30min | FASE 2 (completamento) |
| M2 | Step di analisi per-frame (glue vision→metrics) | T13–T14 | ~1h | FASE 2/3 |
| M3 | Dashboard Streamlit `app.py` | T15–T22 | ~4h | FASE 3 |
| M4 | Persistenza CSV | T23–T25 | ~1h | FASE 4 |
| M5 | Robustezza e gestione errori | T26–T29 | ~2h | FASE 4 |
| M6 | Test e validazione | T30–T33 | ~1h 30min | FASE 4 |
| M7 | Sandbox demo controllato (DA-08) | T34–T36 | ~2h | FASE 4 |
| M8 | Demo, pitch e chiusura governance | T37–T41 | ~3h 50min | FASE 4 |

**Tempo totale stimato:** ~18–22 ore di lavoro effettivo. La base FASE 0–2 già scritta abbatte il tempo rispetto a un progetto da zero.

> **Nota stime:** valgono per uno sviluppatore singolo assistito da un editor AI (Cursor/Codex) come copilot, incluse review del diff + integrazione + test rapido + commit + push. Codice scritto interamente a mano: raddoppiare.

---

## Convenzioni

- **ID task:** `TNN`. Da citare nei commit: `git commit -m "T17: render video Streamlit"`.
- **Dipendenza:** task X dipende da Y → Y completata **e testata** prima di iniziare X.
- **DoD (Definition of Done):** criterio specifico e verificabile. Se il DoD non è soddisfatto, la task è aperta.
- **Stima:** tempo realistico inizio → DoD, pause escluse.
- **Refs:** collegamento a MVP-xxx / RF-xxx / § della spec v1.1 per tracciabilità.

---

## M0 — Allineamento base esistente ↔ spec v1.1

### T01 — Congelare la spec e sostituire `spec.txt`
- **Dipendenze:** nessuna
- **Cosa fare:** portare la spec v1.1 allo stato CONGELATA (registro §16); sostituire il contenuto di `spec.txt` nella repo con la spec v1.1 (l'editor AI legge `@spec.txt` come contesto globale). Il vecchio contenuto resta nella history Git.
- **DoD:** `spec.txt` contiene la v1.1; commit `T01: freeze spec v1.1`. La vecchia spec è recuperabile da `git log`.
- **Stima:** 10 min
- **Refs:** spec §16, guida sviluppo (contesto `@spec.txt`)

### T02 — Pin versione MediaPipe (DA-06)
- **Dipendenze:** nessuna
- **Cosa fare:** leggere la versione funzionante nel `venv` (`pip freeze | findstr mediapipe`) e pinnarla in `requirements.txt` (es. `mediapipe==X.Y.Z`). Reinstallare pulito per verifica.
- **DoD:** `requirements.txt` pinnato; `pip install -r requirements.txt` in venv pulito → import OK.
- **Stima:** 15 min
- **Refs:** spec §7.1, §7.2, DA-06

### T03 — Test reale FASE 1 su MP4 provvisorio + webcam
- **Dipendenze:** T02
- **Cosa fare:** verificare `vision_tracker.py` su un **MP4 laterale provvisorio** (una clip di profilo qualsiasi, in attesa del video ufficiale del sandbox T35) e sulla webcam. Questo test non era ancora stato fatto.
- **DoD:** `python vision_tracker.py --source <clip>.mp4` mostra lo scheletro; webcam idem (best-effort); premendo `q` chiude senza crash; a fine video chiude pulito.
- **Stima:** 30 min
- **Refs:** RF-003, RF-013, MVP-002

### T04 — Decisione `matplotlib` (DA-07)
- **Dipendenze:** T02
- **Cosa fare:** verificare se `matplotlib` è usato; se no, rimuoverlo da `requirements.txt` (i grafici usano `st.line_chart`). Mantenere solo l'import di cache config se serve a MediaPipe.
- **DoD:** `requirements.txt` pulito; import test OK; nessun riferimento morto.
- **Stima:** 10 min
- **Refs:** spec §7.2, DA-07

### T05 — Demossione Symmetry Score ad airbag (DA-01 = A)
- **Dipendenze:** T01
- **Cosa fare:** **non cancellare** `calculate_symmetry_score`, ma escluderla dalla pipeline e dai KPI. Aggiungere commento/docstring: `# FUORI MVP v1 — vedi spec §4.2 (contraddice vista laterale). Riattivabile in v2 con cambio protocollo`. Assicurarsi che nessun modulo la richiami.
- **DoD:** funzione presente ma non invocata; grep del progetto → 0 chiamate attive; commento presente.
- **Stima:** 20 min
- **Refs:** DA-01, spec §4.2, §14.4

### T06 — Aggiornare governance con la nuova baseline
- **Dipendenze:** T01, T05
- **Cosa fare:** in `incidents.md`/`prompt_log.md`/`breakdown_status.md` registrare: passaggio `spec.txt` → v1.1, demossione simmetria, MP4 primario. Nuova baseline del progetto.
- **DoD:** almeno una entry per file che documenta il cambio; committato.
- **Stima:** 15 min
- **Refs:** governance corso, spec §14.4

---

## M1 — Hardening motore metriche (`metrics_engine.py`)

### T07 — Selezione arto lato-camera
- **Dipendenze:** T01
- **Cosa fare:** `select_camera_side_arm(landmarks)` che sceglie tra sinistro (11/13/15) e destro (12/14/16) l'arto con `visibility` media più alta e restituisce le tre coordinate (spalla, gomito, polso).
- **DoD:** unit test con landmark sintetici (un lato più visibile) → seleziona il lato corretto.
- **Stima:** 25 min
- **Refs:** RF-004, MVP-003

### T08 — Forward-fill occlusioni sull'angolo
- **Dipendenze:** T07
- **Cosa fare:** logica stateful (`ElbowAngleSmoother` o funzione con stato) che, se la visibility dei landmark scelti scende < 0.5, mantiene l'ultimo angolo valido invece di ricalcolare su dati sporchi.
- **DoD:** unit test: sequenza con frame occluso → l'angolo resta all'ultimo valido, nessun picco, nessuna eccezione.
- **Stima:** 40 min
- **Refs:** RF-008, MVP-006, spec §9.3

### T09 — Unit test `calculate_elbow_angle`
- **Dipendenze:** T01
- **Cosa fare:** test su input noti (braccio disteso ~180°, gomito a ~90°) e verifica range [0,180].
- **DoD:** test verde su ≥3 casi.
- **Stima:** 15 min
- **Refs:** RF-005, spec §11.1

### T10 — Unit test `StrokeCounter`
- **Dipendenze:** T01
- **Cosa fare:** costruire una serie temporale sintetica di Y del polso (sinusoide) con timestamp; verificare conteggio atteso, debounce 0.6 s, gate spalla, dead-band `min_delta`.
- **DoD:** test verde su ≥2 scenari (ritmo regolare; ritmo con jitter sotto dead-band che non deve contare).
- **Stima:** 30 min
- **Refs:** RF-006, spec §9.4

### T11 — Unit test Fluidity + documentazione costante K
- **Dipendenze:** T01
- **Cosa fare:** test: intervalli regolari → punteggio alto, irregolari → basso, <3 picchi → 0. Aggiungere commento che `K=50` è euristica e il punteggio è **indice relativo** (DA-04).
- **DoD:** test verde; commento presente in codice.
- **Stima:** 20 min
- **Refs:** RF-007, spec §9.4, DA-04

### T12 — Script di validazione aggregata `scripts/test_metrics.py`
- **Dipendenze:** T09, T10, T11
- **Cosa fare:** un runner che esegue tutti i check del motore e stampa un riepilogo (sostituisce i "test sintetici" informali già fatti dall'amico).
- **DoD:** `python scripts/test_metrics.py` → exit code 0, conteggi/esiti a schermo.
- **Stima:** 20 min
- **Refs:** spec §11.2

---

## M2 — Step di analisi per-frame (glue vision → metrics)

### T13 — `analyze_frame(landmarks, timestamp, state)`
- **Dipendenze:** T07, T08, T10
- **Cosa fare:** funzione che orchestra un singolo frame: seleziona arto (T07), calcola angolo con forward-fill (T08), aggiorna `StrokeCounter`, restituisce dict `{arm_side, elbow_angle, stroke_count, fluidity_score, wrist_y, peak_detected}`. **Nessun campo simmetria.**
- **DoD:** chiamata su landmark sintetici → dict completo e coerente; grep conferma assenza di simmetria.
- **Stima:** 30 min
- **Refs:** spec §8.1, MVP-003/004/005/006

### T14 — Validazione preliminare da CLI su MP4 provvisorio
- **Dipendenze:** T13, T03
- **Cosa fare:** collegare `analyze_frame` all'output reale di `extract_pose_landmarks`; script che processa l'MP4 provvisorio e stampa in console angolo + stroke count (validazione "Settimana 2" della roadmap).
- **DoD:** su clip reale i valori scorrono in console con senso (angolo in [0,180], conteggio non impazzisce).
- **Stima:** 30 min
- **Refs:** spec §5.1, RF-004/005/006

---

## M3 — Dashboard Streamlit (`app.py`) — FASE 3

### T15 — Scaffold `app.py` + layout a due colonne
- **Dipendenze:** T01
- **Cosa fare:** pagina Streamlit, `st.set_page_config`, due colonne asimmetriche (sinistra video, destra metriche). Config cache MediaPipe se serve.
- **DoD:** `streamlit run app.py` apre una pagina con due colonne (anche vuote).
- **Stima:** 20 min
- **Refs:** MVP-007, RF-009, spec §7 UI

### T16 — Selettore input (MP4 primario, webcam best-effort)
- **Dipendenze:** T15
- **Cosa fare:** `st.radio` "File MP4" / "Webcam (sperimentale)"; `st.file_uploader` per `.mp4`. Alla scelta webcam mostrare avviso "modalità sperimentale".
- **DoD:** upload MP4 → file disponibile alla pipeline; webcam mostra avviso; MP4 è il default.
- **Stima:** 30 min
- **Refs:** MVP-001, MVP-009, RF-001, RF-014

### T17 — Rendering video in colonna sinistra (`st.image`)
- **Dipendenze:** T16, T03
- **Cosa fare:** loop di lettura frame (riuso funzioni `vision_tracker`), overlay scheletro, sostituire `cv2.imshow` con `st.image` aggiornato in un placeholder.
- **DoD:** il video con scheletro scorre nella UI dal MP4 caricato.
- **Stima:** 45 min
- **Refs:** RF-003, spec §14.2

### T18 — Overlay angolo gomito live
- **Dipendenze:** T17, T13
- **Cosa fare:** stampare l'angolo del gomito sul frame (testo) e/o accanto al video, aggiornato frame per frame.
- **DoD:** il numero dell'angolo cambia coerentemente col movimento nel video.
- **Stima:** 20 min
- **Refs:** RF-005, spec §7 UI

### T19 — KPI colonna destra (`st.metric`) — senza simmetria
- **Dipendenze:** T15, T13
- **Cosa fare:** due blocchi `st.metric`: "Bracciate totali" e "Fluidity Score". **Nessun blocco Symmetry** (rispetta T05).
- **DoD:** i due KPI presenti; nessun riferimento a simmetria nella UI.
- **Stima:** 20 min
- **Refs:** MVP-004/005, RF-006/007, spec §4.2

### T20 — Grafico onda Y del polso (`st.line_chart`)
- **Dipendenze:** T15
- **Cosa fare:** line chart che accumula la coordinata Y del polso nel tempo, aggiornato durante l'elaborazione.
- **DoD:** la curva si popola mentre il video scorre.
- **Stima:** 30 min
- **Refs:** RF-010, MVP-007

### T21 — Collegare `analyze_frame` al loop (dati reali)
- **Dipendenze:** T17, T18, T19, T20
- **Cosa fare:** far derivare KPI, angolo e grafico dai valori reali di `analyze_frame`, non da placeholder.
- **DoD:** sull'MP4 provvisorio i numeri sono coerenti col video (conteggio segue le bracciate visibili).
- **Stima:** 40 min
- **Refs:** spec §8.2, MVP-003/004/005

### T22 — Gestione `st.session_state`
- **Dipendenze:** T21
- **Cosa fare:** conservare contatori/stato in `session_state` per non azzerarli a ogni rerun di Streamlit durante la sessione.
- **DoD:** interagendo con i widget durante una sessione i KPI non si resettano.
- **Stima:** 40 min
- **Refs:** spec §14.2 (limite Streamlit)

---

## M4 — Persistenza CSV — FASE 4

### T23 — Pulsante "Termina Sessione ed Esporta Dati" + aggregazione
- **Dipendenze:** T21
- **Cosa fare:** bottone che aggrega le metriche finali (bracciate totali, fluidity finale, angolo medio/max) in un DataFrame Pandas.
- **DoD:** click → DataFrame con i campi attesi (verificabile con stampa/preview).
- **Stima:** 25 min
- **Refs:** MVP-008, RF-011

### T24 — Append a `data/sessions.csv` con timestamp
- **Dipendenze:** T23
- **Cosa fare:** append al CSV locale (crea header se assente), includendo un timestamp della sessione.
- **DoD:** nuova riga con data/ora; append non sovrascrive; file apribile.
- **Stima:** 25 min
- **Refs:** RF-011, spec §8.3

### T25 — Verifica non-salvataggio del video (privacy)
- **Dipendenze:** T24
- **Cosa fare:** controllare che a fine sessione in `data/` ci sia **solo** il CSV, nessun frame/video persistito.
- **DoD:** ispezione cartella → solo `sessions.csv`; nota in `incidents.md` se serve.
- **Stima:** 10 min
- **Refs:** spec §10.1, §10.2

---

## M5 — Robustezza e gestione errori — FASE 4

### T26 — Occlusion smoothing collegato nel loop app
- **Dipendenze:** T21, T08
- **Cosa fare:** usare `ElbowAngleSmoother` (T08) nel loop dell'app; verificare assenza di picchi/crash su arto occluso.
- **DoD:** MP4 con arto coperto → grafico angoli senza picchi spuri, nessun crash.
- **Stima:** 40 min
- **Refs:** RF-008, MVP-006, spec §12

### T27 — Sorgente non valida / fine stream / nessuna persona
- **Dipendenze:** T21
- **Cosa fare:** gestire percorso inesistente (messaggio leggibile), fine video ("Elaborazione terminata"), frame senza persona (skip senza errore).
- **DoD:** i tre scenari gestiti, nessuna eccezione non gestita, messaggi visibili in UI.
- **Stima:** 30 min
- **Refs:** RF-001, RF-013, spec §12

### T28 — Webcam best-effort con degrado documentato
- **Dipendenze:** T27
- **Cosa fare:** se la webcam è instabile in Streamlit, mostrare avviso e permettere di ripiegare su MP4 senza crash.
- **DoD:** selezione webcam funziona o degrada in modo documentato; nessun crash.
- **Stima:** 30 min
- **Refs:** RF-014, spec §14.2

### T29 — Cleanup risorse su stop/switch
- **Dipendenze:** T27
- **Cosa fare:** garantire `capture.release()` e nessun handle aperto quando si ferma o si cambia input.
- **DoD:** stop a metà elaborazione → nessuna eccezione, risorse liberate.
- **Stima:** 20 min
- **Refs:** RF-013

---

## M6 — Test e validazione — FASE 4

### T30 — Test caso normale (conteggio ±1 vs manuale)
- **Dipendenze:** T21, T35 *(usa il video ufficiale del sandbox; in attesa, l'MP4 provvisorio)*
- **Cosa fare:** contare a mano le bracciate nel video di riferimento e confrontare con `stroke_count`.
- **DoD:** conteggio manuale documentato; |differenza| ≤ 1.
- **Stima:** 30 min
- **Refs:** spec §1.2, §11.3, RF-006

### T31 — Test occlusione formale
- **Dipendenze:** T26
- **Cosa fare:** eseguire uno scenario con occlusione controllata e documentarne l'esito.
- **DoD:** esito registrato in `incidents.md`/`prompt_log.md`; nessun picco/crash.
- **Stima:** 15 min
- **Refs:** spec §11.3

### T32 — Test input non valido + fine stream + stop
- **Dipendenze:** T27, T29
- **Cosa fare:** eseguire i tre casi limite e verificare la gestione.
- **DoD:** tutti e tre gestiti; log presente.
- **Stima:** 30 min
- **Refs:** spec §11.3, §12

### T33 — Test riproducibilità
- **Dipendenze:** T30
- **Cosa fare:** due run sullo stesso MP4 → confronto KPI.
- **DoD:** KPI identici tra i due run.
- **Stima:** 15 min
- **Refs:** spec §1.2 (Riproducibilità)

---

## M7 — Sandbox demo controllato (DA-08) — FASE 4

### T34 — Montare il sandbox controllato
- **Dipendenze:** nessuna (parallelizzabile, ma serve prima di T35)
- **Cosa fare:** allestire l'ambiente §3.4 a costo zero: supporto camera fisso a 90°, sfondo neutro (telo/parete), luci esistenti uniformi, marker a terra per la posizione del soggetto.
- **DoD:** setup montato; foto del setup salvata; costo €0 confermato; elenco materiali in `incidents.md`/README.
- **Stima:** 60 min
- **Refs:** spec §3.4, DA-08

### T35 — Registrare il video di riferimento nel sandbox
- **Dipendenze:** T34
- **Cosa fare:** registrare una clip dryland di profilo pulita → `test_videos/profilo_test.mp4`. Diventa il video **ufficiale** di validazione/demo (sostituisce l'MP4 provvisorio di T03/T14).
- **DoD:** `profilo_test.mp4` presente, laterale, soggetto tracciabile.
- **Stima:** 30 min
- **Refs:** spec §3, §5.2, DA-05

### T36 — Validare la pipeline sul video ufficiale
- **Dipendenze:** T35, T21
- **Cosa fare:** giro completo pipeline sul video del sandbox: KPI, grafico, export CSV.
- **DoD:** KPI plausibili, nessun picco spurio, CSV generato.
- **Stima:** 30 min
- **Refs:** spec §1.2

---

## M8 — Demo, pitch e chiusura governance

### T37 — README aggiornato (onesto + disclaimer)
- **Dipendenze:** T36
- **Cosa fare:** README con descrizione onesta, "come funziona", **disclaimer "non è un dispositivo medico e non fornisce consigli clinici/di prevenzione infortuni"**, vincolo €0, roadmap con sensori, link alla spec v1.1.
- **DoD:** README coerente con la spec; disclaimer presente; link funzionanti.
- **Stima:** 45 min
- **Refs:** spec §10.3, §0

### T38 — Screenshot/grafici per le slide
- **Dipendenze:** T36
- **Cosa fare:** catturare video annotato, KPI e grafico onda dalla dashboard.
- **DoD:** ≥3 immagini salvate per il pitch.
- **Stima:** 20 min
- **Refs:** demo prep

### T39 — Slide del pitch (con richiesta fondi)
- **Dipendenze:** T38
- **Cosa fare:** 8–12 slide: problema, target, soluzione, architettura, demo, **costo €0**, roadmap con sensori (edge/subacquee/LiDAR), **richiesta fondi**. Inquadrare il dry-run onestamente: *prova che il software funziona, non validità in acqua* (§14.4). Angolo di vendita: "rischio software azzerato, finanziate il rischio hardware".
- **DoD:** slide esportate in PDF, riviste.
- **Stima:** 90 min
- **Refs:** spec §0 (contesto strategico), §2.2

### T40 — Rehearsal demo nel sandbox (≥2 volte)
- **Dipendenze:** T36, T39
- **Cosa fare:** provare la demo end-to-end nel sandbox, cronometrata, almeno due volte di fila.
- **DoD:** demo ripetuta 2× senza intoppi; tempo entro il limite di presentazione.
- **Stima:** 45 min
- **Refs:** spec §1.2 (ripetibilità demo)

### T41 — Chiusura governance
- **Dipendenze:** T40
- **Cosa fare:** aggiornare `incidents.md` (problemi reali incontrati), `prompt_log.md` (iterazioni rilevanti) e `breakdown_status.md` ("FASE 3–4 completate").
- **DoD:** documenti aggiornati e committati; ≥5 entry totali in `incidents.md`.
- **Stima:** 30 min
- **Refs:** governance corso (peso documentazione)

---

## Catena critica (path lungo del progetto)

T01 → T02 → T03 → T07 → T08 → T13 → T14 → T15 → T16 → T17 → T21 → T23 → T24 → T26 → T34 → T35 → T36 → T39 → T40

**Lunghezza:** ~19 task essenziali, ~13–14 ore di lavoro effettivo. Le altre task (unit test M1, casi limite M5, test M6, README/screenshot) sono parallelizzabili o ritardabili senza bloccare la consegna.

> **Nota dipendenza video:** lo sviluppo (T03/T14/T30) può partire con un **MP4 laterale provvisorio**. Il video ufficiale del sandbox (T35) lo sostituisce per validazione e demo. Non aspettare il sandbox per iniziare a costruire.

---

## Dipendenze cross-modulo (vista semplificata)

```
M0 (allineamento) → tutto il resto
M1 (metriche) → M2 (glue) → M3 (dashboard)
M2 → M3 → M4 (persistenza) → M5 (robustezza) → M6 (test)
M7 (sandbox) → M6 (validazione su video ufficiale) → M8 (demo/pitch)
M3 → M7/M8 (serve la dashboard funzionante per registrare e presentare)
```

---

## Note pratiche

1. **Commit per task.** Ogni task chiusa = 1 commit `T17: render video Streamlit`. Facilita rollback e tracciabilità.
2. **Editor AI.** Per ogni task, dare all'assistente (Cursor/Codex) il blocco "Cosa fare" + "DoD" + `@spec.txt`. Rivedere il diff prima di accettare.
3. **Test as you go.** Non rimandare i test a M6: M1 ha già i suoi (T09–T12). Se un test fallisce, fixare prima di procedere.
4. **NON riaggiungere la simmetria.** È la trappola di scope creep di questo progetto: contraddice la vista laterale. Se torna la tentazione → entry in `incidents.md` "scope creep evitato", non codice.
5. **Onestà nel pitch.** Il dry-run prova il software, non la biomeccanica in acqua. Presentarlo come "rischio software azzerato" regge; spacciarlo per validità sportiva no.
6. **Vincolo €0.** Sandbox = materiali di recupero. Nessuna spesa in tutto l'MVP.
7. **Governance viva.** `incidents.md`/`prompt_log.md` si aggiornano quando serve, non a fine progetto.

---

*Breakdown task — AI Swimming Motion Analyzer — supporto Filippo Moruzzi — Corso AI Projects Development, ITS ICT Academy Roma*
