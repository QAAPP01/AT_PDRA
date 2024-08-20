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
@allure.feature("Cutout")
class Test_Shortcut_Cutout:
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
    def test_entry_from_shortcut(self, driver):
        try:
            self.page_shortcut.enter_shortcut('Cutout')

            assert self.element(L.main.shortcut.demo_title).text == 'AI Smart Cutout'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Cutout')

    @allure.story("Entry")
    @allure.title("Back from demo")
    def test_back_from_demo(self, driver):
        try:
            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()

    @allure.story("Media")
    @allure.title("Enter Media Picker")
    def test_entry_media_picker(self, driver):
        try:
            assert self.page_shortcut.enter_media_picker('Cutout')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_media_picker('Cutout')

    @allure.story("Media")
    @allure.title("Back from media picker")
    def test_back_from_media_picker(self, driver):
        try:
            assert self.page_shortcut.back_from_media_picker()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()

    @allure.story("Media")
    @allure.title("Enter trim before edit")
    def test_entry_trim_before_edit(self, driver):
        try:
            assert self.page_shortcut.enter_trim_before_edit('Cutout')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_trim_before_edit('Cutout')

    @allure.story("Media")
    @allure.title("Back from trim before edit")
    def test_back_from_trim_before_edit(self, driver):
        try:
            assert self.page_shortcut.back_from_trim()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_media_picker('Cutout')

    @allure.story("Media")
    @allure.title("Trim video and edit")
    def test_trim_and_edit(self, driver):
        try:
            assert self.page_shortcut.trim_and_edit()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_editor('Cutout')

    @allure.story("Media")
    @allure.title("Back from editor")
    def test_back_from_editor(self, driver):
        try:
            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_media_picker('Cutout')

    @allure.story("Media")
    @allure.title("Enter editor")
    def test_enter_editor(self, data):
        try:
            assert self.page_shortcut.enter_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Play preview")
    def test_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Cutout')

            assert self.page_shortcut.play_preview()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    # @allure.story("Editor")
    # @allure.title("Add background photo")
    # def test_add_background_photo(self,data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout')
    #
    #         assert self.page_shortcut.add_background_photo(test_material_folder,photo_9_16)
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise
    #
    # @allure.story("Editor")
    # @allure.title("Remove background")
    # def test_remove_background(self,data):
    #     try:
    #         if self.last_is_fail(data):
    #             self.page_shortcut.enter_editor('Cutout')
    #
    #         assert self.page_shortcut.remove_background()
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         logger(e)
    #         data['last_result'] = False
    #         raise


    @allure.story("Editor")
    @allure.title("Export")
    def test_export(self):
        try:
            assert self.page_shortcut.export()

        except Exception as e:
            traceback.print_exc()
            logger(e)


    def sce_6_5_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.play)
            time.sleep(3)
            self.timecode_play = self.element(L.main.shortcut.timecode).text

            if self.timecode_play != "00:00":
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {self.timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_edit.waiting()

            return "FAIL"

    def sce_6_5_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.play)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play != self.timecode_play:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_edit.waiting()

            return "FAIL"

    def sce_6_5_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play == '00:00':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_edit.waiting()

            return "FAIL"


