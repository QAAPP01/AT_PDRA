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


class Test_sce_02_01_01:
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
        self.report = report
        # ---- local mode > end ----

        # retry 3 time if craete driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                                       desired_caps)
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
        self.main_page.clean_movie_cache()
        self.driver.implicit_wait(5)
        yield self.driver  # keep driver for the function which uses 'initial'
        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_01_01(self):
        main = self.main_page
        import_media = self.import_media
        edit = self.edit

        # Initi #
        main.project_create_new()

        ## Video ##
        logger("[V]split")
        self.report.start_uuid('923cc0c9-f6d8-4f65-8076-f1b585d5b1a3')
        result = main.is_exist(L.edit.timeline.clip)
        self.report.new_result("923cc0c9-f6d8-4f65-8076-f1b585d5b1a3", result)

        self.report.start_uuid('a6faa123-8177-429b-9202-14c21e8905c0')
        edit.swipe_element(L.edit.timeline.timeline_ruler, "left", 0.5)
        edit.click(L.edit.timeline.clip)
        edit.swipe_element(L.edit.timeline.timeline_ruler, "left", 0.5)
        result = edit.is_exist_in_bottom_edit_menu('Split')
        self.report.new_result("a6faa123-8177-429b-9202-14c21e8905c0", result)

        self.report.start_uuid("8973afb2-a0de-4e47-bd0c-d670f83f3c88")
        self.report.start_uuid("09cadca9-f7cd-4d6e-a0d1-e26cce285fcf")
        is_split_success, is_thumbnail_change = edit.split_clip(L.edit.timeline.clip)
        self.report.new_result("8973afb2-a0de-4e47-bd0c-d670f83f3c88", is_split_success)
        self.report.new_result("09cadca9-f7cd-4d6e-a0d1-e26cce285fcf", is_thumbnail_change)

        logger("[V]Rotate")
        self.report.start_uuid("b3121bdd-b1f5-4532-9f6c-13237193ee4f")
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        result = edit.is_exist_in_bottom_edit_menu('Rotate')
        self.report.new_result("b3121bdd-b1f5-4532-9f6c-13237193ee4f", result)

        result = edit.click_rotate()
        self.report.start_uuid("6805d7b3-1775-4b5f-930f-159965846428")
        self.report.start_uuid("d5b79a1e-03ee-443a-8a49-d98349bba1b3")
        self.report.new_result("6805d7b3-1775-4b5f-930f-159965846428", result)
        self.report.new_result("d5b79a1e-03ee-443a-8a49-d98349bba1b3", result)

        logger("[V]Trim")
        self.report.start_uuid("394f27cb-9e6f-411b-add7-638473575131")
        self.report.start_uuid("73720235-b876-49a2-82d9-75b7e3a4d620")
        result_trim, result_thumbnail = edit.trim_video(L.edit.timeline.clip)
        self.report.new_result("394f27cb-9e6f-411b-add7-638473575131", result_trim)
        self.report.new_result("73720235-b876-49a2-82d9-75b7e3a4d620", result_thumbnail)
        
        self.report.start_uuid("ae24be03-9cad-455e-b23e-924d12984199")
        result = edit.check_timeline_gap()
        self.report.new_result("ae24be03-9cad-455e-b23e-924d12984199", result)

        logger("[V]Flip")
        # edit.click(L.edit.menu.edit)
        self.report.start_uuid("bef218e9-b099-4126-ac5b-1d5a80ed0554")
        result = edit.is_exist_in_bottom_edit_menu('Flip')
        self.report.new_result("bef218e9-b099-4126-ac5b-1d5a80ed0554", result)

        self.report.start_uuid("6be89ea0-524f-4d3f-bc99-e27c2acbe909")
        self.report.start_uuid("cac9a824-5140-47d6-ae60-d126e04becde")
        result = edit.click_flip()
        self.report.new_result("6be89ea0-524f-4d3f-bc99-e27c2acbe909", result)
        self.report.new_result("cac9a824-5140-47d6-ae60-d126e04becde", result)

        logger("[V]Crop")
        self.report.start_uuid("4a9dcf18-a3a8-414f-839f-bc4b085f79c2")
        # edit.click(L.edit.menu.edit) #keep previous step
        result = edit.is_exist_in_bottom_edit_menu('Crop')
        self.report.new_result("4a9dcf18-a3a8-414f-839f-bc4b085f79c2", result)

        result = edit.click_crop()
        self.report.start_uuid("789d8fa7-6027-47f5-a979-c165c4dc6028")
        self.report.new_result("789d8fa7-6027-47f5-a979-c165c4dc6028", result)
        #edit.click(L.edit.menu.back_session)

        logger("[V]Reverse")
        self.report.start_uuid("227a3419-90e9-465a-b230-6efe8bc640d0")
        #edit.click(L.edit.menu.edit)
        result = edit.is_exist_in_bottom_edit_menu('Reverse')
        self.report.new_result("227a3419-90e9-465a-b230-6efe8bc640d0", result)

        '''
        self.report.start_uuid("73b8a01c-23d2-498c-8d99-0d1e6fb681c3")
        self.report.start_uuid("63ef8f5b-b929-400d-b32c-69e647e9f4b6")
        edit.timeline_get_item_by_index_on_track(1, 2).click()  # select longer clip
        result_show_ad, result_remove_reverse = edit.click_reverse()
        self.report.new_result("73b8a01c-23d2-498c-8d99-0d1e6fb681c3", result_show_ad)
        self.report.new_result("63ef8f5b-b929-400d-b32c-69e647e9f4b6", result_remove_reverse)
        '''
        edit.timeline_get_item_by_index_on_track(1, 1).click()  # select original clip

        logger("[V]Stabilizer")
        self.report.start_uuid("dce25f23-067f-4a5f-8dda-692ee46fada3")
        #edit.click(L.edit.menu.edit)
        result = edit.is_exist_in_bottom_edit_menu('Stabilizer')
        self.report.new_result("dce25f23-067f-4a5f-8dda-692ee46fada3", result)

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
            self.report.start_uuid("8ce1701e-fa22-4544-a586-98eef705981d")
            self.report.start_uuid("36454a6f-1031-4372-a1fb-f2f3f79a8ce3")
            self.report.new_result("8ce1701e-fa22-4544-a586-98eef705981d", result_default_value)
            self.report.new_result("36454a6f-1031-4372-a1fb-f2f3f79a8ce3", result_show_ad)
            self.report.start_uuid("f770a0a8-68b9-4811-86c6-7131c3a732f3")
            result = edit.set_stabilizer("0.0")
            self.report.new_result("f770a0a8-68b9-4811-86c6-7131c3a732f3", result)
            self.report.start_uuid("aae26929-d157-441c-9959-cc4f3004cd7c")
            result = edit.set_stabilizer("100.0")
            self.report.new_result("aae26929-d157-441c-9959-cc4f3004cd7c", result)
            edit.back()

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_01_01a(self):
        logger("test_scenario_02_01_01a")
        self.page = self.main_page
        main = self.page
        import_media = self.import_media
        edit = self.edit

        # Initi #
        main.project_create_new()
        edit.click(L.edit.timeline.clip)

        logger("[V]Sharpness")
        self.report.start_uuid("66247e49-e3aa-4b77-929e-33b67fff2f63")
        #edit.click(L.edit.menu.edit)
        result_default_value = edit.click_sharpness()
        self.report.new_result("66247e49-e3aa-4b77-929e-33b67fff2f63", result_default_value)

        self.report.start_uuid("8ac1816f-4cf6-4c48-95b7-6f770176cf73")
        result_preview = edit.set_sharpness(1)
        self.report.new_result("8ac1816f-4cf6-4c48-95b7-6f770176cf73", result_preview)
        edit.back()

        logger("[V]Color_Preset")
        self.report.start_uuid("300efe76-5d15-4f53-821f-9d0ce6f859d2")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        result = edit.select_preset()
        self.report.new_result("300efe76-5d15-4f53-821f-9d0ce6f859d2", result)
        self.driver.driver.back()

        logger("[V]Color_Adjust")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        #edit.click(L.edit.color_sub.adjust)
        edit.select_from_bottom_edit_menu('Adjustment')

        logger("[V]Color_Adjust_brightness")
        self.report.start_uuid("4017ecaf-4099-45c4-bdff-2fb9633d42c4")
        edit.select_adjustment_from_bottom_edit_menu('Brightness')
        result = edit.color.adjust.brightness.is_number(0)
        self.report.new_result("4017ecaf-4099-45c4-bdff-2fb9633d42c4", result)

        self.report.start_uuid("56bfcf3c-ebc3-4c44-b278-2f99a5ac017e")
        edit.color.adjust.brightness.set_progress(0)
        result = edit.color.adjust.brightness.is_number(-100)
        self.report.new_result("56bfcf3c-ebc3-4c44-b278-2f99a5ac017e", result)

        self.report.start_uuid("5be6d9f5-cf81-4408-80a7-2aca089389cb")
        edit.color.adjust.brightness.set_progress(1)
        result = edit.color.adjust.brightness.is_number(100)
        self.report.new_result("5be6d9f5-cf81-4408-80a7-2aca089389cb", result)

        self.report.start_uuid("206d5ec5-53fc-439e-8277-6fc407bdd26e")
        edit.color.adjust.brightness.set_progress(0.3)
        result = edit.color.adjust.brightness.is_progress(0.3)
        self.report.new_result("206d5ec5-53fc-439e-8277-6fc407bdd26e", result)

        self.report.start_uuid("94c02d7d-3fc6-479a-969e-c9aee5cc4ca1")
        edit.color.adjust.brightness.set_progress(0.9)
        result = edit.color.adjust.brightness.is_progress(0.9)
        self.report.new_result("94c02d7d-3fc6-479a-969e-c9aee5cc4ca1", result)

        logger("[V]Color_Adjust_contrast")
        self.report.start_uuid("176f1faa-cf8d-47e7-aa9d-15f975a5abae")
        edit.select_adjustment_from_bottom_edit_menu('Contrast')
        result = edit.color.adjust.contrast.is_number(0)
        self.report.new_result("176f1faa-cf8d-47e7-aa9d-15f975a5abae", result)

        self.report.start_uuid("6e38e549-1176-4c7c-b247-dfb73b34c98e")
        edit.color.adjust.contrast.set_progress(0)
        result = edit.color.adjust.contrast.is_number(-100)
        self.report.new_result("6e38e549-1176-4c7c-b247-dfb73b34c98e", result)

        self.report.start_uuid("8ceae3f4-e25a-4420-8e9e-036efe2c32ad")
        edit.color.adjust.contrast.set_progress(1)
        result = edit.color.adjust.contrast.is_number(100)
        self.report.new_result("8ceae3f4-e25a-4420-8e9e-036efe2c32ad", result)

        self.report.start_uuid("a4434695-07e6-4013-92d3-a776e99ce42a")
        edit.color.adjust.contrast.set_progress(0.3)
        result = edit.color.adjust.contrast.is_progress(0.3)
        self.report.new_result("a4434695-07e6-4013-92d3-a776e99ce42a", result)

        self.report.start_uuid("120dc857-7115-4dff-aa89-9a4c87cac13c")
        edit.color.adjust.contrast.set_progress(0.9)
        result = edit.color.adjust.contrast.is_progress(0.9)
        self.report.new_result("120dc857-7115-4dff-aa89-9a4c87cac13c", result)

        logger("[V]Color_Adjust_saturation")
        self.report.start_uuid("563a3999-87e2-4b02-8256-ea1c0c42e6a8")
        edit.select_adjustment_from_bottom_edit_menu('Saturation')
        result = edit.color.adjust.saturation.is_number(100)
        self.report.new_result("563a3999-87e2-4b02-8256-ea1c0c42e6a8", result)

        self.report.start_uuid("4641b18f-3f95-431a-85a3-8d68bd6afc22")
        edit.color.adjust.saturation.set_progress(0)
        result = edit.color.adjust.saturation.is_number(0)
        self.report.new_result("4641b18f-3f95-431a-85a3-8d68bd6afc22", result)

        self.report.start_uuid("7156957f-4dca-496f-a4c6-65e674753603")
        edit.color.adjust.saturation.set_progress(1)
        result = edit.color.adjust.saturation.is_number(200)
        self.report.new_result("7156957f-4dca-496f-a4c6-65e674753603", result)

        self.report.start_uuid("0523771e-346a-4477-80ef-b7c2d2c4f46d")
        edit.color.adjust.saturation.set_progress(0.3)
        result = edit.color.adjust.saturation.is_progress(0.3)
        self.report.new_result("0523771e-346a-4477-80ef-b7c2d2c4f46d", result)

        self.report.start_uuid("d8fe2c0e-f903-4c34-9f3b-dc4b1165c19e")
        edit.color.adjust.saturation.set_progress(0.9)
        result = edit.color.adjust.saturation.is_progress(0.9)
        self.report.new_result("d8fe2c0e-f903-4c34-9f3b-dc4b1165c19e", result)

        logger("[V]Color_Adjust_hue")
        self.report.start_uuid("8d509724-ad94-41ba-8add-ca7a0c018aae")
        edit.select_adjustment_from_bottom_edit_menu('Hue')
        result = edit.color.adjust.hue.is_number(100)
        self.report.new_result("8d509724-ad94-41ba-8add-ca7a0c018aae", result)

        self.report.start_uuid("55d52fc1-4867-408c-aa91-0240796084f0")
        edit.color.adjust.hue.set_progress(0)
        result = edit.color.adjust.hue.is_number(0)
        self.report.new_result("55d52fc1-4867-408c-aa91-0240796084f0", result)

        self.report.start_uuid("e1e887e6-8cba-4c26-9de3-ee1ad93c0599")
        edit.color.adjust.hue.set_progress(1)
        result = edit.color.adjust.hue.is_number(200)
        self.report.new_result("e1e887e6-8cba-4c26-9de3-ee1ad93c0599", result)

        self.report.start_uuid("c7701799-6d27-4126-8ab9-f158d6ca49ac")
        edit.color.adjust.hue.set_progress(0.3)
        result = edit.color.adjust.hue.is_progress(0.3)
        self.report.new_result("c7701799-6d27-4126-8ab9-f158d6ca49ac", result)

        self.report.start_uuid("eb384538-b939-4445-b12c-4c2038c9a51d")
        edit.color.adjust.hue.set_progress(0.9)
        result = edit.color.adjust.hue.is_progress(0.9)
        self.report.new_result("eb384538-b939-4445-b12c-4c2038c9a51d", result)

        logger("[V]White_Balance")
        #edit.click(L.edit.color_sub.white_balance)
        logger("[V]White_Balance_Color_Temperature")
        self.report.start_uuid("ae478e12-9e67-42d0-9052-1cf63f3394ca")
        edit.select_adjustment_from_bottom_edit_menu('Temp')
        result = edit.color.white_balance.color_temperature.is_number(50)
        self.report.new_result("ae478e12-9e67-42d0-9052-1cf63f3394ca", result)

        self.report.start_uuid("ed5d6e4a-eeb7-47af-936f-ae7c2ff8ef95")
        edit.color.white_balance.color_temperature.set_progress(0)
        result = edit.color.white_balance.color_temperature.is_number(0)
        self.report.new_result("ed5d6e4a-eeb7-47af-936f-ae7c2ff8ef95", result)

        self.report.start_uuid("0a4208a2-2d52-4964-9df4-23c29aba3f2a")
        edit.color.white_balance.color_temperature.set_progress(1)
        result = edit.color.white_balance.color_temperature.is_number(100)
        self.report.new_result("0a4208a2-2d52-4964-9df4-23c29aba3f2a", result)

        self.report.start_uuid("c01e1811-16c2-447c-980d-cbe12e197e1c")
        edit.color.white_balance.color_temperature.set_progress(0.3)
        result = edit.color.white_balance.color_temperature.is_progress(0.3)
        self.report.new_result("c01e1811-16c2-447c-980d-cbe12e197e1c", result)

        self.report.start_uuid("cb5ef2e5-c9c4-422e-8a53-a1e0a67c717e")
        edit.color.white_balance.color_temperature.set_progress(0.9)
        result = edit.color.white_balance.color_temperature.is_progress(0.9)
        self.report.new_result("cb5ef2e5-c9c4-422e-8a53-a1e0a67c717e", result)

        logger("[V]White_Balance_Color_tint")
        self.report.start_uuid("7ef47ca5-1eaf-4202-bb35-b576ea881f21")
        edit.select_adjustment_from_bottom_edit_menu('Tint')
        result = edit.color.white_balance.tint.is_number(50)
        self.report.new_result("7ef47ca5-1eaf-4202-bb35-b576ea881f21", result)

        self.report.start_uuid("cb672a5c-543a-4d03-b81c-0a1a9f56070a")
        edit.color.white_balance.tint.set_progress(0)
        result = edit.color.white_balance.tint.is_number(0)
        self.report.new_result("cb672a5c-543a-4d03-b81c-0a1a9f56070a", result)

        self.report.start_uuid("1637dd88-bb2a-40c0-ab03-c854f9681e58")
        edit.color.white_balance.tint.set_progress(1)
        result = edit.color.white_balance.tint.is_number(100)
        self.report.new_result("1637dd88-bb2a-40c0-ab03-c854f9681e58", result)

        self.report.start_uuid("2049e934-49b4-4f49-b4b2-5c5b2bbfa708")
        edit.color.white_balance.tint.set_progress(0.3)
        result = edit.color.white_balance.tint.is_progress(0.3)
        self.report.new_result("2049e934-49b4-4f49-b4b2-5c5b2bbfa708", result)

        self.report.start_uuid("8a325e3f-f985-4bae-91da-c58266a6d4dc")
        edit.color.white_balance.tint.set_progress(0.9)
        result = edit.color.white_balance.tint.is_progress(0.9)
        self.report.new_result("8a325e3f-f985-4bae-91da-c58266a6d4dc", result)

        edit.back()

        logger("[V]Skin_smoothener")
        self.report.start_uuid("5205c71f-b7ee-4d85-91ff-85db47e21d33")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.skin_smoothener)
        edit.select_from_bottom_edit_menu('Skin Smoothener')
        logger("[V]Skin_smoothener_Skin_Brightness")
        edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        result = edit.skin_smoothener.skin_brightness.is_number(80)
        self.report.new_result("5205c71f-b7ee-4d85-91ff-85db47e21d33", result)

        self.report.start_uuid("e5838f68-1e4c-4364-a45c-dbc8ceeaa47d")
        edit.skin_smoothener.skin_brightness.set_progress(0)
        result = edit.skin_smoothener.skin_brightness.is_number(40)
        self.report.new_result("e5838f68-1e4c-4364-a45c-dbc8ceeaa47d", result)

        self.report.start_uuid("30928b0e-7adf-49bb-9985-6f942fde8659")
        edit.skin_smoothener.skin_brightness.set_progress(1)
        result = edit.skin_smoothener.skin_brightness.is_number(100)
        self.report.new_result("30928b0e-7adf-49bb-9985-6f942fde8659", result)

        self.report.start_uuid("d0dc8798-0ade-4c09-a472-d2a2b7b00c56")
        edit.skin_smoothener.skin_brightness.set_progress(0.3)
        result = edit.skin_smoothener.skin_brightness.is_progress(0.3)
        self.report.new_result("d0dc8798-0ade-4c09-a472-d2a2b7b00c56", result)

        self.report.start_uuid("523fa5b4-4430-4696-a383-d2225a96f4ae")
        edit.skin_smoothener.skin_brightness.set_progress(0.9)
        result = edit.skin_smoothener.skin_brightness.is_progress(0.9)
        self.report.new_result("523fa5b4-4430-4696-a383-d2225a96f4ae", result)

        logger("[V]Skin_smoothener_Skin_Smoothness")
        self.report.start_uuid("393cfcfd-43b0-475f-b13d-fe0252d6c02a")
        edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        result = edit.skin_smoothener.skin_smoothness.is_number(80)
        self.report.new_result("393cfcfd-43b0-475f-b13d-fe0252d6c02a", result)

        self.report.start_uuid("f96b2755-2cab-4f5c-bcfa-49da0a234a26")
        edit.skin_smoothener.skin_smoothness.set_progress(0)
        result = edit.skin_smoothener.skin_smoothness.is_number(0)
        self.report.new_result("f96b2755-2cab-4f5c-bcfa-49da0a234a26", result)

        self.report.start_uuid("4d4f4af3-6c98-4a4c-9774-bac2339ed28a")
        edit.skin_smoothener.skin_smoothness.set_progress(1)
        result = edit.skin_smoothener.skin_smoothness.is_number(100)
        self.report.new_result("4d4f4af3-6c98-4a4c-9774-bac2339ed28a", result)

        self.report.start_uuid("cd508710-449f-46a2-9885-02f359ea68bb")
        edit.skin_smoothener.skin_smoothness.set_progress(0.3)
        result = edit.skin_smoothener.skin_smoothness.is_progress(0.3)
        self.report.new_result("cd508710-449f-46a2-9885-02f359ea68bb", result)

        self.report.start_uuid("86e0beb3-2ccf-4458-bb7f-11d91d70306c")
        edit.skin_smoothener.skin_smoothness.set_progress(0.9)
        result = edit.skin_smoothener.skin_smoothness.is_progress(0.9)
        self.report.new_result("86e0beb3-2ccf-4458-bb7f-11d91d70306c", result)

        edit.back()
        self.report.start_uuid("ef0b9513-1de9-45a3-a6e4-2059298ee095")
        self.report.start_uuid("e843e5e9-7186-48e9-abb1-9c4f2b9030c8")
        result_apply_to_main_track = edit.is_exist_in_bottom_edit_menu('Skin Smoothener')
        self.report.new_result("ef0b9513-1de9-45a3-a6e4-2059298ee095", result_apply_to_main_track)
        self.report.new_result("e843e5e9-7186-48e9-abb1-9c4f2b9030c8", result_apply_to_main_track)

        logger("[V]Preview")
        self.report.start_uuid("666bb375-a688-4f90-9dc1-535a374ad165")
        result_preview = edit.click_preview()
        self.report.new_result("666bb375-a688-4f90-9dc1-535a374ad165", result_preview)

        self.report.start_uuid("d21dac5a-a1a4-46e6-a587-1c14512a663c")
        result_has_timecode = edit.is_exist(L.edit.timeline.timecode)
        self.report.new_result("d21dac5a-a1a4-46e6-a587-1c14512a663c", result_has_timecode)
        edit.el(L.edit.menu.play).click()  # stop playback

        logger("[V]undo")
        self.report.start_uuid("1cccd2a9-0e20-4988-95a9-cda0dabef154")
        edit.click(L.edit.menu.undo)
        result_undo = edit.is_exist_in_bottom_edit_menu('Skin Smoothener')
        self.report.new_result("1cccd2a9-0e20-4988-95a9-cda0dabef154", result_undo)

        logger("[V]Auto Save")
        self.report.start_uuid("2653a289-4c3f-44f0-98fd-7496f6a52d0a")
        result_auto_save = edit.is_auto_save()
        self.report.new_result("2653a289-4c3f-44f0-98fd-7496f6a52d0a", result_auto_save)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_01_02(self):
        logger("test_scenario_02_01_02")
        main = self.main_page
        import_media = self.import_media
        edit = self.edit

        # Initi #
        main.project_create_new(type="photo")

        ## Photo ##
        logger("[P]split")
        self.report.start_uuid("a29fa42b-7da3-47ae-8f5b-8d3d9a8b4dfb")
        edit.swipe_element(L.edit.timeline.clip_photo, "left", 400)
        edit.click(L.edit.timeline.clip_photo)
        result = edit.is_exist_in_bottom_edit_menu('Split')
        self.report.new_result("a29fa42b-7da3-47ae-8f5b-8d3d9a8b4dfb", result)

        self.report.start_uuid("a8b1a23a-6604-4ea4-b703-388bf7afaca0")
        self.report.start_uuid("f210260a-0827-41aa-a792-85d5cbf3c1e3")
        is_split_success, is_thumbnail_change = edit.split_clip(L.edit.timeline.clip_photo)
        self.report.new_result("a8b1a23a-6604-4ea4-b703-388bf7afaca0", is_split_success)
        self.report.new_result("f210260a-0827-41aa-a792-85d5cbf3c1e3", is_thumbnail_change)

        logger("[P]Rotate")
        self.report.start_uuid("0ed05cdd-8647-4dcf-9747-9894dad0e3e3")
        edit.click(L.edit.timeline.clip_photo)
        #edit.click(L.edit.menu.edit)
        result = edit.is_exist_in_bottom_edit_menu('Rotate')
        self.report.new_result("0ed05cdd-8647-4dcf-9747-9894dad0e3e3", result)

        self.report.start_uuid("1a05c9a6-66b7-4703-9f22-6172a920c201")
        self.report.start_uuid("9a0bb1c8-ad1a-435c-9857-de26254509d0")
        result = edit.click_rotate()
        self.report.new_result("1a05c9a6-66b7-4703-9f22-6172a920c201", result)
        self.report.new_result("9a0bb1c8-ad1a-435c-9857-de26254509d0", result)

        logger("[P]Trim")
        self.report.start_uuid("2ace49cd-c714-4e6c-a8fc-ae494f61b24b")
        self.report.start_uuid("89c4c006-39de-49b3-8152-3d32058ee865")
        result_trim, result_thumbnail = edit.trim_video(L.edit.timeline.clip_photo)
        self.report.new_result("2ace49cd-c714-4e6c-a8fc-ae494f61b24b", result_trim)
        self.report.new_result("89c4c006-39de-49b3-8152-3d32058ee865", result_thumbnail)

        self.report.start_uuid("48a4971d-ce32-4169-9aea-bb8a55f9cd47")
        result = edit.check_timeline_gap(type="Photo")
        self.report.new_result("48a4971d-ce32-4169-9aea-bb8a55f9cd47", result)

        logger("[P]Flip")
        self.report.start_uuid("4ac3df8a-866a-4b1a-9b2f-131828bec003")
        # edit.click(L.edit.menu.edit)
        edit.timeline_select_item_by_index_on_track(1, 2)
        edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(3)
        result = edit.is_exist_in_bottom_edit_menu('Flip')
        self.report.new_result("4ac3df8a-866a-4b1a-9b2f-131828bec003", result)

        self.report.start_uuid("f25a6a25-0e02-47e7-a946-ced87e59c5b7")
        self.report.start_uuid("9fdbe069-5de1-4c45-bb21-d3ea110a0342")
        result = edit.click_flip()
        self.report.new_result("f25a6a25-0e02-47e7-a946-ced87e59c5b7", result)
        self.report.new_result("9fdbe069-5de1-4c45-bb21-d3ea110a0342", result)

        logger("[P]Crop")
        self.report.start_uuid("15c5cdc8-d471-4df4-9ae8-bfd5dcc32067")
        # edit.click(L.edit.menu.edit) #keep previous step
        result = edit.is_exist_in_bottom_edit_menu('Crop')
        self.report.new_result("15c5cdc8-d471-4df4-9ae8-bfd5dcc32067", result)

        self.report.start_uuid("8683f4f6-9110-4577-be14-3b7174f60f32")
        result = edit.click_crop()
        self.report.new_result("8683f4f6-9110-4577-be14-3b7174f60f32", result)
        #edit.click(L.edit.menu.back_session)

        logger("[P]Sharpness")
        self.report.start_uuid("bca3a613-0136-4e50-bed8-d3bcaa2916dc")
        #edit.click(L.edit.menu.edit)
        result_default_value = edit.click_sharpness()
        self.report.new_result("bca3a613-0136-4e50-bed8-d3bcaa2916dc", result_default_value)

        self.report.start_uuid("4c4e9e25-e039-4899-a165-1e18c39db2bd")
        result_preview = edit.set_sharpness(1)
        self.report.new_result("4c4e9e25-e039-4899-a165-1e18c39db2bd", result_preview)
        edit.back()

        logger("[P]Color_Preset")
        self.report.start_uuid("72409732-13c5-4490-a1a9-3bd1d6ba34db")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        result = edit.select_preset()
        self.report.new_result("72409732-13c5-4490-a1a9-3bd1d6ba34db", result)
        self.driver.driver.back()

        logger("[P]Skin_smoothener")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.skin_smoothener)
        edit.select_from_bottom_edit_menu('Skin Smoothener')
        logger("[P]Skin_smoothener_Skin_Brightness")
        self.report.start_uuid("e6c5ef78-3357-4d24-bd2c-35b84312ab6e")
        edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        result_default = edit.skin_smoothener.skin_brightness.is_number(80)
        self.report.new_result("e6c5ef78-3357-4d24-bd2c-35b84312ab6e", result_default)

        self.report.start_uuid("d0a7463a-9844-446a-bd11-d569093a238e")
        edit.skin_smoothener.skin_brightness.set_progress(0)
        result_min = edit.skin_smoothener.skin_brightness.is_number(40)
        self.report.new_result("d0a7463a-9844-446a-bd11-d569093a238e", result_min)

        self.report.start_uuid("d137ff35-e784-48a6-932c-8c6043842bd0")
        edit.skin_smoothener.skin_brightness.set_progress(1)
        result_max = edit.skin_smoothener.skin_brightness.is_number(100)
        self.report.new_result("d137ff35-e784-48a6-932c-8c6043842bd0", result_max)

        self.report.start_uuid("a4eca9b7-5e95-4705-85c3-215ced32e652")
        edit.skin_smoothener.skin_brightness.set_progress(0.3)
        result_decrease = edit.skin_smoothener.skin_brightness.is_progress(0.3)
        self.report.new_result("a4eca9b7-5e95-4705-85c3-215ced32e652", result_decrease)

        self.report.start_uuid("7702acb8-01ab-485b-a1b9-1ae0d40b3db0")
        edit.skin_smoothener.skin_brightness.set_progress(0.9)
        result_increase = edit.skin_smoothener.skin_brightness.is_progress(0.9)
        self.report.new_result("7702acb8-01ab-485b-a1b9-1ae0d40b3db0", result_increase)

        logger("[P]Skin_smoothener_Skin_Smoothness")
        self.report.start_uuid("b8555a72-e79c-48e8-be81-b8cd86c7e385")
        edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        result_default = edit.skin_smoothener.skin_smoothness.is_number(80)
        self.report.new_result("b8555a72-e79c-48e8-be81-b8cd86c7e385", result_default)

        self.report.start_uuid("cb153b5e-c536-4ed6-8d9f-71f235711d5d")
        edit.skin_smoothener.skin_smoothness.set_progress(0)
        result_min = edit.skin_smoothener.skin_smoothness.is_number(0)
        self.report.new_result("cb153b5e-c536-4ed6-8d9f-71f235711d5d", result_min)

        self.report.start_uuid("a410a826-d866-4cf9-a1c7-a7a77af7432b")
        edit.skin_smoothener.skin_smoothness.set_progress(1)
        result_max = edit.skin_smoothener.skin_smoothness.is_number(100)
        self.report.new_result("a410a826-d866-4cf9-a1c7-a7a77af7432b", result_max)

        self.report.start_uuid("a7a640c4-9eb1-457b-9983-96fabfd51c26")
        edit.skin_smoothener.skin_smoothness.set_progress(0.3)
        result_decrease = edit.skin_smoothener.skin_smoothness.is_progress(0.3)
        self.report.new_result("a7a640c4-9eb1-457b-9983-96fabfd51c26", result_decrease)

        self.report.start_uuid("98e4a27e-3f30-4416-99c5-09a5120d3d0d")
        edit.skin_smoothener.skin_smoothness.set_progress(0.9)
        result_increase = edit.skin_smoothener.skin_smoothness.is_progress(0.9)
        self.report.new_result("98e4a27e-3f30-4416-99c5-09a5120d3d0d", result_increase)
        edit.back()

        self.report.start_uuid("9876425c-07fa-4251-aac2-043efba6099e")
        self.report.start_uuid("efbf6762-c2be-423a-866a-5f02850339b0")
        result_apply_to_main_track = edit.is_exist_in_bottom_edit_menu('Skin Smoothener')
        self.report.new_result("9876425c-07fa-4251-aac2-043efba6099e", result_apply_to_main_track)
        self.report.new_result("efbf6762-c2be-423a-866a-5f02850339b0", result_apply_to_main_track)
        
        
        logger("[P]Fit & Fill")
        self.report.start_uuid("1dd00bf7-eb3d-4c16-a59e-df719e686705")
        edit.timeline_select_item_by_index_on_track(1,2)
        edit.select_from_bottom_edit_menu('Fit & Fill')
        result = edit.fit_and_fill.apply_fit()
        self.report.new_result("1dd00bf7-eb3d-4c16-a59e-df719e686705", result)        
        
        self.report.start_uuid("a7a218b8-8869-4823-b94f-09e43738c99d")
        result = edit.fit_and_fill.apply_fill()
        self.report.new_result("a7a218b8-8869-4823-b94f-09e43738c99d", result)        
        
        self.report.start_uuid("df25ea97-3885-4565-8674-8e1dab542c1f")
        result = edit.fit_and_fill.zoom_preview()
        self.report.new_result("df25ea97-3885-4565-8674-8e1dab542c1f", result)        
        
        self.report.start_uuid("9ce3c256-c06f-4d46-ae32-690a8f55dc0e")
        edit.fit_and_fill.apply_fit()
        result = edit.fit_and_fill.enter_background()
        self.report.new_result("9ce3c256-c06f-4d46-ae32-690a8f55dc0e", result)        
        
        self.report.start_uuid("da46e132-84b5-4309-85e6-25912abfe68c")
        edit.click(L.edit.fit_and_fill.btn_blur)
        time.sleep(5)
        default_value = edit.fit_and_fill.get_value()
        if default_value == '5.0':
            result = True
        else:
            result - False
        self.report.new_result("da46e132-84b5-4309-85e6-25912abfe68c", result)        
        
        self.report.start_uuid("5421f1c3-fa82-4e1c-9bd2-3ec000e6bc79")
        apply_result = edit.fit_and_fill.set_slider(0)
        default_value = edit.fit_and_fill.get_value()
        if default_value == '10.0':
            result = True
        else:
            result - False
        self.report.new_result("5421f1c3-fa82-4e1c-9bd2-3ec000e6bc79", result)        
        
        self.report.start_uuid("392c83be-1b18-4144-8139-e37f4bc78912")
        apply_result = edit.fit_and_fill.set_slider(1)
        default_value = edit.fit_and_fill.get_value()
        if default_value == '0.0':
            result = True
        else:
            result - False
        self.report.new_result("392c83be-1b18-4144-8139-e37f4bc78912", result)        
        
        self.report.start_uuid("788d9d49-a399-4836-9a5a-73e6adbcec6b")
        self.report.start_uuid("12078d3f-6e1e-4c7c-9646-cdd0b4f1bf78")
        edit.click(L.edit.fit_and_fill.btn_background_color)
        apply_result = edit.fit_and_fill.select_color_by_order(2)
        default_value = edit.fit_and_fill.get_value()
        if default_value == '0.0':
            result = True
        else:
            result - False
        self.report.new_result("788d9d49-a399-4836-9a5a-73e6adbcec6b", result)
        self.report.new_result("12078d3f-6e1e-4c7c-9646-cdd0b4f1bf78", apply_result)

        self.report.start_uuid("839b984f-7bbc-4c90-9f7c-937517e968c7")
        apply_result = edit.fit_and_fill.set_slider(0)
        default_value = edit.fit_and_fill.get_value()
        if default_value == '1.0':
            result = True
        else:
            result - False
        self.report.new_result("839b984f-7bbc-4c90-9f7c-937517e968c7", result)    
        
        self.report.start_uuid("b4f3d847-7ca1-49d8-9675-2548942ff9c4")
        apply_result = edit.fit_and_fill.set_slider(1)
        default_value = edit.fit_and_fill.get_value()
        if default_value == '-1.0':
            result = True
        else:
            result - False
        self.report.new_result("b4f3d847-7ca1-49d8-9675-2548942ff9c4", result)    
        
        self.report.start_uuid("2700a3cb-50c3-4b20-b2a6-c53551176f01")
        result = edit.fit_and_fill.select_color_by_colorpicker()
        self.report.new_result("2700a3cb-50c3-4b20-b2a6-c53551176f01", result)        
        
        self.report.start_uuid("9576806e-542b-454e-bcb9-f68b2129b64d")
        result = edit.fit_and_fill.select_color_by_order(3, 5)
        self.report.new_result("9576806e-542b-454e-bcb9-f68b2129b64d", result)        
        
        
        self.report.start_uuid("a7c251ce-afdb-48d7-9ee3-5ecf91451c7c")
        edit.back()
        edit.click(L.edit.fit_and_fill.btn_background_pattern)
        result = edit.fit_and_fill.select_pattern_by_order(1)
        self.report.new_result("a7c251ce-afdb-48d7-9ee3-5ecf91451c7c", result)        
        
        self.report.start_uuid("5df5c584-5393-4b89-bee8-cf139e820fb0")
        edit.fit_and_fill.select_pattern_by_order(4)
        result = edit.check_premium_features_used()
        self.report.new_result("5df5c584-5393-4b89-bee8-cf139e820fb0", result)

        self.report.start_uuid("1f282e0d-52ca-4dd5-8f58-901afba122e7")
        result_watermark = edit.is_exist(L.edit.preview.watermark)
        self.report.new_result("1f282e0d-52ca-4dd5-8f58-901afba122e7", result_watermark)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_01_03(self):
        logger("test_scenario_02_01_03")
        main = self.main_page
        import_media = self.import_media
        edit = self.edit

        # Initi #
        main.project_create_new(type='audio')

        logger("[A]split")
        edit.force_uncheck_help_enable_tip_to_Leave()
        self.report.start_uuid("a1963b21-6657-428a-8d7c-e364759ff8f7")
        edit.swipe_element(L.edit.timeline.clip_audio, "left", 400)
        edit.click(L.edit.timeline.clip_audio)
        result_split = edit.is_exist_in_bottom_edit_menu('Split')
        self.report.new_result("a1963b21-6657-428a-8d7c-e364759ff8f7", result_split)

        self.report.start_uuid("edf7a556-0c94-4873-8964-f3607bb7bea6")
        self.report.start_uuid("4c5605cb-b555-49e2-98af-42f218648b7d")
        is_split_success, is_thumbnail_change = edit.split_music(L.edit.timeline.clip_audio)
        edit.click(L.edit.menu.delete)
        self.report.new_result("edf7a556-0c94-4873-8964-f3607bb7bea6", is_split_success)
        self.report.new_result("4c5605cb-b555-49e2-98af-42f218648b7d", is_thumbnail_change)

        logger("[A]Trim")
        self.report.start_uuid("cf534cbd-b813-4ff4-b4e5-8f6d78d8d038")
        self.report.start_uuid("d08f9e0a-2f6c-4671-9337-360023460dd2")
        edit.click(L.edit.timeline.clip_audio)
        result_trim, result_thumbnail = edit.trim_video(L.edit.timeline.clip_audio)
        self.report.new_result("cf534cbd-b813-4ff4-b4e5-8f6d78d8d038", result_trim)
        self.report.new_result("d08f9e0a-2f6c-4671-9337-360023460dd2", result_thumbnail)

        self.report.start_uuid("4afec38c-bc92-4b82-9f80-0f34c02668b1")
        result = edit.check_timeline_gap(type="Audio")
        self.report.new_result("4afec38c-bc92-4b82-9f80-0f34c02668b1", result)
"""
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_01_04(self):
        logger("test_scenario_02_01_04")
        main = self.main_page
        import_media = self.import_media
        edit = self.edit

        # Initi #
        main.project_create_new(type="photo")

        logger("[V]Blanding_Overlay")
        self.report.start_uuid("18ebb862-1dd2-11b2-8002-080027b246c3")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.mask)
        edit.select_from_bottom_edit_menu('Blending')
        result = edit.select_Blanding1()
        self.report.new_result("18ebb862-1dd2-11b2-8002-080027b246c3", result)
        self.driver.driver.back()

        logger("[V]Blanding_Multiply")
        self.report.start_uuid("18ebb862-1dd2-11b2-8004-080027b246c3")
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.mask)
        edit.select_from_bottom_edit_menu('Blending')
        result = edit.select_Blanding2()
        self.report.new_result("18ebb862-1dd2-11b2-8004-080027b246c3", result)
        self.driver.driver.back()
"""