import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Predictor")
st.write(
    "Predict a student's final mathematics grade "
    "using academic and study-related information."
)

st.info("Enter the student's information below.")

st.subheader("📚 Student Information")

studytime = st.selectbox(
    "Weekly study time",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Less than 2 hours",
        2: "2 to 5 hours",
        3: "5 to 10 hours",
        4: "More than 10 hours"
    }[x]
)

failures = st.selectbox(
    "Number of past class failures",
    options=[0, 1, 2, 3]
)

absences = st.number_input(
    "Number of school absences",
    min_value=0,
    max_value=100,
    value=0
)

G1 = st.slider("First period grade (G1)", 0, 20, 10)
G2 = st.slider("Second period grade (G2)", 0, 20, 10)

Medu = st.selectbox("Mother's education level (0–4)", [0, 1, 2, 3, 4])
Fedu = st.selectbox("Father's education level (0–4)", [0, 1, 2, 3, 4])
health = st.selectbox("Health status (1 = very bad, 5 = very good)", [1, 2, 3, 4, 5])

st.divider()

if st.button("Predict Final Grade", type="primary"):
    try:
        model_data = joblib.load("student_performance_model.joblib")
        model = model_data["model"]
        features = model_data["features"]

        student_data = pd.DataFrame([{
            "studytime": studytime,
            "failures": failures,
            "absences": absences,
            "G1": G1,
            "G2": G2,
            "Medu": Medu,
            "Fedu": Fedu,
            "health": health
        }])[features]

        prediction = model.predict(student_data)[0]
        prediction = max(0, min(20, prediction))

        st.success(f"Predicted Final Grade: {prediction:.2f} / 20")

        if prediction >= 10:
            st.write("The predicted grade is passing.")
        else:
            st.write("The predicted grade is below the passing mark.")

        st.caption(
            "This is an estimate from a machine learning model, "
            "not a guaranteed result."
        )

    except FileNotFoundError:
        st.error(
            "Model file not found. Please upload "
            "student_performance_model.joblib to the app folder."
        )
