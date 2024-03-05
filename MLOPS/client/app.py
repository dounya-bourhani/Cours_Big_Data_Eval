# app/client/app.py
import streamlit as st
import requests

st.title("Iris Classification App")

# Feature inputs
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.3)

# Button to trigger prediction
if st.button("Predict"):
    # Make a request to FastAPI server for prediction
    response = requests.post(
        "http://server:8000/predict",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
    )

    # Display predicted class
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicted Class: {prediction}")
        st.balloons()
    else:
        st.error("Prediction failed. Please try again.")
