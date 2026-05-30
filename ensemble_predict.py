import joblib
import pandas as pd
import numpy as np
import tensorflow as tf

ENSEMBLE_WEIGHTS = {
    'linear_regression': 0.20,
    'decision_tree': 0.20,
    'xgboost': 0.50,
    'neural_network': 0.10,
}

linear_model = joblib.load('linear_regression_model_best.pkl')
decision_tree_model = joblib.load('decision_tree_model_best.pkl')
xgboost_model = joblib.load('xgboost_model_best_final.pkl')

nn_model = tf.keras.models.load_model('neural_network_model.keras')
nn_preprocessor = joblib.load('nn_preprocessor.pkl')

sample = {
    'work_year': 2024,
    'experience_level': 'SE',
    'employment_type': 'FT',
    'job_title': 'Data Scientist',
    'salary_currency': 'USD',
    'employee_residence': 'US',
    'remote_ratio': 100,
    'company_location': 'US',
    'company_size': 'L'
}

input_df = pd.DataFrame([sample])

linear_pred = linear_model.predict(input_df)[0]
decision_tree_pred = decision_tree_model.predict(input_df)[0]
xgboost_pred = xgboost_model.predict(input_df)[0]

processed_input = nn_preprocessor.transform(input_df)
processed_input = processed_input.toarray()

nn_pred = nn_model.predict(processed_input)[0][0]

ensemble_prediction = (
    linear_pred * ENSEMBLE_WEIGHTS['linear_regression']
    + decision_tree_pred * ENSEMBLE_WEIGHTS['decision_tree']
    + xgboost_pred * ENSEMBLE_WEIGHTS['xgboost']
    + nn_pred * ENSEMBLE_WEIGHTS['neural_network']
)

print("\n===== Individual Model Predictions =====")
print(f"Linear Regression: ${linear_pred:.2f}")
print(f"Decision Tree:     ${decision_tree_pred:.2f}")
print(f"XGBoost:           ${xgboost_pred:.2f}")
print(f"Neural Network:    ${nn_pred:.2f}")

print("\n===== Final Ensemble Prediction =====")
print(f"Average Predicted Salary: ${ensemble_prediction:.2f}")

summary = f'''
Predicted Salary Report:

1. Linear Regression predicted ${linear_pred:.2f}
2. Decision Tree predicted ${decision_tree_pred:.2f}
3. XGBoost predicted ${xgboost_pred:.2f}
4. Neural Network predicted ${nn_pred:.2f}

Final Weighted Ensemble Salary Prediction:
${ensemble_prediction:.2f}
'''

print(summary)