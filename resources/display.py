import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# Define a simple DataFrame for demonstration
df = pd.DataFrame(
   np.random.randn(10, 2),
   columns=['a', 'b']
)

# Define a simple Altair chart
chart = alt.Chart(df).mark_circle().encode(
    x='a', y='b', color='b', tooltip=['a', 'b']
)

# Define a simple Matplotlib figure
fig, ax = plt.subplots()
ax.plot(df['a'], df['b'])

# Define a simple Vega-Lite chart specification
spec = {
    "mark": "bar",
    "encoding": {
        "x": {"field": "a", "type": "ordinal"},
        "y": {"field": "b", "type": "quantitative"}
    }
}

# Define data for Media category
# You can replace 'your_media_file.mp3' with the path to your audio file
audio_file_path = 'audio-test/meeting-clip1.mp3'
video_file_path = 'streamlit/video/SampleVideo_1280x720_1mb.mp4'  # Replace with your video file path

# Define a generator function
def my_generator():
    for i in range(5):
        yield f"Generating data: {i}"

# Define a stream for a language learning model
# This is a simplified example, in a real-world scenario, you would use a proper LLM
def my_llm_stream(prompt):
    for word in prompt.split():
        yield word

def display_element(label, code_snippet, explanation):
    st.subheader(label)
    col1, col2 = st.columns(2)
    with col1:
        eval(code_snippet)
    with col2:
        st.markdown(explanation)
        if st.toggle("Show code", key=label):
            st.code(code_snippet, language='python')

elements_text = [
    ('Write Function (Text)', 'st.write("Most objects")', "Displays text, data, charts, and more."),
    ('Write Function (List)', 'st.write(["st", "is <", 3])', "Displays a list of items."),
    ('Write Stream Function (Generator)', 'st.write_stream(my_generator)', "Writes output from a generator function to the app."),
    ('Write Stream Function (LLM Stream)', 'st.write_stream(my_llm_stream(st.text_input("Enter your prompt here:")))', "Writes output from a language learning model stream to the app."),
    ('Text Function', 'st.text("Fixed width text")', "Displays fixed width text."),
    ('Markdown Function', 'st.markdown("_Markdown_")', "Displays text with Markdown syntax."),
    ('Latex Function', 'st.latex(r""" e^{i\pi} + 1 = 0 """)', "Displays mathematical expressions using LaTeX syntax."),
    ('Title Function', 'st.title("My title")', "Displays a title."),
    ('Header Function', 'st.header("My header")', "Displays a header."),
    ('Subheader Function', 'st.subheader("My sub")', "Displays a subheader."),
    ('Code Function', 'st.code("for i in range(8): foo()")', "Displays a block of code."),
    ('HTML Function', 'st.html("<p>Hi!</p>")', "Displays HTML."),
]

elements_data = [
    ('DataFrame Function', 'st.dataframe(df)', "Displays a DataFrame as an interactive table."),
    ('Table Function', 'st.table(df)', "Displays a static table."),
    ('JSON Function', 'st.json({"foo":"bar","fu":"ba"})', "Displays JSON data."),
    ('Metric Function', 'st.metric("My metric", 42, 2)', "Displays a metric in a big bold font with an optional indicator of how the metric is doing."),
]

elements_media = [
    ('Image Function', 'st.image("img/streamlit-logo-primary-colormark-darktext.png")', "Displays an image."),
    ('Audio Function', 'st.audio(audio_file_path)', "Displays an audio file."),
    ('Video Function', 'st.video(video_file_path)', "Displays a video file."),
    ('Code Function', 'st.code(\'st.logo("img/logo-Cyy6uKYt.png")\')', "Displays a block of code."),
]

elements_charts = [
    ('Line Chart Function', 'st.line_chart(df)', "Displays a line chart."),
    ('Altair Chart Function', 'st.altair_chart(chart)', "Displays an Altair chart."),
    ('Pyplot Function', 'st.pyplot(fig)', "Displays a matplotlib.pyplot figure."),
    ('Vega-Lite Chart Function', 'st.vega_lite_chart(df, spec)', "Displays a Vega-Lite chart."),
]

def display_page():
    st.title("Streamlit Display Function Guide")

    # Create a sidebar for filtering options
    st.sidebar.header("Filter by Category")
    category = st.sidebar.radio("", ["Text", "Data", "Media", "Charts"])

    if category == "Text":
        for i, (label, code, explanation) in enumerate(elements_text):
            display_element(f"{i+1}. {label}", code, explanation)

    elif category == "Data":
        for i, (label, code, explanation) in enumerate(elements_data):
            display_element(f"{i+1}. {label}", code, explanation)

    elif category == "Media":
        for i, (label, code, explanation) in enumerate(elements_media):
            display_element(f"{i+1}. {label}", code, explanation)

    elif category == "Charts":
        for i, (label, code, explanation) in enumerate(elements_charts):
            display_element(f"{i+1}. {label}", code, explanation)
