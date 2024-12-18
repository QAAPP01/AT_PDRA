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


@allure.epic("Shortcut - AI Music")
class Test_Shortcut_AI_Music:
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
    @allure.title("Enter from AI creation")
    def test_entry_from_ai_creation(self, data):
        try:
            assert self.page_shortcut.enter_ai_feature('AI Music Generator')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Back to AI creation")
    def test_back_to_ai_creation(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_ai_feature('AI Music Generator', check=False)

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Enter from Shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            assert self.page_shortcut.enter_shortcut('AI Music Generator')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Back to Shortcut")
    def test_back_to_shortcut(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Music Generator', check=False)

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Don't show again")
    def test_demo_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.demo_dont_show_again('AI Music Generator')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    # @allure.feature("Entry")
    # @allure.story("Demo")
    # @allure.title("Reset don't show again")
    # def test_reset_dont_show_again(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_shortcut('AI Music Generator', check=False)
    #
    #         assert self.page_shortcut.reset_dont_show_again('AI Music Generator')
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise


    #
    # @allure.feature("Editor")
    # @allure.story("Video")
    # @allure.title("Preview play")
    # def test_video_play_preview(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             pass
    #
    #         assert self.page_shortcut.preview_play()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Editor")
    # @allure.story("Video")
    # @allure.title("Preview pause")
    # def test_video_pause_preview(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('AI Music Generator')
    #
    #         assert self.page_shortcut.preview_pause()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # # @allure.feature("Editor")
    # # @allure.story("Video")
    # # @allure.title("Preview beginning")
    # # def test_video_preview_beginning(self, data):
    # #     try:
    # #         if self.last_is_fail(data):
    # #             self.page_shortcut.enter_editor('Cutout')
    # #
    # #         assert self.page_shortcut.preview_beginning()
    # #
    # #     except Exception as e:
    # #         traceback.print_exc()
    # #         logger(e)
    # #         data['last_result'] = False
    # #         raise
    # #
    # # @allure.feature("Editor")
    # # @allure.story("Video")
    # # @allure.title("Preview ending")
    # # def test_video_preview_ending(self, data):
    # #     try:
    # #         if self.last_is_fail(data):
    # #             self.page_shortcut.enter_editor('Cutout')
    # #
    # #         assert self.page_shortcut.preview_ending()
    # #
    # #     except Exception as e:
    # #         traceback.print_exc()
    # #         logger(e)
    # #         data['last_result'] = False
    # #         raise
    #
    # # @allure.story("Editor")
    # # @allure.title("Add background photo")
    # # def test_add_background_photo(self,data):
    # #     try:
    # #         if self.last_is_fail(data):
    # #             self.page_shortcut.enter_editor('Cutout')
    # #
    # #         assert self.page_shortcut.add_background_photo(test_material_folder,photo_9_16)
    # #
    # #     except Exception as e:
    # #         traceback.print_exc()
    # #         logger(e)
    # #         data['last_result'] = False
    # #         raise
    # #
    # # @allure.story("Editor")
    # # @allure.title("Remove background")
    # # def test_remove_background(self,data):
    # #     try:
    # #         if self.last_is_fail(data):
    # #             self.page_shortcut.enter_editor('Cutout')
    # #
    # #         assert self.page_shortcut.remove_background()
    # #
    # #     except Exception as e:
    # #         traceback.print_exc()
    # #         logger(e)
    # #         data['last_result'] = False
    # #         raise
    #
    # @allure.feature("Export")
    # @allure.story("Video")
    # @allure.title("Back from export")
    # def test_video_back_from_export(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout')
    #
    #         assert self.page_shortcut.export_back()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Export")
    # @allure.story("Video")
    # @allure.title("Produce Save")
    # def test_video_export(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout')
    #
    #         assert self.page_shortcut.export()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Export")
    # @allure.story("Produced")
    # @allure.title("Back to editor")
    # def test_export_back_to_editor(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout')
    #             self.page_shortcut.export()
    #
    #         assert self.page_shortcut.export_back_to_editor()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Editor")
    # @allure.story("Photo")
    # @allure.title("Import photo")
    # def test_photo_import(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             pass
    #         else:
    #             self.page_shortcut.back_from_editor()
    #
    #         assert self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # # @allure.feature("Editor")
    # # @allure.story("Photo")
    # # @allure.title("Back from editor")
    # # def test_photo_back_from_editor(self, data):
    # #     try:
    # #         if self.last_is_fail(data):
    # #             self.page_shortcut.enter_editor('Cutout')
    # #
    # #         assert self.page_shortcut.back_from_editor()
    # #
    # #     except Exception as e:
    # #         traceback.print_exc()
    # #         logger(e)
    # #         data['last_result'] = False
    # #         raise
    #
    # @allure.feature("Editor")
    # @allure.story("Photo")
    # @allure.title("Preview play")
    # def test_photo_play_preview(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    #
    #         assert self.page_shortcut.preview_play()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Editor")
    # @allure.story("Photo")
    # @allure.title("Preview pause")
    # def test_photo_pause_preview(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    #
    #         assert self.page_shortcut.preview_pause()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # # @allure.feature("Editor")
    # # @allure.story("Photo")
    # # @allure.title("Preview beginning")
    # # def test_photo_preview_beginning(self, data):
    # #     try:
    # #         if self.last_is_fail(data):
    # #             self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    # #
    # #         assert self.page_shortcut.preview_beginning()
    # #
    # #     except Exception as e:
    # #         traceback.print_exc()
    # #         logger(e)
    # #         data['last_result'] = False
    # #         raise
    # #
    # # @allure.feature("Editor")
    # # @allure.story("Photo")
    # # @allure.title("Preview ending")
    # # def test_photo_preview_ending(self, data):
    # #     try:
    # #         if self.last_is_fail(data):
    # #             self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    # #
    # #         assert self.page_shortcut.preview_ending()
    # #
    # #     except Exception as e:
    # #         traceback.print_exc()
    # #         logger(e)
    # #         data['last_result'] = False
    # #         raise
    #
    # @allure.feature("Export")
    # @allure.story("Photo")
    # @allure.title("Back from export")
    # def test_photo_back_from_export(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    #
    #         assert self.page_shortcut.export_back()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Export")
    # @allure.story("Photo")
    # @allure.title("Produce save")
    # def test_photo_export(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    #
    #         assert self.page_shortcut.export()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Export")
    # @allure.story("Produced")
    # @allure.title("Back to launcher")
    # def test_export_back_to_launcher(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout', media_type='photo', file=photo_9_16)
    #             self.page_shortcut.export()
    #
    #         assert self.page_shortcut.export_back_to_launcher()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    #
    # def sce_6_5_10(self):
    #
    #
    #     try:
    #         self.click(L.edit.menu.play)
    #         timecode_play = self.element(L.edit.menu.timecode).text
    #
    #         if timecode_play != self.timecode_play:
    #
    #             return "PASS"
    #         else:
    #             raise Exception(f'[Fail] Timecode no change: {timecode_play}')
    #
    #     except Exception as err:
    #         traceback.print_exc()
    #
    #
    #         self.driver.driver.close_app()
    #         self.driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_shortcut.enter_shortcut('Cutout')
    #         self.click(L.main.shortcut.try_it_now)
    #         self.page_media.select_local_video(test_material_folder,video_9_16)
    #         self.page_edit.waiting()
    #
    #         return "FAIL"
    #
    # def sce_6_5_11(self):
    #
    #
    #     try:
    #         self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
    #         timecode_play = self.element(L.edit.menu.timecode).text
    #
    #         if timecode_play == '00:00':
    #
    #             return "PASS"
    #         else:
    #             raise Exception(f'[Fail] Timecode no change: {timecode_play}')
    #
    #     except Exception as err:
    #         traceback.print_exc()
    #
    #
    #         self.driver.driver.close_app()
    #         self.driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_shortcut.enter_shortcut('Cutout')
    #         self.click(L.main.shortcut.try_it_now)
    #         self.page_media.select_local_video(test_material_folder,video_9_16)
    #         self.page_edit.waiting()
    #
    #         return "FAIL"
    #
    #
