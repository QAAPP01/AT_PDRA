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
        logger('[V] Set Permission')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        logger('[Permission] Confirm GDPR')
        if page_main.exist_click(L.main.permission.gdpr_accept,5): # Android version  < 6 or locate in EU
            logger("[Permission] GDPR found and closed")
        page_main.is_exist(L.main.permission.file_ok, 120)
        page_main.el(L.main.permission.file_ok).click()
        page_main.el(L.main.permission.photo_allow).click()
    
    @pytest.mark.skip
    @pytest.mark.usefixtures('set_permission')
    @report.exception_screenshot
    def test_sce_00_01_01(self):
        udid = ['35bdb1ab-dbba-45aa-ab6f-22ec495c0344', '18600fa6-2720-4d35-8677-ac985eee1616']
        #Tips_Edit Page
        #self.report.start_uuid(udid[1])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_01_01")
        page_main.project_set_9_16()  
        logger('[V] Tips_Edit Page')
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.el(L.import_media.video_entry.back).click()
        #6.8.1 new feature: tool menu is hide by default
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.open_tool_menu_when_selecting('ON')
        
        '''
        self.report.new_result(udid[1], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[0])
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, 0, L.edit.menu.timeline_setting, 2)
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[0], page_edit.check_help_enable_tip_visible())
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, 0, L.edit.menu.timeline_setting, 2)
        page_main.back_to_leave_and_save_project(2)
        '''
    '''
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_00_01_02(self):
        udid = ['e4bba393-2d8f-4001-8580-68a35eea7ecd', 'ea91473b-c83d-4d3c-ad4a-43da25128d18',
                '6a9cd909-4916-40a6-bbc6-2d905b693ec3', '79abb5f6-bcc8-4c2e-a1c8-7d878c9e6cf8']
        media_list = ['mkv.mkv']
        self.report.start_uuid(udid[1])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_01_02")
        page_main.project_set_9_16()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_check_media(media_list[0])
        #logger('[V] Tips_Select Video/ Photo')
        page_edit.timeline_select_media(media_list[0], 'Video')
        self.report.new_result(udid[1], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[0])
        page_edit.force_uncheck_help_enable_tip_to_Leave(-50)
        #check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[0], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[3])
        page_edit.force_uncheck_help_enable_tip_to_Leave(-50)
        logger('[V] Tips_Speed')
        page_edit.el(L.edit.menu.edit).click()
        page_edit.el(L.edit.edit_sub.speed).click()
        self.report.new_result(udid[3], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[2])
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[2], page_edit.check_help_enable_tip_visible())
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        #page_edit.el(L.edit.menu.back_session).click()
        page_main.back_to_leave_and_save_project(4)
    '''
    #@pytest.mark.skip
    @pytest.mark.usefixtures('set_permission')
    @report.exception_screenshot
    def test_sce_00_01_03(self):
        udid = ['5a237f73-d5ac-4dfa-b16a-585a39f384bd', 'da7b1a17-1104-4403-9ba3-6d18641fc111',
                '1dc34369-00a6-4c3d-ad2d-951c5d94e3dd', 'f914eb95-c545-434b-8877-dd50e2a6e736',
                '0497a3a1-eb5a-4233-9f47-572f96567a04']
        media_list = ['mkv.mkv']
        self.report.start_uuid(udid[1])
        self.report.start_uuid(udid[4])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_01_03")
        page_main.project_set_9_16()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_check_media(media_list[0])
        page_edit.timeline_select_media(media_list[0], 'Video')
        logger('[V] Tips_Crop')
        page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.crop).click()  
        page_edit.select_from_bottom_edit_menu('Crop')
        self.report.new_result(udid[1], page_edit.check_help_enable_tip_visible())
        self.report.new_result(udid[4], page_edit.check_help_enable_tip_visible())
        #self.report.start_uuid(udid[0])
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        
        #6.8.1 new feature: tool menu is hide by default
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(5)
        page_edit.settings.swipe_to_option('Open Tool Menu When Selecting an Object in Timeline')
        page_timeline_settings.open_tool_menu_when_selecting('ON')
        '''
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[0], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[3])
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        page_edit.el(L.edit.menu.back_session).click()
        logger('[V] Tips_Pan_Zoom')
        page_edit.el(L.edit.menu.edit).click()
        page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        self.report.new_result(udid[3], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[2])
        time.sleep(5)
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, -300)
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[2], page_edit.check_help_enable_tip_visible())
        '''
    '''
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_00_01_04(self):
        udid = ['8a9fd489-92e6-4b67-911c-896e7d932256', '397ba771-581b-4446-b8a3-259d4e36f4be',
                '00be410a-ec88-47e9-bbce-82580cf1c71d', 'bc79bcf4-3215-4d4b-9578-5a505467c209']
        media_list = ['slow_motion.mp4']
        self.report.start_uuid(udid[1])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_01_04")
        page_main.project_set_9_16()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_check_media(media_list[0])
        page_edit.timeline_select_media(media_list[0], 'Video')
        page_edit.el(L.edit.menu.back).click()
        logger('[V] Tips_Sticker')
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.effect.menu.sticker).click()
        self.report.new_result(udid[1], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[3])
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, 0, L.import_media.menu.back)
        page_media.el(L.import_media.menu.back)
        logger('[V] Tips_Stabilizer')
        page_edit.timeline_select_media(media_list[0], 'Video')
        page_edit.el(L.edit.menu.edit).click()
        page_edit.el(L.edit.edit_sub.stabilizer).click()
        page_edit.wait_for_stabilizing_complete()
        self.report.new_result(udid[3], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[2])
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[2], page_edit.check_help_enable_tip_visible())
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        logger("[V] remove Tips_color")
        #page_edit.force_uncheck_help_enable_tip_to_Leave()
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.edit).click()
        page_edit.el(L.edit.edit_sub.color).click()
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        logger("[V] remove Tips_Title")
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        # select Assembly Line to add timeline
        page_media.select_media_by_text('Assembly Line')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.force_uncheck_help_enable_tip_to_Leave()
    '''