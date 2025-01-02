import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.SFT.test_file import *


@allure.epic("Shortcut - Tempo Effect")
class Test_Shortcut_Tempo_Effect:
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
            assert self.page_shortcut.enter_shortcut('Tempo Effect')

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
                self.page_shortcut.enter_shortcut('Tempo Effect', check=False)

            assert self.page_shortcut.back_from_demo()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise
        
    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Don't show again")
    def test_demo_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.demo_dont_show_again('Tempo Effect')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Reset don't show again")
    def test_reset_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Tempo Effect', check=False)

            assert self.page_shortcut.reset_dont_show_again('Tempo Effect')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Enter")
    @allure.title("Enter media picker")
    def test_enter_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Tempo Effect', check=False)

            assert self.page_shortcut.enter_media_picker()

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
                self.page_shortcut.enter_media_picker('Tempo Effect')

            assert self.page_shortcut.back_from_media_picker()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Enter Trim")
    def test_video_entry_trim(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_trim_before_edit('Tempo Effect')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Back from trim")
    def test_video_back_from_trim(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_trim_before_edit('Tempo Effect')

            assert self.page_shortcut.back_from_trim()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Trim and import")
    def test_video_trim_and_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Tempo Effect')

            assert self.page_shortcut.trim_and_import()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Back from editor")
    def test_video_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Tempo Effect')

            assert self.page_shortcut.back_from_editor()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Import video")
    def test_video_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Tempo Effect')

            assert self.page_shortcut.enter_editor()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview play")
    def test_video_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Tempo Effect')

            assert self.page_shortcut.preview_play()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise


    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview pause")
    def test_video_pause_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Tempo Effect')

            assert self.page_shortcut.preview_pause()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview beginning")
    def test_video_preview_beginning(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Tempo Effect')

            assert self.page_shortcut.preview_beginning()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview ending")
    def test_video_preview_ending(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Tempo Effect')

            assert self.page_shortcut.preview_ending()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Video")
    @allure.title("Back from export")
    def test_video_back_from_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Tempo Effect')

            assert self.page_shortcut.export_back()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Video")
    @allure.title("Produce Save")
    def test_video_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Tempo Effect')

            assert self.page_shortcut.export()

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
                self.page_shortcut.enter_editor('Tempo Effect')
                self.page_shortcut.export()

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
                self.page_shortcut.enter_editor('Tempo Effect')

            self.page_shortcut.export()

            assert self.page_shortcut.export_back_to_launcher()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise
        