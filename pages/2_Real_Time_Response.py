import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Operations Center",
    layout="wide"
)

# -------------------------
# Load files
# -------------------------

df = pd.read_csv("clean_events.csv")
deployment = pd.read_csv("deployment_summary.csv")
corridor_summary = pd.read_csv("corridor_summary.csv")

rf = joblib.load("duration_mode.pkl")
encoders = joblib.load("encoders.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("Operations Center")

st.markdown(
"""
Real-time event forecasting and operational planning.
"""
)

st.divider()
st.header("Event Configuration")

left, right = st.columns(2)

with left:

    event_type = st.selectbox(
        "Event Type",
        sorted(df["event_type"].dropna().unique())
    )

    event_cause = st.selectbox(
        "Event Cause",
        sorted(df["event_cause"].dropna().unique())
    )

    corridor = st.selectbox(
        "Corridor",
        sorted(df["corridor"].dropna().unique())
    )

    priority = st.selectbox(
        "Priority",
        sorted(df["priority"].dropna().unique())
    )

with right:

    road_closure = st.selectbox(
        "Road Closure",
        [False,True]
    )

    hour = st.slider(
        "Start Hour",
        0,
        23,
        18
    )

    weather = st.selectbox(
        "Weather",
        [
            "Normal",
            "Rain",
            "Heavy Rain"
        ]
    )

    crowd_size = st.selectbox(
        "Crowd Size",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    simultaneous_events = st.slider(
        "Nearby Simultaneous Events",
        0,
        5,
        0
    )

run = st.button("Generate Deployment Plan")

st.divider()
if run:
    st.success("Button pressed")
    weekday = 0
    st.write("Encoding...")
    event_type_encoded = encoders["event_type"].transform([event_type])[0]
    event_cause_encoded = encoders["event_cause"].transform([event_cause])[0]
    corridor_encoded = encoders["corridor"].transform([corridor])[0]
    priority_encoded = encoders["priority"].transform([priority])[0]
    st.success("Encoding successful")

    row = pd.DataFrame({
        "event_cause":[event_cause_encoded],
        "corridor":[corridor_encoded],
        "priority":[priority_encoded],
        "requires_road_closure":[road_closure],
        "hour":[hour],
        "weekday":[weekday],
        "event_type":[event_type_encoded]
    })
    st.write(row)

    row=row.reindex(columns=feature_columns,fill_value=0)
    st.write(row)
    st.write(feature_columns)
    st.write("Starting prediction")

    duration=float(rf.predict(row)[0])
    st.success("Prediction complete")
    st.write(duration)
    score = 0

    if road_closure:
        score += 2

    if weather=="Rain":
        duration *= 1.1
        score += 1

    if weather=="Heavy Rain":
        duration *= 1.3
        score += 2

    if crowd_size=="Medium":
        score += 1

    if crowd_size=="High":
        score += 2

    score += simultaneous_events

    if hour in [8,9,17,18,19,20]:
        score += 2
    if score >= 7:

        risk="Critical"
        officers=10
        barricades=5
        diversions=3

    elif score >= 4:

        risk="High"
        officers=7
        barricades=3
        diversions=2

    else:

        risk="Medium"
        officers=4
        barricades=2
        diversions=1