import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Adult Income Prediction App")

# Input form
age = st.number_input("Age", 17, 90, 35)
workclass = st.selectbox("Workclass", ["Private", "Self-emp-not-inc", "Local-gov"])
fnlwgt = st.number_input("Fnlwgt", 10000, 1000000, 200000)
education = st.selectbox("Education", ["Bachelors", "HS-grad", "Masters"])
educational_num = st.number_input("Educational Num", 1, 20, 10)
marital_status = st.selectbox("Marital Status", ["Married-civ-spouse", "Never-married"])
occupation = st.selectbox("Occupation", ["Tech-support", "Sales", "Exec-managerial"])
relationship = st.selectbox("Relationship", ["Husband", "Not-in-family"])
race = st.selectbox("Race", ["White", "Black"])
gender = st.selectbox("Gender", ["Male", "Female"])
capital_gain = st.number_input("Capital Gain", 0, 99999, 0)
capital_loss = st.number_input("Capital Loss", 0, 99999, 0)
hours_per_week = st.number_input("Hours per Week", 1, 100, 40)
native_country = st.selectbox("Native Country", ["United-States", "India"])

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "age": age,
        "workclass": workclass,
        "fnlwgt": fnlwgt,
        "education": education,
        "educational-num": educational_num,
        "marital-status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital-gain": capital_gain,
        "capital-loss": capital_loss,
        "hours-per-week": hours_per_week,
        "native-country": native_country
    }])

    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")