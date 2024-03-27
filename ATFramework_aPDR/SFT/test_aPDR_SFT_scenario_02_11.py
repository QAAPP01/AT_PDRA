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


class Test_SFT_Scenario_02_11:
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
                                                              
        # retry 3 time if create driver fail
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
    def test_sce_02_11_01(self):
        logger('>>> test_sce_02_11_01: Video template <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.remove_video_templates(self.device_udid, pdr_package)
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        # page_main.subscribe()
        
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        
        # Enter Video Template library
        self.report.start_uuid('887b1c51-c069-47d9-aa07-c29f599737e0')
        # page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_media.click(L.edit.menu.import_media)
        page_media.switch_to_template_library()
        result = page_media.search_template_by_image('videotemplate')
        # result = page_media.select_media_by_order(1)
        self.report.new_result('887b1c51-c069-47d9-aa07-c29f599737e0', result)

        # Select category template
        self.report.start_uuid('6f041f67-2a37-47d6-b1f9-c3d8d4f5e573')
        self.report.start_uuid('158b06ef-720e-4b2f-962e-0780b76471ed')
        result = page_media.select_template_category('Simple')
        self.report.new_result('6f041f67-2a37-47d6-b1f9-c3d8d4f5e573', result)
        self.report.new_result('158b06ef-720e-4b2f-962e-0780b76471ed', result)

        self.report.start_uuid('259fa333-3a67-4ad2-9246-6b822f80f227')
        result = page_media.check_category_is_highlighted('Simple')
        self.report.new_result('259fa333-3a67-4ad2-9246-6b822f80f227', result)

        # Download template
        self.report.start_uuid('f5e8c1ea-f355-43b1-8f4b-7751f2c1d092')
        result = page_media.download_video()
        self.report.new_result('f5e8c1ea-f355-43b1-8f4b-7751f2c1d092', result)

        self.report.start_uuid('b41642e1-10ff-46e6-8766-5e235262ce3f')
        result = page_media.is_exist(L.import_media.library_gridview.play)
        self.report.new_result('b41642e1-10ff-46e6-8766-5e235262ce3f', result)

        # Add to timeline - intro
        self.report.start_uuid('1059e1f2-00e4-47e3-9622-cb61d54c01f2')
        self.report.start_uuid('c72f8469-a93c-45b1-b517-99d40bf89b5b')
        self.report.start_uuid('ec5d3514-d630-4872-8d73-c056681aeea7')
        result, result_premium = page_media.add_video_template_to_timeline('intro')
        self.report.new_result('1059e1f2-00e4-47e3-9622-cb61d54c01f2', result)
        self.report.new_result('c72f8469-a93c-45b1-b517-99d40bf89b5b', result)
        self.report.new_result('ec5d3514-d630-4872-8d73-c056681aeea7', result_premium)

        # Add to timeline - outro
        self.report.start_uuid('ae4fbdcf-a930-4658-a4b2-f700191d0175')
        self.report.start_uuid('768f572d-60a5-4163-add5-b09c75292cce')
        result, result_premium = page_media.add_video_template_to_timeline('outro')
        self.report.new_result('ae4fbdcf-a930-4658-a4b2-f700191d0175', result)
        self.report.new_result('768f572d-60a5-4163-add5-b09c75292cce', result)

        # Edit functions: Video
        self.report.start_uuid('186e614c-e9b4-497e-ae9d-5b412080d6b9')
        page_main.click(L.import_media.menu.back)
        time.sleep(5)
        # page_edit.timeline_select_item_on_track('0014_16_9.mp4', 1, 'Video')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_edit.click(L.edit.menu.play)
        time.sleep(2)
        page_edit.click(L.edit.menu.play)
        result = page_edit.select_from_bottom_edit_menu('Split')
        self.report.new_result('186e614c-e9b4-497e-ae9d-5b412080d6b9', result)

        self.report.start_uuid('b98b6b45-1676-49fb-8c80-2266781e4a43')
        result = page_edit.select_from_bottom_edit_menu('Audio Mixing')
        page_edit.back()
        self.report.new_result('b98b6b45-1676-49fb-8c80-2266781e4a43', result)

        self.report.start_uuid('1970b93f-5856-4d25-a10b-cf91355a145d')
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        page_edit.back()
        self.report.new_result('1970b93f-5856-4d25-a10b-cf91355a145d', result)

        # Edit functions: Title
        self.report.start_uuid('feb607a1-fe3f-4432-b288-0174f1b8cc7e')
        page_edit.select_title_from_timeline('SUBSCRIBE')
        result = page_edit.select_from_bottom_edit_menu('Split')
        time.sleep(5)
        self.report.new_result('feb607a1-fe3f-4432-b288-0174f1b8cc7e', result)

        self.report.start_uuid('54c4972d-f188-4ae7-8c70-fdbc0d5415e0')
        page_edit.select_from_bottom_edit_menu('Edit Text')
        page_edit.el(L.edit.title_designer.title_text_edit_area).set_text('CyberLink\ntest')
        result = True if page_edit.el(L.edit.title_designer.title_text_edit_area).text == 'CyberLink\ntest' else False
        page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
        time.sleep(5)
        self.report.new_result('54c4972d-f188-4ae7-8c70-fdbc0d5415e0', result)

        self.report.start_uuid('b890ead9-ab30-4f25-8a0a-8f274558d71c')
        result = page_edit.select_from_bottom_edit_menu('Title Designer')
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        self.report.new_result('b890ead9-ab30-4f25-8a0a-8f274558d71c', result)

        self.report.start_uuid('8e8981d4-8ea3-487c-b9d7-e29500e477a6')
        result = page_edit.select_from_bottom_edit_menu('Backdrop')
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        self.report.new_result('8e8981d4-8ea3-487c-b9d7-e29500e477a6', result)

        self.report.start_uuid('76e4e4c5-3859-46ab-a821-673640f9d0d4')
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        self.report.new_result('76e4e4c5-3859-46ab-a821-673640f9d0d4', result)

        # Edit functions: MGT
        self.report.start_uuid('6779a1b4-116e-4448-8080-2c8ad6e636f5')
        page_edit.select_title_from_timeline('THANKS')
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Edit Text')
        page_edit.el(L.edit.title_designer.title_text_edit_area).set_text('MGT\ntest')
        result = True if page_edit.el(L.edit.title_designer.title_text_edit_area).text == 'MGT\ntest' else False
        page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
        time.sleep(5)
        self.report.new_result('6779a1b4-116e-4448-8080-2c8ad6e636f5', result)

        self.report.start_uuid('663dea7c-d2a6-4dd4-8a30-722a9b00defa')
        result = page_edit.select_from_bottom_edit_menu('Font')
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        self.report.new_result('663dea7c-d2a6-4dd4-8a30-722a9b00defa', result)

        self.report.start_uuid('06fc9082-ce32-4b88-af45-4b55e5e5b31d')
        result = page_edit.select_from_bottom_edit_menu('Color')
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        self.report.new_result('06fc9082-ce32-4b88-af45-4b55e5e5b31d', result)

        self.report.start_uuid('feb8c151-9182-4a6a-bf4b-bf74833303bf')
        page_edit.el(L.edit.motion_graphic_title.dropdownmenu_text).click()
        time.sleep(5)
        result = page_edit.mgt_select_title_from_menu(2)
        time.sleep(5)
        self.report.new_result('feb8c151-9182-4a6a-bf4b-bf74833303bf', result)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_11_02(self):
        logger('>>> test_sce_02_11_02: Overlay Room <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.remove_video_templates(self.device_udid, pdr_package)
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)

        # Enter Overlay library
        self.report.start_uuid('53a794b9-9645-40df-a078-5d49dac45708')
        self.report.start_uuid('d10771dd-58ee-4080-ae5f-47101195cba7')
        page_media.click(L.edit.menu.fx_layer)
        page_media.switch_to_overlay_library()
        result = page_media.is_exist(L.import_media.library_gridview.template_library_category_list)
        self.report.new_result('53a794b9-9645-40df-a078-5d49dac45708', result)
        self.report.new_result('d10771dd-58ee-4080-ae5f-47101195cba7', result)

        # Select category
        self.report.start_uuid('470b7f8d-3704-49a9-bd2e-1ab587fa460b')
        result = page_media.select_template_category('Frame')
        self.report.new_result('470b7f8d-3704-49a9-bd2e-1ab587fa460b', result)

        self.report.start_uuid('d29d243c-ba4f-4823-a61c-a521296e2749')
        result = page_media.check_category_is_highlighted('Frame')
        self.report.new_result('d29d243c-ba4f-4823-a61c-a521296e2749', result)

        self.report.start_uuid('92bbe04c-1aea-4bc0-95ea-a2a706b14a10')
        page_media.select_template_category('Light')
        page_media.search_template_by_image('overlay')
        result = page_media.download_video()
        self.report.new_result('92bbe04c-1aea-4bc0-95ea-a2a706b14a10', result)

        self.report.start_uuid('07a567d3-aecc-4aa0-afc1-1ffad3c7cde7')
        result = page_media.is_exist(L.import_media.library_gridview.play)
        self.report.new_result('07a567d3-aecc-4aa0-afc1-1ffad3c7cde7', result)

        # Premium dialog
        self.report.start_uuid('8d226161-4506-480e-bd6c-668ddab1f92e')
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        result = page_edit.trying_premium_content('sub')
        time.sleep(5)
        page_edit.click(L.main.subscribe.back_btn)
        time.sleep(5)
        self.report.new_result('8d226161-4506-480e-bd6c-668ddab1f92e', result)

        self.report.start_uuid('5ca44fbd-30b2-4538-9124-6f4f48a98964')
        result = page_edit.trying_premium_content('try')
        time.sleep(5)
        self.report.new_result('5ca44fbd-30b2-4538-9124-6f4f48a98964', result)

        # Edit functions
        self.report.start_uuid('809c95c2-0b05-4c52-943d-84f25f3093f7')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.click(L.edit.menu.play)
        time.sleep(2)
        page_edit.click(L.edit.menu.play)
        result = page_edit.select_from_bottom_edit_menu('Split')
        time.sleep(5)
        self.report.new_result('809c95c2-0b05-4c52-943d-84f25f3093f7', result)

        self.report.start_uuid('1f9af490-bebb-4947-bbe4-220b307814b7')
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        self.report.new_result('1f9af490-bebb-4947-bbe4-220b307814b7', result)