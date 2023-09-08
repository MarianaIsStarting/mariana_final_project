import streamlit as st
from PIL import Image
import pickle
import numpy as np
import streamlit as st
import pandas as pd

# Building the model

st.title("Model Construction")
st.write("")
st.header("* How was the model built?*", divider = "green")
st.write("")
st.write("")
st.write("")
st.subheader(":large_green_circle: The model was trained and tested on a Database with over 2000 CTG observations, already classified by 3 obstetricians:")
st.write("")
st.write("")
st.write("")
col27, col28, col29 = st.columns(3)
with col28:
    st.subheader(":white_check_mark: Healthy")
    st.subheader(":bell: Suspicious")
    st.subheader(":rotating_light: Pathological")
st.write("")
st.write("")
st.write("")

st.write("")

image_8 = Image.open("Python-image-with-logo-940x530-1.jpg.webp")
col21, col22 = st.columns(2)
with col21:
    st.image(image_8)
with col22:
    st.write("")
    st.write("")
    st.write(":heavy_check_mark: Data Cleaning")
    st.write(":heavy_check_mark: Libraries: Pandas, Numpy, Matplotlib, Seaborn, ScikitLearn")
    st.write(":heavy_check_mark: Many attempts with different models")
st.write("")
st.write("")
st.write("")
st.write("")

image_7 = Image.open("random_forest.jpg")
col25, col26 = st.columns(2)
with col25:
    st.image(image_7)
with col26:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader(":white_check_mark: Best Result: *Ramdom Forest* through *Randomized Search* with *Cross-validation*")
st.write("")
st.write("")
st.write("")
st.write("")
st.subheader(":large_green_circle: Accuracy: 94%")
st.write("")
st.write("")

df = pd.DataFrame(
    [
        {"Fetal Health": "Healthy", "Precision": 0.94, "Recall": 0.99, "F1-score": 0.96},
        {"Fetal Health": "Suspicious", "Precision": 0.91, "Recall": 0.75, "F1-score": 0.82},
        {"Fetal Health": "Pathological", "Precision": 0.97, "Recall": 0.87, "F1-score": 0.92}
    ])
st.dataframe(df, use_container_width=True, hide_index = True)