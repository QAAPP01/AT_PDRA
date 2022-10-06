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

class Test_SFT_Scenario_06_09:
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
    def test_sce_06_09_01(self):
        logger('>>> test_sce_06_09_01 : Premium Link/Icon <<<')
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
        
        page_main.subscribe()

        self.report.start_uuid('99a2e6d2-0995-4379-8e7e-a5a29d96250d')
        self.report.start_uuid('b5886642-5318-4908-b437-57792d553009')
        page_main.select_existed_project_by_title(project_title)
        time.sleep(5)
        page_main.back()
        time.sleep(5)
        result = page_main.check_premium_label()
        self.report.new_result('99a2e6d2-0995-4379-8e7e-a5a29d96250d', result)
        self.report.new_result('b5886642-5318-4908-b437-57792d553009', result)
        
        self.report.start_uuid('aef350c3-18b9-4cf1-90ab-ce41c912d45e')
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(5)
        result = page_edit.settings.swipe_to_option('Premium Feature/Template Icon')
        page_edit.back()
        self.report.new_result('aef350c3-18b9-4cf1-90ab-ce41c912d45e', not result)
        
        self.report.start_uuid('768c75d8-3b26-45d3-b3df-cc8929b19d72')
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        result = page_edit.is_exist(L.main.premium.icon_library_lock)
        self.report.new_result('768c75d8-3b26-45d3-b3df-cc8929b19d72', not result)        
        
        self.report.start_uuid('8e05043a-c017-4629-b83e-f3805e754ba2')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        result = page_edit.is_exist(L.main.premium.icon_tool_premium)
        self.report.new_result('8e05043a-c017-4629-b83e-f3805e754ba2', not result)
        
        self.report.start_uuid('c7055132-f723-4662-829f-eec0deef15ec')
        self.report.start_uuid('50defc2b-9f4e-49a9-ace9-430a9354e84a')
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.switch_to_pip_video_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        result = page_main.check_video_overlay_limit_message()
        self.report.new_result('c7055132-f723-4662-829f-eec0deef15ec', result)
        self.report.new_result('50defc2b-9f4e-49a9-ace9-430a9354e84a', result)
        
        