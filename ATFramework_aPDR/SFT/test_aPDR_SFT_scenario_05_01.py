import sys
from os.path import dirname as dir
from pprint import pprint

from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.ATFramework.utils.log import logger
import pytest
import time
from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
sys.path.insert(0, (dir(dir(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_05_01:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger("\n[Start] Init driver session")
        desired_caps = {}
        desired_caps.update(app_config.cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        if desired_caps['udid'] == 'auto':
            del desired_caps['udid']
        logger(f"\n[Info] caps={desired_caps}")
        self.report = report
        self.device_udid = DRIVER_DESIRED_CAPS['udid']
        # ---- local mode > end ----
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

        # retry 3 time if create driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                                       desired_caps)
                if self.driver:
                    logger("\n[Done] Driver created!")
                    break
                else:
                    raise Exception("\n[Fail] Create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1

        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.report.set_driver(self.driver)
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(1)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Done] Teardown")
        self.driver.stop_driver()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_05_01(self):
        result = {}

        # sce_05_01_01
        logger("\n[Start] sce_05_01_01")
        self.report.start_uuid('d0bafbda-e361-4cbf-af80-9da541351a27')
        self.page_main.enter_launcher()
        self.page_main.enter_timeline('sce_05_01')
        result['05_01_01'] = self.page_edit.intro_video.enter_intro()
        self.report.new_result('d0bafbda-e361-4cbf-af80-9da541351a27', result['05_01_01'])

        # sce_05_01_02
        logger("\n[Start] sce_05_01_02")
        self.report.start_uuid('a110aba2-999a-4d58-85bb-cdb217d5d2e7')
        result['05_01_02'] = self.page_edit.intro_video.check_intro_caption()
        self.report.new_result('a110aba2-999a-4d58-85bb-cdb217d5d2e7', result['05_01_02'])

        # sce_05_01_04
        logger("\n[Start] sce_05_01_04")
        self.report.start_uuid('8a5cbcca-3072-45fe-ad31-5640d95b18a3')
        result['05_01_04'] = self.page_edit.intro_video.check_intro_search()
        self.report.new_result('8a5cbcca-3072-45fe-ad31-5640d95b18a3', result['05_01_04'])

        # sce_05_01_05
        logger("\n[Start] sce_05_01_05")
        self.report.start_uuid('1ae322d8-d8ec-481f-84a3-08a5fdd76adb')
        result['05_01_05'] = self.page_edit.intro_video.intro_tutorial()
        self.report.new_result('1ae322d8-d8ec-481f-84a3-08a5fdd76adb', result['05_01_05'])

        # sce_05_01_06
        logger("\n[Start] sce_05_01_06")
        self.report.start_uuid('71adbc41-8fea-4aca-a384-9afb48612000')
        result['05_01_06'] = self.page_edit.intro_video.intro_profile()
        self.report.new_result('71adbc41-8fea-4aca-a384-9afb48612000', result['05_01_06'])

        # sce_05_01_07
        logger("\n[Start] sce_05_01_07")
        self.report.start_uuid('57ee9b4b-7809-42e0-9dab-f0f2c9f913f1')
        result['05_01_07'] = self.page_edit.intro_video.my_favorite()
        self.report.new_result('57ee9b4b-7809-42e0-9dab-f0f2c9f913f1', result['05_01_07'])

        # sce_05_01_11
        if result['05_01_07']:
            logger("\n[Start] sce_05_01_11")
            self.report.start_uuid('882daf2e-a106-4ee9-9c21-69cc8c4bebe3')
            result['05_01_11'] = self.page_edit.intro_video.tap_category()
            self.report.new_result('882daf2e-a106-4ee9-9c21-69cc8c4bebe3', result['05_01_11'])
        else:
            logger("\n[Skip] sce_05_01_11")

        # sce_05_01_08, 09
        logger("\n[Start] sce_05_01_08, sce_05_01_09")
        self.report.start_uuid('9b2f2a26-aac6-4f88-bb91-25957758fa2b')
        self.report.start_uuid('6f81c401-70fb-4e16-9f23-99de8e9deef0')
        category = self.page_edit.intro_video.check_category()
        defined = ['Beauty', 'Black & White', 'Business', 'Design', 'Education', 'Event', 'Family', 'Fashion', 'Food',
                   'Fun & Playful', 'Gaming', 'Handwritten', 'Health', 'Holiday', 'Life', 'Love', 'Minimalist',
                   'Modern', 'Music', 'Nature', 'Pets', 'Repair', 'Retro', 'Season', 'Social Media', 'Sport',
                   'Technology', 'Travel']
        result['05_01_09'] = True
        for name in defined:
            if name not in category:
                result['05_01_09'] = False
                break
        result['05_01_08'] = 'CyberLink' in category
        self.report.new_result('9b2f2a26-aac6-4f88-bb91-25957758fa2b', result['05_01_08'])
        self.report.new_result('6f81c401-70fb-4e16-9f23-99de8e9deef0', result['05_01_09'])

        # sce_05_01_03
        logger("\n[Start] sce_05_01_03")
        self.report.start_uuid('ecd0fd71-aee2-40a0-a69b-52f55ebd7ed9')
        result['05_01_03'] = self.page_edit.intro_video.intro_back()
        self.report.new_result('ecd0fd71-aee2-40a0-a69b-52f55ebd7ed9', result['05_01_03'])

        # sce_05_01_10
        logger("\n[Start] sce_05_01_10")
        self.report.start_uuid('22104cdc-9087-464f-8797-5dabae9e750c')
        if result['05_01_09']:
            result['05_01_10'] = True
        else:
            result['05_01_10'] = self.page_edit.intro_video.check_scroll_category()
        self.report.new_result('22104cdc-9087-464f-8797-5dabae9e750c', result['05_01_10'])





        # # sce_05_01_11
        # logger("\n[Start] sce_05_01_11")
        # self.report.start_uuid('ecd0fd71-aee2-40a0-a69b-52f55ebd7ed9')
        # result['05_01_11'] = self.page_edit.intro_video.intro_back()
        # self.report.new_result('ecd0fd71-aee2-40a0-a69b-52f55ebd7ed9', result['05_01_11'])







    #
    # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_02(self):
    #     logger('>>> test_sce_05_01_02: Video Intro - Search Page<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # New project
    #     self.report.start_uuid('01ecaa20-c94e-4779-a668-a196727d2700')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_02")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     result = page_edit.intro_video.enter_intro_video_library()
    #     self.report.new_result('01ecaa20-c94e-4779-a668-a196727d2700', result)
    #
    #
    # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_03(self):
    #     logger('>>> test_sce_05_01_03: Video Intro - Template Details Page<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # New project
    #     self.report.start_uuid('7da7c6b3-6b84-422a-882b-467e556d856e')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_03")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     result = page_edit.intro_video.enter_intro_video_library()
    #     self.report.new_result('7da7c6b3-6b84-422a-882b-467e556d856e', result)
    #
    #
    # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_04(self):
    #     logger('>>> test_sce_05_01_04: Video Intro - Report Page<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # New project
    #     self.report.start_uuid('621de74d-2547-44ae-a39a-235e64e6e26f')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_04")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     result = page_edit.intro_video.enter_intro_video_library()
    #     self.report.new_result('621de74d-2547-44ae-a39a-235e64e6e26f', result)
    #
    #
    # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_05(self):
    #     logger('>>> test_sce_05_01_05: Video Intro - Comments Page<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # New project
    #     self.report.start_uuid('c94efe1e-e049-4606-995d-652173cd54a1')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_05")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     result = page_edit.intro_video.enter_intro_video_library()
    #     self.report.new_result('c94efe1e-e049-4606-995d-652173cd54a1', result)
    #
    # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_06(self):
    #     logger('>>> test_sce_05_01_06: Video Intro - Creator Profile Page<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # New project
    #     self.report.start_uuid('9eb3a788-de3d-41d9-a6c4-2bd33a0c82b5')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_06")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     result = page_edit.intro_video.enter_intro_video_library()
    #     self.report.new_result('9eb3a788-de3d-41d9-a6c4-2bd33a0c82b5', result)
    #
    #
    # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_07(self):
    #     logger('>>> test_sce_05_01_07: Video Intro - Edit Template<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # New project
    #     self.report.start_uuid('de952998-2613-48cb-8cc0-aa3ea4775b31')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_07")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     page_edit.intro_video.enter_intro_video_library()
    #     time.sleep(5)
    #     page_edit.intro_video.select_template_by_index(1)
    #     result = page_edit.intro_video.enter_intro_video_designer()
    #     self.report.new_result('de952998-2613-48cb-8cc0-aa3ea4775b31', result)
    #
    #     self.report.start_uuid('9da5d7ac-a916-4099-adf8-cf1c1cbd5b39')
    #     result = page_edit.intro_video.tap_back_button('leave')
    #     self.report.new_result('9da5d7ac-a916-4099-adf8-cf1c1cbd5b39', result)
    #
    #     self.report.start_uuid('5368ba24-e0a1-4563-bcad-fcc929cf6d95')
    #     page_edit.intro_video.select_template_by_index(1)
    #     page_edit.intro_video.enter_intro_video_designer()
    #     time.sleep(10)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.click(L.edit.menu.play)
    #     time.sleep(1)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('5368ba24-e0a1-4563-bcad-fcc929cf6d95', result)
    #
    #     self.report.start_uuid('5416692c-5dfd-4998-bb4d-712925d91183')
    #     result = page_edit.enter_fullscreen_preview()
    #     self.report.new_result('5416692c-5dfd-4998-bb4d-712925d91183', result)
    #
    #     self.report.start_uuid('a94359d5-950f-4ac8-8cb9-9c9f5ec6bd54')
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.click_on_preview_area()
    #     time.sleep(1)
    #     page_edit.click(L.edit.preview.btn_fullscreen_play_pause)
    #     time.sleep(3)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('a94359d5-950f-4ac8-8cb9-9c9f5ec6bd54', result)
    #
    #     self.report.start_uuid('c35bc68c-cb4e-4cab-a083-6a7cd67486e4')
    #     page_edit.click_on_preview_area()
    #     time.sleep(1)
    #     page_edit.click(L.edit.preview.btn_close_fullscreen)
    #     result = True if page_edit.is_exist(L.edit.menu.play, 10) else False
    #     self.report.new_result('c35bc68c-cb4e-4cab-a083-6a7cd67486e4', result)
    #
    # # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_08(self):
    #     logger('>>> test_sce_05_01_08: Video Intro - Edit Background Video<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # New project
    #     self.report.start_uuid('1b12117e-6941-4222-b106-042f7f9836f1')
    #     self.report.start_uuid('eac5b5dc-9fa7-4b4d-b948-6cddaa635df6')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_08")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     page_edit.intro_video.enter_intro_video_library()
    #     time.sleep(5)
    #     page_edit.intro_video.select_template_by_index(1)
    #     page_edit.intro_video.enter_intro_video_designer()
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.intro_video.select_library_entry('Media')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Replace')
    #     page_media.select_media_by_text(self.test_material_folder)
    #     page_media.select_media_by_text('mp4.mp4')
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     page_edit.el(L.edit.replace.ok_btn).click()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('1b12117e-6941-4222-b106-042f7f9836f1', result)
    #     self.report.new_result('eac5b5dc-9fa7-4b4d-b948-6cddaa635df6', result)
    #
    #     self.report.start_uuid('e9577a25-9256-46b7-90bb-6fb06e877bbe')
    #     pic_base = pic_after
    #     page_edit.intro_video.select_library_entry('Media')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Replace')
    #     page_media.select_media_by_text('Stock Video')
    #     time.sleep(5)
    #     page_media.select_media_by_order(1)
    #     page_media.download_video()
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     page_edit.el(L.edit.replace.ok_btn).click()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('e9577a25-9256-46b7-90bb-6fb06e877bbe', result)
    #
    #     self.report.start_uuid('6e57feed-e68d-4a68-85ed-90ece09522f9')
    #     pic_base = pic_after
    #     page_edit.intro_video.select_library_entry('Media')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Replace')
    #     page_media.select_media_by_text('Stock Video')
    #     page_media.select_stock_category('pixabay')
    #     time.sleep(5)
    #     page_media.select_media_by_order(1)
    #     page_media.download_video()
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     page_edit.el(L.edit.replace.ok_btn).click()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('6e57feed-e68d-4a68-85ed-90ece09522f9', result)
    #
    #     self.report.start_uuid('780893c1-2c1e-4b08-a6b7-0d7eeca13652')
    #     pic_base = pic_after
    #     page_edit.intro_video.select_library_entry('Media')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Replace')
    #     page_media.switch_to_photo_library()
    #     page_media.select_media_by_text(self.test_material_folder)
    #     page_media.select_media_by_text('bmp.bmp')
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     page_edit.el(L.edit.replace.ok_btn).click()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('780893c1-2c1e-4b08-a6b7-0d7eeca13652', result)
    #
    #     self.report.start_uuid('57ac8ada-9243-4716-8441-7d554588997c')
    #     pic_base = pic_after
    #     page_edit.intro_video.select_library_entry('Media')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Replace')
    #     page_media.switch_to_photo_library()
    #     page_media.select_media_by_text('Stock Photo')
    #     time.sleep(5)
    #     page_media.select_media_by_order(1)
    #     page_media.download_video()
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     page_edit.el(L.edit.replace.ok_btn).click()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('57ac8ada-9243-4716-8441-7d554588997c', result)
    #
    #     self.report.start_uuid('e398e51c-2bcc-44a4-8175-83505d8c3715')
    #     pic_base_0 = pic_after
    #     page_edit.intro_video.select_library_entry('Media')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Replace')
    #     page_media.select_media_by_text(self.test_material_folder)
    #     page_media.select_media_by_text('mp4.mp4')
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_media.click(L.edit.intro_video.trim_play)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('e398e51c-2bcc-44a4-8175-83505d8c3715', result)
    #
    #     self.report.start_uuid('3b3ddc03-acbc-4912-8586-f14be8e6983a')
    #     result = page_edit.replace.move_trim_area()
    #     self.report.new_result('3b3ddc03-acbc-4912-8586-f14be8e6983a', result)
    #
    #     self.report.start_uuid('293e18a4-b878-4305-a252-e4d3bc7a869d')
    #     page_media.click(L.edit.intro_video.btn_cancel)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base_0, pic_after, 3).compare_image() else False
    #     self.report.new_result('293e18a4-b878-4305-a252-e4d3bc7a869d', result)
    #
    #     self.report.start_uuid('4821e1f0-1fd7-477a-8642-1201c0f1bcd1')
    #     page_edit.intro_video.select_library_entry('Media')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Replace')
    #     page_media.select_media_by_text(self.test_material_folder_01)
    #     page_media.select_media_by_text('01_static.mp4')
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     result = True if page_edit.is_exist(L.edit.replace.warning_title) else False
    #     self.report.new_result('4821e1f0-1fd7-477a-8642-1201c0f1bcd1', result)
    #
    #     self.report.start_uuid('5a2d7b31-b331-43ed-a118-35b711f856b3')
    #     page_media.click(L.edit.replace.ok_btn)
    #     time.sleep(3)
    #     page_edit.back()
    #     time.sleep(3)
    #     page_edit.back()
    #     time.sleep(5)
    #     pic_base_0 = page_edit.get_preview_pic()
    #     page_edit.select_from_bottom_edit_menu('Crop & Range')
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_media.click(L.edit.intro_video.trim_play)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('5a2d7b31-b331-43ed-a118-35b711f856b3', result)
    #
    #     self.report.start_uuid('768d7c98-e036-4776-9e3b-70a9d07548fe')
    #     result = page_edit.replace.move_trim_area()
    #     self.report.new_result('768d7c98-e036-4776-9e3b-70a9d07548fe', result)
    #
    #     self.report.start_uuid('55cb04be-66e8-4640-9245-53b371c1deb0')
    #     page_media.click(L.edit.intro_video.btn_cancel)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base_0, pic_after, 3).compare_image() else False
    #     self.report.new_result('55cb04be-66e8-4640-9245-53b371c1deb0', result)
    #
    #     self.report.start_uuid('8ed017a1-6763-462a-9b9e-48bac192e056')
    #     page_edit.select_from_bottom_edit_menu('Crop & Range')
    #     time.sleep(5)
    #     result = page_media.click(L.edit.replace.ok_btn)
    #     self.report.new_result('8ed017a1-6763-462a-9b9e-48bac192e056', result)
    #
    #     self.report.start_uuid('5a3a3021-4249-47a5-9bb4-85ef27390089')
    #     page_edit.select_from_bottom_edit_menu('Volume')
    #     time.sleep(5)
    #     result = True if page_edit.get_opacity_value() == '100' else False
    #     self.report.new_result('5a3a3021-4249-47a5-9bb4-85ef27390089', result)
    #
    #     self.report.start_uuid('d973f9bd-7d66-406b-a95e-f70fe0c99351')
    #     page_edit.opacity_set_slider(0.05)
    #     time.sleep(5)
    #     result = True if page_edit.get_opacity_value() == '0' else False
    #     self.report.new_result('d973f9bd-7d66-406b-a95e-f70fe0c99351', result)
    #
    #     self.report.start_uuid('71294df6-c95c-4fa9-8465-e1a03c673563')
    #     page_edit.opacity_set_slider(1)
    #     time.sleep(5)
    #     result = True if page_edit.get_opacity_value() == '200' else False
    #     self.report.new_result('71294df6-c95c-4fa9-8465-e1a03c673563', result)
    #
    #     self.report.start_uuid('195802de-43b8-4776-a0f8-b7adb49e7700')
    #     page_edit.select_from_bottom_edit_menu('Filter')
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.select_from_bottom_edit_menu('SS01')
    #     time.sleep(10)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('195802de-43b8-4776-a0f8-b7adb49e7700', result)
    #
    #     self.report.start_uuid('2e7caeea-68e1-489a-b0f6-bb84cf3819f8')
    #     page_edit.opacity_set_slider(0.05)
    #     time.sleep(5)
    #     result = True if page_edit.get_opacity_value() == '0' else False
    #     self.report.new_result('2e7caeea-68e1-489a-b0f6-bb84cf3819f8', result)
    #
    #     self.report.start_uuid('da0f6504-f42c-4182-8455-fe8e0ec83c30')
    #     page_edit.opacity_set_slider(1)
    #     time.sleep(5)
    #     result = True if page_edit.get_opacity_value() == '100' else False
    #     self.report.new_result('da0f6504-f42c-4182-8455-fe8e0ec83c30', result)
    #
    #     self.report.start_uuid('77620833-7764-4763-a4ed-7bdec0152161')
    #     page_edit.click(L.edit.Blending_Sub.Reset)
    #     time.sleep(10)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('77620833-7764-4763-a4ed-7bdec0152161', result)
    #
    #     self.report.start_uuid('0e818dde-73a2-4069-ab11-ad09a12221f7')
    #     page_edit.select_from_bottom_edit_menu('SS01')
    #     time.sleep(10)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.select_from_bottom_edit_menu('None')
    #     time.sleep(10)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('0e818dde-73a2-4069-ab11-ad09a12221f7', result)
    #
    #     self.report.start_uuid('4968d627-c3f6-4c28-9309-dec4999a4541')
    #     page_edit.select_from_bottom_edit_menu('SS01')
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.back()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('4968d627-c3f6-4c28-9309-dec4999a4541', result)
    #
    # # @pytest.mark.skip
    # @report.exception_screenshot
    # def test_sce_05_01_09(self):
    #     logger('>>> test_sce_05_01_09: Video Intro - Add Default Text<<<')
    #     media_list = ['01_static.mp4']
    #     page_main = PageFactory().get_page_object("main_page", self.driver)
    #     page_edit = PageFactory().get_page_object("edit", self.driver)
    #     page_media = PageFactory().get_page_object("import_media", self.driver)
    #     # page_effect = PageFactory().get_page_object("effect", self.driver)
    #     page_produce = PageFactory().get_page_object("produce", self.driver)
    #     page_produce.ad.close_opening_ads()
    #     # create existed 16_9 project
    #     project_title = '16_9'
    #     page_main.reset_project_list(self.device_udid, pdr_package, project_title)
    #
    #     # Edit Text
    #     self.report.start_uuid('c594ca3c-8f7c-4a10-a4bb-96d9e5b2fb28')
    #     page_main.project_click_new()
    #     page_main.project_set_name("sce_05_01_09")
    #     page_main.project_set_16_9()
    #     time.sleep(5)
    #     page_edit.back()
    #     time.sleep(3)
    #     page_edit.intro_video.enter_intro_video_library()
    #     time.sleep(5)
    #     page_edit.intro_video.select_template_by_index(1)
    #     page_edit.intro_video.enter_intro_video_designer()
    #     time.sleep(5)
    #     page_edit.intro_video.select_library_entry('Add')
    #     time.sleep(5)
    #     page_edit.select_from_bottom_edit_menu('Text')
    #     page_media.select_title_by_order(1)
    #     time.sleep(5)
    #     page_media.el(L.import_media.library_gridview.add).click()
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.select_from_bottom_edit_menu('Edit Text')
    #     time.sleep(5)
    #     page_edit.el(L.edit.title_designer.title_text_edit_area).set_text("CyberLink\nTest")
    #     page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('c594ca3c-8f7c-4a10-a4bb-96d9e5b2fb28', result)
    #
    #     self.report.start_uuid('b3155857-1837-4530-838d-595ecd44c5cd')
    #     page_edit.select_from_bottom_edit_menu('Font')
    #     result = page_edit.title_designer.download_font()
    #     self.report.new_result('b3155857-1837-4530-838d-595ecd44c5cd', result)
    #
    #     self.report.start_uuid('14bf04b8-41a9-4cc6-b8f3-e6d645493785')
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.title_designer.select_font_by_name('Default')
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('14bf04b8-41a9-4cc6-b8f3-e6d645493785', result)
    #
    #     self.report.start_uuid('16f427e8-db47-47c2-8c7b-a460af8c375b')
    #     page_edit.back()
    #     page_edit.select_from_bottom_edit_menu('Designer')
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.title_designer.select_color_by_order(4)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('16f427e8-db47-47c2-8c7b-a460af8c375b', result)
    #
    #     self.report.start_uuid('adc83641-ba1d-44c2-9cbb-37f8abd0e783')
    #     pic_base = pic_after
    #     page_edit.title_designer.select_color_by_order(1)
    #     time.sleep(5)
    #     page_edit.title_designer.set_RGB_number('red', 150)
    #     page_edit.title_designer.set_RGB_number('green',200)
    #     page_edit.title_designer.set_RGB_number('blue',70)
    #     page_edit.back()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('adc83641-ba1d-44c2-9cbb-37f8abd0e783', result)
    #
    #     self.report.start_uuid('5ad54379-1f3b-4cfa-bac5-3ecf82bb99a5')
    #     page_edit.title_designer.select_tab('Format')
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.title_designer.set_font_bold()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('5ad54379-1f3b-4cfa-bac5-3ecf82bb99a5', result)
    #
    #     self.report.start_uuid('ec22cfc9-0a21-4d7e-947f-b9c8cd710df9')
    #     pic_base = pic_after
    #     page_edit.title_designer.set_font_italic()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('ec22cfc9-0a21-4d7e-947f-b9c8cd710df9', result)
    #
    #     self.report.start_uuid('87c35655-02a2-4985-a5d9-31f118d0f2af')
    #     pic_base = pic_after
    #     page_edit.click(L.edit.title_designer.align_center)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('87c35655-02a2-4985-a5d9-31f118d0f2af', result)
    #
    #     self.report.start_uuid('c8a836ff-a9bc-4c2d-a5a7-f3c5dc47006e')
    #     page_edit.title_designer.select_tab('Border')
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.title_designer.select_color_by_order(3)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('c8a836ff-a9bc-4c2d-a5a7-f3c5dc47006e', result)
    #
    #     self.report.start_uuid('3e578f84-5c36-44ab-8cb8-93bcfc309d98')
    #     pic_base = pic_after
    #     page_edit.title_designer.select_color_by_order(1)
    #     time.sleep(5)
    #     page_edit.title_designer.set_RGB_number('red', 70)
    #     page_edit.title_designer.set_RGB_number('green', 200)
    #     page_edit.title_designer.set_RGB_number('blue', 150)
    #     page_edit.back()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('3e578f84-5c36-44ab-8cb8-93bcfc309d98', result)
    #
    #     self.report.start_uuid('48430734-3f5c-45f1-ac5d-04a8249f5a64')
    #     pic_base = pic_after
    #     page_edit.title_designer.set_slider(L.edit.title_designer.slider_size, 1)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('48430734-3f5c-45f1-ac5d-04a8249f5a64', result)
    #
    #     self.report.start_uuid('74a3c28c-6b92-453c-b06c-4c655fc291dc')
    #     pic_base = pic_after
    #     page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('74a3c28c-6b92-453c-b06c-4c655fc291dc', result)
    #
    #     self.report.start_uuid('8fd883cc-533c-4544-be81-54c6409e4fc6')
    #     page_edit.title_designer.select_tab('Shadow')
    #     time.sleep(5)
    #     pic_base = page_edit.get_preview_pic()
    #     page_edit.title_designer.select_color_by_order(3)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('8fd883cc-533c-4544-be81-54c6409e4fc6', result)
    #
    #     self.report.start_uuid('7cd8126c-5a73-4853-8183-469ca12dff96')
    #     pic_base = pic_after
    #     page_edit.title_designer.select_color_by_order(1)
    #     time.sleep(5)
    #     page_edit.title_designer.set_RGB_number('red', 200)
    #     page_edit.title_designer.set_RGB_number('green', 70)
    #     page_edit.title_designer.set_RGB_number('blue', 150)
    #     page_edit.back()
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('7cd8126c-5a73-4853-8183-469ca12dff96', result)
    #
    #     self.report.start_uuid('19cc15b9-6485-49df-9e65-99beefa5fda5')
    #     pic_base = pic_after
    #     page_edit.title_designer.set_slider(L.edit.title_designer.slider_angle, 0.5)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('19cc15b9-6485-49df-9e65-99beefa5fda5', result)
    #
    #     self.report.start_uuid('bf872bd2-8c61-4b8d-88cd-386bde8030c4')
    #     pic_base = pic_after
    #     page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('bf872bd2-8c61-4b8d-88cd-386bde8030c4', result)
    #
    #     self.report.start_uuid('f830b4e6-4818-4136-bb82-66e849f4cf99')
    #     pic_base = pic_after
    #     page_edit.title_designer.set_slider(L.edit.title_designer.slider_distance, 0.5)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('f830b4e6-4818-4136-bb82-66e849f4cf99', result)
    #
    #     self.report.start_uuid('69a170a7-1fc6-40dc-886b-d135aab50eb8')
    #     pic_base = pic_after
    #     page_edit.title_designer.swipe_slider_area('up')
    #     page_edit.title_designer.swipe_slider_area('up')
    #     page_edit.title_designer.set_slider(L.edit.title_designer.slider_blur, 0.5)
    #     time.sleep(5)
    #     pic_after = page_edit.get_preview_pic()
    #     result = True if not CompareImage(pic_base, pic_after, 3).compare_image() else False
    #     self.report.new_result('69a170a7-1fc6-40dc-886b-d135aab50eb8', result)
    #
    #     self.report.start_uuid('7aa6e795-c8a1-4492-8930-b24bb797989b')
    #     self.report.start_uuid('569cc940-0417-4b58-a01f-27547aad0531')
    #     page_edit.back()
    #     page_edit.select_from_bottom_edit_menu('Animation')
    #     page_edit.select_from_bottom_edit_menu('In Animation')
    #     time.sleep(5)
    #     result = page_edit.select_from_bottom_edit_menu('Pop-up I')
    #     self.report.new_result('7aa6e795-c8a1-4492-8930-b24bb797989b', result)
    #     self.report.new_result('569cc940-0417-4b58-a01f-27547aad0531', result)
    #
    #     self.report.start_uuid('e7eb7674-608e-46a5-b05b-2e92fac0cc44')
    #     base_length = page_edit.get_opacity_value()
    #     page_edit.opacity_set_slider(0.2)
    #     time.sleep(5)
    #     after_length = page_edit.get_opacity_value()
    #     result = True if base_length > after_length else False
    #     self.report.new_result('e7eb7674-608e-46a5-b05b-2e92fac0cc44', result)
    #
    #     self.report.start_uuid('493a3b81-8771-4c92-a1aa-614484f4497f')
    #     self.report.start_uuid('112dd68b-9bf7-43af-b065-d6f4a7e019f3')
    #     page_edit.back()
    #     page_edit.select_from_bottom_edit_menu('Out Animation')
    #     time.sleep(5)
    #     result = page_edit.select_from_bottom_edit_menu('Pop-up I')
    #     self.report.new_result('493a3b81-8771-4c92-a1aa-614484f4497f', result)
    #     self.report.new_result('112dd68b-9bf7-43af-b065-d6f4a7e019f3', result)
    #
    #     self.report.start_uuid('c6bb4af3-7f07-4b40-a30e-a96dd82f54b3')
    #     base_length = page_edit.get_opacity_value()
    #     page_edit.opacity_set_slider(0.2)
    #     time.sleep(5)
    #     after_length = page_edit.get_opacity_value()
    #     result = True if base_length > after_length else False
    #     self.report.new_result('c6bb4af3-7f07-4b40-a30e-a96dd82f54b3', result)
