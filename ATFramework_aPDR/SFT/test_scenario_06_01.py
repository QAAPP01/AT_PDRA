import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest
import time

from pages.locator import locator as L
from pages.locator.locator_type import *

from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
report = REPORT_INSTANCE


test_material_folder = TEST_MATERIAL_FOLDER

BETTER_QUALITY = 0
STANDARD = 1
SMALLER_SIZE = 2

FPS_24 = 0
FPS_30 = 1
FPS_60 = 2

ULTRA_HD = 0
FULL_HD = 1
HD = 2
SD = 3

class Test_sce_06_01_01:    # free account
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        self.report = report
        # ---- local mode > end ----
                                                              
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
        self.driver.start_app(PACKAGE_NAME)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.produce = PageFactory().get_page_object("produce", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)
        self.settings = PageFactory().get_page_object("timeline_settings", self.driver)

        self.main_page.clean_movie_cache()
        self.main_page.project_reload('16_9')
        logger('copying produced video')
        self.main_page.copy_produced_video()
        self.driver.implicit_wait(5)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_01_01(self):
        SUBSCRIPTION_PAGE = 'com.cyberlink.powerdirector.StorePageActivity'
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        _start('d0979612-dcbb-488f-a883-5c29610c2da8')
        result_dispaly_shopping_cart =  main.is_exist(L.main.project.shopping_cart)
        _end('d0979612-dcbb-488f-a883-5c29610c2da8',result_dispaly_shopping_cart)
        
        _start('5e225481-1f07-4891-be84-c78700ee3432')
        main.click(L.main.project.shopping_cart)
        time.sleep(1)
        result_enter_subscription = main.ad.is_subscription_page()
        main.back()
        _end('5e225481-1f07-4891-be84-c78700ee3432',result_enter_subscription)
        
        _start('6d4971d5-8633-4b34-ae6e-aaf68a40f18a')
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #main.click(L.main.project.tutorials)
        main.new_launcher_enter_tutorials()
        result_dispaly_shopping_cart =  main.is_exist(L.main.project.shopping_cart)
        _end('6d4971d5-8633-4b34-ae6e-aaf68a40f18a',result_dispaly_shopping_cart)

        _start('66f283f8-c5ad-42cb-b075-67d11b994ae2')
        main.click(L.main.project.shopping_cart)
        time.sleep(1)
        result_enter_subscription = main.ad.is_subscription_page()
        main.back()
        main.back()
        _end('66f283f8-c5ad-42cb-b075-67d11b994ae2',result_enter_subscription)
        
        _start('b14caff2-a901-4e13-8f1b-c3f5467b7cd4')
        main.project_create_new()
        edit.click(L.edit.timeline.clip)
        edit.click(L.edit.menu.timeline_setting)
        edit.click(L.edit.sub_menu.settings)
        result_dispaly_shopping_cart =  settings.is_exist(L.timeline_settings.settings.shopping_cart)
        _end('b14caff2-a901-4e13-8f1b-c3f5467b7cd4',result_dispaly_shopping_cart)
        
        _start('47c34531-7ba6-40a1-9ebb-adcb34882c4a')
        settings.click(L.timeline_settings.settings.shopping_cart)
        time.sleep(1)
        result_enter_subscription = settings.ad.is_subscription_page()
        settings.back()
        settings.back()
        settings.back()
        settings.back() # at main page
        _end('47c34531-7ba6-40a1-9ebb-adcb34882c4a',result_enter_subscription)
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_01_02(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        ## exit app
        _start('cd7e7776-56a5-449e-ad3b-68869a89a2c1')
        main.back()
        result_has_ad = main.ad.has_ad(L.ad.frame_leave_app)
        main.back()
        _end('cd7e7776-56a5-449e-ad3b-68869a89a2c1',result_has_ad)
        
        ##Project list page (Native Ads)
        _start('cdbb10ea-e4fd-468f-8455-85b5f3123acf')
        main.relaunch_app(PACKAGE_NAME)
        result_ad_x = main.ad.has_x()    # x button of AD in main page
        #_end('cdbb10ea-e4fd-468f-8455-85b5f3123acf',result_ad_x)
        self.report.add_result('cdbb10ea-e4fd-468f-8455-85b5f3123acf', None, 'N/A', 'AT cannot verify')
            
            
        ## Produced video page (Native Ads)
        _start('62ca3975-afc3-4590-b808-c67e8c86523f')
        _start('38f5b994-86ba-4d41-b10a-f1cf3c80d8ce')
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #main.click(L.main.project.btn_produced_videos)
        main.new_launcher_enter_produced_video()
        result_has_ad, result_ratio = main.ad.check_ad_and_ratio(orientation=main.ad.PORTRAIT)
        _end('62ca3975-afc3-4590-b808-c67e8c86523f',result_has_ad)
        _end('38f5b994-86ba-4d41-b10a-f1cf3c80d8ce',result_ratio)
        
        _start('8bc7b8d4-06b0-4e10-98f6-fdce08848166')
        result_enter_ad = main.ad.click_ad()
        _end('8bc7b8d4-06b0-4e10-98f6-fdce08848166',result_enter_ad)
        time.sleep(1)
        main.back_main()  # return main page
        
        ##help page (Native Ads)
        _start('45c5534f-6477-4735-bb2a-2c2ba4b41dfb')
        _start('f7a1b6b9-0fd5-435b-86de-95527972521b')
        #main.click(L.main.project.tutorials)
        main.new_launcher_enter_tutorials()
        result_has_ad, result_ratio = main.ad.check_ad_and_ratio()
        _end('45c5534f-6477-4735-bb2a-2c2ba4b41dfb',result_has_ad)
        _end('f7a1b6b9-0fd5-435b-86de-95527972521b',result_ratio)
        
        _start('15ab10e3-7b24-4d74-8c4b-c4cebe9b0062')
        result_enter_ad = main.ad.click_ad()
        _end('15ab10e3-7b24-4d74-8c4b-c4cebe9b0062',result_enter_ad)
        time.sleep(1)
        main.back_main() # return main page
        
        ## Reverse page
        _start('faf405c7-f194-4b49-9c65-62bed0c20087')
        _start('2156bd1b-d848-40f3-b55f-1938d4e2a2e8')
        main.project_create_new()
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.reverse)
        edit.select_from_bottom_edit_menu('Reverse')
        edit.click(L.edit.reverse.dialog_ok)
        result_has_ad, result_ratio = edit.ad.check_ad_and_ratio()
        _end('faf405c7-f194-4b49-9c65-62bed0c20087',result_has_ad)
        _end('2156bd1b-d848-40f3-b55f-1938d4e2a2e8',result_ratio)
        
        _start('6163defc-d2d6-4bba-ab24-eacb24dcadc0')
        result_enter_ad = edit.ad.click_ad()
        edit.click(L.edit.reverse_video_window.cancel)
        _end('6163defc-d2d6-4bba-ab24-eacb24dcadc0',result_ratio)
        
        ## Stabilizer
        '''
        _start('bd3e1fd6-3905-4fe6-bbbf-abbdecee35e4')
        _start('38430fb0-ce4a-4aa7-9c86-5d8a628573cd')
        #edit.click(L.edit.menu.edit)
        edit.click(L.edit.edit_sub.stabilizer)
        result_has_ad, result_ratio = edit.ad.check_ad_and_ratio()
        _end('bd3e1fd6-3905-4fe6-bbbf-abbdecee35e4',result_has_ad)
        _end('38430fb0-ce4a-4aa7-9c86-5d8a628573cd',result_ratio)
        
        _start('5fbbc2f4-de3a-4eee-b310-82d3b4a82206')
        result_enter_ad = edit.ad.click_ad()
        edit.click(L.edit.reverse_video_window.cancel)
        _end('5fbbc2f4-de3a-4eee-b310-82d3b4a82206',result_ratio)
        '''
        ##Produce video page ( Full screen Ads)
        _start('4449cad8-9150-40b6-9629-8d71ffb19561')
        _start('5d482f66-7879-49c9-8bf2-04c455d37e99')
        edit.click(L.edit.menu.produce)
        edit.click(L.edit.menu.Produce_sub_page.produce)
        produce.click(L.produce.tab.gallery)
        produce.click(L.produce.facebook.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        if not produce.ad.find_target_ad(produce.ad.AD_NORMAL): raise Exception("Find AD error.")
        result_has_ad, result_ratio = produce.ad.check_ad_and_ratio()
        _end('4449cad8-9150-40b6-9629-8d71ffb19561',result_has_ad)
        _end('5d482f66-7879-49c9-8bf2-04c455d37e99',result_ratio)
        
        
        _start('af7e7eec-39fe-43af-9e87-b279a9d33817')
        result_enter_ad = produce.ad.click_ad()
        produce.click(L.produce.facebook.produce_page.cancel)
        _end('af7e7eec-39fe-43af-9e87-b279a9d33817',result_enter_ad)

        ##Produce video page ( Promotion Ads)
        _start('aefefc61-1171-47ec-a421-7ecfe2045c29')
        _start('050c2089-953b-4378-8eec-b833ad1ebdc2')
        produce.click(L.produce.facebook.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        time.sleep(1)
        if not produce.ad.find_target_ad(produce.ad.AD_PROMOTION): raise Exception("Find AD error.")
        result_has_ad, result_ratio = produce.ad.check_ad_and_ratio()
        _end('aefefc61-1171-47ec-a421-7ecfe2045c29',result_has_ad)
        _end('050c2089-953b-4378-8eec-b833ad1ebdc2',result_ratio)
        
        
        _start('7b129dff-a3b2-4516-8997-b684684ffe2e')
        result_enter_ad = produce.ad.click_ad()
        produce.click(L.produce.facebook.produce_page.cancel)
        _end('7b129dff-a3b2-4516-8997-b684684ffe2e',result_enter_ad)

        ## upload cloud
        _start('71b57e46-89d0-45c5-985c-cce98339a0e9')
        _start('3c8122c9-a00c-43fd-a614-4c934bb6b87f')
        produce.select_cloud()
        produce.exist_click(L.produce.cloud.signout,3)
        produce.click(L.produce.cloud.export)
        produce.set_text(L.produce.cloud.email,"cloudtest193@cyberlink.com")
        produce.set_text(L.produce.cloud.pw,"1234")
        produce.click(L.produce.cloud.signin)
        result_has_ad, result_ratio = produce.ad.check_ad_and_ratio()
        _end('71b57e46-89d0-45c5-985c-cce98339a0e9',result_has_ad)
        _end('3c8122c9-a00c-43fd-a614-4c934bb6b87f',result_ratio)
        
        _start('658a40ff-9900-409b-a3da-d3c5b6685673')
        result_enter_ad = produce.ad.click_ad()
        _end('658a40ff-9900-409b-a3da-d3c5b6685673',result_enter_ad)
        produce.close_produce_page()
        
        ## preview watermark
        _start('148eecdd-8f72-4a8d-a1f0-983ac91732db')
        produce.back()
        result_has_watermark = edit.is_exist(L.edit.preview.watermark)
        _end('148eecdd-8f72-4a8d-a1f0-983ac91732db',result_has_watermark)
        
        _start('ee997e3a-a6bf-4af3-bfac-5a6b1b8d84bf')
        edit.click(L.edit.preview.watermark)
        edit.click(L.edit.preview.water_mark_border)
        result_has_ad = bool(edit.ad.get_ad_type())
        _end('ee997e3a-a6bf-4af3-bfac-5a6b1b8d84bf',result_has_ad)
        edit.back()
        
        ## Hide notification in settings
        _start('c4c26350-5c44-4f58-86ac-ecc06b3a1807')
        edit.click(L.edit.menu.timeline_setting)
        edit.click(L.edit.sub_menu.settings)
        result_not_found = not edit.search_text("Notification")
        _end('c4c26350-5c44-4f58-86ac-ecc06b3a1807',result_not_found)
        
        ## version in about page
        _start('e79c449d-0558-46f2-8236-19425a757c0b')
        edit.click(L.edit.settings.about_btn)
        result_version = edit.el(L.edit.settings.about.version).text >= "6.5.0"
        _end('e79c449d-0558-46f2-8236-19425a757c0b',result_version)
        edit.back()
        edit.back()
        edit.back() # un-selecte clip

        ## block  2~9 pip track
        _start('adedfa3b-9a0b-4913-8a35-867b15a0e3ec')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.video)
        import_media.select_media_by_text("00PDRa_Testing_Material")
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        result_block_multiple_pip = import_media.ad.get_ad_type() > 0
        _end('adedfa3b-9a0b-4913-8a35-867b15a0e3ec',result_block_multiple_pip)
        time.sleep(1)
        import_media.back() #close ad
        time.sleep(1)
        import_media.back() # leave test material
        time.sleep(1)
        import_media.back() # leave import media

        ## Block Fx pack
        _start('73cb0b42-6695-4627-ac57-e54d84c9923e')
        _start('6d192dcb-bda6-44a4-9f49-82abd1f3bafb')
        edit.timeline_select_item_by_index_on_track(2, 1)
        #edit.click(L.edit.menu.fx)
        edit.select_from_bottom_edit_menu('Effect')        
        result_subscription , result_unlock_ad = import_media.download_media("Glitch Pack Vol. 1")
        _end('73cb0b42-6695-4627-ac57-e54d84c9923e',result_subscription)
        _end('6d192dcb-bda6-44a4-9f49-82abd1f3bafb',result_unlock_ad)
        import_media.back() # exit import media page
        
        ## Block Title pack (Get more)  
        _start('a25119af-e3ad-4bed-9677-607d37ac6e35')
        _start('75bb1962-00ce-4ab8-bd00-3957a90e6234')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.title)
        result_subscription , result_unlock_ad = import_media.download_media("Fly Pack Vol. 1")
        _end('a25119af-e3ad-4bed-9677-607d37ac6e35',result_subscription)
        _end('75bb1962-00ce-4ab8-bd00-3957a90e6234',result_unlock_ad)
        import_media.back() # exit import media page
        
        ## Block Sticker pack (Get more)    
        _start('c8b0c1eb-c97e-4323-9992-207661955fd5')
        _start('cc0b4d55-7d61-40f0-8c8e-146d568b7b1f')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.sticker)
        result_subscription , result_unlock_ad = import_media.download_media("Decorative Vines Vol.2")
        _end('c8b0c1eb-c97e-4323-9992-207661955fd5',result_subscription)
        _end('cc0b4d55-7d61-40f0-8c8e-146d568b7b1f',result_unlock_ad)
        import_media.back() # exit import media page
        
        ## Block Color pack (Get more)    
        _start('aea8e41b-4555-46d7-8190-c4bfac212ca7')
        _start('a8201435-53e1-42bb-829c-f6260123cbc3')
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        result_subscription , result_unlock_ad = edit.download_media("Aurora")
        _end('aea8e41b-4555-46d7-8190-c4bfac212ca7',result_subscription)
        _end('a8201435-53e1-42bb-829c-f6260123cbc3',result_unlock_ad)
        import_media.back() # exit import media page
        import_media.back() # unselect clip
        
        ## Block some Music/ Sound Clip 
        _start('a7d2cac9-09cd-4b66-9d99-afde1e1311af')
        _start('c134b184-b853-4be8-b25c-d518847beb02')
        edit.click(L.edit.menu.import_media)
        edit.click(L.import_media.menu.music_library)
        result_subscription , result_unlock_ad = import_media.download_media("Classical","Acceptance")
        _end('a7d2cac9-09cd-4b66-9d99-afde1e1311af',result_subscription)
        _end('c134b184-b853-4be8-b25c-d518847beb02',not result_unlock_ad) #6.1.49 should not have AD
        import_media.back() # exit more page
        import_media.back() # exit music page
        import_media.back() # exit import_media page
        
        ## Block 4k/fhd video (Get more)    
        _start('82742047-81ca-4efd-92ca-997b69f5c6d7')
        _start('cfa01e67-32d1-4fe9-9c3b-8a1991693948')
        edit.click(L.edit.menu.produce)
        edit.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.gallery)
        result_subscription , result_unlock_ad = produce.check_produce_ad("Full_HD")
        _end('82742047-81ca-4efd-92ca-997b69f5c6d7',result_subscription)
        _end('cfa01e67-32d1-4fe9-9c3b-8a1991693948',result_unlock_ad)
        
        
        
        
        
