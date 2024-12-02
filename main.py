import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("Select animal type", ("dog", "cat", "cow", "horse"))
color = st.sidebar.selectbox("Select color", ("brown", "black", "white", "grey"))

# Add a button to generate pet names
if st.button("Generate Pet Names"):
    response = lch.generate_pet_name(animal_type, color)
    st.write(response['pet_name']) 

