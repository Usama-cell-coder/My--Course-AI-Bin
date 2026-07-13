# WORKING WITH SPACEX STARLINK SATELITTE TIME SERIES ANALYSIS
# IMPORTING LIBARARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM, GRU, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import warnings
warnings.filterwarnings('ignore')
# LOADING DATASET
df = pd.read_csv(r'C:\Users\PMLS\Documents\GitHub\My_Course_AI_Bin\All DataSets\Final_Assessment_DataSets\Starlink and SpaceX Data Datset\spacex_starlink.csv')
print("="*60)
print("SPACEX STARLINK SATELLITE TIME SERIES ANALYSIS")
print("="*60)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")

# STARTING WITH DATA PREPROCESSING
print("--- DATA PREPROCESSING ---")

# Clean column names
df.columns = df.columns.str.strip()

# Convert to numeric, handle missing values
df['height_km'] = pd.to_numeric(df['height_km'], errors='coerce')
df['velocity_kms'] = pd.to_numeric(df['velocity_kms'], errors='coerce')
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# Drop rows with all NaN in numeric columns
numeric_cols = ['height_km', 'velocity_kms', 'latitude', 'longitude']
df_clean = df.dropna(subset=['height_km', 'velocity_kms'], how='all')

# Sort by launch_date (if available, else use index as time)
if 'launch_date' in df_clean.columns:    df_clean['launch_date'] = pd.to_datetime(df_clean['launch_date'], errors='coerce')   df_clean = df_clean.sort_values('launch_date').reset_index(drop=True)
else:    df_clean = df_clean.reset_index(drop=True)

# Fill remaining missing values with forward fill
df_clean[numeric_cols] = df_clean[numeric_cols].fillna(method='ffill').fillna(method='bfill')

print(f"Cleaned data shape: {df_clean.shape[0]} rows")
print(f"Height range: {df_clean['height_km'].min():.1f} - {df_clean['height_km'].max():.1f} km")
print(f"Velocity range: {df_clean['velocity_kms'].min():.3f} - {df_clean['velocity_kms'].max():.3f} km/s")
print(f"Latitude range: {df_clean['latitude'].min():.1f}° - {df_clean['latitude'].max():.1f}°\n")

# EDA VISUALIZATIONS


fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Starlink Satellite Data Analysis', fontsize=16)

# Time series: Height over index
axes[0,0].plot(df_clean.index, df_clean['height_km'], alpha=0.5)
axes[0,0].set_title('Height (km) Over Time')
axes[0,0].set_xlabel('Satellite Index')
axes[0,0].set_ylabel('Height (km)')
axes[0,0].grid(True)

# Time series: Velocity over index
axes[0,1].plot(df_clean.index, df_clean['velocity_kms'], alpha=0.5, color='orange')
axes[0,1].set_title('Velocity (km/s) Over Time')
axes[0,1].set_xlabel('Satellite Index')
axes[0,1].set_ylabel('Velocity (km/s)')
axes[0,1].grid(True)

# SCATTER PLOT
scatter = axes[1,0].scatter(df_clean['longitude'], df_clean['latitude'],   c=df_clean['height_km'], cmap='viridis', s=3, alpha=0.6)
axes[1,0].set_title('Satellite Positions (Latitude vs Longitude)')
axes[1,0].set_xlabel('Longitude')
axes[1,0].set_ylabel('Latitude')
plt.colorbar(scatter, ax=axes[1,0], label='Height (km)')

# HISTOGRAM
axes[1,1].hist(df_clean['velocity_kms'].dropna(), bins=30, alpha=0.7, color='green', edgecolor='black')
axes[1,1].set_title('Velocity Distribution')
axes[1,1].set_xlabel('Velocity (km/s)')
axes[1,1].set_ylabel('Frequency')
axes[1,1].axvline(df_clean['velocity_kms'].mean(), color='red', linestyle='dashed', label=f'Mean: {df_clean["velocity_kms"].mean():.3f}')
axes[1,1].legend()

plt.tight_layout()
plt.savefig('starlink_eda.png', dpi=300, bbox_inches='tight')
print("EDA plots saved as 'starlink_eda.png'")
plt.show()

# DATA PREPARATION FOR TIME SERIES
print(" TIME SERIES DATA PREPARATION ")

