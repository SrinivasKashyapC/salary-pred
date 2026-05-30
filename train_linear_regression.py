import joblib

from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score

from preprocessing import load_and_preprocess

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess()

model = Pipeline([
    ('preprocessor', preprocessor),

    ('regressor', Ridge(
        alpha=1.0
    ))
])

model.fit(X_train, y_train)

preds = model.predict(X_test)

mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print(f"MAE: {mae}")
print(f"R2 Score: {r2}")

joblib.dump(model, 'linear_regression_model_best.pkl')

print("Linear Regression model saved!")