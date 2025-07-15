import pandas as pd

# Load prediction CSVs
chl = pd.read_csv("/content/prediction_data/predicted_chlorophyll.csv")
sst = pd.read_csv("/content/prediction_data/predicted_sst.csv")

# Remove first 12 chlorophyll rows to align with LSTM predictions
chl = chl.iloc[12:].reset_index(drop=True)

# Round coordinates to ensure alignment
chl['lat'] = chl['lat'].round(3)
chl['lon'] = chl['lon'].round(3)
sst['lat'] = sst['lat'].round(3)
sst['lon'] = sst['lon'].round(3)

# Ensure consistent date format
chl['date'] = pd.to_datetime(chl['date']).dt.date
sst['date'] = pd.to_datetime(sst['date']).dt.date

# Merge both dataframes on date and coordinates
merged = pd.merge(sst, chl, on=['date', 'lat', 'lon'])

# Preview merged result
print("✅ Number of merged rows:", len(merged))
print(merged.head())

# Save merged data
merged.to_csv("prediction_data/merged_chl_sst.csv", index=False)
