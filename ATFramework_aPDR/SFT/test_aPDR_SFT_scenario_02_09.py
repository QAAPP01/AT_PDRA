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


class Test_SFT_Scenario_02_09:
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
    
    def test_sce_02_09_01(self):
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)

        self.report.start_uuid('d56f8534-a7ea-4431-b876-cc0a9f95ceb5')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_edit.select_from_bottom_edit_menu('Volume')
        page_edit.timeline_swipe('left', 400)
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('d56f8534-a7ea-4431-b876-cc0a9f95ceb5', True if (not compare_result) else False)
        
        self.report.start_uuid('27fc139f-0c63-40d4-aaaa-01b0bb042149')
        pic_base = pic_after
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('27fc139f-0c63-40d4-aaaa-01b0bb042149', True if (not compare_result) else False)        
        
        # Fade in
        self.report.start_uuid('30418966-f420-4c92-a617-6e2b532d0c9a')
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.select_from_bottom_edit_menu('Fade in')
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('30418966-f420-4c92-a617-6e2b532d0c9a', True if (not compare_result) else False)        
        
        # Fade out
        self.report.start_uuid('e403f109-fe08-4d00-a0fe-2a1d8923b48e')
        page_edit.timeline_swipe('left', 400)
        page_edit.driver.driver.back()
        page_edit.select_from_bottom_edit_menu('Split')
        time.sleep(2)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Volume')
        time.sleep(2)
        pic_base = page_edit.keyframe.get_keyframe_pic()
        page_edit.select_from_bottom_edit_menu('Fade out')
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('e403f109-fe08-4d00-a0fe-2a1d8923b48e', True if (not compare_result) else False)        
        
        # Remove all   
        self.report.start_uuid('2d2f1e69-5fe7-4a39-a3a2-9de6fec76b58')
        pic_base = pic_after
        page_edit.keyframe.longpress_keyframe('remove')
        time.sleep(2)
        pic_after = page_edit.keyframe.get_keyframe_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('2d2f1e69-5fe7-4a39-a3a2-9de6fec76b58', True if (not compare_result) else False)        
        
        # Duplicate previous
        self.report.start_uuid('247bbc31-830d-4c79-bb01-1b72f79f6163')
        page_edit.timeline_swipe('right', 400)
        time.sleep(2)
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        page_edit.timeline_swipe('right', 400)
        time.sleep(2)
        page_edit.el(L.edit.keyframe.btn_keyframe).click()
        time.sleep(2)
        #page_edit.audio_configration_set_clip_volume('200')
        page_edit.opacity_set_slider(1)
        page_edit.timeline_swipe('left', 400)
        page_edit.keyframe.longpress_keyframe('previous')
        time.sleep(2)
        result = page_edit.audio_configration_check_clip_volume('100')
        self.report.new_result('247bbc31-830d-4c79-bb01-1b72f79f6163', True if (not result) else False)        
        
        # Duplicate next
        self.report.start_uuid('5c61a699-1170-4d31-b6cd-78d9e4380852')
        #page_edit.audio_configration_set_clip_volume('50')
        page_edit.opacity_set_slider(0.1)
        page_edit.timeline_swipe('right', 400)
        time.sleep(2)
        page_edit.keyframe.longpress_keyframe('next')
        time.sleep(2)
        result = page_edit.audio_configration_check_clip_volume('200')
        self.report.new_result('5c61a699-1170-4d31-b6cd-78d9e4380852', True if (not result) else False)
        
        
    # @pytest.mark.skip
    
    def test_sce_02_09_02(self):
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        
        # Free voice changer effect
        self.report.start_uuid('953ce5fc-3fe4-4441-ad00-1f16d3ca8b07')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_edit.select_from_bottom_edit_menu('Audio Tool')
        page_edit.select_from_bottom_edit_menu('Voice Changer')
        result = page_edit.select_from_bottom_edit_menu('Man')
        self.report.new_result('953ce5fc-3fe4-4441-ad00-1f16d3ca8b07', result)    
        
        # Premium voice changer effect
        self.report.start_uuid('6eb9cfd5-ce77-4c36-b590-5e064dff52ae')
        result = page_edit.select_from_bottom_edit_menu('Child')
        self.report.new_result('6eb9cfd5-ce77-4c36-b590-5e064dff52ae', result)               
        
        self.report.start_uuid('5a51f30d-61dd-4bc5-9a92-e9d5143e3102')
        page_edit.driver.driver.back()
        if  page_edit.is_exist(L.edit.try_before_buy.remove):
            #page_edit.el(L.edit.try_before_buy.remove).click()
            result = True 
        else:
            result = False
        self.report.new_result('5a51f30d-61dd-4bc5-9a92-e9d5143e3102', result)           
        
        # Try before buy - free trial
        self.report.start_uuid('9059d9a1-1588-47a3-9f71-4c149e5050e2')
        page_edit.el(L.edit.try_before_buy.free_trial).click()  
        if  page_edit.is_exist(L.main.subscribe.back_btn):
            page_edit.el(L.main.subscribe.back_btn).click()
            result = True 
        else:
            result = False
        self.report.new_result('9059d9a1-1588-47a3-9f71-4c149e5050e2', result)             
        
        # Try before buy - remove
        self.report.start_uuid('223ba44b-a92d-4442-9f4b-d3abdb308af7')
        page_edit.el(L.edit.try_before_buy.remove).click()  
        result = page_edit.select_from_bottom_edit_menu('No Effect')
        self.report.new_result('223ba44b-a92d-4442-9f4b-d3abdb308af7', result)            
        
        self.report.start_uuid('08301dd3-aa39-4db0-b9bf-56096c0e0546')
        page_edit.el(L.edit.menu.play).click()  
        result = page_edit.select_from_bottom_edit_menu('No Effect')
        self.report.new_result('08301dd3-aa39-4db0-b9bf-56096c0e0546', result)          
        
        self.report.start_uuid('76a2ea5a-c323-483f-8d5f-986564d80313')
        result = page_edit.select_from_bottom_edit_menu('Man')
        self.report.new_result('76a2ea5a-c323-483f-8d5f-986564d80313', result)
        
        self.report.start_uuid('7fae9a83-25a9-4163-95a6-6414550e3e52')
        result = page_edit.select_from_bottom_edit_menu('Woman')
        self.report.new_result('7fae9a83-25a9-4163-95a6-6414550e3e52', result)
        
        self.report.start_uuid('45f4b6ba-ea5b-441e-b617-c9c16202a687')
        result = page_edit.select_from_bottom_edit_menu('Chipmunk 1')
        self.report.new_result('45f4b6ba-ea5b-441e-b617-c9c16202a687', result)
        
        self.report.start_uuid('cef0ce22-27d0-445d-8276-88b3b359c7b3')
        result = page_edit.select_from_bottom_edit_menu('Chipmunk 2')
        self.report.new_result('cef0ce22-27d0-445d-8276-88b3b359c7b3', result)
        
        self.report.start_uuid('6e8dde37-96da-474f-bdfb-e64dd3e5e5e4')
        result = page_edit.select_from_bottom_edit_menu('Child')
        self.report.new_result('6e8dde37-96da-474f-bdfb-e64dd3e5e5e4', result)
        
        self.report.start_uuid('075b2ef6-30c8-4424-9b1f-607c2408db14')
        result = page_edit.select_from_bottom_edit_menu('Robot')
        self.report.new_result('075b2ef6-30c8-4424-9b1f-607c2408db14', result)
        
        self.report.start_uuid('42c874c3-9798-43f6-a7c5-8e889a09959a')
        result = page_edit.select_from_bottom_edit_menu('Duck')
        self.report.new_result('42c874c3-9798-43f6-a7c5-8e889a09959a', result)
        
        self.report.start_uuid('f16d4f20-a110-43e4-a2dc-ba1498b8a75c')
        result = page_edit.select_from_bottom_edit_menu('Radio 1')
        self.report.new_result('f16d4f20-a110-43e4-a2dc-ba1498b8a75c', result)
        
        self.report.start_uuid('08af559d-7682-4192-acf6-373515681e60')
        result = page_edit.select_from_bottom_edit_menu('Radio 2')
        self.report.new_result('08af559d-7682-4192-acf6-373515681e60', result)
        
        self.report.start_uuid('10479983-21c4-4bb9-ad54-4c5e6065475a')
        result = page_edit.select_from_bottom_edit_menu('Phone 1')
        self.report.new_result('10479983-21c4-4bb9-ad54-4c5e6065475a', result)
        
        self.report.start_uuid('c21d6722-d9ad-450e-aac9-140e510042ab')
        result = page_edit.select_from_bottom_edit_menu('Phone 2')
        self.report.new_result('c21d6722-d9ad-450e-aac9-140e510042ab', result)

   #@pytest.mark.skip
    
    def test_sce_02_09_03(self):
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        
        # Apply denoise
        self.report.start_uuid('86e660a0-40c8-4686-9474-4286cd5879e1')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_edit.select_from_bottom_edit_menu('Audio Tool')
        page_edit.select_from_bottom_edit_menu('Denoise')
        default_value = page_edit.audio_denoise.get_strength_value()
        if default_value == '80':
            result = True
        else:
            result = False
        self.report.new_result('86e660a0-40c8-4686-9474-4286cd5879e1', result)

        
        self.report.start_uuid('3ba55605-d229-4e3b-969f-df2dab85ba24')
        result = page_edit.check_premium_features_used()
        self.report.new_result('3ba55605-d229-4e3b-969f-df2dab85ba24', result)      

        self.report.start_uuid('ba438ea2-9430-4936-b59c-1625dface96d')
        page_edit.audio_denoise.set_slider(0)
        max_value = page_edit.audio_denoise.get_strength_value()
        if max_value == '100':
            result = True
        else:
            result = False
        self.report.new_result('ba438ea2-9430-4936-b59c-1625dface96d', result)
        
        self.report.start_uuid('783d8129-b35f-4906-92ac-453585fe19ec')
        page_edit.audio_denoise.set_slider(1)
        min_value = page_edit.audio_denoise.get_strength_value()
        if min_value == '0':
            result = True
        else:
            result = False
        self.report.new_result('783d8129-b35f-4906-92ac-453585fe19ec', result)

        self.report.start_uuid('bdf30ff8-04ec-43ed-87a8-32d4a0e4cf99')
        result = page_edit.select_from_bottom_edit_menu('Remove')
        self.report.new_result('bdf30ff8-04ec-43ed-87a8-32d4a0e4cf99', result)

        # Apply Extract Audio
        self.report.start_uuid('2f73f44a-90c9-48b3-9095-84b09bd7010b')
        result = page_edit.select_from_bottom_edit_menu('Extract Audio')
        self.report.new_result('2f73f44a-90c9-48b3-9095-84b09bd7010b', result)

        self.report.start_uuid('ace9c10a-8a2d-411c-b463-08c9691dce45')
        time.sleep(30)
        result = page_edit.timeline_check_item_on_track('mp4.mp4', 3, 'Audio')
        self.report.new_result('ace9c10a-8a2d-411c-b463-08c9691dce45', result)