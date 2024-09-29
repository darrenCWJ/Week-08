import pandas as pd
import streamlit as st
import json

filepath = './data/courses-full.json'

with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

df = pd.DataFrame(dict_of_courses)

# Display the DataFrame in a Streamlit table
df = df.T.reset_index(drop=True)
st.dataframe(df)