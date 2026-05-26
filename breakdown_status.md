# Breakdown Status

Data aggiornamento: 2026-05-26

## Stato Generale

Progetto inizializzato come repository Git locale collegato alla repo remota:
`https://github.com/Maxdavi789/Acquatic-intelligence-system.git`.

La root del repository viene trattata come root logica del progetto `swim_ai_poc/`
descritta nella specifica, per evitare un livello di cartelle superfluo dentro
la repo GitHub gia' dedicata al progetto.

## Avanzamento Roadmap

| Fase | Periodo da breakdown | Stato | Note |
| --- | --- | --- | --- |
| FASE 0 - Setup ambiente e scaffold locale | Giorni 1-2 | In corso | Repo locale collegata, scaffold iniziale creato. Ambiente Python ancora da verificare/sistemare. |
| FASE 1 - Ingestione video e pose tracking | Settimana 1 | Non iniziata | Da avviare dopo completamento FASE 0. |
| FASE 2 - Motore biomeccanico e metriche 2D | Settimana 2 | Non iniziata | Dipende da FASE 1. |
| FASE 3 - Dashboard Streamlit locale | Settimana 3 | Non iniziata | Dipende da FASE 1 e FASE 2. |
| FASE 4 - Persistenza, errori e pitch demo | Settimana 4 | Non iniziata | Dipende da pipeline e dashboard integrate. |

## Dettaglio FASE 0

| Step | Descrizione | Stato | Evidenza |
| --- | --- | --- | --- |
| 0.1 | Creare struttura progetto e file iniziali | Completato | `app.py`, `vision_tracker.py`, `metrics_engine.py`, `requirements.txt`, `spec.txt`, `data/`, `test_videos/`. |
| 0.2 | Creare virtual environment Python | Bloccato | `python.exe` non e' utilizzabile nella sessione corrente; vedi `incidents.md`. |
| 0.3 | Scrivere dipendenze e installarle | In sospeso | Da fare dopo ripristino ambiente Python. |

## Prossima Task

Sistemare l'ambiente Python locale per poter eseguire:

```powershell
python -m venv venv
```

Poi completare `requirements.txt` e installare le dipendenze previste dalla
specifica tecnica.

## Task Arretrate o Bloccate

- Autenticazione GitHub push non ancora verificata: Git e GitHub CLI sono
  installati, ma `gh auth status` segnala utente non autenticato.
- Ambiente Python non pronto: `python.exe` punta allo stub WindowsApps e fallisce.
- `data/sessions.csv` non creato ora per non anticipare la FASE 4; verra'
  generato dal modulo di esportazione dati.

