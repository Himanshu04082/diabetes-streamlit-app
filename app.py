import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# App title
st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient details to check if they're diabetic.")

# Sidebar input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Predict button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 The person is likely Diabetic.")
    else:
        st.success("✅ The person is likely NOT Diabetic.")
