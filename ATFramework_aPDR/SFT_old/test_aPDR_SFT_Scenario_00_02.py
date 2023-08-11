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

from pages.locator import locator as L

from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
report = REPORT_INSTANCE

pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER

class Test_SFT_Scenario_00_02b:
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
        desired_caps.update(app_config.prod_install_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        logger(f"desired_caps={desired_caps}")
        cls.report = report
        cls.device_udid = DRIVER_DESIRED_CAPS['udid']
        # ---- local mode > end ----
        cls.test_material_folder = test_material_folder

                                                              
        # retry 3 time if craete driver fail
        retry = 3
        while retry:
            try:
                cls.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',desired_caps)
                if cls.driver:
                    logger("driver created!")
                    break
                else:
                    raise Exception("create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
                
        cls.report.set_driver(cls.driver)
        cls.driver.implicit_wait(15)
        cls.driver.reset_app(pdr_package)

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
    
    #@pytest.mark.skip
    @pytest.mark.usefixtures('set_permission')
    @report.exception_screenshot
    def test_sce_00_02_01(self):
        udid = ['36a2d103-2852-4f11-9ded-0f3f681e4ee5', '2dc11c74-7245-490e-9f36-9fbb35a4ecb7']
        #self.report.start_uuid('2dc11c74-7245-490e-9f36-9fbb35a4ecb7')
        #Tips_Edit Page
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_02_01")
        page_main.project_set_9_16()
        logger('[V] Tips_Edit Page')
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.el(L.import_media.video_entry.back).click()
        '''
        self.report.new_result(udid[1], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid('36a2d103-2852-4f11-9ded-0f3f681e4ee5')
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
    #@pytest.mark.usefixtures('set_permission')
    @report.exception_screenshot
    def test_sce_00_02_02(self):
        udid = ['cdab4753-ecb9-430f-b3eb-ed0fd36b4761', '848b90c4-da3b-48f6-b246-cd6daf4f497c',
                'b0ccacbd-be6f-4d6f-9735-e0134f50ded7', '20bcee25-7f62-45b1-98e9-501496df7c1b']
        media_list = ['mkv.mkv']
        self.report.start_uuid('848b90c4-da3b-48f6-b246-cd6daf4f497c')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_02_02")
        page_main.project_set_16_9()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_check_media(media_list[0])
        logger('[V] Tips_Select Video/ Photo')
        page_edit.timeline_select_media(media_list[0], 'Video')
        self.report.new_result(udid[1], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid('cdab4753-ecb9-430f-b3eb-ed0fd36b4761')
        page_edit.force_uncheck_help_enable_tip_to_Leave(-50)
        #check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[0], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid('20bcee25-7f62-45b1-98e9-501496df7c1b')
        page_edit.force_uncheck_help_enable_tip_to_Leave(-50)
        logger('[V] Tips_Speed')
        #page_edit.el(L.edit.menu.edit).click()
        page_edit.el(L.edit.edit_sub.speed).click()
        self.report.new_result(udid[3], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid('b0ccacbd-be6f-4d6f-9735-e0134f50ded7')
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[2], page_edit.check_help_enable_tip_visible())
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        #page_edit.el(L.edit.menu.back_session).click()
        page_main.back_to_leave_and_save_project(4)
    '''
    # @pytest.mark.skip
    #@pytest.mark.usefixtures('set_permission')
    @report.exception_screenshot
    def test_sce_00_02_03(self):
        udid = ['a7adcdab-c512-462d-ae45-e370e570fb8a', 'fc60dd0f-82a2-434c-a073-648f59f483bb',
                '7fc864c0-854c-41cc-8312-4632a8ce0675', '7cab7892-9ee1-4fa8-8144-51c4a35c6498',
                'af6b9dc7-3318-47bd-93e9-cdf5e452b326']
        media_list = ['mkv.mkv']
        self.report.start_uuid('fc60dd0f-82a2-434c-a073-648f59f483bb')
        self.report.start_uuid('af6b9dc7-3318-47bd-93e9-cdf5e452b326')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_02_03")
        page_main.project_set_16_9()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_check_media(media_list[0])
        page_edit.timeline_select_media(media_list[0], 'Video')
        logger('[V] Tips_Crop')
        page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.crop).click()
        page_edit.select_from_bottom_edit_menu('Crop')
        self.report.new_result(udid[1], page_edit.check_help_enable_tip_visible())
        self.report.new_result(udid[4], page_edit.check_help_enable_tip_visible())
        #self.report.start_uuid('a7adcdab-c512-462d-ae45-e370e570fb8a')
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        
        #6.8.1 new feature: tool menu is hide by default
        #page_edit.el(L.edit.menu.timeline_setting).click()
        #page_edit.el(L.edit.sub_menu.settings).click()
        #time.sleep(5)
        #page_edit.settings.swipe_to_option('Open Tool Menu When Selecting an Object in Timeline')
        #page_timeline_settings.open_tool_menu_when_selecting('ON')
        #page_edit.settings.swipe_to_option('Display File Name in Media Library')
        #page_timeline_settings.display_file_name_in_library('ON')
        
        
        '''
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[0], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid('7cab7892-9ee1-4fa8-8144-51c4a35c6498')
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        page_edit.el(L.edit.menu.back_session).click()
        
        logger('[V] Tips_Pan_Zoom')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        self.report.new_result(udid[3], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid('7fc864c0-854c-41cc-8312-4632a8ce0675')
        time.sleep(5)
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, -300)
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[2], page_edit.check_help_enable_tip_visible())
        '''
    '''
    #@pytest.mark.skip
    #@pytest.mark.usefixtures('set_permission')
    @report.exception_screenshot
    def test_sce_00_02_04(self):
        udid = ['6bb8826e-765e-4172-9ec8-2b1748c15a84', '9e067d50-df7e-43e8-b76f-6cb36fc8d03d',
                '2e469c7d-aea7-417a-99bf-e0d440487249', '81ac64fb-ec6e-4762-a0b1-1ff786f9af0f']
        media_list = ['slow_motion.mp4']
        self.report.start_uuid(udid[1])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("sce_00_02_04")
        page_main.project_set_16_9()
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
        #page_edit.el(L.edit.menu.edit).click()
        page_edit.el(L.edit.edit_sub.stabilizer).click()
        page_edit.wait_for_stabilizing_complete()
        self.report.new_result(udid[3], page_edit.check_help_enable_tip_visible())
        self.report.start_uuid(udid[2])
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        # check settings > tips
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.tips).click()
        self.report.new_result(udid[2], page_edit.check_help_enable_tip_visible())
        page_edit.clean_movie_cache()
        logger("[V] remove Tips_color")
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        time.sleep(1)
        page_edit.driver.driver.back()
        #page_edit.el(L.edit.menu.edit).click()
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
