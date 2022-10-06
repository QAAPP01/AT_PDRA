import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest
import time
import os

from pages.locator import locator as L

from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
report = REPORT_INSTANCE

pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER
package_path = os.path.dirname(os.path.dirname(__file__)) + r"\app\PowerDirector.apk"

class Test_SFT_Scenario_00_01a:
    @classmethod
    def setup_class(cls):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver session>============')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        #desired_caps.update(app_config.prod_fullreset_cap)
        desired_caps.update(app_config.native_settings_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        logger(f"desired_caps={desired_caps}")
        logger("connect to report instance")
        cls.report = report
        logger("set udid")
        cls.device_udid = DRIVER_DESIRED_CAPS['udid']
        # ---- local mode > end ----
        logger("set testing material path")
        cls.test_material_folder = test_material_folder
        
                                                              
        # retry 10 time if craete driver fail
        retry = 10
        while retry:
            try:
                logger("creating driver.")
                cls.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',desired_caps)
                if cls.driver:
                    logger("driver created!")
                    break
                else:
                    raise Exception("create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
        else:
            logger("[ERROR] Unable to create driver, exit now")
            os._exit(1)
                
        #cls.report.set_driver(cls.driver)
        cls.driver.implicit_wait(15)

    def remove_pdr_projects(self):
        import subprocess
        logger('\n============<remove_pdr_projects>============')
        try:
            command = f'adb -s {self.device_udid} shell rm -r "storage/emulated/0/PowerDirector/projects"'
            subprocess.call(command)
        except Exception:
            pass
        return True

    @classmethod
    def teardown_class(cls):
        logger('\n============<Teardown>============')
        cls.driver.stop_driver()

    def setup_method(self, method):
        logger('\n============<Setup Method>============')
        self.remove_pdr_projects()
        #self.driver.start_app(pdr_package)

    def teardown_method(self, method):
        logger('\n============<TearDown Method>============')
        #self.driver.stop_app(pdr_package)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_00_01_01a(self):
        logger('[V] Install and reset app')
        self.driver.remove_app(pdr_package)
        logger(f'package path={package_path}')
        self.driver.install_app(package_path, pdr_package)


class Test_SFT_Scenario_00_01b:
    @classmethod
    def setup_class(cls):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        from .conftest import REPORT_INSTANCE
        global report
        logger('\n============<Init driver session>============')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        #desired_caps.update(app_config.prod_install_cap)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        logger(f"desired_caps={desired_caps}")
        cls.report = REPORT_INSTANCE
        # ---- local mode > end ----
        cls.test_material_folder = test_material_folder
        cls.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                              desired_caps)
        cls.report.set_driver(cls.driver)
        cls.driver.implicit_wait(15)
        cls.driver.reset_app(pdr_package)

    @classmethod
    def teardown_class(cls):
        logger('\n============<Teardown>============')
        cls.driver.stop_driver()

    def setup_method(self, method):
        logger('\n============<Setup Method>============')
        self.driver.start_app(pdr_package)

    def teardown_method(self, method):
        logger('\n============<TearDown Method>============')
        self.driver.stop_app(pdr_package)

    @pytest.fixture(name='set_permission')
    def set_permission(self):
        page_main = PageFactory().get_page_object("main_page", self.driver)
        logger('[V] Set Permission')
        logger('[Permission] Confirm GDPR')
        if page_main.exist_click(L.main.permission.gdpr_accept,5): # Android version  < 6 or locate in EU
            logger("[Permission] GDPR found and closed")
        page_main.is_exist(L.main.permission.file_ok, 120)
        page_main.el(L.main.permission.file_ok).click()
        page_main.el(L.main.permission.photo_allow).click()
        page_main.check_open_tutorial()
    
    #@pytest.mark.skip
    @pytest.mark.usefixtures('set_permission')
    @report.exception_screenshot
    def test_sce_00_01_01(self):
        #Tips_Edit Page
        #self.report.start_uuid(udid[1])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        time.sleep(15)
        page_main.check_open_tutorial()
        page_main.project_click_new()
        page_main.project_set_name("sce_00_01_01")
        page_main.project_set_9_16()  
        page_main.project_set_to_landscape_mode()  
        logger('[V] Tips_Edit Page')
        page_media = PageFactory().get_page_object("import_media", self.driver)
        
        time.sleep(10)
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        
        page_media.el(L.import_media.video_library.back).click()
        page_media.el(L.import_media.video_library.back).click()

        page_edit.el(L.edit.menu.play).click()
        page_edit.close_full_screen_preview_tip()
        time.sleep(5)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(5)
        # page_edit.settings.swipe_to_option('Advanced')
        page_edit.settings.swipe_to_option('Information')
        page_timeline_settings.enter_advanced_page()
        page_edit.settings.swipe_to_option('Open Tool Menu When Selecting an Object in Timeline')
        # page_edit.settings.swipe_to_option('File Name in Media Library')
        page_timeline_settings.open_tool_menu_when_selecting('ON')
        # page_edit.settings.swipe_to_option('File Name in Media Library')
        page_edit.settings.swipe_to_option('Premium Content')
        page_timeline_settings.display_file_name_in_library('ON')
        time.sleep(5)

