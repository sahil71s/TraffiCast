import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Operations Center",
    layout="wide"
)

# =====================================
# Load Data and Models
# =====================================

df = pd.read_csv("clean_events.csv")

rf = joblib.load("duration_mode.pkl")
encoders = joblib.load("encoders.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# =====================================
# Header
# =====================================

st.title("Operations Center")
st.write("Real-time event forecasting and resource recommendation.")

st.divider()

# =====================================
# Input Section
# =====================================

col1, col2 = st.columns(2)

with col1:

    event_type = st.selectbox(
        "Event Type",
        list(encoders["event_type"].classes_)
    )

    event_cause = st.selectbox(
        "Event Cause",
        list(encoders["event_cause"].classes_)
    )

    corridor = st.selectbox(
        "Corridor",
        list(encoders["corridor"].classes_)
    )

    priority = st.selectbox(
        "Priority",
        list(encoders["priority"].classes_)
    )

with col2:

    road_closure = st.selectbox(
        "Road Closure",
        [False, True]
    )

    hour = st.slider(
        "Start Hour",
        0,
        23,
        18
    )

    weather = st.selectbox(
        "Weather",
        ["Normal", "Rain", "Fog"]
    )

    crowd_size = st.selectbox(
        "Crowd Size",
        ["Low", "Medium", "High"]
    )

    simultaneous_events = st.slider(
        "Nearby Simultaneous Events",
        0,
        5,
        1
    )

st.divider()

# =====================================
# Historical Intelligence
# =====================================

similar_events = df[
    (df["event_cause"] == event_cause)
    &
    (df["corridor"] == corridor)
    &
    (df["priority"] == priority)
]

if len(similar_events) > 0:

    historical_count = len(similar_events)

    avg_duration_hist = round(
        similar_events["duration_minutes"].mean(),
        1
    )

    closure_rate = round(
        100 * similar_events["requires_road_closure"].mean(),
        1
    )

else:

    historical_count = 0
    avg_duration_hist = 0
    closure_rate = 0

st.subheader("Historical Intelligence")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Similar Historical Events",
    historical_count
)

c2.metric(
    "Average Duration",
    f"{avg_duration_hist} min"
)

c3.metric(
    "Road Closure Frequency",
    f"{closure_rate}%"
)

st.divider()

# =====================================
# Generate Deployment Plan
# =====================================

if st.button("Generate Deployment Plan"):

    event_type_encoded = encoders["event_type"].transform([event_type])[0]
    event_cause_encoded = encoders["event_cause"].transform([event_cause])[0]
    corridor_encoded = encoders["corridor"].transform([corridor])[0]
    priority_encoded = encoders["priority"].transform([priority])[0]

    weekday = 0

    x_input = pd.DataFrame(
        [[
            event_cause_encoded,
            corridor_encoded,
            priority_encoded,
            road_closure,
            hour,
            weekday,
            event_type_encoded
        ]],
        columns=feature_columns
    )

    duration_prediction = round(
        rf.predict(x_input)[0],
        1
    )

    # =====================================
    # Risk Score
    # =====================================

    score = 0

    if priority == "High":
        score += 3

    if road_closure:
        score += 2

    if crowd_size == "High":
        score += 3

    elif crowd_size == "Medium":
        score += 2

    if weather == "Rain":
        score += 1

    score += simultaneous_events

    # =====================================
    # Resource Recommendation
    # =====================================

    if score >= 8:

        risk = "Critical"
        officers = 12
        barricades = 5
        diversions = 3

    elif score >= 5:

        risk = "High"
        officers = 8
        barricades = 3
        diversions = 2

    else:

        risk = "Medium"
        officers = 4
        barricades = 2
        diversions = 1

    st.divider()

    st.subheader("Predicted Event Impact")

    a, b, c, d = st.columns(4)

    a.metric("Duration", f"{duration_prediction} min")
    b.metric("Risk Level", risk)
    c.metric("Officers", officers)
    d.metric("Barricades", barricades)

    st.metric(
        "Diversion Routes",
        diversions
    )

    st.divider()

    st.subheader("Command Summary")

    st.success(f"""
Expected Duration : {duration_prediction} min

Risk Level : {risk}

Deploy {officers} officers.

Install {barricades} barricades.

Activate {diversions} diversion routes.

Monitor the corridor continuously until clearance.
""")