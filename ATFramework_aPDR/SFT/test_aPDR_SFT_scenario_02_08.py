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


class Test_SFT_Scenario_02_08:
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
    def test_sce_02_08_01(self):
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
       
        # Apply free In effect
        self.report.start_uuid('c3ba23bb-93f9-4297-8ba4-ba4f94ad4d6e')   
        page_edit.el(L.edit.menu.fx_layer).click()
        # page_media.select_media_by_text('Default')
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Animation')
        page_edit.el(L.edit.title_animation.btn_in_animation).click()
        page_edit.select_from_bottom_edit_menu('Fade')
        result = (True if page_edit.is_exist(L.edit.title_animation.duration_slider) else False)
        self.report.new_result('c3ba23bb-93f9-4297-8ba4-ba4f94ad4d6e', result)
        
        # Apply premium effect -> Open IAP
        self.report.start_uuid('e4e1e6ba-2a37-450b-b39a-65aab359c8c4')  
        page_edit.select_from_bottom_edit_menu('Hide Down')     
        result = page_edit.check_premium_features_used()
        self.report.new_result('e4e1e6ba-2a37-450b-b39a-65aab359c8c4', result)
        
        self.report.start_uuid('3b7760e3-bd86-4778-b4e1-134813c51153') 
        page_edit.swipe_bottom_edit_menu('right')
        page_edit.swipe_bottom_edit_menu('right')
        page_edit.select_from_bottom_edit_menu('Fade')
        duration = page_edit.title_animation_get_duration()
        result = (True if duration == '3.3' else False)
        self.report.new_result('3b7760e3-bd86-4778-b4e1-134813c51153', result)
        
        self.report.start_uuid('e0e309af-eae1-42ab-88c2-4935ac75f975') 
        page_edit.speed.set_slider(0)
        duration = page_edit.title_animation_get_duration()
        result = (True if duration == '0.0' else False)
        self.report.new_result('e0e309af-eae1-42ab-88c2-4935ac75f975', result)
        
        self.report.start_uuid('8f0c0c60-f532-4a23-892b-fa3b68d9ab59') 
        page_edit.speed.set_slider(50)
        duration = page_edit.title_animation_get_duration()
        result = (True if duration == '5.0' else False)
        self.report.new_result('8f0c0c60-f532-4a23-892b-fa3b68d9ab59', result)
        
        self.report.start_uuid('187c3298-c49f-48d7-be93-1ed65027eda0') 
        page_edit.select_from_bottom_edit_menu('None')
        time.sleep(3)
        page_edit.el(L.edit.edit_sub.back_button).click()
        time.sleep(3)
        page_edit.el(L.edit.edit_sub.back_button).click()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Backdrop')
        page_edit.el(L.edit.backdrop.btn_backdrop_enable).click()
        page_edit.el(L.edit.edit_sub.back_button).click()
        page_edit.select_from_bottom_edit_menu('Animation')
        page_edit.el(L.edit.title_animation.btn_in_animation).click()   
        page_edit.el(L.edit.title_animation.cancel_btn).click()
        result = (True if page_edit.is_exist(L.edit.title_animation.btn_in_animation) else False)
        self.report.new_result('187c3298-c49f-48d7-be93-1ed65027eda0', result)   
        
        self.report.start_uuid('47a23942-e91b-4176-92fc-dbbede792c6a') 
        page_edit.el(L.edit.title_animation.btn_in_animation).click()
        page_edit.el(L.edit.title_animation.ok_btn).click()
        result = (True if page_edit.is_exist(L.edit.title_animation.effect_list) else False)
        self.report.new_result('47a23942-e91b-4176-92fc-dbbede792c6a', result)
        
        
        # Apply free Out effect
        self.report.start_uuid('16eaff05-1997-4a3f-9bf6-fd56657231e0')   
        page_edit.el(L.edit.edit_sub.back_button).click()
        page_edit.el(L.edit.title_animation.btn_out_animation).click()
        page_edit.select_from_bottom_edit_menu('Fade')
        result = (True if page_edit.is_exist(L.edit.title_animation.duration_slider) else False)
        self.report.new_result('16eaff05-1997-4a3f-9bf6-fd56657231e0', result)
        
        # Apply premium effect -> Open IAP
        self.report.start_uuid('dd196c9f-b8a5-46d2-8b7d-e98aaee09f00')  
        page_edit.select_from_bottom_edit_menu('Hide Down')     
        result = page_edit.check_premium_features_used()
        self.report.new_result('dd196c9f-b8a5-46d2-8b7d-e98aaee09f00', result)
        
        
        self.report.start_uuid('745aaaac-0489-452f-a532-7273b89d38ad') 
        page_edit.swipe_bottom_edit_menu('right')
        page_edit.swipe_bottom_edit_menu('right')
        page_edit.select_from_bottom_edit_menu('Fade')
        duration = page_edit.title_animation_get_duration()
        result = (True if duration == '3.3' else False)
        self.report.new_result('745aaaac-0489-452f-a532-7273b89d38ad', result)
        
        self.report.start_uuid('2c855f3a-edf9-454a-9477-641018d9f6da') 
        page_edit.speed.set_slider(0)
        duration = page_edit.title_animation_get_duration()
        result = (True if duration == '0.0' else False)
        self.report.new_result('2c855f3a-edf9-454a-9477-641018d9f6da', result)
        
        self.report.start_uuid('54fb752f-7325-47c5-8690-fa026deb9207') 
        page_edit.speed.set_slider(50)
        duration = page_edit.title_animation_get_duration()
        result = (True if duration == '5.0' else False)
        self.report.new_result('54fb752f-7325-47c5-8690-fa026deb9207', result)
        
        self.report.start_uuid('75dc0a3d-7c47-4bc2-8808-03345fb75e82') 
        page_edit.select_from_bottom_edit_menu('None')
        time.sleep(3)
        page_edit.el(L.edit.edit_sub.back_button).click()
        time.sleep(3)
        page_edit.el(L.edit.edit_sub.back_button).click()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Backdrop')
        page_edit.el(L.edit.backdrop.btn_backdrop_enable).click()
        page_edit.el(L.edit.edit_sub.back_button).click()
        page_edit.select_from_bottom_edit_menu('Animation')
        page_edit.el(L.edit.title_animation.btn_out_animation).click()   
        page_edit.el(L.edit.title_animation.cancel_btn).click()
        result = (True if page_edit.is_exist(L.edit.title_animation.btn_out_animation) else False)
        self.report.new_result('75dc0a3d-7c47-4bc2-8808-03345fb75e82', result)   
        
        self.report.start_uuid('5e7a4d96-0a24-4502-a8bd-2da95ec0cac4') 
        page_edit.el(L.edit.title_animation.btn_out_animation).click()
        page_edit.el(L.edit.title_animation.ok_btn).click()
        result = (True if page_edit.is_exist(L.edit.title_animation.effect_list) else False)
        self.report.new_result('5e7a4d96-0a24-4502-a8bd-2da95ec0cac4', result)
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_08_02(self):
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        
        # Apply backdrop
        self.report.start_uuid('2f788797-8d3b-4ec0-9e55-5ed201d7f118')   
        page_edit.el(L.edit.menu.fx_layer).click()
        # page_media.select_media_by_text('Default')
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Backdrop')
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_backdrop_enable).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('2f788797-8d3b-4ec0-9e55-5ed201d7f118', True if (not compare_result) else False)
        
        self.report.start_uuid('6112bac1-1bd3-4150-85e0-4759cc06f3d0')
        pic_base = pic_after
        page_edit.el(L.edit.backdrop.btn_backdrop_enable).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('6112bac1-1bd3-4150-85e0-4759cc06f3d0', True if (not compare_result) else False)        
        
        # Set backdrop type
        self.report.start_uuid('f97c1ec8-9c13-4f1b-98ed-c10aca70e5df')
        page_edit.el(L.edit.backdrop.btn_backdrop_enable).click()
        page_edit.el(L.edit.backdrop.btn_backdrop_type).click()
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_type_curved_edge).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('f97c1ec8-9c13-4f1b-98ed-c10aca70e5df', True if (not compare_result) else False)
        
        self.report.start_uuid('c72494fc-73db-4c1b-8a0b-31ddac80622f')
        pic_base = pic_after
        page_edit.el(L.edit.backdrop.btn_type_rectangle).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('c72494fc-73db-4c1b-8a0b-31ddac80622f', True if (not compare_result) else False)        
        
        self.report.start_uuid('ea59a53f-744c-4cda-a488-bbd591ab54ff')
        pic_base = pic_after
        page_edit.el(L.edit.backdrop.btn_type_rounded).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('ea59a53f-744c-4cda-a488-bbd591ab54ff', True if (not compare_result) else False)        
        # Set backdrop type - Premium type
        self.report.start_uuid('338f9df6-b9c1-4644-ba35-6cbdf507f4f0')
        page_edit.el(L.edit.backdrop.btn_type_ellipse).click()
        result = page_edit.check_premium_features_used()
        self.report.new_result('338f9df6-b9c1-4644-ba35-6cbdf507f4f0', result)        
        
        self.report.start_uuid('6ec1e84a-db1f-4b30-917a-e7922ee2a619')
        page_edit.el(L.edit.backdrop.btn_type_bar).click()
        result = page_edit.check_premium_features_used()
        self.report.new_result('6ec1e84a-db1f-4b30-917a-e7922ee2a619', result)
        
        # Set color
        self.report.start_uuid('e35bfe78-13f3-4892-a4ce-b439e2f5d032')
        page_edit.el(L.edit.backdrop.btn_type_rounded).click()
        page_edit.driver.driver.back()
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_backdrop_color).click()
        page_edit.color_selector.set_hue_slider(10)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('e35bfe78-13f3-4892-a4ce-b439e2f5d032', True if (not compare_result) else False)
        
        self.report.start_uuid('7bdfecb4-0819-43f8-bc49-dede076678dc')
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_backdrop_color).click()
        page_edit.color_selector.set_saturation_slider(150)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('7bdfecb4-0819-43f8-bc49-dede076678dc', True if (not compare_result) else False)        
        
        self.report.start_uuid('5bb321a6-a1f2-4fe1-a067-076d43091a5d')     
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_backdrop_color).click()
        page_edit.color_selector.set_red_number(0)
        page_edit.color_selector.set_green_number(255)
        page_edit.color_selector.set_blue_number(230)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('5bb321a6-a1f2-4fe1-a067-076d43091a5d', True if (not compare_result) else False)        
        
        self.report.start_uuid('2e31bad5-ab38-40cc-a574-3e08735a6b33')
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_backdrop_color).click()
        page_edit.el(L.edit.backdrop.preset_red).click()
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('2e31bad5-ab38-40cc-a574-3e08735a6b33', True if (not compare_result) else False)        
        
        # Set Opacity 
        self.report.start_uuid('03dc8b37-a759-4338-af10-6901adcf9bf4')
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_backdrop_opacity).click()
        page_edit.opacity_set_slider(0.1)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('03dc8b37-a759-4338-af10-6901adcf9bf4', True if (not compare_result) else False)
        
        self.report.start_uuid('44414d74-bcd9-489e-8a9a-2db7790b97fc')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(1)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('44414d74-bcd9-489e-8a9a-2db7790b97fc', True if (not compare_result) else False)        
        
        self.report.start_uuid('d0f0071f-2660-46c6-a13c-aeb657635d3a')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(0.5)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('d0f0071f-2660-46c6-a13c-aeb657635d3a', True if (not compare_result) else False)
                
        # Set Y Offset
        self.report.start_uuid('658a8315-1088-42ec-b005-a7059d878060')
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.backdrop.btn_backdrop_y_offset).click()
        page_edit.opacity_set_slider(1)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('658a8315-1088-42ec-b005-a7059d878060', True if (not compare_result) else False)
        
        self.report.start_uuid('2ff9fd47-baf7-4dfd-a3c9-db5d7de51299')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(0.1)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('2ff9fd47-baf7-4dfd-a3c9-db5d7de51299', True if (not compare_result) else False)        
        
        self.report.start_uuid('928a22ba-9956-4e5a-88bb-3b41c1af7ceb')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(0.5)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('928a22ba-9956-4e5a-88bb-3b41c1af7ceb', True if (not compare_result) else False)
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_08_03(self):
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        
        # Transform Keyframe
        self.report.start_uuid('cec30fc6-3e0f-42db-ae57-c562656bcdff')   
        self.report.start_uuid('6f15d2cb-72a3-4f67-8389-f4d33678f080')   
        self.report.start_uuid('bc8e7cc2-a02f-4777-b8cb-1052d3ba62a7')   
        self.report.start_uuid('288e70f6-f9ea-4c10-8502-2cc482e0d955')   
        page_edit.el(L.edit.menu.fx_layer).click()
        # page_media.select_media_by_text('Default')
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_media('mp4.mp4', 'Video')
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Transform Keyframe')
        x, y, scale, rotation = page_edit.keyframe.get_transform_keyframe_value()
        
        self.report.new_result('cec30fc6-3e0f-42db-ae57-c562656bcdff', True if x == '0.500' else False)
        self.report.new_result('6f15d2cb-72a3-4f67-8389-f4d33678f080', True if y == '0.500' else False)
        self.report.new_result('bc8e7cc2-a02f-4777-b8cb-1052d3ba62a7', True if scale == '0.210' else False)
        self.report.new_result('288e70f6-f9ea-4c10-8502-2cc482e0d955', True if rotation == '0' else False)
        
        self.report.start_uuid('39103673-ab11-4e8b-ab82-afefd419206f')
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('39103673-ab11-4e8b-ab82-afefd419206f', True if (not compare_result) else False)        
        
        self.report.start_uuid('928ff7f6-ea3f-441f-85c4-035380a0c40b')
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('928ff7f6-ea3f-441f-85c4-035380a0c40b', True if (not compare_result) else False)        
        
        self.report.start_uuid('2d247eb8-e9a9-4e5c-8d95-28bbca8ae93c')
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        page_effect.move_title()
        x, y, scale, rotation = page_edit.keyframe.get_transform_keyframe_value()
        self.report.new_result('2d247eb8-e9a9-4e5c-8d95-28bbca8ae93c', True if not(x == '0.500') and not(y == '0.500') else False)

        self.report.start_uuid('710685c7-a44c-4f70-b2ea-ac11c05564d1')
        time.sleep(2)
        page_effect.modify_title_size()
        x, y, scale, rotation = page_edit.keyframe.get_transform_keyframe_value()
        self.report.new_result('710685c7-a44c-4f70-b2ea-ac11c05564d1', True if not(scale == '0.209') else False)        
        
        self.report.start_uuid('b4b5ec0d-bc28-4319-8185-f8b2de1eb8a5')
        time.sleep(2)
        page_effect.modify_title_rotate()
        x, y, scale, rotation = page_edit.keyframe.get_transform_keyframe_value()
        self.report.new_result('b4b5ec0d-bc28-4319-8185-f8b2de1eb8a5', True if not(rotation == '0') else False)        
        
        self.report.start_uuid('e18a1f0f-6f93-4a99-857e-ee99aa781a4f')
        time.sleep(2)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(2)
        page_edit.el(L.edit.menu.fx_layer).click()
        # page_media.select_media_by_text('Default')
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Transform Keyframe')
        time.sleep(2)
        page_edit.timeline_swipe('left', 100)
        page_edit.timeline_swipe('right', 100)
        time.sleep(2)
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        page_edit.timeline_swipe('left', 100)
        time.sleep(2)
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        page_edit.timeline_swipe('right', 100)
        time.sleep(2)
        page_edit.keyframe.longpress_keyframe('remove')
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 2).compare_image())(
            pic_base, pic_after)
        self.report.new_result('e18a1f0f-6f93-4a99-857e-ee99aa781a4f', True if compare_result else False)         
        
        
        self.report.start_uuid('a7641535-8980-4e1c-9bb4-edee0b98a01f')
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        page_edit.timeline_swipe('left', 100)
        time.sleep(2)
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        page_effect.move_title()
        time.sleep(2)
        page_effect.modify_title_size()
        time.sleep(2)
        page_effect.modify_title_rotate()
        time.sleep(2)
        page_edit.keyframe.longpress_keyframe('previous')
        x, y, scale, rotation = page_edit.keyframe.get_transform_keyframe_value()
        if  x == '0.500' and y == '0.500' and scale == '0.210' and rotation == '0':
            result = True
        else:
            result = False  
        self.report.new_result('a7641535-8980-4e1c-9bb4-edee0b98a01f', result)          
        
        self.report.start_uuid('ed06e2a2-ce49-411d-9d66-1484b917769c')
        page_edit.timeline_swipe('left', 100)
        time.sleep(2)
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        page_effect.move_title()
        time.sleep(2)
        page_effect.modify_title_size()
        time.sleep(2)
        page_effect.modify_title_rotate()
        time.sleep(2)
        page_edit.timeline_swipe('right', 100)
        time.sleep(2)
        page_edit.keyframe.longpress_keyframe('next')
        x, y, scale, rotation = page_edit.keyframe.get_transform_keyframe_value()
        if  x == '0.500' and y == '0.500' and scale == '0.209' and rotation == '0':
            result = False
        else:
            result = True  
        self.report.new_result('ed06e2a2-ce49-411d-9d66-1484b917769c', result)  

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_08_04(self):
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        
        # Motion Graphic Titles
        self.report.start_uuid('a1e85062-b9ed-4986-a775-a27939876e41')
        page_edit.timeline_select_media('mp4.mp4', 'Video')
        page_edit.el(L.edit.menu.delete).click()
        page_edit.el(L.edit.menu.fx_layer).click()
        page_media.select_title_category('Expressive Titles')
        page_media.search_template_by_image('mgt_premium')
        time.sleep(5)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.trying_premium_content('try')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        result = page_edit.check_premium_features_used()
        page_edit.click(L.edit.menu.delete)
        self.report.new_result('a1e85062-b9ed-4986-a775-a27939876e41', result)

        self.report.start_uuid('9f3aa52b-e2e6-4261-9223-9fb6f834e0da')
        page_edit.el(L.edit.menu.fx_layer).click()
        page_media.select_title_category('Expressive Titles')
        page_media.search_template_by_image('mgt_free')
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        result = (True if page_edit.is_exist(L.edit.motion_graphic_title.dropdownmenu_text) else False)
        self.report.new_result('9f3aa52b-e2e6-4261-9223-9fb6f834e0da', result)

        self.report.start_uuid('a6c9ec54-05d5-4709-9aa0-c1e071daadb6')
        page_edit.el(L.edit.motion_graphic_title.dropdownmenu_text).click()
        if page_edit.get_motion_title_text_number() > 1:
            page_edit.el(L.edit.motion_graphic_title.dropdownmenu_text).click()
            result = True 
        else:
            result = False
        self.report.new_result('a6c9ec54-05d5-4709-9aa0-c1e071daadb6', result)  
        
        self.report.start_uuid('27305720-d00b-4cba-a138-c0171e015255')   
        self.report.start_uuid('d78c7106-73e5-4f1c-b8e8-e932adc65a21')   
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Edit')
        page_edit.el(L.edit.title_designer.title_text_edit_area).set_text('AT Test')
        page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('27305720-d00b-4cba-a138-c0171e015255', True if (not compare_result) else False)
        self.report.new_result('d78c7106-73e5-4f1c-b8e8-e932adc65a21', True if page_edit.el(L.edit.motion_graphic_title.dropdownmenu_text).text == 'AT Test' else False)

        # Set color
        self.report.start_uuid('783bfdbb-9ba2-4c66-b603-61fd13e2619a')
        # pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Color')
        page_edit.title_designer.select_color_by_order(0)
        result = page_edit.title_designer.set_hue_slider(0.3)
        # page_edit.color_selector.set_hue_slider(10)
        # pic_after = page_edit.get_preview_pic()
        # compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
        #     pic_base, pic_after)
        self.report.new_result('783bfdbb-9ba2-4c66-b603-61fd13e2619a', result)
        
        self.report.start_uuid('d8aa2141-fdcc-4c67-941b-159a5702f06b')
        # pic_base = page_edit.get_preview_pic()
        # page_edit.select_from_bottom_edit_menu('Color')
        # page_edit.color_selector.set_saturation_slider(150)
        # page_edit.driver.driver.back()
        # pic_after = page_edit.get_preview_pic()
        # compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
        #     pic_base, pic_after)
        self.report.new_result('d8aa2141-fdcc-4c67-941b-159a5702f06b', None, 'N/A', 'Removed in New Color Picker page')
        
        self.report.start_uuid('96a3fb7b-1bc4-443c-858e-10734253247a')     
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 255)
        # page_edit.select_from_bottom_edit_menu('Color')
        # page_edit.color_selector.set_red_number(0)
        # page_edit.color_selector.set_green_number(255)
        # page_edit.color_selector.set_blue_number(230)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('96a3fb7b-1bc4-443c-858e-10734253247a', True if (not compare_result) else False)        
        
        self.report.start_uuid('dd5eb183-2ccf-4550-bf15-6455bc497f99')
        pic_base = page_edit.get_preview_pic()
        # page_edit.select_from_bottom_edit_menu('Color')
        # page_edit.el(L.edit.backdrop.preset_red).click()
        page_edit.title_designer.select_color_by_order(7)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('dd5eb183-2ccf-4550-bf15-6455bc497f99', True if (not compare_result) else False)     

        self.report.start_uuid('daf84af7-8760-429a-a853-6b643117e15e')   
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Font')
        page_edit.mgt_set_font_by_name('Coming Soon', 'No')
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('daf84af7-8760-429a-a853-6b643117e15e', True if (not compare_result) else False)          
        
        self.report.start_uuid('ca5ca0f3-e212-424b-ad15-0d1a39d220b7')   
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Font')
        page_edit.title_designer.mgt_download_font()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('ca5ca0f3-e212-424b-ad15-0d1a39d220b7', True if (not compare_result) else False)

        self.report.start_uuid('a9de4c5c-6c5f-4143-8296-5bf6a942f4fc')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Font')
        page_edit.title_designer.mgt_download_premium_font()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('a9de4c5c-6c5f-4143-8296-5bf6a942f4fc', True if (not compare_result) else False)
        
        # Select another text in title
        self.report.start_uuid('4daf549a-61c7-42b3-a8af-bee7f6f565f0')     
        page_edit.el(L.edit.motion_graphic_title.dropdownmenu_text).click()
        time.sleep(3)
        page_edit.mgt_select_title_from_menu(1)
        time.sleep(3)
        result = True if page_edit.el(L.edit.motion_graphic_title.dropdownmenu_text).text == 'By CyberLink' else False
        self.report.new_result('4daf549a-61c7-42b3-a8af-bee7f6f565f0', result)  
        
        self.report.start_uuid('440ca53b-c753-4247-9a66-e4f0ba687667')   
        self.report.start_uuid('884da1eb-4c87-4e2c-940e-28781dc89fbe')   
        pic_base = page_edit.get_preview_pic()
        #page_edit.select_from_bottom_edit_menu('Edit Text')
        page_edit.select_from_bottom_edit_menu_by_order(1)
        page_edit.el(L.edit.title_designer.title_text_edit_area).set_text('CyberLink\ntest')
        page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('440ca53b-c753-4247-9a66-e4f0ba687667', True if (not compare_result) else False)
        self.report.new_result('884da1eb-4c87-4e2c-940e-28781dc89fbe', True if page_edit.el(L.edit.motion_graphic_title.dropdownmenu_text).text == 'CyberLink test' else False)
        
        # Set color
        self.report.start_uuid('c8ec44b7-9436-4362-a192-c038fa5802e0')
        # pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Color')
        page_edit.title_designer.select_color_by_order(0)
        result = page_edit.title_designer.set_hue_slider(0.3)
        # page_edit.color_selector.set_hue_slider(10)
        # page_edit.driver.driver.back()
        # pic_after = page_edit.get_preview_pic()
        # compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
        #     pic_base, pic_after)
        self.report.new_result('c8ec44b7-9436-4362-a192-c038fa5802e0', result)
        
        self.report.start_uuid('d805097d-8135-42f1-a4a6-7bd15334d470')
        # pic_base = page_edit.get_preview_pic()
        # page_edit.select_from_bottom_edit_menu('Color')
        # page_edit.color_selector.set_saturation_slider(150)
        # page_edit.driver.driver.back()
        # pic_after = page_edit.get_preview_pic()
        # compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
        #     pic_base, pic_after)
        self.report.new_result('d805097d-8135-42f1-a4a6-7bd15334d470', None, 'N/A', 'Removed in New Color Picker page')
        
        self.report.start_uuid('f8e0ed84-7b5e-42bc-9a22-e5fbe24dcbb3')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 255)
        # page_edit.select_from_bottom_edit_menu('Color')
        # page_edit.color_selector.set_red_number(0)
        # page_edit.color_selector.set_green_number(255)
        # page_edit.color_selector.set_blue_number(230)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('f8e0ed84-7b5e-42bc-9a22-e5fbe24dcbb3', True if (not compare_result) else False)        
        
        self.report.start_uuid('c836cefd-bf4a-47c0-9019-a50be30a2de9')
        pic_base = page_edit.get_preview_pic()
        # page_edit.select_from_bottom_edit_menu('Color')
        # page_edit.el(L.edit.backdrop.preset_red).click()
        page_edit.title_designer.select_color_by_order(7)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('c836cefd-bf4a-47c0-9019-a50be30a2de9', True if (not compare_result) else False)     
        
        
        self.report.start_uuid('0038fe83-6a99-471c-8a6f-bdc56cc9e832')   
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Font')
        page_edit.mgt_set_font_by_name('Coming Soon', 'No')
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('0038fe83-6a99-471c-8a6f-bdc56cc9e832', True if (not compare_result) else False)          
        
        self.report.start_uuid('d88d431d-cd14-4a03-bbad-c6f588f6a85d')   
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Font')
        page_edit.title_designer.mgt_download_font()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('d88d431d-cd14-4a03-bbad-c6f588f6a85d', True if (not compare_result) else False)

        self.report.start_uuid('c0ac8fc2-cf02-4a9b-ac3e-1ff12409aa6e')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Font')
        page_edit.title_designer.mgt_download_premium_font()
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('c0ac8fc2-cf02-4a9b-ac3e-1ff12409aa6e', True if (not compare_result) else False)

        # Color Palette
        self.report.start_uuid('b17bd9f2-920e-4537-b1fc-895f525c3477')
        page_edit.click(L.edit.menu.delete)
        page_edit.el(L.edit.menu.fx_layer).click()
        page_media.select_title_category('Expressive Titles')
        page_media.search_template_by_image('mgt_premium')
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        pic_before = page_edit.snapshot_bottom_menu()
        result = page_edit.select_from_bottom_edit_menu('Graphics Color')
        self.report.new_result('b17bd9f2-920e-4537-b1fc-895f525c3477', result)

        self.report.start_uuid('a84beba8-2265-4db4-af63-b3817965cfb9')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_palette_by_order(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('a84beba8-2265-4db4-af63-b3817965cfb9', True if (not compare_result) else False)

        self.report.start_uuid('bebe4db5-c6e5-4b78-8d67-e614568800d6')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_palette_by_order(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('bebe4db5-c6e5-4b78-8d67-e614568800d6', True if (not compare_result) else False)

        self.report.start_uuid('32eab35d-0ef3-4e96-98f2-ffb1d8f893c7')
        pic_base = page_edit.snapshot_bottom_menu()
        page_edit.title_designer.select_color_palette_by_order(3)
        pic_after = page_edit.snapshot_bottom_menu()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('32eab35d-0ef3-4e96-98f2-ffb1d8f893c7', True if (not compare_result) else False)

        self.report.start_uuid('9f307638-1450-4e31-bf54-2e2a910574e7')
        page_edit.driver.driver.back()
        time.sleep(5)
        pic_after = page_edit.snapshot_bottom_menu()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_before, pic_after)
        self.report.new_result('9f307638-1450-4e31-bf54-2e2a910574e7', True if (not compare_result) else False)