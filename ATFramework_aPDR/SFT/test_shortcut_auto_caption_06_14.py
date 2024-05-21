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


class Test_Shortcut_Auto_Caption:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "993f8ed2-e092-43fc-94d4-28cc240da66d",
            "1864064b-afa3-44fd-aa14-b28b2c0971c2",
            "ffc58b53-a852-4de8-beb5-4ef2442cc4f4",
            "3d47a314-780a-49ee-9a04-be4e204050f2",
            "a93bbcb8-b820-4521-ae16-331ef6401441",
            "32162938-21f3-4dda-8a92-6c7d377ab3bc",
            "df0e9df2-fda9-4e59-a354-a9ce70be426f",
            "4b86903b-12ba-4802-ac3e-4d157824a877",
            "38e8ff77-7d79-41f7-82e8-f72612cc3646",
            "121ff0bc-32e9-4bfe-9032-bf328df9a631",
            "c33ae730-9913-40e6-bf6a-1f05ea40d192",
            "918e4fde-6d14-4cad-9ed1-34c69d4f1e88",
            "d35f058c-aaf5-460f-8206-42bbc32b72df",
            "f334c9c5-3f6d-493a-867d-d6d8b2960026",
            "3c599597-9993-4971-9990-8193eb5d76b5",
            "db3756ec-e113-4851-8f28-610cea7b5ed8",
            "51d359c8-ce87-420f-a656-7ba51eadcdb7",
            "896533e3-ac74-4599-a296-4ed381149939",
            "281b6119-9a6c-49eb-948d-3bd73d43fce8",
            "1368df97-43b7-4d91-9216-00a4a8d75ff3",
            "d80f4c54-d0cc-46aa-8bb2-32f9ff2ddf1e",
            "a93c9287-1de6-44e7-91bd-d8c75732097b",
            "b4792c4e-e97b-419d-b75b-125e11a9c128",
            "ae394810-4479-4f13-a3b3-5759c84bd6e4",
            "41bf8229-7b58-4f8e-aa3c-73c34011b8c2",
            "b34788b2-cd7f-438c-b938-8d4231b915ef",
            "8cdc6364-798d-41db-b70b-9c76d699fb7f",
            "f61e6a98-d295-4821-b631-922b3f8cc583",
            "68db002c-b530-420b-99f6-4d3672eba45a",
            "5d20f7b0-cf29-4252-87c2-56c33d1aacab",
            "b8693b38-ce9a-44d7-90f2-03336b08faa9",
            "4ae989ae-58d1-46ec-80e2-f1409e903b5e"
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

    def sce_6_14_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Auto Captions')

            if self.is_exist(find_string('Auto Caption')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Demo page')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Auto Captions')

            return "FAIL"

    def sce_6_14_2(self):
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

    def sce_6_14_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)

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
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_14_4(self):
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

    def sce_6_14_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Auto Captions')
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
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"
        
    def sce_6_14_7(self):
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
                raise Exception('[Fail] Cannot enter Auto Captions')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_14_8(self):
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
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"
        
    def sce_6_14_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            for wait in range(60):
                if self.is_exist(find_string('Cancel')):
                    time.sleep(2)
                else:
                    break

            if self.is_exist(find_string('Export')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Auto Captions')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_14_10(self):
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
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_14_11(self):
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
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_14_12(self):
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
            self.page_main.enter_shortcut('Auto Captions')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    
    def test_case(self):
        result = {"sce_6_14_1": self.sce_6_14_1(),
                  "sce_6_14_2": self.sce_6_14_2(),
                  "sce_6_14_3": self.sce_6_14_3(),
                  "sce_6_14_4": self.sce_6_14_4(),
                  # "sce_6_14_5": self.sce_6_14_5(),
                  "sce_6_14_6": self.sce_6_14_6(),
                  "sce_6_14_7": self.sce_6_14_7(),
                  "sce_6_14_8": self.sce_6_14_8(),
                  "sce_6_14_9": self.sce_6_14_9(),
                  "sce_6_14_10": self.sce_6_14_10(),
                  "sce_6_14_11": self.sce_6_14_11(),
                  "sce_6_14_12": self.sce_6_14_12(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
