@echo off
setlocal
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
  echo ERRORE: ambiente Python non trovato in venv\Scripts\python.exe
  echo Prima installazione:
  echo   python -m venv venv
  echo   venv\Scripts\python.exe -m pip install -r requirements.txt
  if not defined NO_PAUSE pause
  exit /b 1
)

if /I "%~1"=="--check" (
  "venv\Scripts\python.exe" -m streamlit version
  exit /b %ERRORLEVEL%
)

echo Avvio AI Swimming Motion Analyzer...
"venv\Scripts\python.exe" -m streamlit run app.py %*
set "EXIT_CODE=%ERRORLEVEL%"

if not defined NO_PAUSE pause
exit /b %EXIT_CODE%
