import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from appium.webdriver.common.touch_action import TouchAction

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import REPORT_INSTANCE as report
from .conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_Shortcut_Cutout:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "49954661-274f-4576-9d70-0f20c82683f1",
            "ecd162dd-291e-4fbb-81ed-394efb6b8def",
            "d1c954e9-5820-4110-995d-b8258769460b",
            "1185af9c-e5b3-4879-b7a8-df4f950b6c5d",
            "b30feff2-f97a-4a7b-8f5d-3cdef6dc62ab",
            "2741425b-48c3-4d74-be86-d224c438dbfc",
            "07235130-94d5-47ed-a3c7-efd4cbed5e1f",
            "c2b502d3-5055-4fea-924a-68c379c94019",
            "20668266-4fb7-4584-a1ad-a7665959ccfc",
            "27ac5df9-d38f-4a83-9c9f-407c13c8338f",
            "d872f119-8866-4d40-93c1-94dc09fc42a9",
            "e6720182-8f14-421b-be51-6eaaa2207a72",
            "6ce12ece-7c6a-46ca-99fd-175e6b337fa5",
            "8d937f89-8d17-42a9-a6b1-5c6e1c80f3f5",
            "90c8f4c2-4619-49a0-9145-f4958f75d4b0",
            "06de8d25-50ce-4ad2-acb8-0125ec2adbc5",
            "1c72c4f8-69f9-43f8-98dd-855b7e387545",
            "2185db8e-9cf5-488d-b727-7920d21fa04d",
            "0de81833-7df4-4b7f-87e1-eda64979f39c",
            "d5230efc-25ca-4567-bcef-3b164b736eab",
            "06489090-1a00-405c-9d8f-6b1e356406d3",
            "d9a4f627-8cbd-4af2-a0d1-3c4b2d1215f5",
            "3f8b3bba-84e0-4d35-aca6-82b485d33ca4",
            "3305fcd3-3c6e-4610-bc7a-c7720dd4ec40",
            "69d1d813-2f44-449f-ba07-e51861998ec8",
            "e8eb4f3a-69f2-4841-b494-aa14550ab829",
            "92400711-2c85-4215-8604-732e9aff66a6",
            "4aba7adc-ebbf-42aa-9b81-1173a2b8ff80",
            "953e997f-c3c7-477c-8a51-560d2c74907d",
            "af61d739-48fe-4401-9947-101a178c274d",
            "4c4beda0-b978-4a2c-9f2f-aa978a196c7d",
            "06702757-e3e4-4ab0-9c50-7b9679f45996",
            "741e50d5-673d-4def-9650-8dec0c151daa",
            "e3c8fe25-f078-4ee4-b59a-7dc60bb5b6a6",
            "2b3ef07b-3a4a-4883-a631-a9f195a4d88c",
            "429f036a-a05d-4319-96e6-7c3a7f256c2d",
            "92953934-6fef-4f3d-b79e-7c700b7799aa",
            "098565b9-6ef1-4ee9-aab2-b23bafad2c80",
            "9d04a415-d759-49f8-942e-4f4d32e9c93f",
            "c1f15ea3-865e-4474-ab3a-dc76d8c87c42",
            "62515f29-7a9b-42eb-be29-072ee6f2079d",
            "80f6b7e3-9b71-4b09-ad33-2876ca829e69",
            "ad52350d-96cb-4127-a2ed-ec5a05fff3f5",
            "55d83727-6391-4424-aa32-071a6cd2fe54",
            "9c5f8aba-3826-4b4c-b95c-a55d5166b49b",
            "edf1de5c-2d4c-4e4d-8a69-b7392883e9ae",
            "73da9412-5a4b-4366-8277-ae42afe1dce0",
            "45cbff57-93e5-4c50-aa53-6b0daffbb6ab"
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

        report.set_driver(driver)
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

    def sce_6_5_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')

            if self.is_exist(find_string('Cutout')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Demo page')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')

            return "FAIL"

    def sce_6_5_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.demo_back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_5_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_5_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_5_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_back)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

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
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            if self.is_exist(L.main.shortcut.cutout.color(0)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Cutout')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

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
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.editor_back)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_5_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            if self.is_exist(L.main.shortcut.cutout.color(0)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Cutout')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_5_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.play)
            time.sleep(3)
            self.timecode_play = self.element(L.main.shortcut.timecode).text

            if self.timecode_play != "00:00":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {self.timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_5_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.play)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play != self.timecode_play:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_5_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play == '00:00':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Cutout')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    @report.exception_screenshot
    def test_sce_6_1_1_to_135(self):
        result = {"sce_6_5_1": self.sce_6_5_1(),
                  "sce_6_5_2": self.sce_6_5_2(),
                  "sce_6_5_3": self.sce_6_5_3(),
                  "sce_6_5_4": self.sce_6_5_4(),
                  "sce_6_5_5": self.sce_6_5_5(),
                  "sce_6_5_6": self.sce_6_5_6(),
                  "sce_6_5_7": self.sce_6_5_7(),
                  "sce_6_5_8": self.sce_6_5_8(),
                  "sce_6_5_9": self.sce_6_5_9(),
                  "sce_6_5_10": self.sce_6_5_10(),
                  "sce_6_5_11": self.sce_6_5_11(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
