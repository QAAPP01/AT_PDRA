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
@allure.feature("AI Art")
class Test_Shortcut_AI_Art:
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
    @allure.title("From shortcut")
    def test_entry_from_shortcut(self, driver):
        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Art')

            assert self.is_exist(find_string('AI Art'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_ai_feature('AI Art')
            raise

    @allure.story("Entry")
    @allure.title("Back to launcher")
    def test_back_to_launcher(self, driver):
        try:
            self.click(L.main.shortcut.demo_back)

            assert self.is_exist(L.main.shortcut.shortcut_name(0))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            raise

    @allure.story("Entry")
    @allure.title("From AI creation")
    def test_entry_from_ai_creation(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')

            assert self.is_exist(find_string('AI Art'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
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
    @allure.title("Enter media picker")
    def test_enter_media_picker(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)

            assert self.is_exist(find_string('Add Media'))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
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
            self.page_main.enter_ai_feature('AI Art')
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
            self.page_main.enter_ai_feature('AI Art')
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
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            raise

    @allure.story("Editor")
    @allure.title("Enter prompt")
    def test_enter_prompt(self, driver):
        try:
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            self.click(find_string('Custom'))
            self.element(L.main.shortcut.ai_art.prompt).send_keys('Apple')
            text = self.element(L.main.shortcut.ai_art.prompt).text

            assert text == 'Apple'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            self.click(find_string('Custom'))
            self.element(L.main.shortcut.ai_art.prompt).send_keys('Apple')
            raise

    @allure.story("Editor")
    @allure.title("Clear prompt")
    def test_clear_prompt(self, driver):
        try:
            self.click(L.main.shortcut.ai_art.clear)
            text = self.element(L.main.shortcut.ai_art.prompt).text

            assert 'Please provide a description' in text

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            self.click(find_string('Custom'))
            raise

    @allure.story("Editor")
    @allure.title("Gen custom")
    def test_gen_custom(self, driver):
        try:
            self.element(L.main.shortcut.ai_art.prompt).send_keys('Apple')

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.apply)
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

            preview = self.page_edit.get_preview_pic()
            assert HCompareImg(preview).is_not_black()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            raise

    @allure.story("Editor")
    @allure.title("Gen style")
    def test_paid_style(self, driver):
        try:
            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name())
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

            preview = self.page_edit.get_preview_pic()
            assert HCompareImg(preview).is_not_black()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            raise



