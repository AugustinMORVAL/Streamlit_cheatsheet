import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import time 
import random
from utils.tutorial_display import full_display

# Define a simple DataFrame for demonstration
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

# Define a simple Altair chart
chart = alt.Chart(df).mark_circle().encode(
    x='lat', y='lon', color='lon', tooltip=['lat', 'lon']
)

# Define a simple Matplotlib figure
fig, ax = plt.subplots()
ax.plot(df['lat'], df['lon'])

# Define a simple Vega-Lite chart specification
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

elements_text = [
    {
        "label": "Display text",
        "code_snippet": "st.write('Most objects') # df, err, func, keras!",
        "explanation": "This code displays text using Streamlit's write function."
    },
    {
        "label": "Display list",
        "code_snippet": "st.write(['st', 'is <', 3]) # see *",
        "explanation": "This code displays a list using Streamlit's write function."
    },
    {
        "label": "Display stream",
        "code_snippet": "st.write_stream(data)",
        "explanation": "This code displays a stream of data using Streamlit's write_stream function.",
        "data" : my_generator(),
        "alt" : "st.write(my_generator())"
    },
    {
        "label": "Display fixed width text",
        "code_snippet": "st.text('Fixed width text')",
        "explanation": "This code displays fixed width text using Streamlit's text function."
    },
    {
        "label": "Display markdown",
        "code_snippet": "st.markdown('_Markdown_') # see *",
        "explanation": "This code displays markdown text using Streamlit's markdown function."
    },
    {
        "label": "Display latex",
        "code_snippet": "st.latex(r''' e^{i\pi} + 1 = 0 ''')",
        "explanation": "This code displays latex text using Streamlit's latex function."
    },
    {
        "label": "Display title",
        "code_snippet": "st.title('My title')",
        "explanation": "This code displays a title using Streamlit's title function."
    },
    {
        "label": "Display header",
        "code_snippet": "st.header('My header')",
        "explanation": "This code displays a header using Streamlit's header function."
    },
    {
        "label": "Display subheader",
        "code_snippet": "st.subheader('My sub')",
        "explanation": "This code displays a subheader using Streamlit's subheader function."
    },
    {
        "label": "Display code",
        "code_snippet": "st.code('for i in range(8): foo()')",
        "explanation": "This code displays code using Streamlit's code function."
    },
    {
        "label": "Display html",
        "code_snippet": "st.html('<p>Hi!</p>')",
        "explanation": "This code displays html using Streamlit's html function."
    }
]

elements_data = [
    {
        "label": "DataFrame Function",
        "code_snippet": "st.dataframe(data)",
        "explanation": "Displays a DataFrame as an interactive table.",
        "data": df,
        "alt": "st.dataframe(df)",
    },
    {
        "label": "Table Function",
        "code_snippet": "st.table(data)",
        "explanation": "Displays a static table.",
        "data": df,
        "alt": "st.table(df)",
    },
    {
        "label": "JSON Function",
        "code_snippet": "st.json({'foo':'bar','fu':'ba'})",
        "explanation": "Displays JSON data.",
    },
    {
        "label": "Metric Function",
        "code_snippet": "st.metric('My metric', 42, 2)",
        "explanation": "Displays a metric in a big bold font with an optional indicator of how the metric is doing.",
    }
]
elements_media = [
    {
        "label": "Image",
        "code_snippet": "st.image(data)",
        "explanation": "Displays an image.",
        "data": image_file_path,
        "alt": "st.image(image_file_path)",
    },
    {
        "label": "Audio",
        "code_snippet": "st.audio(data)",
        "explanation": "Displays an audio file.",
        "data": audio_file_path,
        "alt" : "st.audio(audio_file_path)",
    },
    {
        "label": "Video",
        "code_snippet": "st.video(data)",
        "explanation": "Displays a video file.",
        "data": video_file_path,
        "alt" : "st.video(video_file_path)",
    },
    {
        "label": "Logo",
        "code_snippet": 'st.logo(data)',
        "explanation": "Displays a logo.",
        "data": logo_file_path,
        "alt" : 'st.logo(logo_file_path)',
    }
]