class Test_sce_06_02_01:    # purchased account
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        self.report = report
        # ---- local mode > end ----
        self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                              desired_caps)
        self.report.set_driver(self.driver)
        self.driver.start_app(PACKAGE_NAME)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.produce = PageFactory().get_page_object("produce", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)
        self.settings = PageFactory().get_page_object("timeline_settings", self.driver)

        self.main_page.clean_movie_cache()
        self.main_page.clean_projects()
        self.main_page.copy_produced_video()
        # self.main_page.project_reload('16_9')
        self.driver.implicit_wait(5)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()
        
    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_02_01(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        _start('84eaa02a-211c-4cb8-8b69-a55f34177851')
        result_cart = main.is_exist(L.main.project.shopping_cart)
        _end('84eaa02a-211c-4cb8-8b69-a55f34177851',result_cart)
        
        _start('37307ca7-4c66-41fd-bd66-2c8bd3f12e4b')
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        main.click(L.main.project.tutorials)
        result_cart = main.is_exist(L.main.tutorials.shopping_cart)
        _end('37307ca7-4c66-41fd-bd66-2c8bd3f12e4b',result_cart)
        main.back()
        
        _start('a1e3e52c-4bdd-4ce6-8ab1-02d1c61f2f91')
        main.project_create_new()
        edit.click(L.edit.timeline.clip)
        edit.click(L.edit.menu.timeline_setting)
        edit.click(L.edit.sub_menu.settings)
        result_cart = main.is_exist(L.main.tutorials.shopping_cart)
        _end('a1e3e52c-4bdd-4ce6-8ab1-02d1c61f2f91',result_cart)
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_02_02(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        ## account: pdr.test.one@gmail.com / pdrtestone##
        ## exit app
        _start('9115bdc9-2c99-4611-90c3-081c1caec739')
        main.back()
        result_no_ad = not main.ad.get_ad_type()
        main.back()
        _end('9115bdc9-2c99-4611-90c3-081c1caec739',result_no_ad)
        
        ##Project list page (Native Ads)
        _start('34e28205-a565-4545-bf09-c52d287679f6')
        result_no_ad = not main.ad.get_ad_type()
        _end('34e28205-a565-4545-bf09-c52d287679f6',result_no_ad)
        
        ## Help page (Native Ads)
        _start('1cc47e98-78e1-40e1-9a3a-29520154f413')
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        main.click(L.main.project.tutorials)
        result_no_ad = not main.ad.get_ad_type()
        _end('1cc47e98-78e1-40e1-9a3a-29520154f413',result_no_ad)
        main.back()
        
        ## Produced video page (Native Ads)
        _start('b436426d-cba3-49ba-82b0-975fee132362')
        time.sleep(1)
        main.click(L.main.project.btn_produced_videos)
        result_no_ad = not main.ad.get_ad_type()
        _end('b436426d-cba3-49ba-82b0-975fee132362',result_no_ad)
        main.back()  # return main page
        
        ## Reverse page
        _start('b1c1d2ce-cc5f-4425-9e76-4dfe50536d92')
        main.project_create_new()
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.reverse)
        edit.select_from_bottom_edit_menu('Reverse')
        edit.click(L.edit.reverse.dialog_ok)
        result_no_ad = not main.ad.get_ad_type()
        _end('b1c1d2ce-cc5f-4425-9e76-4dfe50536d92',result_no_ad)
        edit.click(L.edit.reverse_video_window.cancel)
        
        ## Stabilizer
        _start('3a3e09bf-b539-4001-a342-5f8149982556')
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.stabilizer)
        edit.select_from_bottom_edit_menu('Stabilizer')
        result_no_ad = not main.ad.get_ad_type()
        _end('3a3e09bf-b539-4001-a342-5f8149982556',result_no_ad)
        edit.click(L.edit.reverse_video_window.cancel)
        
        ## Producing video page (Native Ads)	
        _start('130e95b2-b3bc-4df3-acd0-cc5346e493c6')
        _start('b5034624-a167-41ef-b0de-f1eb97b14d1a')
        produce.click(L.edit.timeline.clip)
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.gallery)
        produce.click(L.produce.gallery.full_hd)
        time.sleep(1.5)
        produce.click(L.produce.gallery.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        result_no_ad = not main.ad.get_ad_type()
        _end('130e95b2-b3bc-4df3-acd0-cc5346e493c6',result_no_ad)
        _end('b5034624-a167-41ef-b0de-f1eb97b14d1a',result_no_ad)
        produce.click(L.produce.gallery.produce_page.cancel)
        
        ## upload cloud
        _start('f9bd229e-e0ba-4ef5-8a22-d7675ea5bbb0')
        produce.select_cloud()
        produce.exist_click(L.produce.cloud.signout,3)
        produce.click(L.produce.cloud.export)
        produce.set_text(L.produce.cloud.email,"cloudtest193@cyberlink.com")
        produce.set_text(L.produce.cloud.pw,"1234")
        produce.click(L.produce.cloud.signin)
        result_no_ad = not main.ad.get_ad_type()
        _end('f9bd229e-e0ba-4ef5-8a22-d7675ea5bbb0',result_no_ad)
        produce.close_produce_page()
        produce.back() # exit produce page
        
        ##Remove Watermark in...
        
        _start('fd9f3f7e-9636-49ad-861f-c3e20df3c7ee')
        result_no_watermark = edit.is_vanish(L.edit.preview.watermark)
        _end('fd9f3f7e-9636-49ad-861f-c3e20df3c7ee',result_no_watermark)
        

        
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_02_03(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        ## Hide notification in settings
        _start('5df0a433-bf69-4619-a649-740462205379')
        main.project_create_new()
        edit.click(L.edit.timeline.clip)
        edit.click(L.edit.menu.timeline_setting)
        edit.click(L.edit.sub_menu.settings)
        result_not_found = not edit.search_text("Notification")
        _end('5df0a433-bf69-4619-a649-740462205379',result_not_found)
        
        ## version in about page
        _start('8f5d4d6d-da5f-4d49-bfbb-79db0a5c7afc')
        edit.search_text("About PowerDirector")
        edit.click(L.edit.settings.about_btn)
        result_version = edit.el(L.edit.settings.about.version).text >= "6.3.0"
        _end('8f5d4d6d-da5f-4d49-bfbb-79db0a5c7afc',result_version)
        time.sleep(1)
        edit.back()
        time.sleep(1)
        edit.back()
        time.sleep(1)
        edit.back() # un-selecte clip

        ## block  3nd pip video track
        _start('14f2a17e-19e0-4d58-9c77-f5d1bef98a82')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.video)
        import_media.select_media_by_text("00PDRa_Testing_Material")
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        time.sleep(1)
        result_maximum = import_media.is_exist(L.edit.timeline.exceed_max_video)
        _end('14f2a17e-19e0-4d58-9c77-f5d1bef98a82',result_maximum)
        import_media.click(L.edit.timeline.exceed_max_video)
        time.sleep(1)
        import_media.back()
        time.sleep(1)
        import_media.back()

        ## Block Fx pack
        _start('e475b40b-188f-45aa-9ab3-e3c470f06f25')
        _start('0b0b35c3-3c7c-49c5-bc7f-917f0da24fa5')
        edit.timeline_select_item_by_index_on_track(2, 1)
        #edit.click(L.edit.menu.fx)
        edit.select_from_bottom_edit_menu('Effect')
        result_subscription , result_unlock_ad = import_media.download_media("Glitch Pack Vol. 1")
        _end('e475b40b-188f-45aa-9ab3-e3c470f06f25',result_subscription)
        _end('0b0b35c3-3c7c-49c5-bc7f-917f0da24fa5',result_unlock_ad)
        import_media.back() # exit import media page
        
        ## Block Title pack (Get more)  
        _start('7b11cab6-e2d4-4ae1-a705-e3b4b199817c')
        _start('570ff0eb-3b6a-43a1-a929-205123549ffd')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.title)
        result_subscription , result_unlock_ad = import_media.download_media("Fly Pack Vol. 1")
        _end('7b11cab6-e2d4-4ae1-a705-e3b4b199817c',result_subscription)
        _end('570ff0eb-3b6a-43a1-a929-205123549ffd',result_unlock_ad)
        import_media.back() # exit import media page
        
        ## Block Sticker pack (Get more)    
        _start('d517e146-9a7c-43de-b3b5-116722349452')
        _start('5e71b450-f59d-4fff-adda-4b9c53aa2e33')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.sticker)
        result_subscription , result_unlock_ad = import_media.download_media("Decorative Vines Vol.2")
        _end('d517e146-9a7c-43de-b3b5-116722349452',result_subscription)
        _end('5e71b450-f59d-4fff-adda-4b9c53aa2e33',result_unlock_ad)
        import_media.back() # exit import media page
        
        ## Block Color pack (Get more)    
        _start('c212bf66-d653-4449-9940-79618beaa496')
        _start('313cfb52-8921-4275-ad8b-1ee5aa324bf0')
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        result_subscription , result_unlock_ad = edit.download_media("Aurora")
        _end('c212bf66-d653-4449-9940-79618beaa496',result_subscription)
        _end('313cfb52-8921-4275-ad8b-1ee5aa324bf0',result_unlock_ad)
        import_media.back() # exit import media page
        import_media.back() # unselect clip
        
        ## Block some Music/ Sound Clip 
        _start('91a89327-6299-4092-ab4e-f1484441f86a')
        _start('38a0c661-e70d-4b3c-b685-397808e52ac2')
        edit.click(L.edit.menu.import_media)
        edit.click(L.import_media.menu.music_library)
        result_subscription , result_unlock_ad = import_media.download_media("Classical","Arirang Blossom")
        _end('91a89327-6299-4092-ab4e-f1484441f86a',result_subscription)
        _end('38a0c661-e70d-4b3c-b685-397808e52ac2',not result_unlock_ad) #6.1.49 should not have AD
        import_media.back() # exit more page
        import_media.back() # exit music page
        import_media.back() # exit import_media page
        
        ## enable 4k/fhd video (Get more)    
        _start('07ecec3e-bc5b-45f9-8c4e-fb5a03e0e36f')
        edit.click(L.edit.menu.produce)
        edit.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.gallery)
        produce.click(L.produce.gallery.full_hd)
        result_no_ad = not produce.ad.get_ad_type()
        _end('07ecec3e-bc5b-45f9-8c4e-fb5a03e0e36f',result_no_ad)
        
        _start('ff2fa2d9-0bbf-470c-b290-b2476244926d')
        produce.click(L.produce.gallery.sd)
        time.sleep(1.5)
        produce.click(L.produce.gallery.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        result_no_watermark = produce.ground_truth_video('video_no_watermark.mp4')
        _end('ff2fa2d9-0bbf-470c-b290-b2476244926d',result_no_watermark)
        
class Test_sce_06_03_01:    # subscribe account
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        self.report = report
        # ---- local mode > end ----
        self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                              desired_caps)
        self.report.set_driver(self.driver)
        self.driver.start_app(PACKAGE_NAME)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.produce = PageFactory().get_page_object("produce", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)
        self.settings = PageFactory().get_page_object("timeline_settings", self.driver)

        self.main_page.clean_movie_cache()
        self.main_page.project_reload('16_9')
        self.main_page.copy_produced_video()
        ## subscribe now
        self.main_page.subscribe()
        
        self.driver.implicit_wait(5)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_03_01(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        _start('5796828c-640a-4a2c-aea3-3cd321157db7')
        result_no_cart = main.is_not_exist(L.main.project.shopping_cart)
        _end('5796828c-640a-4a2c-aea3-3cd321157db7',result_no_cart)
        
        _start('c25e15a3-9b58-48a8-8cd2-0247bb98cecc')
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "up", 200)
        #main.click(L.main.project.tutorials)
        main.new_launcher_enter_tutorials()
        result_no_cart = main.is_not_exist(L.main.tutorials.shopping_cart)
        _end('c25e15a3-9b58-48a8-8cd2-0247bb98cecc',result_no_cart)
        time.sleep(2)
        main.back()
        
        _start('388d9f9e-f698-42e2-8417-49af8254b193')
        #edit.swipe_element(L.main.project.new_launcher_scroll, "down", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "down", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "down", 200)
        #edit.swipe_element(L.main.project.new_launcher_scroll, "down", 200)
        main.project_create_new()
        edit.click(L.edit.timeline.clip)
        edit.click(L.edit.menu.timeline_setting)
        edit.click(L.edit.sub_menu.settings)
        result_no_cart = main.is_not_exist(L.main.tutorials.shopping_cart)
        _end('388d9f9e-f698-42e2-8417-49af8254b193',result_no_cart)
        
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_03_02(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        ## exit app
        _start('3bc0ce98-cf14-4865-861c-2b31a0fe9d0b')
        main.back()
        result_no_ad = not main.ad.get_ad_type()
        main.back()
        _end('3bc0ce98-cf14-4865-861c-2b31a0fe9d0b',result_no_ad)
        
        ##Project list page (Native Ads)
        _start('36100605-816d-4823-a5a7-5276bda1cd7d')
        result_no_ad = not main.ad.get_ad_type()
        _end('36100605-816d-4823-a5a7-5276bda1cd7d',result_no_ad)
        
        ## Produced video page (Native Ads)
        _start('45bfa307-1d43-4920-b8df-3b91269cf71c')
        main.click(L.main.project.btn_produced_videos)
        result_no_ad = not main.ad.get_ad_type()
        _end('45bfa307-1d43-4920-b8df-3b91269cf71c',result_no_ad)
        main.back()  # return main page
        
        ## Help page (Native Ads)
        _start('d93f1fb6-98e1-4234-8e29-f8f04430191a')
        main.click(L.main.project.tutorials)
        result_no_ad = not main.ad.get_ad_type()
        _end('d93f1fb6-98e1-4234-8e29-f8f04430191a',result_no_ad)
        main.back()
        
        ## Reverse page
        _start('28c32bba-3885-4cfd-bc90-5916e782f8c3')
        main.project_create_new()
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.reverse)
        edit.select_from_bottom_edit_menu('Reverse')
        edit.click(L.edit.reverse.dialog_ok)
        result_no_ad = not main.ad.get_ad_type()
        _end('28c32bba-3885-4cfd-bc90-5916e782f8c3',result_no_ad)
        edit.click(L.edit.reverse_video_window.cancel)
        
        ## Stabilizer
        _start('663cc308-d232-4295-9239-53af7c59e232')
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.stabilizer)
        edit.select_from_bottom_edit_menu('Stabilizer')
        result_no_ad = not main.ad.get_ad_type()
        _end('663cc308-d232-4295-9239-53af7c59e232',result_no_ad)
        edit.click(L.edit.reverse_video_window.cancel)
        
        ## Producing video page (Native Ads)
        _start('f89de861-5764-43bf-86a7-a86d34f7f634')
        _start('5934e951-b0eb-4e43-9ea1-515e0711ff9e')
        produce.click(L.edit.timeline.clip)
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.gallery)
        produce.click(L.produce.gallery.full_hd)
        time.sleep(1)
        produce.click(L.produce.gallery.next)
        result_no_ad = not main.ad.get_ad_type()
        _end('f89de861-5764-43bf-86a7-a86d34f7f634',result_no_ad)
        _end('5934e951-b0eb-4e43-9ea1-515e0711ff9e',result_no_ad)
        produce.click(L.produce.gallery.produce_page.cancel)
        
        ## upload cloud
        _start('ac813c42-0b0b-4208-8589-19a7d08841be')
        produce.select_cloud()
        produce.exist_click(L.produce.cloud.signout,3)
        produce.click(L.produce.cloud.export)
        produce.set_text(L.produce.cloud.email,"cloudtest193@cyberlink.com")
        produce.set_text(L.produce.cloud.pw,"1234")
        produce.click(L.produce.cloud.signin)
        result_no_ad = not main.ad.get_ad_type()
        _end('ac813c42-0b0b-4208-8589-19a7d08841be',result_no_ad)
        produce.close_produce_page()
        produce.back() # exit produce page
        
        ##Remove Watermark in...
        
        _start('e741220f-3ef6-44d0-ad94-325d5e8e802f')
        result_no_watermark = edit.is_vanish(L.edit.preview.watermark)
        _end('e741220f-3ef6-44d0-ad94-325d5e8e802f',result_no_watermark)
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_03_03(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        

        _start('53a41c3a-ceb6-463f-9368-a5f9307bc6f6')
        _start('80a77075-6054-4abc-ac5c-0f354bff8139')
        main.project_create_new(ratio = "9:16")
        edit.click(L.edit.timeline.clip)
        edit.back()
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.video)
        import_media.select_media_by_text("01PDRa_Testing_Material")
        import_media.select_media_by_text("00:10")
        #import_media.select_media_by_order(7)
        import_media.click(L.import_media.library_listview.add)
        result_4k_to_fhd = import_media.is_exist(L.import_media.library_gridview.dialog_ok)
        _end('80a77075-6054-4abc-ac5c-0f354bff8139',result_4k_to_fhd)
        _end('53a41c3a-ceb6-463f-9368-a5f9307bc6f6',result_4k_to_fhd)
        import_media.click(L.import_media.library_gridview.dialog_ok)
        import_media.click(L.import_media.library_gridview.dialog_cancel)
        import_media.back()

        ## 9:16 block  3nd pip video track [3.3.58]
        _start('505b6fd4-74ee-4ea5-a207-33658ed7c1c6')
        import_media.select_media_by_text("00PDRa_Testing_Material")
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        result_maximum = import_media.is_exist(L.edit.timeline.exceed_max_video)
        _end('505b6fd4-74ee-4ea5-a207-33658ed7c1c6',result_maximum)
        import_media.click(L.edit.timeline.exceed_max_video)    # close dialog
        time.sleep(1)
        import_media.back()     # exit 00PDRa_Testing_Material
        time.sleep(1)
        import_media.back()     # exit import_media
        time.sleep(1)
        import_media.back()     # exit edit
        time.sleep(1)
        import_media.back()     # exit created project
        
        ## trim video first
        main.project_create_new()
        edit.swipe_element(L.edit.timeline.clip,"left",600)
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.split)
        edit.select_from_bottom_edit_menu('Split')
        edit.select_main_video(1)
        edit.click(L.edit.menu.delete)
        edit.swipe_element(L.edit.timeline.clip,"right",600)
        
        ## 16:9 - Hide notification in settings
        _start('84c1df5a-ab02-44e9-9b71-908e18001c0f')
        edit.click(L.edit.menu.timeline_setting)
        edit.click(L.edit.sub_menu.settings)
        result_not_found = not edit.search_text("Notification")
        _end('84c1df5a-ab02-44e9-9b71-908e18001c0f',result_not_found)
        
        ## version in about page
        _start('62d48d38-c1f2-47c8-9a62-5d5d3d2d3449')
        edit.search_text("About PowerDirector")
        edit.click(L.edit.settings.about_btn)
        result_version = edit.el(L.edit.settings.about.version).text >= "6.3.0"
        _end('62d48d38-c1f2-47c8-9a62-5d5d3d2d3449',result_version)
        edit.back()
        edit.back()
        # edit.back() # un-selecte clip

        ## block  3nd pip video track
        _start('63a59ae6-026a-4e2b-9ac6-cccbbecfed8f')
        _start('6f31384c-d256-4995-b11a-05bd98f8cfb1')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.video)
        import_media.select_media_by_text("00PDRa_Testing_Material")
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        #import_media.select_media_by_text("mp4.mp4")
        import_media.select_media_by_order(1)
        import_media.click(L.import_media.library_listview.add)
        result_maximum = import_media.is_exist(L.edit.timeline.exceed_max_video)
        _end('63a59ae6-026a-4e2b-9ac6-cccbbecfed8f',result_maximum)
        _end('6f31384c-d256-4995-b11a-05bd98f8cfb1',result_maximum)
        import_media.click(L.edit.timeline.exceed_max_video)    # close dialog
        time.sleep(1)
        import_media.back()     # exit 00PDRa_Testing_Material
        time.sleep(1)
        import_media.back()     # exit import_media

        ## Block Fx pack
        _start('01bc40eb-0354-4ef2-8d01-1487d5be9960')
        edit.timeline_select_item_by_index_on_track(2, 1)
        #edit.click(L.edit.menu.fx)
        edit.select_from_bottom_edit_menu('Effect')
        result_subscription , _ = import_media.download_media("Glitch Pack Vol. 1")
        _end('01bc40eb-0354-4ef2-8d01-1487d5be9960',not result_subscription)
        import_media.back() # exit import media page
        
        ## Block Title pack (Get more)  
        _start('9069d1b1-97b6-4d09-9dfa-b37b252fe7d8')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.title)
        result_subscription , _ = import_media.download_media("Fly Pack Vol. 1")
        _end('9069d1b1-97b6-4d09-9dfa-b37b252fe7d8',not result_subscription)
        import_media.back() # exit import media page
        
        ## Block Sticker pack (Get more)    
        _start('864353ee-0a2b-4a06-9775-add61cae9a73')
        edit.click(L.edit.menu.effect)
        edit.click(L.edit.effect_sub.sticker)
        result_subscription , _ = import_media.download_media("Decorative Vines Vol.2")
        _end('864353ee-0a2b-4a06-9775-add61cae9a73',not result_subscription)
        import_media.back() # exit import media page
        
        ## Block Color pack (Get more)    
        _start('fbd69544-9bbb-40e5-8ace-e71fae9e3335')
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        result_subscription , _ = edit.download_media("Aurora")
        _end('fbd69544-9bbb-40e5-8ace-e71fae9e3335',not result_subscription)
        time.sleep(1)
        import_media.back() # unselect clip
        
        ## Block some Music/ Sound Clip 
        _start('cd4d5294-28dd-4ade-9b21-eea4d5fb7f10')
        edit.click(L.edit.menu.import_media)
        edit.click(L.import_media.menu.music_library)
        result_subscription , _ = import_media.download_media("Classical","Acceptance")
        _end('cd4d5294-28dd-4ade-9b21-eea4d5fb7f10',not result_subscription)
        import_media.back() # exit music page
        import_media.back() # exit import_media page
        time.sleep(1)
        edit.click(L.edit.menu.undo)    # didn't apply color setting, but undo button is enabled. bug:
        time.sleep(1)
        edit.click(L.edit.menu.undo)    # remove 2nd pip
        time.sleep(1)
        edit.click(L.edit.menu.undo)    # remove 1st pip
        
        ## enable 4k/fhd video (Get more)    
        _start('0a9c50ac-7b44-43d7-b610-9796b4bee367')
        edit.click(L.edit.menu.produce)
        edit.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.gallery)
        produce.click(L.produce.gallery.full_hd)
        result_no_ad = not produce.ad.get_ad_type()
        _end('0a9c50ac-7b44-43d7-b610-9796b4bee367',result_no_ad)
        
        _start('73906cd8-c93d-4e86-a62e-43d0f967179f')
        produce.click(L.produce.gallery.sd)
        time.sleep(1.5)
        produce.click(L.produce.gallery.next)
        result_no_watermark = produce.ground_truth_video('video_no_watermark.mp4')
        _end('73906cd8-c93d-4e86-a62e-43d0f967179f',result_no_watermark)

