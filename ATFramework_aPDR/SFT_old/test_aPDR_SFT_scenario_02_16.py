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


class Test_SFT_Scenario_02_16:
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
    def test_sce_02_16_01(self):
        logger('>>> test_sce_02_16_01: New Music Library <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.subscribe()
        
        # New project
        self.report.start_uuid('5d9cb4c0-d1cd-48ef-a737-371e12c5a79a')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_16_01")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.switch_to_music_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Music')
        time.sleep(5)
        page_media.select_media_by_text('Audio Logos')
        time.sleep(5)
        page_media.select_media_by_text('Action Audio Logo')
        time.sleep(3)
        result = page_media.download_music()
        self.report.new_result('5d9cb4c0-d1cd-48ef-a737-371e12c5a79a', result)

        self.report.start_uuid('383ba349-cb31-4a59-a39c-fe42ea9ce021')
        page_edit.back()
        time.sleep(5)
        page_media.search_video('24')
        time.sleep(10)
        page_media.select_media_by_text('24/7')
        time.sleep(5)
        result = page_media.download_music()
        self.report.new_result('383ba349-cb31-4a59-a39c-fe42ea9ce021', result)

        self.report.start_uuid('1af3bc1e-b7b1-4ede-8176-d963a6e2d501')
        page_edit.back()
        time.sleep(5)
        page_media.select_media_by_text('Audio Logos')
        time.sleep(5)
        page_media.search_video('lake')
        time.sleep(10)
        page_media.select_media_by_text('Lake Logo')
        time.sleep(5)
        result = page_media.download_music()
        self.report.new_result('1af3bc1e-b7b1-4ede-8176-d963a6e2d501', result)

        # Preview
        self.report.start_uuid('7288a45f-0fa8-42fa-8cb4-734ac0f0c48b')
        page_edit.back()
        time.sleep(5)
        page_media.select_media_by_text('Audio Logos')
        time.sleep(5)
        page_media.search_video('lake')
        time.sleep(10)
        page_media.select_media_by_text('Lake Logo')
        time.sleep(5)
        result = page_media.download_music()
        self.report.new_result('7288a45f-0fa8-42fa-8cb4-734ac0f0c48b', result)

