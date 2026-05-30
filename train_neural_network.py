import joblib
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

from sklearn.metrics import mean_absolute_error, r2_score

from preprocessing import load_and_preprocess

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess()

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

X_train_processed = X_train_processed.toarray()
X_test_processed = X_test_processed.toarray()

input_dim = X_train_processed.shape[1]

model = Sequential([

    Input(shape=(input_dim,)),

    Dense(128, activation='relu'),
    Dropout(0.2),

    Dense(64, activation='relu'),
    Dropout(0.1),

    Dense(32, activation='relu'),

    Dense(1)
])

optimizer = tf.keras.optimizers.Adam(
    learning_rate=0.001
)

model.compile(
    optimizer=optimizer,
    loss='mse',
    metrics=['mae']
)

checkpoint = ModelCheckpoint(
    'neural_network_model.keras',
    monitor='val_loss',
    save_best_only=True,
    verbose=1
)

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=15,
    restore_best_weights=True,
    verbose=1
)

model.fit(
    X_train_processed,
    y_train,
    validation_split=0.2,
    epochs=200,
    batch_size=8,
    callbacks=[checkpoint, early_stopping],
    verbose=1
)

preds = model.predict(X_test_processed).flatten()

mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print(f"\nMAE: {mae}")
print(f"R2 Score: {r2}")

joblib.dump(preprocessor, 'nn_preprocessor.pkl')

print("\nNeural Network model saved!")