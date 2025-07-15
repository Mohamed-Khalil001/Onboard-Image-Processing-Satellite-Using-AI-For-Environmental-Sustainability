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

### 🌐 Interface System – Full Technical Breakdown

The Interface System in our project acts as the *nerve center* that connects simulated sensor data, machine learning predictions, cloud storage, and interactive dashboards. Due to the lack of real mission data, we divided the implementation into **two partial cycles**:

1. **First half** simulates the real sensor layer and its interface with LabVIEW.
2. **Second half** continues the pipeline using training data, simulating a complete system from preprocessing to real-time and historical visualization.

![image](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/0-System_Inteface.PNG)

---

### 🔷 **Stage 1: Sensor Simulation + LabVIEW Kit**

#### 🧩 Components:

* DHT Sensor (SST – simulated)
* Camera/NDVI (Chlorophyll – simulated)
* GPS Module (simulated coordinates)

#### 🛠 Description:

Since no live mission data was available, we developed a LabVIEW **dashboard kit** to simulate the sensor interface.

* The Raspberry Pi streams sensor values to LabVIEW over **TCP/IP**.
* The dashboard visualizes the values in real-time using indicators and charts.

⚠️ This phase **does not upload to Firebase** because the data isn’t real yet. Once the mission is live, Firebase upload will be activated.

#### 🖼 LabVIEW Dashboard :

![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/1-Raspberry%20Pi%20%20and%20LabVIEW%20Interface.png)

---

### 🔷 **Stage 2: Synthetic Data → Full Colab Cycle**

#### 🧩 Data Engineering:

To simulate real pipeline behavior:

* Took training data CSVs (`sst_weekly_style.csv`, `chl_weekly_style.csv`)
* Removed timestamps and injected artificial current dates
* Generated weekly data per location (12 weeks)

Created two engineered DataFrames:

* For LSTM: 12-week sequences
* For XGBoost: feature-extracted snapshots

[🔗_Code](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/Python%20Codes/Data_Preparation.py)

#### 🖼 Full Colab Cycle:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/2-%20Colab%20as%20the%20Core%20Interface.png)
#### 🖼 Data Engineering output:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/3-%20Data%20Sensors%20%26%20Prediction%20Models%20Interface.png)

---

### 🔷 **Stage 3: Model Prediction (LSTM + XGBoost)**

#### 🧠 Models:

* `lstm_sst.h5` → Predict SST
* `xgb_chlorophyll.joblib` → Predict Chlorophyll

#### 🛠 Description:

Each model receives its respective preprocessed DataFrame and outputs predictions for week 13.

* Proper scaling applied (`MinMaxScaler`, `StandardScaler`)
* Results exported to CSV

[🔗_Prediction Code](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/Python%20Codes/Prediction_Interface.py)
[🔗_Merge Prediction Code outputs](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/Python%20Codes/Prediction_Interface.py)

#### 🖼 prediction outputs:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/3-prediction_output.PNG)
#### 🖼 Merge prediction outputs:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/4-prediction_file_integration.PNG)


---

### 🔷 **Stage 4: Detection & Fish Classification**

#### 🐟 Algorithm:

Predicted SST and Chlorophyll are merged by location.

* Classification logic assigns **fish type and quantity**
* Based on temperature/chlorophyll suitability ranges

[🔗_Detection Algorithm interface ](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/Python%20Codes/Detiction_pridiction_interface.py)


#### 🖼 Detection outputs:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/4-%20Prediction%20Data%20%26%20Detection%20Fish%20Interface.png)


---

### 🔷 **Stage 5: Firebase Upload (Live Feed + Archive)**

#### 🔁 Description:

Simulated fish detection results are:

* Streamed to `/fishdata` every minute (latest 20 points)
* Archived fully in `/fishdata_archive`

This enables both real-time and historical data views.

[🔗_Firebase interface ](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/Python%20Codes/Detiction_pridiction_interface.py)


#### 🖼 Firebase interface outputs:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/5-%20Firebase%20Upload%20Interface(Realtime%20%26%20Archive).png)

---

### 🔷 **Stage 6: G Web Dashboard (Live Map)**

#### 📍 Tool:

LabVIEW G Web Development (WebVI + Leaflet.js)

#### 🛠 Description:

* Fetches data from Firebase `/fishdata`
* Renders live Red Sea map with fish markers
* Marker tooltip shows fish type, quantity, SST, Chl-a, and date

[🔗VI interface](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/Labview_Gweb_Codes/Labview%20and%20RPI%20interface.vi)


#### 🖼 G_web Code:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/6-%20G%20Web%20Interface%20(Realtime%20display).png)
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/6-%20G%20Web%20Interface%20(Realtime%20display)1.png)
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/6-%20G%20Web%20Interface%20(Realtime%20display)2.png)
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/6-%20G%20Web%20Interface%20(Realtime%20display)3.png)
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/6-%20G%20Web%20Interface%20(Realtime%20display)4.png)

---

### 🔷 **Stage 7: Web App (Historical Lookup)**

#### 🌐 Tools:

* Python, Flask or Streamlit (Web interface)

#### 🛠 Description:

* User selects date
* App pulls `/fishdata_archive` entries
* Displays them in table or map form

#### 🔗 Code:

`/webapp/historical_fish_viewer.py`

#### 🖼 Placeholder for Image:

`[Insert Web App UI screenshot]`

---
## Final Result 
interactive real time Map with furue date , sst , chl , fish type and Quantity for every single coordinate
#### 🖼 G_web Map:
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/real_time_G_web_result2.PNG)
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/real_time_G_web_result1.PNG)

###👾 Preocess Video
![](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/e789147c8febb4229b4af19059b2307d246d164c/PICS%20%26%20Simulations/real_time_G_web_result1.PNG)

### ✅ Final Highlights

| Capability            | Description                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| 🚧 Partial Simulation | Divided pipeline: LabVIEW kit (real-time) + full Colab cycle (model output) |
| 🌐 Real-Time Sync     | Firebase bridges prediction with UI layers                                  |
| 🧠 Model Integration  | LSTM & XGBoost work in parallel on engineered inputs                        |
| 🐟 Actionable Output  | Outputs fish type & quantity per point                                      |
| 📈 Dual Access        | G Web (live) + Web App (historical lookup)                                  |

---
