import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME

from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))


pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_SFT_Scenario_01_05:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
        logger("[Start] Init driver session")

        self.driver = driver
        

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        
        driver.driver.launch_app()
        yield
        driver.driver.close_app()

    def sce_1_5_1(self):
        uuid = '45479986-4700-48e9-af00-d889b3ec09e0'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(skip_media=False)
        self.click(L.import_media.media_library.btn_preview())
        self.page_media.waiting_loading()

        if self.is_exist(L.import_media.media_library.video.display_preview):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "display_preview" is not exist'

        self.driver.driver.back()

        
        return "PASS" if result else "FAIL"

    def sce_1_5_2(self):
        uuid = '2cce56be-b6a5-4655-9c3e-a022085ebdfe'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.long_press(L.import_media.media_library.media())
        self.page_media.waiting_loading()

        if self.is_exist(L.import_media.media_library.video.display_preview):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "display_preview" is not exist'

        self.driver.driver.back()

        
        return "PASS" if result else "FAIL"

    def sce_1_5_3(self):
        uuid = '6821d9a8-3839-4921-8323-5ee9b8c6c4a8'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.report.new_result(uuid, None, 'N/A', 'Stock is removed')
        return 'N/A'

        # try:
        #     if not self.page_media.select_video_library("shutterstock"):
        #         
        #         return "PASS"
        #     else:
        #         fail_log = f'[Fail] shutterstock is exist'
        #         
        #         raise Exception(fail_log)
        #
        # except Exception as err:
        #     logger(f'\n{err}')
        #
        #     self.driver.driver.close_app()
        #     self.driver.driver.launch_app()
        #     self.page_main.enter_launcher()
        #     self.page_main.enter_timeline(skip_media=False)
        #
        #     return "FAIL"

    def sce_1_5_4(self):
        uuid = '5e99435d-14bd-484e-8384-ba2bf5276c94'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.report.new_result(uuid, None, 'N/A', 'Stock is removed')
        return 'N/A'

    def sce_1_5_5(self):
        uuid = '9b1af418-19cd-4ae0-81c6-a40da8c8ec84'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.page_media.select_video_library("getty")
        self.click(L.import_media.media_library.btn_preview())
        self.page_media.waiting_loading()

        if self.is_exist(L.import_media.media_library.video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        
        return "PASS" if result else "FAIL"

    def sce_1_5_6(self):
        uuid = '8335bee7-4b82-44b5-8682-4a7077d35495'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.page_media.select_video_library("getty")
        self.long_press(L.import_media.media_library.media())
        self.page_media.waiting_loading()

        if self.is_exist(L.import_media.media_library.video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        
        return "PASS" if result else "FAIL"

    def sce_1_5_7(self):
        uuid = 'f143d1a6-7761-478a-96f7-842b9cb01254'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_media.select_video_library("getty_pro"):
                
                return "PASS"
            else:
                fail_log = f'[Fail] getty_pro is exist'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"


    def sce_1_5_8(self):
        uuid = '78f56ea6-74f9-4833-b9ec-e76ea0a61bfb'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.report.new_result(uuid, None, 'N/A', 'Stock is removed')
        return 'N/A'

    def sce_1_5_9(self):
        uuid = '6014c97f-91d4-42ff-af47-119a13ee90a5'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        try:
            if not self.page_media.select_video_library("giphy"):
                raise Exception('Enter Giphy stock fail')

            if not self.is_exist(L.import_media.media_library.btn_preview()):
                
                return "PASS"
            else:
                fail_log = '[Fail] id "videoDisplay" is exist'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"


    def sce_1_5_10(self):
        uuid = '74e2d6cf-28d2-4c0f-9d2c-74183ca10472'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        try:
            if not self.page_media.select_video_library("giphy"):
                raise Exception('Enter Giphy stock fail')
            self.long_press(L.import_media.media_library.media())

            if not self.is_exist(id("videoDisplay")):
                
                return "PASS"
            else:
                fail_log = '[Fail] id "videoDisplay" is not exist'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_5_11(self):
        uuid = 'f44f57f1-ca9f-4d4c-b359-ae7446bcb1f8'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.page_media.select_video_library("pexels")
        self.click(L.import_media.media_library.btn_preview())
        self.page_media.waiting_loading()

        if self.is_exist(id("videoDisplay")):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        
        return "PASS" if result else "FAIL"

    def sce_1_5_12(self):
        uuid = 'f953d5d4-fd9b-4dd3-9014-c9896e356d63'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.page_media.select_video_library("pexels")
        self.long_press(L.import_media.media_library.media())
        self.page_media.waiting_loading()

        if self.is_exist(id("videoDisplay")):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        
        return "PASS" if result else "FAIL"

    def sce_1_5_13(self):
        uuid = 'f84c3132-2e68-49c5-bd1a-1d25ad3f6289'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.click(L.import_media.media_library.creator_page)

        if self.is_exist(find_string("pexels.com/@")):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Cannot find "pexels.com/@"'

        
        return "PASS" if result else "FAIL"

    def sce_1_5_14(self):
        uuid = '87def98e-a0df-4769-a56c-dc1c90c68bc7'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.page_media.select_video_library("pixabay")
        self.click(L.import_media.media_library.btn_preview())
        self.page_media.waiting_loading()

        if self.is_exist(L.import_media.media_library.video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        
        return "PASS" if result else "FAIL"

    def sce_1_5_15(self):
        uuid = '481cecde-a89e-466f-978b-72552512d9fd'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        

        self.page_media.select_video_library("pixabay")
        self.long_press(L.import_media.media_library.media())
        self.page_media.waiting_loading()

        if self.is_exist(L.import_media.media_library.video.display_preview):
            self.driver.driver.back()
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] id "videoDisplay" is not exist'

        
        return "PASS" if result else "FAIL"

    def test_case(self):
        result = {"sce_1_5_1": self.sce_1_5_1(),
                  "sce_1_5_2": self.sce_1_5_2(),
                  "sce_1_5_3": self.sce_1_5_3(),
                  "sce_1_5_4": self.sce_1_5_4(),
                  "sce_1_5_5": self.sce_1_5_5(),
                  "sce_1_5_6": self.sce_1_5_6(),
                  "sce_1_5_7": self.sce_1_5_7(),
                  "sce_1_5_8": self.sce_1_5_8(),
                  "sce_1_5_9": self.sce_1_5_9(),
                  "sce_1_5_10": self.sce_1_5_10(),
                  "sce_1_5_11": self.sce_1_5_11(),
                  "sce_1_5_12": self.sce_1_5_12(),
                  "sce_1_5_13": self.sce_1_5_13(),
                  "sce_1_5_14": self.sce_1_5_14(),
                  "sce_1_5_15": self.sce_1_5_15(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
