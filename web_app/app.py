import numpy as np
import pandas as pd
import joblib
import streamlit as st
from model.config import config


st.header('Welcome to insurance prediction web app', divider='rainbow')

st.write("SEX ?")
female = st.checkbox('Female')
man = st.checkbox('Male')

if female:
    st.write('Great you are female')

if man:
    st.write('Great you are male')