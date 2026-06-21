import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Overview",
    layout="wide"
)
df = pd.read_csv(
    "clean_events.csv"
)

deployment_summary = pd.read_csv(
    "deployment_summary.csv"
)
st.title(
"📊 Overview Dashboard"
)

st.markdown(
"""
Traffic Intelligence Summary for Bengaluru
"""
)
col1,col2,col3,col4=st.columns(4)

col1.metric(
"Total Events",
len(df)
)

col2.metric(
"Critical Events",
len(
df[
df['severity_label']=="Critical"
]
)
)

col3.metric(
"Road Closures",
df['requires_road_closure'].sum()
)

col4.metric(
"Average Duration",
round(
df['duration_minutes'].mean()
)
)
st.subheader(
"Event Cause Distribution"
)

cause_df = df[
'event_cause'
].value_counts()

cause_df = cause_df.reset_index()

cause_df.columns=[
'Cause',
'Count'
]

fig = px.bar(
cause_df,
x='Cause',
y='Count',
color='Count'
)

st.plotly_chart(
fig,
use_container_width=True
)
st.subheader(
"Severity Distribution"
)

severity_df=df[
'severity_label'
].value_counts()

severity_df=severity_df.reset_index()

severity_df.columns=[
'Severity',
'Count'
]

fig2=px.pie(
severity_df,
names='Severity',
values='Count'
)

st.plotly_chart(
fig2,
use_container_width=True
)
st.subheader(
"Peak Hour Pattern"
)

hour_df=df.groupby(
'hour'
).size()

hour_df=hour_df.reset_index(
name='Events'
)

fig3=px.line(
hour_df,
x='hour',
y='Events',
markers=True
)

st.plotly_chart(
fig3,
use_container_width=True
)
st.subheader(
"Top Deployment Corridors"
)

fig4=px.bar(
deployment_summary.head(10),
x='corridor',
y='deployment_score',
color='deployment_score'
)

st.plotly_chart(
fig4,
use_container_width=True
)