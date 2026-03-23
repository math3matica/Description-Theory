@echo off
setlocal

set PORT=8765
set URL=http://127.0.0.1:%PORT%/viewer.html

where py >nul 2>nul
if %errorlevel%==0 (
  start "DT Viewer Server" cmd /k py -3 -m http.server %PORT%
  timeout /t 2 /nobreak >nul
  start "" %URL%
  exit /b 0
)

where python >nul 2>nul
if %errorlevel%==0 (
  start "DT Viewer Server" cmd /k python -m http.server %PORT%
  timeout /t 2 /nobreak >nul
  start "" %URL%
  exit /b 0
)

echo Python was not found.
echo Install Python or use the embedded snapshot in viewer.html.
pause
