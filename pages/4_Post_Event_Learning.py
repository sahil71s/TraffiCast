import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title="Event Learning System",
    layout="wide"
)

# -------------------------------------------------------
# Load historical data
# -------------------------------------------------------

df = pd.read_csv("clean_events.csv")

# -------------------------------------------------------
# Create learning database if not exists
# -------------------------------------------------------

if not os.path.exists("learning_db.csv"):

    learning_db = pd.DataFrame(columns=[
        "timestamp",
        "event_type",
        "corridor",
        "actual_duration",
        "officers",
        "barricades",
        "diversion_effective",
        "severity",
        "unexpected_issues",
        "lessons_learned",
        "recommendations"
    ])

    learning_db.to_csv(
        "learning_db.csv",
        index=False
    )

# -------------------------------------------------------
# Create officer notes database
# -------------------------------------------------------

if not os.path.exists("officer_notes.csv"):

    notes_db = pd.DataFrame(columns=[
        "timestamp",
        "officer_name",
        "station",
        "observation"
    ])

    notes_db.to_csv(
        "officer_notes.csv",
        index=False
    )

learning_db = pd.read_csv("learning_db.csv")
notes_db = pd.read_csv("officer_notes.csv")

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.title("Event Learning System")

st.markdown("""
Institutional memory engine for continuous improvement
of traffic operations.
""")

st.divider()

# =====================================================
# Historical Learning
# =====================================================

st.header("Historical Learning")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Historical Events",
    len(df)
)

c2.metric(
    "Event Causes",
    df["event_cause"].nunique()
)

c3.metric(
    "Corridors",
    df["corridor"].nunique()
)

c4.metric(
    "Road Closures",
    int(df["requires_road_closure"].sum())
)

st.divider()

# =====================================================
# Lessons Learned
# =====================================================

st.header("Lessons Learned")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
"""
Construction events generally produce longer durations.

Early barricading is recommended.
"""
)

with col2:

    st.info(
"""
Vehicle breakdowns are the dominant incident category.

Rapid response reduces congestion.
"""
)

with col3:

    st.info(
"""
Public events require diversion planning
and additional manpower.
"""
)

st.divider()

# =====================================================
# POST EVENT DEBRIEF
# =====================================================

st.header("Post Event Debrief")

event_type = st.selectbox(
    "Event Type",
    sorted(df["event_cause"].dropna().unique())
)

corridor = st.selectbox(
    "Corridor",
    sorted(df["corridor"].dropna().unique())
)

actual_duration = st.number_input(
    "Actual Duration (minutes)",
    0
)

officers = st.number_input(
    "Officers Deployed",
    0
)

barricades = st.number_input(
    "Barricades Used",
    0
)

diversion_effective = st.selectbox(
    "Was Diversion Effective?",
    ["Yes","No"]
)

severity = st.selectbox(
    "Observed Severity",
    ["Low","Medium","High","Critical"]
)

unexpected_issues = st.text_area(
    "Unexpected Issues"
)

lessons_learned = st.text_area(
    "Lessons Learned"
)

recommendations = st.text_area(
    "Recommendations For Future Events"
)

if st.button("Save Debrief"):

    new_row = pd.DataFrame({

        "timestamp":[datetime.now()],

        "event_type":[event_type],

        "corridor":[corridor],

        "actual_duration":[actual_duration],

        "officers":[officers],

        "barricades":[barricades],

        "diversion_effective":[diversion_effective],

        "severity":[severity],

        "unexpected_issues":[unexpected_issues],

        "lessons_learned":[lessons_learned],

        "recommendations":[recommendations]

    })

    learning_db = pd.concat(
        [learning_db,new_row],
        ignore_index=True
    )

    learning_db.to_csv(
        "learning_db.csv",
        index=False
    )

    st.success("Debrief stored successfully")

st.divider()

# =====================================================
# OFFICER NOTES
# =====================================================

st.header("Officer Notes Repository")

officer_name = st.text_input(
    "Officer Name"
)

station = st.text_input(
    "Police Station"
)

observation = st.text_area(
    "Observation"
)

if st.button("Submit Note"):

    note = pd.DataFrame({

        "timestamp":[datetime.now()],

        "officer_name":[officer_name],

        "station":[station],

        "observation":[observation]

    })

    notes_db = pd.concat(
        [notes_db,note],
        ignore_index=True
    )

    notes_db.to_csv(
        "officer_notes.csv",
        index=False
    )

    st.success("Observation saved")

st.divider()

# =====================================================
# Historical Search
# =====================================================

st.header("Historical Memory Search")

search_corridor = st.selectbox(
    "Search Corridor",
    sorted(df["corridor"].dropna().unique())
)

result = learning_db[
    learning_db["corridor"]==search_corridor
]

st.dataframe(
    result,
    use_container_width=True
)

st.divider()

# =====================================================
# Officer Knowledge Base
# =====================================================

st.header("Officer Knowledge Base")

st.dataframe(
    notes_db,
    use_container_width=True
)

st.divider()
