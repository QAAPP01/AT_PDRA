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
from .conftest import TEST_MATERIAL_FOLDER_01

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_06_05:
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
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01
                                                              
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
    def test_sce_06_05_01(self):
        logger('>>> test_sce_06_05_01 : Sample Projects <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        self.report.start_uuid('79a75a2c-9892-47f7-8239-614f75b47cf8')
        time.sleep(5)
        page_main.swipe_main_page('up', 1)
        result = page_main.is_exist(L.main.sample_projects.list)
        self.report.new_result('79a75a2c-9892-47f7-8239-614f75b47cf8', result)

        self.report.start_uuid('c0591c2d-ce72-435e-992d-45caa3ebafbe')
        time.sleep(10)
        result = page_main.check_sample_projects_thumbnails()
        self.report.new_result('c0591c2d-ce72-435e-992d-45caa3ebafbe', result)

        self.report.start_uuid('9c828d42-5358-478c-964f-6a3aec00d23e')
        amount = page_main.calculate_sample_projects_amount()
        result = True if not amount == 0 else False
        self.report.new_result('9c828d42-5358-478c-964f-6a3aec00d23e', result)

        self.report.start_uuid('521aa32c-f667-4611-8eb1-db36dcd56fdd')
        self.report.start_uuid('1d4ae95c-b58a-4719-b50b-1044603f439b')
        page_main.swipe_sample_projects_list('right', 10)
        result = page_main.select_sample_project('Effect')
        self.report.new_result('521aa32c-f667-4611-8eb1-db36dcd56fdd', result)
        self.report.new_result('1d4ae95c-b58a-4719-b50b-1044603f439b', result)

        self.report.start_uuid('24c00042-5796-4c0d-9d75-05d69f653954')
        result = page_edit.check_premium_features_used()
        self.report.new_result('24c00042-5796-4c0d-9d75-05d69f653954', result)

        self.report.start_uuid('10bb663b-71ef-4b51-9dc2-01b5be71acce')
        page_edit.click(L.edit.menu.produce)
        time.sleep(5)
        result = True if page_edit.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('10bb663b-71ef-4b51-9dc2-01b5be71acce', result)

