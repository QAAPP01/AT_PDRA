"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
"""


class PageFactory:
    """ PageFactory uses the factory design pattern.  """
    @staticmethod
    def get_page_object(page_name, driver):
        # Return the appropriate page object based on page_name
        page_obj = None
        page_name = page_name.lower()
        if page_name == "main_page":
            from .main_page import MainPage
            page_obj = MainPage(driver)
        elif page_name == "import_media":
            from .import_media import MediaPage
            page_obj = MediaPage(driver)
        elif page_name == "effect":
            from .effect import EffectPage
            page_obj = EffectPage(driver)
        elif page_name == "edit":
            from .edit import EditPage
            page_obj = EditPage(driver)
        elif page_name == "timeline_settings":
            from .timeline_settings import TimelineSettingsPage
            page_obj = TimelineSettingsPage(driver)
        elif page_name == "produce":
            from .produce import ProducePage
            page_obj = ProducePage(driver)
        elif page_name == "ai_effect":
            from .ai_effect import AIEffect
            page_obj = AIEffect(driver)
        return page_obj