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


class Test_SFT_Scenario_04_12:
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

    def sce_4_12_90(self):
        try:
            uuid = 'e6ce5712-3727-461d-b755-90bc5ae93e97'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            while not self.is_exist(L.import_media.media_library.media(), 1):
                time.sleep(1)
            global pic_all
            pic_all = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 10):
                time.sleep(1)
            self.click(L.import_media.media_library.btn_preview())
            while self.is_exist(L.import_media.media_library.loading_circle, 1):
                time.sleep(1)
            rect = self.element(L.import_media.media_library.video.videoDisplay).rect

            if rect["height"] > rect["width"]:
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                self.driver.driver.back() 
                result = False
                fail_log = f'\n[Fail] Orientation incorrect, height: {rect["height"]}, width: {rect["width"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_4_12_91(self):
        try:
            uuid = '64ab5b20-5a8e-4189-80ec-83b6f5da2c19'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 10):
                time.sleep(1)
            self.click(L.import_media.media_library.btn_preview())
            while self.is_exist(L.import_media.media_library.loading_circle, 1):
                time.sleep(1)
            rect = self.element(L.import_media.media_library.Video.display_preview).rect

            if rect["height"] < rect["width"]:
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                self.driver.driver.back()
                result = False
                fail_log = f'\n[Fail] Orientation incorrect, height: {rect["height"]}, width: {rect["width"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_4_12_92(self):
        try:
            uuid = '42e359c4-59ab-4233-8843-ae916d55ec13'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_square)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 10):
                time.sleep(1)
            self.click(L.import_media.media_library.btn_preview())
            while self.is_exist(L.import_media.media_library.loading_circle, 1):
                time.sleep(1)
            rect = self.element(L.import_media.media_library.Video.display_preview).rect

            if rect["height"] == rect["width"]:
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                self.driver.driver.back() 
                result = False
                fail_log = f'\n[Fail] Orientation incorrect, height: {rect["height"]}, width: {rect["width"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_4_12_93(self):
        try:
            uuid = 'cdd2739c-a665-441d-829c-2e57f5c17a7b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 10):
                time.sleep(1)
            pic_tgt = self.page_main.h_full_screenshot()

            if HCompareImg(pic_tgt, pic_all).full_compare() > 0.98:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images not the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_4_12_94(self):
        try:
            uuid = 'ec9a9973-0c65-4705-8e04-4da068385302'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_media.select_photo_library("pexels")
            while not self.is_exist(L.import_media.media_library.media(), 1):
                time.sleep(1)
            global pic_all
            pic_all = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 10):
                time.sleep(1)
            self.click(L.import_media.media_library.btn_preview())
            while self.is_exist(L.import_media.media_library.loading_circle, 1):
                time.sleep(1)
            rect = self.element(L.import_media.media_library.photo.display_preview).rect

            if rect["height"] > rect["width"]:
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                self.driver.driver.back() 
                result = False
                fail_log = f'\n[Fail] Orientation incorrect, height: {rect["height"]}, width: {rect["width"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_4_12_95(self):
        try:
            uuid = '06cc1673-aad7-48a3-8946-1061cb0b0609'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 10):
                time.sleep(1)
            self.click(L.import_media.media_library.btn_preview())
            while self.is_exist(L.import_media.media_library.loading_circle, 1):
                time.sleep(1)
            rect = self.element(L.import_media.media_library.photo.display_preview).rect

            if rect["height"] < rect["width"]:
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                self.driver.driver.back() 
                result = False
                fail_log = f'\n[Fail] Orientation incorrect, height: {rect["height"]}, width: {rect["width"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_4_12_96(self):
        try:
            uuid = '7aefd9a0-bd00-4157-96a8-8891d8a7eb15'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_square)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 10):
                time.sleep(1)
            self.click(L.import_media.media_library.btn_preview())
            while self.is_exist(L.import_media.media_library.loading_circle, 1):
                time.sleep(1)
            rect = self.element(L.import_media.media_library.photo.display_preview).rect

            if rect["height"] == rect["width"]:
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                self.driver.driver.back() 
                result = False
                fail_log = f'\n[Fail] Orientation incorrect, height: {rect["height"]}, width: {rect["width"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_4_12_97(self):
        try:
            uuid = 'ece0b838-cd8b-4752-8eb0-b26e7119b288'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            while self.is_exist(L.import_media.media_library.waiting_cursor, 1):
                time.sleep(10)
            pic_tgt = self.page_main.h_full_screenshot()

            if HCompareImg(pic_tgt, pic_all).full_compare() > 0.98:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images not the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_4_12_90_to_97(self):
        result = {
            "sce_4_12_90": self.sce_4_12_90(),
            "sce_4_12_91": self.sce_4_12_91(),
            "sce_4_12_93": self.sce_4_12_93(),
            "sce_4_12_94": self.sce_4_12_94(),
            "sce_4_12_95": self.sce_4_12_95(),
            "sce_4_12_96": self.sce_4_12_96(),
            "sce_4_12_97": self.sce_4_12_97(),
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[FAIL] {key}")
