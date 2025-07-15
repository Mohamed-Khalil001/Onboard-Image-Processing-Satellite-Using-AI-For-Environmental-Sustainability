import os
import pandas as pd
import json
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

# Create folder to store local JSON output
folder = "firebase_data"
os.makedirs(folder, exist_ok=True)

# Load Firebase credentials (adjust path as needed)
cred_path = "/content/drive/My Drive/Fish_database/fish-monitor-efd05-firebase-adminsdk-fbsvc-e0a1cfe228.json"
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://fish-monitor-efd05-default-rtdb.firebaseio.com'
    })

# Define file paths
csv_path = "/content/Detection Data/classified_fish_predictions.csv"
json_path = os.path.join(folder, "classified_fish.json")

# Load full dataset once
df = pd.read_csv(csv_path)
total_rows = len(df)
chunk_size = 10
index = 0

# Real-time update loop
try:
    while True:
        if index >= total_rows:
            index = 0  # Restart from beginning when finished

        # Get 10 rows at a time
        batch = df.iloc[index:index + chunk_size]
        index += chunk_size

        json_output = []
        archive_data = []

        for _, row in batch.iterrows():
            short_date = pd.to_datetime(row['date']).strftime('%d-%m')
            text = f"{short_date} | F:{row['fish_type']} | T:{row['predicted_sst']:.1f} | C:{row['predicted_chlorophyll']:.2f} | Q:{row['estimated_quantity']}"

            entry = {
                "coordinate": {
                    "latitude": float(row['lat']),
                    "longitude": float(row['lon'])
                },
                "text": text
            }
            json_output.append(entry)

            # For archive
            archive_data.append({
                "date": row['date'],
                "lat": float(row['lat']),
                "lon": float(row['lon']),
                "predicted_sst": float(row['predicted_sst']),
                "predicted_chlorophyll": float(row['predicted_chlorophyll']),
                "fish_type": row['fish_type'],
                "estimated_quantity": int(row['estimated_quantity'])
            })

        # Save JSON locally
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_output, f, indent=2)

        # Push real-time update to Firebase
        db.reference("/fishdata").set(json_output)

        # Push archive snapshot
        db.reference("/fishdata_archive").push({
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "data": archive_data
        })

        print(f"✅ Updated at: {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(6)

except KeyboardInterrupt:
    print("\n🛑 Stopped by user.")
