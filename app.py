import streamlit as st
import requests

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

# Predict button
if st.button("Predict"):
    data = {
        "age": age,
        "workclass": workclass,
        "fnlwgt": fnlwgt,
        "education": education,
        "educational_num": educational_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        st.success(f"Prediction: {response.json()['prediction']}")
    else:
        st.error("Error in prediction")