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
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE

file_video = 'video.mp4'
file_photo = 'photo.jpg'


class Test_SFT_Scenario_06_02:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", driver)
        self.page_ai_effect = PageFactory().get_page_object("ai_effect", driver)
        self.page_media = PageFactory().get_page_object("import_media", driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        self.report.set_driver(driver)
        driver.driver.launch_app()

    def sce_6_4_70(self):
        uuid = '19a47ca2-91a4-40cb-a7ed-481baa667804'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.enter_free_template_media_picker()
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
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            return "ERROR"

    def sce_6_4_71(self):
        uuid = '4bcad19b-ad8b-48c8-a2bb-1ba5c9ec4be6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)
            self.page_media.select_photo_library("google_drive")
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
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            return "ERROR"


    @report.exception_screenshot
    def test_sce_6_1_1_to_135(self):
        result = {"sce_6_4_70": self.sce_6_4_70(),
                  "sce_6_4_71": self.sce_6_4_71(),

                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")