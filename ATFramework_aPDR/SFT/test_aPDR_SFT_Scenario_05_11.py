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


class Test_SFT_Scenario_05_11:
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

    def sce_5_11_27(self):
        try:
            uuid = 'bfb8aabd-5575-47b4-9838-f0d6429974fa'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()
            self.page_edit.intro_video.edit_1st_template()
            self.page_edit.intro_video.customize()
            self.page_edit.click_tool('Add')
            self.page_edit.click_sub_tool('Photo')
            self.page_media.select_local_photo(self.test_material_folder, 'photo.jpg')
            self.page_edit.click_sub_tool('Flip')
            pic_tgt = self.page_main.get_picture(L.edit.pip.pip_object)
            pic_src = path.join(path.dirname(__file__), 'test_material', '05_11', '5_11_27.png')

            if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96:
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
    def test_sce_05_11_27(self):
        result = {"sce_5_11_27": self.sce_5_11_27(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")