@echo off
REM Quick start script for Salary Predictor application

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║     SalaryPredictAI - Full Stack Application Launcher      ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    exit /b 1
)

echo [✓] Python and Node.js found

REM Start Backend
echo.
echo Starting FastAPI Backend (Port 8000)...
start "Salary Predictor Backend" cmd /k "python app.py"

REM Wait a moment for backend to start
timeout /t 3 /nobreak

REM Start Frontend
echo.
echo Starting React Frontend...
cd frontend
if not exist node_modules (
    echo [*] Installing frontend dependencies...
    call npm install
)

echo Launching React app on http://localhost:3000...
start http://localhost:3000
npm start

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                Application is running!                     ║
echo ║                                                            ║
echo ║  Backend:  http://localhost:8000                          ║
echo ║  Frontend: http://localhost:3000                          ║
echo ║                                                            ║
echo ║  Press Ctrl+C in any window to stop                       ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
