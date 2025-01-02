import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.SFT.test_file import *


@allure.epic("Shortcut - AI Anime Video")
class Test_Shortcut_AI_Anime_Video:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @pytest.fixture(scope="module")
    def data(self):
        data = {'last_result': True}
        yield data

    def last_is_fail(self, data):
        if not data['last_result']:
            data['last_result'] = True
            self.page_main.relaunch()
            return True
        return False

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Enter from Shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            assert self.page_shortcut.enter_shortcut('AI Anime Video')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Back to Shortcut")
    def test_back_to_shortcut(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Anime Video')

            assert self.page_shortcut.back_from_demo()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Enter from AI creation")
    def test_entry_from_ai_creation(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_ai_feature('AI Anime Video')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Back to AI creation")
    def test_back_to_ai_creation(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_ai_feature('AI Anime Video')

            assert self.page_shortcut.back_from_demo()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

