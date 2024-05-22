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


class Test_Shortcut_Video_Effect:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "4f4d9263-874b-444d-a83b-66d5ed94df2d",
            "ff093cee-2bb2-422e-8b04-7acc842d89be",
            "4bf3eb09-2acc-4167-9b69-2e1cb439f102",
            "2a8e9eb2-0a71-4c33-85bc-8e8f63593120",
            "3110b92b-da32-4678-a4c2-453021925ba5",
            "2effa00c-045e-4476-bcb0-c6861eb74946",
            "41efe64e-56ee-4932-a0a5-bdd74284b64b",
            "dd71f621-c59e-4a15-8158-e20b67becfba",
            "18acf6b6-e41d-4ffb-ab09-4de26aac5e46",
            "c503c2d8-3a89-45b5-b189-cdd1f99c02f8",
            "bd9e44ef-32cf-40af-b592-520819c22019",
            "a26bbfb1-2ee7-4219-aaec-7c585fa2209e",
            "3553acc2-0ca4-4083-a830-9962cee2c970",
            "0558c8a1-d747-4681-a352-9ef9b076af28",
            "593d747c-7a80-4b1a-8300-9eac0d01dadc",
            "3944b7c8-646a-41ce-a909-474b36607f13",
            "3259deb3-a6bd-4fbf-bbb0-0423400aaf89",
            "8a27902e-ffe6-4143-afc0-8168c467865b",
            "de891b7b-ad1c-4bf9-bee4-af9f44698ada",
            "a4fd3c8e-320b-42bc-bbb6-6d28fe60640d",
            "01d2054b-f3b4-423d-830c-d220c6416ed9",
            "0c81c674-0160-4ae8-9213-90ab529c2998",
            "bfe7dc50-dabf-49cb-a124-6620b60d28bd",
            "69ed52b3-70cf-4abb-81fe-b8fb1949ebc0",
            "f9bdb803-3c56-4227-b9dc-1d0b79d00c51",
            "3c2351be-d2da-4139-a874-bca02af37e16",
            "55800552-5fd4-4c2a-9ac4-95f76dacdc6d",
            "f00a59a0-424a-4367-8924-bf2b128217db",
            "039e3545-477b-4fcc-af1b-946f509f26ac",
            "fe452e9c-19ab-47e9-a870-592cdb8852de",
            "b7716c87-123b-4439-be90-5a7ea2f38c83",
            "ac678dd3-83c2-4637-b5f3-d9ef67259539"
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

    def sce_6_6_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Video Effect')

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
            self.page_main.enter_shortcut('Video Effect')

            return "FAIL"

    def sce_6_6_2(self):
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

    def sce_6_6_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Video Effect')
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
            self.page_main.enter_shortcut('Video Effect')

            return "FAIL"

    def sce_6_6_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            if self.is_exist(L.main.shortcut.video_effect.effect(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Video Effect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Video Effect')
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)

            return "FAIL"

    def sce_6_6_5(self):
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
            self.page_main.enter_shortcut('Video Effect')

            return "FAIL"

    def sce_6_6_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            if self.is_exist(L.main.shortcut.video_effect.effect(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Video Effect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Video Effect')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_6_7(self):
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
            self.page_main.enter_shortcut('Video Effect')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_6_8(self):
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
            self.page_main.enter_shortcut('Video Effect')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_6_9(self):
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
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    
    def test_sce_6_1_1_to_135(self):
        result = {"sce_6_6_1": self.sce_6_6_1(),
                  "sce_6_6_2": self.sce_6_6_2(),
                  "sce_6_6_3": self.sce_6_6_3(),
                  "sce_6_6_4": self.sce_6_6_4(),
                  "sce_6_6_5": self.sce_6_6_5(),
                  "sce_6_6_6": self.sce_6_6_6(),
                  "sce_6_6_7": self.sce_6_6_7(),
                  "sce_6_6_8": self.sce_6_6_8(),
                  "sce_6_6_9": self.sce_6_6_9(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
