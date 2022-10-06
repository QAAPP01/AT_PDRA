import sys
from os.path import dirname as _dir
sys.path.insert(0, (_dir(_dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest
import time

from pages.locator import locator as L
from pages.locator.locator_type import *

from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
report = REPORT_INSTANCE

pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER

BETTER_QUALITY = 0
STANDARD = 1
SMALLER_SIZE = 2

FPS_24 = 0
FPS_30 = 1
FPS_60 = 2

ULTRA_HD = 0
FULL_HD = 1
HD = 2
SD = 3


class Test_sce_04_01_01:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        self.report = report
        # ---- local mode > end ----
                                                              
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
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.produce = PageFactory().get_page_object("produce", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)

        self.driver.implicit_wait(5)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_04_01_01(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        _start('6b85d6db-b44c-4033-9fb3-22a358e907f2')
        main.project_reload("2-5_add_color_board")
        result_project_with_settings =  main.project_select_with_correct_setting("2-5_add_color_board","00:00:15")
        _end('6b85d6db-b44c-4033-9fb3-22a358e907f2',result_project_with_settings)
        
        # block 1080p
        _start('c74358ce-293f-4181-8722-bc4dcf131c01')
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.facebook)
        result_lock_1080p = produce.is_exist(L.produce.facebook.fhd_lock)
        _end('c74358ce-293f-4181-8722-bc4dcf131c01',result_lock_1080p)
        
        # block 24 fps + 1080p
        _start('e5bb9c90-a7d6-48ad-9922-df9643a79dd0')
        produce.click(L.produce.facebook.setting)
        produce.setting.set_bitrate(SMALLER_SIZE)
        produce.setting.set_framerate(FPS_24)
        produce.click(L.produce.facebook.setting_page.ok)
        result_lock_1080p_24fps = produce.is_exist(L.produce.facebook.fhd_lock)
        _end('e5bb9c90-a7d6-48ad-9922-df9643a79dd0',result_lock_1080p_24fps)
        
        # default is HD
        _start('80905080-5e15-482f-9999-d8bb9652319b')
        result_default_is_hd = produce.el(L.produce.facebook.hd).get_attribute('checked').lower() == 'true'
        _end('80905080-5e15-482f-9999-d8bb9652319b',result_default_is_hd)
        
        # BETTER_QUALITY + FPS_30
        _start('52f82180-1a98-43ff-aeab-c15485fd8f3a')
        produce.click(L.produce.facebook.setting)
        produce.setting.set_bitrate(BETTER_QUALITY)
        produce.setting.set_framerate(FPS_30)
        produce.click(L.produce.facebook.setting_page.ok)
        produce.click(L.produce.facebook.next)
        #produce.exist_click(L.main.subscribe.back_btn,3)
        #produce.ad.close_full_page_ad()
        result_share_to_fb = produce.close_produce_page()
        _end('52f82180-1a98-43ff-aeab-c15485fd8f3a',result_share_to_fb)
        
        # default is HD
        _start('ef331790-9e21-4ad4-b81f-a11b9dc86c5f')
        produce.back()
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.facebook)
        result_default_is_hd = produce.el(L.produce.facebook.hd).get_attribute('checked').lower() == 'true'
        _end('ef331790-9e21-4ad4-b81f-a11b9dc86c5f',result_default_is_hd)
        
        # SD + STANDARD + FPS_60
        _start('330116a5-370b-4de0-86a3-eb4199beb282')
        produce.set_resolution(SD)
        produce.click(L.produce.facebook.setting)
        produce.setting.set_bitrate(STANDARD)
        produce.setting.set_framerate(FPS_60)
        produce.click(L.produce.facebook.setting_page.ok)
        produce.click(L.produce.facebook.next)
        #produce.exist_click(L.main.subscribe.back_btn,3)
        #produce.ad.close_full_page_ad()
        result_share_to_fb = produce.close_produce_page()
        _end('330116a5-370b-4de0-86a3-eb4199beb282',result_share_to_fb)
        
        
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_04_01_02(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        _start('25c690f4-cf13-4b3c-9284-69b625798af8')
        main.project_reload("3-5_add_color_board")
        result_project_with_settings =  main.project_select_with_correct_setting("3-5_add_color_board","00:00:15")
        _end('25c690f4-cf13-4b3c-9284-69b625798af8',result_project_with_settings)
        
        # default is HD
        _start('0c3df89e-316c-4042-931b-e5c97cb9e590')
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.facebook)
        result_default_is_hd = produce.el(L.produce.facebook.hd).get_attribute('checked').lower() == 'true'
        _end('0c3df89e-316c-4042-931b-e5c97cb9e590',result_default_is_hd)
        
        # HD +  small + FPS_60
        _start('080e9f6b-1be8-4975-baf6-edfd47d91e9f')
        produce.set_resolution(HD)
        produce.click(L.produce.facebook.setting)
        produce.setting.set_bitrate(SMALLER_SIZE)
        produce.setting.set_framerate(FPS_60)
        produce.click(L.produce.facebook.setting_page.ok)
        produce.click(L.produce.facebook.next)
        #produce.exist_click(L.main.subscribe.back_btn,3)
        #produce.ad.close_full_page_ad()
        result_share_to_fb = produce.close_produce_page()
        _end('080e9f6b-1be8-4975-baf6-edfd47d91e9f',result_share_to_fb)
        
        # default is HD
        _start('c0321f5b-d1e0-413d-b7c1-5b7a0bec5b24')
        produce.back()
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.facebook)
        result_default_is_hd = produce.el(L.produce.facebook.hd).get_attribute('checked').lower() == 'true'
        _end('c0321f5b-d1e0-413d-b7c1-5b7a0bec5b24',result_default_is_hd)
        
        # sd +  better + FPS_30
        logger("sd +  better + FPS_30")
        _start('9ba6d5e8-eade-4fcc-8bcd-7b8d25d18f08')
        produce.set_resolution(SD)
        produce.click(L.produce.facebook.setting)
        produce.setting.set_bitrate(BETTER_QUALITY)
        produce.setting.set_framerate(FPS_30)
        produce.click(L.produce.facebook.setting_page.ok)
        produce.click(L.produce.facebook.next)
        #produce.exist_click(L.main.subscribe.back_btn,3)
        #produce.ad.close_full_page_ad()
        result_share_to_fb = produce.close_produce_page()
        _end('9ba6d5e8-eade-4fcc-8bcd-7b8d25d18f08',result_share_to_fb)
        
        # default is HD
        logger("default is HD")
        _start('7938f9d3-73f9-467f-b6cc-794a595b0620')
        time.sleep(1)
        produce.back()
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.facebook)
        result_default_is_hd = produce.el(L.produce.facebook.hd).get_attribute('checked').lower() == 'true'
        _end('7938f9d3-73f9-467f-b6cc-794a595b0620',result_default_is_hd)
        
        # hd + smaller + FPS_24
        _start('d9f93608-7882-435b-8ff7-0a9e36e072d1')
        produce.set_resolution(HD)
        produce.click(L.produce.facebook.setting)
        produce.setting.set_bitrate(SMALLER_SIZE)
        produce.setting.set_framerate(FPS_24)
        produce.click(L.produce.facebook.setting_page.ok)
        produce.click(L.produce.facebook.next)
        #produce.exist_click(L.main.subscribe.back_btn,3)
        #produce.ad.close_full_page_ad()
        result_share_to_fb = produce.close_produce_page()
        _end('d9f93608-7882-435b-8ff7-0a9e36e072d1',result_share_to_fb)
        
        

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_04_01_03(self):
        """
            Implement it on product release build.
            Subscription then same steps as test_sce_04_01_01
            Note: Move to test_sce_06_04_01
        """
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_04_01_04(self):
        """
            Implement it on product release build.
            Subscription then same steps as test_sce_04_01_02
            Note: Move to test_sce_06_04_02
        """

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_04_01_05(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        _start('3d2022d4-391b-4a9a-8420-936fd79ec347')
        main.project_reload("16_9")
        result_project_with_settings =  main.project_select_with_correct_setting("16_9","00:02:20")
        _end('3d2022d4-391b-4a9a-8420-936fd79ec347',result_project_with_settings)
        
        _start('b83f975b-d3e6-4d83-b6d1-13b3cb9582a7')
        time.sleep(2)
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.select_cloud()
        produce.exist_click(L.produce.cloud.signout,3)
        produce.click(L.produce.cloud.export)
        produce.set_text(L.produce.cloud.email,"cloudtest193@cyberlink.com")
        produce.set_text(L.produce.cloud.pw,"1234")
        produce.click(L.produce.cloud.signin)
        #produce.exist_click(L.main.subscribe.back_btn,3)
        produce.close_produce_page()
        #result_finish_upload = produce.is_exist(L.produce.tab.cloud)
        result_finish_upload = produce.is_exist(L.main.project.new)
        _end('b83f975b-d3e6-4d83-b6d1-13b3cb9582a7',result_finish_upload)

'''        
        result = main.click_tutorials("Pan & Zoom (Ken Burns) Effect")
        self.report.new_result("170599e4-2431-4960-b65e-f9aef05c0cf8", result[0])
        self.report.new_result("58cb54a4-8a44-45d5-850e-08c84ccceeb7", result[1])
'''        
        

