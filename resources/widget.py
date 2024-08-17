import streamlit as st
import pandas as pd
from utils.tutorial_display import full_display

data = pd.DataFrame({
'col1': [1, 2, 3, 4],
'col2': [10, 20, 30, 40]
})

url = "https://www.example.com"

widgets = [
    {
    "label": 'Classic Button',
    "code_snippet": 'st.button("Click me")',
    "explanation": "A simple button that does nothing when clicked."
    },
    {
    "label": 'Download Button',
    "code_snippet": 'st.download_button("Download file", "Hello")',
    "explanation": "A button that allows users to download a file when clicked.",
    },
    {
    "label": 'Feedback',
    "code_snippet": 'st.feedback("thumbs")',
    "explanation": "",
    },
    {
    "label": 'Link Button',
    "code_snippet": 'st.link_button("Go to gallery", data)',
    "explanation": "A button that links to a specified URL when clicked.",
    "data": url,
    "alt": 'st.link_button("Go to gallery", url)',
    },
    {
    "label": 'Page Link',
    "code_snippet": 'st.page_link("app.py", label="Home")',
    "explanation": "",
    },
    {
    "label": 'Data Editor',
    "code_snippet": 'st.data_editor(data)',
    "explanation": "A data editor that allows users to edit data in a table format.",
    "data": data,
    },
    {
    "label": 'Checkbox',
    "code_snippet": 'st.checkbox("I agree")',
    "explanation": "A checkbox that allows users to select or deselect an option.",
    },
    {
    "label": 'Toggle',
    "code_snippet": 'st.toggle("Enable")',
    "explanation": "A toggle switch that allows users to switch between two states.",
    },
    {
    "label": 'Radio',
    "code_snippet": 'st.radio("Pick one", ["cats", "dogs"])',
    "explanation": "A radio button group that allows users to select one option from a list.",
    },
    {
    "label": 'Select Box',
    "code_snippet": 'st.selectbox("Pick one", ["cats", "dogs"])',
    "explanation": "A select box that allows users to select one option from a dropdown list.",
    },
    {
    "label": 'Multiselect Box',
    "code_snippet": 'st.multiselect("Buy", ["milk", "apples", "potatoes"])',
    "explanation": "A select box that allows users to select multiple options from a list.",
    },
    {
    "label": 'Slider',
    "code_snippet": 'st.slider("Pick a number", 0, 100)',
    "explanation": "A slider that allows users to select a value within a specified range.",
    },
    {
    "label": 'Slider with Default Value',
    "code_snippet": 'st.slider("Pick a number", 0, 100, value=50)',
    "explanation": "A slider with a default value.",
    },
    {
    "label": 'Slider with Steps',
    "code_snippet": 'st.slider("Pick a number", 0, 100, step=5)',
    "explanation": "A slider with a specified step size.",
    },
    {
    "label": 'Slider with Format',
    "code_snippet": 'st.slider("Pick a number", 0, 100, format="%d%%")',
    "explanation": "A slider with a specified format for the displayed value.",
    },
    {
    "label": 'Select Slider',
    "code_snippet": 'st.select_slider("Pick a size", ["S", "M", "L"])',
    "explanation": "A select slider that allows users to select a value from a list of options.",
    },
    {
    "label": 'Text Input Field',
    "code_snippet": 'st.text_input("First name")',
    "explanation": "A text input field that allows users to enter text.",
    },
    {
    "label": 'Number Input',
    "code_snippet": 'st.number_input("Num:")',
    "explanation": "A number input field that returns a value that can be used in your code.",
    },
    {
    "label": 'Number Input wiht Range',
    "code_snippet": 'st.number_input("Pick a number", 0, 10)',
    "explanation": "A number input field that allows users to enter a number within a specified range.",
    },
    {
    "label": 'Text Area',
    "code_snippet": 'st.text_area("Text to translate")',
    "explanation": "A text area that allows users to enter multiple lines of text.",
    },
    {
    "label": 'Date Input',
    "code_snippet": 'st.date_input("Your birthday")',
    "explanation": "A date input field that allows users to select a date.",
    },
    {
    "label": 'Time Input',
    "code_snippet": 'st.time_input("Meeting time")',
    "explanation": "A time input field that allows users to select a time.",
    },
    {
    "label": 'File Uploader',
    "code_snippet": 'st.file_uploader("Upload a CSV")',
    "explanation": "A file uploader that allows users to upload a file.",
    },
    {
    "label": 'Camera Input',
    "code_snippet": 'st.camera_input("Take a picture")',
    "explanation": "A camera input that allows users to take a picture using their webcam.",
    },
    {
    "label": 'Color Picker',
    "code_snippet": 'st.color_picker("Pick a color")',
    "explanation": "A color picker that allows users to select a color.",
    },
    {
    "label": 'Disabled Widget',
    "code_snippet": 'st.slider("Pick a number", 0, 100, disabled=True, key="Disabled Widget")',
    "explanation": "Disable widgets to remove interactivity",
    "alt": 'st.slider("Pick a number", 0, 100, disabled=True)',
    },
]

def widget_page():
    st.title("Streamlit Interactive Widgets")
    st.markdown("This page demonstrates all the Streamlit interactive widgets. Each widget is explained and has a code snippet that you can use in your own apps.")
    full_display(widgets)