# Target: Predict height_km from previous sequence
sequence_length = 10
target_col = 'height_km'
feature_cols = ['height_km', 'velocity_kms', 'latitude', 'longitude']

# Scale data
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(df_clean[feature_cols].values)

def create_sequences(data, seq_length):   X, y = [], []   for i in range(seq_length, len(data)):        X.append(data[i-seq_length:i])        y.append(data[i, 0])  # Predict height_km    return np.array(X), np.array(y)

X, y = create_sequences(data_scaled, sequence_length)

# Train-test split (80-20, maintaining sequence order)
split_idx = int(0.8 * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(f"Sequence length: {sequence_length}")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}\n")

# DEEP LEARNING MODELS


# Model configuration
n_features = X_train.shape[2]
n_units = 64
dropout_rate = 0.2
epochs = 50
batch_size = 64

# Early stopping callback
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Model 1: Simple RNN 

rnn_model = Sequential([
   SimpleRNN(n_units, activation='tanh', return_sequences=True, input_shape=(sequence_length, n_features)),   Dropout(dropout_rate)    SimpleRNN(n_units//2, activation='tanh'),   Dropout(dropout_rate),    Dense(32, activation='relu'),   Dense(1)
])
rnn_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print(rnn_model.summary())

#  Model 2: LSTM 

lstm_model = Sequential([   LSTM(n_units, activation='tanh', return_sequences=True, input_shape=(sequence_length, n_features)),   Dropout(dropout_rate),    LSTM(n_units//2, activation='tanh'),   Dropout(dropout_rate),    Dense(32, activation='relu'),    Dense(1)
])
lstm_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print(lstm_model.summary())

#  Model 3: GRU 

gru_model = Sequential([  GRU(n_units, activation='tanh', return_sequences=True, input_shape=(sequence_length, n_features)),    Dropout(dropout_rate),    GRU(n_units//2, activation='tanh'),   Dropout(dropout_rate),    Dense(32, activation='relu'),  Dense(1)
])
gru_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print(gru_model.summary())

# TRAINING MODELS
print("\n" + "="*60)
print("TRAINING DEEP LEARNING MODELS")
print("="*60)

# Train RNN
print("\nTraining RNN Model...")
rnn_history = rnn_model.fit(X_train, y_train,   epochs=epochs, batch_size=batch_size,  validation_data=(X_test, y_test),  callbacks=[early_stop],  verbose=1)

# Train LSTM
print("\nTraining LSTM Model...")
lstm_history = lstm_model.fit(X_train, y_train,epochs=epochs, batch_size=batch_size, validation_data=(X_test, y_test),callbacks=[early_stop],
verbose=1)

# Train GRU
print("\nTraining GRU Model...")
gru_history = gru_model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size,
validation_data=(X_test, y_test),  callbacks=[early_stop],                           verbose=1)

# MODEL EVALUATION
print("\n" + "="*60)
print("MODEL EVALUATION & METRICS")
print("="*60)

def evaluate_model(model, X_test, y_test, scaler, model_name):    # Predictions    y_pred_scaled = model.predict(X_test)      # Inverse transform to original scale   dummy = np.zeros((len(y_pred_scaled), scaler.scale_.shape[0]))   dummy[:, 0] = y_pred_scaled.flatten()   y_pred = scaler.inverse_transform(dummy)[:, 0]      dummy_y = np.zeros((len(y_test), scaler.scale_.shape[0]))   dummy_y[:, 0] = y_test.flatten()   y_true = scaler.inverse_transform(dummy_y)[:, 0]      # Metrics   mse = mean_squared_error(y_true, y_pred)   rmse = np.sqrt(mse)   mae = mean_absolute_error(y_true, y_pred)   r2 = r2_score(y_true, y_pred)       print(f"\n{model_name} Performance:")    print(f"  MSE  : {mse:.3f}")   print(f"  RMSE : {rmse:.3f} km")    print(f"  MAE  : {mae:.3f} km")   print(f"  R²   : {r2:.4f}")   return y_true, y_pred, mse, rmse, mae, r2

# Evaluate all models
rnn_results = evaluate_model(rnn_model, X_test, y_test, scaler, "RNN")
lstm_results = evaluate_model(lstm_model, X_test, y_test, scaler, "LSTM")
gru_results = evaluate_model(gru_model, X_test, y_test, scaler, "GRU")

# TRAINING VISUALIZATION


fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Model Training History Comparison', fontsize=16)

models = [   (rnn_history, 'RNN', axes[0,0], axes[1,0]),   (lstm_history, 'LSTM', axes[0,1], axes[1,1]),    (gru_history, 'GRU', axes[0,2], axes[1,2])
]

for history, name, ax_loss, ax_mae in models:   # Loss plot   ax_loss.plot(history.history['loss'], label='Train Loss', linewidth=2)   ax_loss.plot(history.history['val_loss'], label='Val Loss', linewidth=2)   ax_loss.set_title(f'{name} - Loss')   ax_loss.set_xlabel('Epoch')   ax_loss.set_ylabel('Loss')   ax_loss.legend()    ax_loss.grid(True)      # MAE plot    ax_mae.plot(history.history['mae'], label='Train MAE', linewidth=2)   ax_mae.plot(history.history['val_mae'], label='Val MAE', linewidth=2)    ax_mae.set_title(f'{name} - MAE')   ax_mae.set_xlabel('Epoch')  ax_mae.set_ylabel('MAE')  ax_mae.legend()  ax_mae.grid(True)

plt.tight_layout()
plt.savefig('training_history.png', dpi=300, bbox_inches='tight')
print(" Training history plots saved as 'training_history.png'")
plt.show()
# PREDICTIONS VISUALIZATIONS


fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Model Predictions vs Actual Values', fontsize=16)

model_results = [
    (rnn_results, 'RNN', axes[0]),    (lstm_results, 'LSTM', axes[1]),    (gru_results, 'GRU', axes[2])
]

for (y_true, y_pred, mse, rmse, mae, r2), name, ax in model_results: ax.scatter(y_true, y_pred, alpha=0.3, s=5)   ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', linewidth=2, label='Ideal')   ax.set_xlabel('Actual Height (km)')   ax.set_ylabel('Predicted Height (km)   ax.set_title(f'{name}\nRMSE: {rmse:.2f} km, R²: {r2:.4f}')   ax.legend()    ax.grid(True)

plt.tight_layout()
plt.savefig('predictions_scatter.png', dpi=300, bbox_inches='tight')
print(" Predictions plot saved as 'predictions_scatter.png'")
plt.show()

# TIME SERIES FORECASTING
print("\n--- GENERATING TIME SERIES FORECAST PLOT ---")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Time Series Predictions (First 200 Samples)', fontsize=16)

model_results_ts = [   (rnn_results, 'RNN', axes[0]),   (lstm_results, 'LSTM', axes[1]),   (gru_results, 'GRU', axes[2])
]

for (y_true, y_pred, mse, rmse, mae, r2), name, ax in model_results_ts:    # Plot first 200 samples    n_samples = min(200, len(y_true))    ax.plot(y_true[:n_samples], label='Actual', linewidth=2, alpha=0.8)   ax.plot(y_pred[:n_samples], label='Predicted', linewidth=2, alpha=0.8, linestyle='--')   ax.set_xlabel('Test Sample Index')    ax.set_ylabel('Height (km)')    ax.set_title(f'{name} - First {n_samples} Predictions')    ax.legend()    ax.grid(True)

plt.tight_layout()
plt.savefig('time_series_forecast.png', dpi=300, bbox_inches='tight')
print(" Time series forecast plot saved as 'time_series_forecast.png'")
plt.show()

# SUMMARIZING
print("\n" + "="*60)
print("FINAL MODEL COMPARISON SUMMARY")
print("="*60)

summary_df = pd.DataFrame({   'Model': ['RNN', 'LSTM', 'GRU'],   'MSE': [rnn_results[2], lstm_results[2], gru_results[2]],   'RMSE': [rnn_results[3], lstm_results[3], gru_results[3]],   'MAE': [rnn_results[4], lstm_results[4], gru_results[4]],    'R²': [rnn_results[5], lstm_results[5], gru_results[5]]
})

print(summary_df.to_string(index=False))

# Identify best model
best_idx = summary_df['RMSE'].idxmin()
best_model_name = summary_df.loc[best_idx, 'Model']
best_rmse = summary_df.loc[best_idx, 'RMSE']

print(f" Best Model: {best_model_name} (RMSE: {best_rmse:.3f} km)")

