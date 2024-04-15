import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from selenium.webdriver import ActionChains

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


class Test_Shortcut_HSL:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            '4fee0ef7-fc78-4b5a-98c6-7fdda1e630d3',
            '521825f5-3ea1-4749-98ff-a3c911836823',
            '0c5539d3-0d78-402f-8bc3-fcf5af74fc9e',
            'd6d36056-7a06-4f64-b5ab-0f1bb734e208',
            'fc0db595-9bce-4cb0-9a74-ddbc58010698',
            '882eaae1-df07-40b3-a4d8-726c89ef4646',
            'd2bc5847-2a54-48fa-b1e2-373d3d44d0bd',
            '3c7c09d2-c7da-4151-8870-05e8f8421d3c',
            '87b13181-338e-4430-82b0-36d02bbe0373',
            'bf32f49c-fce7-49f9-8fcf-9f07417ce7ad',
            'ae603cf7-62f8-4e80-8b95-97e22966089e',
            'bd1a2cdf-d534-4fd9-8cc0-eff63afc5b98',
            '767ddcf0-af92-4fdf-9027-ba4c07e17251',
            '0915e550-da9a-4a72-bd5f-5f696c501fe2',
            'a81bac13-7d33-4e63-b6e6-e718164a3768',
            '9e65386a-5a63-444f-b7a7-44f4e4265067',
            '0a0d97ba-ab43-4356-bb06-21686e54345d',
            '35e5b4a4-8409-4577-9458-3662527b1d4a',
            '9466ff04-9d8c-4e36-9ceb-15df1841d89a',
            '97784a57-0eb0-4156-959d-b8721fc64816',
            '8489da3b-2e45-42e1-8803-a33ddbe51f2f',
            'f131bc46-b881-4d3f-a714-54c461337138',
            '38deaa44-85c3-461e-b0b5-3a10833c4c72',
            '2fb7926f-0cd6-4a63-b395-4f8026dacd62',
            '619edce2-f1b3-45b0-9c7f-80a864a6c46a',
            '87ce49a5-004b-4a6e-b317-abbda5270f43',
            '72ae969f-d7a1-4cfb-a247-6960a90f3e76',
            '8ef8a360-4569-43cb-8ad6-3a311b2b43ec',
            '33ed4f34-c2c7-4a85-a5b3-d91a6c12b319',
            'fe5ac190-2f78-4b0a-b8c4-68b3aadbbaa3',
            'd932f0ba-5ec0-4f7f-9311-07687031a8b1',
            'a0248dff-b5b8-44e5-8b3e-7698cad05db3',
            'b1785692-7f69-4c8b-89df-e6eced38a316',
            '790000ec-e49f-4326-8717-b2eb1638a434',
            'd3a13504-11b6-4361-83e3-46ad64192b4a',
            'ea2fe0b6-dd36-403b-b52e-cc01e37060da',
            '965f4648-c935-40eb-bfd7-ca8d17a6da43',
            'a38b13ce-ba64-4a58-85e2-e4d8d78c1fb0'
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

    def sce_6_1_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')

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
            self.page_main.enter_shortcut('Color Enhancer')

            return "FAIL"

    def sce_6_1_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        report.new_result(uuid, None, "Demo is removed")

    def sce_6_1_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        report.new_result(uuid, None, "Demo is removed")

    def sce_6_1_4(self):
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

    def sce_6_1_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Color\nEnhancer')
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
            self.page_main.enter_shortcut('Color\nEnhancer')

            return "FAIL"

    def sce_6_1_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)

            if self.is_exist(find_string('Color Enhancer')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Color Enhancer')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)

            return "FAIL"

    def sce_6_1_7(self):
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
            self.page_main.enter_shortcut('Color\nEnhancer')

            return "FAIL"

    def sce_6_1_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)

            if self.is_exist(find_string('Color Enhancer')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Color Enhancer')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder,video_9_16)

            return "FAIL"

    def sce_6_1_9(self):
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
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder,video_9_16)

            return "FAIL"

    def sce_6_1_10(self):
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
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder,video_9_16)

            return "FAIL"

    def sce_6_1_11(self):
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
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder,video_9_16)

            return "FAIL"

    def sce_6_1_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            if self.element(L.main.shortcut.hsl.red).get_attribute('selected') == 'true':
                raise Exception('Red is already selected, please change the color')
            self.click(L.main.shortcut.hsl.red)

            if self.element(L.main.shortcut.hsl.red).get_attribute('selected') == 'true':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Color is not changed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder,video_9_16)

            return "FAIL"

    def sce_6_1_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            value = self.element(L.main.shortcut.hsl.hue_value).text

            if value == '0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.hue_slider)
            value = self.element(L.main.shortcut.hsl.hue_value).text

            if value == '-50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.hue_slider)

            return "FAIL"

    def sce_6_1_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.hue_slider)
            value = self.element(L.main.shortcut.hsl.hue_value).text

            if value == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.hue_slider)

            return "FAIL"

    def sce_6_1_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.saturation_slider)
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '-50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.saturation_slider)

            return "FAIL"

    def sce_6_1_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.saturation_slider)
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.saturation_slider)

            return "FAIL"

    def sce_6_1_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            value = self.element(L.main.shortcut.hsl.luminance_value).text

            if value == '0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.luminance_slider)
            value = self.element(L.main.shortcut.hsl.luminance_value).text

            if value == '-50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.luminance_slider)

            return "FAIL"

    def sce_6_1_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.luminance_slider)
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.luminance_slider)

            return "FAIL"

    def sce_6_1_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_4_37(self):
        uuid = 'bb17a360-fce3-444f-976c-9e0022ce648b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.switch_to_photo_library()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.descending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name, reverse=True)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()

            return "FAIL"

    def sce_6_4_38(self):
        uuid = 'e2848afa-8649-4064-8649-db1da9d1dec4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.ascending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_39(self):
        uuid = 'e571055b-e737-4284-9b5c-cc698238afa1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            file_name = "jpg.jpg"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_40(self):
        uuid = 'bdb051bd-5092-4e9e-9430-1dee5a391f4f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            file_name = "gif.gif"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_41(self):
        uuid = 'a4302371-48b7-4cac-86c2-7a85889d793b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            file_name = "png.png"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_42(self):
        uuid = '7f2aeaf7-62d2-4348-b7a5-b4c377cb3ea6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            if not self.is_exist(L.import_media.media_library.color_board):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Can find color_board'

            self.click(L.main.ai_effect.back)

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_43(self):
        uuid = '47039469-aa7c-4628-bd2a-03729c325a41'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_44(self):
        uuid = '70dd1f07-5aea-403a-9029-9419f42d4edc'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_45(self):
        uuid = '0591683c-e463-4e99-88ef-3a74cce46e17'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_46(self):
        uuid = '37c652fe-f97f-451f-a0e3-63d53e859ac3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_47(self):
        uuid = '41c0c860-9e5a-4545-ad54-57fea2dbf769'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_48(self):
        uuid = 'fa743ffe-22c0-485a-adfb-2975d16b5537'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.try_now)

            self.page_media.select_photo_library("getty")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_49(self):
        uuid = '041fcba0-af79-439f-9378-009fc9e08c9f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_50(self):
        uuid = 'f7e26440-d1b1-4704-b76e-88117bf520ba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_51(self):
        uuid = 'c2ad3af3-00a1-4e6e-8d0c-4cacb75e98b5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_52(self):
        uuid = 'a11cb1b4-cd8d-4f2f-8c28-7a4a7cae5aed'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_53(self):
        uuid = 'afa2ced7-bdb2-4054-982c-99c3a06fb899'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("getty_pro")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_54(self):
        uuid = '7718ae03-38e7-4989-8861-9ecc98bd6b23'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_55(self):
        uuid = '4d1a50ad-1226-41fd-9695-9bfd0e531b1d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_56(self):
        uuid = 'ee83ed66-bb25-4843-aad0-545fe8c5d624'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_57(self):
        uuid = 'ebe7c158-bf56-4984-9646-d3e5e59dbb26'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.gettyimages_premium.buy_dialog.btn_buy)
            self.click(find_string("1-tap buy"), 10)
            self.click(L.import_media.media_library.media(), 10)
            self.click(L.import_media.media_library.next)

            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_58(self):
        uuid = '0597ea98-5cae-4b2a-8714-8289bb624ca2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("pexels")
            self.click(L.import_media.media_library.pexels_link)

            if self.is_exist(find_string("pexels.com")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Not find "pexels.com"'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_59(self):
        uuid = 'c9683ebd-c159-4c88-9a96-3cdcf4a637e4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            pic_src = self.page_main.h_full_screenshot()
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_60(self):
        uuid = '9df4e187-e974-4c26-ba04-fa308832c0a9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_61(self):
        uuid = 'e964df3f-8d0a-4eac-b898-49be83ac472c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_62(self):
        uuid = '5f904d0e-7fb8-48b2-9eed-18806a334f2b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_63(self):
        uuid = '83c6529e-f81b-4f31-a726-82f5cb4b3df5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("pixabay")
            self.click(L.import_media.media_library.pixabay_link)

            if self.is_exist(find_string("pixabay.com")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Not find "pixabay.com"'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_64(self):
        uuid = 'ffe5e33c-17cd-4856-b6f1-18898714f950'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            pic_src = self.page_main.h_full_screenshot()
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_65(self):
        uuid = '50ebb786-fa6b-4ac7-9f12-34feb0b6a0fe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_66(self):
        uuid = '68727700-ba6e-4be4-a988-386898963aba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_67(self):
        uuid = '57850b35-b48c-4a3f-affc-1e87a89763c7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_68(self):
        uuid = 'f683a635-e229-4ce7-8fee-3f34ff839c7a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.click(L.import_media.media_library.video.video_capture)
            self.click(L.import_media.media_library.video.start_recording)
            time.sleep(5)
            self.click(L.import_media.media_library.video.stop_recording)
            self.click(L.import_media.media_library.video.camera_ok)
            self.page_media.sort_date_descend()
            self.click(L.import_media.media_library.media())
            self.click(L.import_media.media_library.next)
            import_timeout = self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce) and import_timeout:
                result = True
                fail_log = None
            elif not import_timeout:
                result = False
                fail_log = '\n[Fail] Media import timeout'
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_69(self):
        uuid = '6b4b4ae3-2d24-4914-aebe-688bb2424c75'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.photo.photo_capture)
            self.click(L.import_media.media_library.photo.take_picture)
            self.click(L.import_media.media_library.photo.camera_ok)
            self.click(L.import_media.media_library.media())
            self.click(L.import_media.media_library.next)
            import_timeout = self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce) and import_timeout:
                result = True
                fail_log = None
            elif not import_timeout:
                result = False
                fail_log = '\n[Fail] Media import timeout'
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_70(self):
        uuid = '19a47ca2-91a4-40cb-a7ed-481baa667804'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)
            self.page_media.select_video_library("google_drive")
            self.click(('id', 'com.google.android.gms:id/account_name'))
            self.page_media.waiting_loading()
            self.click(L.import_media.media_library.google_folder())
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_71(self):
        uuid = '4bcad19b-ad8b-48c8-a2bb-1ba5c9ec4be6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)
            self.page_media.select_photo_library("google_drive")
            self.click(('id', 'com.google.android.gms:id/account_name'), 3)
            self.page_media.waiting_loading()
            self.click(L.import_media.media_library.google_folder())
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_72(self):
        uuid = 'e424e887-0930-4d95-b868-aa69a8d9371f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.play_btn)
            playing_time = self.element(L.ai_effect.editor.playing_time).text

            if playing_time != "00:00":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] playing time is not increase: {playing_time}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()
            return "FAIL"

    def sce_6_4_73(self):
        uuid = '2be47a53-4aa2-4337-8415-d54d12f9e7a6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True, clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            selected_num = len(self.elements(L.import_media.media_library.media_order(0)))

            if selected_num == 2:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] media order number incorrect: {selected_num}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            return "FAIL"

    def sce_6_4_74(self):
        uuid = '07286423-8bf8-4644-a21a-d2e7d07b15f9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            if self.element(L.import_media.media_library.next).get_attribute("enabled") == "true":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] "Next" button is not clickable'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            return "FAIL"

    def sce_6_5_1(self):
        uuid = '5f7ad02b-21bd-49bd-9981-4bdf351b12ff'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.next)

            if self.is_exist(L.import_media.media_library.downloading):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] downloading bar is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            self.click(L.import_media.media_library.next)
            return "FAIL"

    def sce_6_5_2(self):
        uuid = 'eaaadb38-b1d0-4554-9c21-2352d30cd212'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.cancel)

            if self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] "Next" button is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)

            return "FAIL"

    def sce_6_6_1(self):
        uuid = '6cbfa1ad-7017-4fba-83da-ce0d89d04513'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.page_ai_effect.leave_editor_to_library:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] back to library fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_template_library()
            return "FAIL"

    def sce_6_6_2(self):
        uuid = '6c2a7cab-5d78-418b-abd4-b35f9d53aad3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.enter_editor(skip_enter_template_library=True, clip=2)
            time.sleep(2)

            if self.element(L.ai_effect.editor.playing_time).text != "00:00":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Playing time = "00:00"'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_3(self):
        uuid = '485634cf-42c7-4821-998c-7cd85c29d18e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.replace_all)

            if self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No "Next" button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_4(self):
        uuid = '2b98fc6b-6ce5-45d0-9362-89b7f3c2ce68'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.back)
            self.click(L.ai_effect.editor.volume_entry)
            volume = self.element(L.ai_effect.editor.slider_text).text

            if volume == "100":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Volume not 100: {volume}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_5(self):
        uuid = 'eb0b0f9b-30bb-446f-b2fa-9ee61e81475a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.volume.play)

            if not self.is_exist(L.ai_effect.editor.volume.play, 2):
                self.click(L.ai_effect.editor.preview)
                if self.is_exist(L.ai_effect.editor.volume.play):
                    result = True
                    fail_log = None
                else:
                    result = False
                    fail_log = f'\n[Fail] Preview is not stopped after tapped'
            else:
                result = False
                fail_log = f'\n[Fail] Play btn is not disappear tapped'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_6(self):
        uuid = '3994d2ce-a9a4-4ab4-a917-b655ef53e227'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.volume.cancel)

            if self.is_exist(L.ai_effect.editor.volume_entry):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No volume entry'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_7(self):
        uuid = '12304abd-5541-48f7-9d50-1489c5460bd1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_main.drag_element(L.ai_effect.editor.volume.slider_text, L.ai_effect.editor.volume.slider)
            self.click(L.ai_effect.editor.volume.apply)

            if self.is_exist(L.ai_effect.editor.volume_entry):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No volume entry'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_8(self):
        uuid = '3a6192b7-3212-441e-8f7e-eb1b97563169'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            playing_time = self.click(L.ai_effect.editor.playing_time).text
            self.click(L.ai_effect.editor.play_btn)
            time.sleep(2)

            if self.click(L.ai_effect.editor.playing_time).text != playing_time:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Playing time no change'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_9(self):
        uuid = '59c63a35-fbec-4df1-8745-a42cb81c9f40'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_main.drag_slider_from_center_to_left(L.ai_effect.editor.playing_bar)
            preview_before = self.page_main.get_picture(L.ai_effect.editor.preview)
            self.page_main.drag_slider_from_center_to_right(L.ai_effect.editor.playing_bar)
            preview_after = self.page_main.get_picture(L.ai_effect.editor.preview)

            if not HCompareImg(preview_after, preview_before).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are the same after dragged slider'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_10(self):
        uuid = 'e9988c06-7a3c-49cd-955b-4ba45e5fa138'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Replace"))

            if not self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Exist "Next" button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_11(self):
        uuid = '77d3f699-a355-484a-a7f7-3a4f26362519'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.back)
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Crop & Range"))
            self.driver.zoom(L.ai_effect.editor.preview)
            self.driver.drag_slider_from_center_to_left(L.ai_effect.editor.crop_range.trim_bar)
            pic_src = self.page_main.get_picture(L.ai_effect.editor.preview)
            self.click(L.ai_effect.editor.crop_range.done)
            self.page_media.waiting_download()
            pic_tgt = self.page_main.get_picture(L.ai_effect.editor.preview)

            if HCompareImg(pic_tgt, pic_src).full_compare() >= 0.9:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Similarity < 0.9'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_12(self):
        uuid = '7747da3f-31f6-4c19-8eae-a9fc1bf052b3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Volume"))
            volume = self.element(L.ai_effect.editor.slider_text).text

            if not self.is_exist(L.ai_effect.editor.volume.play, 2):
                self.click(L.ai_effect.editor.preview)
                if self.is_exist(L.ai_effect.editor.volume.play):
                    if volume == "0":
                        result = True
                        fail_log = None
                    else:
                        result = False
                        fail_log = f'\n[Fail] Volume not 100: {volume}'
                else:
                    result = False
                    fail_log = f'\n[Fail] Preview is not stopped after tapped'
            else:
                result = False
                fail_log = f'\n[Fail] Play btn is not disappear tapped'

            self.driver.drag_slider_from_left_to_right()
            self.click(L.ai_effect.editor.volume.apply)

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_13(self):
        uuid = '2776fd95-8f2d-4019-99c9-4217435a9171'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.export)

            if self.is_exist(L.ai_effect.editor.produce.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_1(self):
        uuid = '74673b45-4847-48f8-b55e-2395b40dd80d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.produce.back)

            if not self.is_exist(L.ai_effect.editor.produce.back):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_7_2(self):
        uuid = '6f5aca48-62ff-49be-a11e-0569569e8116'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.export)
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_1)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "0.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_3(self):
        uuid = '4fe8c038-5eac-41a3-8cfa-d6d4b973ebe1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_2)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "1.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_4(self):
        uuid = '52b6104e-32de-4807-971c-9d37ad05737d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_3)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "2.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_5(self):
        uuid = '1fb7010d-3f70-46a1-97d8-b7af71614290'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_4)

            if self.is_exist(L.produce.iap_back):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No IAP page'

            self.click(L.produce.iap_back)

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_6(self):
        uuid = '855995da-c1ed-455f-b4bc-0932fee039d4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.produce.produce)

            if self.is_exist(L.ai_effect.producing.progress_bar):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No progress bar'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            return "FAIL"

    def sce_6_7_7(self):
        uuid = '4167881a-77ab-42c0-b923-9922bf7f2656'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.producing.cancel)
            self.click(L.ai_effect.editor.producing.cancel_ok)

            if self.is_exist(L.ai_effect.editor.export):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No export button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break
            return "FAIL"

    def sce_6_8_1(self):
        uuid = '1f876e02-b413-4a06-9147-e8c9f3535988'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.produce.produced_back)

            if self.is_exist(L.ai_effect.editor.export):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No export button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_8_2(self):
        uuid = '60f0b428-a199-432a-a07a-4cf49e43aa38'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break

            self.click(L.ai_effect.producing.save_to_file)
            current_pack = self.driver.driver.current_package

            if current_pack != pdr_package:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] current_package is still pdr: {current_pack}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break
            return "FAIL"

    def sce_6_8_3(self):
        uuid = 'edde24ab-5aa4-49c9-b9ea-b68018b17148'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.driver.driver.activate_app(pdr_package)
            self.click(L.ai_effect.producing.share_app_name())
            self.click(L.ai_effect.producing.share_ok, 2)
            current_pack = self.driver.driver.current_package

            if current_pack != pdr_package:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] current_package is still pdr: {current_pack}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break

            return "FAIL"

    def sce_6_8_4(self):
        uuid = '3d8d3218-05f2-4306-8187-82b87155a3bb'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.driver.driver.back()
            self.click(L.ai_effect.producing.done)

            if self.is_exist(L.ai_effect.template.template()):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No template'

            self.report.new_result(uuid, result, fail_log=fail_log)
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_6_1_1": self.sce_6_1_1(),
                  "sce_6_1_2": self.sce_6_1_2(),
                  "sce_6_1_3": self.sce_6_1_3(),
                  "sce_6_1_4": self.sce_6_1_4(),
                  "sce_6_1_5": self.sce_6_1_5(),
                  "sce_6_1_6": self.sce_6_1_6(),
                  "sce_6_1_7": self.sce_6_1_7(),
                  "sce_6_1_8": self.sce_6_1_8(),
                  "sce_6_1_9": self.sce_6_1_9(),
                  "sce_6_1_10": self.sce_6_1_10(),
                  "sce_6_1_11": self.sce_6_1_11(),
                  "sce_6_1_12": self.sce_6_1_12(),
                  "sce_6_1_13": self.sce_6_1_13(),
                  "sce_6_1_14": self.sce_6_1_14(),
                  "sce_6_1_15": self.sce_6_1_15(),
                  "sce_6_1_16": self.sce_6_1_16(),
                  "sce_6_1_17": self.sce_6_1_17(),
                  "sce_6_1_18": self.sce_6_1_18(),
                  "sce_6_1_19": self.sce_6_1_19(),
                  "sce_6_1_20": self.sce_6_1_20(),
                  "sce_6_1_21": self.sce_6_1_21(),
                  "sce_6_1_22": self.sce_6_1_22(),
                  "sce_6_1_23": self.sce_6_1_23(),
                  "sce_6_1_24": self.sce_6_1_24(),
                  "sce_6_1_25": self.sce_6_1_25(),
                  "sce_6_1_26": self.sce_6_1_26(),
                  "sce_6_1_27": self.sce_6_1_27(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
