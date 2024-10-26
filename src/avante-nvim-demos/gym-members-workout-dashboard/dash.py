"""
Dataset Sample:

Age,Gender,Weight (kg),Height (m),Max_BPM,Avg_BPM,Resting_BPM,Session_Duration (hours),Calories_Burned,Workout_Type,Fat_Percentage,Water_Intake (liters),Workout_Frequency (days/week),Experience_Level,BMI
56,Male,88.3,1.71,180,157,60,1.69,1313.0,Yoga,12.6,3.5,4,3,30.2
46,Female,74.9,1.53,179,151,66,1.3,883.0,HIIT,33.9,2.1,4,2,32.0
32,Female,68.1,1.66,167,122,54,1.11,677.0,Cardio,33.4,2.3,4,2,24.71
25,Male,53.2,1.7,190,164,56,0.59,532.0,Strength,28.8,2.1,3,1,18.41
38,Male,46.1,1.79,188,158,68,0.64,556.0,Strength,29.2,2.8,3,1,14.39
56,Female,58.0,1.68,168,156,74,1.59,1116.0,HIIT,15.5,2.7,5,3,20.55
36,Male,70.3,1.72,174,169,73,1.49,1385.0,Cardio,21.3,2.3,3,2,23.76
40,Female,69.7,1.51,189,141,64,1.27,895.0,Cardio,30.6,1.9,3,2,30.57
28,Male,121.7,1.94,185,127,52,1.03,719.0,Strength,28.9,2.6,4,2,32.34
28,Male,101.8,1.84,169,136,64,1.08,808.0,Cardio,29.7,2.7,3,1,30.07
41,Male,120.8,1.67,188,146,54,0.82,593.0,HIIT,20.5,3.0,2,1,43.31
53,Male,51.7,1.7,175,152,72,1.15,865.0,HIIT,23.6,3.5,3,2,17.89
57,Male,112.5,1.61,195,165,61,1.24,1013.0,Cardio,22.1,2.7,3,2,43.4
41,Male,94.5,2.0,179,136,69,1.18,794.0,HIIT,27.6,3.7,3,1,23.62

"""

import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Title of the dashboard
st.title("Gym Members Workout Dashboard")

# Welcome message
st.write("Welcome to the Gym Members Workout Dashboard!")

# Load the dataset
data = pd.read_csv("../data/gym_members_exercise_tracking.csv")

# Sidebar filters
age_filter = st.sidebar.slider(
    "Select Age Range", int(data["Age"].min()), int(data["Age"].max()), (20, 60)
)
weight_filter = st.sidebar.slider(
    "Select Weight Range (kg)",
    float(data["Weight (kg)"].min()),
    float(data["Weight (kg)"].max()),
    (50.0, 100.0),
)
height_filter = st.sidebar.slider(
    "Select Height Range (m)",
    float(data["Height (m)"].min()),
    float(data["Height (m)"].max()),
    (1.5, 2.0),
)
gender_filter = st.sidebar.selectbox(
    "Select Gender", options=["All"] + data["Gender"].unique().tolist()
)
experience_level_filter = st.sidebar.selectbox(
    "Select Experience Level",
    options=["All"] + data["Experience_Level"].unique().tolist(),
)
workout_type_filter = st.sidebar.multiselect(
    "Select Workout Type",
    options=data["Workout_Type"].unique().tolist(),
    default=data["Workout_Type"].unique().tolist(),
)

# Filter data based on selections
filtered_data = data[
    (data["Age"].between(age_filter[0], age_filter[1]))
    & (
        data["Gender"].isin(
            [gender_filter] if gender_filter != "All" else data["Gender"].unique()
        )
    )
    & (data["Weight (kg)"].between(weight_filter[0], weight_filter[1]))
    & (data["Height (m)"].between(height_filter[0], height_filter[1]))
    & (
        data["Experience_Level"].isin(
            [experience_level_filter]
            if experience_level_filter != "All"
            else data["Experience_Level"].unique()
        )
    )
    & (data["Workout_Type"].isin(workout_type_filter))
]

# Display filtered data
st.write("Filtered Workout Data")
st.dataframe(filtered_data)

# Visualizations
st.write("Workout Type Distribution")
workout_counts = filtered_data["Workout_Type"].value_counts().reset_index()
workout_counts.columns = ["Workout_Type", "Count"]
chart = (
    alt.Chart(workout_counts)
    .mark_bar()
    .encode(x="Workout_Type", y="Count", color="Workout_Type")
    .properties(title="Workout Type Distribution")
)
st.altair_chart(chart, use_container_width=True)

st.write("Calories Burned by Gender")
calories_gender = filtered_data.groupby("Gender")["Calories_Burned"].sum().reset_index()
calories_gender.columns = ["Gender", "Calories_Burned"]
pie_chart = (
    alt.Chart(calories_gender)
    .mark_arc()
    .encode(
        theta=alt.Theta(field="Calories_Burned", type="quantitative"),
        color=alt.Color(field="Gender", type="nominal"),
        tooltip=["Gender", "Calories_Burned"],
    )
    .properties(title="Calories Burned by Gender")
)
st.altair_chart(pie_chart, use_container_width=True)
