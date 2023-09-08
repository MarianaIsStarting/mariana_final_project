import streamlit as st
from PIL import Image
import pickle
import numpy as np


st.title("Process Evaluation")
st.write("")
st.header("***Challenges and Future Improvements***", divider = "red")
st.write("")
st.write("")
st.write("")
st.subheader("Challenges",  divider = "red")
st.write("")
st.write("")
col31, col32= st.columns([1,3])
with col32:
    st.subheader(":small_red_triangle_down: Finding the right columns")
    st.write("- Not too many to be easy to use; not too little to not loose predictive power.")
    st.subheader(":small_red_triangle_down: Finding the right model")
    st.write("- Hyperparameter tuning was very challenging.")
st.write("")
st.write("")
st.subheader("Future Improvements",  divider = "red")
st.write("")
st.write("")
col33, col34= st.columns([1,3])
with col34:
    st.subheader(":small_red_triangle: More data to train the model")
    st.write("- To increase its predictive power.")
    st.subheader(":small_red_triangle: Connecting the CTG machine with the app to run the model")
    st.write("- Continuos readings and predictions.")
    st.subheader(":small_red_triangle: Adding a feature to contact the clinical team")
    st.write("- It would make the model more useful.")
