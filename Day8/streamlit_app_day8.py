import streamlit as st
from datetime import time,  datetime

st.header('st.slider')

#example

st.subheader('Slider')

age = st.slider('How old are you?', 0,130,25)
st.write('I am ', age, 'years old')

#example

st.subheader('Range slider')
values = st.slider(
    'Select a range of values',
    0.0,100.0,(25.0,75.0))
st.write('Values:', values)

#example

st.subheader('Range time slider')

appointment = st.slider(
    'Schedule your appointment:',
    value = (time(11,30), time(12,45)))
st.write('You scheduled your appointment at:', appointment)

#example

st.subheader('Slider with datetime.time values')

start_time = st.slider(
    'When do you start?',
    value = datetime(2023,2,5,9,30),
    format='MM/DD/YY - hh:mm')
st.write('Start time:', start_time)