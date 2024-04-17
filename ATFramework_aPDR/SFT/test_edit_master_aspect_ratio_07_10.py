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


class Test_Import_Stock_Filter:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "151e1c57-f2e2-47f8-8669-14f7d86bfb36",
            "0bc56cba-9ee9-499d-8499-e58c2b90f702",
            "d5acb1cd-5810-44d8-ba0e-571c988a7ae4",
            "2e869d26-d734-476c-a948-8fb7bcf3b64b",
            "42d6c14a-c2d9-4d54-a888-85c6337e33e4",
            "9e04fdc7-beb5-442f-be6f-bedb66909e8f",
            "c0edb49c-02f5-4fcb-a404-3488077f466c"
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
        self.is_not_exist = self.page_main.h_is_not_exist

        report.set_driver(driver)
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def sce_7_10_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            if self.is_exist(L.edit.aspect_ratio.ratio_16_9):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Enter aspect ratio failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            return "FAIL"

    def sce_7_10_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.toolbar.back)
            self.page_edit.click_tool("Aspect Ratio")

            if self.is_exist(L.edit.aspect_ratio.ratio_16_9):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Enter aspect ratio failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            return "FAIL"

    def sce_7_10_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.aspect_ratio.ratio_16_9)
            ratio = self.page_edit.preview_ratio()

            if ratio == "16:9":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Ratio not match: {ratio}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            return "FAIL"

    def sce_7_10_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.aspect_ratio.ratio_9_16)
            ratio = self.page_edit.preview_ratio()

            if ratio == "9:16":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Ratio not match: {ratio}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            return "FAIL"

    def sce_7_10_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.aspect_ratio.ratio_1_1)
            ratio = self.page_edit.preview_ratio()

            if ratio == "1:1":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Ratio not match: {ratio}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            return "FAIL"

    def sce_7_10_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.aspect_ratio.ratio_21_9)
            ratio = self.page_edit.preview_ratio()

            if ratio == "21:9":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Ratio not match: {ratio}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            return "FAIL"

    def sce_7_10_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.aspect_ratio.ratio_4_5)
            ratio = self.page_edit.preview_ratio()

            if ratio == "4:5":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Ratio not match: {ratio}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {
            "sce_7_10_1": self.sce_7_10_1(),
            "sce_7_10_2": self.sce_7_10_2(),
            "sce_7_10_3": self.sce_7_10_3(),
            "sce_7_10_4": self.sce_7_10_4(),
            "sce_7_10_5": self.sce_7_10_5(),
            "sce_7_10_6": self.sce_7_10_6(),
            "sce_7_10_7": self.sce_7_10_7()
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
