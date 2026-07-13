# WORKING WITH THE 2026 TECH MEGA IPO UNICORN ANALYSIS
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
df = pd.read_csv(r'C:\Users\PMLS\Documents\GitHub\My_Course_AI_Bin\All DataSets\Final_Assessment_DataSets\The 2026 Tech Mega\data.csv')
print("="*60)
print("IPO UNICORN TIME SERIES ANALYSIS")
print("="*60)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")

# DATA PREPROCESSING


# Clean column names
df.columns = df.columns.str.strip()

# Convert year founded to numeric
df['year_founded'] = pd.to_numeric(df['year_founded'], errors='coerce')

# Clean numeric columns
numeric_cols = ['ipo_valuation_usd_b', 'last_private_valuation_usd_b', 'amount_raised_usd_b',   'latest_annual_revenue_or_arr_usd_b', 'valuation_to_revenue_multiple', 'years_to_ipo']

for col in numeric_cols:   df[col] = pd.to_numeric(df[col], errors='coerce')

# Fill missing values
df['valuation_to_revenue_multiple'].fillna(df['valuation_to_revenue_multiple'].median(), inplace=True)
df['years_to_ipo'].fillna(df['years_to_ipo'].median(), inplace=True)

# Sort by year founded to create time series
df = df.sort_values('year_founded').reset_index(drop=True)

# Create additional time-based features
df['company_age_at_ipo'] = df['years_to_ipo']
df['valuation_growth'] = df['ipo_valuation_usd_b'] - df['last_private_valuation_usd_b']
df['valuation_growth_pct'] = (df['valuation_growth'] / df['last_private_valuation_usd_b']) * 100

# Handle infinite values
df['valuation_growth_pct'] = df['valuation_growth_pct'].replace([np.inf, -np.inf], np.nan)
df['valuation_growth_pct'].fillna(df['valuation_growth_pct'].median(), inplace=True)

print(f"Cleaned data shape: {df.shape[0]} rows")
print(f"Year range: {df['year_founded'].min():.0f} - {df['year_founded'].max():.0f}")
print(f"Valuation range: ${df['ipo_valuation_usd_b'].min():.1f}B - ${df['ipo_valuation_usd_b'].max():.0f}B")
print(f"Average years to IPO: {df['years_to_ipo'].mean():.1f} years\n")

# EDA VISUALIZATIONS


fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('IPO Unicorn Time Series Analysis', fontsize=16)

# Time series: Valuation over founding year
axes[0,0].scatter(df['year_founded'], df['ipo_valuation_usd_b'], alpha=0.6, s=50)
axes[0,0].plot(df['year_founded'], df['ipo_valuation_usd_b'], alpha=0.3, linestyle='--')
axes[0,0].set_title('IPO Valuation Over Founding Year')
axes[0,0].set_xlabel('Year Founded')
axes[0,0].set_ylabel('IPO Valuation (USD B)')
axes[0,0].grid(True)

# Time series: Revenue over founding year
axes[0,1].scatter(df['year_founded'], df['latest_annual_revenue_or_arr_usd_b'], alpha=0.6, s=50, color='orange')
axes[0,1].plot(df['year_founded'], df['latest_annual_revenue_or_arr_usd_b'], alpha=0.3, linestyle='--', color='orange')
axes[0,1].set_title('Revenue Over Founding Year')
axes[0,1].set_xlabel('Year Founded')
axes[0,1].set_ylabel('Revenue (USD B)')
axes[0,1].grid(True)

# SCATTER PLOT
scatter = axes[1,0].scatter(df['years_to_ipo'], df['ipo_valuation_usd_b'],    c=df['valuation_to_revenue_multiple'], cmap='viridis', s=100, alpha=0.6)
axes[1,0].set_title('Years to IPO vs Valuation')
axes[1,0].set_xlabel('Years to IPO')
axes[1,0].set_ylabel('IPO Valuation (USD B)')
plt.colorbar(scatter, ax=axes[1,0], label='Valuation/Revenue Multiple')

# HISTOGRAM
axes[1,1].hist(df['ipo_valuation_usd_b'], bins=15, alpha=0.7, color='green', edgecolor='black')
axes[1,1].set_title('IPO Valuation Distribution')
axes[1,1].set_xlabel('Valuation (USD B)')
axes[1,1].set_ylabel('Frequency')
axes[1,1].axvline(df['ipo_valuation_usd_b'].mean(), color='red', linestyle='dashed', label=f'Mean: {df["ipo_valuation_usd_b"].mean():.1f}B')
axes[1,1].legend()

plt.tight_layout()
plt.savefig('ipo_time_series_eda.png', dpi=300, bbox_inches='tight')
print(" EDA plots saved as 'ipo_time_series_eda.png'")
plt.show()




# Select features for time series prediction
# We want to predict IPO valuation based on historical patterns
feature_cols = ['last_private_valuation_usd_b', 'amount_raised_usd_b',     'latest_annual_revenue_or_arr_usd_b', 'valuation_to_revenue_multiple',   'years_to_ipo', 'company_age_at_ipo']

