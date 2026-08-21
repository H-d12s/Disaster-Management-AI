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