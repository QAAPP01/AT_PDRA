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


class Test_SFT_Scenario_02_18:
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
    def test_sce_02_18_01(self):
        logger('>>> test_sce_02_18_01: Animation - Video Clip <<<')
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
        
        # New project
        self.report.start_uuid('9996c977-d294-4f0a-bb7b-bacb6850f519')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_18_01")
        page_main.project_set_16_9()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_video_library()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Animation')
        time.sleep(3)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('9996c977-d294-4f0a-bb7b-bacb6850f519', result)

        self.report.start_uuid('94a574a3-5865-4284-9db1-7048bf89a6f6')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('94a574a3-5865-4284-9db1-7048bf89a6f6', result)

        self.report.start_uuid('78a35efa-3130-42cc-9d46-b11639b85f30')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('78a35efa-3130-42cc-9d46-b11639b85f30', result)

        self.report.start_uuid('8ab38720-74ed-4907-9b13-8fea7fc92ad9')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('8ab38720-74ed-4907-9b13-8fea7fc92ad9', result)

        self.report.start_uuid('3b77adf6-a582-4799-bd71-7abcbbe6f77a')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('3b77adf6-a582-4799-bd71-7abcbbe6f77a', result)

        self.report.start_uuid('a6641b8f-9d2e-4b8e-81ad-b6f4d82d2f4f')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('a6641b8f-9d2e-4b8e-81ad-b6f4d82d2f4f', result)

        self.report.start_uuid('ab63db00-3f92-4807-9606-3ed28a63ab9a')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('ab63db00-3f92-4807-9606-3ed28a63ab9a', result)

        self.report.start_uuid('d19b7e22-17b2-4afc-9259-677415cce76a')
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('d19b7e22-17b2-4afc-9259-677415cce76a', result)

        self.report.start_uuid('297dca7e-4d49-4669-8c83-bbf7bc0e4b95')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('297dca7e-4d49-4669-8c83-bbf7bc0e4b95', result)

        self.report.start_uuid('ff7a22e5-2073-4426-8194-1f1c4ececdd7')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('ff7a22e5-2073-4426-8194-1f1c4ececdd7', result)

        self.report.start_uuid('dd05f293-9d74-4e5f-9dac-b724f4eb80f9')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('dd05f293-9d74-4e5f-9dac-b724f4eb80f9', result)

        self.report.start_uuid('c0151590-b002-4b79-ada9-137a3b671ce9')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('c0151590-b002-4b79-ada9-137a3b671ce9', result)

        self.report.start_uuid('50b67aa2-03ec-45d1-b72d-63f4389ebce7')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('50b67aa2-03ec-45d1-b72d-63f4389ebce7', result)

        self.report.start_uuid('be3a8055-9252-4138-8277-fe52d5115249')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('be3a8055-9252-4138-8277-fe52d5115249', result)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_18_02(self):
        logger('>>> test_sce_02_18_02: Animation - Photo Clip <<<')
        media_list = ['png.png']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        # New project
        self.report.start_uuid('04f7ac88-7ca0-4649-9026-037e32503c12')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_18_02")
        page_main.project_set_16_9()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Animation')
        time.sleep(3)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('04f7ac88-7ca0-4649-9026-037e32503c12', result)

        self.report.start_uuid('b1034504-b639-4d8b-86bb-be000e3a95ea')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('b1034504-b639-4d8b-86bb-be000e3a95ea', result)

        self.report.start_uuid('971fa609-cc2d-4436-a04f-b2a838836802')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('971fa609-cc2d-4436-a04f-b2a838836802', result)

        self.report.start_uuid('2b472549-3db1-45c2-909f-435a25b82443')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('2b472549-3db1-45c2-909f-435a25b82443', result)

        self.report.start_uuid('5d0d6139-f677-484f-ab93-fbbd1fb43e30')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('5d0d6139-f677-484f-ab93-fbbd1fb43e30', result)

        self.report.start_uuid('640ae5e8-55a3-4b90-8667-180b271c3772')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('640ae5e8-55a3-4b90-8667-180b271c3772', result)

        self.report.start_uuid('42b265cc-6dd1-4936-b7dd-10b3779a0cf9')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('42b265cc-6dd1-4936-b7dd-10b3779a0cf9', result)

        self.report.start_uuid('35608057-fdd2-49bc-b098-c92585ed1c4f')
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('35608057-fdd2-49bc-b098-c92585ed1c4f', result)

        self.report.start_uuid('d43131ab-ab9c-4eb3-974b-508f71889e55')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('d43131ab-ab9c-4eb3-974b-508f71889e55', result)

        self.report.start_uuid('1f9583d9-42b5-4152-ba12-d3b7734097d8')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('1f9583d9-42b5-4152-ba12-d3b7734097d8', result)

        self.report.start_uuid('541ddc79-acea-4867-8862-c5c684f054c7')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('541ddc79-acea-4867-8862-c5c684f054c7', result)

        self.report.start_uuid('5926cac2-cb3b-4ad5-8ebc-cb461401e0e2')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('5926cac2-cb3b-4ad5-8ebc-cb461401e0e2', result)

        self.report.start_uuid('a4f5a229-880d-4605-af25-5c3dadf926b7')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('a4f5a229-880d-4605-af25-5c3dadf926b7', result)

        self.report.start_uuid('57d01ef0-97a1-4668-a791-c7309ce42205')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('57d01ef0-97a1-4668-a791-c7309ce42205', result)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_18_03(self):
        logger('>>> test_sce_02_18_03: Animation - Sticker Clip <<<')
        media_list = ['png.png']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        # New project
        self.report.start_uuid('600a59ea-4d95-4f33-b467-b4fe759b43ff')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_18_03")
        page_main.project_set_16_9()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_sticker_library()
        time.sleep(3)
        page_media.select_sticker_by_order(1)
        time.sleep(10)
        page_edit.select_from_bottom_edit_menu('Animation')
        time.sleep(3)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('600a59ea-4d95-4f33-b467-b4fe759b43ff', result)

        self.report.start_uuid('2e85654a-e9b0-4638-91da-8ff940d008b9')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('2e85654a-e9b0-4638-91da-8ff940d008b9', result)

        self.report.start_uuid('22b96075-bcfa-4de8-b9db-ce0ff1c708d1')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('22b96075-bcfa-4de8-b9db-ce0ff1c708d1', result)

        self.report.start_uuid('8b90bf3d-9311-479c-b5a9-c8bf347478ce')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('8b90bf3d-9311-479c-b5a9-c8bf347478ce', result)

        self.report.start_uuid('54a46b5e-398a-4dfb-8b47-f99281c40bd5')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('54a46b5e-398a-4dfb-8b47-f99281c40bd5', result)

        self.report.start_uuid('42d30788-da6f-4b70-87e5-8fa662843209')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('42d30788-da6f-4b70-87e5-8fa662843209', result)

        self.report.start_uuid('c475442b-c8ed-4b2d-ba31-14047a8a89fa')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('c475442b-c8ed-4b2d-ba31-14047a8a89fa', result)

        self.report.start_uuid('935ba437-f39e-4252-9749-5cf7bff71b6e')
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('935ba437-f39e-4252-9749-5cf7bff71b6e', result)

        self.report.start_uuid('d2214d07-ee9e-4560-b366-7725248bf628')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('d2214d07-ee9e-4560-b366-7725248bf628', result)

        self.report.start_uuid('2b30a561-c202-491b-a30c-7ff69975a854')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('2b30a561-c202-491b-a30c-7ff69975a854', result)

        self.report.start_uuid('87b5275a-1f1a-4554-b83f-8a2c1e41d26c')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('87b5275a-1f1a-4554-b83f-8a2c1e41d26c', result)

        self.report.start_uuid('403f9231-bb3b-4da5-a0d4-039014ffe159')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('403f9231-bb3b-4da5-a0d4-039014ffe159', result)

        self.report.start_uuid('62d43ef8-97c5-406f-99f2-747380d56189')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('62d43ef8-97c5-406f-99f2-747380d56189', result)

        self.report.start_uuid('7bcdab84-5fdd-497b-81c8-41dfa90f3f3d')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('7bcdab84-5fdd-497b-81c8-41dfa90f3f3d', result)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_18_04(self):
        logger('>>> test_sce_02_18_04: Animation - Colorboard Clip <<<')
        media_list = ['png.png']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        # New project
        self.report.start_uuid('da7f5bcf-c604-4da0-987b-9f88f658341b')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_18_04")
        page_main.project_set_16_9()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text('Color Board')
        time.sleep(3)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Animation')
        time.sleep(3)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('da7f5bcf-c604-4da0-987b-9f88f658341b', result)

        self.report.start_uuid('414d1cf3-5984-4ac0-8d73-79205c45e7d0')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('414d1cf3-5984-4ac0-8d73-79205c45e7d0', result)

        self.report.start_uuid('e843d1b0-13b2-4c88-83f3-4cf7464a32d6')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('e843d1b0-13b2-4c88-83f3-4cf7464a32d6', result)

        self.report.start_uuid('db77facb-18ad-4dfe-b98f-a4fa438efde3')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('db77facb-18ad-4dfe-b98f-a4fa438efde3', result)

        self.report.start_uuid('3bb074a7-5942-41b7-9e15-f19509dc3635')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('3bb074a7-5942-41b7-9e15-f19509dc3635', result)

        self.report.start_uuid('f22b15a2-abcb-4e09-a5d1-0cfbf1a5f9bb')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('f22b15a2-abcb-4e09-a5d1-0cfbf1a5f9bb', result)

        self.report.start_uuid('bd1b8b2c-34cb-4099-a6f3-bc9dba9b0355')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('bd1b8b2c-34cb-4099-a6f3-bc9dba9b0355', result)

        self.report.start_uuid('aba2356b-bdf9-4b23-9c03-5c14e71f54cd')
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.edit_sub.in_animation_entry)
        time.sleep(3)
        result = page_edit.select_from_bottom_edit_menu('None')
        self.report.new_result('aba2356b-bdf9-4b23-9c03-5c14e71f54cd', result)

        self.report.start_uuid('468d7cf4-c7e5-4a3d-969f-02d1dd5e5870')
        page_edit.select_from_bottom_edit_menu('Zoom Out 01')
        result = page_edit.check_premium_features_used()
        self.report.new_result('468d7cf4-c7e5-4a3d-969f-02d1dd5e5870', result)

        self.report.start_uuid('cf401a16-01a3-49bf-befd-f94d9b531b13')
        result = page_edit.select_from_bottom_edit_menu('Blur')
        self.report.new_result('cf401a16-01a3-49bf-befd-f94d9b531b13', result)

        self.report.start_uuid('3bb8b410-ffe4-4543-af8c-ad0fb5bc7101')
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.8' else False
        self.report.new_result('3bb8b410-ffe4-4543-af8c-ad0fb5bc7101', result)

        self.report.start_uuid('9b3f30de-1015-45dd-9125-39b52068552c')
        page_edit.opacity_set_slider(1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '5.0' else False
        self.report.new_result('9b3f30de-1015-45dd-9125-39b52068552c', result)

        self.report.start_uuid('c8b8d583-4a17-4f73-831b-1769ae4905d2')
        page_edit.opacity_set_slider(0.1)
        duration = page_edit.get_opacity_value()
        result = True if duration == '0.1' else False
        self.report.new_result('c8b8d583-4a17-4f73-831b-1769ae4905d2', result)

        self.report.start_uuid('1a41a168-0c3b-4dde-a833-35476eed34c6')
        page_edit.select_from_bottom_edit_menu('None')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('1a41a168-0c3b-4dde-a833-35476eed34c6', result)
