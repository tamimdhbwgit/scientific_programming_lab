import streamlit as st
import pandas as pd
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Session state to remember last prediction ---
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# --- Page Config ---
st.set_page_config(page_title="Medical Insurance Premium Calculator", page_icon="🏥")
st.title("🏥 Medical Insurance Premium Calculator")
st.write("Fill in your health details below to get an instant premium estimate.")
st.divider()

# --- Input Fields ---
col1, col2 = st.columns(2)

with col1:
    age        = st.slider("Age", 18, 66, 30)
    height     = st.number_input("Height (cm)", 140, 200, 165)
    weight     = st.number_input("Weight (kg)", 40, 150, 70)
    diabetes   = st.selectbox("Diabetes?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    bp         = st.selectbox("Blood Pressure Problems?", [0, 1], format_func=lambda x: "Yes" if x else "No")

with col2:
    transplant = st.selectbox("Any Transplants?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    chronic    = st.selectbox("Any Chronic Diseases?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    allergies  = st.selectbox("Known Allergies?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    cancer_fam = st.selectbox("History of Cancer in Family?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    surgeries  = st.slider("Number of Major Surgeries", 0, 3, 0)

st.divider()

# --- Auto BMI ---
bmi = weight / ((height / 100) ** 2)
st.metric("Your Calculated BMI", f"{bmi:.1f}")

# --- Predict Button ---
if st.button("💰 Predict My Premium"):
    input_data = pd.DataFrame(
        [[age, diabetes, bp, transplant, chronic,
          height, weight, allergies, cancer_fam, surgeries, bmi]],
        columns=["Age", "Diabetes", "BloodPressureProblems", "AnyTransplants",
                 "AnyChronicDiseases", "Height", "Weight", "KnownAllergies",
                 "HistoryOfCancerInFamily", "NumberOfMajorSurgeries", "BMI"]
    )
    st.session_state.prediction = model.predict(input_data)[0]  # store result

# --- Show result (persists even if user changes a slider) ---
if st.session_state.prediction is not None:
    st.success(f"### Estimated Annual Premium: ₹{st.session_state.prediction:,.0f}")
