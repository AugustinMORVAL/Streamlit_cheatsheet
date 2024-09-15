import streamlit as st
from pages_registry import pages

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

    st.markdown("### What you can find here:")

    col1, col2 = st.columns(2)

    for i, (page_name, page_function) in enumerate(pages.items()):
        if page_name != "Home":
            with col1 if i % 2 == 0 else col2:
                st.subheader(page_name)
                st.write(f"Learn about {page_name.lower()} in Streamlit.")
                if st.button(f"Go to {page_name} Tutorial"):
                    st.switch_page(f"pages/{i:02d}_{page_name.replace(' ', '_')}.py")

    # visual separation
    st.markdown("---")

if __name__ == "__main__":
    main_page()