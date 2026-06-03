import streamlit as st
import joblib
import gdown
import os
import numpy as np

file_id = '1EWF_APBIYu9MjbMPwBuhp-qS8lA9Ew2c'
url = f'https://drive.google.com/uc?export=download&id={file_id}'
output = 'best_random_forest_model.pkl'

@st.cache_resource
def load_model():
    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)
    return joblib.load(output)
try:
    model = load_model()
    st.success("sucessfly")
except Exception as e:
    st.error(f"error : {e}")






scaler = joblib.load("scaler.pkl")
columns = joblib.load("model_columns.pkl")

st.title(" Protein Structure Resolution Prediction")

col1, col2 = st.columns(2)

with col1:
    matthews = st.slider("Matthews Coefficient", 1.0, 5.0, 2.5, key="matthews")
    solvent = st.slider("Solvent Content (%)", 0.0, 100.0, 50.0, key="solvent")
    ph = st.slider("pH", 0.0, 14.0, 7.0, key="ph")

with col2:
    temp = st.slider("Temperature (K)", 250.0, 350.0, 300.0, key="temp")
    r_free = st.slider("R Free", 0.0, 1.0, 0.2, key="r_free")
    r_work = st.slider("R Work", 0.0, 1.0, 0.2, key="r_work")


if st.button("Predict Resolution", key="predict_btn"):

    input_data = np.zeros(len(columns))

    input_data[0] = matthews
    input_data[1] = solvent
    input_data[2] = ph
    input_data[3] = temp
    input_data[4] = r_free
    input_data[5] = r_work

    input_data = scaler.transform([input_data])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Resolution: {round(prediction, 2)} Å")

    if prediction < 2:
        st.info("🟢 High resolution (Excellent quality)")
    elif prediction < 3:
        st.warning("🟡 Medium resolution")
    else:
        st.error("🔴 Low resolution")







    
