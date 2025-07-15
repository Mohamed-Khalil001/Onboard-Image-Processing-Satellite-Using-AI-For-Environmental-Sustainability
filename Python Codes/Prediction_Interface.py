# ✅ Import libraries
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import joblib
import xgboost as xgb
from tensorflow.keras.models import load_model

# ✅ Create folder for predictions
os.makedirs("prediction_data", exist_ok=True)

# ⬅️ 1. Run XGBoost Model (Chlorophyll Prediction)

# Load XGBoost input data
xgb_data = pd.read_csv(
    "/content/sensors_data/synthetic_chlorophyll_features.csv")

# Store coordinates
xgb_lat = xgb_data['lat']
xgb_lon = xgb_data['lon']

# Store prediction target date (next week)
next_week_date = (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")

# Drop non-numeric columns
xgb_features = xgb_data.drop(columns=['date'])

# Normalize using a new scaler (should match training config if saved)
scaler_xgb = StandardScaler()
xgb_scaled = scaler_xgb.fit_transform(xgb_features)

# Load trained XGBoost model
xgb_model = joblib.load("/content/xgboost_chlorophyll_model.pkl")

# Predict (output is log1p-transformed)
y_pred_log = xgb_model.predict(xgb_scaled)
y_pred_chla = np.expm1(y_pred_log)  # Convert back to normal scale

# Extract only one row per sea point (last row of 12-week window)
window_size = 12
predicted_chla = y_pred_chla[window_size-1::window_size]
lat_chla = xgb_lat[window_size-1::window_size].reset_index(drop=True)
lon_chla = xgb_lon[window_size-1::window_size].reset_index(drop=True)

# Save chlorophyll predictions
df_chla = pd.DataFrame({
    'date': [next_week_date] * len(predicted_chla),
    'lat': lat_chla,
    'lon': lon_chla,
    'predicted_chlorophyll': predicted_chla
})
df_chla.to_csv("prediction_data/predicted_chlorophyll.csv", index=False)

# ⬅️ 2. Run LSTM Model (SST Prediction)

# Load pre-trained LSTM model
lstm_model = load_model("/content/sst_lstm_model (1).h5", compile=False)

# Load LSTM input data
sst_data = pd.read_csv("/content/sensors_data/synthetic_lstm_ready_data.csv")
features = ['lat', 'lon', 'sst', 'qual_sst']

# Normalize input features
scaler_lstm = MinMaxScaler()
scaled = scaler_lstm.fit_transform(sst_data[features])

# Create sequences (12 weeks per point)
X = [scaled[i:i+window_size]
     for i in range(len(scaled) - window_size + 1) if (i + 1) % window_size == 0]
X = np.array(X)

# Predict SST
y_pred = lstm_model.predict(X)

# Reverse scaling for SST only
temp = np.zeros((y_pred.shape[0], len(features)))
temp[:, 2] = y_pred[:, 0]  # Only SST column
sst_back = scaler_lstm.inverse_transform(temp)[:, 2]

# Get corresponding lat/lon from last rows of each window
last_rows_lstm = sst_data.iloc[window_size -
                               1::window_size].reset_index(drop=True)
# Align length with predictions
last_rows_lstm = last_rows_lstm.iloc[:len(sst_back)]

# Save SST predictions
df_sst = pd.DataFrame({
    'date': [next_week_date] * len(sst_back),
    'lat': last_rows_lstm['lat'],
    'lon': last_rows_lstm['lon'],
    'predicted_sst': sst_back
})
df_sst.to_csv("prediction_data/predicted_sst.csv", index=False)

print("✅ Weekly predictions for SST and Chlorophyll saved in 'prediction_data/'")
