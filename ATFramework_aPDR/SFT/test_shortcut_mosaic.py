import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


@allure.epic("Shortcut")
@allure.feature("Mosaic")
class Test_Shortcut_Mosaic:
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
    def shared_data(self):
        data = {}
        yield data

    @allure.story("Entry")
    @allure.title("From shortcut")
    def test_entry_demo_page(self, driver):
        try:
            self.page_main.enter_launcher()

            self.page_main.enter_shortcut('Mosaic')

            assert self.element(L.main.shortcut.demo_title).text == 'Mosaic'

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Mosaic')

            pytest.fail(f"{str(e)}")

    @allure.story("Entry")
    @allure.title("Back from demo")
    def test_back_from_demo(self, driver):
        try:
            assert self.page_shortcut.back_from_demo()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()

    @allure.story("Media")
    @allure.title("Enter Media Picker")
    def test_entry_media_picker(self, driver):
        try:
            assert self.page_shortcut.enter_media_picker('Mosaic')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_media_picker('Mosaic')

    @allure.story("Media")
    @allure.title("Back from media picker")
    def test_back_from_media_picker(self, driver):
        try:
            assert self.page_shortcut.back_from_media_picker()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()

    @allure.story("Media")
    @allure.title("Enter trim before edit")
    def test_entry_trim_before_edit(self, driver):
        try:
            assert self.page_shortcut.enter_trim_before_edit('Mosaic')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_trim_before_edit('Mosaic')

    @allure.story("Media")
    @allure.title("Back from trim before edit")
    def test_back_from_trim_before_edit(self, driver):
        try:
            assert self.page_shortcut.back_from_trim()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_media_picker('Mosaic')

    @allure.story("Media")
    @allure.title("Trim video and edit")
    def test_trim_and_edit(self, driver):
        try:
            assert self.page_shortcut.trim_and_edit()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_editor('Mosaic')

    @allure.story("Media")
    @allure.title("Back from editor")
    def test_back_from_editor(self, driver):
        try:
            assert self.page_shortcut.back_from_editor()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_media_picker('Mosaic')

    @allure.story("Media")
    @allure.title("Enter editor")
    def test_enter_editor(self, driver):
        try:
            assert self.page_shortcut.enter_editor()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_editor('Mosaic')

    @allure.story("Editor")
    @allure.title("Export")
    def test_export(self):
        try:
            assert self.page_shortcut.export()

        except Exception:
            traceback.print_exc()