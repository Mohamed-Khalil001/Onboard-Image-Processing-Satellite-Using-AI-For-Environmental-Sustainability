import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create output folder
folder_name = "sensors_data"
os.makedirs(folder_name, exist_ok=True)

# Load input data
chl_file = "chl_weekly_style.csv"
sst_file = "sst_weekly_style.csv"
df_chl = pd.read_csv(chl_file).reset_index(drop=True)
df_sst = pd.read_csv(sst_file).reset_index(drop=True)

# Settings
window_size = 12
num_points = len(df_chl) // window_size
now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
month = now.month

# Generate 12 historical weekly timestamps and 1 future prediction timestamp
dates_real = [now - timedelta(weeks=11 - i) for i in range(12)]
date_prediction = now + timedelta(weeks=1)

# Prepare output containers
all_lstm = []
all_xgb = []

for i in range(num_points):
    start_idx = i * window_size
    end_idx = start_idx + window_size

    chl_slice = df_chl.iloc[start_idx:end_idx].copy()
    sst_slice = df_sst.iloc[start_idx:end_idx].copy()

    # LSTM data: 12 weeks + 1 prediction row
    df_real = pd.DataFrame({
        "date": dates_real,
        "lat": sst_slice["lat"].values,
        "lon": sst_slice["lon"].values,
        "sst": sst_slice["sst"].values,
        "chlor_a": chl_slice["chlor_a"].values,
        "qual_sst": sst_slice["qual_sst"].values,
        "is_prediction": False
    })

    # Append one prediction row with the same coordinates and future date
    last_row = df_real.iloc[-1:].copy()
    df_pred = last_row.copy()
    df_pred["date"] = date_prediction
    df_pred["is_prediction"] = True

    df_lstm = pd.concat([df_real, df_pred], ignore_index=True)
    all_lstm.append(df_lstm)

    # XGBoost features from 12 historical weeks
    df_x = pd.DataFrame({
        "chl_diff": chl_slice["chlor_a"].diff().fillna(0),
        "chl_ma3": chl_slice["chlor_a"].rolling(window=3).mean().fillna(method="bfill"),
        "chl_std3": chl_slice["chlor_a"].rolling(window=3).std().fillna(0),
        "sst": sst_slice["sst"],
        "sst_diff": sst_slice["sst"].diff().fillna(0),
        "sst_ma3": sst_slice["sst"].rolling(window=3).mean().fillna(method="bfill"),
        "month_sin": np.sin(2 * np.pi * (month / 12)),
        "month_cos": np.cos(2 * np.pi * (month / 12)),
        "lat": sst_slice["lat"],
        "lon": sst_slice["lon"],
        "date": [d.strftime("%Y-%m-%d %H:%M:%S") for d in dates_real]
    })

    all_xgb.append(df_x)

# Save outputs
pd.concat(all_lstm, ignore_index=True).to_csv(f"{folder_name}/synthetic_lstm_ready_data.csv", index=False)
pd.concat(all_xgb, ignore_index=True).to_csv(f"{folder_name}/synthetic_chlorophyll_features.csv", index=False)

print(f"Generated {num_points} sea points × 12 weeks + 1 prediction row with unified timestamp: {date_prediction.strftime('%Y-%m-%d')}")
