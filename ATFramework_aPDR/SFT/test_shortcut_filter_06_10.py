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


class Test_Shortcut_Filter:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "d791327c-6619-4c20-9b12-32caec20ede5",
            "b34238d3-975f-4de7-a43f-9985a88db2aa",
            "d903d277-0a48-4426-a98b-a3a1bb2c1fdd",
            "29062252-7cac-4b6b-97d5-05c473c65dd9",
            "d638ea6f-e8e6-4279-be64-9ca7ec5bde3d",
            "87c37b48-8381-464b-80fb-b0da8b94a2c4",
            "06c6dc9c-c193-482d-8702-4a60d5179b0e",
            "126fe72e-d621-4b29-9c2f-189ca87a939a",
            "cc7d34ea-4ba3-4b44-963f-b8436184a7ca",
            "ad401e79-6f87-4438-8817-c1d478474079",
            "335805ee-9346-4bba-83b2-0a4df44fa235",
            "025a374d-656b-4b34-9753-f8645363f190",
            "c201a11b-330d-4876-8492-cb3e306aba27",
            "0d06729f-3d8a-4d1c-9b06-dcbaa4cd368f",
            "c48fb904-bc74-4de6-b0c8-f3303e628d78",
            "6db14e2c-271e-4df5-8f3f-a3971ff10f72",
            "4765fe8d-b5c3-4d3a-b11a-9b0a6495f03d",
            "b0c5278c-029d-4c7f-8218-6743874507db",
            "f2c38449-f096-47ad-9b4c-8c0b657ef82f",
            "729ee7e9-7e63-405e-bcc3-0e3eec1ded4b",
            "2e123016-50e5-4218-b283-96114d9ee9c3",
            "4f74307b-881b-4ba0-99d6-d72fa83ff07a",
            "d56bdf35-cd7b-4e07-9869-8e7e41e2fe55",
            "0d009937-b5e7-49ab-bd8f-fa8e8139bce6",
            "4ea3a8a7-8f23-466c-9c56-a85dc91ff7fa",
            "fbcd0f4d-6192-4eb3-abff-3eb3a655fd66",
            "f72db29d-bb21-4022-a5a7-419473aa2605",
            "eb6a8e1d-d293-4441-a92a-e012d2ead9a7",
            "4c6915a9-6c18-4fee-aa5b-21872d7444b5",
            "c08c7606-7133-4eb6-b679-fdc3d1a2330d",
            "bed8b19b-1a91-40d7-b8e5-ec6c445c80f4",
            "bd7a3f29-60c5-4b97-8b66-e81455fe405a",
            "48e1e7a6-70bd-471c-8892-2cd383320103",
            "c4c505c1-e279-4a0b-abdf-8853c1e4b3a8",
            "4f122e85-0f16-4204-a329-304a869832b8",
            "042eb070-2f83-42d4-91f2-a79aeacf59bc",
            "7cf42f4f-2a1c-4583-add2-d9140f5eedca"
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

    def sce_6_10_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Filter')

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
            self.page_main.enter_shortcut('Filter')

            return "FAIL"

    def sce_6_10_2(self):
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

    def sce_6_10_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Filter')
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
            self.page_main.enter_shortcut('Filter')

            return "FAIL"

    def sce_6_10_4(self):
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

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Filter')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Filter')
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_10_5(self):
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
            self.page_main.enter_shortcut('Filter')

            return "FAIL"

    def sce_6_10_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Filter')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Filter')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_10_7(self):
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
            self.page_main.enter_shortcut('Crop & Rotate')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_10_8(self):
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
            self.page_main.enter_shortcut('Crop & Rotate')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_10_9(self):
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
            self.page_main.enter_shortcut('Crop & Rotate')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_6_10_1": self.sce_6_10_1(),
                  "sce_6_10_2": self.sce_6_10_2(),
                  "sce_6_10_3": self.sce_6_10_3(),
                  "sce_6_10_4": self.sce_6_10_4(),
                  "sce_6_10_5": self.sce_6_10_5(),
                  "sce_6_10_6": self.sce_6_10_6(),
                  "sce_6_10_7": self.sce_6_10_7(),
                  "sce_6_10_8": self.sce_6_10_8(),
                  "sce_6_10_9": self.sce_6_10_9(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")