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


class Test_SFT_Scenario_04_06:
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
    def test_sce_04_06_01(self):
        logger('>>> test_sce_04_06_01 : New produce flow <<<')
        media_list = ['01_static.mp4']
        self.report.start_uuid('35c7eac7-f4ce-4295-940e-b0c193e8a1a8')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        #page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        page_main.el(L.edit.menu.produce).click()
        page_main.exist_click(L.produce.iap_back)
        self.report.new_result('35c7eac7-f4ce-4295-940e-b0c193e8a1a8', page_edit.is_exist(L.produce.tab.gallery))
          
        self.report.start_uuid('f72af7a1-4a67-411c-bc85-5794f16e1f0c')
        self.report.start_uuid('d1f32691-2b98-4ec3-9ae8-f284691813c9')
        self.report.start_uuid('686d112e-2667-4886-be2e-69e091eebaf8')
        self.report.start_uuid('b4c3211e-43ad-4079-8605-6f2ec26e3aa3')
        self.report.start_uuid('16c7fea8-fd50-49a9-a3b2-b67d8022bf1f')
        page_produce.select_produce_type('gallery')
        result_progress, result_thumbnail, result_ad, result_back, result_cancel = page_produce.check_produce_progress()
        self.report.new_result('f72af7a1-4a67-411c-bc85-5794f16e1f0c', result_progress)
        self.report.new_result('d1f32691-2b98-4ec3-9ae8-f284691813c9', result_thumbnail)
        self.report.new_result('686d112e-2667-4886-be2e-69e091eebaf8', result_back)
        self.report.new_result('b4c3211e-43ad-4079-8605-6f2ec26e3aa3', result_ad)
        self.report.new_result('16c7fea8-fd50-49a9-a3b2-b67d8022bf1f', result_cancel)
        
        self.report.start_uuid('f0c16e27-f9f3-42d5-8653-cc883212935f')
        result = page_produce.preview_produced_video()
        self.report.new_result('f0c16e27-f9f3-42d5-8653-cc883212935f', result)        
        
        self.report.start_uuid('62f324f2-eba1-440e-bd09-34d56f679f16')
        result = page_produce.is_exist(L.produce.gallery.produce_page.ad_frame)
        self.report.new_result('62f324f2-eba1-440e-bd09-34d56f679f16', result)        
        self.report.start_uuid('74f01340-a7c8-48e8-b17c-906429cd34a9')
        result = page_produce.is_exist(L.produce.gallery.produce_page.btn_back)
        self.report.new_result('74f01340-a7c8-48e8-b17c-906429cd34a9', result)
        self.report.start_uuid('57db25c0-3b36-4753-9bef-d7591234d1e2')
        result = page_produce.is_exist(L.produce.gallery.produce_page.btn_file_location)
        self.report.new_result('57db25c0-3b36-4753-9bef-d7591234d1e2', result)        
        self.report.start_uuid('3eb3ecfc-a3a4-4a76-8e1e-7f94b4908b70')
        result = page_produce.is_exist(L.produce.gallery.produce_page.btn_share_to)
        self.report.new_result('3eb3ecfc-a3a4-4a76-8e1e-7f94b4908b70', result)      
        self.report.start_uuid('89c5164c-de6a-4e2e-acc1-cecc8eb46c6b')
        result = page_produce.is_exist(L.produce.gallery.produce_page.btn_cancel)
        self.report.new_result('89c5164c-de6a-4e2e-acc1-cecc8eb46c6b', result)     
        self.report.start_uuid('88c8a821-a88a-437f-9c71-b18dac4d6d4c')
        result = page_produce.is_exist(L.produce.gallery.produce_page.ad_frame)
        self.report.new_result('88c8a821-a88a-437f-9c71-b18dac4d6d4c', result)  
    
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_04_06_02(self):
        logger('>>> test_sce_04_06_02 : Share to IG/TikTok <<<')
        media_list = ['01_static.mp4']
        self.report.start_uuid('e7279a0f-ebc8-40ed-ad34-a7940f0d3af7')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        project_title = '16_9'
        page_main.enter_settings_from_main()
        page_main.sign_in_cyberlink_account()
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        # page_main.subscribe()
        
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        page_main.el(L.edit.menu.produce).click()       
        time.sleep(5)
        # IG
        result = page_produce.select_produce_type('ig')
        self.report.new_result('e7279a0f-ebc8-40ed-ad34-a7940f0d3af7', result)        
       
        self.report.start_uuid('e27a0fcf-0ef4-441f-a75a-17152dfa673d')
        page_produce.click(L.produce.gallery.hd)
        time.sleep(5)
        result = page_produce.start_produce()
        time.sleep(5)
        self.report.new_result('e27a0fcf-0ef4-441f-a75a-17152dfa673d', result)       
        
        self.report.start_uuid('8b6a464a-5e7f-48d2-95a9-3d3076cdbc2c')
        result = page_produce.share_to_ig()
        self.report.new_result('8b6a464a-5e7f-48d2-95a9-3d3076cdbc2c', result)        
       
        # TikTok
        self.report.start_uuid('b5b9d1ef-cf09-4fe1-82fe-9d696ec577ca')
        page_produce.back()
        time.sleep(5)
        result = page_produce.select_produce_type('tiktok')
        time.sleep(5)
        page_produce.click(L.produce.gallery.full_hd)
        time.sleep(5)
        self.report.new_result('b5b9d1ef-cf09-4fe1-82fe-9d696ec577ca', result)        
       
        self.report.start_uuid('4ac0c8f2-392a-4ac3-a6b2-9a211fe2de67')
        result = page_produce.start_produce()
        self.report.new_result('4ac0c8f2-392a-4ac3-a6b2-9a211fe2de67', result)       
        
        self.report.start_uuid('b9eed939-a553-4579-ad28-14ad5c676a55')
        result = page_produce.share_to_tiktok()
        self.report.new_result('b9eed939-a553-4579-ad28-14ad5c676a55', result)
        
        # Kill PDR and TikTok app
        page_main._terminate_app(pdr_package)
        page_main._terminate_app('com.ss.android.ugc.trill')