class Test_sce_06_04_01:    # [4. Output]  + subscribe account 
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        self.report = report
        # ---- local mode > end ----
        self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                              desired_caps)
        self.report.set_driver(self.driver)
        self.driver.start_app(PACKAGE_NAME)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.produce = PageFactory().get_page_object("produce", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)
        self.settings = PageFactory().get_page_object("timeline_settings", self.driver)

        self.main_page.clean_movie_cache()
        self.main_page.project_reload('16_9')
        self.main_page.copy_produced_video()
        ## subscribe now
        self.main_page.subscribe()
        
        self.driver.implicit_wait(5)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()
        
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_04_01(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        
        _start('651da968-9f43-480a-a8e1-824b87a4e8f1')
        main.project_reload("2-6_adjust_speed")
        result_project_with_settings =  main.project_select_with_correct_setting("2-6_adjust_speed","00:00:10")
        _end('651da968-9f43-480a-a8e1-824b87a4e8f1',result_project_with_settings)
        
        
        # defaut should be 4k
        _start('82b77a0d-25a8-4f23-8d55-e4d4ba0c6c20')
        _start('74f9f9c0-8fa5-4e99-af3b-6425b5a526bd')
        _start('d0727c7e-71f9-4560-b646-143b96b43b8b')
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.gallery)
        result_default_4k = bool (produce.el(L.produce.gallery.ultra_hd).get_attribute('checked'))
        _end('82b77a0d-25a8-4f23-8d55-e4d4ba0c6c20',result_default_4k)
        _end('74f9f9c0-8fa5-4e99-af3b-6425b5a526bd',result_default_4k)
        _end('d0727c7e-71f9-4560-b646-143b96b43b8b',result_default_4k)
        
        # 4k + better quality + 60 fps
        _start('6c5cd91c-6d7c-43e1-9b56-e508f3fbe754')
        produce.click(L.produce.gallery.preference)
        produce.preference.set_bitrate(BETTER_QUALITY)
        produce.preference.set_framerate(FPS_60)
        produce.click(L.produce.gallery.setting_page.ok)
        produce.click(L.produce.gallery.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        produce.ad.close_full_page_ad()
        result_4k_better_60fps = produce.close_produce_page()
        _end('6c5cd91c-6d7c-43e1-9b56-e508f3fbe754',result_4k_better_60fps)
        
        # BETTER_QUALITY + FPS_30
        _start('c7bb9a56-1199-43c7-a943-caa469305ab9')
        produce.click(L.produce.tab.gallery)
        produce.set_resolution(FULL_HD)
        produce.click(L.produce.gallery.preference)
        produce.preference.set_bitrate(STANDARD)
        produce.preference.set_framerate(FPS_30)
        produce.click(L.produce.gallery.setting_page.ok)
        produce.click(L.produce.gallery.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        produce.ad.close_full_page_ad()
        result_fhd_standard_30fps = produce.close_produce_page()
        _end('c7bb9a56-1199-43c7-a943-caa469305ab9',result_fhd_standard_30fps)
        
        # SD + STANDARD + FPS_60
        _start('01997dc0-1873-4f78-8af0-9702cbe17bad')
        produce.click(L.produce.tab.gallery)
        produce.set_resolution(HD)
        produce.click(L.produce.gallery.preference)
        produce.preference.set_bitrate(SMALLER_SIZE)
        produce.preference.set_framerate(FPS_24)
        produce.click(L.produce.gallery.setting_page.ok)
        produce.click(L.produce.gallery.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        produce.ad.close_full_page_ad()
        
        _start('505fd59a-8537-4f9b-a9fb-6b6a576b9109') # adjust speed
        _start('6941c056-4fc4-4d49-8877-0def9dd1ec79') # no watermark
        _start('4d72ffb1-e301-47f9-ab10-8ccb1ee97bb5') # quality
        _start('c7314948-e8c9-4dfc-8417-b6c41b3862ef') # aspect ratio
        result = produce.ground_truth_video('video_adjust_speed_HD_720p_16_9.mp4')
        _end('505fd59a-8537-4f9b-a9fb-6b6a576b9109',result)
        _end('6941c056-4fc4-4d49-8877-0def9dd1ec79',result)
        _end('4d72ffb1-e301-47f9-ab10-8ccb1ee97bb5',result)
        _end('c7314948-e8c9-4dfc-8417-b6c41b3862ef',result)
        
        result_hd_smaller_24fps = produce.close_produce_page()
        _end('01997dc0-1873-4f78-8af0-9702cbe17bad',result_hd_smaller_24fps)
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_04_02(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        
        _start('f1fb3066-9075-4ba1-9485-8868b0c87669')
        main.project_reload("3-6_adjust_speed")
        result_project_with_settings =  main.project_select_with_correct_setting("3-6_adjust_speed","00:00:10")
        _end('f1fb3066-9075-4ba1-9485-8868b0c87669',result_project_with_settings)
        
        
        # defaut should be 4k
        _start('8c73f790-7643-4622-8a8e-c9f686f6e3d2')
        _start('e624d44e-8994-40b4-a693-7a8991d448fb')
        _start('4ffa2221-8476-4d1d-84ce-6fc62182270d')
        produce.click(L.edit.menu.produce)
        produce.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.youtube)
        result_default_4k = bool (produce.el(L.produce.youtube.ultra_hd).get_attribute('checked'))
        _end('8c73f790-7643-4622-8a8e-c9f686f6e3d2',result_default_4k)
        _end('e624d44e-8994-40b4-a693-7a8991d448fb',result_default_4k)
        _end('4ffa2221-8476-4d1d-84ce-6fc62182270d',result_default_4k)
        
        # 4k + better quality + 60 fps
        _start('26939d03-5b04-4511-aab7-f9b886ffa348')
        produce.click(L.produce.youtube.preference)
        produce.preference.set_bitrate(SMALLER_SIZE)
        produce.preference.set_framerate(FPS_60)
        produce.click(L.produce.youtube.setting_page.ok)
        produce.click(L.produce.youtube.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        produce.ad.close_full_page_ad()
        result_4k_better_60fps = produce.close_produce_page()
        _end('26939d03-5b04-4511-aab7-f9b886ffa348',result_4k_better_60fps)
        
        # BETTER_QUALITY + FPS_30
        _start('c15d5f51-c6e2-4364-9d0e-88d5a4d6c6fa')
        produce.click(L.produce.tab.youtube)
        produce.set_resolution(HD)
        produce.click(L.produce.youtube.preference)
        produce.preference.set_bitrate(BETTER_QUALITY)
        produce.preference.set_framerate(FPS_30)
        produce.click(L.produce.youtube.setting_page.ok)
        produce.click(L.produce.youtube.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        produce.ad.close_full_page_ad()
        result_fhd_standard_30fps = produce.close_produce_page()
        _end('c15d5f51-c6e2-4364-9d0e-88d5a4d6c6fa',result_fhd_standard_30fps)
        
        # SD + STANDARD + FPS_60
        _start('5a3a3de6-a799-4d37-8f43-50b899474b5c')
        produce.click(L.produce.tab.youtube)
        produce.set_resolution(SD)
        produce.click(L.produce.youtube.preference)
        produce.preference.set_bitrate(SMALLER_SIZE)
        produce.preference.set_framerate(FPS_24)
        produce.click(L.produce.youtube.setting_page.ok)
        produce.click(L.produce.youtube.next)
        produce.exist_click(L.main.subscribe.back_btn,3)
        produce.ad.close_full_page_ad()
        
        _start('afa22cd1-3df7-4020-98f5-feeed6c0f40f') # adjust speed
        _start('3d11288b-40c5-4822-9e49-594c11c5daf6') # no watermark
        _start('89438aff-2d28-4965-980c-384768431ea2') # quality
        _start('1e5ea937-a5d9-411e-9f8d-d2f803a56edf') # aspect ratio
        result = produce.ground_truth_video('video_adjust_speed_HD_720p_9_16.mp4')
        _end('afa22cd1-3df7-4020-98f5-feeed6c0f40f',result)
        _end('3d11288b-40c5-4822-9e49-594c11c5daf6',result)
        _end('89438aff-2d28-4965-980c-384768431ea2',result)
        _end('1e5ea937-a5d9-411e-9f8d-d2f803a56edf',result)
        
        result_hd_smaller_24fps = produce.close_produce_page()
        _end('5a3a3de6-a799-4d37-8f43-50b899474b5c',result_hd_smaller_24fps)
'''
        _start('')
        
        _end('',result)
'''