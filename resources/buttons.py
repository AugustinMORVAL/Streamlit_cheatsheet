import streamlit as st
import pandas as pd
from utils.tutorial_display import full_display

data = pd.DataFrame({
'col1': [1, 2, 3, 4],
'col2': [10, 20, 30, 40]
})

url = "https://www.example.com"

widgets = [
    ('Classic Button', 'button', "Click me", "A simple button that does nothing when clicked."),
    ('Download Button', 'download_button', "Download file", "text.txt", "A button that allows users to download a file when clicked."),
    ('Link Button', 'link_button', "Go to gallery", url, "A button that links to a specified URL when clicked."),
    ('Data Editor', 'data_editor', data, "A data editor that allows users to edit data in a table format."),
    ('Checkbox', 'checkbox', "I agree", "A checkbox that allows users to select or deselect an option."),
    ('Toggle', 'toggle', "Enable", "A toggle switch that allows users to switch between two states."),
    ('Radio', 'radio', "Pick one", ["cats", "dogs"], "A radio button group that allows users to select one option from a list."),
    ('Selectbox', 'selectbox', "Pick one", ["cats", "dogs"], "A select box that allows users to select one option from a dropdown list."),
    ('Multiselect', 'multiselect', "Buy", ["milk", "apples", "potatoes"], "A multiselect box that allows users to select multiple options from a list."),
    ('Slider', 'slider', "Pick a number", 0, 100, "A slider that allows users to select a value within a specified range."),
    ('Select Slider', 'select_slider', "Pick a size", ["S", "M", "L"], "A select slider that allows users to select a value from a list of options."),
    ('Text Input', 'text_input', "First name", "A text input field that allows users to enter text."),
    ('Number Input', 'number_input', "Pick a number", 0, 10, "A number input field that allows users to enter a number within a specified range."),
    ('Text Area', 'text_area', "Text to translate", "A text area that allows users to enter multiple lines of text."),
    ('Date Input', 'date_input', "Your birthday", "A date input field that allows users to select a date."),
    ('Time Input', 'time_input', "Meeting time", "A time input field that allows users to select a time."),
    ('File Uploader', 'file_uploader', "Upload a CSV", "A file uploader that allows users to upload a file."),
    ('Camera Input', 'camera_input', "Take a picture", "A camera input that allows users to take a picture using their webcam."),
    ('Color Picker', 'color_picker', "Pick a color", "A color picker that allows users to select a color."),
    # ('Slider with Min/Max Value', 'slider', "Pick a number", 0, 100, value=50, "A slider with a default value."),
    # ('Slider with Step', 'slider', "Pick a number", 0, 100, step=5, "A slider with a specified step size."),
    # ('Slider with Format', 'slider', "Pick a number", 0, 100, format="%d%%", "A slider with a specified format for the displayed value."),
    ('Number Input with Variable', 'number_input', "Num:", "A number input field that returns a value that can be used in your code."),
]

def button_page():
    st.title("Streamlit Interactive Widgets")
    st.markdown("This page demonstrates all the Streamlit interactive widgets. Each widget is explained and has a code snippet that you can use in your own apps.")
 
    for i, (label, function, *args, explanation) in enumerate(widgets):
        full_display(f"{i+1}. {label}", function, *args, explanation=explanation)

