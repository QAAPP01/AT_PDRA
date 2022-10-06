"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
"""

from .main_page import MainPage
from .import_media import MediaPage
from .effect import EffectPage
from .edit import EditPage
from .timeline_settings import TimelineSettingsPage
from .produce import ProducePage

class PageFactory():
    """ PageFactory uses the factory design pattern.  """
    @staticmethod
    def get_page_object(page_name, driver):
        # Return the appropriate page object based on page_name
        page_obj = None
        page_name = page_name.lower()
        if page_name == "main_page":
            page_obj = MainPage(driver)
        elif page_name == "import_media":
            page_obj = MediaPage(driver)
        elif page_name == "effect":
            page_obj = EffectPage(driver)
        elif page_name == "edit":
            page_obj = EditPage(driver)
        elif page_name == "timeline_settings":
            page_obj = TimelineSettingsPage(driver)
        elif page_name == "produce":
            page_obj = ProducePage(driver)
        return page_obj