#!/bin/bash

# Quick start script for Salary Predictor application

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║     SalaryPredictAI - Full Stack Application Launcher      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "[ERROR] Node.js is not installed"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo "[✓] Python and Node.js found"

# Start Backend
echo ""
echo "Starting FastAPI Backend (Port 8000)..."
python3 app.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Install frontend dependencies if needed
cd frontend
if [ ! -d "node_modules" ]; then
    echo "[*] Installing frontend dependencies..."
    npm install
fi

echo ""
echo "Starting React Frontend..."
npm start &
FRONTEND_PID=$!

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                Application is running!                     ║"
echo "║                                                            ║"
echo "║  Backend:  http://localhost:8000                          ║"
echo "║  Frontend: http://localhost:3000                          ║"
echo "║                                                            ║"
echo "║  Press Ctrl+C to stop                                     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Wait for both processes
wait
