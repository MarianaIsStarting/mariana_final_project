import streamlit as st
from PIL import Image
import pickle
import numpy as np



## fetal health - beginning
st.set_page_config(page_title = "Fetal Health", page_icon = ":foot:", layout = "wide")

st.sidebar.success("Select a page")

st.title("Fetal Health Prediction from Cardiotocogram (CTG)")
st.write("")
st.header("***A tool to improve care plans based on CTG readings***", divider = "gray")
st.write("")
st.write("")
st.write("")
st.write("")
st.header("Mother and Baby's well being",  divider = "orange")
st.write("")
st.write("")

image5 = Image.open("newborn.jpg.webp")
col23, col24 = st.columns(2)
with col23:
    st.image(image5, caption = "Newborn baby")
with col24:
    st.write("")
    st.write("- *A maternal death occurred almost every two minutes in 2020.* (WHO)")
    st.write("- *Children who die within the first 28 days of birth suffer from conditions and diseases associated with lack of quality care at or immediately after birth and in the first days of life.* (WHO)")
st.write("")
st.write("")
st.subheader(":large_orange_diamond: It is possible to reduce infant and maternal death with appropriate healthcare assistance and monitoring during and prior birth.")
st.write("")
st.write("")
st.write("")
st.write("")






