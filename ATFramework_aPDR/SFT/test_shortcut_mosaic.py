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
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

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
    @allure.title("Enter Demo page")
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
    @allure.title("Enter Media Picker")
    def test_entry_media_picker(self, driver):
        try:
            self.click(L.main.shortcut.try_it_now)

            assert self.is_exist(find_string('Add Media'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Mosaic')
            self.click(L.main.shortcut.try_it_now)

            pytest.fail(f"{str(e)}")

    @allure.story("Entry")
    @allure.title("Enter Editor")
    def test_entry_editor(self, driver):
        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_edit.waiting()

            assert self.is_exist(L.main.shortcut.export)

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Mosaic')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_edit.waiting()

            pytest.fail(f"{str(e)}")

    @allure.story("Entry")
    @allure.title("Export")
    def test_entry_export(self, driver):
        try:
            self.click(L.main.shortcut.export)
            self.click(L.main.shortcut.produce)
            self.page_edit.waiting_produce()

            assert self.is_exist(L.main.shortcut.save_to_camera_roll)

        except Exception as e:
            traceback.print_exc()

            pytest.fail(f"{str(e)}")
