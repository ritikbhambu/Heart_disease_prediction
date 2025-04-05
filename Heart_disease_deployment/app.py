import streamlit as st
import pickle

st.title("Heart Disease Predictor")



with open("heart_model_new.pkl", "rb") as f:
    model = pickle.load(f)




with st.form("heart_form"):
    age = st.number_input("Age", min_value=1, max_value=120)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting BP (trestbps)", min_value=0)
    chol = st.number_input("Cholesterol (chol)", min_value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 (fbs)", [0, 1])
    restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate (thalach)", min_value=0)
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
    oldpeak = st.number_input("Oldpeak", format="%.2f")
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.selectbox("Number of Vessels Colored (ca)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

    submit = st.form_submit_button("Predict")

    if submit:
        sex = 1 if sex == "Male" else 0

        input_data = [[age, sex, cp, trestbps, chol, fbs, restecg,
                       thalach, exang, oldpeak, slope, ca, thal]]



        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error(" High risk of Heart disease.")
        else:
            st.success(" Low risk of Heart disease.")


        st.subheader(" Your Health Insights")


        if chol < 200:
            st.success(" Cholesterol is in the desirable range (< 200 mg/dL).")
        elif 200 <= chol <= 239:
            st.info(" Cholesterol is in the borderline high range (200–239 mg/dL).")
        else:
            st.warning(" Cholesterol is high (> 240 mg/dL). Consider getting it checked.")


        if trestbps < 120:
            st.success(" Resting BP is normal (< 120 mm Hg).")
        elif 120 <= trestbps <= 139:
            st.info(" Resting BP is medium (120–139 mm Hg).")
        else:
            st.warning(" Resting BP is high (≥ 140 mm Hg). Risk of hypertension.")


        cp_types = {
            0: "Typical angina (chest pain with exertion)",
            1: "Atypical angina (less predictable pain)",
            2: "Non-anginal pain",
            3: "Asymptomatic (no chest pain)"
        }
        st.info(f" Chest pain type: {cp_types.get(cp, 'Unknown')}.")

        if cp == 0:
            st.info(" Typical angina can indicate serious heart disease.")
        elif cp == 3:
            st.success(" No chest pain reported — asymptomatic.")


        if fbs == 1:
            st.info(" Fasting blood sugar is high (> 120 mg/dL). Risk of diabetes.")
        else:
            st.success(" Fasting blood sugar is normal (≤ 120 mg/dL).")


        if thalach < 100:
            st.info(" Max heart rate is low (< 100 bpm). Could indicate heart issues.")
        elif thalach > 170:
            st.info(" Max heart rate is very high (> 170 bpm).")
        else:
            st.success(" Max heart rate is in average range (100–170 bpm).")


        if exang == 1:
            st.info(" You experience angina during exercise. Consult a cardiologist.")
        else:
            st.success(" No angina during exercise — good sign.")


        if oldpeak < 1:
            st.success("ST depression is minimal — low risk.")
        elif 1 <= oldpeak <= 2:
            st.info(" Moderate ST depression (1–2 mm). Keep an eye on it.")
        else:
            st.info(" Significant ST depression (> 2 mm). Suggests heart stress.")


        if ca == 0:
            st.success(" No major vessels colored — low risk.")
        else:
            st.info(f" {ca} major vessels detected — higher risk of heart disease.")


        if thal == 1:
            thal_desc = "Fixed defect"
        elif thal == 2:
            thal_desc = "Normal"
        elif thal == 3:
            thal_desc = "Reversible defect"
        else:
            thal_desc = "Unknown"


        st.info(f"Thalassemia: {thal_desc}.")

        if thal == 1 or thal == 3:
            st.warning("Abnormal thalassemia detected — may increase heart disease risk.")


