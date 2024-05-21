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


class Test_SFT_Scenario_02_07:
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
    
    def test_sce_02_07_01(self):
        media_list = ['01_static.mp4']
        self.report.start_uuid('b1c17996-e38a-4841-b229-479f99ab0024')
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
        self.report.new_result('b1c17996-e38a-4841-b229-479f99ab0024',
                               page_edit.check_preview_aspect_ratio(project_title))
        
        self.report.start_uuid('a3966abc-292f-4adf-afd9-556c68555f8b')   
        page_edit.el(L.edit.menu.fx_layer).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(2)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        # open Transform Keyframe panel
        page_edit.select_from_bottom_edit_menu('Transform Keyframe')
        time.sleep(3)
        x, y, scale, rotation = page_edit.keyframe.get_transform_keyframe_value()
        if  x == '0.500' and y == '0.500' and scale == '0.500' and rotation == '0':
            result = True
        else:
            result = False
        self.report.new_result('a3966abc-292f-4adf-afd9-556c68555f8b', result)
        
        self.report.start_uuid('e324b57f-3445-4d3a-933c-db81a942f21c') 
        result = page_edit.keyframe.add_remove_keyframe()
        self.report.new_result('e324b57f-3445-4d3a-933c-db81a942f21c', result)       
        
        self.report.start_uuid('b95cf6e2-f320-442e-9498-772346d8d7d0') 
        result = page_edit.keyframe.add_remove_keyframe()
        self.report.new_result('b95cf6e2-f320-442e-9498-772346d8d7d0', result) 
        
        self.report.start_uuid('38d92045-71fa-4f9a-9fad-78c4a69faa40') 
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.play).click()
        time.sleep(5)
        result = page_edit.keyframe.add_remove_keyframe()
        self.report.new_result('38d92045-71fa-4f9a-9fad-78c4a69faa40', result)
        
        # modify Scale on preview
        self.report.start_uuid('0c7d6e56-564f-485d-9764-06c1ca9e8827') 
        page_edit.driver.driver.back()
        page_edit.driver.driver.back()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Transform Keyframe')
        time.sleep(3)
        page_effect.modify_effect_size()
        x, y, scale_edit, rotation = page_edit.keyframe.get_transform_keyframe_value()
        if scale == scale_edit:
            result = False
        else:
            result = True
        self.report.new_result('0c7d6e56-564f-485d-9764-06c1ca9e8827', result)  
        
        # Rotate on preview
        self.report.start_uuid('6d26679f-8948-47d8-a00d-b034f519f47b') 
        page_effect.modify_effect_rotate('up')
        x, y, scale, rotation_up = page_edit.keyframe.get_transform_keyframe_value()
        if rotation == rotation_up:
            result = False
        else:
            result = True
        self.report.new_result('6d26679f-8948-47d8-a00d-b034f519f47b', result)
        
        self.report.start_uuid('07b812c9-8508-4070-9059-338403b0d8b2') 
        page_effect.modify_effect_rotate('down')
        x, y, scale, rotation_down = page_edit.keyframe.get_transform_keyframe_value()
        if rotation_up == rotation_down:
            result = False
        else:
            result = True
        self.report.new_result('07b812c9-8508-4070-9059-338403b0d8b2', result) 
        
        # Open Opacity
        self.report.start_uuid('c36bed45-bb59-4a93-8e2a-08179f4be76f') 
        self.report.start_uuid('1e052050-13a5-4993-b9a7-04dac1851529') 
        page_edit.el(L.edit.edit_sub.back_button).click()
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.select_from_bottom_edit_menu('Opacity')
        time.sleep(1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)
        self.report.new_result('c36bed45-bb59-4a93-8e2a-08179f4be76f', result)  
        self.report.new_result('1e052050-13a5-4993-b9a7-04dac1851529', result)  
       
        self.report.start_uuid('b407aabc-dad2-4696-a279-8f040e27f985') 
        result = page_edit.keyframe.add_remove_keyframe()
        self.report.new_result('b407aabc-dad2-4696-a279-8f040e27f985', result)    
       
        self.report.start_uuid('1df8419f-1eef-4587-b178-5a37a72d0259') 
        pic_base = pic_after
        page_edit.el(L.edit.edit_sub.back_button).click()
        page_edit.select_from_bottom_edit_menu('Fade')
        page_edit.select_adjustment_from_bottom_edit_menu('Fade in')
        time.sleep(1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)       
        self.report.new_result('1df8419f-1eef-4587-b178-5a37a72d0259', result)      
        
        self.report.start_uuid('b0f3f7b6-891a-4c4b-8972-884a2747b5e7') 
        pic_base = pic_after
        page_edit.el(L.edit.edit_sub.back_button).click()
        page_edit.select_from_bottom_edit_menu('Fade')
        page_edit.select_adjustment_from_bottom_edit_menu('Fade out')
        time.sleep(1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)       
        self.report.new_result('b0f3f7b6-891a-4c4b-8972-884a2747b5e7', result)    

        self.report.start_uuid('7af591a4-19cc-4c5f-b2d3-20308d3eb054') 
        page_edit.el(L.edit.edit_sub.back_button).click()
        time.sleep(1)
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.select_from_bottom_edit_menu('Blending')
        time.sleep(1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)       
        self.report.new_result('7af591a4-19cc-4c5f-b2d3-20308d3eb054', result) 
        
        self.report.start_uuid('c57ccc73-c7e9-4110-9ba1-ace4189d3e45') 
        page_edit.el(L.edit.edit_sub.back_button).click()
        time.sleep(1)
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.select_from_bottom_edit_menu('Mask')
        time.sleep(1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)       
        self.report.new_result('c57ccc73-c7e9-4110-9ba1-ace4189d3e45', result) 
   
        # Add keyframe button should be grayed out when no mask
        self.report.start_uuid('bf7dca30-4cad-4c23-b94f-40745080ed8e') 
        result = not (page_edit.keyframe.get_add_keyframe_btn_status())
        self.report.new_result('bf7dca30-4cad-4c23-b94f-40745080ed8e', result)     
        
        # Add keyframe button should be enable after apply mask
        self.report.start_uuid('1ff3acfc-6f12-444b-9efe-2e4de7d32404') 
        page_edit.select_mask_linear()
        result = page_edit.keyframe.get_add_keyframe_btn_status()
        self.report.new_result('1ff3acfc-6f12-444b-9efe-2e4de7d32404', result)     
        
        self.report.start_uuid('7ab52324-6bf4-4542-ae83-c0bf4b0d751e') 
        result = page_edit.keyframe.add_remove_keyframe()
        self.report.new_result('7ab52324-6bf4-4542-ae83-c0bf4b0d751e', result)     
        
        self.report.start_uuid('01e55540-c26d-443d-b3bb-2c3f842a66e1') 
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.opacity_set_slider(0.1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)          
        self.report.new_result('01e55540-c26d-443d-b3bb-2c3f842a66e1', result)  
        
        self.report.start_uuid('2ebc4c57-7afd-4513-9680-ee2173a59082') 
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_effect.modify_mask_rotate()
        time.sleep(1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)          
        self.report.new_result('2ebc4c57-7afd-4513-9680-ee2173a59082', result)   
        
        self.report.start_uuid('0c41041c-2cef-4567-b48a-e62120866198') 
        pic_base = pic_after
        page_edit.select_mask_parallel()
        time.sleep(1)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)          
        self.report.new_result('0c41041c-2cef-4567-b48a-e62120866198', result)     
        
        self.report.start_uuid('9b122f81-1a49-4a16-9df7-cfc38258b5c8') 
        page_edit.el(L.edit.menu.back).click()
        page_edit.el(L.edit.menu.back).click()
        page_edit.el(L.edit.menu.home).click()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)        
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.select_from_bottom_edit_menu('Mask')
        time.sleep(2)  
        pic_after = page_edit.keyframe.get_keyframe_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)          
        self.report.new_result('9b122f81-1a49-4a16-9df7-cfc38258b5c8', result) 

