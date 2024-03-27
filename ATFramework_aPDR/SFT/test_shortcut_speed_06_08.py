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


class Test_Shortcut_Speed:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "722a867c-f657-4076-9e31-146428e32b11",
            "b8de0896-786a-439a-bfe1-7ec9b007ef52",
            "408b8d97-7654-4ddb-a9da-1d5121c67605",
            "13bdd464-467b-4d4e-b685-49deada1b624",
            "809e0fc3-e907-42ce-b19b-1ca35fbce4b2",
            "361e181b-56f1-4d0d-b6a0-757ada8b19ef",
            "1c919d4c-58df-4ec2-a295-130f17059232",
            "bbe85604-e8c4-4dae-8c09-92702b3b0ec8",
            "1337c9d5-d3bb-4bac-b8c2-af1677f13931",
            "39e9fe63-c4d4-4244-9204-c74dfb9eb4e9",
            "41268302-b3bb-4fe0-b37f-36180426421c",
            "e7b04472-7660-424f-bbd3-45b2e42c15c9",
            "f178d008-88a7-40f0-a5b4-87b40284ce95",
            "268833d0-3a0b-482e-ac13-94468cbe8904",
            "4167b624-6593-4aa8-9578-33489d8236be",
            "7fe326a6-738a-428a-92e1-4259f0b4c644",
            "8bef40d7-e08c-4760-a158-338af4e712fe",
            "a43f05e8-a2e4-4375-87d6-bf8421f031bd",
            "0e1fc490-3f7f-4221-954f-5638be8a82e6",
            "4a1e2084-a681-4921-815a-fd8e65c507b1",
            "ac0c93ee-4551-4d07-a907-c8a12206b2fa",
            "1ab34f28-ccc1-4f61-90fe-a68ce8ad083d",
            "151801b8-c2a2-4f9c-a2c8-dc1b298cc65e"
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

    def sce_6_8_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Speed')

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
            self.page_main.enter_shortcut('Speed')

            return "FAIL"

    def sce_6_8_2(self):
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

    def sce_6_8_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Speed')
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
            self.page_main.enter_shortcut('Speed')

            return "FAIL"

    def sce_6_8_4(self):
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
                raise Exception('[Fail] Cannot enter Speed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Speed')
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)

            return "FAIL"

    def sce_6_8_5(self):
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
            self.page_main.enter_shortcut('Speed')

            return "FAIL"

    def sce_6_8_6(self):
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
                raise Exception('[Fail] Cannot enter Speed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Speed')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_8_7(self):
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
            self.page_main.enter_shortcut('Speed')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_8_8(self):
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
            self.page_main.enter_shortcut('Speed')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_8_9(self):
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
            self.page_main.enter_shortcut('Speed')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    @report.exception_screenshot
    def test_sce_6_1_1_to_135(self):
        result = {"sce_6_8_1": self.sce_6_8_1(),
                  "sce_6_8_2": self.sce_6_8_2(),
                  "sce_6_8_3": self.sce_6_8_3(),
                  "sce_6_8_4": self.sce_6_8_4(),
                  "sce_6_8_5": self.sce_6_8_5(),
                  "sce_6_8_6": self.sce_6_8_6(),
                  "sce_6_8_7": self.sce_6_8_7(),
                  "sce_6_8_8": self.sce_6_8_8(),
                  "sce_6_8_9": self.sce_6_8_9(),

                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
