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


class Test_Class:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "849a7e87-4060-4adc-bcfd-9fb09dbbde6c",
            "3c71ba5c-de2f-4836-a23c-84174b88b393",
            "d1129fb8-8787-4f21-8977-2a635e6f36b1",
            "9a1bab74-3288-4479-89e4-10afd4b363ba",
            "0b29db18-4449-4542-89b6-2290c5bdf0af",
            "6a1f4f60-8b63-4715-b20d-fb2bc38d4816",
            "ec96edb3-2661-4289-bc1d-0f1f7fde76d5",
            "49680802-f61b-4261-98c0-ade94f0c56c9",
            "c97a1527-856a-424e-ad6f-7fb95e8c62a7",
            "d9dc3a24-5cfa-41b2-98ac-15b8f11f2cc5",
            "618efcda-c7ea-4b95-ad6a-8fe68d056c9c",
            "039845d1-d651-4a4b-b5c4-767d32e39ee0",
            "9f058b03-f2bf-431f-9264-685778b2a21a",
            "9606b8a7-0c4f-4c6f-b721-534c605cb428",
            "4bbbe64a-00aa-43c3-8baa-dba274e195f1",
            "b7af9a5e-4c47-4385-aea5-fee220109256",
            "07a93302-832e-4147-89da-3769a6b003c9",
            "9c76ba28-7b29-4d02-9cbe-bf2d4f16f8db",
            "465e3ba4-c8dc-4ea8-9cc4-34d20dc4bff9",
            "3fa99d21-773f-45ec-9b31-75f79d676ac4",
            "92911834-3c4a-4a42-a6f2-86fcbd2edbdf",
            "4d32c30a-6e8e-4aab-959c-fc7f8b0688f5",
            "ba2383dd-3375-43f1-aa4d-f526596babdf",
            "0e807767-04f7-469b-8cd8-ad28d05f5129",
            "17c59fa9-d631-442a-b4a4-5fa8d1c85aed",
            "0bb4905a-b617-42f3-b78d-c34d745e98c8",
            "27c8e278-07f9-47cc-b065-75554fe885e0",
            "1f452f93-8641-41e9-ac63-a22599b8c998",
            "bc54359e-7688-4975-968c-aaf91d1ebb87",
            "904c9910-6258-4a3e-84ed-054c509d105f",
            "5fa83ecb-6fb7-4ecc-82db-4b789fdb2677",
            "5463812f-f36d-4008-8c42-3a6f33c4c3bb",
            "ec1594d6-9391-4333-a54f-d00ee0fa910e",
            "f0963b6a-f74a-4dcd-9e26-550eab5e8eab",
            "33eee74d-c031-49af-b370-89d898d02991",
            "3b473277-8479-4397-91ae-737067524c6f"
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

    def sce_6_21_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            time.sleep(1)

            if self.element(L.main.shortcut.demo_title).text == "Tempo Effect":
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
            self.page_main.enter_shortcut('Tempo Effect')

            return "FAIL"

    def sce_6_21_2(self):
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

    def sce_6_21_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Tempo Effect')
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
            self.page_main.enter_shortcut('Tempo Effect')

            return "FAIL"

    def sce_6_21_4(self):
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
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_21_5(self):
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

    def sce_6_21_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Tempo Effect')
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_21_7(self):
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_21_8(self):
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_9(self):
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_21_10(self):
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_11(self):
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_12(self):
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_13(self):
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.tempo_effect.premium_item())

            if self.click(L.edit.try_before_buy.try_it_first):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try it first" fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
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
            slider = self.element(L.main.shortcut.audio_tool.slider(1)).text
            if slider == '50.0':
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
            self.page_main.enter_shortcut('Tempo Effect')
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
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.slider(1))
            slider = self.element(L.main.shortcut.audio_tool.slider(1)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
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
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.slider(1))
            slider = self.element(L.main.shortcut.audio_tool.slider(1)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
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
            slider = self.element(L.main.shortcut.audio_tool.slider(2)).text
            if slider == '50.0':
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
            self.page_main.enter_shortcut('Tempo Effect')
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
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.slider(2))
            slider = self.element(L.main.shortcut.audio_tool.slider(2)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
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
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.slider(2))
            slider = self.element(L.main.shortcut.audio_tool.slider(2)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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

            if self.click(find_string('Try it now')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try it now" fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            slider = self.element(L.main.shortcut.audio_tool.slider(1)).text
            if slider == '50.0':
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.slider(1))
            slider = self.element(L.main.shortcut.audio_tool.slider(1)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.slider(1))
            slider = self.element(L.main.shortcut.audio_tool.slider(1)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            slider = self.element(L.main.shortcut.audio_tool.slider(2)).text
            if slider == '50.0':
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.slider(2))
            slider = self.element(L.main.shortcut.audio_tool.slider(2)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.slider(2))
            slider = self.element(L.main.shortcut.audio_tool.slider(2)).text
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(find_string('Audio Denoise'))
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
                  # "sce_6_19_5": self.sce_6_19_5(),

                  "sce_6_19_29": self.sce_6_19_29(),
                  "sce_6_19_30": self.sce_6_19_30(),
                  "sce_6_19_31": self.sce_6_19_31(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
