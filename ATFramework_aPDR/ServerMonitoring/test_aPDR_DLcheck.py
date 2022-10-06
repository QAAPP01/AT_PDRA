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
report = REPORT_INSTANCE

pdr_package = PACKAGE_NAME
ad_package = 'com.android.vending'
test_material_folder = TEST_MATERIAL_FOLDER


class Test_DLcheck:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver session>============')
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
        self.test_material_folder = test_material_folder
        
        # retry 3 time if craete driver fail
        for retry in range(3):
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
    def test_sce_video(self):
        #create new project > set aspect ratio
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)

        # Enter Shutterstock
        self.report.start_uuid('0ebd7445-c423-484c-9853-c5fb70c2f83d')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                #page_main._terminate_app(pdr_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("video")
                page_main.project_set_16_9()
                page_media.switch_to_video_library()
                page_media.select_media_by_text('Stock Video')
                page_media.select_media_by_order(2)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                page_media.select_media_by_order(2)

                time.sleep(5)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)    
                retry -= 1
        self.report.new_result('0ebd7445-c423-484c-9853-c5fb70c2f83d', result) 
            
            
        
        # Search in Shutterstock
        self.report.start_uuid('ccfbc4dd-6bc0-469a-89a4-0965dae1baa4')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("video")
                page_main.project_set_16_9()
                page_media.switch_to_video_library()
                page_media.select_media_by_text('Stock Video')
                time.sleep(15)
                page_media.search_video('star')
                page_media.select_media_by_order(2)
                # page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                # page_media.select_media_by_order(1)
                page_media.select_media_by_order(2)
                time.sleep(5)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)    
                retry -= 1
        self.report.new_result('ccfbc4dd-6bc0-469a-89a4-0965dae1baa4', result) 

        
        # Enter stock video: Getty Images
        self.report.start_uuid('d15bbbca-245e-4829-bf9f-501683992d7b')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("video")
                page_main.project_set_16_9()
                page_media.switch_to_video_library()
                page_media.select_media_by_text('Stock Video')
                page_media.el(L.import_media.video_library.tab_video_gettyimages).click()
                page_media.select_media_by_order(2)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('d15bbbca-245e-4829-bf9f-501683992d7b', result)        
        
        
        # Search in Getty Images
        self.report.start_uuid('ff1a390d-adda-487f-99f7-d791232aa671')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("video")
                page_main.project_set_16_9()
                page_media.switch_to_video_library()
                page_media.select_media_by_text('Stock Video')
                page_media.el(L.import_media.video_library.tab_video_gettyimages).click()
                time.sleep(15)
                page_media.search_video('ball')
                page_media.select_media_by_order(2)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('ff1a390d-adda-487f-99f7-d791232aa671', result)         
        
        # Enter stock video: pixabay
        self.report.start_uuid('2d748d11-432d-489b-bbad-f2f710608992')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("video")
                page_main.project_set_16_9()
                page_media.switch_to_video_library()
                page_media.select_media_by_text('Stock Video')
                # page_media.el(L.import_media.video_library.tab_pixabay).click()
                page_media.select_stock_category('pixabay')
                page_media.select_media_by_order(2)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('2d748d11-432d-489b-bbad-f2f710608992', result)        
        
        
        # Search in pixabay
        self.report.start_uuid('dd73a4e5-97c8-4d66-8bc9-885b4e0af3a4')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("video")
                page_main.project_set_16_9()
                page_media.switch_to_video_library()
                page_media.select_media_by_text('Stock Video')
                # page_media.el(L.import_media.video_library.tab_pixabay).click()
                page_media.select_stock_category('pixabay')
                time.sleep(15)
                page_media.search_video('ball')
                # time.sleep(15)
                page_media.select_media_by_order(2)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('dd73a4e5-97c8-4d66-8bc9-885b4e0af3a4', result) 

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_image(self):
        #create new project > set aspect ratio
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)

        self.report.start_uuid('54009239-efee-48fa-bcba-a2cfac0116a6')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                #page_main._terminate_app(pdr_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                # page_main.start_app(pdr_package)
                # time.sleep(10)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("image")
                page_main.project_set_16_9()      
                page_media.switch_to_photo_library()            
                page_media.select_media_by_text('Stock Photo')
                # time.sleep(15)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('54009239-efee-48fa-bcba-a2cfac0116a6', result)        

        # Search in Shutterstock
        self.report.start_uuid('21cac099-2753-47c0-9185-f0ed0440d4f0')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                #page_main._terminate_app(pdr_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                # page_main.start_app(pdr_package)
                # time.sleep(10)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("image")
                page_main.project_set_16_9()      
                page_media.switch_to_photo_library()            
                page_media.select_media_by_text('Stock Photo')
                # time.sleep(15)
                page_media.search_video('star')
                time.sleep(15)
                page_media.select_media_by_order(2)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('21cac099-2753-47c0-9185-f0ed0440d4f0', result) 
        
        # Getty Images photo
        self.report.start_uuid('403d1a49-4f83-460f-9617-fbd50e85bce5')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                #page_main._terminate_app(pdr_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                # page_main.start_app(pdr_package)
                # time.sleep(10)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("image")
                page_main.project_set_16_9()      
                page_media.switch_to_photo_library()            
                page_media.select_media_by_text('Stock Photo')
                time.sleep(15)
                page_media.el(L.import_media.video_library.tab_video_gettyimages).click()
                # time.sleep(15)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('403d1a49-4f83-460f-9617-fbd50e85bce5', result)        

        # Search in Getty Images
        self.report.start_uuid('3fbf197f-0898-4169-ae70-832d236a4aef')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("image")
                page_main.project_set_16_9()      
                page_media.switch_to_photo_library()            
                page_media.select_media_by_text('Stock Photo')
                time.sleep(15)
                page_media.el(L.import_media.video_library.tab_video_gettyimages).click()
                time.sleep(15)
                page_media.search_video('star')
                page_media.select_media_by_order(2)
                page_media.select_media_by_order(1)
                page_media.download_video()
                time.sleep(5)
                page_media.select_media_by_order(1)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('3fbf197f-0898-4169-ae70-832d236a4aef', result) 
        
        # Download sticker
        self.report.start_uuid('a04e1acd-9ce5-407d-ab07-3499aeabf6bd')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("image")
                page_main.project_set_16_9()
                time.sleep(15)
                page_edit.back()
                time.sleep(5)
                page_edit.click(L.edit.menu.effect)
                page_media.switch_to_sticker_library()
                time.sleep(5)
                result = page_media.select_sticker_by_order(1)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('a04e1acd-9ce5-407d-ab07-3499aeabf6bd', result)        


    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_music(self):
        #create new project > set aspect ratio
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        
        self.report.start_uuid('7b3fcf9b-9b4d-4ac1-945c-4ab0b13d58b7')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                #page_main._terminate_app(pdr_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                # page_main.start_app(pdr_package)
                # time.sleep(10)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("music")
                page_main.project_set_16_9()
                page_media.switch_to_music_library()
                page_media.select_media_by_text('Stock Music')
                time.sleep(15)
                page_media.select_media_by_order(1)
                time.sleep(5)
                page_media.select_list_media_by_order(1)
                page_media.download_music()
                time.sleep(5)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('7b3fcf9b-9b4d-4ac1-945c-4ab0b13d58b7', result)        
        
        self.report.start_uuid('faaa7482-3816-4fae-b258-4f07f8112cab')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("music")
                page_main.project_set_16_9()
                page_media.switch_to_music_library()
                page_media.select_media_by_text('Stock Music')
                time.sleep(5)
                category_count = page_edit.calculate_library_content_amount()
                result = True if category_count >= 46 else False
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('faaa7482-3816-4fae-b258-4f07f8112cab', result, f'category_count={category_count}' )        

        # DL CL music
        self.report.start_uuid('cbf14b6b-ddd0-4921-bbd2-73b2cccd24c8')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                #page_main._terminate_app(pdr_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("music")
                page_main.project_set_16_9()
                page_media.switch_to_music_library()
                page_media.select_media_by_text('Stock Music')
                page_media.el(L.import_media.music_library.pdr_tab).click()
                time.sleep(15)
                page_media.select_media_by_order(1)
                time.sleep(5)
                page_media.select_list_media_by_order(1)
                page_media.download_music()
                time.sleep(5)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('cbf14b6b-ddd0-4921-bbd2-73b2cccd24c8', result) 
               
        # DL CL sound
        self.report.start_uuid('9f68b3c8-aacc-44a6-a106-37005f6cad5a')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("music")
                page_main.project_set_16_9()
                page_media.switch_to_soundfx_library()
                time.sleep(15)
                page_media.select_media_by_order(1)
                time.sleep(5)
                page_media.select_list_media_by_order(1)
                page_media.download_music()
                time.sleep(5)
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('9f68b3c8-aacc-44a6-a106-37005f6cad5a', result) 
       
      
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_effect(self):
        #create new project > set aspect ratio
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        
        self.report.start_uuid('c055d555-e197-4358-a941-c484e4707064')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("effect")
                page_main.project_set_16_9()
                page_media.select_media_by_text(self.test_material_folder)
                time.sleep(5)
                page_media.select_media_by_text('slow_motion.mp4')
                page_media.el(L.import_media.library_gridview.add).click()
                page_edit.timeline_select_media('slow_motion.mp4', 'Video')
                page_edit.select_from_bottom_edit_menu('Filter')
                page_edit.el(L.edit.color_sub.get_more).click()
                time.sleep(5)
                page_media.select_media_by_order(1)
                page_media.download_video()
                result = page_edit.is_exist(L.import_media.library_gridview.add)
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('c055d555-e197-4358-a941-c484e4707064', result)        
 
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_title(self):
        #create new project > set aspect ratio
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)

        self.report.start_uuid('f08f92f3-0fc3-4002-ab85-f1aa8864118c')
        result = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("title")
                page_main.project_set_16_9()
                page_edit.el(L.edit.menu.home).click()
                page_media.el(L.edit.menu.effect).click()
                page_media.el(L.edit.effect_sub.title).click()
                time.sleep(5)
                page_media.select_media_by_order(1)     
                time.sleep(5)
                page_media.el(L.import_media.library_gridview.add).click()
                page_edit.timeline_select_item_by_index_on_track(2, 1)
                page_edit.el(L.edit.preview.btn_title_designer_right_top).click()
                result = page_edit.title_designer.download_font()
                if result: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('f08f92f3-0fc3-4002-ab85-f1aa8864118c', result)
 
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_produce(self):
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        
        self.report.start_uuid('576cffcc-9874-4dfd-a6a3-474f57e1cd3b')
        result_finish_upload = False
        for retry in range(3):
            try:
                page_main._terminate_app(ad_package)
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.subscribe(0)
                page_main.project_click_new()
                page_main.project_set_name("title")
                page_main.project_set_16_9()
                page_edit.el(L.edit.menu.home).click()
                page_media.el(L.edit.menu.effect).click()
                page_media.el(L.edit.effect_sub.title).click()
                time.sleep(5)
                page_media.select_media_by_order(1)     
                time.sleep(5)
                page_media.el(L.import_media.library_gridview.add).click()
                page_edit.timeline_select_item_by_index_on_track(2, 1)
                time.sleep(5)
                page_produce.click(L.edit.menu.produce)
                page_produce.select_cloud()
                page_produce.exist_click(L.produce.cloud.signout,3)
                page_produce.click(L.produce.cloud.export)
                page_produce.set_text(L.produce.cloud.email, "cloudtest193@cyberlink.com")
                page_produce.set_text(L.produce.cloud.pw, "1234")
                page_produce.click(L.produce.cloud.signin)
                page_produce.close_produce_page()
                result_finish_upload = page_produce.is_exist(L.produce.tab.cloud)
                if result_finish_upload: 
                    logger('Test pass!')
                    break
                else:
                    raise Exception("Test fail")
            except Exception as e:
                logger(e)   
                retry -= 1
        self.report.new_result('576cffcc-9874-4dfd-a6a3-474f57e1cd3b', result_finish_upload)