elements_charts = [
    {
        "label": "Area Chart",
        "code_snippet": "st.area_chart(data)",
        "explanation": "Displays an area chart.",
        "data": df,
        "alt": "st.area_chart(df)",
    },
    {
        "label": "Bar Chart",
        "code_snippet": "st.bar_chart(data)",
        "explanation": "Displays a bar chart.",
        "data": df,
        "alt": "st.bar_chart(df)",
    },
    {
        "label": "Horizontal Bar Chart",
        "code_snippet": "st.bar_chart(data, horizontal=True)",
        "explanation": "Displays a horizontal bar chart.",
        "data": df,
        "alt": "st.bar_chart(df, horizontal=True)",
    },
    {
        "label": "Line Chart",
        "code_snippet": "st.line_chart(data)",
        "explanation": "Displays a line chart.",
        "data": df,
        "alt": "st.line_chart(df)",
    },
    {
        "label": "Map",
        "code_snippet": "st.map(data)",
        "explanation": "Displays a map.",
        "data": coordonates,
        "alt": "st.map(df)",
    },
    {
        "label": "Scatter Chart",
        "code_snippet": "st.scatter_chart(data)",
        "explanation": "Displays a scatter chart.",
        "data": df,
        "alt": "st.scatter_chart(df)",
    },
    {
        "label": "Altair Chart",
        "code_snippet": "st.altair_chart(data)",
        "explanation": "Displays an Altair chart.",
        "data": chart,
        "alt": "st.altair_chart(fig)",
    },
    {
        "label": "Bokeh Figure",
        "code_snippet": "st.bokeh_chart(data)",
        "explanation": "Displays an Bokkeh figure.",
        "data": fig,
        "alt": "st.bokeh_chart(fig)",
    },
    {
        "label": "Gaphviz Chart",
        "code_snippet": "st.graphviz_chart(data)",
        "explanation": "Displays an Bokkeh figure.",
        "data": fig,
        "alt": "st.graphviz_chart(fig)",
    },
    {
        "label": "Plotly Chart",
        "code_snippet": "st.plotly_chart(data)",
        "explanation": "Displays an matplotlib.pyplot figure.",
        "data": fig,
        "alt": "st.plotly_chart(fig)",
    },
    {
        "label": "Pydeck Chart",
        "code_snippet": "st.pydeck_chart(data)",
        "explanation": "Displays a Pydeck chart.",
        "data": chart,
        "alt": "st.pydeck_chart(chart)",
    },
    {
        "label": "Pyplot Figure",
        "code_snippet": "st.pyplot(data)",
        "explanation": "Displays a matplotlib.pyplot figure.",
        "data": fig,
        "alt": "st.pyplot(fig)",
    },
    {
        "label": "Vega Lite Chart",
        "code_snippet": "st.vega_lite_chart(data)",
        "explanation": "Displays a Vega Lite chart.",
        "data": [df, spec],
        "alt": "st.vega_lite_chart(df, spec)",
    },
    {
        "label": "Handle user interaction",
        "code_snippet": '# Work with user selections\nevent = st.plotly_chart(\n df,\n   on_select="rerun"\n)\nevent = st.altair_chart(\n    chart,\n    on_select="rerun"\n)\nevent = st.vega_lite_chart(\n df,\    spec,\n on_select="rerun"\n)',
        "explanation": "", 
        "data": "", 
        "alt": '# Work with user selections\nevent = st.plotly_chart(\n df,\n   on_select="rerun"\n)\nevent = st.altair_chart(\n    chart,\n    on_select="rerun"\n)\nevent = st.vega_lite_chart(\n df,\    spec,\n on_select="rerun"\n)',
    }
]


elements_column = [
    {
        "label": "Two equal columns",
        "code_snippet": "col1, col2 = st.columns(2)\ncol1.write('This is column 1')\ncol2.write('This is column 2')",
        "explanation": "This code creates two equal columns in Streamlit."
    },
    {
        "label": "Three different columns",
        "code_snippet":  "col3, col4, col5 = st.columns([3, 1, 1])\ncol3.write('This is column 1')\ncol4.write('This is column 2')\ncol5.write('This is column 3')",
        "explanation": "This code creates three different columns in Streamlit."
    },
]

elements_tab = [
    {
        "label": "Tabs",
        "code_snippet": "tab1, tab2 = st.tabs(['Tab 1', 'Tab2'])\ntab1.write('this is tab 1')\ntab2.write('this is tab 2')",
        "explanation": "This code creates two tabs in Streamlit."
    },
]

elements_expander = [
    {
        "label": "Expandable containers",
        "code_snippet": "expand = st.expander('My label', icon=':material/info:')\nexpand.write('Inside the expander.')\npop = st.popover('Button label')\npop.checkbox('Show all')\n\n# You can also use 'with' notation:\nwith expand:\n    st.radio('Select one:', [1, 2])",
        "explanation": "This code creates an expandable container in Streamlit."
    }
]

def display_page():
    st.subheader("Streamlit Display Function Guide")

    # Create a sidebar for filtering options
    category = st.selectbox("Filter by Category", ["Text", "Data", "Media", "Charts", "More Layout"])

    if category == "Text":
        st.title("Display text")
        full_display(elements_text)

    elif category == "Data":
        st.title("Display data")
        full_display(elements_data)

    elif category == "Media":
        st.title("Display media")
        full_display(elements_media)
        

    elif category == "Charts":
        st.title("Display charts")
        full_display(elements_charts)

        
    elif category == "More Layout":
        st.title("Columns")
        full_display(elements_column)
        st.title("Tab")
        full_display(elements_tab)
        st.title("Expander and Popover")
        full_display(elements_expander)