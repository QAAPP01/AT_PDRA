import inspect
import sys, os, glob
from os.path import dirname
from os import path
import subprocess
from pprint import pprint
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *

from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.ATFramework.utils.log import logger
import pytest
import time

from main import deviceName
from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

class Test_SFT_Scenario_01_04:
    @pytest.fixture(autouse=True)
    def initial(self):

        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger("[Start] Init driver session")
        desired_caps = {}
        desired_caps.update(app_config.cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        if desired_caps['udid'] == 'auto':
            desired_caps['udid'] = deviceName
        logger(f"[Info] caps={desired_caps}")
        self.report = report
        self.device_udid = desired_caps['udid']
        # ---- local mode > end ----
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

        # retry 3 time if create driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                                       desired_caps)
                if self.driver:
                    logger("\n[Done] Driver created!")
                    break
                else:
                    raise Exception("\n[Fail] Create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
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

        self.report.set_driver(self.driver)
        self.driver.driver.start_recording_screen()
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(0.1)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Stop] Teardown")
        self.driver.stop_driver()

    def sce_01_04_01(self):
        uuid = 'c3410853-f64a-49a8-9e82-ac0b2e42dcaf'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        mode_setting = self.page_main.change_UI_mode("portrait")
        self.driver.driver.orientation = "LANDSCAPE"
        self.page_main.enter_timeline()
        orientation = self.driver.driver.orientation
        self.page_edit.back_to_launcher()

        if mode_setting == "portrait" and orientation == "PORTRAIT":
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] mode_setting = {mode_setting}, orientation = {orientation}'
            logger(fail_log)

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_04_02(self):
        uuid = 'd6381ed1-92fc-45b0-a3e9-46dbbc9e50bb'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        mode_setting = self.page_main.change_UI_mode("landscape")
        self.driver.driver.orientation = "PORTRAIT"
        self.page_main.enter_timeline()
        orientation = self.driver.driver.orientation
        self.page_edit.back_to_launcher()

        if mode_setting == "landscape" and orientation == "LANDSCAPE":
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] mode_setting = {mode_setting}, orientation = {orientation}'
            logger(fail_log)

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_04_03(self):
        uuid = '1c8e65a8-8de5-4853-ba25-ef0789b35c33'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        # auto_portrait
        mode_setting = self.page_main.change_UI_mode("auto-rotate")
        self.driver.driver.orientation = "PORTRAIT"
        self.page_main.enter_timeline(skip_media=False)
        orientation = self.driver.driver.orientation
        self.click(L.import_media.menu.back)

        if mode_setting == "auto-rotate" and orientation == "PORTRAIT":
            result_portrait = True
        else:
            result_portrait = False
            logger(f'\n[Fail] mode_setting = {mode_setting}, orientation = {orientation}')

        # auto_landscape
        self.page_edit.back_to_launcher()
        mode_setting = self.page_main.change_UI_mode("auto-rotate")
        self.driver.driver.orientation = "LANDSCAPE"
        self.page_main.enter_timeline(skip_media=False)
        orientation = self.driver.driver.orientation

        if mode_setting == "auto-rotate" and orientation == "LANDSCAPE":
            result_landscape = True
        else:
            result_landscape = False
            logger(f'\n[Fail] mode_setting = {mode_setting}, orientation = {orientation}')

        if result_portrait and result_landscape:
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] result_portrait = {result_portrait}, result_landscape = {result_landscape}'
            logger(fail_log)

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    @report.exception_screenshot
    def test_sce_01_04_01_to_03(self):
        try:
            result = {
                "sce_01_04_01": self.sce_01_04_01(),
                "sce_01_04_02": self.sce_01_04_02(),
                "sce_01_04_03": self.sce_01_04_03()
            }
            pprint(result)
        except Exception as err:
            logger(f'[Error] {err}')
