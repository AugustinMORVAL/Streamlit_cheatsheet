def get_pages():
    from lessons.Home import main_page
    from lessons.Installation import installation_page
    from lessons.Widgets import widget_page
    from lessons.Display import display_page
    from lessons.Placeholder import placeholder_page
    from lessons.ChatBot import chatbot_page


    return {
        "Home": main_page,
        "Installation": installation_page,
        "Button Widgets": widget_page,
        "Display": display_page,
        "Placeholder & Help": placeholder_page,
        "Build a ChatBot": chatbot_page,
    }
