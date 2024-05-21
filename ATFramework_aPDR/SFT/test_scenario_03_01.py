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


from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER


pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER


class Test_sce_03_01_01:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        
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
        self.udid = DRIVER_DESIRED_CAPS['udid']
        self.driver.start_app(pdr_package)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.effect_page = PageFactory().get_page_object("effect", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)
        
        self.main_page.clean_projects()
        self.driver.implicit_wait(5)
        yield self.driver  # keep driver for the function which uses 'initial'
        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    
    # @pytest.mark.skip
    
    def test_sce_03_01_01(self):
        main = self.main_page
        import_media = self.import_media
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        # Initi #
        main.project_create_new("9:16")
        
        ## Video ##
        logger ("[V]split")
        _start("881ea315-b291-47fd-bb64-544ff525f18b")
        result = main.is_exist(L.edit.timeline.clip)
        _end("881ea315-b291-47fd-bb64-544ff525f18b", result)
        
        _start("2df42426-ab9e-4db0-9670-b47c8e2ecbdd")
        edit.click(L.edit.timeline.clip)
        edit.swipe_element(L.edit.timeline.clip,"left",300)
        result = edit.is_exist_in_bottom_edit_menu('Split')
        _end("2df42426-ab9e-4db0-9670-b47c8e2ecbdd",result)
        
        _start("693d53bb-0bf8-49d6-bcc3-81266846b13b")
        _start("4a006433-b984-40f5-b83f-16bdde6d0a01")
        is_split_success , is_thumbnail_change = edit.split_clip(L.edit.timeline.clip)
        _end("693d53bb-0bf8-49d6-bcc3-81266846b13b", is_split_success)
        _end("4a006433-b984-40f5-b83f-16bdde6d0a01", is_thumbnail_change)
        
        logger("[V]Rotate")
        _start("201a6950-d48c-4200-a089-b00a5860795c")
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #result = edit.is_exist(L.edit.edit_sub.rotate)
        result = edit.is_exist_in_bottom_edit_menu('Rotate')
        _end("201a6950-d48c-4200-a089-b00a5860795c", result)
        
        _start("757058e8-9ba3-4807-92d1-2bb11f51fd57")
        _start("59224f60-cb6c-4c42-b0c7-be04c3948ffe")
        result = edit.click_rotate()
        _end("757058e8-9ba3-4807-92d1-2bb11f51fd57", result)
        _end("59224f60-cb6c-4c42-b0c7-be04c3948ffe", result)
        
        logger("[V]Trim")
        _start("011671c4-3915-4cad-b9e7-e308f76b29d0")
        _start("b7c02a4f-13d2-4146-bc69-ad96d10f7041")
        result_trim , result_thumbnail = edit.trim_video(L.edit.timeline.clip)
        _end("011671c4-3915-4cad-b9e7-e308f76b29d0", result_trim)
        _end("b7c02a4f-13d2-4146-bc69-ad96d10f7041", result_thumbnail)
        
        _start("f1aa80c9-529a-4c36-a62b-9d49efda5874")
        result = edit.check_timeline_gap()
        _end("f1aa80c9-529a-4c36-a62b-9d49efda5874", result)

        logger("[V]Flip")
        _start("8593c8cd-2ba9-4544-9104-fc457d5c1a9a")
        # edit.click(L.edit.menu.edit)
        #result = edit.is_exist(L.edit.edit_sub.flip)
        result = edit.is_exist_in_bottom_edit_menu('Flip')
        _end("8593c8cd-2ba9-4544-9104-fc457d5c1a9a", result)
        
        _start("d15c12c2-0f5a-49b9-a33e-95087888f406")
        _start("3c13086a-fff8-4d16-969b-9d6ce8f98d63")
        result = edit.click_flip()
        _end("d15c12c2-0f5a-49b9-a33e-95087888f406", result)
        _end("3c13086a-fff8-4d16-969b-9d6ce8f98d63", result)

        logger("[V]Crop")
        _start("c689e6e9-0da9-497e-b26a-f2d1c3115c26")
        #edit.click(L.edit.menu.edit) #keep previous step
        #result = edit.is_exist(L.edit.edit_sub.crop)
        result = edit.is_exist_in_bottom_edit_menu('Crop')
        _end("c689e6e9-0da9-497e-b26a-f2d1c3115c26", result)
        
        _start("3140fc2e-722a-44c2-b9c1-08763387ce67")
        result = edit.click_crop()
        _end("3140fc2e-722a-44c2-b9c1-08763387ce67", result)
        #edit.click(L.edit.menu.back_session)

        logger("[V]Reverse")
        _start("34019ee0-a830-495b-9174-5ceee0d3e8b5")
        #edit.click(L.edit.menu.edit)
        #result = edit.is_exist(L.edit.edit_sub.reverse)
        result = edit.is_exist_in_bottom_edit_menu('Reverse')
        _end("34019ee0-a830-495b-9174-5ceee0d3e8b5", result)
        
        #_start("fcaba53d-9a85-43b4-956b-cbfce2c14d24")
        _start("7868a9b4-fa1b-46b7-8bf1-892a4b6fb8fd")
        result_show_ad , result_remove_reverse = edit.click_reverse()
        #_end("fcaba53d-9a85-43b4-956b-cbfce2c14d24", result_show_ad)
        _end("7868a9b4-fa1b-46b7-8bf1-892a4b6fb8fd", result_remove_reverse)
        
        logger("[V]Stabilizer")
        _start("59c73546-a481-466e-be02-b5d6064342a1")
        #edit.click(L.edit.menu.edit)
        #result = edit.is_exist(L.edit.edit_sub.stabilizer)
        result = edit.is_exist_in_bottom_edit_menu('Stabilizer')
        _end("59c73546-a481-466e-be02-b5d6064342a1", result)
        
        result_default_value, result_show_ad , result_show_iap= edit.click_stabilizer()
        if  result_show_iap:
            edit.back()
            self.report.add_result('f3e4f1d5-bbd6-4ee1-94c0-ead8f26253e', None, 'remove_item',
                               'For Sub only')        
            self.report.add_result('6ddc5158-9236-4993-9d8e-2083b9c83399', None, 'remove_item',
                               'For Sub only')          
            self.report.add_result('6a7a4a9d-003c-4f62-8202-e5d0f8b4fc6d', None, 'remove_item',
                               'For Sub only')             
            self.report.add_result('710dc935-8336-4d80-851b-ebf58b5b9489', None, 'remove_item',
                               'For Sub only')             
        else:
            _start("f3e4f1d5-bbd6-4ee1-94c0-ead8f26253e9")
            _start("6ddc5158-9236-4993-9d8e-2083b9c83399")
            #result_default_value , result_show_ad = edit.click_stabilizer()
            _end("f3e4f1d5-bbd6-4ee1-94c0-ead8f26253e9", result_default_value)
            _end("6ddc5158-9236-4993-9d8e-2083b9c83399", result_show_ad)
        
            _start("6a7a4a9d-003c-4f62-8202-e5d0f8b4fc6d")
            result  = edit.set_stabilizer("0.0")
            _end("6a7a4a9d-003c-4f62-8202-e5d0f8b4fc6d", result)
        
            _start("710dc935-8336-4d80-851b-ebf58b5b9489")
            result  = edit.set_stabilizer("100.0")
            _end("710dc935-8336-4d80-851b-ebf58b5b9489", result)
            edit.back()
        
    # @pytest.mark.skip
    
    def test_sce_03_01_01a(self):
        logger("test_scenario_02_01_01a")
        main = self.main_page
        import_media = self.import_media
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        # Initi #
        main.project_create_new("9:16")
        edit.swipe_element(L.edit.timeline.clip,"left",300) # prevent blank video in first few sec
        edit.click(L.edit.timeline.clip)
        
        logger("[V]Sharpness")
        _start("d6a49340-9aa3-48be-ab31-c0f449f5bdcc")
        #edit.click(L.edit.menu.edit)
        result_default_value = edit.click_sharpness()
        _end("d6a49340-9aa3-48be-ab31-c0f449f5bdcc", result_default_value)
        
        _start("aafee45f-1038-4ed8-baf2-48d8a659058a")
        #result_preview = edit.set_sharpness("200.0")
        result_preview = edit.set_sharpness(1)
        _end("aafee45f-1038-4ed8-baf2-48d8a659058a", result_preview)
        edit.back()
        
        logger("[V]Color_Preset")
        _start("75dd89e1-d3c4-4aa7-bdce-1e36f9b35913")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        result = edit.select_preset()
        _end("75dd89e1-d3c4-4aa7-bdce-1e36f9b35913", result)
        self.driver.driver.back()
        
        logger("[V]Color_Adjust")
        _start("f435b506-3f57-4da6-88f4-5be3d0e7d5c3")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        #edit.click(L.edit.color_sub.adjust)
        edit.select_from_bottom_edit_menu('Adjustment')
        logger("[V]Color_Adjust_brightness")
        edit.select_adjustment_from_bottom_edit_menu('Brightness')
        result = edit.color.adjust.brightness.is_number(0)
        _end("f435b506-3f57-4da6-88f4-5be3d0e7d5c3", result)
        
        _start("8ed63a6a-1b99-47e3-8903-6afeedc210f2")
        #edit.color.adjust.brightness.set_number(-200)
        edit.color.adjust.brightness.set_progress(0)
        result = edit.color.adjust.brightness.is_number(-100)
        _end("8ed63a6a-1b99-47e3-8903-6afeedc210f2", result)
        
        _start("f70f6c8a-6f97-4ca5-9a30-d855c01e1ed6")
        #edit.color.adjust.brightness.set_number(200)
        edit.color.adjust.brightness.set_progress(1)
        result = edit.color.adjust.brightness.is_number(100)
        _end("f70f6c8a-6f97-4ca5-9a30-d855c01e1ed6", result)
        
        _start("790feace-4dd1-4341-8b4e-1f821eeecc79")
        edit.color.adjust.brightness.set_progress(0.3)
        result = edit.color.adjust.brightness.is_progress(0.3)
        _end("790feace-4dd1-4341-8b4e-1f821eeecc79", result)
        
        _start("863dacc8-c1c4-4760-a148-92815bb3b468")
        edit.color.adjust.brightness.set_progress(0.9)
        result = edit.color.adjust.brightness.is_progress(0.9)
        _end("863dacc8-c1c4-4760-a148-92815bb3b468", result)
        
        logger("[V]Color_Adjust_contrast")
        _start("6267f08b-fe7b-4021-93c2-ac07b34776f7")
        edit.select_adjustment_from_bottom_edit_menu('Contrast')
        result = edit.color.adjust.contrast.is_number(0)
        _end("6267f08b-fe7b-4021-93c2-ac07b34776f7", result)
        
        _start("8bd3e74f-efa8-4a8a-ad9c-8a8d4f478fda")
        #edit.color.adjust.contrast.set_number(-200)
        edit.color.adjust.contrast.set_progress(0)
        result = edit.color.adjust.contrast.is_number(-100)
        _end("8bd3e74f-efa8-4a8a-ad9c-8a8d4f478fda", result)
        
        _start("7cc95326-2964-4f05-a1a6-756a6da1a2f0")
        #edit.color.adjust.contrast.set_number(200)
        edit.color.adjust.contrast.set_progress(1)
        result = edit.color.adjust.contrast.is_number(100)
        _end("7cc95326-2964-4f05-a1a6-756a6da1a2f0", result)
        
        _start("03dae198-e036-43c6-941e-098f8ed91f23")
        edit.color.adjust.contrast.set_progress(0.3)
        result = edit.color.adjust.contrast.is_progress(0.3)
        _end("03dae198-e036-43c6-941e-098f8ed91f23", result)
        
        _start("303dfbb2-13ed-41c5-863a-6baa9e672a6d")
        edit.color.adjust.contrast.set_progress(0.9)
        result = edit.color.adjust.contrast.is_progress(0.9)
        _end("303dfbb2-13ed-41c5-863a-6baa9e672a6d", result)
        
        logger("[V]Color_Adjust_saturation")
        
        _start("3f7a95a7-22b5-4008-9000-748b0310962f")
        edit.select_adjustment_from_bottom_edit_menu('Saturation')
        result = edit.color.adjust.saturation.is_number(100)
        _end("3f7a95a7-22b5-4008-9000-748b0310962f", result)
        
        _start("1994c75b-49fc-42ed-8f0c-e2bf29741aa7")
        #edit.color.adjust.saturation.set_number(-100)
        edit.color.adjust.saturation.set_progress(0)
        result = edit.color.adjust.saturation.is_number(0)
        _end("1994c75b-49fc-42ed-8f0c-e2bf29741aa7", result)
        
        _start("3d2d385e-3159-4af2-9673-c4427eee215d")
        #edit.color.adjust.saturation.set_number(300)
        edit.color.adjust.saturation.set_progress(1)
        result = edit.color.adjust.saturation.is_number(200)
        _end("3d2d385e-3159-4af2-9673-c4427eee215d", result)
        
        _start("0d9b7937-a83b-4302-8fb1-6ddb4a7fba0f")
        edit.color.adjust.saturation.set_progress(0.3)
        result = edit.color.adjust.saturation.is_progress(0.3)
        _end("0d9b7937-a83b-4302-8fb1-6ddb4a7fba0f", result)
        
        _start("cd218b0e-b32c-4738-a8d9-117cf40d3e37")
        edit.color.adjust.saturation.set_progress(0.9)
        result = edit.color.adjust.saturation.is_progress(0.9)
        _end("cd218b0e-b32c-4738-a8d9-117cf40d3e37", result)
        
        logger("[V]Color_Adjust_hue")
        _start("aabfdefe-7a41-4c13-91eb-ec0e21f3a0df")
        edit.select_adjustment_from_bottom_edit_menu('Hue')
        result = edit.color.adjust.hue.is_number(100)
        _end("aabfdefe-7a41-4c13-91eb-ec0e21f3a0df", result)
        
        _start("ed0de814-146d-431e-894d-cd5d91f9d19d")
        #edit.color.adjust.hue.set_number(-100)
        edit.color.adjust.hue.set_progress(0)
        result = edit.color.adjust.hue.is_number(0)
        _end("ed0de814-146d-431e-894d-cd5d91f9d19d", result)
        
        _start("7833e029-4e24-4b53-9501-2dd16df81536")
        #edit.color.adjust.hue.set_number(300)
        edit.color.adjust.hue.set_progress(1)
        result = edit.color.adjust.hue.is_number(200)
        _end("7833e029-4e24-4b53-9501-2dd16df81536", result)
        
        _start("26f27d64-d6a4-4bc9-82d7-bd922ca6fa27")
        edit.color.adjust.hue.set_progress(0.3)
        result = edit.color.adjust.hue.is_progress(0.3)
        _end("26f27d64-d6a4-4bc9-82d7-bd922ca6fa27", result)
        
        _start("1645f09e-b014-4143-b3b6-70840cd4156c")
        edit.color.adjust.hue.set_progress(0.9)
        result = edit.color.adjust.hue.is_progress(0.9)
        _end("1645f09e-b014-4143-b3b6-70840cd4156c", result)
        
        logger("[V]White_Balance")
        _start("1558ecd7-74c3-4c4c-92d4-a3f546493e02")
        #edit.click(L.edit.color_sub.white_balance)
        logger("[V]White_Balance_Color_Temperature")
        edit.select_adjustment_from_bottom_edit_menu('Temp')
        result = edit.color.white_balance.color_temperature.is_number(50)
        _end("1558ecd7-74c3-4c4c-92d4-a3f546493e02", result)
        
        _start("d9ccdcaf-215e-4422-8287-e84393a71374")
        #edit.color.white_balance.color_temperature.set_number(-100)
        edit.color.white_balance.color_temperature.set_progress(0)
        result = edit.color.white_balance.color_temperature.is_number(0)
        _end("d9ccdcaf-215e-4422-8287-e84393a71374", result)
        
        _start("da02ec01-bd3e-4ac0-9355-d6854edf79b1")
        #edit.color.white_balance.color_temperature.set_number(200)
        edit.color.white_balance.color_temperature.set_progress(1)
        result = edit.color.white_balance.color_temperature.is_number(100)
        _end("da02ec01-bd3e-4ac0-9355-d6854edf79b1", result)
        
        _start("9989a33d-fbde-4a23-80f4-3195b3cd9e2b")
        edit.color.white_balance.color_temperature.set_progress(0.3)
        result = edit.color.white_balance.color_temperature.is_progress(0.3)
        _end("9989a33d-fbde-4a23-80f4-3195b3cd9e2b", result)
        
        _start("cbad3c2e-4201-4fa5-9efe-acfa77e3b930")
        edit.color.white_balance.color_temperature.set_progress(0.9)
        result = edit.color.white_balance.color_temperature.is_progress(0.9)
        _end("cbad3c2e-4201-4fa5-9efe-acfa77e3b930", result)
        
        logger("[V]White_Balance_Color_tint")
        _start("dde7779a-2768-4ab2-85f6-bf324d53064c")
        edit.select_adjustment_from_bottom_edit_menu('Tint')
        result = edit.color.white_balance.tint.is_number(50)
        _end("dde7779a-2768-4ab2-85f6-bf324d53064c", result)
        
        _start("2c0b590f-301f-471b-996c-7bb6e8d36155")
        #edit.color.white_balance.tint.set_number(-100)
        edit.color.white_balance.tint.set_progress(0)
        result = edit.color.white_balance.tint.is_number(0)
        _end("2c0b590f-301f-471b-996c-7bb6e8d36155", result)
        
        _start("4582dd76-74d6-41a6-9435-3c8b21a64d96")
        #edit.color.white_balance.tint.set_number(200)
        edit.color.white_balance.tint.set_progress(1)
        result = edit.color.white_balance.tint.is_number(100)
        _end("4582dd76-74d6-41a6-9435-3c8b21a64d96", result)
        
        _start("15adc142-fc0a-414f-932e-1aa885ecf786")
        edit.color.white_balance.tint.set_progress(0.3)
        result = edit.color.white_balance.tint.is_progress(0.3)
        _end("15adc142-fc0a-414f-932e-1aa885ecf786", result)
        
        _start("fa00be60-b2ef-4ae4-9e7b-5fcc807f31ba")
        edit.color.white_balance.tint.set_progress(0.9)
        result = edit.color.white_balance.tint.is_progress(0.9)
        _end("fa00be60-b2ef-4ae4-9e7b-5fcc807f31ba", result)
        edit.back()
        
        logger("[V]Skin_smoothener")
        
        _start("afd765a2-1209-4551-a690-fc014c0b64a3")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.skin_smoothener)
        logger("[V]Skin_smoothener_Skin_Brightness")
        edit.select_from_bottom_edit_menu('Skin Smoothener')
        edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        result = edit.skin_smoothener.skin_brightness.is_number(80)
        _end("afd765a2-1209-4551-a690-fc014c0b64a3", result)
        
        _start("aee598a4-2019-42d9-af57-c0fdc95ac3e5")
        #edit.skin_smoothener.skin_brightness.set_number(0)
        edit.skin_smoothener.skin_brightness.set_progress(0)
        result = edit.skin_smoothener.skin_brightness.is_number(40)
        _end("aee598a4-2019-42d9-af57-c0fdc95ac3e5", result)
        
        _start("50392bf6-81d4-4e16-a6f6-d03d34505d90")
        #edit.skin_smoothener.skin_brightness.set_number(200)
        edit.skin_smoothener.skin_brightness.set_progress(1)
        result = edit.skin_smoothener.skin_brightness.is_number(100)
        _end("50392bf6-81d4-4e16-a6f6-d03d34505d90", result)
        
        _start("f8bb26d5-09b6-495f-a960-3ccd4ea5adb3")
        edit.skin_smoothener.skin_brightness.set_progress(0.3)
        result = edit.skin_smoothener.skin_brightness.is_progress(0.3)
        _end("f8bb26d5-09b6-495f-a960-3ccd4ea5adb3", result)
        
        _start("614aaf1a-800d-4521-b80c-58d76260a1d4")
        edit.skin_smoothener.skin_brightness.set_progress(0.9)
        result = edit.skin_smoothener.skin_brightness.is_progress(0.9)
        _end("614aaf1a-800d-4521-b80c-58d76260a1d4", result)
        
        logger("[V]Skin_smoothener_Skin_Smoothness")
        _start("eec19c97-94f5-4104-8188-8756efd7a561")
        edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        result = edit.skin_smoothener.skin_smoothness.is_number(80)
        _end("eec19c97-94f5-4104-8188-8756efd7a561", result)
        
        _start("09e860b6-9f2c-4937-9347-ac54251e941b")
        #edit.skin_smoothener.skin_smoothness.set_number(-100)
        edit.skin_smoothener.skin_smoothness.set_progress(0)
        result = edit.skin_smoothener.skin_smoothness.is_number(0)
        _end("09e860b6-9f2c-4937-9347-ac54251e941b", result)
        
        _start("61b999cb-eeee-487f-978e-0bdb95c20a9f")
        #edit.skin_smoothener.skin_smoothness.set_number(200)
        edit.skin_smoothener.skin_smoothness.set_progress(1)
        result = edit.skin_smoothener.skin_smoothness.is_number(100)
        _end("61b999cb-eeee-487f-978e-0bdb95c20a9f", result)
        
        _start("58092a32-a957-4177-ac29-38a890f957ec")
        edit.skin_smoothener.skin_smoothness.set_progress(0.3)
        result = edit.skin_smoothener.skin_smoothness.is_progress(0.3)
        _end("58092a32-a957-4177-ac29-38a890f957ec", result)
        
        _start("2d2089d3-7ac6-47c2-b280-03257ff833c6")
        edit.skin_smoothener.skin_smoothness.set_progress(0.9)
        result = edit.skin_smoothener.skin_smoothness.is_progress(0.9)
        _end("2d2089d3-7ac6-47c2-b280-03257ff833c6", result)
        edit.back()
        
        _start("31f79677-0bd2-4af0-88f4-8b5d67b131dd")
        _start("e758cdf8-6034-488b-8e14-d7f832536554")
        #result_apply_to_main_track = edit.is_exist(L.edit.timeline.skin_smoothener)
        result_apply_to_main_track = edit.is_exist_in_bottom_edit_menu('Skin Smoothener')
        _end("31f79677-0bd2-4af0-88f4-8b5d67b131dd", result_apply_to_main_track)
        _end("e758cdf8-6034-488b-8e14-d7f832536554", result_apply_to_main_track)

        logger("[V]Preview")
        _start("1870d51f-0f44-46b9-a6d3-1d988cbed60f")
        result_preview = edit.click_preview()
        _end("1870d51f-0f44-46b9-a6d3-1d988cbed60f", result_preview)
        
        _start("642408c7-5144-4ecf-89ea-7dc66fefb7b2")
        result_has_timecode = edit.is_exist(L.edit.timeline.timecode)
        _end("642408c7-5144-4ecf-89ea-7dc66fefb7b2", result_has_timecode)
        edit.el(L.edit.menu.play).click() # stop playback
        
        logger("[V]undo")
        _start("60d96a29-7a25-4875-9801-119802042811")
        edit.click(L.edit.menu.undo)
        #result_undo = edit.is_not_exist(L.edit.timeline.skin_smoothener)
        result_undo = edit.is_exist_in_bottom_edit_menu('Skin Smoothener')
        _end("60d96a29-7a25-4875-9801-119802042811", result_undo)
        
        logger("[V]Auto Save")
        _start("7052a9a2-ec48-4258-95aa-a730b8f8cb78")
        result_auto_save = edit.is_auto_save()
        _end("7052a9a2-ec48-4258-95aa-a730b8f8cb78", result_auto_save) 
      
    # @pytest.mark.skip
    
    def test_sce_03_01_02(self):
        logger("test_scenario_03_01_02")
        main = self.main_page
        import_media = self.import_media
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        # Initi #
        main.project_create_new("9:16",type="photo")
        
        ## Photo ##
        logger ("[P]split")
        _start("51372bfb-13ca-4f3f-875c-85cc58b7627b")
        edit.swipe_element(L.edit.timeline.clip_photo,"left",400)
        edit.click(L.edit.timeline.clip_photo)
        #result = edit.is_exist(L.edit.menu.split)
        result = edit.is_exist_in_bottom_edit_menu('Split')
        _end("51372bfb-13ca-4f3f-875c-85cc58b7627b",result)
        
        _start("9f32b193-edb8-45fd-ae72-86f8ba356476")
        _start("646aa117-1668-4d4d-abab-8a80ee67bc5c")
        is_split_success , is_thumbnail_change = edit.split_clip(L.edit.timeline.clip_photo)
        _end("9f32b193-edb8-45fd-ae72-86f8ba356476", is_split_success)
        _end("646aa117-1668-4d4d-abab-8a80ee67bc5c", is_thumbnail_change)
        
        logger("[P]Rotate")
        _start("31b8a9a7-57d8-4f72-b69d-892bae8472f2")
        edit.click(L.edit.timeline.clip_photo)
        #edit.click(L.edit.menu.edit)
        #result = edit.is_exist(L.edit.edit_sub.rotate)
        result = edit.is_exist_in_bottom_edit_menu('Rotate')
        _end("31b8a9a7-57d8-4f72-b69d-892bae8472f2", result)
        
        result = edit.click_rotate()
        _start("91240549-3449-45d5-8af9-69d06bb58343")
        _start("65f8f7c1-662a-4373-8462-b908de3460a3")
        _end("91240549-3449-45d5-8af9-69d06bb58343", result)
        _end("65f8f7c1-662a-4373-8462-b908de3460a3", result)
        
        logger("[P]Trim")
        _start("c0518890-8fe1-45bb-aab5-06eaeb1d9e07")
        _start("899c3300-34d7-4771-b256-c29ad769fd7a")
        result_trim , result_thumbnail = edit.trim_video(L.edit.timeline.clip_photo)
        _end("c0518890-8fe1-45bb-aab5-06eaeb1d9e07", result_trim)
        _end("899c3300-34d7-4771-b256-c29ad769fd7a", result_thumbnail)
        
        _start("ef59a1d2-c54a-4735-8efb-a1aa49b4e28a")
        result = edit.check_timeline_gap(type="Photo")
        _end("ef59a1d2-c54a-4735-8efb-a1aa49b4e28a", result)
        
        logger("[P]Flip")
        _start("2bd61098-a7e8-4fc1-a5ec-aeb3b6321455")
        # edit.click(L.edit.menu.edit)
        #result = edit.is_exist(L.edit.edit_sub.flip)
        edit.timeline_select_item_by_index_on_track(1, 2)
        edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(3)
        result = edit.is_exist_in_bottom_edit_menu('Flip')
        _end("2bd61098-a7e8-4fc1-a5ec-aeb3b6321455", result)
        
        _start("7a07b620-720f-41be-8124-6b3a5ead4fa6")
        _start("60431b61-2ab9-4cc3-a9cf-789336f8b9c4")
        result = edit.click_flip()
        _end("7a07b620-720f-41be-8124-6b3a5ead4fa6", result)
        _end("60431b61-2ab9-4cc3-a9cf-789336f8b9c4", result)
        
        logger("[P]Crop")
        _start("83e45940-99c9-4885-b8de-765c796b65eb")
        #edit.click(L.edit.menu.edit) #keep previous step
        #result = edit.is_exist(L.edit.edit_sub.crop)
        result = edit.is_exist_in_bottom_edit_menu('Crop')
        _end("83e45940-99c9-4885-b8de-765c796b65eb", result)
        
        _start("07e07185-bc5f-4711-a64a-1044fbac331b")
        result = edit.click_crop()
        _end("07e07185-bc5f-4711-a64a-1044fbac331b", result)
        #edit.click(L.edit.menu.back_session)
       
        logger("[P]Sharpness")
        _start("c087b4f1-2747-4ffb-b98d-8b6346c6b7b1")
        #edit.click(L.edit.menu.edit)
        result_default_value = edit.click_sharpness()
        _end("c087b4f1-2747-4ffb-b98d-8b6346c6b7b1", result_default_value)
        
        _start("05458250-bb73-4284-9aec-5469513a2613")
        #result_preview = edit.set_sharpness("200.0")
        result_preview = edit.set_sharpness(1)
        _end("05458250-bb73-4284-9aec-5469513a2613", result_preview)
        edit.back()
        
        logger("[P]Color_Preset")
        _start("32f18701-f3f4-4ba8-a9aa-e748f37e4161")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        result = edit.select_preset()
        _end("32f18701-f3f4-4ba8-a9aa-e748f37e4161", result)
        self.driver.driver.back()
        
        logger("[P]Skin_smoothener")
        _start("80111c4c-4c67-48ee-b654-775973d38f7f")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.skin_smoothener)
        logger("[P]Skin_smoothener_Skin_Brightness")
        edit.select_from_bottom_edit_menu('Skin Smoothener')
        logger("[P]Skin_smoothener_Skin_Brightness")
        result_default = edit.skin_smoothener.skin_brightness.is_number(80)
        _end("80111c4c-4c67-48ee-b654-775973d38f7f", result_default)
        
        _start("5b38dc29-6e43-449c-80af-72d6783befa4")
        #edit.skin_smoothener.skin_brightness.set_number(0)
        edit.skin_smoothener.skin_brightness.set_progress(0)
        result_min = edit.skin_smoothener.skin_brightness.is_number(40)
        _end("5b38dc29-6e43-449c-80af-72d6783befa4", result_min)
        
        _start("4e3a7f58-be40-4fc7-82e1-2f0c64bf09b9")
        #edit.skin_smoothener.skin_brightness.set_number(200)
        edit.skin_smoothener.skin_brightness.set_progress(1)
        result_max = edit.skin_smoothener.skin_brightness.is_number(100)
        _end("4e3a7f58-be40-4fc7-82e1-2f0c64bf09b9", result_max)
        
        _start("0e657646-fb1a-459a-82b7-aa8bf2a7b558")
        edit.skin_smoothener.skin_brightness.set_progress(0.3)
        result_decrease = edit.skin_smoothener.skin_brightness.is_progress(0.3)
        _end("0e657646-fb1a-459a-82b7-aa8bf2a7b558", result_decrease)
        
        _start("63c9e50e-25b2-4e65-a8dc-53debb15b994")
        edit.skin_smoothener.skin_brightness.set_progress(0.9)
        result_increase = edit.skin_smoothener.skin_brightness.is_progress(0.9)
        _end("63c9e50e-25b2-4e65-a8dc-53debb15b994", result_increase)
        
        logger("[P]Skin_smoothener_Skin_Smoothness")
        _start("81d2a3ff-b8ea-4e36-bb1c-61f63c6ebafc")
        edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        result_default = edit.skin_smoothener.skin_smoothness.is_number(80)
        _end("81d2a3ff-b8ea-4e36-bb1c-61f63c6ebafc", result_default)
        
        _start("7a502afa-4fa0-417a-8071-e54f88a8f407")
        #edit.skin_smoothener.skin_smoothness.set_number(-100)
        edit.skin_smoothener.skin_smoothness.set_progress(0)
        result_min = edit.skin_smoothener.skin_smoothness.is_number(0)
        _end("7a502afa-4fa0-417a-8071-e54f88a8f407", result_min)
        
        _start("c7638963-d450-48f5-8140-90ba4b74a6eb")
        #edit.skin_smoothener.skin_smoothness.set_number(200)
        edit.skin_smoothener.skin_smoothness.set_progress(1)
        result_max = edit.skin_smoothener.skin_smoothness.is_number(100)
        _end("c7638963-d450-48f5-8140-90ba4b74a6eb", result_max)
        
        _start("df389530-9faa-4f57-99b8-9d43ebb3bba7")
        edit.skin_smoothener.skin_smoothness.set_progress(0.3)
        result_decrease = edit.skin_smoothener.skin_smoothness.is_progress(0.3)
        _end("df389530-9faa-4f57-99b8-9d43ebb3bba7", result_decrease)
        
        _start("b7c2d6b5-a647-47aa-8b8c-f4ea4958096a")
        edit.skin_smoothener.skin_smoothness.set_progress(0.9)
        result_increase = edit.skin_smoothener.skin_smoothness.is_progress(0.9)
        _end("b7c2d6b5-a647-47aa-8b8c-f4ea4958096a", result_increase)
        
        edit.back()
        
        _start("661f3b4e-2325-4830-bd4d-b403d68c86bf")
        _start("8e5d6eca-c34a-47d0-aecf-365d7a3b45a3")
        #result_apply_to_main_track = edit.is_exist(L.edit.timeline.skin_smoothener)
        result_apply_to_main_track = edit.is_exist_in_bottom_edit_menu('Skin Smoothener')
        _end("661f3b4e-2325-4830-bd4d-b403d68c86bf", result_apply_to_main_track)
        _end("8e5d6eca-c34a-47d0-aecf-365d7a3b45a3", result_apply_to_main_track)
        
        _start("ac73ae48-3a3f-46f8-a96c-676c5f4d7280")
        result_watermark = edit.is_exist(L.edit.preview.watermark)
        _end("ac73ae48-3a3f-46f8-a96c-676c5f4d7280", result_watermark)

        
    # @pytest.mark.skip
    
    def test_sce_03_01_03(self):
        logger("test_scenario_02_01_03")
        main = self.main_page
        import_media = self.import_media
        edit = self.edit
        _start = self.report.start_uuid
        _end = self.report.new_result
        
        # Initi #
        main.project_create_new(type='audio')
        
        logger ("[A]split")
        _start("a0455be4-9390-48c8-8b12-10eb5e4e0cef")
        edit.force_uncheck_help_enable_tip_to_Leave()
        edit.swipe_element(L.edit.timeline.clip_audio,"left",400)
        edit.click(L.edit.timeline.clip_audio)
        #result_split = edit.is_exist(L.edit.menu.split)
        result_split = edit.is_exist_in_bottom_edit_menu('Split')
        _end("a0455be4-9390-48c8-8b12-10eb5e4e0cef",result_split)
        
        _start("062810da-eb7c-42a2-8fd8-e26b3dd63e04")
        _start("b4011393-246d-4dda-a8f9-741b471069f2")
        is_split_success , is_thumbnail_change = edit.split_music(L.edit.timeline.clip_audio)
        edit.click(L.edit.menu.delete)
        _end("062810da-eb7c-42a2-8fd8-e26b3dd63e04", is_split_success)
        _end("b4011393-246d-4dda-a8f9-741b471069f2", is_thumbnail_change) 
        
        
        logger("[A]Trim")
        _start("93298696-14aa-4d9b-b95d-7511021206c3")
        _start("3bf3600e-2e59-4b5a-b6d6-2d676093b86f")
        edit.click(L.edit.timeline.clip_audio)
        result_trim , result_thumbnail = edit.trim_video(L.edit.timeline.clip_audio)
        _end("93298696-14aa-4d9b-b95d-7511021206c3", result_trim)
        _end("3bf3600e-2e59-4b5a-b6d6-2d676093b86f", result_thumbnail)
        
        _start("eb625c3f-fbd6-4b32-b36a-df27df745874")
        result = edit.check_timeline_gap(type="Audio")
        _end("eb625c3f-fbd6-4b32-b36a-df27df745874", result)
