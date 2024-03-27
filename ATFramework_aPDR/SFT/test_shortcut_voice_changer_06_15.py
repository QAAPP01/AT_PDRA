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
video_speech = 'speech_noise_1.mp4'


class Test_Shortcut_Voice_Changer:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "c720aa67-9e59-4ad6-aca2-9c868c0e2a4f",
            "646db8fb-4c86-47f2-94d3-b89ef50ddd7f",
            "be41d1df-2d5a-42ba-8ffd-8459dfeeabb3",
            "b279f39e-dd0b-4c45-a79e-1160e8b01872",
            "4d592499-3399-4df5-9f4c-56f6fd602f73",
            "a5da34b1-6a3d-42c7-b958-5927f99441d6",
            "2a354d7b-cf82-4ba7-b167-8aa3cb25451a",
            "6870d4ee-f5ab-484d-ae66-170701377bfe",
            "868e8ce5-b019-4c3d-9b70-fe810ef90868",
            "65659aba-c082-4d6c-9db3-52e1b0b88074",
            "1461d36a-31e0-45cf-a65b-b0a7c88f7051",
            "a1261cc3-5f2c-44ff-90e9-4a2e03182b9a",
            "36626cc0-67c7-4e20-9fea-d421dc2d0482",
            "da076c8e-7abf-485f-866c-50f32eba6894",
            "dc1c4d77-5eb1-4996-8602-f90158f6b2ac",
            "844d906d-a145-468a-996b-b5fb4c7188ac",
            "e4ff5939-1681-48b5-a5cd-d9676d8e5742",
            "505edb40-ead8-480c-87e9-5ad3d8beb599",
            "1884fe7e-2bb7-481a-9373-0ce9cd3667a3",
            "fc9fad7d-6528-4fdd-8145-9b01689bdc04",
            "60cf9246-fd36-4149-93cb-7911f69485c1",
            "eb76c3b4-8dcf-43b0-a47e-0915b6f9c8ca",
            "03866171-2d99-410f-8dcf-50d5de194f47"
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

    def sce_6_15_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Voice\nChanger')

            if self.is_exist(find_string('Voice Changer')):
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
            self.page_main.enter_shortcut('AI Voice\nChanger')

            return "FAIL"

    def sce_6_15_2(self):
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

    def sce_6_15_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Voice\nChanger')
            before = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)
            self.click(L.main.shortcut.voice_changer.mute)
            after = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)

            if not HCompareImg(before, after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Mute button no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Voice\nChanger')

            return "FAIL"

    def sce_6_15_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
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
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_15_5(self):
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
                raise Exception('[Fail] Return launcher fail')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_15_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_16_9)

            if self.is_exist(find_string('No sound detected')):
                report.new_result(uuid, True)

                self.click(id('btn_ok'))

                return "PASS"
            else:
                raise Exception('[Fail] No found "No sound detected" dialog')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_15_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.click(L.import_media.media_library.trim_back)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Tap preview "{video_speech}" fail')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_15_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Voice Changer')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_15_9(self):
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
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_15_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Voice Changer')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_15_11(self):
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
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_15_12(self):
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
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_15_13(self):
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
            self.page_main.enter_shortcut('AI Voice\nChanger')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_6_15_1": self.sce_6_15_1(),
                  "sce_6_15_2": self.sce_6_15_2(),
                  "sce_6_15_3": self.sce_6_15_3(),
                  "sce_6_15_4": self.sce_6_15_4(),
                  "sce_6_15_5": self.sce_6_15_5(),
                  "sce_6_15_6": self.sce_6_15_6(),
                  "sce_6_15_7": self.sce_6_15_7(),
                  "sce_6_15_8": self.sce_6_15_8(),
                  "sce_6_15_9": self.sce_6_15_9(),
                  "sce_6_15_10": self.sce_6_15_10(),
                  "sce_6_15_11": self.sce_6_15_11(),
                  "sce_6_15_12": self.sce_6_15_12(),
                  "sce_6_15_13": self.sce_6_15_13(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
