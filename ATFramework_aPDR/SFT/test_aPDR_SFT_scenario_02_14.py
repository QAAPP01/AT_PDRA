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


from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01


pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_02_14:
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
    
    def test_sce_02_14_01(self):
        logger('>>> test_sce_02_14_01: Facilitate Usage <<<')
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
        
        # New project
        self.report.start_uuid('57f86e19-21ef-427b-a5cd-74903b01e9c8')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_14_01")
        page_main.project_set_16_9()
        time.sleep(5)
        result = page_edit.is_exist(L.edit.timeline.btn_import)
        self.report.new_result('57f86e19-21ef-427b-a5cd-74903b01e9c8', not result)

        self.report.start_uuid('1f8416d8-4e6e-4d7c-a3ff-49f7b09fe0a4')
        page_edit.back()
        time.sleep(5)
        result = page_edit.is_exist(L.edit.timeline.btn_import)
        self.report.new_result('1f8416d8-4e6e-4d7c-a3ff-49f7b09fe0a4', result)

        self.report.start_uuid('52916c54-30cc-42e5-a41b-733aa7900b3f')
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        result = page_edit.is_exist(L.edit.timeline.btn_import)
        page_edit.back()
        time.sleep(5)
        self.report.new_result('52916c54-30cc-42e5-a41b-733aa7900b3f', not result)

        self.report.start_uuid('bd53c6c1-7318-41b4-81ce-c80b93591e2c')
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        result = page_edit.is_exist(L.edit.timeline.btn_import)
        page_edit.back()
        time.sleep(5)
        self.report.new_result('bd53c6c1-7318-41b4-81ce-c80b93591e2c', not result)

        self.report.start_uuid('3fa38922-fb9e-4183-8dcb-7345087f6019')
        page_edit.click(L.edit.preview.import_tips_icon)
        result = page_media.select_media_by_text(self.test_material_folder_01)
        self.report.new_result('3fa38922-fb9e-4183-8dcb-7345087f6019', result)

        self.report.start_uuid('bf6b402a-fe74-4077-9c75-c2fce8bd7768')
        time.sleep(5)
        page_media.select_media_by_text('01_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.back()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        pos_before = page_edit.get_facilitate_usage_position()
        result = page_edit.enter_library_from_facilitate_usage()
        self.report.new_result('bf6b402a-fe74-4077-9c75-c2fce8bd7768', result)

        self.report.start_uuid('b1ea3fc2-84ed-4f43-83fe-a91e6daedb59')
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_text('02_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.back()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        pos_after = page_edit.get_facilitate_usage_position()
        self.report.new_result('b1ea3fc2-84ed-4f43-83fe-a91e6daedb59', True if pos_before < pos_after else False)

        self.report.start_uuid('2a0ca27e-cefa-42e1-aee2-05c7c13cb775')
        pos_before = pos_after
        page_edit.adjust_clip_length(L.edit.timeline.clip, "start", "right", 30)
        time.sleep(5)
        pos_after = page_edit.get_facilitate_usage_position()
        self.report.new_result('2a0ca27e-cefa-42e1-aee2-05c7c13cb775', True if pos_before != pos_after else False)

        self.report.start_uuid('8a6daad4-ecb8-4cdf-8c57-d22207e30e48')
        self.report.start_uuid('c2afa529-2cb6-4e79-b369-abdbc369fb5a')
        pos_before = pos_after
        page_edit.select_from_bottom_edit_menu('Speed')
        result_2ndlayer = page_edit.is_exist(L.edit.timeline.btn_import2)
        page_edit.opacity_set_slider(0.3)
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        pos_after = page_edit.get_facilitate_usage_position()
        self.report.new_result('8a6daad4-ecb8-4cdf-8c57-d22207e30e48', True if pos_before != pos_after else False)
        self.report.new_result('c2afa529-2cb6-4e79-b369-abdbc369fb5a', not result_2ndlayer)

        self.report.start_uuid('501b853f-ee38-443d-9f8a-13e8f76608c5')
        page_edit.timeline_select_transition_effect()
        time.sleep(10)
        result = page_edit.is_exist(L.edit.timeline.btn_import2)
        self.report.new_result('501b853f-ee38-443d-9f8a-13e8f76608c5', not result)

        self.report.start_uuid('2715d1bb-1f7d-4b68-b742-69246be4b064')
        page_edit.back()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        pos_before = pos_after
        page_edit.pinch_timeline()
        time.sleep(10)
        pos_after = page_edit.get_facilitate_usage_position()
        self.report.new_result('2715d1bb-1f7d-4b68-b742-69246be4b064', True if pos_before != pos_after else False)

    # @pytest.mark.skip
    
    def test_sce_02_14_02(self):
        logger('>>> test_sce_02_14_02: Drag Clip Master between PiP Track <<<')
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

        # Drag Master Clip to PiP Track - Video
        self.report.start_uuid('256865d5-ac46-4e2e-935d-17f1bc2268d5')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_14_02")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_text('01_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        pic_base = page_edit.get_timeline_pic()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.drag_timeline_clip('down')
        time.sleep(5)
        pic_after = page_edit.get_timeline_pic()
        self.report.new_result('256865d5-ac46-4e2e-935d-17f1bc2268d5', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Drag PiP Clip to Master Track - Video
        self.report.start_uuid('2e00ced9-10cd-47a3-be8d-ba45cc55866d')
        pic_base = pic_after
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.drag_timeline_clip('up')
        time.sleep(5)
        pic_after = page_edit.get_timeline_pic()
        self.report.new_result('2e00ced9-10cd-47a3-be8d-ba45cc55866d', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Drag Master Clip to PiP Track - Photo
        self.report.start_uuid('320f5798-ff45-4e2a-bece-662552ac6a67')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.select_media_by_text('jpg.jpg')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        pic_base = page_edit.get_timeline_pic()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.drag_timeline_clip('down')
        time.sleep(5)
        pic_after = page_edit.get_timeline_pic()
        self.report.new_result('320f5798-ff45-4e2a-bece-662552ac6a67', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Drag PiP Clip to Master Track - Photo
        self.report.start_uuid('d64f1ec5-927b-4d79-ab14-ef1a2e1e8912')
        pic_base = pic_after
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.drag_timeline_clip('up')
        time.sleep(5)
        pic_after = page_edit.get_timeline_pic()
        self.report.new_result('d64f1ec5-927b-4d79-ab14-ef1a2e1e8912', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Drag Master Clip to PiP Track - Color Board
        self.report.start_uuid('78abf00a-6e19-4f57-aea5-9a6915f9a9b8')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text('Color Board')
        time.sleep(5)
        page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        pic_base = page_edit.get_timeline_pic()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.drag_timeline_clip('down')
        time.sleep(5)
        pic_after = page_edit.get_timeline_pic()
        self.report.new_result('78abf00a-6e19-4f57-aea5-9a6915f9a9b8', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Drag PiP Clip to Master Track - Color Board
        self.report.start_uuid('590f5110-8d44-42c0-bd56-a492aec762f3')
        pic_base = pic_after
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.drag_timeline_clip('up')
        time.sleep(5)
        pic_after = page_edit.get_timeline_pic()
        self.report.new_result('590f5110-8d44-42c0-bd56-a492aec762f3', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

    # @pytest.mark.skip
    
    def test_sce_02_14_03(self):
        logger('>>> test_sce_02_14_03: Freeze Frame <<<')
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

        # Freeze Frame - Master
        self.report.start_uuid('7cd74f98-f14b-474d-9e84-85f6b1a083bb')
        self.report.start_uuid('fcd679d0-f982-43b1-a8b3-39f9948ecde7')
        self.report.start_uuid('07b52766-71aa-4cf3-bf50-41cefa8f6bfd')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_14_03")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_text('01_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Freeze Frame')
        self.report.new_result('7cd74f98-f14b-474d-9e84-85f6b1a083bb', result)
        self.report.new_result('fcd679d0-f982-43b1-a8b3-39f9948ecde7', result)
        self.report.new_result('07b52766-71aa-4cf3-bf50-41cefa8f6bfd', result)

        # No Freeze Frame in Photo item - Master
        self.report.start_uuid('baf0e83a-4602-404a-9db9-d439cba28671')
        time.sleep(5)
        result = page_edit.is_exist_in_bottom_edit_menu('Freeze Frame')
        self.report.new_result('baf0e83a-4602-404a-9db9-d439cba28671', not result)

        # No Freeze Frame in Color Board item - Master
        self.report.start_uuid('22c7c7c7-047c-4d65-8b50-d0880ec1f1c2')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text('Color Board')
        time.sleep(5)
        page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        result = page_edit.is_exist_in_bottom_edit_menu('Freeze Frame')
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        self.report.new_result('22c7c7c7-047c-4d65-8b50-d0880ec1f1c2', not result)

        # Freeze Frame - PiP
        self.report.start_uuid('05bd5eb6-b4cc-4129-b7f3-0d99f2879724')
        self.report.start_uuid('9f567800-ea19-4e8b-bf9b-a721dfd90ff2')
        self.report.start_uuid('8169eca1-4d2b-455f-9570-1b7914e12d3c')
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.switch_to_pip_video_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text('01_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Freeze Frame')
        self.report.new_result('05bd5eb6-b4cc-4129-b7f3-0d99f2879724', result)
        self.report.new_result('9f567800-ea19-4e8b-bf9b-a721dfd90ff2', result)
        self.report.new_result('8169eca1-4d2b-455f-9570-1b7914e12d3c', result)

        # No Freeze Frame in Photo item - PiP
        self.report.start_uuid('25e1ca85-7bc3-4cc0-a230-f8bb0a3dda0f')
        time.sleep(5)
        result = page_edit.is_exist_in_bottom_edit_menu('Freeze Frame')
        self.report.new_result('25e1ca85-7bc3-4cc0-a230-f8bb0a3dda0f', not result)

        # No Freeze Frame in Color Board item - Master
        self.report.start_uuid('26301cfd-0e15-4cb6-9089-2d5e12054aeb')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text('Color Board')
        time.sleep(5)
        page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        result = page_edit.is_exist_in_bottom_edit_menu('Freeze Frame')
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        self.report.new_result('26301cfd-0e15-4cb6-9089-2d5e12054aeb', not result)

        # Freeze Frame in the end of clip - Master
        self.report.start_uuid('a6dcf88a-a376-4e2d-ab3c-c7d85cc7bc0f')
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_text('01_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        result = page_edit.select_from_bottom_edit_menu('Freeze Frame')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        self.report.new_result('a6dcf88a-a376-4e2d-ab3c-c7d85cc7bc0f', result)

        # Freeze Frame in the end of clip - Master
        self.report.start_uuid('42dd8da5-2ca6-45a7-bde7-0f15af9a2bec')
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_video_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_text('01_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        result = page_edit.select_from_bottom_edit_menu('Freeze Frame')
        self.report.new_result('42dd8da5-2ca6-45a7-bde7-0f15af9a2bec', result)

    # @pytest.mark.skip
    
    def test_sce_02_14_04(self):
        logger('>>> test_sce_02_14_04: Replace Audio <<<')
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

        self.report.start_uuid('8bdb0287-bd41-4e6d-98ef-ad6117c23326')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_14_04")
        page_main.project_set_16_9()
        page_media.switch_to_music_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.add_song_to_timeline_by_name('m4a.m4a')
        # page_media.select_song_by_text('m4a.m4a')
        # page_media.add_selected_song_to_timeline()
        time.sleep(5)
        page_edit.back()
        time.sleep(2)
        page_edit.back()
        time.sleep(2)
        page_edit.timeline_select_audio('m4a.m4a')
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        self.report.new_result('8bdb0287-bd41-4e6d-98ef-ad6117c23326', result)

        self.report.start_uuid('59fbfba1-b1ab-41f0-aaa2-a03067f1a9f2')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.add_song_to_timeline_by_name('mp3.mp3')
        # page_media.select_song_by_text('mp3.mp3')
        # page_media.add_selected_song_to_timeline()
        time.sleep(5)
        result = True if page_media.is_exist(L.edit.replace.btn_replace_anyway) else False
        self.report.new_result('59fbfba1-b1ab-41f0-aaa2-a03067f1a9f2', result)

        self.report.start_uuid('5e437521-119a-4049-b495-4b7f26ba1acc')
        page_media.click(L.edit.replace.btn_replace_anyway)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        self.report.new_result('5e437521-119a-4049-b495-4b7f26ba1acc', result)

        self.report.start_uuid('f0584533-910a-4102-8519-3c2e850cec11')
        self.report.start_uuid('52bc38e2-f076-4991-99dd-8699ccba5b65')
        self.report.start_uuid('1a49a277-047d-445b-b64d-1675c61e2cad')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.add_song_to_timeline_by_name('m4a.m4a')
        # page_media.select_song_by_text('m4a.m4a')
        # page_media.add_selected_song_to_timeline()
        time.sleep(5)
        result_trim_page, result_trim_text, result_duration = page_edit.replace.check_replace_trim_view()
        self.report.new_result('f0584533-910a-4102-8519-3c2e850cec11', result_trim_page)
        self.report.new_result('52bc38e2-f076-4991-99dd-8699ccba5b65', result_trim_text)
        self.report.new_result('1a49a277-047d-445b-b64d-1675c61e2cad', result_duration)

        self.report.start_uuid('a99792c4-482e-4a09-8c6c-c1f72b14f8db')
        result = page_edit.replace.move_trim_area_audio()
        self.report.new_result('a99792c4-482e-4a09-8c6c-c1f72b14f8db', result)

        self.report.start_uuid('197ea67f-be24-4244-8bb6-bf650fd35ef8')
        self.report.start_uuid('bcace2e3-1e5e-4f7f-a833-fb2bde2fc359')
        self.report.start_uuid('fa5ddd52-7cd5-42c6-9182-8338fc241c41')
        result = page_edit.replace.seek_by_indicator_audio()
        self.report.new_result('197ea67f-be24-4244-8bb6-bf650fd35ef8', result)
        self.report.new_result('bcace2e3-1e5e-4f7f-a833-fb2bde2fc359', result)
        self.report.new_result('fa5ddd52-7cd5-42c6-9182-8338fc241c41', result)

        self.report.start_uuid('eb67b252-50c2-4a4a-9b21-ed17dc67bfe1')
        pos_before = page_edit.replace.get_indicator_pos()
        page_edit.click(L.edit.menu.play)
        time.sleep(3)
        page_edit.click(L.edit.menu.play)
        pos_after = page_edit.replace.get_indicator_pos()
        result = True if pos_before < pos_after else False
        self.report.new_result('eb67b252-50c2-4a4a-9b21-ed17dc67bfe1', result)

        self.report.start_uuid('f791563d-bbab-4d82-b30b-996e56a5f641')
        page_edit.back()
        time.sleep(2)
        page_edit.back()
        time.sleep(2)
        result = page_edit.timeline_select_audio('m4a.m4a')
        self.report.new_result('f791563d-bbab-4d82-b30b-996e56a5f641', result)

        self.report.start_uuid('9032a3e6-5b41-4e2f-9727-b39208563ea4')
        self.report.start_uuid('1f7185f1-2e41-4637-af55-38e70df04b87')
        self.report.start_uuid('e03185c9-0b94-426d-80e3-1a18f0ce3203')
        self.report.start_uuid('c311cec9-4d29-4f81-9296-dd10278f96e3')
        self.report.start_uuid('3106f155-a527-4840-b916-3bec4a1f1619')
        self.report.start_uuid('8ef120fc-99d8-49b3-ae1a-12896c947c92')
        page_edit.select_from_bottom_edit_menu('Volume')
        page_edit.select_from_bottom_edit_menu('Fade in')
        page_edit.select_from_bottom_edit_menu('Fade out')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Audio Tool')
        page_edit.select_from_bottom_edit_menu('Voice Changer')
        page_edit.select_from_bottom_edit_menu('Man')
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.add_song_to_timeline_by_name('mp3.mp3')
        # page_media.select_song_by_text('mp3.mp3')
        # page_media.add_selected_song_to_timeline()
        time.sleep(5)
        result_volume = page_edit.check_bottom_edit_menu_item_apply_status('Volume')
        result_audiotool = page_edit.check_bottom_edit_menu_item_apply_status('Audio Tool')
        self.report.new_result('9032a3e6-5b41-4e2f-9727-b39208563ea4', result_volume)
        self.report.new_result('1f7185f1-2e41-4637-af55-38e70df04b87', result_volume)
        self.report.new_result('e03185c9-0b94-426d-80e3-1a18f0ce3203', result_volume)
        self.report.new_result('c311cec9-4d29-4f81-9296-dd10278f96e3', result_volume)
        self.report.new_result('3106f155-a527-4840-b916-3bec4a1f1619', result_audiotool)
        self.report.new_result('8ef120fc-99d8-49b3-ae1a-12896c947c92', result_audiotool)

    # @pytest.mark.skip
    
    def test_sce_02_14_05(self):
        logger('>>> test_sce_02_14_05: Enabled all pip/audio tracks for free user  <<<')
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

        self.report.start_uuid('ecafebd1-d4a4-4713-b951-c69d022d6345')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_14_05")
        page_main.project_set_16_9()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_video_library()
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        for n in range(3):
            page_edit.click(L.edit.menu.fx_layer)
            page_media.switch_to_pip_video_library()
            page_media.select_media_by_text(self.test_material_folder_01)
            time.sleep(5)
            page_media.select_media_by_text(media_list[0])
            time.sleep(5)
            page_edit.click(L.import_media.library_gridview.add)
            time.sleep(5)
        result = True if page_media.is_exist(L.import_media.device_limit.btn_remind_ok) else False
        page_media.click(L.import_media.device_limit.btn_remind_ok)
        self.report.new_result('ecafebd1-d4a4-4713-b951-c69d022d6345', result)

        self.report.start_uuid('3647c477-8dc4-4c84-85bc-40fdf3e85926')
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.select_media_by_text('jpg.jpg')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('3647c477-8dc4-4c84-85bc-40fdf3e85926', result)

        self.report.start_uuid('0974471e-c105-429a-ad85-08860760860e')
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        for n in range(4):
            page_media.select_media_by_text('jpg.jpg')
            time.sleep(5)
            page_edit.click(L.import_media.library_gridview.add)
            time.sleep(5)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('0974471e-c105-429a-ad85-08860760860e', result)

        self.report.start_uuid('6960c6d0-1229-483a-a63c-c0709f8fa86d')
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.select_media_by_text('Default')
        time.sleep(5)
        for n in range(4):
            page_edit.click(L.import_media.library_gridview.add)
            time.sleep(5)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('6960c6d0-1229-483a-a63c-c0709f8fa86d', result)

        self.report.start_uuid('f3391802-eb55-4379-82ff-d377e7300260')
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_sticker_library()
        time.sleep(5)
        page_media.select_template_category('Text')
        time.sleep(5)
        page_media.search_template_by_image('sticker')
        for n in range(4):
            page_media.click(L.import_media.library_gridview.add_sticker)
            time.sleep(5)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('f3391802-eb55-4379-82ff-d377e7300260', result)

        self.report.start_uuid('2001cf22-5599-4229-a875-cab89b4d02ab')
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_overlay_library()
        time.sleep(5)
        page_media.select_template_category('Light')
        page_media.search_template_by_image('overlay')
        page_media.download_video()
        for n in range(4):
            page_media.click(L.import_media.library_gridview.add)
            time.sleep(5)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('2001cf22-5599-4229-a875-cab89b4d02ab', result)

        self.report.start_uuid('981638e8-6be1-4227-9bea-e1a7ef616848')
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_effect_layer_library()
        time.sleep(5)
        page_media.search_template_by_image('highlight')
        for n in range(4):
            page_media.click(L.import_media.library_gridview.add)
            time.sleep(5)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('981638e8-6be1-4227-9bea-e1a7ef616848', result)

        self.report.start_uuid('ac09b641-15ec-4aa6-9d15-5ad6698d084a')
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.play)
        time.sleep(15)
        page_edit.click(L.edit.menu.fx_layer)
        page_media.switch_to_pip_video_library()
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        for n in range(2):
            page_media.select_media_by_text(media_list[0])
            time.sleep(5)
            page_edit.click(L.import_media.library_gridview.add)
            time.sleep(5)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        for n in range(2):
            page_media.select_media_by_text('jpg.jpg')
            time.sleep(5)
            page_edit.click(L.import_media.library_gridview.add)
            time.sleep(5)
        page_media.switch_to_title_library()
        time.sleep(5)
        page_media.select_media_by_text('Default')
        time.sleep(5)
        for n in range(2):
            page_edit.click(L.import_media.library_gridview.add)
            time.sleep(5)
        page_media.switch_to_sticker_library()
        time.sleep(5)
        page_media.select_template_category('Text')
        time.sleep(5)
        page_media.search_template_by_image('sticker')
        page_media.click(L.import_media.library_gridview.add_sticker)
        page_media.switch_to_overlay_library()
        time.sleep(5)
        page_media.select_template_category('Light')
        page_media.search_template_by_image('overlay')
        page_media.click(L.import_media.library_gridview.add)
        page_media.switch_to_effect_layer_library()
        time.sleep(5)
        page_media.search_template_by_image('highlight')
        for n in range(4):
            page_media.click(L.import_media.library_gridview.add)
            time.sleep(5)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('ac09b641-15ec-4aa6-9d15-5ad6698d084a', result)

        self.report.start_uuid('b7a46bc1-6138-4563-a047-27ad76f5f947')
        self.report.start_uuid('5a61f310-5769-44f6-8d1d-e80507e23525')
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_music_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        for n in range(9):
            page_media.add_song_to_timeline_by_name('m4a.m4a')
            # page_media.select_song_by_text('m4a.m4a')
            # page_media.add_selected_song_to_timeline()
            time.sleep(5)
        page_edit.back()
        time.sleep(2)
        page_edit.back()
        time.sleep(2)
        result = True if not page_media.is_exist(L.main.subscribe.back_btn) else False
        self.report.new_result('b7a46bc1-6138-4563-a047-27ad76f5f947', result)
        self.report.new_result('5a61f310-5769-44f6-8d1d-e80507e23525', result)

    # @pytest.mark.skip
    
    def test_sce_02_14_06(self):
        logger('>>> test_sce_02_14_06: IAP check and Trim Stabilized Video<<<')
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

        self.report.start_uuid('a1afdfa0-3351-4b76-86a3-5b4b40f4135e')
        page_main.wait_subscribe_expire()
        page_main.click(L.main.project.shopping_cart)
        time.sleep(5)
        result = page_main.check_iap_feature_items('More Overlay Tracks')
        page_edit.back()
        time.sleep(2)
        self.report.new_result('a1afdfa0-3351-4b76-86a3-5b4b40f4135e', not result)

        self.report.start_uuid('791c7b6d-3945-4169-bcca-1422e0530033')
        page_main.subscribe()
        if not page_main.is_exist(L.main.premium.btn_premium):
            page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.click(L.main.premium.btn_premium)
        result = page_main.check_iap_feature_items('More Overlay Tracks')
        self.report.new_result('791c7b6d-3945-4169-bcca-1422e0530033', not result)

        # Trim Stabilized Video
        self.report.start_uuid('7401b851-9c7d-4fdf-aaea-d910eabdb923')
        self.report.start_uuid('d80f48be-a1e4-4a7f-be69-de564f4cfb81')
        page_edit.back()
        time.sleep(2)
        page_main.project_click_new()
        page_main.project_set_name("sce_02_14_06")
        page_main.project_set_16_9()
        time.sleep(3)
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_text('01_static.mp4')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Stabilizer')
        page_edit.wait_for_stabilizing_complete()
        result = page_edit.trim_video(L.edit.timeline.clip)
        self.report.new_result('7401b851-9c7d-4fdf-aaea-d910eabdb923', result)
        self.report.new_result('d80f48be-a1e4-4a7f-be69-de564f4cfb81', result)

    # @pytest.mark.skip
    
    def test_sce_02_14_07(self):
        logger('>>> test_sce_02_14_07: Download Getty Images<<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.enter_settings_from_main()
        page_main.sign_in_cyberlink_account()
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        self.report.start_uuid('75f64d96-5982-4c2c-be60-0150e77f96fd')
        time.sleep(10)
        # page_main.subscribe()
        page_main.project_click_new()
        page_main.project_set_name("sce_02_14_07")
        page_main.project_set_16_9()
        time.sleep(3)
        page_media.select_media_by_text('Stock Video')
        time.sleep(5)
        page_media.click(L.import_media.video_entry.tab_video_gettyimages)
        time.sleep(10)
        page_media.select_media_by_order(1)
        result = page_media.download_video()
        self.report.new_result('75f64d96-5982-4c2c-be60-0150e77f96fd', result)

        self.report.start_uuid('7cbd90d2-9e8d-41fe-b227-544b9432441e')
        page_media.search_video('star')
        time.sleep(10)
        page_media.select_media_by_order(2)
        result = page_media.download_video()
        self.report.new_result('7cbd90d2-9e8d-41fe-b227-544b9432441e', result)

        self.report.start_uuid('081c823a-b701-4ac8-a78f-e42601a196cf')
        page_media.switch_to_photo_library()
        page_media.select_media_by_text('Stock Photo')
        time.sleep(5)
        page_media.click(L.import_media.video_entry.tab_video_gettyimages)
        time.sleep(10)
        page_media.select_media_by_order(1)
        result = page_media.download_video()
        self.report.new_result('081c823a-b701-4ac8-a78f-e42601a196cf', result)

        self.report.start_uuid('ac252835-0992-4c44-bdc4-fc21e12d6544')
        page_media.search_video('star')
        time.sleep(10)
        page_media.select_media_by_order(2)
        result = page_media.download_video()
        self.report.new_result('ac252835-0992-4c44-bdc4-fc21e12d6544', result)