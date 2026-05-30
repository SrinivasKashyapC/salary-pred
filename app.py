from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import tensorflow as tf

app = FastAPI()

ENSEMBLE_WEIGHTS = {
    "linear_regression": 0.20,
    "decision_tree": 0.20,
    "xgboost": 0.50,
    "neural_network": 0.10,
}

# Add CORS middleware to allow React frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load all models
linear_model = joblib.load('linear_regression_model_best.pkl')
decision_tree_model = joblib.load('decision_tree_model_best.pkl')
xgboost_model = joblib.load('xgboost_model_best_final.pkl')
nn_model = tf.keras.models.load_model('neural_network_model.keras')
nn_preprocessor = joblib.load('nn_preprocessor.pkl')


class PredictionInput(BaseModel):
    work_year: int
    experience_level: str
    employment_type: str
    job_title: str
    salary_currency: str
    employee_residence: str
    remote_ratio: int
    company_location: str
    company_size: str


@app.get("/")
def read_root():
    return {"message": "Salary Prediction API is running!"}


@app.post("/predict")
def predict(input_data: PredictionInput):
    # Convert input to dictionary and then DataFrame
    input_dict = {
        'work_year': input_data.work_year,
        'experience_level': input_data.experience_level,
        'employment_type': input_data.employment_type,
        'job_title': input_data.job_title,
        'salary_currency': input_data.salary_currency,
        'employee_residence': input_data.employee_residence,
        'remote_ratio': input_data.remote_ratio,
        'company_location': input_data.company_location,
        'company_size': input_data.company_size
    }
    
    input_df = pd.DataFrame([input_dict])
    
    # Get predictions from all models
    linear_pred = float(linear_model.predict(input_df)[0])
    decision_tree_pred = float(decision_tree_model.predict(input_df)[0])
    xgboost_pred = float(xgboost_model.predict(input_df)[0])
    
    # Neural Network prediction
    processed_input = nn_preprocessor.transform(input_df)
    processed_input = processed_input.toarray()
    nn_pred = float(nn_model.predict(processed_input, verbose=0)[0][0])
    
    # Calculate weighted ensemble prediction
    ensemble_prediction = float(
        (
            linear_pred * ENSEMBLE_WEIGHTS["linear_regression"]
            + decision_tree_pred * ENSEMBLE_WEIGHTS["decision_tree"]
            + xgboost_pred * ENSEMBLE_WEIGHTS["xgboost"]
            + nn_pred * ENSEMBLE_WEIGHTS["neural_network"]
        )
    )
    
    return {
        "linear_regression": round(linear_pred, 2),
        "decision_tree": round(decision_tree_pred, 2),
        "xgboost": round(xgboost_pred, 2),
        "neural_network": round(nn_pred, 2),
        "ensemble_prediction": round(ensemble_prediction, 2)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
