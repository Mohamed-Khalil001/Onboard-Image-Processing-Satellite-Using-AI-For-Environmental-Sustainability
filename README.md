# Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability
# 🐟 Smart Satellite-Based Fish Forecasting System using AI for Environmental Sustainability

### 🎓 Graduation Project 2024–2025

*Faculty of Navigation Science and space Technology*

---

## 📌 Overview

This project presents a complete AI-powered system that utilizes satellite data and embedded systems to predict potential fish aggregation zones in the Red Sea. By integrating remote sensing, machine learning, embedded software, and real-time dashboards, the system aims to support sustainable fishing practices and environmental monitoring.

---

## 🧩 Project Architecture

1. **Satellite Data Collection**

   * Uses MODIS & Sentinel-3 for historical SST & Chlorophyll-a.
   * Preprocessing: Cleaning, filtering, spatial-temporal alignment.

2. **AI Modeling**

   * **XGBoost**: Predicts chlorophyll concentration based on derived features.
   * **LSTM**: Predicts future SST values using sequential data.
   * Rule-based fish classification based on SST/Chl thresholds for 20+ species.

3. **Fish Detection Algorithm**

   * Classifies fish type + estimated quantity for each geo-point.
   * Generates CSV files for visualization and dashboard use.

4. **Embedded System Simulation**

   * Simulates a CubeSat using Raspberry Pi.
   * Collects GPS + environmental data (SST/Chl) + image capture.
   * Stores locally and interfaces with cloud pipelines.

5. **Interface & Visualization**

   * Google Colab: Hosts full pipeline from data to detection.
   * Firebase: Real-time & archive data storage.
   * LabVIEW G Web: Real-time interactive map for predictions.
   * Web App: Historical fish presence query by date.

---

## 👥 Team Contributions

### 🤖 AI Team

* Built LSTM and XGBoost models for SST and chlorophyll prediction.
* Conducted feature engineering, model training & evaluation (R^2 > 0.97).
* Developed rule-based classification to estimate fish type & quantity.
* Evaluated predictions across multiple years for model robustness.

### 💻 Embedded Software Team

* Built Python scripts for collecting sensor data (DHT22, GPS, Camera).
* Implemented NDVI processing from captured images to estimate chlorophyll.
* Enabled real-time CSV generation for integration with AI models.
* Developed local GUI using Tkinter for visual monitoring of fish detection.

### 🔩 Embedded Hardware Team

* Assembled Raspberry Pi with sensors (GPS, DHT22, Pi Camera).
* Designed the PCB and power systems.
* Tested circuit reliability, EMI tolerance, and runtime power efficiency.
* Ensured data collection hardware matched mission requirements.

### 🧱 Structural Team

* Designed the 3U CubeSat enclosure.
* Ran simulations (thermal, stress, vibration) via ANSYS/SolidWorks.
* Built models for deployable solar panels & mounting supports.
* Ensured mechanical integration for sensors, boards, and shielding.

### 🛰️ STK & Orbit Design Team

* Designed sun-synchronous orbit (SSO) for Red Sea coverage.
* Simulated revisit time, coverage area, and ground masks using STK.
* Provided mission profiles and communication window analysis.
* Delivered orbital data to synchronize AI/ground station timing.

### 🌐 Interface System Team

* Designed full integration layer using Google Colab, Firebase, and LabVIEW.
* Simulated sensor input and automated 12-week sequence generation.
* Integrated LSTM + XGBoost predictions with rule-based detection.
* Built real-time update pipeline to Firebase (/fishdata, /archive).
* Developed G Web dashboard + Python web app for live/historical visualization.

---

## 🧠 Final Outcome

* A fully functional system that mimics a real CubeSat fish-monitoring workflow.
* Can predict fish type and quantity based on weekly environmental data.
* Supports field use (offline GUI) and cloud deployment (Firebase/Web).
* Easily expandable to support new sensors, fish types, or geographic areas.

---

## ⚙️ Tech Stack

* **Languages**: Python, LabVIEW, MATLAB
* **ML Models**: LSTM, XGBoost
* **Visualization**: Tkinter, Folium, G Web VI
* **Cloud**: Firebase Realtime DB, Google Colab
* **Simulation Tools**: STK, SolidWorks, ANSYS
* **Hardware**: Raspberry Pi 4, GPS, DHT22, Pi Camera, Solar cells

---
# 🌐 Interface System – Detailed Module (Our Team)

