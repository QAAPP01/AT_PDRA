import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from appium.webdriver.common.touch_action import TouchAction

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory

from .conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_Shortcut_Crop:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "2d2300ac-420d-404a-af92-49fdf6e48c9a",
            "eb345ff2-e6a8-44d8-8d02-e782f13f12ad",
            "55e0b687-aae9-4e0c-89d4-770c5ccf7b48",
            "7d592da5-a49d-4530-98d9-6c9c08e5f871",
            "ef4c47a0-5951-4d68-bcb1-b507efe68eea",
            "2c51c68a-b62f-4151-b9b4-9b678b9ba9cd",
            "58c62b58-6080-4517-b242-55105655bc3f",
            "cae474b2-1c6c-4aac-8429-54357e5e8c2d",
            "00684768-4f39-4b27-a431-4f97945e9bfe",
            "74014c76-18f8-45d3-b2fa-eca697b78e1f",
            "7410e2ab-f7a3-4328-a5b2-20d79ef3154d",
            "61c6c983-8b72-4018-aa8e-d14dbf70b417",
            "09b3a678-d0d8-4dbc-8bbd-42c9eaa69dc1",
            "b5ba5f03-827b-466b-9afc-eb7e26180ecf",
            "52753e20-05db-49c5-9e8d-c4140e4ea5d3",
            "f533ef52-5185-43b6-9a12-d77006839b96",
            "bde517f3-c228-48fc-9fd4-8b49419d232a",
            "22e64865-d783-41ce-aa6c-483bad162fcf",
            "7ccb59f6-58c5-4867-a88f-af159817d2aa",
            "8896cb4e-da7a-4135-8696-15c0c03cd510",
            "5f7528ca-d50a-4eb9-b660-415656b8ef42",
            "c10aa56e-a39a-4dc8-a36d-066b6d9a3f24",
            "73cba1c6-5de4-404f-902e-20a5d2a7ccd2",
            "f38655ec-b798-4e94-935e-005ad1e31559",
            "11c670d7-4f3b-4586-bd2d-aecf6c0fdd57",
            "41d0a0ed-a871-471c-955d-d898ff78cdf3",
            "91bb756c-3864-4b85-92a0-bde3b226c055",
            "a8fb6854-c79e-4a28-94fd-01095db05355",
            "d15bf2db-ae70-40c3-893e-339915169044"
                     ]

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='medium', video_fps=30)

    def sce_6_7_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Crop & Rotate')

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
            self.page_main.enter_shortcut('Crop & Rotate')

            return "FAIL"

    def sce_6_7_2(self):
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

    def sce_6_7_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Crop & Rotate')
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
            self.page_main.enter_shortcut('Crop & Rotate')

            return "FAIL"

    def sce_6_7_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            if self.is_exist(find_string('Export')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Crop & Rotate')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Crop & Rotate')
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_7_5(self):
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
            self.page_main.enter_shortcut('Crop & Rotate')

            return "FAIL"

    def sce_6_7_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            if self.is_exist(find_string('Export')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Crop & Rotate')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Crop & Rotate')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_7_7(self):
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
            self.page_main.enter_shortcut('Crop & Rotate')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_7_8(self):
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
            self.page_main.enter_shortcut('Crop & Rotate')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_7_9(self):
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
            self.page_main.enter_shortcut('Crop & Rotate')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    
    def test_case(self):
        result = {"sce_6_7_1": self.sce_6_7_1(),
                  "sce_6_7_2": self.sce_6_7_2(),
                  "sce_6_7_3": self.sce_6_7_3(),
                  "sce_6_7_4": self.sce_6_7_4(),
                  "sce_6_7_5": self.sce_6_7_5(),
                  "sce_6_7_6": self.sce_6_7_6(),
                  "sce_6_7_7": self.sce_6_7_7(),
                  "sce_6_7_8": self.sce_6_7_8(),
                  "sce_6_7_9": self.sce_6_7_9(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
