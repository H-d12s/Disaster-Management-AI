import streamlit as st
import requests
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="DisasterGuard AI",
    page_icon="🌊",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"



@st.cache_data(ttl=30)
def get_summary():

    response = requests.get(
        f"{API_URL}/api/summary"
    )

    response.raise_for_status()

    return response.json()


@st.cache_data(ttl=30)
def get_bayesian():

    response = requests.get(
        f"{API_URL}/api/bayesian"
    )

    response.raise_for_status()

    return response.json()


@st.cache_data(ttl=30)
def get_risk():

    response = requests.get(
        f"{API_URL}/api/risk"
    )

    response.raise_for_status()

    return pd.DataFrame(
        response.json()
    )


@st.cache_data(ttl=30)
def get_evacuation():

    response = requests.get(
        f"{API_URL}/api/evacuation"
    )

    response.raise_for_status()

    return pd.DataFrame(
        response.json()
    )



try:

    summary = get_summary()
    bayesian = get_bayesian()
    risk_df = get_risk()
    evacuation_df = get_evacuation()

except Exception as e:

    st.error(
        "Cannot connect to DisasterGuard backend."
    )

    st.code(str(e))

    st.info(
        "Make sure FastAPI is running with: "
        "uvicorn dashboard.backend.app:app --reload"
    )

    st.stop()



st.sidebar.title("🌊 DisasterGuard AI")

st.sidebar.markdown(
    """
    ### Disaster Intelligence

    Integrated AI pipeline:

    🧠 Bayesian Forecasting  
    🛰️ Satellite Segmentation  
    📊 Impact Assessment  
    ⚠️ Risk Fusion  
    🚨 Evacuation Intelligence
    """
)

st.sidebar.divider()

st.sidebar.success(
    "● System Online"
)



st.title("🌊 DisasterGuard AI")

st.markdown(
    "### AI-Powered Flood Disaster Intelligence & Decision Support"
)

st.markdown(
    """
    DisasterGuard combines flood probability, prediction uncertainty,
    satellite-derived flooded area, impact assessment and evacuation
    intelligence into a unified disaster-risk view.
    """
)

st.divider()



risk_distribution = summary[
    "risk_distribution"
]

evac_distribution = summary[
    "evacuation_distribution"
]


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🌧️ Avg Flood Probability",
        f"{summary['average_flood_probability'] * 100:.2f}%"
    )


with col2:

    st.metric(
        "🛰️ Avg Flooded Area",
        f"{summary['average_flooded_area'] * 100:.2f}%"
    )


with col3:

    st.metric(
        "🧠 Avg Uncertainty",
        f"{summary['average_uncertainty'] * 100:.2f}%"
    )


with col4:

    st.metric(
        "📍 Risk Scenarios",
        summary["total_scenarios"]
    )


st.divider()




st.header("⚠️ Disaster Risk Overview")


col1, col2 = st.columns(2)


with col1:

    risk_chart_df = pd.DataFrame({
        "Risk Level":
            list(risk_distribution.keys()),

        "Scenarios":
            list(risk_distribution.values())
    })

    fig = px.pie(
        risk_chart_df,
        names="Risk Level",
        values="Scenarios",
        hole=0.45,
        title="Final Risk Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    fig = px.histogram(
        risk_df,
        x="risk_score",
        nbins=20,
        title="Risk Score Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )




st.header("🌧️ Bayesian Flood Forecast")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Predictions",
        f"{bayesian['number_of_predictions']:,}"
    )


with col2:

    st.metric(
        "Average Probability",
        f"{bayesian['average_probability'] * 100:.2f}%"
    )


with col3:

    st.metric(
        "Average Uncertainty",
        f"{bayesian['average_uncertainty'] * 100:.2f}%"
    )


st.markdown("#### Flood Probability by Scenario")


probability_chart = px.scatter(
    risk_df,
    x="scenario_id",
    y="flood_probability",
    size="uncertainty",
    color="final_risk",
    hover_data=[
        "flooded_area_fraction",
        "impact_score",
        "risk_score"
    ],
    title="Flood Probability & Uncertainty"
)

