import streamlit as st
import pandas as pd
import joblib

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# -------------------- Load Model --------------------
model = joblib.load("best_model.joblib")

# -------------------- Title --------------------
st.title("❤️ Heart Disease Prediction")
st.markdown("Enter the patient's information and click **Predict**.")

# -------------------- Sidebar --------------------
st.sidebar.header("About")
st.sidebar.write("""
This application predicts whether a patient is likely to have heart disease using a trained CatBoost model.
""")

# -------------------- Input --------------------
col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Enter the patient's age.",
        min_value=1,
        max_value=120,
        value=45
    )

    sex = st.selectbox(
        "Select the patient's gender.",
        ["Female", "Male"]
    )

    cp = st.selectbox(
        "Select the type of chest pain experienced",
        [
            "Asymptomatic",
            "Non-anginal Pain",
            "Atypical Angina",
            "Typical Angina"
        ]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Cholesterol Level (mg/dL)",
        min_value=50,
        max_value=700,
        value=200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        ["No", "Yes"]
    )

    restecg = st.selectbox(
        "Resting ECG Result",
        [
            "Normal",
            "ST-T Abnormality",
            "Left Ventricular Hypertrophy"
        ]
    )

with col2:

    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

    exang = st.selectbox(
        "Chest Pain During Exercise?",
        ["No", "Yes"]
    )

    oldpeak = st.number_input(
        "ST Depression Value",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    slope = st.selectbox(
        "ECG Stress Test Result",
        [
            "Upsloping",
            "Flat",
            "Downsloping"
        ]
    )

    ca = st.selectbox(
        "Blocked Major Blood Vessels",
        [0,1,2,3,4]
    )

    thal = st.selectbox(
        "Thalassemia Test Result",
        [
            "Normal",
            "Fixed Defect",
            "Reversible Defect",
            "Unknown"
        ]
    )

# -------------------- Encoding --------------------

sex = 1 if sex == "Male" else 0

cp = {
    "Typical Angina":0,
    "Atypical Angina":1,
    "Non-anginal Pain":2,
    "Asymptomatic":3
}[cp]

fbs = 1 if fbs=="Yes" else 0

restecg = {
    "Normal":0,
    "ST-T Abnormality":1,
    "Left Ventricular Hypertrophy":2
}[restecg]

exang = 1 if exang=="Yes" else 0

slope = {
    "Upsloping":0,
    "Downsloping":2,
    "Flat":1
}[slope]

thal = {
    "Unknown":0,
    "Normal":1,
    "Fixed Defect":2,
    "Reversible Defect":3
}[thal]

# -------------------- Predict --------------------

if st.button("Predict Heart Disease"):

    data = pd.DataFrame(
        [[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]],
        columns=[
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal"
        ]
    )

    prediction = model.predict(data)[0]

    try:
        probability = model.predict_proba(data)[0][1]
    except:
        probability = None

    st.divider()

    if prediction == 1:

        st.error("⚠️ Heart Disease Detected")

    else:

        st.success("✅ No Heart Disease")

    if probability is not None:

        st.subheader("Prediction Probability")

        st.progress(float(probability))

        st.write(f"Probability : **{probability:.2%}**")

    st.subheader("Patient Data")

    st.dataframe(data)
