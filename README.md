# Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability

# 🐟 Smart Satellite-Based Fish Forecasting System using AI for Environmental Sustainability

### 🎓 Graduation Project 2024–2025

**Faculty of NSST_BSU – Class of 2024/2025,**
**under the sponsorship of EgSA-Egyptian Space Agency.**

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

* Developed LSTM and XGBoost models for SST and chlorophyll prediction.
* Performed data preprocessing, feature engineering, model training, and evaluation.
* Achieved high model accuracy (R² > 0.97) across multiple test years.
* Built fish classification rules and tested output integrity.

### 💻 Embedded Software Team

* Built Python scripts to read from DHT22, GPS, and Pi Camera.
* Simulated NDVI-based chlorophyll estimation from image input.
* Created a Tkinter GUI for local fish monitoring display.

### 🔩 Embedded Hardware Team

* Integrated Raspberry Pi with sensors.
* Designed PCB and tested for power stability and EMI resistance.
* Ensured hardware is space-compatible (thermal/vibration tolerances).

### 🧱 Structural Team

* Designed the 3U CubeSat structure.
* Simulated mechanical stress and thermal conditions.
* Integrated deployment mechanism for solar panels.

### 🛰️ STK & Orbit Design Team

* Designed SSO orbit for maximum Red Sea coverage.
* Simulated coverage and revisit times.
* Provided ground station visibility windows.

### 🌐 Interface System Team

* Built integration pipeline using LabVIEW, Google Colab, and Firebase.
* Divided implementation into two cycles due to lack of real data:

  * **Cycle 1:** LabVIEW dashboard simulates real-time sensor readings.
  * **Cycle 2:** Full pipeline run using re-engineered training data.
* Enabled real-time upload to Firebase and dynamic visualization via G Web.
* Web App enables historical fish detection exploration.

---

## 🧠 Final Outcome

* Complete system that emulates CubeSat-based fish monitoring.
* Can predict fish types & quantities for specific Red Sea regions.
* Provides real-time and historical outputs.
* Designed for easy future integration with real mission data.

---

## ⚙️ Tech Stack

* **Languages**: Python, LabVIEW, MATLAB
* **ML Models**: LSTM, XGBoost
* **Visualization**: Tkinter, Folium, G Web VI
* **Cloud**: Firebase Realtime DB, Google Colab
* **Simulation Tools**: STK, SolidWorks, ANSYS
* **Hardware**: Raspberry Pi 4, GPS, DHT22, Pi Camera

---


---

# 🌐 Interface System – Full Technical Breakdown

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

### 👾 Preocess Video
[](https://github.com/Mohamed-Khalil001/Onboard-Image-Processing-Satellite-Using-AI-For-Environmental-Sustainability/blob/0348806eb4b1b3e7058921333223f7229675739a/PICS%20%26%20Simulations/interface_vid.mp4)

### ✅ Final Highlights

| Capability            | Description                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| 🚧 Partial Simulation | Divided pipeline: LabVIEW kit (real-time) + full Colab cycle (model output) |
| 🌐 Real-Time Sync     | Firebase bridges prediction with UI layers                                  |
| 🧠 Model Integration  | LSTM & XGBoost work in parallel on engineered inputs                        |
| 🐟 Actionable Output  | Outputs fish type & quantity per point                                      |
| 📈 Dual Access        | G Web (live) + Web App (historical lookup)                                  |

---
