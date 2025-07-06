import streamlit as st
import numpy as np
import pickle

# Load model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Diabetes Prediction App")

# Input fields
preg = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

# Predict
if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]
    st.success("Prediction: Diabetic" if prediction == 1 else "Prediction: Not Diabetic")
