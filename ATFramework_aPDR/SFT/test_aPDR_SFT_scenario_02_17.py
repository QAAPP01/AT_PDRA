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


class Test_SFT_Scenario_02_17:
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
    def test_sce_02_17_01(self):
        logger('>>> test_sce_02_17_01: Music Favorite <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        # page_main.put_voiceover_file(self.device_udid, pdr_package)
        
        # New project
        self.report.start_uuid('34d9e211-d6b4-4f76-8fc2-527ff296817a')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_17_01")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.switch_to_music_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_song_by_text('mp3.mp3')
        time.sleep(3)
        result = page_media.tap_favorite()
        self.report.new_result('34d9e211-d6b4-4f76-8fc2-527ff296817a', result)
        
        self.report.start_uuid('2ffcb50c-6090-4b22-a96d-984291b2d575')
        page_main.back()
        time.sleep(5)
        page_media.select_media_by_text('Stock Music')
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        page_media.click(L.import_media.music_library.filter_all)
        page_media.back()
        time.sleep(3)
        page_media.select_media_by_text('Audio Logos')
        page_media.select_song_by_text('Action Audio Logo')
        time.sleep(3)
        result = page_media.tap_favorite()
        self.report.new_result('2ffcb50c-6090-4b22-a96d-984291b2d575', result)        
        
        self.report.start_uuid('bfa6ac5a-7f45-4980-b39b-70774c76da61')
        page_main.back()
        time.sleep(5)
        page_media.click(L.import_media.music_library.pdr_tab)
        time.sleep(5)
        page_media.select_media_by_text('Classical')
        page_media.select_song_by_text('Acceptance')
        time.sleep(3)
        result = page_media.tap_favorite()
        self.report.new_result('bfa6ac5a-7f45-4980-b39b-70774c76da61', result)
        
        self.report.start_uuid('67b576df-2869-41a2-a329-ab1aaf7810f7')
        page_main.back()
        time.sleep(5)
        page_main.back()
        time.sleep(5)
        page_media.select_media_by_text('Recorded_Voices')
        page_media.select_song_by_text('VoiceOver.wav')
        time.sleep(3)
        result = page_media.tap_favorite()
        self.report.new_result('67b576df-2869-41a2-a329-ab1aaf7810f7', result)
        
        # Sort in Favorite folder
        self.report.start_uuid('eed51121-b3e5-4b32-b706-ad8a57e48ba2')
        page_main.back()
        time.sleep(5)
        page_media.select_media_by_text('Favorite')
        time.sleep(3)
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_name)
        page_media.click(L.import_media.music_library.sort_menu.ascending)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('Acceptance', 'mp3.mp3')
        self.report.new_result('eed51121-b3e5-4b32-b706-ad8a57e48ba2', result)
        
        self.report.start_uuid('e5573b72-4200-4bda-b04f-44bee3226a36')
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.descending)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('mp3.mp3', 'Acceptance')
        self.report.new_result('e5573b72-4200-4bda-b04f-44bee3226a36', result)
        
        self.report.start_uuid('b35f95eb-cff7-4239-8e1e-3920c6dca138')
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_duration)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('Acceptance', 'VoiceOver.wav')
        self.report.new_result('b35f95eb-cff7-4239-8e1e-3920c6dca138', result)
        
        self.report.start_uuid('30872b34-bd26-4d83-955a-4f66bfa720db')
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.ascending)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('VoiceOver.wav', 'Acceptance')
        self.report.new_result('30872b34-bd26-4d83-955a-4f66bfa720db', result)


        self.report.start_uuid('beae1276-c1b5-4f3c-abe1-c356b738f033')
        page_media.select_song_by_text('Acceptance')
        time.sleep(3)
        result = page_media.play_music_in_library()
        self.report.new_result('beae1276-c1b5-4f3c-abe1-c356b738f033', result)
        
        self.report.start_uuid('bb48e2c7-28e2-48e2-a07d-ae33b49f918b')
        result = page_media.download_music()
        self.report.new_result('bb48e2c7-28e2-48e2-a07d-ae33b49f918b', result)
        
        self.report.start_uuid('a28e0f66-ecea-41c3-b01a-54c00789224d')
        result = page_media.add_selected_song_to_timeline()
        self.report.new_result('a28e0f66-ecea-41c3-b01a-54c00789224d', result)
        
        self.report.start_uuid('42868508-3e22-497e-a2a5-f1ddf10c92d2')
        result = page_media.tap_favorite(0)
        self.report.new_result('42868508-3e22-497e-a2a5-f1ddf10c92d2', result)
    
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_17_02(self):
        logger('>>> test_sce_02_17_02: Sound Clips Favorite <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        # page_main.put_voiceover_file(self.device_udid, pdr_package)
        
        # New project
        self.report.start_uuid('326ad356-9baf-434c-aab3-4909010ebf4b')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_17_02")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.switch_to_sound_clips_library()
        time.sleep(5)
        page_media.select_media_by_text('Animals')
        page_media.select_song_by_text('Cat01')
        time.sleep(3)
        result_1 = page_media.tap_favorite()
        page_main.back()
        time.sleep(5)
        page_media.select_media_by_text('Miscellaneous')
        page_media.select_song_by_text('Bell01')
        time.sleep(3)
        result_2 = page_media.tap_favorite()
        page_main.back()
        time.sleep(5)
        page_media.select_media_by_text('People')
        page_media.select_song_by_text('Applause01')
        time.sleep(3)
        result_3 = page_media.tap_favorite()
        self.report.new_result('326ad356-9baf-434c-aab3-4909010ebf4b', result_1 and result_2 and result_3)

        # Sort in Favorite folder
        self.report.start_uuid('74ede52d-b0da-497f-be4c-a781f8e6f77e')
        page_main.back()
        time.sleep(5)
        page_media.select_media_by_text('Favorite')
        time.sleep(3)
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_name)
        page_media.click(L.import_media.music_library.sort_menu.ascending)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('Applause01', 'Cat01')
        self.report.new_result('74ede52d-b0da-497f-be4c-a781f8e6f77e', result)
        
        self.report.start_uuid('0d7c9bc6-02d2-4072-8dec-c888ac2c0931')
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.descending)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('Cat01', 'Applause01')
        self.report.new_result('0d7c9bc6-02d2-4072-8dec-c888ac2c0931', result)
        
        self.report.start_uuid('bd6bc99d-ae8b-4854-84b8-58489a4887f1')
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_duration)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('Bell01', 'Cat01')
        self.report.new_result('bd6bc99d-ae8b-4854-84b8-58489a4887f1', result)
        
        self.report.start_uuid('0ba6cffe-db0c-4e8b-bd37-9a54b6c1a5fd')
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.ascending)
        page_media.back()
        time.sleep(5)
        result = page_media.music_list_check_item('Cat01', 'Bell01')
        self.report.new_result('0ba6cffe-db0c-4e8b-bd37-9a54b6c1a5fd', result)


        self.report.start_uuid('61117523-e740-49ea-95ab-bc1cb214f9cb')
        page_media.select_song_by_text('Bell01')
        time.sleep(3)
        result = page_media.play_music_in_library()
        self.report.new_result('61117523-e740-49ea-95ab-bc1cb214f9cb', result)
        
        self.report.start_uuid('905dd75b-bed5-46f1-933e-afad4e0a6058')
        result = page_media.download_music()
        self.report.new_result('905dd75b-bed5-46f1-933e-afad4e0a6058', result)
        
        self.report.start_uuid('7ca4b1aa-74cc-497d-b3b0-5919d5ff947e')
        result = page_media.add_selected_song_to_timeline()
        self.report.new_result('7ca4b1aa-74cc-497d-b3b0-5919d5ff947e', result)
        
        self.report.start_uuid('7e6478d4-5cfc-4c1b-91a6-11f1b8b370dd')
        result = page_media.tap_favorite(0)
        self.report.new_result('7e6478d4-5cfc-4c1b-91a6-11f1b8b370dd', result)
        
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_17_03(self):
        logger('>>> test_sce_02_17_03: Sound FX Title <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        # page_main.put_voiceover_file(self.device_udid, pdr_package)
        
        # New project
        self.report.start_uuid('f7e73835-101e-400c-95f4-b2d035c78a56')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_17_03")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.back()
        time.sleep(5)
        page_media.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.select_title_category('Speech Bubbles')
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.library_unit_sound_fx_icon)
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        result = page_edit.timeline_select_item_by_index_on_track(2, 1)
        self.report.new_result('f7e73835-101e-400c-95f4-b2d035c78a56', result)
        
        
        self.report.start_uuid('60e68a5c-b959-46a1-8962-ae0879d3a1ab')
        page_edit.select_from_bottom_edit_menu('Sound FX')
        result = True if page_edit.get_opacity_value() == '100' else False
        self.report.new_result('60e68a5c-b959-46a1-8962-ae0879d3a1ab', result)
        
        self.report.start_uuid('5c3328fd-0ec4-47c3-ac6f-b14b28ab8554')
        page_edit.opacity_set_slider(1)
        result = True if page_edit.get_opacity_value() == '200' else False
        self.report.new_result('5c3328fd-0ec4-47c3-ac6f-b14b28ab8554', result)
        
        self.report.start_uuid('301f51b5-44df-4d89-b265-71b9e4928d24')
        page_edit.opacity_set_slider(0.05)
        result = True if page_edit.get_opacity_value() == '0' else False
        self.report.new_result('301f51b5-44df-4d89-b265-71b9e4928d24', result)
