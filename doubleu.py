import streamlit as st

st.title("BMI Checker")

# User input
weight = st.number_input("Enter your weight (kg):", min_value=1)
height = st.number_input("Enter your height (meters):",
                         min_value=0.1, format="%.2f")

# Calculate BMI
if weight and height:
    bmi = weight / (height ** 2)
    st.write("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi <= 24.9:
        st.success("Healthy")
    elif 25 <= bmi <= 29.9:
        st.info("Overweight")
    else:
        st.error("Obese")
