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


class Test_SFT_Scenario_02_04:
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
    def test_sce_02_04_01(self):
        media_list = ['01_static.mp4']
        self.report.start_uuid('feb1ee58-7e07-4b8e-a85c-247962411769')
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
        self.report.new_result('feb1ee58-7e07-4b8e-a85c-247962411769',
                               page_edit.check_preview_aspect_ratio(project_title))
        self.report.start_uuid('ab9fab56-8d6c-4b50-b006-6115de7f85df')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        # check default clip volume of main track and pip track
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.volume).click()
        page_edit.select_from_bottom_edit_menu('Volume')
        result_default_main_clip = page_edit.audio_configration_check_clip_volume('100')
        page_edit.audio_configration_set_clip_volume('200')
        result_set_main_clip = page_edit.audio_configration_check_clip_volume('200')
        self.report.new_result('ab9fab56-8d6c-4b50-b006-6115de7f85df',
                               True if result_default_main_clip and result_set_main_clip else False)
        self.report.start_uuid('3d616854-3904-4ae2-bbbb-987595e8d992')
        #page_edit.el(L.edit.audio_configuration.ok).click()
        # pip track
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(3)
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        # page_edit.driver.driver.back()
        # time.sleep(1)
        # page_edit.driver.driver.back()
        # time.sleep(1)
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
        self.report.new_result('3d616854-3904-4ae2-bbbb-987595e8d992',
                               page_edit.audio_configration_check_clip_volume('100'))
        self.report.start_uuid('f1f36a38-ae3b-43ac-9fcd-408e7c75cf48')
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
        # check default - main_track clip: 100, pip track clip:
        #result_default_main = page_edit.audio_mixing_check_volume('main', '100')
        result_default_main = page_edit.audio_mixing_check_volume(0, '100')
        result_default_pip = True if page_edit.audio_mixing_check_volume(1, '50') else False
        #result_default_pip = True if page_edit.audio_mixing_check_volume('pip_1', '50') 
        #            and page_edit.audio_mixing_check_volume('pip_2', '50') else False
        self.report.new_result('f1f36a38-ae3b-43ac-9fcd-408e7c75cf48',
                               True if result_default_main and result_default_pip else False)
        # adjust value
        self.report.start_uuid('4b8ec648-d249-4ce8-8daa-a814c3defbed')
        #page_edit.audio_mixing_set_volume('main', '100')
        page_edit.audio_mixing_set_volume(0, '100')
        #result_set_main = page_edit.audio_mixing_check_volume('main', '100')
        result_set_main = page_edit.audio_mixing_check_volume(0, '100')
        #page_edit.audio_mixing_set_volume('pip_1', '100')
        page_edit.audio_mixing_set_volume(1, '100')
        #result_set_pip = page_edit.audio_mixing_check_volume('pip_1', '100')
        result_set_pip = page_edit.audio_mixing_check_volume(1, '100')
        self.report.new_result('4b8ec648-d249-4ce8-8daa-a814c3defbed',
                               True if result_set_main and result_set_pip else False)
        self.report.start_uuid('7dfd3d49-7fc7-46c9-9675-b35da23bd587')
        #page_edit.audio_mixing_set_volume('pip_2', '80')
        #result_set_pip2 = page_edit.audio_mixing_check_volume('pip_2', '80')
        #page_edit.audio_mixing_set_volume('music_1', '80')
        page_edit.audio_mixing_set_volume(2, '80')
        #result_set_music1 = page_edit.audio_mixing_check_volume('music_1', '80')
        result_set_music1 = page_edit.audio_mixing_check_volume(2, '80')
        #page_edit.audio_mixing_set_volume('music_2', '80')
        page_edit.audio_mixing_set_volume(3, '80')
        #result_set_music2 = page_edit.audio_mixing_check_volume('music_2', '80')
        result_set_music2 = page_edit.audio_mixing_check_volume(3, '80')
        self.report.new_result('7dfd3d49-7fc7-46c9-9675-b35da23bd587',
                               True if result_set_music1 and result_set_music2 else False)
        #                       True if result_set_pip2 and result_set_music1 and result_set_music2 else False)
        # self.report.start_uuid('b250439d-85c7-45ea-bda0-fc4af98352a8')
        # time.sleep(2)
        # #page_edit.el(L.edit.audio_configuration.audio_mixing.ok).click()
        # time.sleep(2)
        # # check preview in full screen
        # page_edit.driver.driver.back()
        # time.sleep(1)
        # page_edit.enter_fullscreen_preview()
        # time.sleep(1)
        # page_edit.tap_screen_center()
        # self.report.new_result('b250439d-85c7-45ea-bda0-fc4af98352a8',
        #                        page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        # time.sleep(8)
        # self.report.start_uuid('16704bf9-cc84-4392-85af-df18613b5c3b')
        # self.report.new_result('16704bf9-cc84-4392-85af-df18613b5c3b',
        #                        page_edit.is_exist(L.edit.preview.water_mark))
        # leave and save project
        # # self.report.start_uuid('4a281943-5aeb-497f-80ef-c9e338e513a4')
        # page_edit.tap_screen_center()
        # page_edit.el(L.edit.preview.btn_close_fullscreen).click()
        # time.sleep(1)
        '''
        page_edit.el(L.edit.menu.back).click()
        time.sleep(1)
        #page_edit.driver.driver.back()
        #page_edit.el(L.main.project_info.btn_back).click()
        #logger('project info closed.')
        time.sleep(3)
        page_main.ad.close_full_page_ad()
        page_main.select_existed_project_by_title(project_title)
        page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2) 
        #page_edit.timeline_select_item_by_index_on_track(1, 1)
        #time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.volume).click()
        #page_edit.select_from_bottom_edit_menu('Volume')
        #page_edit.el(L.edit.audio_configuration.btn_audio_mixing).click()
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.audio_mixing).click()
        time.sleep(2)
        #result_set_main = page_edit.audio_mixing_check_volume('main', '100')
        result_set_main = page_edit.audio_mixing_check_volume(0, '100')
        #result_set_pip1 = page_edit.audio_mixing_check_volume('pip_1', '100')
        result_set_pip1 = page_edit.audio_mixing_check_volume(1, '100')
        #result_set_pip2 = page_edit.audio_mixing_check_volume('pip_2', '80')
        #result_set_music1 = page_edit.audio_mixing_check_volume('music_1', '80')
        result_set_music1 = page_edit.audio_mixing_check_volume(2, '80')
        #result_set_music2 = page_edit.audio_mixing_check_volume('music_2', '80')
        result_set_music2 = page_edit.audio_mixing_check_volume(3, '80')
        self.report.new_result('4a281943-5aeb-497f-80ef-c9e338e513a4',
                               True if result_set_main and result_set_pip1 and result_set_music1 and result_set_music2 else False)
        #                       True if result_set_main and result_set_pip1 and result_set_pip2 and result_set_music1 and result_set_music2 else False)
        '''
        # check PowerDirector for Windows in Settings
        self.report.start_uuid('314979e7-d4d4-4455-a3aa-89e63ecbfde1')
        #page_edit.el(L.edit.audio_configuration.audio_mixing.ok).click()
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(1)
        page_edit.settings.swipe_to_option('PowerDirector for PC')
        time.sleep(3)
        page_edit.el(L.edit.settings.powerdirector_for_pc_btn).click()
        #self.report.new_result('314979e7-d4d4-4455-a3aa-89e63ecbfde1', True if page_edit.get_chrome_url().find(
        #    'cyberlink.com/products/powerdirector-video-editing-software/features_') != -1 else False)
        self.report.new_result('314979e7-d4d4-4455-a3aa-89e63ecbfde1', True if page_edit.get_chrome_url().find(
            'cyberlink.com/products/powerdirector-video-editing-software/') != -1 else False)
        page_edit.driver.driver.back()
        time.sleep(1)
