import altair as alt
import pandas as pd
import streamlit as st

# Load the CSV data
data_path = "user_behavior_dataset.csv"
df = pd.read_csv(data_path)

# Set up the Streamlit app
st.title("User Behavior Dashboard")

# Scorecards
st.header("Key Metrics")
st.metric(
    "Average App Usage Time (min/day)", f"{df['App Usage Time (min/day)'].mean():.2f}"
)
st.metric(
    "Average Screen On Time (hours/day)",
    f"{df['Screen On Time (hours/day)'].mean():.2f}",
)
st.metric(
    "Average Battery Drain (mAh/day)", f"{df['Battery Drain (mAh/day)'].mean():.2f}"
)

# Bar chart for App Usage Time by Device Model
st.subheader("App Usage Time by Device Model")
bar_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="Device Model",
        y="App Usage Time (min/day)",
        color=alt.Color("Device Model", scale=alt.Scale(scheme="set2")),
    )
    .properties(width=600)
)
st.altair_chart(bar_chart, use_container_width=True)

# Pie chart for Screen On Time by Operating System
st.subheader("Screen On Time by Operating System")
pie_chart = (
    alt.Chart(df)
    .mark_arc()
    .encode(
        theta=alt.Theta(field="Screen On Time (hours/day)", type="quantitative"),
        color=alt.Color("Operating System", scale=alt.Scale(scheme="set2")),
    )
    .properties(width=400)
)
st.altair_chart(pie_chart, use_container_width=True)

# Pie chart for User Behavior Class distribution
st.subheader("User Behavior Class Distribution")
pie_chart = (
    alt.Chart(df)
    .mark_arc()
    .encode(
        theta=alt.Theta(field="User Behavior Class", type="quantitative"),
        color=alt.Color("User Behavior Class", scale=alt.Scale(scheme="set2")),
    )
    .properties(width=400)
)
st.altair_chart(pie_chart, use_container_width=True)

# Aggregated metrics table
st.subheader("Aggregated Metrics by Device Model and Operating System")
agg_metrics = (
    df.groupby(["Device Model", "Operating System"])
    .agg(
        {
            "App Usage Time (min/day)": "mean",
            "Screen On Time (hours/day)": "mean",
            "Battery Drain (mAh/day)": "mean",
        }
    )
    .reset_index()
)
st.dataframe(agg_metrics)
