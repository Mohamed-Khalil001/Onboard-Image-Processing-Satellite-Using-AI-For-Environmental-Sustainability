import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("Detection Data", exist_ok=True)

# Load merged data
merged = pd.read_csv("prediction_data/merged_chl_sst.csv")

# Classification function


def classify_fish(temp, chl):
    fish_ranges = [
        ('Sardine',    21, 28, 0.3, 1.5, 500),
        ('Tuna',       24, 31, 0.0, 0.8, 300),
        ('Mackerel',   19, 26, 0.7, 2.0, 400),
        ('Shrimp',     25, 31, 0.8, 2.5, 350),
        ('Baga',       20, 27, 0.5, 1.8, 200),
        ('Mullets',    21, 26, 1.0, 2.8, 250),
        ('Anchovy',    22, 29, 0.2, 1.0, 450),
        ('Grouper',    25, 32, 0.3, 1.3, 180),
        ('Sea Bream',  19, 25, 1.5, 3.5, 300),
        ('Barracuda',  27, 33, 0.0, 0.6, 100),
        ('Snapper',    25, 30, 1.0, 2.5, 280),
        ('Trevally',   24, 29, 0.6, 1.5, 320),
        ('Rabbitfish', 22, 28, 0.7, 2.2, 260),
        ('Emperor',    26, 32, 0.5, 1.4, 220),
        ('Jackfish',   23, 30, 0.4, 1.2, 270),
        ('Spadefish',  20, 26, 1.0, 2.8, 210),
        ('Marlin',     28, 34, 0.0, 0.4, 90),
        ('Grunt',      18, 24, 1.0, 2.5, 150),
        ('Needlefish', 21, 27, 0.3, 1.0, 130),
        ('Parrotfish', 23, 30, 0.7, 2.0, 200),
        ('Bonito',     25, 31, 0.1, 0.6, 240),
        ('Kingfish',   26, 32, 0.0, 0.5, 220),
    ]

    for fish, t_min, t_max, c_min, c_max, max_qty in fish_ranges:
        if t_min <= temp <= t_max and c_min <= chl <= c_max:
            t_center = (t_min + t_max) / 2
            c_center = (c_min + c_max) / 2
            t_score = 1 - abs(temp - t_center) / ((t_max - t_min) / 2)
            c_score = 1 - abs(chl - c_center) / ((c_max - c_min) / 2)
            score = max(0, (t_score + c_score) / 2)
            estimated_qty = int(score * max_qty)
            return pd.Series([fish, estimated_qty])

    return pd.Series(['Others', 0])


# Apply classification to merged data
merged[['fish_type', 'estimated_quantity']] = merged.apply(
    lambda row: classify_fish(
        row['predicted_sst'], row['predicted_chlorophyll']),
    axis=1
)

# Save final output
output_path = "Detection Data/classified_fish_predictions.csv"
merged.to_csv(output_path, index=False)

# Preview result
print("✅ First 5 classified rows:")
print(merged[['date', 'lat', 'lon', 'predicted_sst',
      'predicted_chlorophyll', 'fish_type', 'estimated_quantity']].head())
