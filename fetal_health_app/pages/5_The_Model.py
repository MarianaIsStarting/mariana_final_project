import streamlit as st
from PIL import Image
import pickle
import numpy as np


# The Fetal Health Predictive Model
st.title("The Fetal Health Predictive Model")
st.write("")
st.header("*The Model in action*", divider = "blue")
st.write("")
st.write("")
st.write("")
st.subheader(":large_blue_circle: Predictive model of fetal health: healthy, suspicious or pathological situation, based on a few parameters of the CTG scan.")
st.write("")
st.write("")
st.write("")
st.write("")
image_5 = Image.open("images.jpeg")
image_10 = Image.open("feto-2.jpg")
image_11 = Image.open("1611607-ctg-reading-these-bh-2e87b26b3871e385.jpeg")
image_13 = Image.open("cardiotocografia-1-750x430-3.jpg")
col7, col8 = st.columns(2)
with col7:
    st.write("")
    st.write("")
    st.image(image_13)
    st.write("")
    st.write("")
    st.image(image_10)
with col8:
    baseline_heart_rate = st.slider("Baseline Heart Rate", min_value=90, max_value=220, step=1, format=None, label_visibility="visible")
    accelarations = st.number_input("Accelerations per second")
    uterine_contractions = st.number_input("Uterine Contractions per second")
    prolongued_decelarations = st.number_input("Prolongued Decelerations per second")
    abnormal_short_term_variability = st.number_input("Abnormal short term variability", min_value=0)
    percentage_of_time_with_abnormal_long_term_variability = st.slider("Percentage of time with abnormal long term variability", min_value = 0, max_value=100, step=1, label_visibility="visible")
st.write("")
st.write("")
#### PICKLE
# model for 5:the_model = pickle.load(open("random_forest_model.pkl", "rb"))
# model for 6:
the_model = pickle.load(open("random_forest_model_6.pkl", "rb"))

col9, col10 = st.columns(2)
with col10:
    try:
        if st.button("Check the Result"):
            user_input = np.array([[baseline_heart_rate, accelarations, uterine_contractions, prolongued_decelarations, abnormal_short_term_variability, percentage_of_time_with_abnormal_long_term_variability]])
            result = the_model.predict(user_input)
        if result == 1:
            st.subheader("Healthy :white_check_mark:")
        elif result == 2:
            st.subheader("Suspicious :bell:")
        elif result == 3:
            st.subheader("Pathological :rotating_light:")
    except:
        result = "Insert details to check."
st.write("")
st.write("")
col11, col12= st.columns(2) 
col11.metric(label="Baseline Heart Rate", value= baseline_heart_rate, delta = "bpm")
col12.metric(label="Uterine Contractions", value= uterine_contractions, delta = "per sec")
col13, col14= st.columns(2) 
col13.metric(label="Accelerations", value= accelarations, delta = "per sec")
col14.metric(label="Prolongued Decelerations", value= prolongued_decelarations, delta = "per sec")
col15, col16 = st.columns(2)
col15.metric(label="Abnormal Short Term Variability", value= abnormal_short_term_variability, delta = "ms")
col16.metric(label="Percentage of Time with Long Term Variability", value = percentage_of_time_with_abnormal_long_term_variability, delta = "%")
st.write("")
st.write("")
st.write("")
st.write("")
if result == 1:
    agree = st.subheader(":white_check_mark: Email your Team and book your next appoitment.")
if result == 2:
    agree = st.subheader(":bell: Call your Team urgently and scheduale an observation in the next hour.")
if result == 3:
    agree = st.subheader(":rotating_light: Call your Team urgently and follow the protocol.")
st.write("")
st.write("")
col32, col33 = st.columns([1,3])
with col33:
    st.subheader("Choose your Medical Team:")
    st.checkbox("Medical Team A")
    st.checkbox("Medical Team B")
    st.checkbox("Medical Team C")



#if agree:


#if result == 1:
    #st.checkbox("Email your team and book your next appoitment.")
#if result == 2:
    #st.checkbox("Call your team urgently and scheduale a new observation in the next 2 hours.")
#if result == 3:
    #st.checkbox("Call your team urgently and follow the protocol.")
