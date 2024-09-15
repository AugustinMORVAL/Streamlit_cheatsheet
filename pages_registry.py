def get_pages():
    from pages.Home import main_page
    from pages.Installation import installation_page
    from pages.Widgets import widget_page
    from pages.Display import display_page
    from pages.Placeholder import placeholder_page
    from pages.ChatBot import chatbot_page

    return {
        "Home": main_page,
        "Installation": installation_page,
        "Button Widgets": widget_page,
        "Display": display_page,
        "Placeholder & Help": placeholder_page,
        "Build a ChatBot": chatbot_page,
    }
