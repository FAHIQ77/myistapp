import streamlit as st
import os
st.title("this is my app")
name=st.text_input("enter your name",key="name_input")
age=st.number_input("enter your age",min_value=18,max_value=100,step=5)
st.write(f"{name} your age is {age}")
st.selectbox("select your gender",["male","female","other"])
st.multiselect("select your choice",["python","mysql","ml","cs"])
login = st.button("login")
st.divider()
st.image(r"C:\Users\DELL\Downloads\IMG_1964.HEIC",width=90)
st.image(os.path.join(os.getcwd(),"static","static/download (1).png",))
if login:
    st.success("form submitted successfully")
    name=st.text_input("enter your name")
    age=st.number_input("enter your age",min_value=18,max_value=100,step=5)
    st.write(f"{name} your age is {age}")
    st.selectbox("select your gender",["male","female","other"])
    st.multiselect("select your choice",["python","mysql","ml","cs"])
