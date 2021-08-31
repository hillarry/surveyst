# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:18:01 2021

@author: User
"""

import streamlit as st

your_name = st.text_input('Enter your name')

st.title(f"**Welcome from Simbolo,{your_name}**")

st.write(f"**This is the survey web app for simbolo**")

selectbox = st.sidebar.selectbox(
    "Select subject",
    ['',"Natural Language Processing", "Computer vision","Speech Recognition"]
)
st.write(f"I am interested in {selectbox}")

second_selectbox = st.sidebar.selectbox(
        "How many months did you learn in Simbolo",
        ['',"1 month","2 months","3 months"]
)
st.write(f"I learn {selectbox} at simbolo for {second_selectbox}")

#learning_types = ["Enjoy","Not Enjoy"]
#learning = st.radio("Learning",learning_types)
st.write(f'**Learning journey**')
st.slider(label = "Select your enjoy level",min_value=0,max_value=100)

st.write(f'What did you learn from simbolo?')
option1 = st.checkbox('AI')
option2 = st.checkbox('Machine Learning')
option3 = st.checkbox('Deep Learning')
option4 = st.checkbox('Natural Language Processing')

#form = st.form(key='my_form')
#submit_button = form.form_submit_button(label='Submit')
with st.form('Form'):
    submit_button = st.form_submit_button('Submit')

st.write(f'**Thanks for your submitting!!Hope you see in next class**')