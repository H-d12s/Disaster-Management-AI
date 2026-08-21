from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import numpy as np
import os


app = FastAPI(
    title="DisasterGuard AI API",
    description="AI-powered flood disaster intelligence API",
    version="1.0"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../.."
    )
)
PROCESSED_DIR = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)




risk_path = os.path.join(
    PROCESSED_DIR,
    "risk_fusion_scenarios.csv"
)

evacuation_path = os.path.join(
    PROCESSED_DIR,
    "evacuation_recommendations.csv"
)

bnn_probability_path = os.path.join(
    PROCESSED_DIR,
    "bnn_probabilities.npy"
)

bnn_uncertainty_path = os.path.join(
    PROCESSED_DIR,
    "bnn_uncertainties.npy"
)


risk_df = pd.read_csv(risk_path)

evacuation_df = pd.read_csv(
    evacuation_path
)

bnn_probabilities = np.load(
    bnn_probability_path
)

bnn_uncertainties = np.load(
    bnn_uncertainty_path
)




@app.get("/")
def root():

    return {
        "system": "DisasterGuard AI",
        "status": "online",
        "version": "1.0"
    }



@app.get("/api/summary")
def summary():

    risk_counts = (
        risk_df["final_risk"]
        .value_counts()
        .to_dict()
    )

    evacuation_counts = (
        evacuation_df["evacuation_priority"]
        .value_counts()
        .to_dict()
    )

    return {
        "total_scenarios": len(risk_df),

        "risk_distribution": risk_counts,

        "evacuation_distribution":
            evacuation_counts,

        "average_flood_probability":
            float(
                risk_df["flood_probability"].mean()
            ),

        "average_flooded_area":
            float(
                risk_df["flooded_area_fraction"].mean()
            ),

        "average_uncertainty":
            float(
                risk_df["uncertainty"].mean()
            ),

        "total_affected_population":
            float(
                evacuation_df[
                    "affected_population"
                ].sum()
            )
    }



@app.get("/api/risk")
def risk_scenarios():

    return risk_df.to_dict(
        orient="records"
    )



@app.get("/api/evacuation")
def evacuation():

    return evacuation_df.to_dict(
        orient="records"
    )



@app.get("/api/evacuation/high-priority")
def high_priority_evacuation():

    high_priority = evacuation_df[
        evacuation_df[
            "evacuation_priority"
        ].isin(
            ["IMMEDIATE", "HIGH"]
        )
    ]

    return high_priority.to_dict(
        orient="records"
    )




@app.get("/api/bayesian")
def bayesian():

    return {

        "number_of_predictions":
            int(len(bnn_probabilities)),

        "average_probability":
            float(
                bnn_probabilities.mean()
            ),

        "average_uncertainty":
            float(
                bnn_uncertainties.mean()
            ),

        "minimum_uncertainty":
            float(
                bnn_uncertainties.min()
            ),

        "maximum_uncertainty":
            float(
                bnn_uncertainties.max()
            )
    }