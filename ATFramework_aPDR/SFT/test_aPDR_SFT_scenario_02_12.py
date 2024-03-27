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


class Test_SFT_Scenario_02_12:
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
    def test_sce_02_12_01(self):
        logger('>>> test_sce_02_12_01: Effect Layer <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        
        # Enter Effect Layer
        self.report.start_uuid('84a3ab36-5dbd-4522-8550-3550e4e537b8')
        page_edit.click(L.edit.menu.play)
        time.sleep(2)
        page_edit.click(L.edit.menu.play)
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.switch_to_effect_layer_library()
        time.sleep(5)
        result = page_media.search_template_by_image('highlight')
        self.report.new_result('84a3ab36-5dbd-4522-8550-3550e4e537b8', result)

        # Premium effect
        self.report.start_uuid('381221d5-f447-4bb3-bf86-295c5bd31f5d')
        result = True if page_edit.is_exist(L.edit.try_before_buy.icon_try) else False
        self.report.new_result('381221d5-f447-4bb3-bf86-295c5bd31f5d', result)

        # Add
        self.report.start_uuid('1b6d6516-5a08-4f76-8dc1-4e591422f598')
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1b6d6516-5a08-4f76-8dc1-4e591422f598', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Move
        self.report.start_uuid('d4941bf8-f4ad-4937-b609-daad3460cb0f')
        pic_base = pic_after
        page_effect.move_effect_layer()
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('d4941bf8-f4ad-4937-b609-daad3460cb0f', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Resize
        self.report.start_uuid('3eb1a209-fb96-45eb-8428-d67380c64419')
        pic_base = pic_after
        page_effect.modify_effect_layer_size()
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('3eb1a209-fb96-45eb-8428-d67380c64419', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Rotate
        self.report.start_uuid('8e592026-35bd-4e24-8b31-02f0369804b4')
        pic_base = pic_after
        page_effect.modify_effect_layer_rotate()
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('8e592026-35bd-4e24-8b31-02f0369804b4', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Split
        self.report.start_uuid('83b6603e-c7bb-4059-a6f8-e79d53a47879')
        result = page_edit.is_exist_in_bottom_edit_menu('Split')
        self.report.new_result('83b6603e-c7bb-4059-a6f8-e79d53a47879', result)
        # Type
        self.report.start_uuid('dc71348c-ee6f-4b3c-9cc4-7b876183d4a0')
        result = page_edit.is_exist_in_bottom_edit_menu('Type')
        self.report.new_result('dc71348c-ee6f-4b3c-9cc4-7b876183d4a0', result)
        # Shape
        self.report.start_uuid('64db2644-d65c-4ea6-97f9-bd0e15db09e1')
        result = page_edit.is_exist_in_bottom_edit_menu('Shape')
        self.report.new_result('64db2644-d65c-4ea6-97f9-bd0e15db09e1', result)
        # Transform Keyframe
        self.report.start_uuid('e3dcb5b1-1f43-481d-b60a-92a37393f7a1')
        result = page_edit.is_exist_in_bottom_edit_menu('Transform Keyframe')
        self.report.new_result('e3dcb5b1-1f43-481d-b60a-92a37393f7a1', result)
        # Duplicate
        self.report.start_uuid('1f8780b8-1b3e-469b-b209-9e216917416a')
        result = page_edit.is_exist_in_bottom_edit_menu('Duplicate')
        self.report.new_result('1f8780b8-1b3e-469b-b209-9e216917416a', result)

        # Shape
        self.report.start_uuid('cb088b87-0e5e-4d5f-a7b5-9283242792ea')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Shape')
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Ellipse')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('cb088b87-0e5e-4d5f-a7b5-9283242792ea', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.start_uuid('fcdacef7-3aad-4851-9660-96c0a3f3a6ee')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Rectangle')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('fcdacef7-3aad-4851-9660-96c0a3f3a6ee', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.start_uuid('314d1f53-a7cb-4a57-b219-23f094b21aa5')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Curved Edge')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        page_edit.back()
        self.report.new_result('314d1f53-a7cb-4a57-b219-23f094b21aa5', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Type - Highlight
        self.report.start_uuid('6a352703-c648-4e27-8bf1-4764c4af9aea')
        page_edit.select_from_bottom_edit_menu('Type')
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Highlight')
        time.sleep(5)
        default_value = page_edit.get_opacity_value()
        self.report.new_result('6a352703-c648-4e27-8bf1-4764c4af9aea', True if default_value == '50' else False)
        self.report.start_uuid('1e4c2d9a-8a15-45da-bc8c-27b5b349a120')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1e4c2d9a-8a15-45da-bc8c-27b5b349a120', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.start_uuid('b6e5af35-d69c-4ca0-819d-f750fe87366f')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('b6e5af35-d69c-4ca0-819d-f750fe87366f', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        self.report.start_uuid('db080071-991a-42bf-b623-e9f524510918')
        page_edit.select_from_bottom_edit_menu('Shadow')
        time.sleep(5)
        default_value = page_edit.get_opacity_value()
        self.report.new_result('db080071-991a-42bf-b623-e9f524510918', True if default_value == '50' else False)
        self.report.start_uuid('0266d25c-ef63-47b3-a57c-b71a73cf331d')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0266d25c-ef63-47b3-a57c-b71a73cf331d', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.start_uuid('cf2d40a6-6a10-42fa-be6c-c6e0776ef2d9')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('cf2d40a6-6a10-42fa-be6c-c6e0776ef2d9', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        self.report.start_uuid('0024dc3d-40c2-4a4b-8b67-9eed6e1a17a8')
        page_edit.select_from_bottom_edit_menu('Feather')
        time.sleep(5)
        default_value = page_edit.get_opacity_value()
        self.report.new_result('0024dc3d-40c2-4a4b-8b67-9eed6e1a17a8', True if default_value == '10' else False)
        self.report.start_uuid('29c1db6f-9016-48e4-b599-9b7fd683b7bb')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('29c1db6f-9016-48e4-b599-9b7fd683b7bb', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.start_uuid('34cd89d0-f18f-4433-a90b-5bf95dd0c6a6')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        page_edit.back()
        self.report.new_result('34cd89d0-f18f-4433-a90b-5bf95dd0c6a6', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Mosaic
        self.report.start_uuid('b7aed50f-8955-4cf8-8985-3b2b74179945')
        page_edit.select_from_bottom_edit_menu('Mosaic')
        time.sleep(5)
        default_value = page_edit.get_opacity_value()
        self.report.new_result('b7aed50f-8955-4cf8-8985-3b2b74179945', True if default_value == '50' else False)
        self.report.start_uuid('98e47d8f-d80d-4fd8-b182-0a409db3a011')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('98e47d8f-d80d-4fd8-b182-0a409db3a011', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.start_uuid('7a07ba06-8f3e-4940-8b78-6882825e0012')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('7a07ba06-8f3e-4940-8b78-6882825e0012', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Blur
        self.report.start_uuid('3a9d8e72-39c7-41db-9e4a-8f134f3fe4dd')
        page_edit.select_from_bottom_edit_menu('Blur')
        time.sleep(5)
        default_value = page_edit.get_opacity_value()
        self.report.new_result('3a9d8e72-39c7-41db-9e4a-8f134f3fe4dd', True if default_value == '50' else False)
        self.report.start_uuid('029816eb-91c4-4496-84fc-639023cbba34')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('029816eb-91c4-4496-84fc-639023cbba34', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.start_uuid('a0b35ad7-3362-4001-a8fc-ddb527f690c5')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('a0b35ad7-3362-4001-a8fc-ddb527f690c5', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_12_02(self):
        logger('>>> test_sce_02_12_02: Sticker Room <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)

        # Enter Effect Layer
        self.report.start_uuid('9a69264f-b7f1-4c47-b50e-6d66d4959bb8')
        self.report.start_uuid('30d17f86-86d4-4ef1-861c-fae1959fa3a0')
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.switch_to_sticker_library()
        time.sleep(5)
        result = page_media.select_template_category('Text')
        self.report.new_result('9a69264f-b7f1-4c47-b50e-6d66d4959bb8', result)
        self.report.new_result('30d17f86-86d4-4ef1-861c-fae1959fa3a0', result)

        self.report.start_uuid('0e9b22d4-a66c-458b-8861-0f51b0a3ceff')
        self.report.start_uuid('fbb4531c-94d0-4894-bc11-f36012656f7b')
        page_media.search_template_by_image('sticker')
        time.sleep(10)
        result = True if page_media.is_exist(L.import_media.library_gridview.add_sticker) else False
        self.report.new_result('0e9b22d4-a66c-458b-8861-0f51b0a3ceff', result)
        self.report.new_result('fbb4531c-94d0-4894-bc11-f36012656f7b', result)

        self.report.start_uuid('9b138660-c8ce-40ee-a44b-17eb79306f26')
        page_media.click(L.import_media.library_gridview.add_sticker)
        time.sleep(10)
        result = page_edit.timeline_select_item_by_index_on_track(2, 1)
        self.report.new_result('9b138660-c8ce-40ee-a44b-17eb79306f26', result)

        self.report.start_uuid('d684f15f-3fa9-4337-a5b9-35e0a0c7e3a4')
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.switch_to_sticker_library()
        time.sleep(5)
        result = True if page_media.is_exist(L.import_media.library_gridview.icon_try_sticker) else False
        self.report.new_result('d684f15f-3fa9-4337-a5b9-35e0a0c7e3a4', result)

        self.report.start_uuid('94ef9d40-cf25-4db5-9549-a70c0071095f')
        page_edit.click(L.import_media.library_gridview.icon_try_sticker)
        time.sleep(10)
        page_edit.click(L.import_media.library_gridview.icon_try_sticker)
        time.sleep(5)
        result = page_edit.trying_premium_content('try')
        self.report.new_result('94ef9d40-cf25-4db5-9549-a70c0071095f', result)

        self.report.start_uuid('c31ee222-584b-436d-a191-a06c2a267f80')
        time.sleep(5)
        result = page_media.select_template_category('Downloaded')
        self.report.new_result('c31ee222-584b-436d-a191-a06c2a267f80', result)
