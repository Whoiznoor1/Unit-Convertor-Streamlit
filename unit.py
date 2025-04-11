import streamlit as st

# Custom CSS styling for a modern look
st.markdown("""
<style>
h1 {
    color: #2E8B57;
    text-align: center;
    font-weight: 800;
    font-size: 3em;
}
.stSelectbox, .stNumberInput, .stButton {
    font-size: 1.1em !important;
}
.stButton>button {
    background-color: #2E8B57;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    margin-top: 10px;
    transition: 0.3s ease;
}
.stButton>button:hover {
    background-color: #256d46;
}
</style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1>Smart Unit Converter</h1>", unsafe_allow_html=True)

# User selects conversion category
conversion_type = st.selectbox("Choose a Conversion Type", ["Distance", "Temperature", "Weight", "Pressure"])

# Define unit mappings and logic
def get_units(type_):
    if type_ == "Distance":
        return ["Meters", "Kilometers", "Miles", "Yards", "Feet"]
    elif type_ == "Temperature":
        return ["Celsius", "Fahrenheit", "Kelvin"]
    elif type_ == "Weight":
        return ["Kilograms", "Grams", "Pounds", "Ounces"]
    elif type_ == "Pressure":
        return ["Pascal", "Bar", "PSI", "Atmosphere"]

def convert(value, from_unit, to_unit, category):
    if category == "Distance":
        meter_values = {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Yards": 0.9144,
            "Feet": 0.3048
        }
        return value * meter_values[from_unit] / meter_values[to_unit]

    elif category == "Weight":
        kg_values = {
            "Kilograms": 1,
            "Grams": 1000,
            "Pounds": 2.20462,
            "Ounces": 35.274
        }
        return value * kg_values[from_unit] / kg_values[to_unit]

    elif category == "Pressure":
        pa_values = {
            "Pascal": 1,
            "Bar": 100000,
            "PSI": 6894.76,
            "Atmosphere": 101325
        }
        return value * pa_values[from_unit] / pa_values[to_unit]

    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Units based on chosen type
units = get_units(conversion_type)

# Input section
from_unit = st.selectbox("Convert From", units)
to_unit = st.selectbox("Convert To", units)
value = st.number_input("Enter Value to Convert", min_value=0.0, step=0.1)

# Action button
if st.button("Convert Now"):
    if value <= 0:
        st.warning("Please enter a value greater than zero to convert.")
    else:
        converted_value = convert(value, from_unit, to_unit, conversion_type)
        st.success(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit} 🔄")
