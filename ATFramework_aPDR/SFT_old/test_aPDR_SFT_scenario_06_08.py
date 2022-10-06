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
add_package = 'com.cyberlink.addirector'

class Test_SFT_Scenario_06_08:
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
    def test_sce_06_08_01(self):
        logger('>>> test_sce_06_08_01 : Cross promotion <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        self.report.start_uuid('b8e6f7c5-bd3c-4553-868e-beb3e69fe336')
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.switch_to_template_library()
        time.sleep(5)
        page_media.select_template_category('Simple')
        result = page_media.search_add_template_by_image('add_simple')
        self.report.new_result('b8e6f7c5-bd3c-4553-868e-beb3e69fe336', result)
        
        self.report.start_uuid('b1578495-bd12-418b-96f4-bb9746de7c2d')
        time.sleep(10)
        time.sleep(10)
        time.sleep(10)
        result = page_media._terminate_app(add_package)
        time.sleep(10)
        self.report.new_result('b1578495-bd12-418b-96f4-bb9746de7c2d', result)
  
  
        self.report.start_uuid('44971762-7c45-4284-866e-f8a269a2da7a')
        
        self.report.start_uuid('c80703f1-56d8-4af9-8ef0-c3215734f849')
        page_media.select_template_category('Marketing')
        result = page_media.search_add_template_by_image('add_1')
        time.sleep(10)
        time.sleep(10)
        result1 = page_media._terminate_app(add_package)
        time.sleep(10)
        time.sleep(10)
        self.report.new_result('c80703f1-56d8-4af9-8ef0-c3215734f849', result and result1)        
        
        self.report.start_uuid('8426c09b-9ebb-416f-b463-949c7d56146f')
        page_media.select_template_category('Marketing')
        result = page_media.search_add_template_by_image('add_2')
        time.sleep(10)
        time.sleep(10)
        result2 = page_media._terminate_app(add_package)
        time.sleep(10)
        time.sleep(10)
        self.report.new_result('8426c09b-9ebb-416f-b463-949c7d56146f', result and result2)       
        
        self.report.start_uuid('456ea071-5fac-46c6-91a3-c1c470d7b4dd')
        page_media.select_template_category('Marketing')
        result = page_media.search_add_template_by_image('add_3')
        time.sleep(10)
        time.sleep(10)
        result3 = page_media._terminate_app(add_package)
        time.sleep(10)
        time.sleep(10)
        self.report.new_result('456ea071-5fac-46c6-91a3-c1c470d7b4dd', result and result3)       
        
        self.report.start_uuid('6f73a577-35ae-4026-b19d-27bbce0397f2')
        page_media.select_template_category('Marketing')
        result = page_media.search_add_template_by_image('add_4')
        time.sleep(10)
        time.sleep(10)
        result4 = page_media._terminate_app(add_package)
        time.sleep(10)
        time.sleep(10)
        self.report.new_result('6f73a577-35ae-4026-b19d-27bbce0397f2', result and result4)       
        
        self.report.start_uuid('dfc72c0e-4157-4e3d-ba2e-538a416304d8')
        page_media.select_template_category('Marketing')
        result = page_media.search_add_template_by_image('add_5')
        time.sleep(10)
        time.sleep(10)
        result5 = page_media._terminate_app(add_package)
        time.sleep(10)
        time.sleep(10)
        self.report.new_result('dfc72c0e-4157-4e3d-ba2e-538a416304d8', result and result5) 
        
        self.report.start_uuid('3b0c74c9-1a6c-4965-8b8e-eb89abdf78b9')
        page_media.select_template_category('Marketing')
        result = page_media.search_add_template_by_image('add_6')
        time.sleep(10)
        time.sleep(10)
        result6 = page_media._terminate_app(add_package)
        time.sleep(10)
        time.sleep(10)
        self.report.new_result('3b0c74c9-1a6c-4965-8b8e-eb89abdf78b9', result and result6)
        
        self.report.new_result('44971762-7c45-4284-866e-f8a269a2da7a', result1 and result2 and result3 and result4 and result5 and result6)