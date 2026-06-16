import os
import streamlit as st
import requests

API_URL = os.environ.get("API_URL", "http://fastapi:8000")

st.title("House Price Prediction")
st.write("Enter property details to get an estimated price.")

bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
area = st.number_input("Area (sqft)", min_value=100.0, value=2000.0)
age = st.number_input("Age of property (years)", min_value=0, value=10)

if st.button("Predict Price"):
    payload = {
        "bedrooms": int(bedrooms),
        "bathrooms": int(bathrooms),
        "area": float(area),
        "age": int(age)
    }
    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        result = response.json()
        st.success(f"Predicted Price: ${result.get('predicted_price', 'N/A'):,.2f}")
        st.json(result)
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