The Interface System forms the connective core between data generation, model prediction, classification, and real-time user visualization. Below is a standalone deep dive into the Interface subsystem, decoupled from other project components:

---

#### 🧪 1. Sensor Data Simulation & Structuring

* The simulation mimics a real-world CubeSat data feed using Google Colab.
* Three key environmental parameters are simulated:

  * 🌡️ **SST**: Sea Surface Temperature values over time
  * 🌿 **Chlorophyll-a**: Derived from NDVI-like proxy data
  * 📍 **GPS**: Static lat/lon pairs for 1100 sea locations
* A 12-week window is created for each location using sliding sequences (time-series format).
* Output files:

  * `sst_weekly_style.csv`
  * `chl_weekly_style.csv`
* These are stored locally in Colab and synced with Drive for persistence.

---

#### 🔄 2. AI Model Integration (LSTM + XGBoost)

* **LSTM Model**:

  * Input: A sequence of 12 weekly readings per point for SST, lat/lon, and quality.
  * Output: One predicted SST value (for week 13).
  * Scaling: `MinMaxScaler` is applied before feeding sequences into the LSTM model.
  * Postprocessing: Inverse scaling used to recover the true SST value.
* **XGBoost Model**:

  * Input: A feature-based tabular record per location (averages, STD, diffs, seasonality).
  * Output: Log-transformed Chl-a prediction → `exp1m()` used to revert.
  * Scaling: `StandardScaler` is applied on the features.
* Both predictions are saved as:

  * `predicted_sst.csv`
  * `predicted_chlorophyll.csv`

---

#### 🧩 3. Prediction + Detection Bridge

* Using `pandas.merge()` the two files are joined by `date`, `lat`, and `lon`.
* A custom Python function (`classify_fish`) is defined:

  * Contains rule ranges for 21 fish species (SST min/max, Chl min/max, max weight).
  * For each point, it calculates a **score** based on closeness to optimal SST/Chl.
  * Score is then multiplied by max weight to estimate quantity.
  * If no range matched → returns `"Others"`, `0` kg.
* Resulting CSV is:

  * `classified_fish_predictions.csv`
  * Columns: `date`, `lat`, `lon`, `sst`, `chl-a`, `fish_type`, `estimated_quantity`

---

#### ☁️ 4. Firebase Integration – Dual Stream

* Firebase setup includes two paths:

  1. `/fishdata` → updated every minute with 20 random rows from latest predictions
  2. `/fishdata_archive` → full batch uploaded every minute with timestamp
* Libraries used:

  * `pyrebase`
  * `firebase_admin`
* The script includes:

  * Loading classified predictions
  * Random sampling (`df.sample(20)`) every loop
  * Writing to local `classified_fish.json`
  * Pushing to Firebase via `db.reference().set()` and `.push()`
* The loop runs every 60 seconds using `time.sleep(60)` and resets when reaching EOF.

---

#### 🗺️ 5. Real-time Visualization with G Web

* Built using **LabVIEW G Web Development Environment**:

  * Designed a front-end to fetch and visualize data from `/fishdata`.
  * Live map displays 20 points, refreshed every minute.
  * Tooltip on each point displays:

    * 🐠 Fish species
    * 📦 Estimated quantity
    * 🌊 Predicted SST
    * 🍃 Predicted Chl-a
    * 📍 Coordinates + 📆 date
* The map updates using built-in Firebase polling without refresh.

---

#### 📆 6. Historical Web App (Python Flask – Optional Module)

* A minimal Flask-based web interface was implemented for demo:

  * Reads data from `/fishdata_archive` or local archived CSVs
  * Allows the user to pick a date (via calendar input)
  * Displays a table with fish locations, types, and quantities for that date
* Optionally renders a static map with pins (using `folium`)
* Can be hosted locally or via Render.com for free

---

#### ✅ Interface Highlights

* **End-to-end Pipeline**: Sensor → AI → Detection → Dashboard
* **Randomized Real-Time Updates**: Live map always displays diverse points
* **Modular Scripts**: Each block (simulation, prediction, upload) can run independently
* **Firebase-Powered Dashboards**: No need for traditional server setup
* **Zero Manual Interaction**: Fully automatic once launched from Colab
* **Free Infrastructure**: Utilized free tiers of Google Colab, Firebase, and G Web

---

This interface system bridged the gap between prediction and visualization, transforming raw outputs into interactive insights for environmental intelligence and marine sustainability.


## 📬 Contact

**Team Members:** See report cover or project documentation.

**For inquiries:** [example@email.com](mailto:example@email.com)
