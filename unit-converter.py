import streamlit as st

# Conversion factors
def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084, "inches": 39.3701},
        "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
        "Temperature": "special",
        "Time": {"seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400},
        "Digital Storage": {"bytes": 1, "kilobytes": 1/1024, "megabytes": 1/(1024**2), "gigabytes": 1/(1024**3), "terabytes": 1/(1024**4)}
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # Same unit
    
    factor_from = conversion_factors[category][from_unit]
    factor_to = conversion_factors[category][to_unit]
    return value * (factor_to / factor_from)

# Streamlit UI
st.set_page_config(page_title="Advanced Unit Converter", layout="centered")
st.title("🔄 Advanced Unit Converter")

categories = ["Length", "Weight", "Temperature", "Time", "Digital Storage"]
category = st.selectbox("Select Category", categories)

units = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["seconds", "minutes", "hours", "days"],
    "Digital Storage": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
}

col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("Enter Value", min_value=0.0, format="%f")
with col2:
    from_unit = st.selectbox("From", units[category])
with col3:
    to_unit = st.selectbox("To", units[category])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# Additional Information Section
st.markdown("---")
st.markdown("### ℹ️ How it Works")
st.markdown(
    "This unit converter supports multiple measurement categories and provides accurate conversions. "
    "For temperature conversions, special formulas are used. For other categories, standardized conversion factors are applied."
)
