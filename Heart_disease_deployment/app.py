import streamlit as st
import pickle

st.title("Heart Disease Predictor")


with open("heart_model_new.pkl", "rb") as f:
    model = pickle.load(f)


with st.form("heart_form"):
    age = st.number_input("Age", min_value=1, max_value=120)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    chol = st.number_input("Cholesterol", min_value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["Yes", "No"])
    restecg = st.selectbox("Resting ECG", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate", min_value=0)
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak", format="%.2f")
    slope = st.selectbox("ST Slope", [0, 1, 2])

    submit = st.form_submit_button("Predict")

    if submit:

        sex_male = 1 if sex == "Male" else 0

        chest_pain_type_ata = 1 if cp == "Atypical Angina" else 0
        chest_pain_type_nap = 1 if cp == "Non-Anginal" else 0
        chest_pain_type_ta = 1 if cp == "Asymptomatic" else 0

        fasting_blood_sugar_normal = 1 if fbs == "No" else 0
        exang_val = 1 if exang == "Yes" else 0

        input_data = [[
            age, trestbps, chol, restecg, thalach, exang_val, oldpeak, slope,
            sex_male, chest_pain_type_ata, chest_pain_type_nap, chest_pain_type_ta,
            fasting_blood_sugar_normal
        ]]


        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("High risk of Heart disease.")
        else:
            st.success("Low risk of Heart disease.")


        st.subheader("Your Health Insights")

        if chol < 200:
            st.info("Cholesterol is in the desirable range (< 200 mg/dL).")
        elif 200 <= chol <= 239:
            st.info("Cholesterol is in the borderline high range (200–239 mg/dL).")
        else:
            st.info("Cholesterol is high (> 240 mg/dL). Consider getting it checked.")

        if trestbps < 120:
            st.info("Resting BP is normal (< 120 mm Hg).")
        elif 120 <= trestbps <= 139:
            st.info("Resting BP is medium (120–139 mm Hg).")
        else:
            st.info("Resting BP is high (≥ 140 mm Hg). Risk of hypertension.")

        st.info(f"Chest pain type: {cp}.")

        if cp == "Typical Angina":
            st.info("Typical angina can indicate serious heart disease.")
        elif cp == "Asymptomatic":
            st.info("No chest pain reported — asymptomatic.")

        if fbs == "Yes":
            st.info("Fasting blood sugar is high (> 120 mg/dL). Risk of diabetes.")
        else:
            st.info("Fasting blood sugar is normal (≤ 120 mg/dL).")

        if thalach < 100:
            st.info("Max heart rate is low (< 100 bpm). Could indicate heart issues.")
        elif thalach > 170:
            st.info("Max heart rate is very high (> 170 bpm).")
        else:
            st.info("Max heart rate is in average range (100–170 bpm).")

        if exang == "Yes":
            st.info("You experience angina during exercise. Consult a cardiologist.")
        else:
            st.info("No angina during exercise — good sign.")

        if oldpeak < 1:
            st.info("ST depression is minimal — low risk.")
        elif 1 <= oldpeak <= 2:
            st.info("Moderate ST depression (1–2 mm). Keep an eye on it.")
        else:
            st.info("Significant ST depression (> 2 mm). Suggests heart stress.")
