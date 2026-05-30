# Salary Prediction Application

A full-stack application that predicts data science salaries using 4 ML models with an ensemble approach.

## Features

- **4 Machine Learning Models**: Linear Regression, Decision Tree, XGBoost, and Neural Network
- **Ensemble Prediction**: Averages predictions from all 4 models for robust results
- **FastAPI Backend**: Simple REST API for predictions
- **React Frontend**: Interactive web UI for input and predictions
- **Real-time Predictions**: Get instant salary predictions based on job parameters

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Models (if not already done)

Train all four models:

```bash
python train_linear_regression.py
python train_decision_tree.py
python train_xgboost.py
python train_neural_network.py
```

This will generate the model files:
- `linear_regression_model.pkl`
- `decision_tree_model.pkl`
- `xgboost_model.pkl`
- `neural_network_model.keras`
- `nn_preprocessor.pkl`

### 3. Start the FastAPI Server

```bash
python app.py
```

The API will be available at `http://localhost:8000`

API endpoints:
- `GET /` - Health check
- `POST /predict` - Get salary predictions

Example request:
```json
{
  "work_year": 2024,
  "experience_level": "SE",
  "employment_type": "FT",
  "job_title": "Data Scientist",
  "salary_currency": "USD",
  "employee_residence": "US",
  "remote_ratio": 100,
  "company_location": "US",
  "company_size": "L"
}
```

### 4. Start the React Frontend

```bash
cd frontend
npm install
npm start
```

The frontend will open at `http://localhost:3000` automatically.

See [frontend/FRONTEND_SETUP.md](frontend/FRONTEND_SETUP.md) for detailed frontend setup instructions.

## How It Works

1. **User Input**: Fill in job parameters in the web form
2. **API Call**: Frontend sends request to FastAPI backend
3. **Model Predictions**: Backend loads all 4 trained models and generates predictions
4. **Ensemble Result**: Backend averages the 4 predictions
5. **Display Results**: Frontend displays all 4 model predictions and the ensemble average

## Model Details

- **Linear Regression**: Baseline linear model with preprocessing
- **Decision Tree**: Tree-based model with max_depth=10
- **XGBoost**: Gradient boosting with 300 estimators
- **Neural Network**: 3-layer neural network with dropout regularization

All models use one-hot encoding for categorical features and standard scaling for numerical features.

## Project Structure

```
Salary_Pred/
├── app.py                          # FastAPI backend
├── preprocessing.py                # Data preprocessing utilities
├── train_linear_regression.py      # Linear regression trainer
├── train_decision_tree.py          # Decision tree trainer
├── train_xgboost.py               # XGBoost trainer
├── train_neural_network.py         # Neural network trainer
├── ensemble_predict.py             # Command-line ensemble predictor
├── ds_salaries.csv                # Training dataset
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── frontend/                      # React frontend application
    ├── src/
    │   ├── pages/
    │   │   ├── Landing.js         # Beautiful landing page
    │   │   ├── Predictor.js       # Prediction form page
    │   │   └── ...styles
    │   ├── App.js                 # Main app with routing
    │   └── index.js               # Entry point
    ├── public/
    │   └── index.html             # HTML template
    ├── package.json               # Node dependencies
    └── FRONTEND_SETUP.md          # Frontend setup guide
```

## Frontend Features

- **Beautiful Landing Page**: Hero section with feature showcase
- **Modern Predictor Page**: Clean form with real-time predictions
- **Responsive Design**: Works on all devices
- **Glassmorphism UI**: Modern glass effect backgrounds
- **Real-time Results**: Shows all 4 model predictions + ensemble average
- **Error Handling**: User-friendly error messages and loading states

## Backend API

The FastAPI backend provides:

- `GET /` - Health check
- `POST /predict` - Get salary predictions from all 4 models

Request format:
```json
{
  "work_year": 2024,
  "experience_level": "SE",
  "employment_type": "FT",
  "job_title": "Data Scientist",
  "salary_currency": "USD",
  "employee_residence": "US",
  "remote_ratio": 100,
  "company_location": "US",
  "company_size": "L"
}
```

Response format:
```json
{
  "linear_regression": 145000.00,
  "decision_tree": 158000.00,
  "xgboost": 152000.00,
  "neural_network": 150000.00,
  "ensemble_prediction": 151250.00
}
```
