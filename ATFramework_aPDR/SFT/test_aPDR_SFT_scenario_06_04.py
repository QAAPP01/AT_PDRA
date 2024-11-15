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


from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01


pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_06_04:
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
    
    def test_sce_06_04_01(self):
        logger('>>> test_sce_06_04_01 : CSE Sign in <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        self.report.start_uuid('bb0e232d-c201-4a7b-a2e0-587a89c38fca')
        self.report.start_uuid('00e3e5a4-e399-46ac-b205-7ad32c9b346a')
        page_main.enter_settings_from_main()
        result = page_main.sign_in_cyberlink_account()
        self.report.new_result('bb0e232d-c201-4a7b-a2e0-587a89c38fca', result)
        self.report.new_result('00e3e5a4-e399-46ac-b205-7ad32c9b346a', result)

        self.report.start_uuid('503bf1ee-84c5-4ee9-a6da-4b5c9a160720')
        page_main.click(L.timeline_settings.settings.back)
        result = True if not page_edit.is_exist(L.launcher.project.shopping_cart, 0) else False
        self.report.new_result('503bf1ee-84c5-4ee9-a6da-4b5c9a160720', result)

        self.report.start_uuid('cde33cec-4722-40bb-90a5-ca4802523445')
        page_main.swipe_main_page('down', 5)
        result = True if not page_edit.is_exist(id('admob_native_ad_media'), 0) else False
        self.report.new_result('cde33cec-4722-40bb-90a5-ca4802523445', result)

        self.report.start_uuid('53b13bbb-c915-49da-95b6-4e9657519891')
        page_main.select_existed_project_by_title(project_title)
        # page_edit.click(L.main.project_info.btn_edit_project)
        time.sleep(5)
        result = True if not page_edit.is_exist(L.edit.preview.watermark, 0) else False
        self.report.new_result('53b13bbb-c915-49da-95b6-4e9657519891', result)

        self.report.start_uuid('e1b556c0-1d64-437b-b9bf-c932f1aab766')
        page_edit.click(L.edit.menu.export)
        page_produce.select_produce_type('gallery')
        page_produce.set_resolution(1)
        time.sleep(5)
        result = True if not page_edit.is_exist(L.launcher.subscribe.back_btn, 0) else False
        self.report.new_result('e1b556c0-1d64-437b-b9bf-c932f1aab766', result)

        self.driver.stop_app(pdr_package)
        self.driver.start_app(pdr_package)
        page_produce.ad.close_opening_ads()
        page_main.enter_settings_from_main()
        page_main.sign_out_cyberlink_account()