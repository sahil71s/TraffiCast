import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Deployment Intelligence",
    layout="wide"
)

# -----------------------
# Load Data
# -----------------------

corridor_summary = pd.read_csv(
    "corridor_summary.csv"
)

corridor_summary = corridor_summary.sort_values(
    "corridor_risk_score",
    ascending=False
)

# -----------------------
# Title
# -----------------------

st.title("Deployment Intelligence")

st.markdown(
"""
Corridor prioritization and resource planning based on historical traffic incidents.
"""
)

# -----------------------
# KPI Section
# -----------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Total Corridors",
        len(corridor_summary)
    )

with c2:
    st.metric(
        "Total Events",
        int(corridor_summary["total_events"].sum())
    )

with c3:
    st.metric(
        "Average Severity",
        round(
            corridor_summary["avg_severity"].mean(),
            2
        )
    )

with c4:
    st.metric(
        "Average Duration (min)",
        round(
            corridor_summary["avg_duration"].mean(),
            1
        )
    )

st.divider()

# =====================================================
# Corridor Risk Ranking
# =====================================================

st.subheader("Corridor Risk Ranking")

fig1 = px.bar(
    corridor_summary.head(10),
    x="corridor",
    y="corridor_risk_score",
    color="corridor_risk_score"
)

fig1.update_layout(
    plot_bgcolor="#0E1117",
    paper_bgcolor="#0E1117"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================================
# Average Duration
# =====================================================

st.subheader("Average Incident Duration")

duration_df = corridor_summary.sort_values(
    "avg_duration",
    ascending=False
)

fig2 = px.bar(
    duration_df.head(10),
    x="corridor",
    y="avg_duration",
    color="avg_duration"
)

fig2.update_layout(
    plot_bgcolor="#0E1117",
    paper_bgcolor="#0E1117"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================================
# Closure Percentage
# =====================================================

st.subheader("Road Closure Percentage")

fig3 = px.bar(
    corridor_summary.head(10),
    x="corridor",
    y="closure_percent",
    color="closure_percent"
)

fig3.update_layout(
    plot_bgcolor="#0E1117",
    paper_bgcolor="#0E1117"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =====================================================
# Detailed Intelligence Table
# =====================================================

st.subheader("Corridor Intelligence")

st.dataframe(
    corridor_summary[
        [
            "corridor",
            "total_events",
            "avg_severity",
            "avg_duration",
            "road_closure_count",
            "closure_percent",
            "corridor_risk_score"
        ]
    ],
    use_container_width=True
)

# =====================================================
# Top Priority Corridors
# =====================================================

st.subheader("Command Recommendations")

top3 = corridor_summary.head(3)

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
f"""
Highest Priority Corridor

Corridor:
{top3.iloc[0]['corridor']}

Risk Score:
{round(top3.iloc[0]['corridor_risk_score'],1)}

Average Duration:
{round(top3.iloc[0]['avg_duration'],1)} min
"""
)

with col2:
    st.info(
f"""
Second Priority Corridor

Corridor:
{top3.iloc[1]['corridor']}

Risk Score:
{round(top3.iloc[1]['corridor_risk_score'],1)}

Average Duration:
{round(top3.iloc[1]['avg_duration'],1)} min
"""
)

with col3:
    st.info(
f"""
Third Priority Corridor

Corridor:
{top3.iloc[2]['corridor']}

Risk Score:
{round(top3.iloc[2]['corridor_risk_score'],1)}

Average Duration:
{round(top3.iloc[2]['avg_duration'],1)} min
"""
)