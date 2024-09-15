import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import random
import yaml
from utils.tutorial_display import full_display

df = pd.DataFrame(
   np.random.randn(10, 2),
   columns=['lat', 'lon']
)

df2 = pd.DataFrame(
   np.random.randn(10, 2),
)

coordonates = pd.DataFrame(data = {
    'latitude': [37.7749, 34.0522],
    'longitude': [-122.4194, -118.2437],
    'location': ['San Francisco', 'Los Angeles']
})

chart = alt.Chart(df).mark_circle().encode(
    x='lat', y='lon', color='lon', tooltip=['lat', 'lon']
)

fig, ax = plt.subplots()
ax.plot(df['lat'], df['lon'])

spec = {
    "mark": "bar",
    "encoding": {
        "x": {"field": "a", "type": "ordinal"},
        "y": {"field": "b", "type": "quantitative"}
    }
}

image_file_path = 'img/streamlit-logo-primary-colormark-darktext.png'
audio_file_path = 'audio/meeting-clip1.mp3'
video_file_path = 'video/SampleVideo_1280x720_1mb.mp4'
logo_file_path = "img/logo-Cyy6uKYt.png"

def my_generator():
    i = 0
    while i < 5:
        i += 1  
        yield f'Data point {i}: {random.randint(1, 100),}'
    

# Define a stream for a language learning model
# This is a simplified example, in a real-world scenario, you would use a proper LLM
def my_llm_stream(prompt):
    for word in prompt.split():
        yield word

with open('data/display.yaml', 'r') as file:
    elements = yaml.safe_load(file)

for element in elements:
    if element['label'] == 'DataFrame Function':
        element['data'] = df
    elif element['label'] == 'Altair Chart':
        element['data'] = chart
    elif element['label'] == 'Matplotlib Figure':
        element['data'] = fig
    elif element['label'] == 'Vega-Lite Chart':
        element['data'] = spec

def display_page():
    st.title("Streamlit Display Function Guide")
    st.markdown("This page demonstrates various Streamlit display functions. Each function is explained and has a code snippet that you can use in your own apps.")

    category = st.selectbox("Filter by Category", ["All", "Text", "Data", "Media", "Charts", "Layout"])

    global_vars = {
        "df": df,
        "df2": df2,
        "coordonates": coordonates,
        "chart": chart,
        "fig": fig,
        "spec": spec,
        "image_file_path": image_file_path,
        "audio_file_path": audio_file_path,
        "video_file_path": video_file_path,
        "logo_file_path": logo_file_path,
        "my_generator": my_generator,
        "my_llm_stream": my_llm_stream,
        "st": st,
        "plt": plt,
        "alt": alt,
    }

    if category == "All":
        full_display(elements, global_vars)
    else:
        filtered_elements = [e for e in elements if e['category'] == category]
        full_display(filtered_elements, global_vars) 

if __name__ == "__main__":
    display_page()