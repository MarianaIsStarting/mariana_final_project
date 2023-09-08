import streamlit as st
from PIL import Image
import pickle
import numpy as np




#Fetal Monitoring
st.title("Fetal Monitoring")
st.write("")
st.header("*Cardiotocogram - CTG*", divider = "violet")
st.write("")
st.write("")
st.subheader(":large_purple_circle: Cardiotocogram is a simple and cost effective way to monitor the baby and the course of birth.")
st.write("")
st.write("")
st.write("")

image_1 = Image.open("heavily-pregnant-women-hospital-ctg-footage-141947279_iconl.jpeg")
col1, col2 = st.columns(2)
with col1:
    st.image(image_1, caption="CTG Scan")
with col2:
    st.write("")
    st.write("")
    st.write("- Two electrodes are placed on the mother's abdomen and it can be used for continuous or intermittent monitoring.")
    st.write("")
    st.write("- Early detection of fetal distress is important to decide the course of childbirth and prevent complications.")
    st.write("")
st.write("")
st.write("")
st.write("")
st.subheader(":large_purple_circle: The CTG measures:")
st.write("")

col18, col19, col20 = st.columns([1,2,1])
with col19:
    st.subheader (":heartbeat: Fetal Heart Rate")
    st.subheader (":boom: Uterine Contractions")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.subheader(":large_purple_circle: From these measurements, other variables are computed by the CTG software.")
st.write("- Heart rate variability")
st.write("- Accelerations")
st.write("- Decelerations")
st.write("- Etc...")
st.write("")
st.write("")
st.write("")
st.write("")
image_12 = Image.open("CTG_Output.jpg")
image_2 = Image.open("1611607-ctg-reading-these-bh-2e87b26b3871e385.jpeg")
col3, col4 = st.columns(2)
with col3:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader(":large_purple_circle: The interpretation of the CTG comes from the relation between all these variables.")
    
with col4:
    st.image(image_2, caption="CTG Reading")
    
st.write("")
st.write("")
st.write("")
st.write("")


