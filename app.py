import streamlit as st
import pandas as pd
import joblib

# No-show model
pipeline = joblib.load("first/no_show_pipeline.pkl")

# Forecast model
forecast_model = joblib.load("first/forecast_model.pkl")

tab1, tab2 = st.tabs([
    "No-Show Prediction",
    "Demand Forecasting"
])

with tab1:

    st.header("No-Show Prediction")

    age = st.number_input("Age", 0, 100, 30)

    gender = st.selectbox(
        "Gender",
        ["M", "F"]
    )

    hypertension = st.selectbox(
        "Hypertension",
        [0, 1]
    )

    diabetes = st.selectbox(
        "Diabetes",
        [0, 1]
    )

if st.button("Predict"):

    input_data = pd.DataFrame({
    'specialty': [0],
    'appointment_time': [10],
    'gender': [1 if gender=="M" else 0],
    'disability': [0],
    'place': [0],
    'appointment_shift': [0],
    'age': [age],
    'under_12_years_old': [1 if age < 12 else 0],
    'over_60_years_old': [1 if age > 60 else 0],
    'patient_needs_companion': [0],
    'average_temp_day': [30],
    'average_rain_day': [5],
    'max_temp_day': [35],
    'max_rain_day': [10],
    'rainy_day_before': [0],
    'storm_day_before': [0],
    'rain_intensity': [0],
    'heat_intensity': [0],
    'appointment_date_continuous': [100],
    'Hipertension': [hypertension],
    'Diabetes': [diabetes],
    'Alcoholism': [0],
    'Handcap': [0],
    'Scholarship': [0],
    'SMS_received': [1],
    'day': [15],
    'month': [6],
    'weekday': [0],
    'is_weekend': [0]
})

    prediction = pipeline.predict(input_data)

    probability = pipeline.predict_proba(input_data)

    st.write(
        "No-Show Risk:",
        round(probability[0][1] * 100, 2),
        "%"
    )

    if prediction[0] == 1:
        st.error("⚠️ Patient likely to miss appointment")
    else:
        st.success("✅ Patient likely to attend")

with tab2:

    st.header("Demand Forecasting")

    forecast_date = st.date_input("Select Forecast Date")

    lag_1 = st.number_input(
        "Appointments Yesterday",
        min_value=0,
        value=300
    )

    lag_7 = st.number_input(
        "Appointments 7 Days Ago",
        min_value=0,
        value=280
    )

    if st.button("Forecast", key="forecast_btn"):

        input_df = pd.DataFrame({
            'day': [forecast_date.day],
            'month': [forecast_date.month],
            'weekday': [forecast_date.weekday()],
            'lag_1': [lag_1],
            'lag_7': [lag_7]
        })

        result = forecast_model.predict(input_df)

        st.success(
            f"Expected Appointments: {int(result[0])}"
        )    