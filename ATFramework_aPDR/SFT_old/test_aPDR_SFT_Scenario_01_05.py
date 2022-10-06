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


class Test_SFT_Scenario_01_05:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver session>============')
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

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_05_01(self):
        #create new project > set aspect ratio

        video_list = ['mp4.mp4', '3gp.3GP', 'slow_motion.mp4', 'mkv.mkv' ]

        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # page_main.subscribe(0)
        page_main.project_click_new()
        page_main.project_set_name("01_05_01")
        page_main.project_set_16_9()
        #add 3 video to timeline
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit.el(L.import_media.menu.back).click()
        
        page_edit.click(L.edit.menu.timeline_setting)
        page_edit.click(L.edit.sub_menu.settings)
        time.sleep(3)
        page_main.sign_in_cyberlink_account()
        time.sleep(5)
        page_main.back()
        time.sleep(5)
        
        page_edit.el(L.edit.menu.effect).click()
        time.sleep(5)
        page_edit.el(L.edit.effect_sub.video).click()
        #page_media.switch_to_video_library()
        # Enter stock video: pixabay
        self.report.start_uuid('2d748d11-432d-489b-bbad-f2f710608992')
        page_media.select_media_by_text('Stock Video')
        page_media.el(L.import_media.video_library.tab_pixabay).click()
        page_media.select_media_by_order(2)
        page_media.select_media_by_order(1)
        page_media.download_video()
        time.sleep(5)
        page_media.select_media_by_order(2)
        page_media.select_media_by_order(1)
        self.report.new_result('2d748d11-432d-489b-bbad-f2f710608992', page_edit.is_exist(L.import_media.library_gridview.add))        
        # Enter Shutterstock
        self.report.start_uuid('0ebd7445-c423-484c-9853-c5fb70c2f83d')
        page_media.el(L.import_media.video_library.tab_video_shutterstock).click()
        if  page_edit.is_exist(L.import_media.video_library.shutterstock_ToU_OK):
            page_media.el(L.import_media.video_library.shutterstock_ToU_OK).click()
        page_media.select_media_by_order(1)
        page_media.download_video()
        time.sleep(5)
        page_media.select_media_by_order(2)
        page_media.select_media_by_order(1)
        self.report.new_result('0ebd7445-c423-484c-9853-c5fb70c2f83d', page_edit.is_exist(L.import_media.library_gridview.add)) 
        
        # Search in Shutterstock
        self.report.start_uuid('ccfbc4dd-6bc0-469a-89a4-0965dae1baa4')
        page_media.search_video('star')
        time.sleep(15)
        page_media.select_media_by_order(2)
        page_media.select_media_by_order(1)
        page_media.download_video()
        time.sleep(5)
        page_media.select_media_by_order(2)
        page_media.select_media_by_order(1)
        self.report.new_result('ccfbc4dd-6bc0-469a-89a4-0965dae1baa4', page_edit.is_exist(L.import_media.library_gridview.add)) 
        
        # Search in pixabay
        self.report.start_uuid('dd73a4e5-97c8-4d66-8bc9-885b4e0af3a4')
        page_media.el(L.import_media.video_library.searchClear).click()
        time.sleep(5)
        page_media.search_video('ball')
        time.sleep(15)
        page_media.select_media_by_order(2)
        page_media.select_media_by_order(1)
        page_media.download_video()
        time.sleep(5)
        page_media.select_media_by_order(2)
        page_media.select_media_by_order(1)
        self.report.new_result('dd73a4e5-97c8-4d66-8bc9-885b4e0af3a4', page_edit.is_exist(L.import_media.library_gridview.add)) 
        
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.timeline_setting)
        page_edit.click(L.edit.sub_menu.settings)
        time.sleep(3)
        page_main.sign_out_cyberlink_account()
