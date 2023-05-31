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


class Test_SFT_Scenario_05_08:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
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

    def sce_5_8_24(self):
        try:
            uuid = '5841c726-6358-4715-826c-bbcde03e926b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()
            self.page_edit.intro_video.edit_favorite_template()
            self.page_edit.intro_video.customize()
            self.page_edit.click_tool('Media')
            self.page_edit.click_sub_tool('Rotate')
            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '05_08', '5_8_24.png')

            if HCompareImg(pic_tgt, pic_src).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_5_8_25(self):
        try:
            uuid = 'f81a3deb-4a14-42c1-93a7-8a76e703210a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool('Media')
            self.page_edit.click_sub_tool('Flip')
            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '05_08', '5_8_25.png')

            if HCompareImg(pic_tgt, pic_src).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_5_8_24_25(self):
        result = {"sce_5_8_24": self.sce_5_8_24(),
                  "sce_5_8_25": self.sce_5_8_25(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
