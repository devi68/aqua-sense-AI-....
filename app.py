
import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AquaSense AI",
    page_icon="💧",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
DATA_FILE = "/content/aquasense_incidents_50_clean.csv"
df = pd.read_csv(DATA_FILE)

# -----------------------------
# Title
# -----------------------------
st.title("💧 AquaSense AI")
st.subheader("Water-Loss Intelligence and Intervention System")

st.write(
    "AquaSense AI analyzes reported water-loss incidents, "
    "prioritizes them, identifies recurring locations, "
    "and provides intervention guidance."
)

# -----------------------------
# Dashboard Metrics
# -----------------------------
total_incidents = len(df)
high_count = (df["priority"] == "High").sum()
medium_count = (df["priority"] == "Medium").sum()
low_count = (df["priority"] == "Low").sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Incidents", total_incidents)

with col2:
    st.metric("High Priority", high_count)

with col3:
    st.metric("Medium Priority", medium_count)

with col4:
    st.metric("Low Priority", low_count)

st.divider()

# -----------------------------
# Priority Overview
# -----------------------------
st.header("📊 Priority Overview")

priority_counts = (
    df["priority"]
    .value_counts()
    .reindex(["High", "Medium", "Low"])
    .fillna(0)
)

st.bar_chart(priority_counts)

# -----------------------------
# Location Analysis
# -----------------------------
st.header("📍 Water-Loss Incidents by Location")

location_counts = df["location"].value_counts()

st.bar_chart(location_counts)

# -----------------------------
# Individual Incident Analysis
# -----------------------------
st.header("🔎 Incident Analysis")

incident_ids = df["incident_id"].tolist()

selected_id = st.selectbox(
    "Select an incident:",
    incident_ids
)

selected = df[df["incident_id"] == selected_id].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.write("**Incident ID:**", selected["incident_id"])
    st.write("**Location:**", selected["location"])
    st.write("**Incident Type:**", selected["incident_type"])
    st.write("**Reported At:**", selected["reported_at"])
    st.write("**Duration:**", selected["duration_hours"], "hours")
    st.write("**People Potentially Affected:**", selected["people_affected"])

with col2:
    st.write("**Priority Score:**", selected["priority_score"])
    st.write("**Priority:**", selected["priority"])
    st.write("**Hotspot Status:**", selected["hotspot_status"])
    st.write("**Status:**", selected["status"])

st.write("### Incident Description")
st.info(selected["description"])

st.write("### Why This Priority?")
st.info(selected["priority_reason"])

st.write("### Recommended Intervention")
st.success(selected["recommended_action"])

st.write("### Preventive Action")
st.warning(selected["preventive_action"])

st.divider()

# -----------------------------
# High-Priority Intervention Queue
# -----------------------------
st.header("🚨 High-Priority Intervention Queue")

high_priority = (
    df[df["priority"] == "High"]
    .sort_values("priority_score", ascending=False)
    [[
        "incident_id",
        "location",
        "incident_type",
        "priority_score",
        "priority_reason",
        "recommended_action"
    ]]
)

st.dataframe(
    high_priority,
    use_container_width=True,
    hide_index=True
)