probability_chart.update_yaxes(
    tickformat=".0%"
)

st.plotly_chart(
    probability_chart,
    use_container_width=True
)



st.header("🛰️ Satellite Flood Segmentation")


col1, col2 = st.columns(2)


with col1:

    flooded_area = (
        risk_df["flooded_area_fraction"]
        * 100
    )

    fig = px.histogram(
        flooded_area,
        nbins=20,
        title="Flooded Area Distribution"
    )

    fig.update_xaxes(
        title="Flooded Area (%)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    area_df = risk_df[
        [
            "scenario_id",
            "flooded_area_fraction"
        ]
    ].copy()

    area_df["flooded_area_percent"] = (
        area_df["flooded_area_fraction"]
        * 100
    )

    fig = px.bar(
        area_df,
        x="scenario_id",
        y="flooded_area_percent",
        title="Flooded Area by Scenario"
    )

    fig.update_yaxes(
        title="Flooded Area (%)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


st.subheader("🔎 Scenario Intelligence")


display_df = risk_df.copy()

display_df["flood_probability"] *= 100

display_df["flooded_area_fraction"] *= 100

display_df["uncertainty"] *= 100

display_df = display_df.rename(
    columns={
        "scenario_id": "Scenario",
        "flood_probability":
            "Flood Probability (%)",
        "uncertainty":
            "Uncertainty (%)",
        "flooded_area_fraction":
            "Flooded Area (%)",
        "impact_score":
            "Impact Score",
        "risk_score":
            "Risk Score",
        "final_risk":
            "Final Risk"
    }
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)



st.divider()

st.header("🚨 Evacuation Intelligence")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🔴 Immediate",
        evac_distribution.get(
            "IMMEDIATE", 0
        )
    )


with col2:

    st.metric(
        "🟠 High",
        evac_distribution.get(
            "HIGH", 0
        )
    )


with col3:

    st.metric(
        "🟡 Moderate",
        evac_distribution.get(
            "MODERATE", 0
        )
    )


with col4:

    st.metric(
        "🟢 Low",
        evac_distribution.get(
            "LOW", 0
        )
    )



st.subheader("🗺️ Evacuation Priority Map")


map_df = evacuation_df.copy()

fig = px.scatter_mapbox(
    map_df,
    lat="latitude",
    lon="longitude",
    color="evacuation_priority",
    size="evacuation_priority_score",
    hover_name="cell_id",
    hover_data=[
        "affected_population",
        "evacuation_priority_score",
        "recommended_shelter",
        "shelter_distance_km"
    ],
    zoom=4,
    height=600
)

fig.update_layout(
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig,
    use_container_width=True
)



st.subheader("🚨 Highest Priority Evacuation Zones")


top_zones = (
    evacuation_df
    .sort_values(
        "evacuation_priority_score",
        ascending=False
    )
    .head(20)
)


st.dataframe(
    top_zones[
        [
            "cell_id",
            "latitude",
            "longitude",
            "evacuation_priority",
            "evacuation_priority_score",
            "affected_population",
            "recommended_shelter",
            "shelter_distance_km",
            "shelter_schools"
        ]
    ],
    use_container_width=True,
    hide_index=True
)




st.divider()

st.header("🧠 DisasterGuard AI Pipeline")

st.markdown(
    """
    **1. Bayesian Neural Network**  
    Predicts flood probability and estimates prediction uncertainty.

    **2. U-Net Satellite Segmentation**  
    Identifies flooded regions and estimates flooded-area fraction.

    **3. Impact Assessment**  
    Estimates consequences for population, buildings and infrastructure.

    **4. Risk Fusion**  
    Combines flood probability, uncertainty, flooded area and impact
    into a final disaster-risk score.

    **5. Evacuation Engine**  
    Prioritizes affected zones and recommends nearby shelters.

    **6. Dashboard**  
    Presents the results to support disaster-response decisions.
    """
)


st.divider()

st.caption(
    "DisasterGuard AI • Integrated Flood Disaster Intelligence System"
)