target_col = 'ipo_valuation_usd_b'

# Normalize the data
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(df[feature_cols + [target_col]].values)

# Create sequences for time series prediction
sequence_length = 5  # Use 5 previous companies to predict next

def create_sequences(data, seq_length, target_idx=-1):   X, y = [], []   for i in range(seq_length, len(data)):   X.append(data[i-seq_length:i, :-1])  # All features except target    y.append(data[i, target_idx])  # Target column   return np.array(X), np.array(y)

X, y = create_sequences(data_scaled, sequence_length)

# Train-test split (80-20, maintaining sequence order)
split_idx = int(0.8 * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(f"Sequence length: {sequence_length}")
print(f"Number of features: {len(feature_cols)}")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}\n")
# DEEP LEARNING MODELS


# Model configuration
n_features = X_train.shape[2]
n_units = 64
dropout_rate = 0.2
epochs = 100
batch_size = 8

# Early stopping callback
early_stop = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)

# Model 1: Simple RNN 

rnn_model = Sequential([   SimpleRNN(n_units, activation='tanh', return_sequences=True, input_shape=(sequence_length, n_features)),    Dropout(dropout_rate),    SimpleRNN(n_units//2, activation='tanh')    Dropout(dropout_rate),    Dense(32, activation='relu'),    Dense(16, activation='relu'),    Dense(1)
])
rnn_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print(rnn_model.summary())

#  Model 2: LSTM 

lstm_model = Sequential([   LSTM(n_units, activation='tanh', return_sequences=True, input_shape=(sequence_length, n_features)),   Dropout(dropout_rate),   LSTM(n_units//2, activation='tanh'),   Dropout(dropout_rate),   Dense(32, activation='relu'),    Dense(16, activation='relu'),    Dense(1)
])
lstm_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print(lstm_model.summary())

#  Model 3: GRU 

gru_model = Sequential([   GRU(n_units, activation='tanh', return_sequences=True, input_shape=(sequence_length, n_features)),   Dropout(dropout_rate),   GRU(n_units//2, activation='tanh'),   Dropout(dropout_rate),    Dense(32, activation='relu'),    Dense(16, activation='relu'),    Dense(1)
])
gru_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print(gru_model.summary())
# TRAINING MODELS
print("\n" + "="*60)
print("TRAINING DEEP LEARNING MODELS")
print("="*60)

# Train RNN
print("\nTraining RNN Model...")
rnn_history = rnn_model.fit(X_train, y_train,   epochs=epochs, batch_size=batch_size,  validation_data=(X_test, y_test),  callbacks=[early_stop],   verbose=1)

# Train LSTM
print("\nTraining LSTM Model...")
lstm_history = lstm_model.fit(X_train, y_train,epochs=epochs, batch_size=batch_size,
validation_data=(X_test, y_test),callbacks=[early_stop],                            verbose=1)

# Train GRU
print("\nTraining GRU Model...")
gru_history = gru_model.fit(X_train, y_train,  epochs=epochs, batch_size=batch_size,  validation_data=(X_test, y_test),   callbacks=[early_stop],   verbose=1)

# MODELS EVALUATION STARTING
print("\n" + "="*60)
print("MODEL EVALUATION & METRICS")
print("="*60)

def evaluate_model(model, X_test, y_test, scaler, model_name):     y_pred_scaled = model.predict(X_test)         dummy = np.zeros((len(y_pred_scaled), scaler.scale_.shape[0]))   dummy[:, -1] = y_pred_scaled.flatten()      y_pred = scaler.inverse_transform(dummy)[:, -1]        dummy_y = np.zeros((len(y_test), scaler.scale_.shape[0]))    dummy_y[:, -1] = y_test.flatten()    y_true = scaler.inverse_transform(dummy_y)[:, -1]            mse = mean_squared_error(y_true, y_pred)    rmse = np.sqrt(mse)    mae = mean_absolute_error(y_true, y_pred)    r2 = r2_score(y_true, y_pred)        print(f"\n{model_name} Performance:")    print(f"  MSE  : {mse:.3f}")    print(f"  RMSE : {rmse:.3f} USD B")    print(f"  MAE  : {mae:.3f} USD B")    print(f"  R²   : {r2:.4f}")    return y_true, y_pred, mse, rmse, mae, r2

# Evaluate all models
rnn_results = evaluate_model(rnn_model, X_test, y_test, scaler, "RNN")
lstm_results = evaluate_model(lstm_model, X_test, y_test, scaler, "LSTM")
gru_results = evaluate_model(gru_model, X_test, y_test, scaler, "GRU")


print(" GENERATING TRAINING HISTORY PLOTS ")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Model Training History Comparison', fontsize=16)

models = [    (rnn_history, 'RNN', axes[0,0], axes[1,0]),    (lstm_history, 'LSTM', axes[0,1], axes[1,1]),   (gru_history, 'GRU', axes[0,2], axes[1,2])
]

for history, name, ax_loss, ax_mae in models:  ax_loss.plot(history.history['loss'], label='Train Loss', linewidth=2)    ax_loss.plot(history.history['val_loss'], label='Val Loss', linewidth=2)    ax_loss.set_title(f'{name} - Loss')    ax_loss.set_xlabel('Epoch')    ax_loss.set_ylabel('Loss')   ax_loss.legend()     ax_loss.grid(True)    ax_mae.plot(history.history['mae'], label='Train MAE', linewidth=2)    ax_mae.plot(history.history['val_mae'], label='Val MAE', linewidth=2)    ax_mae.set_title(f'{name} - MAE')    ax_mae.set_xlabel('Epoch')    ax_mae.set_ylabel('MAE')    ax_mae.legend()   ax_mae.grid(True)

plt.tight_layout()
plt.savefig('ipo_training_history.png', dpi=300, bbox_inches='tight')
print("Training history plots saved as 'ipo_training_history.png'")
plt.show()



fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Model Predictions vs Actual Values', fontsize=16)

model_results = [   (rnn_results, 'RNN', axes[0]),   (lstm_results, 'LSTM', axes[1]),    (gru_results, 'GRU', axes[2])
]

for (y_true, y_pred, mse, rmse, mae, r2), name, ax in model_results:   ax.scatter(y_true, y_pred, alpha=0.6, s=80)   ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', linewidth=2, label='Ideal')    ax.set_xlabel('Actual Valuation (USD B)')    ax.set_ylabel('Predicted Valuation (USD B)')    ax.set_title(f'{name}\nRMSE: {rmse:.2f}B, R²: {r2:.4f}')   ax.legend()    ax.grid(True)

plt.tight_layout()
plt.savefig('ipo_predictions_scatter.png', dpi=300, bbox_inches='tight')
print(" Predictions plot saved as 'ipo_predictions_scatter.png'")
plt.show()

# TIME SERIES FORECASTING


fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Time Series Predictions (All Test Samples)', fontsize=16)

model_results_ts = [    (rnn_results, 'RNN', axes[0]),    (lstm_results, 'LSTM', axes[1]),    (gru_results, 'GRU', axes[2])
]

for (y_true, y_pred, mse, rmse, mae, r2), name, ax in model_results_ts:    ax.plot(y_true, label='Actual', linewidth=2, alpha=0.8, marker='o', markersize=4)    ax.plot(y_pred, label='Predicted', linewidth=2, alpha=0.8, linestyle='--', marker='s', markersize=4)    ax.set_xlabel('Test Sample Index')    ax.set_ylabel('IPO Valuation (USD B)')   ax.set_title(f'{name} - All Test Predictions\nRMSE: {rmse:.2f}B')   ax.legend()    ax.grid(True)

plt.tight_layout()
plt.savefig('ipo_time_series_forecast.png', dpi=300, bbox_inches='tight')
print("Time series forecast plot saved as 'ipo_time_series_forecast.png'")
plt.show()

# FINALIZING
print("\n" + "="*60)
print("FINAL MODEL COMPARISON SUMMARY")
print("="*60)

summary_df = pd.DataFrame({    'Model': ['RNN', 'LSTM', 'GRU'],    'MSE': [rnn_results[2], lstm_results[2], gru_results[2]],    'RMSE': [rnn_results[3], lstm_results[3], gru_results[3]],    'MAE': [rnn_results[4], lstm_results[4], gru_results[4]],   'R²': [rnn_results[5], lstm_results[5], gru_results[5]]
})

print(summary_df.to_string(index=False))

# Identify best model
best_idx = summary_df['R²'].idxmax()
best_model_name = summary_df.loc[best_idx, 'Model']
best_r2 = summary_df.loc[best_idx, 'R²']

print(f" Best Model: {best_model_name} (R²: {best_r2:.4f})")


print(" ADDITIONAL INSIGHTS ")

# Calculate prediction accuracy
best_model = None
if best_model_name == 'RNN':    best_model = rnn_model
elif best_model_name == 'LSTM':   best_model = lstm_model
else:    best_model = gru_model

y_pred_best_scaled = best_model.predict(X_test)
dummy = np.zeros((len(y_pred_best_scaled), scaler.scale_.shape[0]))
dummy[:, -1] = y_pred_best_scaled.flatten()
y_pred_best = scaler.inverse_transform(dummy)[:, -1]

dummy_y = np.zeros((len(y_test), scaler.scale_.shape[0]))
dummy_y[:, -1] = y_test.flatten()
y_true_best = scaler.inverse_transform(dummy_y)[:, -1]

# Percentage error
percentage_errors = np.abs((y_true_best - y_pred_best) / y_true_best) * 100
print(f"Average Prediction Error: {percentage_errors.mean():.1f}%")
print(f"Median Prediction Error: {percentage_errors.median():.1f}%")
print(f"Best Prediction Error: {percentage_errors.min():.1f}%")
print(f"Worst Prediction Error: {percentage_errors.max():.1f}%")

print(" Time Series Analysis Complete!")
