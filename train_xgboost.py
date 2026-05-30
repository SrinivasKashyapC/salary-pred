import joblib
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor

from preprocessing import load_and_preprocess

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess()

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    ))
])

model.fit(X_train, y_train)

preds = model.predict(X_test)

mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print(f"MAE: {mae}")
print(f"R2 Score: {r2}")

joblib.dump(model, 'xgboost_model_best_final.pkl')

print("XGBoost model saved!")