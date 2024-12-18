import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


@allure.epic("Shortcut")
@allure.feature("AI Anime Video")
class Test_Shortcut_AI_Art:
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

    @allure.story("Entry")
    @allure.title("From shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            self.page_shortcut.enter_shortcut('AI Anime Video')

            assert self.element(L.main.shortcut.demo_title).text == 'AI Anime Video'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Entry")
    @allure.title("Back from demo")
    def test_back_from_demo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Anime Video')

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Entry")
    @allure.title("From AI creation")
    def test_entry_from_ai_creation(self, data):
        try:
            self.page_shortcut.enter_ai_feature('AI Anime Video')

            assert self.element(L.main.shortcut.demo_title).text == 'AI Anime Video'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Entry")
    @allure.title("Back to AI creation")
    def test_back_to_ai_creation(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_ai_feature('AI Anime Video')

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

