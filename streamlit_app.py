import streamlit as st

st.title("Hello World")

name = st.text_input("Name :")

if(name):
    st.write('Halo,', name)
else:
    st.warning("isi nama oi!!!")
