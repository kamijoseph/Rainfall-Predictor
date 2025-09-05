# rainfall_app.py
import streamlit as st
import pandas as pd
import pickle

# ----- Load the model -----
with open("models/logreg_rainfall_model.pkl", "rb") as f:
    model = pickle.load(f)

# ----- Page configuration -----
st.set_page_config(
    page_title="Rainfall Prediction 🌦️",
    page_icon="🌧️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ----- App Title -----
st.title("🌦️ Rainfall Prediction System")
st.divider()
st.subheader("Models Predicts if it will rain based on weather parameters.")

# ----- User Inputs -----
st.header("Enter Weather Parameters:")

# Split inputs into two columns for a cleaner UI
col1, col2 = st.columns(2)

with col1:
    pressure = st.number_input("Pressure (hPa)", min_value=500.0, max_value=1200.0, value=1015.9, step=0.1)
    temperature = st.number_input("Temperature (°C)", min_value=-20.0, max_value=50.0, value=19.9, step=0.1)
    humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=95)

with col2:
    cloud = st.slider("Cloud Cover (%)", min_value=0, max_value=100, value=81)
    sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=24.0, value=0.0, step=0.1)
    wind_direction = st.number_input("Wind Direction (°)", min_value=0, max_value=360, value=40)
    wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=50.0, value=13.7, step=0.1)

# ----- prepare data -----
input_data = [pressure, temperature, humidity, cloud, sunshine, wind_direction, wind_speed]
columns = ["pressure", "temparature", "humidity", "cloud", "sunshine", "winddirection", "windspeed"]

input_df = pd.DataFrame([input_data], columns=columns)

# ----- prediction -----
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][prediction] if hasattr(model, "predict_proba") else None
    percentage_prob = probability * 100

    if prediction == 1:
        st.success(f"🌧️ Prediction: Rainfall likely! Probability: {percentage_prob:.2f}%" if probability else "🌧️ Prediction: Rainfall likely!")
    else:
        st.info(f"☀️ Prediction: No Rainfall. Probability: {percentage_prob:.2f}%" if probability else "☀️ Prediction: No Rainfall")
