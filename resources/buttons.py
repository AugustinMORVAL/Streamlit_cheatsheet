import streamlit as st
import pandas as pd
from utils.tutorial_display import full_display

def button_page():
    st.title("Streamlit Button Widgets")
    st.markdown("This page demonstrates all the Streamlit button widgets. Each widget is explained and has a code snippet that you can use in your own apps.")

    data = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
    })

    url = "https://www.example.com"

    widgets = [
        ('Classique Button', 'st.button("Click me")', "A simple button that does nothing when clicked."),
        ('Download Button', 'st.download_button("Download file", data.to_csv(), "data.csv")', "A button that allows users to download a file when clicked."),
        ('Link Button', 'st.link_button("Go to gallery", url)', "A button that links to a specified URL when clicked."),
        ('Data Editor', 'st.data_editor(data)', "A data editor that allows users to edit data in a table format."),
        ('Checkbox', 'st.checkbox("I agree")', "A checkbox that allows users to select or deselect an option."),
        ('Toggle', 'st.toggle("Enable")', "A toggle switch that allows users to switch between two states."),
        ('Radio', 'st.radio("Pick one", ["cats", "dogs"])', "A radio button group that allows users to select one option from a list."),
        ('Selectbox', 'st.selectbox("Pick one", ["cats", "dogs"])', "A select box that allows users to select one option from a dropdown list."),
        ('Multiselect', 'st.multiselect("Buy", ["milk", "apples", "potatoes"])', "A multiselect box that allows users to select multiple options from a list."),
        ('Slider', 'st.slider("Pick a number", 0, 100)', "A slider that allows users to select a value within a specified range."),
        ('Select Slider', 'st.select_slider("Pick a size", ["S", "M", "L"])', "A select slider that allows users to select a value from a list of options."),
        ('Text Input', 'st.text_input("First name")', "A text input field that allows users to enter text."),
        ('Number Input', 'st.number_input("Pick a number", 0, 10)', "A number input field that allows users to enter a number within a specified range."),
        ('Text Area', 'st.text_area("Text to translate")', "A text area that allows users to enter multiple lines of text."),
        ('Date Input', 'st.date_input("Your birthday")', "A date input field that allows users to select a date."),
        ('Time Input', 'st.time_input("Meeting time")', "A time input field that allows users to select a time."),
        ('File Uploader', 'st.file_uploader("Upload a CSV")', "A file uploader that allows users to upload a file."),
        ('Camera Input', 'st.camera_input("Take a picture")', "A camera input that allows users to take a picture using their webcam."),
        ('Color Picker', 'st.color_picker("Pick a color")', "A color picker that allows users to select a color."),
        ('Slider with Min/Max Value', 'st.slider("Pick a number", 0, 100, value=50)', "A slider with a default value."),
        ('Slider with Step', 'st.slider("Pick a number", 0, 100, step=5)', "A slider with a specified step size."),
        ('Slider with Format', 'st.slider("Pick a number", 0, 100, format="%d%%")', "A slider with a specified format for the displayed value."),
        ('Number Input with Variable', 'int(st.number_input("Num:"))', "A number input field that returns a value that can be used in your code."),
        ]

    for i, (label, code, explanation) in enumerate(widgets):
        full_display(f"{i+1}. {label}", code, explanation)

