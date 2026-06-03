import streamlit as st
import joblib
from huggingface_hub import hf_hub_download

# Repository details and filename
REPO_ID = "7777jnjsd/protein-model"
FILENAME = "best_random_forest_model.pkl"

@st.cache_resource
def load_model():
    # Downloading the model safely from Hugging Face
    model_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    return joblib.load(model_path)

# Loading the model
try:
    model = load_model()
    st.success("Model loaded successfully from Hugging Face!")
except Exception as e:
    st.error(f"Error loading the model: {e}")





model = joblib.load("best_random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("model_columns.pkl")

st.title(" Protein Structure Resolution Prediction")

col1, col2 = st.columns(2)

with col1:
    matthews = st.slider("Matthews Coefficient", 1.0, 5.0, 2.5)
    solvent = st.slider("Solvent Content (%)", 0.0, 100.0, 50.0)
    ph = st.slider("pH", 0.0, 14.0, 7.0)

with col2:
    temp = st.slider("Temperature (K)", 250.0, 350.0, 300.0)
    r_free = st.slider("R Free", 0.0, 1.0, 0.2)
    r_work = st.slider("R Work", 0.0, 1.0, 0.2)


if st.button(" Predict Resolution"):

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