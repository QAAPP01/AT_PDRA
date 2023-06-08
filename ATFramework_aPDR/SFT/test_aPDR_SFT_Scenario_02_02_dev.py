import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_SFT_Scenario_02_02:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
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

    def sce_2_2_1(self):
        uuid = '4979f807-43ed-48ae-b85f-9a28b2ab989a'
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

    def sce_2_2_2(self):
        uuid = '7713342c-d600-43b7-9fe8-1675a2124c7b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16):
                raise Exception('Add media fail')

            if not self.page_edit.enter_main_tool('AI Effect'):
                raise Exception('Enter AI Effect fail')

            if self.is_exist(find_string('None')):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find "None"'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_3(self):
        uuid = 'e8286094-ffe5-4cca-8dd5-4a29e66f1b15'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.is_exist(L.edit.timeline.master_track.trim_indicator):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No master clip is selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_4(self):
        uuid = '283f410f-a8aa-4ff7-aa9f-b60221586e8d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.tap_blank_space():
                raise Exception('Tap blank space fail')
            self.click(L.edit.timeline.master_track.master_clip())
            if not self.page_edit.enter_sub_tool('AI Effect'):
                raise Exception('Enter AI Effect fail')

            if self.is_exist(L.edit.tool_menu.ai_effect.effect(0)):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No master clip is selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_5(self):
        uuid = 'b235c57c-2f0e-41af-94b7-559ef7848880'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.element(L.edit.tool_menu.ai_effect.none_highlight).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] None is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_6(self):
        uuid = '09586d72-f271-4863-9e7e-36416d682706'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            index = 1
            if not self.click(L.edit.tool_menu.ai_effect.effect(index)):
                raise Exception('Click effect fail')
            self.click(L.edit.try_before_buy.try_it, 2)

            if self.element(L.edit.tool_menu.ai_effect.effect_name(index)).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Effect is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.tool_menu.ai_effect.effect(1))

            return "FAIL"

    def sce_2_2_7(self):
        uuid = 'fcebcfb5-f2b5-41d7-91d8-70425154ba2c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.tool_menu.ai_effect.edit):
                raise Exception('Click editing icon fail')

            if self.is_exist(L.edit.tool_menu.ai_effect.param_area):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find param_area'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.tool_menu.ai_effect.effect(1))
            self.click(L.edit.tool_menu.ai_effect.edit)

            return "FAIL"

    def sce_2_2_8(self):
        uuid = '8f6911a6-f3ab-4d48-8626-08287afb95af'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            param_num = len(self.elements(L.edit.tool_menu.ai_effect.param_value(0)))
            param_flag = 0
            global default_value
            for i in range(param_num):
                if self.element(L.edit.tool_menu.ai_effect.param_value(i + 1)).text == "":
                    continue
                else:
                    param_flag = 1
                    default_value = (i + 1, self.element(L.edit.tool_menu.ai_effect.param_value(i + 1)).text)
                    self.click(L.edit.tool_menu.ai_effect.param_value(i + 1))
                    self.driver.drag_slider_from_left_to_right()
                    break
            if not param_flag:
                raise Exception('No parameter can edit in this effect')

            if self.element(L.edit.tool_menu.slider_value).text != default_value[1]:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Param value no change'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.tool_menu.ai_effect.effect(1))
            self.click(L.edit.tool_menu.ai_effect.edit)

            return "FAIL"

    def sce_2_2_9(self):
        uuid = 'b1842e2f-85e1-4733-b66a-e9e9a2709f43'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.tool_menu.ai_effect.reset):
                raise Exception('Click Reset fail')

            if self.element(L.edit.tool_menu.ai_effect.param_value(default_value[0])).text == default_value[1]:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Param value is not equal default value'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.tool_menu.ai_effect.effect(1))
            self.click(L.edit.tool_menu.ai_effect.edit)

            return "FAIL"

    def sce_2_2_10(self):
        uuid = 'aa3241e2-63f4-4e06-b722-d3c751c0aefe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.tool_menu.back):
                raise Exception('Click Back fail')

            if self.is_exist(L.edit.tool_menu.ai_effect.effect()):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No found effect'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.tool_menu.ai_effect.effect(1))


            return "FAIL"

    def sce_2_2_11(self):
        uuid = '9bd61e1e-f41a-4e72-8c8e-0060a3c86afe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.tool_menu.back):
                raise Exception('Tap Back button fail')

            if self.is_exist(L.edit.tool_menu.tool(0)):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No found 2nd layer tool menu'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            return "FAIL"

    def sce_2_2_14(self):
        uuid = '7eb3f4d4-b6a0-464c-a046-3859f69557b5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            global pic_photo_default
            pic_photo_default = self.page_main.get_preview_pic()
            if not self.page_edit.trigger_default_pan_zoom_effect(enable=True):
                raise Exception('Click default_pan_zoom_effect fail')
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)


            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Random')).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_12(self):
        uuid = '6adefecd-8cbd-4164-aa84-9dd4bd06577e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.swipe_element(L.edit.timeline.timeline_ruler, 'left', 300)
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            self.click(find_string('No Effect'))
            if not self.click(L.edit.tool_menu.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('No Effect')).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No Effect is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_13(self):
        uuid = 'd49362dd-6d87-4c27-8d5f-785749caeef2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            self.click(find_string('Random'))
            if not self.click(L.edit.tool_menu.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Random')).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_15(self):
        uuid = '4411db3a-3fdc-461c-930f-793ab72b45a2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.click(L.edit.tool_menu.pan_zoom.custom.apply)
            if not self.click(L.edit.tool_menu.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Custom')).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Custom is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_16(self):
        uuid = '80556c5f-b177-455d-bade-d46c0fa34195'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.scroll_playhead_to_beginning()
            if not self.click(find_string('No Effect')):
                raise Exception('Click No Effect fail')
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are different'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_17(self):
        uuid = 'adc2ccca-482d-4eb7-ac83-5bf5d4de19b7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Random')):
                raise Exception('Click Random fail')
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_19(self):
        uuid = '1b938b47-d9e3-43db-bc7f-93deba4de02f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.driver.swipe_element(L.edit.tool_menu.pan_zoom.custom.start_position, 'up', 100)
            self.click(L.edit.tool_menu.pan_zoom.custom.apply)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_18(self):
        uuid = '2fd0c8b8-59d5-4986-ad84-405637852a86'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:

            if not self.page_edit.trigger_default_pan_zoom_effect(enable=False):
                raise Exception('Disable Pan & Zoom Fail')
            self.page_edit.scroll_playhead_to_beginning()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_20(self):
        uuid = '4a4ad790-5b78-4831-a156-315877f42bb8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.scroll_playhead_to_beginning()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            global pic_video_default
            pic_video_default = self.page_main.get_preview_pic()

            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.click(L.edit.tool_menu.pan_zoom.custom.apply)

            self.driver.swipe_element(L.edit.timeline.timeline_ruler, 'left', 300)
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            self.click(find_string('No Effect'))
            if not self.click(L.edit.tool_menu.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('No Effect')).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No Effect is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_21(self):
        uuid = '5a6815e0-1ac5-48b2-a582-567ebace8f71'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            random_icon = self.element(xpath(f'//*[contains(@text,"Random")]/preceding-sibling::android.widget.ImageView'))
            if not random_icon:
                raise Exception("Cannot locate Random's icon")

            if random_icon.get_attribute('enabled') == 'false':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not disabled'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)

            return "FAIL"

    def sce_2_2_22(self):
        uuid = '415d116b-389c-44f0-bd08-d3ea14ea04de'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.click(L.edit.tool_menu.pan_zoom.custom.apply)
            if not self.click(L.edit.tool_menu.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Custom')).get_attribute('selected') == 'true':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Custom is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_23(self):
        uuid = '60936593-4d5b-4117-9626-a262d693e59e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.scroll_playhead_to_beginning()
            if not self.click(find_string('No Effect')):
                raise Exception('Click No Effect fail')
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_video_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are different'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_24(self):
        uuid = '88b811ec-fcb6-45f3-9480-27a7a68b9cdc'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            random_icon = self.element(xpath(f'//*[contains(@text,"Random")]/preceding-sibling::android.widget.ImageView'))
            if not random_icon:
                raise Exception("Cannot locate Random's icon")

            if random_icon.get_attribute('enabled') == 'false':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not disabled'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_25(self):
        uuid = '822282fc-0374-4534-90d5-902de4e2de66'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.driver.swipe_element(L.edit.tool_menu.pan_zoom.custom.start_position, 'up', 100)
            self.click(L.edit.tool_menu.pan_zoom.custom.apply)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)

            return "FAIL"

    def sce_2_2_26(self):
        uuid = '720154f9-f1e7-4e07-b01a-1b0fe8bcd216'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)
        log = 'Feature removed'
        self.report.new_result(uuid, None, 'N/A', log)
        return 'N/A'

    def sce_2_2_27(self):
        uuid = 'af2a4980-71b7-4181-a105-e978b380bb99'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)
        log = 'Feature removed'
        self.report.new_result(uuid, None, 'N/A', log)
        return 'N/A'

    def sce_2_2_28(self):
        uuid = '343072ee-7556-45fe-bc52-2a8889eed30c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)
        log = 'Feature removed'
        self.report.new_result(uuid, None, 'N/A', log)
        return 'N/A'

    def sce_2_2_31(self):
        uuid = '6cb4e483-d200-4a12-9ae1-14abc04f6d28'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Select clip fail')
            if not self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect'):
                raise Exception('Enter Effect fail')
            if not self.page_edit.click_tool_by_itemName('Beating'):
                raise Exception('Click Beating fail')
            if not self.click(L.edit.tool_menu.effect.edit):
                raise Exception('Click Edit button fail')
            if not self.click(find_string('Frequency')):
                raise Exception('Click Frequency fail')
            value = self.element(L.edit.tool_menu.slider_value).text

            if value == "20":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_30(self):
        uuid = 'fe5e2f0d-ee84-43b7-9bba-1a27df66d71e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.tool_menu.slider_value).text
            self.driver.drag_slider_to_min(L.edit.tool_menu.slider)
            value_after = self.element(L.edit.tool_menu.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_32(self):
        uuid = '7cd0f6de-d928-4319-97f5-c2cb2e66ff7c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.tool_menu.slider_value).text

            if value == "5":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_29(self):
        uuid = '4260b495-a0f0-4ccb-81fc-d816bfd627c6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.tool_menu.slider_value).text
            self.driver.drag_slider_to_max(L.edit.tool_menu.slider)
            value_after = self.element(L.edit.tool_menu.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_33(self):
        uuid = 'b3da4cba-cbe8-49c6-8d1f-5df90e7bef60'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.tool_menu.slider_value).text

            if value == "40":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"

    def sce_2_2_34(self):
        uuid = 'ab490a99-98de-4070-9442-608fe225c520'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Strength')):
                raise Exception('Click Strength fail')
            value = self.element(L.edit.tool_menu.slider_value).text

            if value == "120":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"

    def sce_2_2_35(self):
        uuid = '094cff54-681b-43f6-9bdd-300857c70370'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.tool_menu.slider)
            value = self.element(L.edit.tool_menu.slider_value).text

            if value == "110":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"

    def sce_2_2_36(self):
        uuid = '00a7f2e5-8f0c-467c-a7ae-c4c718ba985b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.tool_menu.slider)
            value = self.element(L.edit.tool_menu.slider_value).text

            if value == "150":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.tool_menu.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"


    def test_case_1(self):
        result = {"sce_2_2_1": self.sce_2_2_1(),
                  "sce_2_2_2": self.sce_2_2_2(),
                  "sce_2_2_3": self.sce_2_2_3(),
                  "sce_2_2_4": self.sce_2_2_4(),
                  "sce_2_2_5": self.sce_2_2_5(),
                  "sce_2_2_6": self.sce_2_2_6(),
                  "sce_2_2_7": self.sce_2_2_7(),
                  "sce_2_2_8": self.sce_2_2_8(),
                  "sce_2_2_9": self.sce_2_2_9(),
                  "sce_2_2_10": self.sce_2_2_10(),
                  "sce_2_2_11": self.sce_2_2_11(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

    def test_case_2(self):
        result = {"sce_2_2_14": self.sce_2_2_14(),
                  "sce_2_2_12": self.sce_2_2_12(),
                  "sce_2_2_13": self.sce_2_2_13(),
                  "sce_2_2_15": self.sce_2_2_15(),
                  "sce_2_2_16": self.sce_2_2_16(),
                  "sce_2_2_17": self.sce_2_2_17(),
                  "sce_2_2_19": self.sce_2_2_19(),
                  "sce_2_2_18": self.sce_2_2_18(),
                  "sce_2_2_20": self.sce_2_2_20(),
                  "sce_2_2_21": self.sce_2_2_21(),
                  "sce_2_2_22": self.sce_2_2_22(),
                  "sce_2_2_23": self.sce_2_2_23(),
                  "sce_2_2_24": self.sce_2_2_24(),
                  "sce_2_2_25": self.sce_2_2_25(),
                  "sce_2_2_26": self.sce_2_2_26(),
                  "sce_2_2_27": self.sce_2_2_27(),
                  "sce_2_2_28": self.sce_2_2_28(),
                  "sce_2_2_31": self.sce_2_2_31(),
                  "sce_2_2_30": self.sce_2_2_30(),
                  "sce_2_2_32": self.sce_2_2_32(),
                  "sce_2_2_29": self.sce_2_2_29(),
                  "sce_2_2_33": self.sce_2_2_33(),
                  "sce_2_2_34": self.sce_2_2_34(),
                  "sce_2_2_35": self.sce_2_2_35(),
                  "sce_2_2_36": self.sce_2_2_36(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")