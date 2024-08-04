import streamlit as st  

def main_page():
    st.title("Welcome to Streamlit Cheatsheet")
    st.markdown("""
    Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. It's particularly well-suited for ML engineering and data science as it allows you to turn data scripts into shareable web apps in minutes.

    Streamlit is useful for several reasons:
    - **Ease of Use**: Streamlit allows you to turn your data scripts into a shareable web app with minimal effort.
    - **Interactive Data Visualization**: Streamlit supports a wide variety of interactive charts and plots.
    - **Real-Time Data**: Streamlit allows you to create real-time data apps.
    - **Deployment**: Streamlit apps can be easily deployed on a variety of platforms.
    - **Community and Resources**: Streamlit has a large and active community.
    - **Integration with Machine Learning Libraries**: Streamlit integrates seamlessly with popular machine learning libraries.
    """)

    st.write("Explore a variety of tutorials to enhance your Streamlit skills.")

    st.markdown("""
    ### What you can find here:
    """)

    # Using columns to create a more visually appealing layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Buttons")
        st.markdown("Learn how to use buttons in Streamlit.")
        if st.button("Go to Buttons Tutorial"):
            st.write("Redirecting to Buttons Tutorial...")

    with col2:
        st.subheader("Page 3")
        st.write("More tutorials coming soon!")
        if st.button("Coming Soon"):
            st.write("Stay tuned for more tutorials!")

    # visual separation
    st.markdown("""
    ---
    """)

    # Footer
    st.markdown("""
    <div style="text-align: center;">
    © 2024 Morval Tech. All rights reserved.
    </div>
    """, unsafe_allow_html=True)