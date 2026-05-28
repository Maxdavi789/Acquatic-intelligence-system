# Breakdown Status

Data aggiornamento: 2026-05-28

## Stato Generale

Progetto inizializzato come repository Git locale collegato alla repo remota:
`https://github.com/Maxdavi789/Acquatic-intelligence-system.git`.

La root del repository viene trattata come root logica del progetto `swim_ai_poc/`
descritta nella specifica, per evitare un livello di cartelle superfluo dentro
la repo GitHub gia' dedicata al progetto.

## Avanzamento Roadmap

| Fase | Periodo da breakdown | Stato | Note |
| --- | --- | --- | --- |
| FASE 0 - Setup ambiente e scaffold locale | Giorni 1-2 | Completata | Python 3.11 installato, `venv` creato, dipendenze installate. |
| FASE 1 - Ingestione video e pose tracking | Settimana 1 | Implementata | `vision_tracker.py` apre webcam/MP4, ridimensiona frame, esegue MediaPipe Pose e disegna overlay. Test reale webcam/MP4 ancora da fare. |
| FASE 2 - Motore biomeccanico e metriche 2D | Settimana 2 | Implementata | `metrics_engine.py` contiene angolo gomito, stroke counter, Fluidity Score e Symmetry Score. Validazione sintetica completata. |
| FASE 3 - Dashboard Streamlit locale | Settimana 3 | Prossima | Da avviare integrando pipeline video e metriche in `app.py`. |
| FASE 4 - Persistenza, errori e pitch demo | Settimana 4 | Non iniziata | Dipende da pipeline e dashboard integrate. |

## Dettaglio FASE 0

| Step | Descrizione | Stato | Evidenza |
| --- | --- | --- | --- |
| 0.1 | Creare struttura progetto e file iniziali | Completato | `app.py`, `vision_tracker.py`, `metrics_engine.py`, `requirements.txt`, `spec.txt`, `data/`, `test_videos/`. |
| 0.2 | Creare virtual environment Python | Completato | `venv/` creato con Python 3.11. |
| 0.3 | Scrivere dipendenze e installarle | Completato | `requirements.txt` compilato e installazione verificata con import test. |

## Prossima Task

Avviare FASE 3 creando la dashboard Streamlit in `app.py`:

- layout a due colonne;
- input file MP4 o webcam;
- rendering frame con overlay;
- KPI per bracciate, Fluidity Score e Symmetry Score;
- grafico in tempo reale della coordinata Y del polso.

## Task Arretrate o Bloccate

- Autenticazione GitHub CLI non ancora attiva: `gh auth status` segnala utente
  non autenticato.
- Test reale webcam/MP4 non ancora eseguito per FASE 1.
- `data/sessions.csv` non creato ora per non anticipare la FASE 4; verra'
  generato dal modulo di esportazione dati.
