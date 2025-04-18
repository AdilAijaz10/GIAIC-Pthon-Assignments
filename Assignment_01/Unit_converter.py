import streamlit as st

# Conversion dictionaries
CONVERSIONS = {
    "Length": {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "feet": 0.3048,
        "inches": 0.0254
    },
    "Weight": {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495
    }
}

def convert_units(value, from_unit, to_unit, conv_type):
    if conv_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        return value
    
    # For Length and Weight
    factors = CONVERSIONS[conv_type]
    return value * factors[from_unit] / factors[to_unit]

st.title("Unit Converter")

# Main conversion interface
conv_type = st.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0)

units = {
    "Length": ["meters", "kilometers", "centimeters", "feet", "inches"],
    "Weight": ["kilograms", "grams", "pounds", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit"]
}

from_unit = st.selectbox("From Unit", units[conv_type])
to_unit = st.selectbox("To Unit", units[conv_type])

result = convert_units(value, from_unit, to_unit, conv_type)
st.write(f"Result: {result:.2f} {to_unit}")