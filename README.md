# Acquatic Intelligence System

**AI Swimming Motion Analyzer - Proof of Concept a secco, 100% locale, costo 0 euro.**

Il sistema analizza un video laterale di movimenti natatori simulati a secco e
ne estrae metriche cinematiche 2D: conteggio bracciate, angolo del gomito e
regolarita' del ritmo. Una rete neurale di pose estimation (MediaPipe
BlazePose) fornisce i landmark corporei; un motore matematico deterministico
calcola le metriche. Tutto gira offline sulla CPU di un PC consumer.

Specifica di riferimento: [`spec.txt`](spec.txt) (v1.1 CONGELATA).
Modifiche successive al congelamento: [`SPEC_ERRATA.md`](SPEC_ERRATA.md).

## Che cosa dimostra (e che cosa NO)

Questo PoC dimostra che **la pipeline software e gli algoritmi funzionano**:
ingestione video -> pose tracking -> metriche -> dashboard -> export, in modo
stabile, riproducibile e a costo zero. E' la leva per un pitch di
finanziamento: provare il software prima di chiedere fondi per l'hardware.

Il PoC **non** dimostra la validita' biomeccanica sportiva del gesto in acqua:
quella validazione appartiene alla fase industriale successiva (telecamere
subacquee, edge computing, sensor fusion), come dichiarato onestamente nella
spec (sez. 1.1, decisione DA-03).

## Demo

Su Windows, per l'avvio con doppio clic usa:

```text
AVVIA_APP.bat
```

In alternativa, dal terminale:

```powershell
.\venv\Scripts\python.exe -m streamlit run app.py
```

1. Carica `test_videos/profilo_test.mp4` (incluso nella repo).
2. Premi "Avvia elaborazione video": il video scorre con lo scheletro
   disegnato e l'angolo del gomito live; il contatore bracciate sale fino a
   10, il Fluidity Score arriva a 93,1 e il grafico dell'onda del polso si
   disegna in tempo reale.
3. Premi "Termina Sessione ed Esporta Dati": la sessione viene accodata a
   `data/sessions.csv` con timestamp.

I numeri sono **riproducibili**: due esecuzioni sullo stesso video producono
KPI e serie identiche bit a bit (test T33). Modalita' webcam disponibile come
percorso sperimentale/best-effort (RF-014).

## Dove sta l'AI (e dove no)

| Componente | Tecnologia | Natura |
| --- | --- | --- |
| Pose estimation | MediaPipe BlazePose (rete neurale profonda pre-addestrata, 33 landmark) | AI, inferenza locale su CPU |
| Angolo gomito | Trigonometria (`arctan2`), range [0,180] | Deterministico |
| Conteggio bracciate | Rilevamento picchi con dead-band, gate spalla, debounce 0,6 s | Deterministico |
| Fluidity Score | `max(0, 100 - std(intervalli) * K)`, K=50 euristico, indice RELATIVO | Deterministico |

Nessun LLM, nessun servizio generativo, nessuna API key, nessuna chiamata di
rete a runtime (RF-012).

## Installazione

Prerequisito: Python 3.12 (validato su 3.12.10; la spec indica 3.11 come
riferimento, vedi SPEC_ERRATA).

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Le dipendenze applicative dirette sono pinnate sulla baseline validata
(MediaPipe 0.10.21 legacy, OpenCV contrib 4.11, Streamlit 1.59.1,
NumPy 1.26.4, Pandas 3.0.3 e protobuf 4.25.9). Non installare
`opencv-python` in parallelo a `opencv-contrib-python`: condividono il
namespace `cv2`.

## Validazione

```powershell
.\venv\Scripts\python.exe scripts\test_metrics.py          # 23/23 unit test motore
.\venv\Scripts\python.exe scripts\test_project_smoke.py    # 3/3 smoke baseline/UI
.\venv\Scripts\python.exe scripts\analyze_video.py         # pipeline CLI su video ufficiale
.\venv\Scripts\python.exe vision_tracker.py --source test_videos\profilo_test.mp4
```

Esiti sul video ufficiale (dettagli in `breakdown_status.md` e `incidents.md`):

| Criterio (spec sez. 1.2) | Esito |
| --- | --- |
| Pipeline end-to-end senza crash | OK (175/175 frame) |
| Conteggio bracciate entro +-1 dal manuale | OK (manuale 10, automatico 10, diff 0) |
| Nessun picco spurio su occlusione | OK (verifica T26; limite documentato INC-011) |
| Riproducibilita' | OK (KPI e serie identiche tra run) |
| Export CSV con timestamp | OK |
| Costo operativo | 0 euro |

