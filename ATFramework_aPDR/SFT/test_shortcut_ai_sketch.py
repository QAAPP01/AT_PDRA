import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

photo_9_16 = 'photo_9_16.jpg'


@allure.epic("Shortcut")
@allure.feature("AI Sketch")
class Test_Shortcut_AI_Sketch:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.story("Entry")
    @allure.title("From AI creation")
    def test_entry_from_ai_creation(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')

            assert self.is_exist(find_string('AI Sketch'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            raise

    @allure.story("Entry")
    @allure.title("Back to AI creation")
    def test_back_to_ai_creation(self, driver):
        try:
            self.click(L.main.shortcut.demo_back)

            assert self.is_exist(find_string('AI Creation'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            raise

    @allure.story("Media Picker")
    @allure.title("Recommendation close")
    def test_recommendation_close(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.main.shortcut.ai_sketch.close)

            assert self.is_exist(find_string('AI Creation'))

        except Exception:
            traceback.print_exc()

            raise

    @allure.story("Media Picker")
    @allure.title("Recommendation continue")
    def test_recommendation_continue(self, driver):
        try:
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.main.shortcut.ai_sketch.continue_btn)

            assert self.is_exist(find_string('Add Media'))

        except Exception:
            traceback.print_exc()

            raise

    @allure.story("Media Picker")
    @allure.title("Recommendation dont show again")
    def test_recommendation_dont_show(self, driver):
        try:
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.main.shortcut.ai_sketch.dont_show_again)
            self.click(L.main.shortcut.ai_sketch.continue_btn)

            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)

            assert not self.is_exist(L.main.shortcut.ai_sketch.continue_btn)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            raise

    @allure.story("Media Picker")
    @allure.title("Back from media picker")
    def test_back_from_media(self, driver):
        try:
            self.click(L.import_media.media_library.back)

            assert self.is_exist(find_string('AI Creation'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            raise

    @allure.story("Media Picker")
    @allure.title("Import photo")
    def test_import_photo(self, driver):
        try:
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            assert self.is_exist(find_string('Export'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            raise

    @allure.story("Editor")
    @allure.title("Back to media picker")
    def test_back_to_media_picker(self, driver):
        try:
            self.click(L.main.shortcut.editor_back)

            assert self.is_exist(find_string('Add Media'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            raise

