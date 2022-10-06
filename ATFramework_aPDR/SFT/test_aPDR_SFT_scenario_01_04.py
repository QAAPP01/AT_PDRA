import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
from ATFramework.utils.compare_Mac import CompareImage
import pytest
import time

from pages.locator import locator as L

from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
report = REPORT_INSTANCE

pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER


class Test_SFT_Scenario_01_04:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver sessioin>============')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        logger(f"desired_caps={desired_caps}")
        self.report = report
        self.device_udid = DRIVER_DESIRED_CAPS['udid']
        # ---- local mode > end ----
        self.test_material_folder = test_material_folder
                                                              
        # retry 3 time if craete driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',desired_caps)
                if self.driver:
                    logger("driver created!")
                    break
                else:
                    raise Exception("create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
                
        self.report.set_driver(self.driver)
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(15)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_04_01(self):
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        logger('Change Edit UI Mode - v10.1.0')
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        self.report.start_uuid('c3410853-f64a-49a8-9e82-ac0b2e42dcaf')
        page_main.enter_settings_from_main()
        page_edit.settings.swipe_to_option('Change UI Edit Mode')
        page_timeline_settings.select_ui_mode_radio('Portrait')
        page_edit.back()
        current_mode = page_timeline_settings.get_selected_ui_mode()
        result = True if current_mode == 'Portrait' else False
        self.report.new_result('c3410853-f64a-49a8-9e82-ac0b2e42dcaf', result)

        self.report.start_uuid('1c8e65a8-8de5-4853-ba25-ef0789b35c33')
        page_timeline_settings.select_ui_mode_radio('Auto-rotate')
        page_edit.back()
        current_mode = page_timeline_settings.get_selected_ui_mode()
        result = True if current_mode == 'Auto-rotate' else False
        self.report.new_result('1c8e65a8-8de5-4853-ba25-ef0789b35c33', result)

        self.report.start_uuid('d6381ed1-92fc-45b0-a3e9-46dbbc9e50bb')
        page_timeline_settings.select_ui_mode_radio('Landscape')
        page_edit.back()
        current_mode = page_timeline_settings.get_selected_ui_mode()
        result = True if current_mode == 'Landscape' else False
        self.report.new_result('d6381ed1-92fc-45b0-a3e9-46dbbc9e50bb', result)