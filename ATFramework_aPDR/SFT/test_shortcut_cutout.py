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

            self.page_main.enter_shortcut('Cutout')

            assert self.element(L.main.shortcut.demo_title).text == 'AI Smart Cutout'

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')

            pytest.fail(f"{str(e)}")

    def sce_6_5_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.demo_back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"


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
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)

            pytest.fail(f"{str(e)}")

    def sce_6_5_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.import_media.media_library.back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_5_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_back)

            if self.is_exist(find_string('Add Media')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_5_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)
            self.page_edit.waiting()

            if self.is_exist(L.main.shortcut.cutout.color(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Cutout')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)

            return "FAIL"

    def sce_6_5_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.editor_back)

            if self.is_exist(find_string('Add Media')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"


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
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
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


