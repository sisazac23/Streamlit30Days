import streamlit as st

st.header('st.checkbox')

icecream = st.checkbox('Icecream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write('You selected icecream')

if coffee:
    st.write('You selected coffee')

if cola:
    st.write('You selected cola')