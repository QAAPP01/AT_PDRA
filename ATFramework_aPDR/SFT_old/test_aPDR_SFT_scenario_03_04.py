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


class Test_SFT_Scenario_03_04:
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
    def test_sce_03_04_01(self):
        media_list = ['01_static.mp4']
        self.report.start_uuid('8bcbf1df-0e7c-4afe-8295-6ed21b128aeb')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        self.report.new_result('8bcbf1df-0e7c-4afe-8295-6ed21b128aeb',
                               page_edit.check_preview_aspect_ratio(project_title))
        self.report.start_uuid('e5fce897-01bb-41c4-8244-84efe87c7065')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        # check default clip volume of main track and pip track
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.volume).click()
        page_edit.select_from_bottom_edit_menu('Volume')
        result_default_main_clip = page_edit.audio_configration_check_clip_volume('100')
        page_edit.audio_configration_set_clip_volume('200')
        result_set_main_clip = page_edit.audio_configration_check_clip_volume('200')
        self.report.new_result('e5fce897-01bb-41c4-8244-84efe87c7065',
                               True if result_default_main_clip and result_set_main_clip else False)
        self.report.start_uuid('015acdec-8fed-401c-ada8-c12ec40e8268')
        #page_edit.el(L.edit.audio_configuration.ok).click()
        # pip track
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)        
        page_edit.el(L.edit.menu.import_media).click()
        page_media.click(L.import_media.menu.music_library)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_song_by_text('mp3.mp3')
        page_media.add_selected_song_to_timeline()
        time.sleep(3)
        page_media.select_song_by_text('mp3.mp3')
        page_media.add_selected_song_to_timeline()
        time.sleep(3)
        page_media.driver.driver.back()
        time.sleep(1)
        page_media.driver.driver.back()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.volume).click()
        page_edit.select_from_bottom_edit_menu('Volume')
        self.report.new_result('015acdec-8fed-401c-ada8-c12ec40e8268',
                               page_edit.audio_configration_check_clip_volume('100'))
        self.report.start_uuid('f1684617-1186-41dc-9446-0c657518f24c')
        #page_edit.el(L.edit.audio_configuration.ok).click()
        time.sleep(1)
        # audio mixing
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.volume).click()
        #page_edit.select_from_bottom_edit_menu('Volume')
        #page_edit.el(L.edit.audio_configuration.btn_audio_mixing).click()
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.audio_mixing).click()
        time.sleep(2)
        # check default - main: 100, pip1/2: 50
        #result_default_main = page_edit.audio_mixing_check_volume('main', '100')
        #result_default_pip = True if page_edit.audio_mixing_check_volume('pip_1',
        #                                                                 '50') and page_edit.audio_mixing_check_volume(
        #    'pip_2', '50') else False
        result_default_main = page_edit.audio_mixing_check_volume(0, '100')
        result_default_pip = True if page_edit.audio_mixing_check_volume(1,'50') else False
        self.report.new_result('f1684617-1186-41dc-9446-0c657518f24c',
                               True if result_default_main and result_default_pip else False)
        # adjust value
        self.report.start_uuid('e7896e79-0d75-4afd-a58f-4936d1b600de')
        #page_edit.audio_mixing_set_volume('main', '100')
        #result_set_main = page_edit.audio_mixing_check_volume('main', '100')
        page_edit.audio_mixing_set_volume(0, '100')
        result_set_main = page_edit.audio_mixing_check_volume(0, '100')
        #page_edit.audio_mixing_set_volume('pip_1', '100')
        #result_set_pip = page_edit.audio_mixing_check_volume('pip_1', '100')        
        page_edit.audio_mixing_set_volume(1, '100')
        result_set_pip = page_edit.audio_mixing_check_volume(1, '100')
        self.report.new_result('e7896e79-0d75-4afd-a58f-4936d1b600de',
                               True if result_set_main and result_set_pip else False)
        self.report.start_uuid('d8f22526-3740-4630-9f3e-e055b2b4d664')
        #page_edit.audio_mixing_set_volume('pip_2', '80')
        #result_set_pip2 = page_edit.audio_mixing_check_volume('pip_2', '80')
        #page_edit.audio_mixing_set_volume('music_1', '80')
        #result_set_music1 = page_edit.audio_mixing_check_volume('music_1', '80')
        #page_edit.audio_mixing_set_volume('music_2', '80')
        #result_set_music2 = page_edit.audio_mixing_check_volume('music_2', '80')       
        page_edit.audio_mixing_set_volume(2, '80')
        result_set_music1 = page_edit.audio_mixing_check_volume(2, '80')
        page_edit.audio_mixing_set_volume(3, '80')
        result_set_music2 = page_edit.audio_mixing_check_volume(3, '80')
        self.report.new_result('d8f22526-3740-4630-9f3e-e055b2b4d664',
                               True if result_set_music1 and result_set_music2 else False)
        #self.report.new_result('d8f22526-3740-4630-9f3e-e055b2b4d664',
        #                       True if result_set_pip2 and result_set_music1 and result_set_music2 else False)
        self.report.start_uuid('876d937b-e217-47b1-a867-0852f9800d62')
        time.sleep(2)
        #page_edit.el(L.edit.audio_configuration.audio_mixing.ok).click()
        time.sleep(2)
        # check preview in full screen
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.enter_fullscreen_preview()
        time.sleep(1)
        page_edit.tap_screen_center()
        self.report.new_result('876d937b-e217-47b1-a867-0852f9800d62',
                               page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        time.sleep(8)
        self.report.start_uuid('a14059b9-c644-4de8-bf31-76a6262da2b0')
        self.report.new_result('a14059b9-c644-4de8-bf31-76a6262da2b0',
                               page_edit.is_exist(L.edit.preview.water_mark))
        page_edit.tap_screen_center()
        page_edit.el(L.edit.preview.btn_close_fullscreen).click()
        time.sleep(1)
        '''
        # leave and save project
        self.report.start_uuid('24f58e60-3fbe-4af4-b194-9079e0f20e06')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_main.select_existed_project_by_title(project_title)
        page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.volume).click()
        page_edit.select_from_bottom_edit_menu('Volume')
        page_edit.el(L.edit.audio_configuration.btn_audio_mixing).click()
        time.sleep(2)
        #result_set_main = page_edit.audio_mixing_check_volume('main', '100')
        #result_set_pip1 = page_edit.audio_mixing_check_volume('pip_1', '100')
        #result_set_pip2 = page_edit.audio_mixing_check_volume('pip_2', '80')
        #result_set_music1 = page_edit.audio_mixing_check_volume('music_1', '80')
        #result_set_music2 = page_edit.audio_mixing_check_volume('music_2', '80')        
        result_set_main = page_edit.audio_mixing_check_volume(0, '100')
        result_set_pip1 = page_edit.audio_mixing_check_volume(1, '100')
        result_set_music1 = page_edit.audio_mixing_check_volume(2, '80')
        result_set_music2 = page_edit.audio_mixing_check_volume(3, '80')
        self.report.new_result('24f58e60-3fbe-4af4-b194-9079e0f20e06',
                               True if result_set_main and result_set_pip1 and result_set_music1 and result_set_music2 else False)
        #                       True if result_set_main and result_set_pip1 and result_set_pip2 and result_set_music1 and result_set_music2 else False)
        # check PowerDirector for Windows in Settings
        '''
        self.report.start_uuid('f8739ef8-d36c-45dc-9c59-8af3f4772b69')
        #page_edit.el(L.edit.audio_configuration.audio_mixing.ok).click()
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(1)
        page_edit.settings.swipe_to_option('PowerDirector for PC')
        time.sleep(3)
        page_edit.el(L.edit.settings.powerdirector_for_pc_btn).click()
        time.sleep(20)
        #self.report.new_result('f8739ef8-d36c-45dc-9c59-8af3f4772b69', True if page_edit.get_chrome_url().find(
        #    'cyberlink.com/products/powerdirector-video-editing-software/features_') != -1 else False)
        self.report.new_result('f8739ef8-d36c-45dc-9c59-8af3f4772b69', True if page_edit.get_chrome_url().find(
            'cyberlink.com/products/powerdirector-video-editing-software/') != -1 else False)
        page_edit.driver.driver.back()
        time.sleep(1)
