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

pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER


class Test_sce_05_01_01:
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
        self.driver.start_app(pdr_package)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.effect_page = PageFactory().get_page_object("effect", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)

        self.driver.implicit_wait(5)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_05_01_01(self):
        main = self.main_page
        import_media = self.import_media
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        
        

        _start('9b07c5c9-10f9-4af7-b23f-76292765351e')
        _start('96ef617c-4ff3-4b90-9d14-58e98f595524')
        main.new_launcher_enter_tutorials()
        time.sleep(10)
        result = main.click_tutorials("Adjust Video Speed")
        _end("9b07c5c9-10f9-4af7-b23f-76292765351e", result[0])
        _end("96ef617c-4ff3-4b90-9d14-58e98f595524", result[1])
        '''
        _start('1a34fe3f-ea2e-4203-a61f-8af323da0f2b')
        _start('07777aa5-cb37-4d96-9d6b-078075e69030')
        result = main.click_tutorials("Stabilize Video")
        _end("1a34fe3f-ea2e-4203-a61f-8af323da0f2b", result[0])
        _end("07777aa5-cb37-4d96-9d6b-078075e69030", result[1])
        '''
        
        _start('62961617-cb3e-46f0-ae8f-c880e7f2502c')
        _start('312e5b73-32c0-46b8-9f10-b032ae4fbc71')
        result = main.click_tutorials("Apply Chroma Key")
        _end("62961617-cb3e-46f0-ae8f-c880e7f2502c", result[0])
        _end("312e5b73-32c0-46b8-9f10-b032ae4fbc71", result[1])
        
        _start('915fa6c6-ddd4-46fb-a1e8-41c7ce2cfff8')
        _start('ea4b7a67-a36b-4d07-aac8-9ca499938378')
        result = main.click_tutorials("Extract Audio from Video")
        _end("915fa6c6-ddd4-46fb-a1e8-41c7ce2cfff8", result[0])
        _end("ea4b7a67-a36b-4d07-aac8-9ca499938378", result[1])
        
        _start('170599e4-2431-4960-b65e-f9aef05c0cf8')
        _start('58cb54a4-8a44-45d5-850e-08c84ccceeb7')
        result = main.click_tutorials("Pan & Zoom (Ken Burns) Effect")
        _end("170599e4-2431-4960-b65e-f9aef05c0cf8", result[0])
        _end("58cb54a4-8a44-45d5-850e-08c84ccceeb7", result[1])    
        
        _start('15b1fe1a-5383-4726-b5e8-b86b28a4a608')
        _start('053cb305-6594-4105-8a7b-627fe79bbc67')
        result = main.click_tutorials("Trim & Split")
        _end("15b1fe1a-5383-4726-b5e8-b86b28a4a608", result[0])
        _end("053cb305-6594-4105-8a7b-627fe79bbc67", result[1])   
        
        _start('1061d3a1-6300-4417-a607-58008bdc8477')
        _start('2202ad0b-9561-417d-a49c-3af735e2779e')
        result = main.click_tutorials("Produce Video")
        _end("1061d3a1-6300-4417-a607-58008bdc8477", result[0])
        _end("2202ad0b-9561-417d-a49c-3af735e2779e", result[1])
        
        _start('d7639a0a-e301-44db-a1d7-485f0b3425f9')
        _start('7de4c8d6-4c65-4213-93f0-4611de732a34')
        result = main.click_tutorials("Add & Edit a Title")
        _end("d7639a0a-e301-44db-a1d7-485f0b3425f9", result[0])
        _end("7de4c8d6-4c65-4213-93f0-4611de732a34", result[1])
        '''
        _start('e1ebc171-af2e-4bbd-9194-e5e9a990350d')
        _start('8ea668d1-73a2-4975-b555-3f407fea379d')
        result = main.click_tutorials("Create Intro")
        _end("e1ebc171-af2e-4bbd-9194-e5e9a990350d", result[0])
        _end("8ea668d1-73a2-4975-b555-3f407fea379d", result[1])
        '''
        _start('4b09a24f-e5db-422d-ba5b-ac860ff55257')
        _start('e6044d47-503a-49d6-9046-13e29c32c77a')
        result = main.click_tutorials("Download Music")
        _end("4b09a24f-e5db-422d-ba5b-ac860ff55257", result[0])
        _end("e6044d47-503a-49d6-9046-13e29c32c77a", result[1])
        '''
        _start('41e09f89-6707-4d68-8e8a-00ef6a7329cb')
        _start('92d363d0-c8df-4cbc-85af-f9ab145aad5e')
        result = main.click_tutorials("Create Family Video")
        _end("41e09f89-6707-4d68-8e8a-00ef6a7329cb", result[0])
        _end("92d363d0-c8df-4cbc-85af-f9ab145aad5e", result[1])
        '''
        _start('f7ea40af-fac8-473d-ace8-30d5b77fbc5b')
        _start('fd9e5a10-18c9-4bfc-8b6b-5527061d4e80')
        result = main.click_tutorials("Record a Voice-over")
        _end("f7ea40af-fac8-473d-ace8-30d5b77fbc5b", result[0])
        _end("fd9e5a10-18c9-4bfc-8b6b-5527061d4e80", result[1])
        '''
        _start('601058bb-f257-45a1-ac98-4f6bd2b1ad04')
        _start('35361159-cce4-4915-9009-2b221f7a2eef')
        result = main.click_tutorials("Add Custom Font")
        _end("601058bb-f257-45a1-ac98-4f6bd2b1ad04", result[0])
        _end("35361159-cce4-4915-9009-2b221f7a2eef", result[1])
        '''
        '''
        _start('8160f133-eeab-42fb-81f3-83512ea7b21e')
        _start('2ee82f19-0681-4217-ad15-75550ad5dfae')
        result = main.click_tutorials("Adjust Video Effects")
        _end("8160f133-eeab-42fb-81f3-83512ea7b21e", result[0])
        _end("2ee82f19-0681-4217-ad15-75550ad5dfae", result[1])
        '''

        '''
        _start('54912f40-2114-48f5-b1f2-41f7bd7c7ac5')
        _start('53234dd1-0d9b-417e-91fe-06263e720224')
        result = main.click_tutorials("Create & Manage Projects")
        _end("54912f40-2114-48f5-b1f2-41f7bd7c7ac5", result[0])
        _end("53234dd1-0d9b-417e-91fe-06263e720224", result[1])
        '''
        '''
        _start('b4f7944c-b080-457f-853e-2a1775c49ead')
        _start('b6dd22b5-c057-4ebf-a3c9-5472b58f70df')
        result = main.click_tutorials("Add a PiP Video")
        _end("b4f7944c-b080-457f-853e-2a1775c49ead", result[0])
        _end("b6dd22b5-c057-4ebf-a3c9-5472b58f70df", result[1])
        '''
        '''
        _start('38b3d6bf-8005-47f7-be41-b5d48f119517')
        _start('47daa03a-255c-4aae-a8e0-c22ba06c8e30')
        result = main.click_tutorials("Export to CyberLink Cloud")
        _end("38b3d6bf-8005-47f7-be41-b5d48f119517", result[0])
        _end("47daa03a-255c-4aae-a8e0-c22ba06c8e30", result[1])
        '''

        
        _start('6e5eb738-274d-4577-b964-ac6023c4ea02')
        main.back()
        time.sleep(3)
        main.new_launcher_enter_tutorials()
        #main.click(L.main.project.tutorials)
        time.sleep(2)
        result = main.click_tutorials("Frequently asked questions")
        time.sleep(3)
        _end("6e5eb738-274d-4577-b964-ac6023c4ea02", result)

