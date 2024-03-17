import numpy as np
import pandas as pd
import streamlit as st
from model.config import config
import tensorflow as tf


st.header('Welcome to insurance prediction web app \U0001f600', divider='rainbow')

# User enter age
age = st.number_input(f'Enter your {config.FEATURES[0].upper()}',min_value=18, max_value=99)

# User Sex select
sex = None
sex = st.radio(f"{config.FEATURES[1].upper()}",["Female", "Male"])

if sex == "Female":
    sex = 0
elif sex == "Male":
    sex = 1

# User enter bmi
bmi = st.number_input(f'Enter your {config.FEATURES[2].upper()}')

#User enter children value
children = st.number_input(f'Enter your {config.FEATURES[3].upper()}', value=None, placeholder="Type a number...",max_value=10)

# Smoker
smoke = None
smoker = st.radio(f"{config.FEATURES[4].upper()}",["No", "Yes"])
if smoker == "No":
    smoke = 0
elif smoker == "Yes":
    smoke = 1

# User select region
regions = [config.NEW_FEATURES[5], config.NEW_FEATURES[6],config.NEW_FEATURES[7], config.NEW_FEATURES[8]]
regions_number_values = regions.copy()
region = st.radio(f"{config.FEATURES[5].upper()}",regions)


# Assigns the value 1 to the selected region and fills the rest of the regions with 0.
def get_region_value(arr):
    for i ,value in enumerate(arr):
        if region == value:
            index = regions.index(region)
            arr[index] = 1
        if any(arr):
        # Bir varlık bulunduğunda, tüm elemanları sıfırlarla doldur
            arr = [0 if x != 1 else 1 for x in arr]
    return arr

region_value = get_region_value(arr=regions_number_values)


# User values
user_values = [age,sex,bmi,children,smoke] + region_value


# Load model
insurance_model = tf.keras.models.load_model(config.MODEL_NAME)


user_values_array = np.array(user_values, dtype=np.float32).reshape(1, -1)
# model predict

if st.button('Predict'):
    result = insurance_model.predict(user_values_array)
    predicted_cost = result[0][0] 
    st.header(f"Predicted insurance cost: {predicted_cost:.2f} \U0001F4B0")