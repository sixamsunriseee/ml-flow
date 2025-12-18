from predict import predict

import streamlit as st


st.title("🌸 Iris Species Predictor")
st.set_page_config(page_title="Iris Detector", page_icon="🌸", layout="centered")

with st.form("iris_form"):
    sepal_length = st.number_input("Sepal length (cm)", value=5.1, step=0.1)
    sepal_width = st.number_input("Sepal width (cm)", value=3.5, step=0.1)
    petal_length = st.number_input("Petal length (cm)", value=1.4, step=0.1)
    petal_width = st.number_input("Petal width (cm)", value=0.2, step=0.1)

    submitted = st.form_submit_button("Predict")

if submitted:
    try:
        features = [sepal_length, sepal_width, petal_length, petal_width]
        print(features)
        species = predict(features)
        st.success(f"Predicted species: **{species}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
