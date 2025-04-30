import streamlit as st
import pandas as pd
import joblib

model = joblib.load('bike_price_model.pkl')

# Streamlit app UI
st.title("🚴‍♂️ Used Bike Price Predictor")

st.markdown("### Enter Bike Details")

bike_name = st.text_input("Bike Name (e.g. Honda Shine)")
city = st.text_input("City (e.g. Mumbai)")
kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=300000, step=100)
owner = st.selectbox("Owner Type", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])
age = st.number_input("Age of the Bike (in years)", min_value=0.0, max_value=30.0, step=0.5)
power = st.number_input("Engine Power (in CC)", min_value=50.0, max_value=1000.0, step=1.0)
brand = st.text_input("Brand (e.g. Honda)")

# Predict button
if st.button("Predict Price"):
    # Prepare input as DataFrame
    input_data = pd.DataFrame({
        'bike_name': [bike_name],
        'city': [city],
        'kms_driven': [kms_driven],
        'owner': [owner],
        'age': [age],
        'power': [power],
        'brand': [brand]
    })

    # Make prediction
    predicted_price = model.predict(input_data)[0]
    st.success(f"💰 Estimated Price: ₹{predicted_price:,.2f}")