## Video di riferimento

`test_videos/profilo_test.mp4` e' una clip stock con **licenza Pexels** (uso
libero, attribuzione non richiesta), adottata in deroga documentata al posto
della registrazione in proprio (DA-05; fonte, hash e motivazioni in
`SPEC_ERRATA.md`): un soggetto in piedi, di profilo, che esegue 10 mulinelli
ritmici del braccio in 7 secondi. La simulazione a secco in piedi e'
espressamente prevista dalla spec (sez. 14.2).

## Limiti noti (onesti)

- Il Fluidity Score e' un **indice relativo** (K=50 euristico), non una misura
  assoluta (DA-04).
- Dopo occlusioni prolungate il tracking MediaPipe puo' perdere un picco
  reale. Nel test controllato INC-011 non sono comparsi falsi positivi, ma
  questo non autorizza un'affermazione assoluta su ogni video futuro.
- La misura e' 2D monoculare su vista laterale: l'arto lontano non e'
  affidabile, per questo il Symmetry Score e' fuori scope MVP (DA-01).
- Webcam in Streamlit: percorso sperimentale limitato a 900 frame per singola
  anteprima (RF-014), circa 30 secondi a 30 fps.
- Un rerun di Streamlit durante l'inferenza nativa resta un limite noto. La
  causa concreta osservata in INC-012 (riscrittura della cache sotto il
  decoder) e' stata rimossa; durante la demo e' comunque prudente non toccare
  i widget nei pochi secondi di elaborazione.

## Roadmap (fase finanziata)

Sandbox di ripresa proprietario, telecamere subacquee, mini-PC edge, sensor
fusion/LiDAR, analisi multi-atleta, validazione biomeccanica in acqua con
protocollo scientifico. Il prodotto futuro prevede inoltre una modalita'
frontale bilaterale: tracking separato di braccio destro e sinistro e metriche
di confronto da calibrare su quel protocollo; non coincide con la metrica
mono-arto del PoC laterale.

## Struttura

```text
.
+-- app.py                  # dashboard Streamlit (input, rendering, KPI, export)
+-- vision_tracker.py       # ingestione video + MediaPipe Pose + overlay
+-- metrics_engine.py       # motore metriche deterministico + analyze_frame
+-- scripts/test_metrics.py # validatore unit (23 test)
+-- scripts/test_project_smoke.py # smoke test ambiente/default/UI
+-- scripts/analyze_video.py# validazione CLI su video reale
+-- test_videos/profilo_test.mp4  # video ufficiale (licenza Pexels)
+-- data/                   # sessions.csv (generato a runtime, gitignored)
+-- docs/governance/        # breakdown sorgente versionato
+-- spec.txt / SPEC_ERRATA.md
+-- breakdown_status.md / prompt_log.md / incidents.md / HANDOFF.md
```

## Privacy

Il video non viene conservato come output di sessione, inserito nel CSV o
versionato: si salvano soltanto metriche aggregate in `data/sessions.csv`
(verifica T25). Per consentire a OpenCV di leggere un upload, Streamlit ne
materializza temporaneamente i byte in `.cache/uploaded_session.mp4`: e' un
file locale gitignored, sovrascritto quando cambia l'upload, ma puo' restare su
disco dopo la sessione e va trattato come dato personale locale. Eventuali
persone riprese devono essere consenzienti; i video di terzi richiedono una
licenza adeguata.

**Questo progetto non e' un dispositivo medico e non fornisce consigli
clinici o di prevenzione degli infortuni.** L'interpretazione dei numeri
spetta a un umano: il sistema e' un supporto alla decisione, non un decisore.

## Governance

- `breakdown_status.md`: avanzamento task T01-T41 con evidenze.
- `prompt_log.md`: registro delle iterazioni di lavoro.
- `incidents.md`: incidenti reali, finding e limiti documentati.
- `SPEC_ERRATA.md`: modifiche tracciate dopo il congelamento della spec.
- `docs/governance/AISwimmingAnalyzer_breakdown_tasks_v1.md`: breakdown
  sorgente usato per T01-T41.

---

*Progetto per il corso AI Projects Development - ITS ICT Academy Roma.*
