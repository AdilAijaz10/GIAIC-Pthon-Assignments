import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="My First Streamlit App", page_icon="👋")

# Add a title
st.title("Welcome to My First Streamlit App!")

# Add a header
st.header("Let's try some cool features")

# Add text input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello {name}! Nice to meet you!")

# Add a slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old")

# Add a button
if st.button("Generate Random Chart"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Line 1', 'Line 2', 'Line 3']
    )
    st.line_chart(chart_data)

# Add sidebar
st.sidebar.header("About")
st.sidebar.write("My Name is Adil Aijaz and I am Graduated as a Computer Engineer. Currently I am enrolled in Governor Sindh Initiative for GenAl, Web3, and Metaverse ")

# Footer
st.markdown("---")

