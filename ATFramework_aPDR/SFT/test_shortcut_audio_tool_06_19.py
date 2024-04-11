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


class Test_Audio_Tool:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "a5d74fde-f520-4628-9ce6-006bb2a78d8e",
            "10c97639-03b9-468b-b294-db870a4c0f39",
            "cb1756aa-4e5a-4762-baa3-14f53acff415",
            "1248d040-8b18-4c2e-8a22-1559eb263133",
            "07b3d8af-d449-44c9-bc68-8f40fd3f07a3",
            "1aa3c869-c3ec-4fd8-8cfd-826362ce4b41",
            "303cb092-a756-4c8c-b021-82b858486215",
            "5b087e17-cea8-42d4-b7f0-42ce8baf32bf",
            "c693b3eb-72ed-47cc-bf20-a6477f9d98ee",
            "d03065cf-5a55-4cf9-b9e5-328175f22a9a",
            "69f43476-db0f-4cca-a87f-b42e3c74b733",
            "5e514853-c570-47ae-9072-14a56eb69262",
            "382f0b5c-ee85-4b3d-91c2-971c08b2c00c",
            "50c93927-5ac3-459b-9bf0-216676622aac",
            "86e89c2f-f1bf-4714-81fb-b4cabceb0123",
            "8be5bdae-c33c-4fc0-be07-c4cd5b60ef6f",
            "d1496647-2851-48b1-927f-502c9ea282a9",
            "707df5f8-63f1-40b0-92a9-d624f67c75c8",
            "eac5326d-5e56-4377-bfaf-68cd7e2d24d7",
            "4e5b4391-ffc4-4e4b-a765-4d9a1739cc80",
            "1f18e118-045a-4293-8cde-061fc524fc14",
            "d8f7f37c-240d-46ca-8acc-dd5263c56c78",
            "c6c6357d-73ae-4f86-825e-1ac637e646f7",
            "d1b9a46d-eb78-4fd8-b319-ed5362ef9128",
            "06283051-843e-42ed-91e4-8ef2d49151aa",
            "e97f6ba7-a480-4f70-a3bd-cba9ef157b6e",
            "dd9bbbe4-56ba-4018-bc3d-457d9729f49d",
            "db3a9f83-1350-49eb-a8cb-b6bdf2b7b5fb",
            "365c083e-fa25-435b-a833-4f5e97ab86c4",
            "069fe9e1-6a25-4f22-a18b-ae144cb08f59",
            "21a73455-0aaf-464a-9935-6136840090b9"
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

    def sce_6_19_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            time.sleep(1)

            if self.element(L.main.shortcut.demo_title).text == "AI Audio Tools":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Enter Demo page fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')

            return "FAIL"

    def sce_6_19_2(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_19_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            before = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)
            self.click(L.main.shortcut.demo_mute)
            after = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)

            if not HCompareImg(before, after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Mute button no change')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')

            return "FAIL"

    def sce_6_19_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_6(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_19_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_16_9)

            if self.is_exist(find_string('No sound detected')):
                report.new_result(uuid, True)

                self.click(id('btn_ok'))

                return "PASS"
            else:
                raise Exception('[Fail] No found "No sound detected" dialog')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_8(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_9(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_10(self):
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
                raise Exception('[Fail] Enter media picker fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()
            self.click(L.main.shortcut.play)

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the export button')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_12(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_13(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_14(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.audio_tool.info)

            if self.click(find_string('Try It Now')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try It Now" fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '80.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '20.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('Speech Enhance'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)

                self.click(L.main.shortcut.editor_back)
                self.click(L.import_media.media_library.back)

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_19_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()
            self.click(L.main.shortcut.audio_tool.info)

            if self.click(find_string('Try It Now')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try It Now" fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '80.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '20.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_28(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_29(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.try_before_buy.premium_tag)

            if self.click(L.main.subscribe.back_btn):
                report.new_result(uuid, True)

                return "PASS"
            else:
                raise Exception(f'[Fail] Click IAP Back button fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_30(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.export)

            if self.click(L.main.subscribe.back_btn):
                report.new_result(uuid, True)

                return "PASS"
            else:
                raise Exception(f'[Fail] Click IAP Back button fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_31(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.full_editor)

            if self.is_exist(L.edit.menu.produce):
                report.new_result(uuid, True)

                return "PASS"
            else:
                raise Exception(f'[Fail] No timeline produce button')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_6_19_1": self.sce_6_19_1(),
                  "sce_6_19_2": self.sce_6_19_2(),
                  "sce_6_19_3": self.sce_6_19_3(),
                  "sce_6_19_4": self.sce_6_19_4(),
                  "sce_6_19_6": self.sce_6_19_6(),
                  "sce_6_19_7": self.sce_6_19_7(),
                  "sce_6_19_8": self.sce_6_19_8(),
                  "sce_6_19_9": self.sce_6_19_9(),
                  "sce_6_19_10": self.sce_6_19_10(),
                  "sce_6_19_11": self.sce_6_19_11(),
                  "sce_6_19_12": self.sce_6_19_12(),
                  "sce_6_19_13": self.sce_6_19_13(),
                  "sce_6_19_14": self.sce_6_19_14(),
                  "sce_6_19_15": self.sce_6_19_15(),
                  "sce_6_19_16": self.sce_6_19_16(),
                  "sce_6_19_17": self.sce_6_19_17(),
                  "sce_6_19_18": self.sce_6_19_18(),
                  "sce_6_19_19": self.sce_6_19_19(),
                  "sce_6_19_20": self.sce_6_19_20(),
                  "sce_6_19_21": self.sce_6_19_21(),
                  "sce_6_19_5": self.sce_6_19_5(),
                  "sce_6_19_22": self.sce_6_19_22(),
                  "sce_6_19_23": self.sce_6_19_23(),
                  "sce_6_19_24": self.sce_6_19_24(),
                  "sce_6_19_25": self.sce_6_19_25(),
                  "sce_6_19_26": self.sce_6_19_26(),
                  "sce_6_19_27": self.sce_6_19_27(),
                  "sce_6_19_28": self.sce_6_19_28(),
                  "sce_6_19_29": self.sce_6_19_29(),
                  "sce_6_19_30": self.sce_6_19_30(),
                  "sce_6_19_31": self.sce_6_19_31(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
