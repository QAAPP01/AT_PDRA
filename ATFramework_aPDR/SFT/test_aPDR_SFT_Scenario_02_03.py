import pytest, inspect, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_SFT_Scenario_02_03:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report

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

        self.report.set_driver(driver)
        driver.driver.launch_app()
        yield
        driver.driver.close_app()

    def sce_2_3_1(self):
        uuid = '4f38b72e-6424-40dc-adec-fe50681b6bdc'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()

            if self.page_main.enter_timeline():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find timeline canvas'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_3_4(self):
        uuid = '4aa79f8e-ec89-4298-9ff7-a332c8af9110'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            duration = self.page_edit.preference.enter_default_text_duration()

            if duration == '5.0 s':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Duration incorrect: {duration}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.preference.enter_default_text_duration()

            return "FAIL"

    def sce_2_3_2(self):
        uuid = '819376c8-8d0b-4a4f-8272-9b1d1dd63e76'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        slider = L.timeline_settings.preference.slider
        try:
            duration_before = self.element(slider).text
            self.driver.drag_slider_to_max(slider)
            duration_after = self.element(slider).text

            if float(duration_after) > float(duration_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] duration_before = {duration_before}, duration_after = {duration_after}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.preference.enter_default_text_duration()
            self.driver.drag_slider_to_max(slider)

            return "FAIL"

    def sce_2_3_6(self):
        uuid = '345b40e7-fe5c-4ce4-b937-620046a29299'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            duration = self.element(L.timeline_settings.preference.duration_text).text

            if duration == '10.0 s':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Duration incorrect: {duration}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.preference.enter_default_text_duration()

            return "FAIL"

    def sce_2_3_3(self):
        uuid = 'a1785993-89ab-4fff-9392-558f1dba1f8b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        slider = L.timeline_settings.preference.slider
        try:
            duration_before = self.element(slider).text
            self.driver.drag_slider_to_min(slider)
            duration_after = self.element(slider).text

            if float(duration_after) < float(duration_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] duration_before = {duration_before}, duration_after = {duration_after}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.preference.enter_default_text_duration()
            self.driver.drag_slider_to_min(slider)

            return "FAIL"

    def sce_2_3_5(self):
        uuid = 'c1920d5d-e501-468f-8a66-8eb3723c0584'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            duration = self.element(L.timeline_settings.preference.duration_text).text
            self.click(L.timeline_settings.preference.ok)
            self.page_edit.preference.back_to_timeline()

            if duration == '0.5 s':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Duration incorrect: {duration}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_3_7(self):
        uuid = '22625080-9f16-4ba3-9bc7-6d6cbd5ee1c1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.page_edit.text.check_built_in_title():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Built in title checking fail'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.text.enter_category('Classic')

            return "FAIL"

    def sce_2_3_8(self):
        uuid = '30281dfe-de3b-4809-9dcd-469ce0741ecf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Assembly Line')):
                raise Exception('No found "Assembly Line"')
            self.click(L.edit.text.add)

            if self.is_exist(L.edit.text.text_preview):
                self.report.new_result(uuid, True)

                self.click(L.edit.menu.delete)

                return "PASS"
            else:
                fail_log = f'[Fail] No found text clip'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_3_9(self):
        uuid = 'bc2a6a8d-5832-4136-a5eb-dcf232d3ad69'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.page_edit.add_pip_media('Video', test_material_folder, video_9_16):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Add pip video fail'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Video', test_material_folder, video_9_16)

            return "FAIL"

    def sce_2_3_10(self):
        uuid = 'a52b08eb-ff8c-4e3f-b4ce-9c9b788495fd'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Add pip photo fail'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_3_11(self):
        uuid = '7a1459b5-88c9-42e7-8e06-d1937b8d2e64'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_tool('Cutout'):
                raise Exception('Enter Cutout fail')

            if self.element(find_string('No Effect')).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] "No Effect" is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')

            return "FAIL"

    def sce_2_3_12(self):
        uuid = 'c2b0eea9-4983-42b3-8e1a-6ee13b2851f5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            pic_src = self.page_main.get_picture(L.edit.preview.pip_preview)
            if not self.page_edit.enter_sub_option_tool('Remove Background'):
                raise Exception('Click Remove Background fail')
            self.click(L.edit.sub_tool.cutout.try_it, 2)
            self.page_edit.waiting()
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image before and after are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')

            return "FAIL"

    def sce_2_3_13(self):
        uuid = 'fd2eb945-b2f0-4697-bfb6-7274e2d11b5d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_option_tool('Chroma Key'):
                raise Exception('Click Chroma Key fail')
            toast_default = 'Drag the color picker on the screen to select a color.'
            toast = self.element(L.edit.toast).text

            if toast == toast_default:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Toast incorrect: {toast}')

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_14(self):
        uuid = '87d52e81-e0e8-4dce-931e-0b814ea32f51'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            pic_src = self.page_main.get_picture(L.edit.sub_tool.cutout.color_picker.preview)
            self.page_edit.drag_color_picker()
            pic_tgt = self.page_main.get_picture(L.edit.sub_tool.cutout.color_picker.preview)

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Before and after images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')
            self.page_edit.drag_color_picker()

            return "FAIL"

    def sce_2_3_15(self):
        uuid = '2c0f4591-9721-4091-8a60-037a3bb30dd2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            result_max = self.driver.drag_slider_to_max(L.edit.sub_tool.cutout.color_picker.picker_slider)
            result_min = self.driver.drag_slider_to_min(L.edit.sub_tool.cutout.color_picker.picker_slider)

            if result_max and result_min:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Drag to max and min fail'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')
            self.driver.drag_slider_from_center_to_right(L.edit.sub_tool.cutout.color_picker.picker_slider)

            return "FAIL"

    def sce_2_3_16(self):
        uuid = '738da597-7238-43ec-99b7-34ea822e51cf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.cutout.color_picker.picker_btn)

            if self.is_exist(L.edit.sub_tool.cutout.color_picker.picker_image):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] No found color picker on the preview'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_17(self):
        uuid = '3167c930-80a6-4113-8e56-c5f352b1749d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            range_value = self.element(L.edit.sub_tool.cutout.color_picker.range_value).text
            global range_value_default
            range_value_default = '13'

            if range_value == range_value_default:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Range value incorrect: {range_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_18(self):
        uuid = '98101220-f6a3-46c0-8044-1a85757b0df9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.cutout.color_picker.range_slider)
            range_value = self.element(L.edit.sub_tool.cutout.color_picker.range_value).text
            range_value_max = "100"

            if range_value == range_value_max:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Range value incorrect:{range_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_19(self):
        uuid = 'c4940dac-33e1-4d08-9d57-0f2dbfee9ae8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.cutout.color_picker.range_slider)
            range_value = self.element(L.edit.sub_tool.cutout.color_picker.range_value).text
            range_value_min= "0"

            if range_value == range_value_min:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Range value incorrect:{range_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_20(self):
        uuid = 'fb594b20-242e-4779-8bcc-6172b648e03e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            denoise_value = self.element(L.edit.sub_tool.cutout.color_picker.denoise_value).text
            global denoise_value_default
            denoise_value_default = "20"

            if denoise_value == denoise_value_default:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Range value incorrect:{denoise_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_21(self):
        uuid = '26578cc4-5a39-446c-b4a5-ac3e0a6aed44'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.cutout.color_picker.denoise_slider)
            denoise_value = self.element(L.edit.sub_tool.cutout.color_picker.denoise_value).text
            denoise_value_max = "100"

            if denoise_value == denoise_value_max:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Range value incorrect:{denoise_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_22(self):
        uuid = 'f8f2dce3-eeb4-4015-8236-453dd3f5baba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.cutout.color_picker.denoise_slider)
            denoise_value = self.element(L.edit.sub_tool.cutout.color_picker.denoise_value).text
            denoise_value_min = "0"

            if denoise_value == denoise_value_min:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Range value incorrect:{denoise_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')
            self.driver.drag_slider_to_min(L.edit.sub_tool.cutout.color_picker.range_slider)
            self.driver.drag_slider_to_min(L.edit.sub_tool.cutout.color_picker.denoise_slider)

            return "FAIL"

    def sce_2_3_23(self):
        uuid = 'f76319dc-54b2-4c10-b286-50e8188ab845'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.sub_tool.cutout.color_picker.apply):
                raise Exception('Click Apply fail')

            if not self.page_edit.enter_sub_option_tool('Chroma Key'):
                raise Exception('Enter Chroma Key fail')

            range_value = self.element(L.edit.sub_tool.cutout.color_picker.range_value).text
            denoise_value = self.element(L.edit.sub_tool.cutout.color_picker.denoise_value).text

            if range_value == denoise_value == "0":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: range_value:{range_value}, denoise_value:{denoise_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"

    def sce_2_3_24(self):
        uuid = '68f5e57a-ac2b-452a-91c6-b4bfb43f2b1b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.sub_tool.cutout.color_picker.reset):
                raise Exception('Click Reset fail')

            range_value = self.element(L.edit.sub_tool.cutout.color_picker.range_value).text
            denoise_value = self.element(L.edit.sub_tool.cutout.color_picker.denoise_value).text

            if range_value == range_value_default and denoise_value == denoise_value_default:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: range_value:{range_value}, denoise_value:{denoise_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')
            self.driver.drag_slider_to_min(L.edit.sub_tool.cutout.color_picker.range_slider)
            self.driver.drag_slider_to_min(L.edit.sub_tool.cutout.color_picker.denoise_slider)

            return "FAIL"

    def sce_2_3_25(self):
        uuid = '545c205b-66f4-4036-8856-ea10ab4a340e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.sub_tool.cutout.color_picker.cancel):
                raise Exception('Click Cancel fail')

            if not self.page_edit.enter_sub_option_tool('Chroma Key'):
                raise Exception('Enter Chroma Key fail')

            range_value = self.element(L.edit.sub_tool.cutout.color_picker.range_value).text
            denoise_value = self.element(L.edit.sub_tool.cutout.color_picker.denoise_value).text

            if range_value == denoise_value == "0":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: range_value:{range_value}, denoise_value:{denoise_value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('Photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Cutout')
            self.page_edit.enter_sub_option_tool('Chroma Key')

            return "FAIL"



    def sce_2_3_32(self):
        try:
            uuid = '2e869d26-d734-476c-a948-8fb7bcf3b64b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            self.page_edit.add_master_media('photo', test_material_folder, '9_16')
            self.page_edit.add_pip_media('photo', test_material_folder, '16_9')
            self.page_edit.click_tool("Aspect Ratio")
            global image_original
            image_original = self.page_main.get_preview_pic()

            self.click(L.edit.aspect_ratio.ratio_9_16)

            if self.page_edit.preview_ratio() == "9_16":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_3_33(self):
        try:
            uuid = '6b9cf2f2-87ab-4738-8dc4-614223eb8df0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_17.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_3_34(self):
        try:
            uuid = '42d6c14a-c2d9-4d54-a888-85c6337e33e4'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_1_1)

            if self.page_edit.preview_ratio() == "1_1":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_3_35(self):
        try:
            uuid = 'f35ceb9e-f37c-42f8-9bfe-b9f23da0d1a9'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_19.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_3_36(self):
        try:
            uuid = '9e04fdc7-beb5-442f-be6f-bedb66909e8f'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_21_9)

            if self.page_edit.preview_ratio() == "21_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_3_37(self):
        try:
            uuid = '8bb03dce-1b63-4f9b-96cf-2e7882d02e76'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_21.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_38(self):
        try:
            uuid = 'c0edb49c-02f5-4fcb-a404-3488077f466c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_4_5)

            if self.page_edit.preview_ratio() == "4_5":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_39(self):
        try:
            uuid = '0ab23f49-c1ba-402a-97fe-714e84346b76'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_23.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_40(self):
        try:
            uuid = 'd5acb1cd-5810-44d8-ba0e-571c988a7ae4'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_16_9)

            if self.page_edit.preview_ratio() == "16_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_41(self):
        try:
            uuid = '6e4025cd-f203-4685-8e49-e6f4bb5b7bdf'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = image_original

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_42(self):
        try:
            uuid = 'b17ecaa4-c427-4337-95f9-cd506284b85a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.timeline.master_clip)
            self.page_edit.click_sub_tool("Fit & Fill")
            self.click(L.edit.fit_and_fill.btn_fill)
            global image_original
            image_original = self.page_main.get_preview_pic()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            self.click(L.edit.aspect_ratio.ratio_9_16)

            if self.page_edit.preview_ratio() == "9_16":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_43(self):
        try:
            uuid = 'faef9b26-5263-432d-9cf9-5b0765bf7ba2'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_27.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_44(self):
        try:
            uuid = 'c23658ab-d37c-471c-93a9-a67f4c7b205c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_1_1)

            if self.page_edit.preview_ratio() == "1_1":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_45(self):
        try:
            uuid = 'fd2fc883-944e-40af-91f2-12258ad5bd69'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_29.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_46(self):
        try:
            uuid = 'd6ceb6f0-fffd-44c4-8fb1-b301315add5e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_21_9)

            if self.page_edit.preview_ratio() == "21_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_47(self):
        try:
            uuid = '679139c0-c69d-43dd-b000-f9551adb6857'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_31.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_48(self):
        try:
            uuid = 'e4555e47-4e3a-42a9-b884-1d06d0cc2b5f'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_4_5)

            if self.page_edit.preview_ratio() == "4_5":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_49(self):
        try:
            uuid = '51dc22bb-e3c4-4ec3-a75d-287002a6e085'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_33.png')

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_50(self):
        try:
            uuid = '775129a4-9c40-46ba-95d3-da00f125b4b7'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_16_9)

            if self.page_edit.preview_ratio() == "16_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_2_3_51(self):
        try:
            uuid = 'c7eba5c2-11c8-4258-a405-945142cf77d8'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = image_original

            if HCompareImg(pic_base, pic_after).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_310(self):
        result = {}

        # sce_02_03_310
        item_id = '02_03_310'
        uuid = '72f8d373-9b32-4dad-bf16-81bce0cb87a7'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_main.enter_launcher()
        self.page_main.enter_timeline()

        self.page_edit.click_tool('Photo')
        if not self.page_media.select_local_photo(test_material_folder, '9_16.jpg'):
            return False
        self.page_edit.click_tool('Effect')
        self.page_edit.h_click(find_string('Adjustment'))
        self.page_edit.h_click(L.effect.sub_menu.add)
        self.page_edit.h_click(L.edit.try_before_buy.try_it, 1)
        self.page_edit.click_sub_tool('Brightness')
        self.page_edit.h_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_310.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '100'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_311
        item_id = '02_03_311'
        uuid = '4f7e1155-33ab-4d1c-b080-e6ecf11af385'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Contrast')
        self.page_edit.h_set_slider(0)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_311.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '-100'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_312
        item_id = '02_03_312'
        uuid = 'f2482eb4-c4f4-42ae-9ae0-fa9b48305eaa'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Saturation')
        self.page_edit.h_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_312.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '200'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_313
        item_id = '02_03_313'
        uuid = 'd7723b46-9d61-442b-a905-0f3be2e45010'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Hue')
        self.page_edit.h_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_313.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '200'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_314
        item_id = '02_03_314'
        uuid = '21609f3c-7e8e-4498-9d81-8002f059998f'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Temp')
        self.page_edit.h_set_slider(0.7)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id + '.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '70'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_315
        item_id = '02_03_315'
        uuid = '0f261b4a-1644-41d6-8534-6f94570712ae'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Tint')
        self.page_edit.h_set_slider(0.5)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id + '.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '50'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        global pic_src
        pic_src = pic_after

        return "PASS"

    def sce_2_3_336(self):
        try:
            uuid = 'e39097dc-d519-4816-8980-bdff9e19f13c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            item_id = inspect.stack()[0][3].split("sce_")[1]
            self.report.start_uuid(uuid)

            self.page_edit.h_click(L.edit.adjust_sub.reset)
            self.page_edit.click_sub_tool('Sharpness')
            self.page_edit.h_set_slider(0.645)
            pic_tgt = self.page_edit.get_preview_pic()

            result_photo = True if not HCompareImg(pic_tgt, pic_src).full_compare() == 1 else False
            result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text != "0"

            if result_photo and result_value:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_photo: {result_photo}, result_value: {result_value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def test_case(self):
        result = {"sce_2_3_1": self.sce_2_3_1(),
                  "sce_2_3_4": self.sce_2_3_4(),
                  "sce_2_3_2": self.sce_2_3_2(),
                  "sce_2_3_6": self.sce_2_3_6(),
                  "sce_2_3_3": self.sce_2_3_3(),
                  "sce_2_3_5": self.sce_2_3_5(),
                  "sce_2_3_7": self.sce_2_3_7(),
                  "sce_2_3_8": self.sce_2_3_8(),
                  "sce_2_3_9": self.sce_2_3_9(),
                  "sce_2_3_10": self.sce_2_3_10(),
                  "sce_2_3_11": self.sce_2_3_11(),
                  "sce_2_3_12": self.sce_2_3_12(),
                  "sce_2_3_13": self.sce_2_3_13(),
                  "sce_2_3_14": self.sce_2_3_14(),
                  "sce_2_3_15": self.sce_2_3_15(),
                  "sce_2_3_16": self.sce_2_3_16(),
                  "sce_2_3_17": self.sce_2_3_17(),
                  "sce_2_3_18": self.sce_2_3_18(),
                  "sce_2_3_19": self.sce_2_3_19(),
                  "sce_2_3_20": self.sce_2_3_20(),
                  "sce_2_3_21": self.sce_2_3_21(),
                  "sce_2_3_22": self.sce_2_3_22(),
                  "sce_2_3_23": self.sce_2_3_23(),
                  "sce_2_3_24": self.sce_2_3_24(),
                  "sce_2_3_25": self.sce_2_3_25(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

    def test_sce_2_3_32_to_51(self):
        result = {"sce_2_3_32": self.sce_2_3_32(),
                  "sce_2_3_33": self.sce_2_3_33(),
                  "sce_2_3_34": self.sce_2_3_34(),
                  "sce_2_3_35": self.sce_2_3_35(),
                  "sce_2_3_36": self.sce_2_3_36(),
                  "sce_2_3_37": self.sce_2_3_37(),
                  "sce_2_3_38": self.sce_2_3_38(),
                  "sce_2_3_39": self.sce_2_3_39(),
                  "sce_2_3_40": self.sce_2_3_40(),
                  "sce_2_3_41": self.sce_2_3_41(),
                  "sce_2_3_42": self.sce_2_3_42(),
                  "sce_2_3_43": self.sce_2_3_43(),
                  "sce_2_3_44": self.sce_2_3_44(),
                  "sce_2_3_45": self.sce_2_3_45(),
                  "sce_2_3_46": self.sce_2_3_46(),
                  "sce_2_3_47": self.sce_2_3_47(),
                  "sce_2_3_48": self.sce_2_3_48(),
                  "sce_2_3_49": self.sce_2_3_49(),
                  "sce_2_3_50": self.sce_2_3_50(),
                  "sce_2_3_51": self.sce_2_3_51(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

    def test_sce_02_330_to_336(self):
        result = {"sce_2_3_310": self.sce_02_03_310(),
                  "sce_2_3_336": self.sce_2_3_336(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

