import streamlit as st
from eda import run_eda
from pred_model import run_model_prediction

st.sidebar.title("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["EDA", "Model Prediksi"])

if selection == "EDA":
    run_eda()
elif selection == "Model Prediksi":
    run_model_prediction()