

# 🌊 DisasterGuard AI

### AI-Powered Flood Disaster Intelligence & Decision Support System

**Developed as part of the IEEE-SMC-KGEC Internship 2026**

🔗 Internship Repository:  
https://github.com/ieeesmckgec-student-branch-chapter/IEEE-SMC-KGEC-Internship-2026

---

## 👥 Team Members

- **Adrish**
- **Gowtami**

---

## 📌 Project Overview

**DisasterGuard AI** is an AI-powered flood disaster intelligence and decision-support prototype designed to assist in flood forecasting, flood-area identification, impact assessment, risk analysis, and evacuation planning.

Instead of relying on a single machine-learning model, DisasterGuard combines multiple AI components into a unified pipeline:

```text
                DISASTERGUARD AI
                       │
        ┌──────────────┴──────────────┐
        │                             │
 Flood Forecasting             Satellite Analysis
        │                             │
 Bayesian Neural Network            U-Net
        │                             │
 Flood Probability              Flood Mask
 + Uncertainty                  Flooded Area %
        │                             │
        └──────────────┬──────────────┘
                       ▼
              IMPACT ASSESSMENT
                       │
                       ▼
                 RISK FUSION
                       │
                       ▼
                FINAL RISK LEVEL
                       │
                       ▼
              EVACUATION ENGINE
                       │
                       ▼
             SAFE SHELTER RECOMMENDATION
                       │
                       ▼
                  DASHBOARD
````

The system is intended as a **prototype for disaster-response decision support**, demonstrating how different AI models and geospatial/tabular information can be combined into one workflow.

---

# 🎯 Objectives

The main objectives of DisasterGuard AI are to:

* Predict the probability of flooding.
* Estimate uncertainty in flood predictions.
* Identify flooded regions from satellite imagery.
* Estimate the percentage of an area affected by flooding.
* Assess potential population and infrastructure impact.
* Combine multiple risk indicators into a unified risk score.
* Prioritize areas requiring evacuation.
* Recommend nearby potential evacuation shelters.
* Present the results through an interactive dashboard.

---

# 🧠 AI & Machine Learning Components

## 1. Bayesian Neural Network

The Bayesian Neural Network is used for flood-risk forecasting.

It provides:

* Flood probability
* Prediction uncertainty
* Binary flood classification

The model uses Monte Carlo Dropout to estimate uncertainty.

### Example output

```text
Flood Probability : 93.3%
Uncertainty       : 4.2%
```

This allows the system to distinguish between predictions that are relatively confident and predictions that have greater uncertainty.

---

## 2. U-Net Satellite Segmentation

A U-Net model is used to perform pixel-level flood segmentation from satellite imagery.

The model receives an image:

```text
128 × 128 × 3
```

and produces:

```text
128 × 128 × 1
```

flood masks.

The predicted mask is then used to estimate:

```text
Flooded Area %
```

Example:

```text
Flooded Area: 18.8%
```

---

## 3. Impact Assessment

The impact assessment component evaluates the potential consequences of flooding using information such as:

* Population
* Buildings
* Roads
* Hospitals
* Schools
* Vulnerability
* Flood depth
* Flood duration
* Building damage
* Road damage
* Affected population
* Estimated economic damage

The system classifies impact into:

```text
None/Low
Moderate
High
Severe
```

---

## 4. Risk Fusion

Risk Fusion combines information from multiple components into a unified disaster-risk assessment.

The fusion process considers factors such as:

* Flood probability
* Flooded area
* Prediction uncertainty
* Impact score

The final system produces risk levels such as:

```text
LOW
MODERATE
HIGH
CRITICAL
```

This allows DisasterGuard to move from individual model predictions toward a combined disaster-risk assessment.

---

## 5. Evacuation Intelligence

The evacuation engine identifies areas requiring greater attention based on an evacuation priority score.

It considers factors such as:

* Impact score
* Population
* Vulnerability
* Flood depth
* Flood duration

Priority levels include:

```text
LOW
MODERATE
HIGH
IMMEDIATE
```

For high-priority areas, the system also identifies a nearby potential shelter using geographic distance.

Example:

```text
Priority: HIGH

Affected Population: 2,084

Recommended Shelter: C08907

Shelter Distance: 6.65 km
```

The current prototype uses geographic distance for shelter assignment rather than real road-network travel time.

---

# 🖥️ Dashboard

DisasterGuard includes an interactive Streamlit dashboard connected to a FastAPI backend.

The dashboard provides:

### Risk Overview

* Flood probability
* Flooded area
* Prediction uncertainty
* Risk distribution
* Risk score distribution

### Bayesian Forecasting

* Prediction statistics
* Flood probability visualization
* Uncertainty visualization

### Satellite Segmentation

* Flooded-area analysis
* Scenario-level flood-area visualization

### Evacuation Intelligence

* Evacuation priority distribution
* Evacuation zones
* Affected population
* Recommended shelters
* Shelter distance

---

# 🛠️ Technologies Used

## Programming

* Python

## Machine Learning

* PyTorch
* XGBoost
* Scikit-learn

## Deep Learning

* Bayesian Neural Network
* Monte Carlo Dropout
* U-Net

## Data Processing

* Pandas
* NumPy

## Backend

* FastAPI
* Uvicorn

## Frontend / Dashboard

* Streamlit
* Plotly

## Development

* Jupyter Notebook
* VS Code
* Git / GitHub

---

# 📁 Project Structure

```text
DisasterGuard-AI/
│
├── dashboard/
│   ├── backend/
│   │   └── app.py
│   │
│   └── frontend/
│       └── app.py
│
├── data/
│   ├── external/
│   │
│   ├── processed/
│   │   ├── bnn_probabilities.npy
│   │   ├── bnn_targets.npy
│   │   ├── bnn_uncertainties.npy
│   │   ├── cleaned_data.csv
│   │   ├── evacuation_recommendations.csv
│   │   └── risk_fusion_scenarios.csv
│   │
│   └── raw/
│       ├── evacuation/
│       ├── flood_forecasting/
│       ├── flood_impact/
│       └── satellite_segmentation/
│
├── docs/
│
├── models/
│   ├── bayesian_model.pth
│   └── unet_best.pth
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Visualization.ipynb
│   ├── 03_flood_forcasting.ipynb
│   ├── 04_bayesian.ipynb
│   ├── 05_satellite.ipynb
│   ├── 06_impact_assessment.ipynb
│   └── 07_risk_fusion.ipynb
│
├── outputs/
│   ├── graphs/
│   ├── predictions/
│   └── reports/
│
├── src/
│   ├── api/
│   ├── models/
│   ├── preprocessing/
│   └── utils/
│
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd DisasterGuard-AI
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

