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


@allure.epic("Shortcut - Image Enhancer")
class Test_Shortcut_Image_Enhancer:
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

    @allure.feature("Media Picker")
    @allure.story("Enter")
    @allure.title("Enter media picker")
    def test_entry_media_picker(self, data):
        try:
            assert self.page_shortcut.enter_media_picker('Image Enhancer')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise
            
    @allure.feature("Media Picker")
    @allure.story("Back")
    @allure.title("From media picker")
    def test_back_from_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Image Enhancer')

            assert self.page_shortcut.back_from_media_picker()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Import photo")
    def test_photo_import(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_editor('Image Enhancer', media_type='photo', file=photo_9_16)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Back from editor")
    def test_photo_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Image Enhancer', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.back_from_shortcut_editor()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Photo")
    @allure.title("Save Image")
    def test_photo_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Image Enhancer')

            self.page_shortcut.enter_editor(media_type='photo', file=photo_9_16)
            assert self.page_shortcut.save_image()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Produced")
    @allure.title("Back to editor")
    def test_export_back_to_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Image Enhancer', media_type='photo', file=photo_9_16)
                self.page_shortcut.save_image()

            assert self.page_shortcut.export_back_to_editor()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Produced")
    @allure.title("Back to launcher")
    def test_export_back_to_launcher(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Image Enhancer', media_type='photo', file=photo_9_16)

            self.page_shortcut.save_image()

            assert self.page_shortcut.export_back_to_launcher()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise