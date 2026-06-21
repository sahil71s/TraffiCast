import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Overview",
    layout="wide"
)

# ======================================
# Load Data
# ======================================

df = pd.read_csv("clean_events.csv")

# ======================================
# Header
# ======================================

st.title("Overview")
st.write("Historical traffic intelligence and event analytics.")

st.divider()

# ======================================
# KPI Cards
# ======================================

total_events = len(df)

avg_duration = round(df["duration_minutes"].mean(), 1)

road_closures = df["requires_road_closure"].sum()

active_corridors = df["corridor"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Events", total_events)

c2.metric("Average Duration (min)", avg_duration)

c3.metric("Road Closures", road_closures)

c4.metric("Active Corridors", active_corridors)

st.divider()

# ======================================
# Event Cause Distribution
# ======================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("Event Cause Distribution")

    cause_df = (
        df["event_cause"]
        .value_counts()
        .reset_index()
    )

    cause_df.columns = ["event_cause", "count"]

    fig = px.bar(
        cause_df,
        x="event_cause",
        y="count"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.subheader("Event Type Distribution")

    fig = px.pie(
        df,
        names="event_type"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================
# Peak Hour Analysis
# ======================================

st.subheader("Peak Hour Analysis")

hourly = (
    df.groupby("hour")
    .size()
    .reset_index(name="events")
)

fig = px.line(
    hourly,
    x="hour",
    y="events",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================
# Top Corridors
# ======================================

st.subheader("Top Corridors")

corridors = (
    df["corridor"]
    .value_counts()
    .head(10)
    .reset_index()
)

corridors.columns = ["corridor", "count"]

fig = px.bar(
    corridors,
    x="corridor",
    y="count"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================
# Average Duration by Event Cause
# ======================================

st.subheader("Average Duration by Event Cause")

duration_df = (
    df.groupby("event_cause")["duration_minutes"]
    .mean()
    .reset_index()
)

fig = px.bar(
    duration_df,
    x="event_cause",
    y="duration_minutes"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================
# Road Closure Percentage
# ======================================

st.subheader("Road Closure Percentage")

closure_df = (
    df["requires_road_closure"]
    .value_counts()
    .reset_index()
)

closure_df.columns = ["requires_road_closure", "count"]

fig = px.pie(
    closure_df,
    names="requires_road_closure",
    values="count"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================
# Top Risk Corridors
# ======================================

if "severity" in df.columns:

    st.subheader("Top Risk Corridors")

    risk_df = (
        df.groupby("corridor")
        .agg({
            "severity": "mean",
            "duration_minutes": "mean"
        })
        .reset_index()
    )

    risk_df["risk_score"] = (
        risk_df["severity"] *
        risk_df["duration_minutes"]
    )

    risk_df = risk_df.sort_values(
        "risk_score",
        ascending=False
    ).head(10)

    fig = px.bar(
        risk_df,
        x="corridor",
        y="risk_score"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================
# Recent Events
# ======================================

st.subheader("Recent Events")

cols = [
    "start_datetime",
    "event_cause",
    "corridor",
    "priority",
    "duration_minutes"
]

available_cols = [c for c in cols if c in df.columns]

st.dataframe(
    df[available_cols].tail(20),
    use_container_width=True
)