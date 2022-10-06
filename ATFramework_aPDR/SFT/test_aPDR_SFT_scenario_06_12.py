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

class Test_SFT_Scenario_06_12:
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
    def test_sce_06_12_01(self):
        logger('>>> test_sce_06_12_01 : Shutterstock Music <<<')
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
        
        self.report.start_uuid('f872d25e-da26-4baf-b7b5-bd51e3248299')
        page_main.project_click_new()
        page_main.project_set_name("sce_06_12_01")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.switch_to_music_library()
        page_media.select_media_by_text('Stock Music')
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        page_media.click(L.import_media.music_library.filter_all)
        page_media.back()
        time.sleep(3)
        amount = page_edit.calculate_library_content_amount()
        result = True if amount >= 72 else False
        self.report.new_result('f872d25e-da26-4baf-b7b5-bd51e3248299', result, f'amount = {amount}')

        self.report.start_uuid('fa458209-d9b8-48a2-9495-2fb3c5113384')
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        page_media.click(L.import_media.music_library.filter_genres)
        page_media.back()
        time.sleep(3)
        amount = page_edit.calculate_library_content_amount()
        result = True if amount >= 46 else False
        self.report.new_result('fa458209-d9b8-48a2-9495-2fb3c5113384', result, f'amount = {amount}')

        self.report.start_uuid('061f2a25-d433-4d69-aa9f-c4373260d0a9')
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        page_media.click(L.import_media.music_library.filter_moods)
        page_media.back()
        time.sleep(3)
        amount = page_edit.calculate_library_content_amount()
        result = True if amount >= 26 else False
        self.report.new_result('061f2a25-d433-4d69-aa9f-c4373260d0a9', result, f'amount = {amount}')
        
        self.report.start_uuid('b7ffc79c-2768-45f8-9246-673279c89511')
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        page_media.click(L.import_media.music_library.filter_all)
        page_media.back()
        time.sleep(3)
        page_media.search_video('star')
        result = True if page_edit.is_exist(L.import_media.library_listview.frame_song, 10) else False
        self.report.new_result('b7ffc79c-2768-45f8-9246-673279c89511', result)

        self.report.start_uuid('1cbc7574-53cb-40f3-ab7b-8e949c0395ca')
        self.report.start_uuid('45bafac6-1911-424b-a94d-a5007ee8a197')
        page_media.back()
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        page_media.click(L.import_media.music_library.filter_genres)
        page_media.back()
        time.sleep(3)
        page_media.search_video('star')
        result = True if page_edit.is_exist(L.import_media.library_listview.frame_song, 10) else False
        page_media.click(L.import_media.library_listview.frame_song)
        time.sleep(3)
        result_download = page_media.download_music()
        self.report.new_result('1cbc7574-53cb-40f3-ab7b-8e949c0395ca', result)
        self.report.new_result('45bafac6-1911-424b-a94d-a5007ee8a197', result_download)

        self.report.start_uuid('ec6be91b-031f-4a11-af93-b7f2da136650')
        self.report.start_uuid('8d2b8884-f3b2-4077-9601-94e2fffadec5')
        page_media.back()
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        page_media.click(L.import_media.music_library.filter_moods)
        page_media.back()
        time.sleep(3)
        page_media.search_video('star')
        result = True if page_edit.is_exist(L.import_media.library_listview.frame_song, 10) else False
        page_media.click(L.import_media.library_listview.frame_song)
        time.sleep(3)
        result_download = page_media.download_music()
        self.report.new_result('ec6be91b-031f-4a11-af93-b7f2da136650', result)
        self.report.new_result('8d2b8884-f3b2-4077-9601-94e2fffadec5', result_download)
