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

class Test_SFT_Scenario_Music_and_Sound_Clips:
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

    #@pytest.mark.skip
    
    def test_sce_music(self):
        #self.report.start_uuid('')
        media_list = ['slow_motion.mp4', 'png.png']
        
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        page_main.el(L.launcher.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_music_library()
        page_media.select_media_by_text('Music')
        time.sleep(3)
        page_edit.el(L.import_media.music_library.pdr_tab).click()
        time.sleep(3)
        # Classical Folder
        udid = ['d1084492-ac6f-460f-bbbe-3d4cd6b445ec']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Classical')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 9 else False, 'sce_music' ,f'Amount = {result}')        
        page_edit.driver.driver.back()
        
        # Comedy Folder
        udid = ['511daa93-82cb-4356-81aa-7196a41bcf48']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Comedy')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 28 else False, 'sce_music' ,f'Amount = {result}')    
        page_edit.driver.driver.back()
        
        # Country Folder
        udid = ['92604302-654c-4335-9ccd-8216071a63d4']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Country')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 18 else False, 'sce_music' ,f'Amount = {result}')     
        page_edit.driver.driver.back()
        
        # Electro Folder
        udid = ['c0d64d4d-873f-4eae-9287-873098d774e2']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Electro')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 20 else False, 'sce_music' ,f'Amount = {result}')     
          
        page_edit.driver.driver.back()
        
        # Jazz Folder
        udid = ['c9f67dee-ad0b-456f-b5a6-eb7998e9cea2']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Jazz')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 22 else False, 'sce_music' ,f'Amount = {result}')     
          
        page_edit.driver.driver.back()
        
        # Lounge Folder
        udid = ['50a008e9-dc25-40c7-96e5-6e1a8f6a4fe7']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Lounge')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 14 else False, 'sce_music' ,f'Amount = {result}')     
        page_edit.driver.driver.back()
        
        # Musical Jingles Folder
        udid = ['76ce8779-8071-42d9-87ea-b0eaac0d804f']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Musical Jingles')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 5 else False, 'sce_music' ,f'Amount = {result}')     

        page_edit.driver.driver.back()
        
        # Orchestral Folder
        udid = ['444d2966-d78d-418d-8486-6fd062e44c95']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Orchestral')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 53 else False, 'sce_music' ,f'Amount = {result}')     
        page_edit.driver.driver.back()
        
        # Piano Folder
        udid = ['a5b59d4f-ad59-4248-8215-8b6e85806642']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Piano')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 31 else False, 'sce_music' ,f'Amount = {result}')     

        page_edit.driver.driver.back()
        
        # Pop Folder
        udid = ['f8a3fcb1-4824-4a2a-af44-dd3e217286da']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Pop')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 28 else False, 'sce_music' ,f'Amount = {result}')     

        page_edit.driver.driver.back()
        
        # Rock Folder
        udid = ['7a913f29-f6d9-4ed2-b14c-0ab65a4ff71f']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Rock')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 26 else False, 'sce_music' ,f'Amount = {result}')     

        page_edit.driver.driver.back()
        
        # World Folder
        udid = ['6143b80b-675c-4904-93ec-7116b2162803']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('World')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 23 else False, 'sce_music' ,f'Amount = {result}')     
                
    #@pytest.mark.skip
    
    def test_sce_sound(self):
        
        media_list = ['png.png']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
     
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        page_main.el(L.launcher.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.import_media).click()
        # page_media.switch_to_music_library()
        page_media.switch_to_sound_clips_library()
        # page_media.select_media_by_text('Sound Clips')
        # page_media.el(L.import_media.music_server_library.tab_sound_clip).click()
        
        # Animals Folder : 54 clips
                        
        udid = ['0b59da80-bb5f-4fbc-938e-a9f83adc930b']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Animals')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 54 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # Environment Folder : 46 clips
                        
        udid = ['cf7b9f07-f305-423c-9fe7-5e99908e2818']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Environment')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 46 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # Instruments Folder : 28 clips
                       
        udid = ['f86b8143-eb10-40fc-8461-3b8c28ff5934']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Instruments')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 28 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # Miscellaneous Folder : 122 clips
                        
        udid = ['be000924-3c22-41de-b502-241c3d816923']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Miscellaneous')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 124 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # Musical Jingles Folder : 29 clips
          
        udid = ['262cd7a6-3581-4950-81f0-3710fdbd79e9']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Musical Jingles')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 29 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # People Folder : 75 clips
        
        udid = ['248d96f5-a999-496b-8c87-6e9b148d0e06']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('People')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 75 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # Sports Folder : 17 clips
                        
        udid = ['7b71e749-e1c0-4cd7-bde0-a424fabe4855']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Sports')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 37 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # Transportation Folder : 40 clips
                        
        udid = ['53949b91-493b-4733-8723-89c416c917f1']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Transportation')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 40 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()
        
        # Weapons Folder : 53 clips
                        
        udid = ['3c3015a2-24d2-4fda-9c66-584bf16010e0']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Weapons')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 53 else False, 'sce_sound' ,f'Amount = {result}')     
                
        page_edit.driver.driver.back()        
        
        # Work/Home/Daily Life Folder : 173 clips
                         
        udid = ['aaf7c1a5-58ad-44fe-bcc3-31da4694ba53']
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text('Work/Home/Daily Life')
        result = page_edit.calculate_music_library_content_amount()
        self.report.add_result(udid[0], True if result >= 173 else False, 'sce_sound' ,f'Amount = {result}')     
        