import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from main import deviceName
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

file_video = 'video.mp4'
file_photo = 'jpg.jpg'


class Test_SFT_Scenario_02_02:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

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
            if not self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo):
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
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

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", self.test_material_folder, file_photo)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
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