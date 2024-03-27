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
add_package = 'com.cyberlink.addirector'

class Test_SFT_Scenario_06_11:
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
    def test_sce_06_11_01(self):
        logger('>>> test_sce_06_11_01 : GettyImages Premium <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        self.report.start_uuid('40284e7a-ee36-4196-bffa-6ae53e7fdd77')
        page_main.project_click_new()
        page_main.project_set_name("sce_06_11_01")
        page_main.project_set_16_9()
        time.sleep(5)
        # page_media.select_media_by_text('Stock Video')
        # page_media.click(L.import_media.video_library.tab_video_gettyimages)
        # time.sleep(5)
        # result = False if page_media.is_exist(L.import_media.gettyimages_premium.library_unit_purchasable) else True
        self.report.new_result('40284e7a-ee36-4196-bffa-6ae53e7fdd77', None, 'New behavior')

        self.report.start_uuid('e46a1772-a2b6-4d9e-847a-5cfba36028eb')
        # page_media.switch_to_photo_library()
        # time.sleep(5)
        # page_media.select_media_by_text('Stock Photo')
        # page_media.click(L.import_media.video_library.tab_video_gettyimages)
        # time.sleep(5)
        # result = False if page_media.is_exist(L.import_media.gettyimages_premium.library_unit_purchasable) else True
        self.report.new_result('e46a1772-a2b6-4d9e-847a-5cfba36028eb', None, 'New behavior')

        # page_main.enter_settings_from_main()
        # page_edit.back()
        # time.sleep(3)
        # page_edit.back()
        # time.sleep(3)
        page_edit.click(L.edit.menu.timeline_setting)
        page_edit.click(L.edit.sub_menu.settings)
        time.sleep(3)
        page_main.sign_in_cyberlink_account()
        
        self.report.start_uuid('55082e27-9db8-4384-ad5a-7194e065f946')
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.select_media_by_text('Stock Video')
        # page_media.click(L.import_media.video_library.tab_video_gettyimages)
        page_media.select_stock_category('gettyimage_premium')
        time.sleep(5)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.library_unit_purchasable) else False
        self.report.new_result('55082e27-9db8-4384-ad5a-7194e065f946', result)
        
        self.report.start_uuid('d58de69f-ebb6-432e-8703-941622a3af70')
        result = page_media.check_gi_library_order()
        self.report.new_result('d58de69f-ebb6-432e-8703-941622a3af70', None, 'New category')
        
        self.report.start_uuid('6d8b13dd-4886-4206-a887-69dd60fbe0f4')
        page_media.click(L.import_media.gettyimages_premium.library_unit_purchasable)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.btn_preview_first) else False
        self.report.new_result('6d8b13dd-4886-4206-a887-69dd60fbe0f4', result)
        
        self.report.start_uuid('163008d8-59ae-4cfc-8f0f-1f5636696bb5')
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.learn_more) else False
        self.report.new_result('163008d8-59ae-4cfc-8f0f-1f5636696bb5', result)
        
        self.report.start_uuid('61eef148-696e-4372-8f1a-c4e579bfa54d')
        page_media.click(L.import_media.gettyimages_premium.btn_preview_first)
        time.sleep(3)
        result = page_edit.timeline_select_item_by_index_on_track(1, 1)
        self.report.new_result('61eef148-696e-4372-8f1a-c4e579bfa54d', result)
        
        self.report.start_uuid('dd3c13b8-8d47-4998-b9d1-3a2d5562e9ac')
        page_media.click(L.edit.try_before_buy.premium_features_used_bubble)
        time.sleep(3)
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.premium_list) else False
        self.report.new_result('dd3c13b8-8d47-4998-b9d1-3a2d5562e9ac', result)

        self.report.start_uuid('0b1cceda-9e88-4935-9922-21484c44a430')
        page_edit.back()
        time.sleep(3)
        page_media.click(L.edit.menu.produce)
        time.sleep(3)
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.premium_list) else False
        self.report.new_result('0b1cceda-9e88-4935-9922-21484c44a430', result)
        
        self.report.start_uuid('65a0cc0b-49d2-43f8-a8ce-2fa04cde37aa')
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_thumbnail) else False
        self.report.new_result('65a0cc0b-49d2-43f8-a8ce-2fa04cde37aa', result)
        
        self.report.start_uuid('d2acb634-cf22-48fb-b6a1-df1c9f2bdf14')
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_price) else False
        self.report.new_result('d2acb634-cf22-48fb-b6a1-df1c9f2bdf14', result)
        
        self.report.start_uuid('2ce54289-1924-4c2f-b329-5109149474a7')
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.total_price) else False
        self.report.new_result('2ce54289-1924-4c2f-b329-5109149474a7', result)
        
        self.report.start_uuid('6a87d6f2-bbc9-413b-8b22-dcd613b4d7da')
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_footer) else False
        self.report.new_result('6a87d6f2-bbc9-413b-8b22-dcd613b4d7da', result)
        
        self.report.start_uuid('0a12d2d0-48e0-4612-b500-8e3f91faa165')
        page_media.click(L.import_media.gettyimages_premium.buy_dialog.btn_buy)
        time.sleep(10)
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.btn_googlepay_buy) else False
        self.report.new_result('0a12d2d0-48e0-4612-b500-8e3f91faa165', result)
        
        
        self.report.start_uuid('43ee12b8-939d-403c-b40d-2bb00474caea')
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Photo')
        # page_media.click(L.import_media.video_library.tab_video_gettyimages)
        page_media.select_stock_category('gettyimage_premium')
        time.sleep(5)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.library_unit_purchasable) else False
        self.report.new_result('43ee12b8-939d-403c-b40d-2bb00474caea', result)
        
        self.report.start_uuid('8f51e00a-7fbf-4203-93b3-5752731f8ca8')
        result = page_media.check_gi_library_order()
        self.report.new_result('8f51e00a-7fbf-4203-93b3-5752731f8ca8', result)
        
        self.report.start_uuid('005cbbef-c815-4b0f-abf0-98b85b4ffe2b')
        page_media.click(L.import_media.gettyimages_premium.library_unit_purchasable)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.btn_preview_first) else False
        self.report.new_result('005cbbef-c815-4b0f-abf0-98b85b4ffe2b', result)
        
        self.report.start_uuid('7c11e52e-eb92-4a36-b33e-8be3e14c5754')
        page_media.click(L.import_media.gettyimages_premium.btn_preview_first)
        time.sleep(3)
        result = page_edit.timeline_select_item_by_index_on_track(1, 1)
        self.report.new_result('7c11e52e-eb92-4a36-b33e-8be3e14c5754', result)
        
        self.report.start_uuid('6948144e-e61a-4f38-9179-337574a0195a')
        page_media.click(L.edit.try_before_buy.premium_features_used_bubble)
        time.sleep(3)
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_price) else False
        self.report.new_result('6948144e-e61a-4f38-9179-337574a0195a', result)
        
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.timeline_setting)
        page_edit.click(L.edit.sub_menu.settings)
        time.sleep(3)
        page_main.sign_out_cyberlink_account()
        
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_11_02(self):
        logger('>>> test_sce_06_11_02 : Stock Video Filter <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        self.report.start_uuid('0c31cbfb-9c11-4b97-b294-49657a8e9468')
        page_main.project_click_new()
        page_main.project_set_name("sce_06_11_02")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.select_media_by_text('Stock Video')
        page_media.select_stock_category('pixabay')
        time.sleep(5)
        result = False if page_media.check_filter_button_status() else True     # Should be disabled
        self.report.new_result('0c31cbfb-9c11-4b97-b294-49657a8e9468', result)        

        self.report.start_uuid('c05596af-d6b7-4a3d-b614-e9a31e4dda86')
        page_media.select_stock_category('shutterstock')
        time.sleep(5)
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('c05596af-d6b7-4a3d-b614-e9a31e4dda86', result)
        
        self.report.start_uuid('8ec6bbd4-f376-4a4e-9709-95283d5b16d5')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('8ec6bbd4-f376-4a4e-9709-95283d5b16d5', result)
        
        self.report.start_uuid('6d41964f-e4ce-45ab-918b-a93b0fe58ed0')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6d41964f-e4ce-45ab-918b-a93b0fe58ed0', result)
        
        self.report.start_uuid('c423e5a2-5961-4c94-97bb-1b84dfefc8f9')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('c423e5a2-5961-4c94-97bb-1b84dfefc8f9', result)
        
        self.report.start_uuid('1a815ebc-ce19-4846-9554-01ea6a0236fd')
        page_media.select_stock_category('gettyimage')
        time.sleep(5)
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('1a815ebc-ce19-4846-9554-01ea6a0236fd', result)

        self.report.start_uuid('6ac19553-691d-4609-8de6-9ac98038a151')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6ac19553-691d-4609-8de6-9ac98038a151', result)  
        
        self.report.start_uuid('000fd8ac-b6c7-4c71-ad78-ce1ce2f5ca23')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('000fd8ac-b6c7-4c71-ad78-ce1ce2f5ca23', result)
        
        self.report.start_uuid('6c138c1e-f0f9-4fc5-aefb-6fdb431a9bf8')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6c138c1e-f0f9-4fc5-aefb-6fdb431a9bf8', result)
        
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.timeline_setting)
        page_edit.click(L.edit.sub_menu.settings)
        time.sleep(3)
        page_main.sign_in_cyberlink_account()
        
        self.report.start_uuid('0ea49a43-3b0f-49ad-abf7-f475114ee7ad')
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.select_media_by_text('Stock Video')
        page_media.select_stock_category('gettyimage')
        time.sleep(5)
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.subscribed)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('0ea49a43-3b0f-49ad-abf7-f475114ee7ad', result)

        self.report.start_uuid('3df555fd-51ed-4ae2-a048-c39cff76333b')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('3df555fd-51ed-4ae2-a048-c39cff76333b', result)  
        
        self.report.start_uuid('51ce8cb6-0e88-4e84-b71b-5157a2a1dd83')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('51ce8cb6-0e88-4e84-b71b-5157a2a1dd83', result)
        
        self.report.start_uuid('d79e703c-d648-4182-b1fc-6e9bd394cdb6')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('d79e703c-d648-4182-b1fc-6e9bd394cdb6', result)
        
        self.report.start_uuid('0eb38fe5-4ce1-41be-9197-9f89c4d3202e')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.pay)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('0eb38fe5-4ce1-41be-9197-9f89c4d3202e', result)
        
        self.report.start_uuid('dadbaa0f-8add-4db6-b524-07d54362b23e')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('dadbaa0f-8add-4db6-b524-07d54362b23e', result)  
        
        self.report.start_uuid('cfdd8336-e7a3-426f-82cf-5986e702e217')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('cfdd8336-e7a3-426f-82cf-5986e702e217', result)
        
        self.report.start_uuid('f654710a-6490-46b7-ac1c-434870c675c2')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('f654710a-6490-46b7-ac1c-434870c675c2', result)
        
        # SS image
        self.report.start_uuid('679dbada-ec20-49da-a7a5-3582b95f1374')
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Photo')
        time.sleep(5)
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('679dbada-ec20-49da-a7a5-3582b95f1374', result)

        self.report.start_uuid('7c940d57-375c-421d-a926-6d010d74a963')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('7c940d57-375c-421d-a926-6d010d74a963', result)  
        
        self.report.start_uuid('e0ab51f5-0590-4938-9dd2-9b82889eee9a')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('e0ab51f5-0590-4938-9dd2-9b82889eee9a', result)
        
        self.report.start_uuid('c44b495f-9ac6-47c1-ab87-af83e8f70225')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('c44b495f-9ac6-47c1-ab87-af83e8f70225', result)
        
        # SS vertical
        self.report.start_uuid('9e1e2062-e2e2-474a-9aa0-93d6370f548f')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_vertical)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('9e1e2062-e2e2-474a-9aa0-93d6370f548f', result)

        self.report.start_uuid('ab10e2ec-9ddf-4287-b173-e59e99fb742a')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('ab10e2ec-9ddf-4287-b173-e59e99fb742a', result)  
        
        self.report.start_uuid('4fe08631-048d-4610-bc93-a468562e9c64')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('4fe08631-048d-4610-bc93-a468562e9c64', result)
        
        self.report.start_uuid('6b283917-0106-4e17-95c2-ef187223897b')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6b283917-0106-4e17-95c2-ef187223897b', result)       
        
        # SS horizontal
        self.report.start_uuid('e19925bc-c4ec-42a4-90a6-ce8e80ae352d')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_horizontal)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('e19925bc-c4ec-42a4-90a6-ce8e80ae352d', result)
        
        self.report.start_uuid('241d79d1-b88b-4f6c-9645-e635b245bd31')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('241d79d1-b88b-4f6c-9645-e635b245bd31', result)  
        
        self.report.start_uuid('cae59dc4-fa00-46e2-a634-539ea62bbd45')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('cae59dc4-fa00-46e2-a634-539ea62bbd45', result)
        
        self.report.start_uuid('6ece48c7-f072-4b28-92c0-95239ad1e291')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6ece48c7-f072-4b28-92c0-95239ad1e291', result)        
        
        # GI All-All
        self.report.start_uuid('4014dadb-0ec9-47db-a6fe-832c75927363')
        page_media.select_stock_category('gettyimage')
        time.sleep(3)
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_all)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('4014dadb-0ec9-47db-a6fe-832c75927363', result)
        
        self.report.start_uuid('148b306d-35af-4c56-a9c9-0139a5e1bcbc')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('148b306d-35af-4c56-a9c9-0139a5e1bcbc', result)  
        
        self.report.start_uuid('ffca230c-c7ea-46b3-b08b-74aa53a61cee')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('ffca230c-c7ea-46b3-b08b-74aa53a61cee', result)
        
        self.report.start_uuid('ce6846df-b88f-4d1d-acfd-9cc9bcab4640')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('ce6846df-b88f-4d1d-acfd-9cc9bcab4640', result)        
        
        # GI All-Vertical
        self.report.start_uuid('959208db-3505-4b57-a999-592841175af4')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_vertical)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('959208db-3505-4b57-a999-592841175af4', result)
        
        self.report.start_uuid('cccde99c-3c48-4bf1-be35-f57b0ea13b3f')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('cccde99c-3c48-4bf1-be35-f57b0ea13b3f', result)  
        
        self.report.start_uuid('328ae8e5-5eec-4908-ba15-0b29060167a7')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('328ae8e5-5eec-4908-ba15-0b29060167a7', result)
        
        self.report.start_uuid('6afcfc64-c215-4cdb-ab9f-fb108d09c65e')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6afcfc64-c215-4cdb-ab9f-fb108d09c65e', result)        
        
        # GI All-horizontal
        self.report.start_uuid('459eba4d-0739-46a5-ab58-79de0ed114fc')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_horizontal)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('459eba4d-0739-46a5-ab58-79de0ed114fc', result)
        
        self.report.start_uuid('3638dbd9-04ec-45eb-8079-496e76f5053c')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('3638dbd9-04ec-45eb-8079-496e76f5053c', result)  
        
        self.report.start_uuid('05675157-7bde-48f7-9457-e21f91abf5c8')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('05675157-7bde-48f7-9457-e21f91abf5c8', result)
        
        self.report.start_uuid('4b713e81-ddca-44c0-b7ec-7fd8dbb79533')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('4b713e81-ddca-44c0-b7ec-7fd8dbb79533', result)        
        
        # GI All-square
        self.report.start_uuid('96556558-48cd-4165-90a8-9459b4a0ab81')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_square)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('96556558-48cd-4165-90a8-9459b4a0ab81', result)
        
        self.report.start_uuid('dc30b4ef-2731-48e3-87a2-732693f27a7b')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('dc30b4ef-2731-48e3-87a2-732693f27a7b', result)  
        
        self.report.start_uuid('2ef50cb6-8a5c-470b-a3eb-c8826f33a8ba')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('2ef50cb6-8a5c-470b-a3eb-c8826f33a8ba', result)
        
        self.report.start_uuid('1b714b68-1d3c-4998-ae5a-9fce81aa47f8')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('1b714b68-1d3c-4998-ae5a-9fce81aa47f8', result)        
        
        # GI All-panoramic
        self.report.start_uuid('f6080364-b14e-4f05-a907-65bfdcce76e9')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_panoramic)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('f6080364-b14e-4f05-a907-65bfdcce76e9', result)
        
        self.report.start_uuid('503c3238-79e8-4186-b817-d8812850fd42')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('503c3238-79e8-4186-b817-d8812850fd42', result)  
        
        self.report.start_uuid('9eef149c-2c99-4edb-8354-52031f2075a9')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('9eef149c-2c99-4edb-8354-52031f2075a9', result)
        
        self.report.start_uuid('a1755927-c4cf-43e2-81b9-49b724b6cb0d')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('a1755927-c4cf-43e2-81b9-49b724b6cb0d', result)        
        
        # GI Sub-All
        self.report.start_uuid('6130fe9b-a2cc-461f-850a-989476efd0a7')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.subscribed)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_all)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6130fe9b-a2cc-461f-850a-989476efd0a7', result)
        
        self.report.start_uuid('3c1bf7d1-51a5-4f7c-a849-4936e0cafe09')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('3c1bf7d1-51a5-4f7c-a849-4936e0cafe09', result)  
        
        self.report.start_uuid('708a3436-8eb8-45b2-b35a-721d94094d4d')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('708a3436-8eb8-45b2-b35a-721d94094d4d', result)
        
        self.report.start_uuid('91f7336d-7ff6-4cdf-b391-5c0fdc34c937')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('91f7336d-7ff6-4cdf-b391-5c0fdc34c937', result)        
        
        # GI Sub-Vertical
        self.report.start_uuid('1e1e3534-36f5-4673-9d05-255465f89a61')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_vertical)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('1e1e3534-36f5-4673-9d05-255465f89a61', result)
        
        self.report.start_uuid('2168ffb0-8209-437e-8571-da85a39bb359')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('2168ffb0-8209-437e-8571-da85a39bb359', result)  
        
        self.report.start_uuid('2671e2ee-37c0-41e3-b1ad-c27fe1c970a6')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('2671e2ee-37c0-41e3-b1ad-c27fe1c970a6', result)
        
        self.report.start_uuid('1c26b504-c280-45e4-a914-ae812b20d228')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('1c26b504-c280-45e4-a914-ae812b20d228', result)        
        
        # GI Sub-horizontal
        self.report.start_uuid('b69c8c3c-65c1-4b4f-92ae-73731fac57e1')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_horizontal)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('b69c8c3c-65c1-4b4f-92ae-73731fac57e1', result)
        
        self.report.start_uuid('7df5f5b2-bb2a-4d7c-b1ce-2f73ff5ab590')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('7df5f5b2-bb2a-4d7c-b1ce-2f73ff5ab590', result)  
        
        self.report.start_uuid('7cd9bf54-c484-4c7b-afd7-bb0909ccbcae')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('7cd9bf54-c484-4c7b-afd7-bb0909ccbcae', result)
        
        self.report.start_uuid('640e14c7-0a86-41c2-9d58-6c70fbe483e8')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('640e14c7-0a86-41c2-9d58-6c70fbe483e8', result)        
        
        # GI Sub-square
        self.report.start_uuid('e4b6902f-4289-41c5-9bc9-7e21b1d21c5c')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_square)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('e4b6902f-4289-41c5-9bc9-7e21b1d21c5c', result)
        
        self.report.start_uuid('e0892c59-d9fe-408b-95ba-b62e1646ffaf')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('e0892c59-d9fe-408b-95ba-b62e1646ffaf', result)  
        
        self.report.start_uuid('59f3fcde-143a-44d5-9528-7a10141d530e')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('59f3fcde-143a-44d5-9528-7a10141d530e', result)
        
        self.report.start_uuid('c23cf26e-fb8b-405b-8eef-83a795e3aa04')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('c23cf26e-fb8b-405b-8eef-83a795e3aa04', result)        
        
        # GI Sub-panoramic
        self.report.start_uuid('d09c9a28-7d52-44cf-91ab-6379f192d2c1')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_panoramic)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('d09c9a28-7d52-44cf-91ab-6379f192d2c1', result)
        
        self.report.start_uuid('92e7f394-0da2-4c4e-abaa-c539ba5e9c5f')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('92e7f394-0da2-4c4e-abaa-c539ba5e9c5f', result)  
        
        self.report.start_uuid('04f6b4fd-19be-4201-af3c-2efc4ff99a1b')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('04f6b4fd-19be-4201-af3c-2efc4ff99a1b', result)
        
        self.report.start_uuid('27c3f9d1-4080-409e-bcec-47c8a8a3bfdd')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('27c3f9d1-4080-409e-bcec-47c8a8a3bfdd', result)
        
        # GI Pay-All
        self.report.start_uuid('913e016f-a751-4ef3-a23c-0bac197f2165')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.pay)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_all)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('913e016f-a751-4ef3-a23c-0bac197f2165', result)
        
        self.report.start_uuid('df19ca93-30ec-4555-9d34-73b877adbc58')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('df19ca93-30ec-4555-9d34-73b877adbc58', result)  
        
        self.report.start_uuid('52a96b91-f217-49ab-b9d9-1b0aee3158fd')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('52a96b91-f217-49ab-b9d9-1b0aee3158fd', result)
        
        self.report.start_uuid('f8ade578-dbde-4aa1-aaab-3cc0a9b97068')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('f8ade578-dbde-4aa1-aaab-3cc0a9b97068', result)        
        
        # GI Pay-Vertical
        self.report.start_uuid('f02aaa69-7659-4a01-a468-a590ed893f47')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_vertical)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('f02aaa69-7659-4a01-a468-a590ed893f47', result)
        
        self.report.start_uuid('9f0a1855-f50d-40eb-97eb-c3ddc975d34d')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('9f0a1855-f50d-40eb-97eb-c3ddc975d34d', result)  
        
        self.report.start_uuid('2bbd5451-c76d-4eae-8ee4-1382b1199bc0')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('2bbd5451-c76d-4eae-8ee4-1382b1199bc0', result)
        
        self.report.start_uuid('70efd1db-dc55-4eaa-ae21-97ac4b4f2f74')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('70efd1db-dc55-4eaa-ae21-97ac4b4f2f74', result)        
        
        # GI Pay-horizontal
        self.report.start_uuid('6f58f4aa-05ec-4295-b175-ad497534f7f1')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_horizontal)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6f58f4aa-05ec-4295-b175-ad497534f7f1', result)
        
        self.report.start_uuid('2b7721a3-0b2a-4534-812d-2dc913b43165')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('2b7721a3-0b2a-4534-812d-2dc913b43165', result)  
        
        self.report.start_uuid('6686b542-17f7-420d-86a7-e8e6e6618baa')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6686b542-17f7-420d-86a7-e8e6e6618baa', result)
        
        self.report.start_uuid('92f1e2b6-b9e7-4c90-be24-a72686748a4a')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('92f1e2b6-b9e7-4c90-be24-a72686748a4a', result)        
        
        # GI Pay-square
        self.report.start_uuid('1f6c0049-6cda-457a-a90c-d3fd1e50f58f')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_square)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('1f6c0049-6cda-457a-a90c-d3fd1e50f58f', result)
        
        self.report.start_uuid('9d63196c-512d-4bf9-a5c8-e5b7f649fffe')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('9d63196c-512d-4bf9-a5c8-e5b7f649fffe', result)  
        
        self.report.start_uuid('a38d93ed-b271-4e7b-b724-eb600a77edc6')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('a38d93ed-b271-4e7b-b724-eb600a77edc6', result)
        
        self.report.start_uuid('6460aa8e-5e24-4e93-be0c-ba52b51729f5')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('6460aa8e-5e24-4e93-be0c-ba52b51729f5', result)        
        
        # GI Pay-panoramic
        self.report.start_uuid('0fb7551e-795a-4809-86fe-43845b6133be')
        pic_base = page_media.get_library_pic()
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.by_panoramic)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.newest)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('0fb7551e-795a-4809-86fe-43845b6133be', result)
        
        self.report.start_uuid('24e5671c-d017-42cd-8fb0-6b18d2b78093')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.best_match)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('24e5671c-d017-42cd-8fb0-6b18d2b78093', result)  
        
        self.report.start_uuid('df9c8887-e3e5-40ed-a6c5-91aa128e0fe9')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.random)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('df9c8887-e3e5-40ed-a6c5-91aa128e0fe9', result)
        
        self.report.start_uuid('a1d9419b-3af1-44d4-8dc8-38b4c1d66c25')
        pic_base = pic_after
        page_media.click(L.import_media.library_gridview.btn_stock_filter)
        time.sleep(3)
        page_media.click(L.import_media.video_entry.sort_menu.most_popular)
        time.sleep(3)
        page_media.back()
        time.sleep(3)
        pic_after = page_media.get_library_pic()
        result = True if not CompareImage(pic_base, pic_after, 7).compare_image() else False
        self.report.new_result('a1d9419b-3af1-44d4-8dc8-38b4c1d66c25', result)
        
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.timeline_setting)
        page_edit.click(L.edit.sub_menu.settings)
        time.sleep(3)
        page_main.sign_out_cyberlink_account()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_06_11_03(self):
        logger('>>> test_sce_06_11_03 : GettyImages Premium for Free User<<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        self.report.start_uuid('b419e32d-cb45-4565-a50b-f18013d45ffe')
        page_main.project_click_new()
        page_main.project_set_name("sce_06_11_01")
        page_main.project_set_16_9()
        time.sleep(5)
        page_media.select_media_by_text('Stock Video')
        # page_media.click(L.import_media.video_library.tab_video_gettyimages)
        page_media.select_stock_category('gettyimage_premium')
        time.sleep(5)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.library_unit_purchasable) else False
        self.report.new_result('b419e32d-cb45-4565-a50b-f18013d45ffe', result)

        self.report.start_uuid('91c89a72-a055-4016-9b01-d25cfb719458')
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Photo')
        # page_media.click(L.import_media.video_library.tab_video_gettyimages)
        page_media.select_stock_category('gettyimage_premium')
        time.sleep(5)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.library_unit_purchasable) else False
        self.report.new_result('91c89a72-a055-4016-9b01-d25cfb719458', result)

        self.report.start_uuid('e769112a-d733-4c66-bc61-9b4c6f3ad9bc')
        page_media.switch_to_video_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Video')
        page_media.select_stock_category('gettyimage_premium')
        time.sleep(5)
        page_media.click(L.import_media.gettyimages_premium.library_unit_purchasable)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.btn_preview_first) else False
        self.report.new_result('e769112a-d733-4c66-bc61-9b4c6f3ad9bc', result)

        self.report.start_uuid('e4660c04-0db2-4af5-aeee-9780ca77c7ab')
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.learn_more) else False
        self.report.new_result('e4660c04-0db2-4af5-aeee-9780ca77c7ab', result)

        self.report.start_uuid('c9eda3fc-d3b1-4a97-bc88-beb02955464e')
        page_media.click(L.import_media.gettyimages_premium.btn_preview_first)
        time.sleep(3)
        result = page_edit.timeline_select_item_by_index_on_track(1, 1)
        self.report.new_result('c9eda3fc-d3b1-4a97-bc88-beb02955464e', result)

        self.report.start_uuid('ee9d52f6-99c4-4a50-a8f6-c5c2e8bf97d7')
        page_media.click(L.edit.try_before_buy.premium_features_used_bubble)
        time.sleep(3)
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.premium_list) else False
        self.report.new_result('ee9d52f6-99c4-4a50-a8f6-c5c2e8bf97d7', result)

        self.report.start_uuid('0240ac6c-970e-47aa-abc3-683705939e77')
        page_edit.back()
        time.sleep(3)
        page_media.click(L.edit.menu.produce)
        time.sleep(3)
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.premium_list) else False
        self.report.new_result('0240ac6c-970e-47aa-abc3-683705939e77', result)

        self.report.start_uuid('e6b41a43-e4cb-47f3-b6e1-0de3e7d32de0')
        result = True if page_edit.is_exist(
            L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_thumbnail) else False
        self.report.new_result('e6b41a43-e4cb-47f3-b6e1-0de3e7d32de0', result)

        self.report.start_uuid('837f54b7-99f5-4b56-bdf6-b39ccddadf98')
        result = True if page_edit.is_exist(
            L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_price) else False
        self.report.new_result('837f54b7-99f5-4b56-bdf6-b39ccddadf98', result)

        self.report.start_uuid('c2247d84-e4d0-4cdb-9518-d28cb3bae5c2')
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.buy_dialog.total_price) else False
        self.report.new_result('c2247d84-e4d0-4cdb-9518-d28cb3bae5c2', result)

        self.report.start_uuid('7debdb38-9b18-4e2b-a0c1-90c1b1723326')
        result = True if page_edit.is_exist(
            L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_footer) else False
        self.report.new_result('7debdb38-9b18-4e2b-a0c1-90c1b1723326', result)

        self.report.start_uuid('16c54aa3-be01-4ff1-9d27-34c27ae6737e')
        page_media.click(L.import_media.gettyimages_premium.buy_dialog.btn_buy)
        time.sleep(10)
        result = True if page_edit.is_exist(L.import_media.gettyimages_premium.btn_googlepay_buy) else False
        self.report.new_result('16c54aa3-be01-4ff1-9d27-34c27ae6737e', result)

        self.report.start_uuid('5893f069-9868-4e6b-94e1-9b482b38f776')
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Photo')
        # page_media.click(L.import_media.video_library.tab_video_gettyimages)
        page_media.select_stock_category('gettyimage_premium')
        time.sleep(5)
        page_media.click(L.import_media.gettyimages_premium.library_unit_purchasable)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        result = True if page_media.is_exist(L.import_media.gettyimages_premium.btn_preview_first) else False
        self.report.new_result('5893f069-9868-4e6b-94e1-9b482b38f776', result)

        self.report.start_uuid('0a94414d-7342-4082-a7ac-09f1ea4d7b99')
        page_media.click(L.import_media.gettyimages_premium.btn_preview_first)
        time.sleep(3)
        result = page_edit.timeline_select_item_by_index_on_track(1, 1)
        self.report.new_result('0a94414d-7342-4082-a7ac-09f1ea4d7b99', result)

        self.report.start_uuid('a9210fa9-9862-43ec-b597-3cb4e6b9eb26')
        page_media.click(L.edit.try_before_buy.premium_features_used_bubble)
        time.sleep(3)
        result = True if page_edit.is_exist(
            L.import_media.gettyimages_premium.buy_dialog.pay_stock_media_price) else False
        self.report.new_result('a9210fa9-9862-43ec-b597-3cb4e6b9eb26', result)