If FastAPI, Uvicorn, Streamlit, or Plotly are not included in the requirements file:

```bash
pip install fastapi uvicorn streamlit plotly requests
```

---

# 🚀 Running the Application

DisasterGuard uses a FastAPI backend and a Streamlit frontend.

Both should be running simultaneously.

## Start the Backend

From the project root:

```bash
uvicorn src.dashboard.backend.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Start the Frontend

Open another terminal and run:

```bash
streamlit run dashboard/frontend/app.py
```

The dashboard will normally be available at:

```text
http://localhost:8501
```

---

# 🔌 API Endpoints

The backend currently provides:

### System Status

```text
GET /
```

### System Summary

```text
GET /api/summary
```

Returns:

* Number of scenarios
* Risk distribution
* Evacuation distribution
* Average flood probability
* Average flooded area
* Average uncertainty
* Affected population

### Risk Scenarios

```text
GET /api/risk
```

### Evacuation Recommendations

```text
GET /api/evacuation
```

### High-Priority Evacuation

```text
GET /api/evacuation/high-priority
```

### Bayesian Statistics

```text
GET /api/bayesian
```

---

# 📊 Model Results

The models were evaluated using the available project datasets.

### Bayesian Neural Network

```text
Accuracy  : ~0.888
Precision : ~0.554
Recall    : ~0.955
F1 Score  : ~0.701
ROC-AUC   : ~0.976
```

The model achieved high recall for the flood class, which is useful for a disaster-response setting where missing a potential flood can be costly.

---

### U-Net

On the available satellite segmentation test set:

```text
Dice : ~0.9998
IoU  : ~0.9996
```

The segmentation dataset contains 200 synthetic scenes with binary flood masks.

---

### Impact Assessment

The impact classification pipeline achieved approximately:

```text
Accuracy : ~0.79
Macro F1 : ~0.81
```

The four impact classes are:

```text
None/Low
Moderate
High
Severe
```

---

# 🗺️ Evacuation System

The evacuation engine currently produces:

```text
Evacuation Priority
Affected Population
Recommended Shelter
Shelter Distance
Available School Count
```

For the current prototype, shelter selection uses geographic distance between cells.

It is therefore a **prototype recommendation system**, rather than a real-world emergency routing system.

---

# 📦 Dataset

The project uses datasets covering:

* Flood forecasting
* Satellite flood segmentation
* Flood impact assessment
* Evacuation infrastructure
* Road networks

The satellite segmentation dataset used for the prototype contains:

```text
200 scenes
128 × 128 RGB images
Binary flood masks
```

The impact assessment dataset contains:

```text
12,000 cells
```

The datasets used in the current prototype include synthetic/project-generated data. Therefore, model performance should be interpreted within the context of the available evaluation datasets.

---

# ⚠️ Limitations

DisasterGuard AI is currently a research/prototype system and is **not intended for direct real-world emergency deployment**.

Current limitations include:

* Several datasets are synthetic.
* Satellite imagery is limited in size and diversity.
* Real-time weather-data integration is not currently implemented.
* Flood forecasts are based on the available project dataset.
* Shelter assignment currently uses geographic distance rather than live road-network routing.
* Risk-fusion outputs are based on the available model outputs and scenario data.
* Real-world validation is required before operational use.

---

# 🔮 Future Improvements

Potential future improvements include:

* Real-time weather and rainfall API integration
* Real satellite imagery integration
* Real-time flood monitoring
* Road-network based evacuation routing
* Traffic-aware evacuation planning
* Dynamic shelter capacity
* Emergency-service integration
* Multi-hazard disaster analysis
* Temporal LSTM/Transformer forecasting
* Larger real-world satellite datasets
* Deployment on cloud infrastructure
* Mobile emergency-response interface

---

# 🎯 Project Vision

DisasterGuard AI aims to demonstrate how multiple AI techniques can work together to support disaster-response decisions.

The key idea is not simply to predict:

> **"Will flooding happen?"**

but to move toward:

> **"What is likely to happen, how uncertain is the prediction, who and what will be affected, how severe is the situation, and what areas should be prioritized for evacuation?"**

---

# 📚 Internship Context

This project was developed as part of the **IEEE-SMC-KGEC Internship 2026**.

Internship repository:

[https://github.com/ieeesmckgec-student-branch-chapter/IEEE-SMC-KGEC-Internship-2026](https://github.com/ieeesmckgec-student-branch-chapter/IEEE-SMC-KGEC-Internship-2026)

---

# 👥 Contributors

### Adrish

Computer Science & Engineering

### Gowtami

Computer Science & Engineering

---

# 📄 License

This project is intended for educational and research purposes as part of the IEEE-SMC-KGEC Internship 2026.

````


```bash
uvicorn src.dashboard.backend.app:app --reload
````

That's worth getting right in the README so a teammate/judge can actually run it.
