# Student Performance Predictor

## Project Overview
Student Performance Predictor is a machine learning project that
estimates students' final mathematics grades using academic and
study-related information.

## Dataset
The project uses the Student Performance dataset from the
UCI Machine Learning Repository.

Dataset source:
https://archive.ics.uci.edu/dataset/320/student+performance

## Technologies
- Python
- Pandas
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning
A Linear Regression model is trained to predict the final grade (G3)
using study time, previous grades, absences, and other student features.

The model is evaluated using MAE, RMSE, and R-squared.

## Application
The Streamlit application allows users to enter student information
and receive an estimated final grade out of 20.

## Disclaimer
Predictions are estimates for educational purposes only.
They are not guaranteed results and should not be used to make
high-stakes decisions about students.

## Run Locally
1. Install the required packages:
   pip install -r requirements.txt

2. Run the application:
   streamlit run app.py
