import pytest, os, inspect, base64, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER

class Test_SFT_Scenario_01_04:
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
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        driver.driver.close_app()
        driver.driver.orientation = "PORTRAIT"


    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')


    def sce_01_04_01(self):
        uuid = 'c3410853-f64a-49a8-9e82-ac0b2e42dcaf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            mode_setting = self.page_main.change_UI_mode("portrait")
            self.driver.driver.orientation = "LANDSCAPE"
            self.page_main.enter_timeline()
            orientation = self.driver.driver.orientation
            self.page_edit.back_to_launcher()

            if mode_setting == "portrait" and orientation == "PORTRAIT":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'\n[Fail] mode_setting = {mode_setting}, orientation = {orientation}')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            return "FAIL"

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

    def test_case(self):
        result = {
                "sce_01_04_01": self.sce_01_04_01(),
                "sce_01_04_02": self.sce_01_04_02(),
                "sce_01_04_03": self.sce_01_04_03()
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

    def test_case1(self):
        result = {
                "sce_01_04_01": self.sce_01_04_01(),

                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

