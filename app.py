import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. SETUP & LOADING
st.set_page_config(page_title="Cardiac AI", layout="wide")

@st.cache_resource # This makes the app faster by loading files only once
def load_assets():
    model = joblib.load('heart_model.pkl')
    scaler = joblib.load('scaler.pkl')
    cols = joblib.load('columns.pkl')
    return model, scaler, cols

model, scaler, all_columns = load_assets()

# 2. SIDEBAR - DATA COLLECTION
def get_user_input():
    st.sidebar.header("📋 Patient Clinical Data")
    
    # Numerical Inputs
    age = st.sidebar.slider("Age", 18, 95, 50)
    rbp = st.sidebar.slider("Resting BP (mm Hg)", 90, 200, 120)
    chol = st.sidebar.slider("Cholesterol (mg/dl)", 100, 500, 200)
    max_hr = st.sidebar.slider("Max Heart Rate", 60, 220, 150)
    oldpeak = st.sidebar.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
    
    # Categorical Inputs (User sees text, model gets numbers)
    sex = st.sidebar.selectbox("Gender", ["Male", "Female"])
    angina = st.sidebar.selectbox("Exercise Angina", ["No", "Yes"])
    slope = st.sidebar.selectbox("ST Slope", ["Up", "Flat", "Down"])
    
    # Create the dictionary to match the One-Hot Encoding names exactly
    data = {
        "Age": age, "RestingBP": rbp, "Cholesterol": chol, 
        "FastingBS": 0, "MaxHR": max_hr, "Oldpeak": oldpeak,
        "Sex_M": 1 if sex == "Male" else 0,
        "ExerciseAngina_Y": 1 if angina == "Yes" else 0,
        "ST_Slope_Flat": 1 if slope == "Flat" else 0,
        "ST_Slope_Up": 1 if slope == "Up" else 0,
        # Filling other dummies as 0 to avoid errors
        "ChestPainType_ATA": 0, "ChestPainType_NAP": 0, "ChestPainType_TA": 0,
        "RestingECG_Normal": 1, "RestingECG_ST": 0
    }
    return data

user_data = get_user_input()
