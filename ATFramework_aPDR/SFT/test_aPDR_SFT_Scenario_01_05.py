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


class Test_SFT_Scenario_01_05:
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

    def sce_01_05_01(self):
        uuid = '45479986-4700-48e9-af00-d889b3ec09e0'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(skip_media=False)
        self.click(L.import_media.media_library.btn_preview())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_02(self):
        uuid = '2cce56be-b6a5-4655-9c3e-a022085ebdfe'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.long_press(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_03(self):
        uuid = '6821d9a8-3839-4921-8323-5ee9b8c6c4a8'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.shutter_stock)
        self.click(L.import_media.media_library.btn_preview())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_04(self):
        uuid = '5e99435d-14bd-484e-8384-ba2bf5276c94'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.shutter_stock)
        self.long_press(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_05(self):
        uuid = '9b1af418-19cd-4ae0-81c6-a40da8c8ec84'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.getty)
        self.click(L.import_media.media_library.btn_preview())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_06(self):
        uuid = '8335bee7-4b82-44b5-8682-4a7077d35495'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.getty)
        self.long_press(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_07(self):
        uuid = 'f143d1a6-7761-478a-96f7-842b9cb01254'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.getty_pro)
        self.click(L.import_media.media_library.btn_preview())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_08(self):
        uuid = '78f56ea6-74f9-4833-b9ec-e76ea0a61bfb'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.getty_pro)
        self.long_press(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_09(self):
        uuid = '6014c97f-91d4-42ff-af47-119a13ee90a5'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.giphy)

        if not self.is_exist(L.import_media.media_library.btn_preview()):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_10(self):
        uuid = '74e2d6cf-28d2-4c0f-9d2c-74183ca10472'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.giphy)
        self.long_press(L.import_media.media_library.media())

        if not self.is_exist(L.import_media.media_library.Video.display_preview):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_11(self):
        uuid = 'f44f57f1-ca9f-4d4c-b359-ae7446bcb1f8'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.pexels)
        self.click(L.import_media.media_library.btn_preview())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_12(self):
        uuid = 'f953d5d4-fd9b-4dd3-9014-c9896e356d63'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.pexels)
        self.long_press(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_13(self):
        uuid = 'f84c3132-2e68-49c5-bd1a-1d25ad3f6289'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.media_library.creator_page)

        if self.is_exist(find_string("pexels.com/@")):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Cannot find "pexels.com/@"'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_14(self):
        uuid = '87def98e-a0df-4769-a56c-dc1c90c68bc7'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.pixabay)
        self.click(L.import_media.media_library.btn_preview())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_05_15(self):
        uuid = '481cecde-a89e-466f-978b-72552512d9fd'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_media.select_video_library(L.import_media.media_library.Video.pixabay)
        self.long_press(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)

        if self.is_exist(L.import_media.media_library.Video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_05_01_to_12(self):
        result = {
            "sce_01_05_01": self.sce_01_05_01(),
            "sce_01_05_02": self.sce_01_05_02(),
            "sce_01_05_03": self.sce_01_05_03(),
            "sce_01_05_04": self.sce_01_05_04(),
            "sce_01_05_05": self.sce_01_05_05(),
            "sce_01_05_06": self.sce_01_05_06(),
            "sce_01_05_07": self.sce_01_05_07(),
            "sce_01_05_08": self.sce_01_05_08(),
            "sce_01_05_09": self.sce_01_05_09(),
            "sce_01_05_10": self.sce_01_05_10(),
            "sce_01_05_11": self.sce_01_05_11(),
            "sce_01_05_12": self.sce_01_05_12(),
            "sce_01_05_13": self.sce_01_05_13(),
            "sce_01_05_14": self.sce_01_05_14(),
            "sce_01_05_15": self.sce_01_05_15(),
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[FAIL] {key}")
