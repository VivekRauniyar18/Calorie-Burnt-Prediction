import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('calories_model.pkl')

st.title('Calories Burnt Prediction App')

# Input fields
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=0)
height = st.number_input('Height (cm)', min_value=0.0)
weight = st.number_input('Weight (kg)', min_value=0.0)
duration = st.number_input('Duration of Exercise (min)', min_value=0.0)
heart_rate = st.number_input('Heart Rate', min_value=0.0)
body_temp = st.number_input('Body Temperature (°C)', min_value=0.0)

# Convert gender to numeric
gender_numeric = 0 if gender == 'Male' else 1

# Prediction
if st.button('Predict Calories Burnt'):
    input_data = np.array([[gender_numeric, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)
    st.success(f'Estimated Calories Burnt: {prediction[0]:.2f}')
