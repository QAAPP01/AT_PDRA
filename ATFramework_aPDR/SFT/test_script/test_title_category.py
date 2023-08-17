import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))


class TestTitle:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist


    def test_case(self):
        try:
            categories = []
            locator = id("library_category_tab_text")
            displayed = self.elements(locator)
            last = displayed[-1].text

            while last not in categories:
                for i in displayed:
                    if i.text not in categories:
                        categories.append(i.text)
                self.page_main.h_swipe_element(displayed[-1], displayed[0], 4)
                displayed = self.elements(locator)
                last = displayed[-1].text

            print(categories)

        except Exception as err:
            logger(f'\n{err}')

