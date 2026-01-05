import streamlit as st
import pickle
import numpy as np

# Load model
with open("weather_model.pkl", "rb") as file:
    model = pickle.load(file)

# App Title
st.title("🌦️ Weather Condition Prediction App")
st.write("Enter daily environmental values to generate prediction")

st.divider()

# Inputs (same order as model training)
hours_sunlight = st.number_input(
    "Hours of Sunlight",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

humidity_level = st.number_input(
    "Humidity Level (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)


# Predict button
if st.button("Predict"):
    input_data = np.array([[
        hours_sunlight,
        humidity_level,
    ]])

    prediction = model.predict(input_data)

    # Output (adjust text based on your target meaning)
    if prediction[0] == 1:
        st.success("✅ Favorable Weather Condition")
    else:
        st.error("⚠️ Unfavorable Weather Condition")
