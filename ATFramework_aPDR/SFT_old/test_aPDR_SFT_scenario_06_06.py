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


class Test_SFT_Scenario_06_06:
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
    def test_sce_06_06_01(self):
        logger('>>> test_sce_06_06_01 : Default Quality <<<')
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

        self.report.start_uuid('60596329-a97c-49d0-8728-054c006d7fd2')
        self.report.start_uuid('782cbeab-94c0-4429-97b5-e7e0308337fb')
        page_main.enter_settings_from_main()
        result = page_timeline_settings.get_settings_default_video_quality()
        self.report.new_result('60596329-a97c-49d0-8728-054c006d7fd2', True if result == 'HD 720p/540p' else False)
        self.report.new_result('782cbeab-94c0-4429-97b5-e7e0308337fb', True if result == 'HD 720p/540p' else False)

        self.report.start_uuid('1f906728-3766-4424-8d9e-ddf9a96e8a3b')
        page_main.click(L.timeline_settings.settings.text_video_quality)
        page_main.click(L.timeline_settings.default_video_quality.radio_btn_uhd)
        # page_timeline_settings.select_settings_video_quality_radio('uhd')
        time.sleep(3)
        if page_main.is_exist(L.ad.iap_back_btn):
            result = True
            page_main.click(L.ad.iap_back_btn)
        else:
            result = False
        self.report.new_result('1f906728-3766-4424-8d9e-ddf9a96e8a3b', result)

        self.report.start_uuid('e9b49525-609c-44d2-91c0-f9dbbf47bd27')
        # page_timeline_settings.select_settings_video_quality_radio('fhd')
        page_main.click(L.timeline_settings.default_video_quality.radio_btn_fhd)
        time.sleep(3)
        if page_main.is_exist(L.ad.iap_back_btn):
            result = True
            page_main.click(L.ad.iap_back_btn)
        else:
            result = False
        self.report.new_result('e9b49525-609c-44d2-91c0-f9dbbf47bd27', result)

        self.report.start_uuid('42eafbdf-81a4-4864-a38b-385261387932')
        # page_timeline_settings.select_settings_video_quality_radio('sd')
        page_main.click(L.timeline_settings.default_video_quality.radio_btn_sd)
        time.sleep(3)
        result = True if page_timeline_settings.get_settings_video_quality_radio_is_checked() == 'sd' else False
        self.report.new_result('42eafbdf-81a4-4864-a38b-385261387932', result)

        self.report.start_uuid('7e8dc38a-1aaa-4f1a-9d8b-3ec4551c523a')
        # page_timeline_settings.select_settings_video_quality_radio('hd')
        page_main.click(L.timeline_settings.default_video_quality.radio_btn_hd)
        time.sleep(3)
        result = True if page_timeline_settings.get_settings_video_quality_radio_is_checked() == 'hd' else False
        self.report.new_result('7e8dc38a-1aaa-4f1a-9d8b-3ec4551c523a', result)

        self.report.start_uuid('8e004f5c-5ec3-439f-a830-b4edb38cb14d')
        # page_timeline_settings.select_settings_video_quality_radio('sd')
        page_main.click(L.timeline_settings.default_video_quality.radio_btn_sd)
        time.sleep(3)
        page_timeline_settings.click(L.timeline_settings.default_video_quality.btn_back)
        page_main.click(L.timeline_settings.settings.back)
        page_main.swipe_main_page('down', 5)
        page_main.select_existed_project_by_title(project_title)
        time.sleep(5)
        # page_main.click(L.main.project_info.btn_edit_project)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(5)
        page_produce.select_produce_type('gallery')
        result = True if page_produce.get_video_quality_radio_is_checked() == 'sd' else False
        self.report.new_result('8e004f5c-5ec3-439f-a830-b4edb38cb14d', result)

