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


@allure.epic("Shortcut - Video Effect")
class Test_Shortcut_Video_Effect:
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
    def test_enter_media_picker(self, data):
        try:
            assert self.page_shortcut.enter_media_picker('Video Effect')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Back")
    @allure.title("From media picker")
    def test_back_from_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Video Effect')

            assert self.page_shortcut.back_from_media_picker()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Enter Trim")
    def test_video_entry_trim(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_trim_before_edit('Video Effect')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Back from trim")
    def test_video_back_from_trim(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_trim_before_edit('Video Effect')

            assert self.page_shortcut.back_from_trim()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Trim and import")
    def test_video_trim_and_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Video Effect')

            assert self.page_shortcut.trim_and_import()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Back from editor")
    def test_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Import video")
    def test_entry_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Video Effect')

            assert self.page_shortcut.enter_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview play")
    def test_video_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.preview_play()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise
        
    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview pause")
    def test_video_pause_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.preview_pause()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview beginning")
    def test_video_preview_beginning(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.preview_beginning()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview ending")
    def test_video_preview_ending(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.preview_ending()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Video")
    @allure.title("Back from export")
    def test_video_back_from_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.export_back()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Video")
    @allure.title("Produce Save")
    def test_video_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.export()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Produced")
    @allure.title("Back to editor")
    def test_export_back_to_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')
                self.page_shortcut.export()

            assert self.page_shortcut.export_back_to_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Import photo")
    def test_photo_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Video Effect')

            self.page_shortcut.back_from_editor()

            assert self.page_shortcut.enter_editor(media_type='photo', file=photo_9_16)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Back from editor")
    def test_photo_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect')

            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview play")
    def test_photo_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Video Effect')

            self.page_shortcut.enter_editor(media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_play()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview pause")
    def test_photo_pause_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_pause()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview beginning")
    def test_photo_preview_beginning(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_beginning()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview ending")
    def test_photo_preview_ending(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_ending()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Photo")
    @allure.title("Back from export")
    def test_photo_back_from_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.export_back()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Photo")
    @allure.title("Produce save")
    def test_photo_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.export()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Produced")
    @allure.title("Back to launcher")
    def test_export_back_to_launcher(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Video Effect', media_type='photo', file=photo_9_16)
                self.page_shortcut.export()

            assert self.page_shortcut.export_back_to_launcher()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise
