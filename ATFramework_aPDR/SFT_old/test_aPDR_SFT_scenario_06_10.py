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

class Test_SFT_Scenario_06_10:
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
    def test_sce_06_10_01(self):
        logger('>>> test_sce_06_10_01 : IAP Entry Refinement <<<')
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

        # No Ads
        self.report.start_uuid('e9200c9a-37bc-44de-a10f-adf80d9be04e')
        time.sleep(10)
        page_main.click_no_ads()
        result = page_main.check_iap_highlighted_item('No Ads')
        page_edit.back()
        time.sleep(5)
        self.report.new_result('e9200c9a-37bc-44de-a10f-adf80d9be04e', result)

        # Watermark
        self.report.start_uuid('e9200c9a-37bc-44de-a10f-adf80d9be04e')
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.preview.watermark)
        page_edit.click(L.edit.preview.watermark)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Remove Watermark')
        page_edit.back()
        time.sleep(5)
        self.report.new_result('e9200c9a-37bc-44de-a10f-adf80d9be04e', result)

        self.report.start_uuid('12ab44a4-545e-450e-b704-e9fe236dca23')
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(5)
        page_timeline_settings.tap_remove_watermark()
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Remove Watermark')
        page_edit.back()
        time.sleep(5)
        self.report.new_result('12ab44a4-545e-450e-b704-e9fe236dca23', result)

        # 4K produce
        self.report.start_uuid('e2f90bc6-7772-4c14-af42-73335bed49a2')
        page_timeline_settings.select_default_video_quality('uhd')
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Ultra HD Videos')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit Default Video Quality page
        time.sleep(3)
        page_edit.back()    # Quit Settings page
        time.sleep(3)
        self.report.new_result('e2f90bc6-7772-4c14-af42-73335bed49a2', result)

        self.report.start_uuid('3ecaada1-ca39-460b-a98c-59558ff5b4ee')
        page_edit.click(L.edit.menu.produce)
        time.sleep(5)
        page_produce.select_produce_type('gallery')
        page_produce.set_resolution(0)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Ultra HD Videos')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('3ecaada1-ca39-460b-a98c-59558ff5b4ee', result)

        self.report.start_uuid('f0d13e1d-6b51-4dc9-a582-c5fcc9c112df')
        page_edit.click(L.produce.gallery.btnPurchase)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Ultra HD Videos')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()  # Quit Produce page
        time.sleep(3)
        self.report.new_result('f0d13e1d-6b51-4dc9-a582-c5fcc9c112df', result)

        # Title - Gradient Angle
        self.report.start_uuid('c28f48d6-17b2-41b7-8a99-1bc152803066')
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.select_media_by_text('Default')
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Title Designer')
        time.sleep(3)
        page_edit.click(L.edit.title_designer.tab_gradient)
        page_edit.title_designer.select_color_by_order(5)
        page_edit.title_designer.set_slider(L.edit.title_designer.slider_angle, 0.9)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('c28f48d6-17b2-41b7-8a99-1bc152803066', result)

        self.report.start_uuid('20275784-c58b-4524-9665-a64cba0041f9')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        self.report.new_result('20275784-c58b-4524-9665-a64cba0041f9', result)

        # Title - Gradient transition
        self.report.start_uuid('00770ce0-3644-47af-a9ce-5afb1b10c93f')
        page_edit.title_designer.set_slider(L.edit.title_designer.slider_transition, 0.1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('00770ce0-3644-47af-a9ce-5afb1b10c93f', result)
        
        self.report.start_uuid('9daa49aa-58ea-49c8-92f0-6d3bafe97254')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        self.report.new_result('9daa49aa-58ea-49c8-92f0-6d3bafe97254', result)

        # Title - Premium font
        self.report.start_uuid('a4321e11-adba-45eb-8a7e-3c4ee187ba17')
        page_edit.click(L.edit.title_designer.btn_font)
        time.sleep(1)
        page_edit.title_designer.download_premium_font()
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('a4321e11-adba-45eb-8a7e-3c4ee187ba17', result)

        self.report.start_uuid('34a1b08f-9261-4cbf-bed8-b6b386268ee0')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        self.report.new_result('34a1b08f-9261-4cbf-bed8-b6b386268ee0', result)

        # Title - Border 2
        self.report.start_uuid('32c359ad-85fc-4c2d-8012-9b2847aa32fd')
        page_edit.click(L.edit.title_designer.btn_edit_bolder)
        time.sleep(1)
        page_edit.click(L.edit.title_designer.tab_border2)
        page_edit.title_designer.select_color_by_order(5)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('32c359ad-85fc-4c2d-8012-9b2847aa32fd', result)

        self.report.start_uuid('d1258f29-374c-4345-a5b1-3c91506de653')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.back()    # Quit Title Designer
        time.sleep(3)
        self.report.new_result('d1258f29-374c-4345-a5b1-3c91506de653', result)

        # Title - Backdrop
        self.report.start_uuid('acddf71e-abf3-4418-9a24-13627f7ca354')
        page_edit.select_from_bottom_edit_menu('Backdrop')
        time.sleep(1)
        page_edit.click(L.edit.backdrop.btn_backdrop_enable)
        time.sleep(3)
        page_edit.click(L.edit.backdrop.btn_backdrop_type)
        time.sleep(3)
        page_edit.click(L.edit.backdrop.btn_type_ellipse)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('More Backdrop Shapes')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('acddf71e-abf3-4418-9a24-13627f7ca354', result)

        self.report.start_uuid('4ac716d2-793a-4579-a1d4-cdbef8bef321')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('More Backdrop Shapes')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.back()    # Quit Backdrop page
        time.sleep(3)
        page_edit.click(L.edit.menu.delete)
        time.sleep(3)
        self.report.new_result('4ac716d2-793a-4579-a1d4-cdbef8bef321', result)

        # Effect Layer
        self.report.start_uuid('6a3d84da-5828-43cd-8079-6b4f19e1d166')
        page_edit.click(L.edit.menu.effect)
        page_media.switch_to_effect_layer_library()
        time.sleep(5)
        page_media.select_effect_layer_by_order(1)
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Effect Layer')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('6a3d84da-5828-43cd-8079-6b4f19e1d166', result)

        self.report.start_uuid('51d75c70-aa65-482b-8bee-e8b536ca6a99')
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Effect Layer')
        page_edit.back()  # Quit IAP page
        time.sleep(3)
        page_edit.back()  # Quit used premium feature page
        time.sleep(3)
        self.report.new_result('51d75c70-aa65-482b-8bee-e8b536ca6a99', result)

        self.report.start_uuid('7b0f5aba-8f1b-4769-adf6-69756c09a8da')
        page_edit.select_from_bottom_edit_menu('Type')
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Blur')
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Effect Layer')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()  # Quit used premium feature page
        time.sleep(3)
        page_edit.click(L.edit.menu.delete)
        time.sleep(3)
        self.report.new_result('7b0f5aba-8f1b-4769-adf6-69756c09a8da', result)

        # Transition
        self.report.start_uuid('c89159ca-42d4-4881-affd-c15736855446')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(3)
        page_media.click(L.edit.menu.play)
        time.sleep(3)
        page_media.click(L.edit.menu.play)
        page_edit.select_from_bottom_edit_menu('Split')
        time.sleep(1)
        page_edit.timeline_select_transition_effect()
        time.sleep(1)
        page_edit.select_transition_category('Basic')
        page_edit.select_transition_from_bottom_menu('Zoom Out 01')
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('100+ Transition Effects')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('c89159ca-42d4-4881-affd-c15736855446', result)

        self.report.start_uuid('7bb6113e-fa83-4a74-9213-51538f7e553e')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('100+ Transition Effects')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.back()    # Quit Transition page
        time.sleep(3)
        self.report.new_result('7bb6113e-fa83-4a74-9213-51538f7e553e', result)

        # Audio Denoise
        self.report.start_uuid('1dc178f9-0aa0-4d0f-b1b2-b05d32f298e2')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Audio Tool')
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Denoise')
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Audio Denoise')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('1dc178f9-0aa0-4d0f-b1b2-b05d32f298e2', result)

        self.report.start_uuid('20e46f48-6f06-4460-be32-8db878cdb028')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Audio Denoise')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        self.report.new_result('20e46f48-6f06-4460-be32-8db878cdb028', result)

        # Voice Changer
        self.report.start_uuid('06b5ecfb-6992-4940-9c3b-2ac8abf125d7')
        page_edit.select_from_bottom_edit_menu('Voice Changer')
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Child')
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Voice Changers')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('06b5ecfb-6992-4940-9c3b-2ac8abf125d7', result)

        self.report.start_uuid('70dc252d-d3a6-45ff-9acc-9fb1075a753e')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Voice Changers')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.back()    # Quit Voice Changer page
        time.sleep(3)
        page_edit.back()    # Quit Audio Tool page
        time.sleep(3)
        self.report.new_result('70dc252d-d3a6-45ff-9acc-9fb1075a753e', result)

        # Fit & Fill Background
        self.report.start_uuid('2acc2c3f-b56b-4b4c-8d36-ef1dcc277195')
        page_edit.select_from_bottom_edit_menu('Fit & Fill')
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Background')
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Pattern')
        time.sleep(1)
        page_edit.fit_and_fill.select_pattern_by_order(4)
        time.sleep(10)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Background Pattern')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('2acc2c3f-b56b-4b4c-8d36-ef1dcc277195', result)

        self.report.start_uuid('3cf6110e-8ded-4f37-8c45-14c01cd2bbbb')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Background Pattern')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(3)
        self.report.new_result('3cf6110e-8ded-4f37-8c45-14c01cd2bbbb', result)

        # Video Effect
        self.report.start_uuid('5fcc95a4-cfc4-464a-a9c1-7a1fa6f03602')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Effect')
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Style Pack Vol. 1')
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('X-Ray')
        time.sleep(10)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('40+ Video Effects')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('5fcc95a4-cfc4-464a-a9c1-7a1fa6f03602', result)

        self.report.start_uuid('7243044e-d12a-4749-97d1-c001d4adff3d')
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('40+ Video Effects')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.back()    # Quit Effect page
        time.sleep(3)
        self.report.new_result('7243044e-d12a-4749-97d1-c001d4adff3d', result)

        # Filter
        self.report.start_uuid('c2b8c7a0-9d29-46b3-8cb3-9854f4d13795')
        page_edit.select_from_bottom_edit_menu('Filter')
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Get More')
        time.sleep(10)
        page_edit.click(L.edit.try_before_buy.icon_try)
        time.sleep(5)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('200+ Filters')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('c2b8c7a0-9d29-46b3-8cb3-9854f4d13795', result)

        self.report.start_uuid('ee1bbb24-8346-4f79-8e4d-0ddf7722744b')
        for retry in range(5):
            page_edit.click(L.edit.try_before_buy.icon_try)
            time.sleep(5)
            page_edit.click(L.edit.try_before_buy.btn_notnow)
            time.sleep(3)
            if page_edit.is_exist(L.edit.try_before_buy.btn_ads_sub):
                page_edit.click(L.edit.try_before_buy.btn_ads_sub)
                time.sleep(1)
                break
        result = page_main.check_iap_highlighted_item('200+ Filters')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit Filter Library page
        time.sleep(3)
        page_edit.back()    # Quit Filter page
        time.sleep(3)
        self.report.new_result('ee1bbb24-8346-4f79-8e4d-0ddf7722744b', result)

        # Video Stabilizer
        self.report.start_uuid('b34a06bd-7858-41dc-b49a-4e4bb6d5367d')
        page_edit.select_from_bottom_edit_menu('Stabilizer')
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Video Stabilizer')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('b34a06bd-7858-41dc-b49a-4e4bb6d5367d', result)

        # MGT
        self.report.start_uuid('2ae94871-04c4-440c-9d4d-bf43e040799c')
        page_edit.click(L.edit.menu.effect)
        time.sleep(1)
        page_media.select_title_category('Quote Titles')
        time.sleep(1)
        page_edit.click(L.edit.try_before_buy.icon_try)
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('2ae94871-04c4-440c-9d4d-bf43e040799c', result)

        self.report.start_uuid('d44fd282-5b08-43d3-bd20-915313edf5e8')
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()  # Quit IAP page
        time.sleep(3)
        page_edit.back()  # Quit used premium feature page
        time.sleep(3)
        page_edit.click(L.edit.menu.delete)
        time.sleep(3)
        self.report.new_result('d44fd282-5b08-43d3-bd20-915313edf5e8', result)

        # Video Overlay
        self.report.start_uuid('69a2c475-b8cf-4071-8f07-fbf008692bcd')
        page_edit.click(L.edit.menu.effect)
        page_media.switch_to_overlay_library()
        time.sleep(5)
        page_edit.click(L.edit.try_before_buy.icon_try)
        time.sleep(5)
        page_media.download_video()
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('60+ Overlay Effects')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('69a2c475-b8cf-4071-8f07-fbf008692bcd', result)

        self.report.start_uuid('63ca0323-53d6-4412-9caa-86e9cdc42481')
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('60+ Overlay Effects')
        page_edit.back()  # Quit IAP page
        time.sleep(3)
        page_edit.back()  # Quit used premium feature page
        time.sleep(3)
        page_edit.click(L.edit.menu.delete)
        time.sleep(3)
        self.report.new_result('63ca0323-53d6-4412-9caa-86e9cdc42481', result)

        # Sticker
        self.report.start_uuid('5a76683a-05e3-4d8c-b7ca-162a350e7981')
        page_edit.click(L.edit.menu.effect)
        page_media.switch_to_sticker_library()
        time.sleep(1)
        page_edit.click(L.edit.try_before_buy.icon_try)
        time.sleep(15)
        page_edit.click(L.edit.try_before_buy.icon_try)
        time.sleep(5)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('200+ Stickers')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('5a76683a-05e3-4d8c-b7ca-162a350e7981', result)

        self.report.start_uuid('12504386-1700-489b-9502-9c5054e69e17')
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('200+ Stickers')
        page_edit.back()  # Quit IAP page
        time.sleep(3)
        page_edit.back()  # Quit used premium feature page
        time.sleep(3)
        page_edit.click(L.edit.menu.delete)
        time.sleep(3)
        self.report.new_result('12504386-1700-489b-9502-9c5054e69e17', result)

        # Premium Title Effect
        self.report.start_uuid('34e6684d-98f8-4df2-9849-6b083f994bea')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.effect)
        time.sleep(1)
        page_media.select_title_category('Cool Effect')
        time.sleep(1)
        page_edit.click(L.edit.try_before_buy.icon_try)
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('34e6684d-98f8-4df2-9849-6b083f994bea', result)

        self.report.start_uuid('983044fa-aaa2-4992-a171-012ce315eb4f')
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        self.report.new_result('983044fa-aaa2-4992-a171-012ce315eb4f', result)

        # Premium Title Presets
        self.report.start_uuid('c11bcd29-4c5c-49a4-b6a7-ee83c2e5bb3c')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.effect)
        time.sleep(1)
        page_media.select_title_category('Colorful')
        time.sleep(1)
        page_edit.click(L.edit.try_before_buy.icon_try)
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('c11bcd29-4c5c-49a4-b6a7-ee83c2e5bb3c', result)

        self.report.start_uuid('27fb0d8d-68ca-4c9f-996e-22fa3f9438f6')
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('Customized Title Styles')
        self.report.new_result('27fb0d8d-68ca-4c9f-996e-22fa3f9438f6', result)

        # Title - In Animation
        self.report.start_uuid('7579658b-cbd5-4118-8351-ee5e13f77879')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.select_media_by_text('Default')
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Animation')
        time.sleep(1)
        page_edit.click(L.edit.title_animation.btn_in_animation)
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Hide Down')
        time.sleep(1)
        page_edit.back()    # Quit animation page to trigger TBB
        time.sleep(1)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('7579658b-cbd5-4118-8351-ee5e13f77879', result)

        self.report.start_uuid('f2b10d71-f16d-41a8-9812-eb4ee3e0181d')
        page_edit.click(L.edit.try_before_buy.btn_notnow)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.back()    # Quit Title Designer
        time.sleep(3)
        self.report.new_result('f2b10d71-f16d-41a8-9812-eb4ee3e0181d', result)

        # Title - Out Animation
        self.report.start_uuid('cf26a145-46ce-45ff-b6e0-9507450463cb')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.select_media_by_text('Default')
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Animation')
        time.sleep(1)
        page_edit.click(L.edit.title_animation.btn_out_animation)
        time.sleep(1)
        page_edit.select_from_bottom_edit_menu('Hide Down')
        time.sleep(1)
        page_edit.back()    # Quit animation page to trigger TBB
        time.sleep(1)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('cf26a145-46ce-45ff-b6e0-9507450463cb', result)

        self.report.start_uuid('7d23aff8-f76e-45c1-857c-70cf489d5ac6')
        page_edit.click(L.edit.try_before_buy.btn_notnow)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('80+ Animated Titles')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_delete_premium)   # delete used premium feature
        time.sleep(5)
        page_edit.back()    # Quit Title Designer
        time.sleep(3)
        self.report.new_result('7d23aff8-f76e-45c1-857c-70cf489d5ac6', result)

        # Shutterstock
        self.report.start_uuid('3735bc18-98f2-4571-bfb4-61a7b5cb483a')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.select_media_by_text('Stock Video')
        time.sleep(5)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('3M+ Shutterstock Videos')
        self.report.new_result('3735bc18-98f2-4571-bfb4-61a7b5cb483a', result)

        self.report.start_uuid('31074dd4-baf8-4ebe-89d4-7e670ca0461c')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit TBB page
        time.sleep(3)
        page_edit.back()    # Quit Stock Video page
        time.sleep(3)
        page_media.select_media_by_text('Downloaded')
        time.sleep(3)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('3M+ Shutterstock Videos')
        self.report.new_result('31074dd4-baf8-4ebe-89d4-7e670ca0461c', result)

        self.report.start_uuid('d95fce5a-b11a-475b-8c7a-26a2c7e1b930')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('3M+ Shutterstock Videos')
        self.report.new_result('d95fce5a-b11a-475b-8c7a-26a2c7e1b930', result)

        # Getty Images
        self.report.start_uuid('d99e32e1-dbcb-4bfd-a7f5-eb91caad064b')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.select_media_by_text('Stock Video')
        time.sleep(3)
        page_media.click(L.import_media.video_library.tab_video_gettyimages)
        time.sleep(5)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('900K+ Getty Images Videos')
        self.report.new_result('d99e32e1-dbcb-4bfd-a7f5-eb91caad064b', result)

        self.report.start_uuid('7619faa1-b587-4417-b20e-9c5fd9a263ab')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit TBB page
        time.sleep(3)
        page_edit.back()    # Quit Stock Video page
        time.sleep(3)
        page_media.select_media_by_text('Downloaded')
        time.sleep(3)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('900K+ Getty Images Videos')
        self.report.new_result('7619faa1-b587-4417-b20e-9c5fd9a263ab', result)

        self.report.start_uuid('8a1e24ea-4467-4ef9-a680-972d6d7c6cb8')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('900K+ Getty Images Videos')
        self.report.new_result('8a1e24ea-4467-4ef9-a680-972d6d7c6cb8', result)

        # Shutterstock Photo
        self.report.start_uuid('3bb4829c-b069-4b75-a466-41a8281e292c')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Photo')
        time.sleep(3)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('2M+ Shutterstock Photos')
        self.report.new_result('3bb4829c-b069-4b75-a466-41a8281e292c', result)

        self.report.start_uuid('75344ff7-ba14-4c97-bbb8-cead3a62a7b1')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit TBB page
        time.sleep(3)
        page_edit.back()    # Quit Stock Video page
        time.sleep(3)
        page_media.select_media_by_text('Downloaded')
        time.sleep(3)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('2M+ Shutterstock Photos')
        self.report.new_result('75344ff7-ba14-4c97-bbb8-cead3a62a7b1', result)

        self.report.start_uuid('a871ea79-6dfd-4028-949b-797e0d9e1ba6')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('2M+ Shutterstock Photos')
        self.report.new_result('a871ea79-6dfd-4028-949b-797e0d9e1ba6', result)

        # Getty Images
        self.report.start_uuid('474cf979-4155-4c93-8c4c-34ca735ca2a7')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Photo')
        time.sleep(3)
        page_media.click(L.import_media.video_library.tab_video_gettyimages)
        time.sleep(5)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.download_video()
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('1M+ Getty Images Photos')
        self.report.new_result('474cf979-4155-4c93-8c4c-34ca735ca2a7', result)

        self.report.start_uuid('9bcce1dc-b912-4a2e-aeeb-0bc2bad9cb71')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit TBB page
        time.sleep(3)
        page_edit.back()    # Quit Stock Video page
        time.sleep(3)
        page_media.select_media_by_text('Downloaded')
        time.sleep(3)
        page_media.select_media_by_order(1)
        time.sleep(3)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('1M+ Getty Images Photos')
        self.report.new_result('9bcce1dc-b912-4a2e-aeeb-0bc2bad9cb71', result)

        self.report.start_uuid('8bc84bc1-ce02-4de2-9a8e-65aa7b8e855a')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('1M+ Getty Images Photos')
        self.report.new_result('8bc84bc1-ce02-4de2-9a8e-65aa7b8e855a', result)

        # Shutterstock Music
        self.report.start_uuid('5602427f-ba9c-4309-9000-5cb35fa3e3a2')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_music_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Music')
        time.sleep(3)
        page_media.select_media_by_text('Audio Logos')
        time.sleep(3)
        page_media.select_song_by_text('Action Audio Logo')
        time.sleep(3)
        page_media.download_music()
        page_media.click(L.import_media.library_listview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('5000+ Shutterstock Music')
        self.report.new_result('5602427f-ba9c-4309-9000-5cb35fa3e3a2', result)

        self.report.start_uuid('efd56572-e081-470e-9feb-9461548d44bd')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit TBB page
        time.sleep(3)
        page_edit.back()    # Quit Stock Music Folder
        time.sleep(3)
        page_edit.back()    # Quit Stock Music Page
        time.sleep(3)
        page_media.select_media_by_text('Downloaded')
        time.sleep(3)
        page_media.add_song_to_timeline_by_name('Action Audio Logo.wav')
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('5000+ Shutterstock Music')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        self.report.new_result('efd56572-e081-470e-9feb-9461548d44bd', result)

        self.report.start_uuid('5972959d-f8e1-4931-a6af-f5f734cbae56')
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('5000+ Shutterstock Music')
        self.report.new_result('5972959d-f8e1-4931-a6af-f5f734cbae56', result)

        # CL Music
        self.report.start_uuid('c2b4d563-75d2-473c-8bd4-19e439cf4393')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_music_library()
        time.sleep(5)
        page_media.select_media_by_text('Stock Music')
        time.sleep(3)
        page_media.click(L.import_media.music_library.pdr_tab)
        time.sleep(3)
        page_media.select_media_by_text('Classical')
        time.sleep(3)
        page_media.select_song_by_text('Acceptance')
        time.sleep(3)
        page_media.download_music()
        page_media.click(L.import_media.library_listview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('200+ Music Tracks')
        self.report.new_result('c2b4d563-75d2-473c-8bd4-19e439cf4393', result)

        self.report.start_uuid('fd5b3dfb-018b-4ae6-bde1-afce48dbc1bd')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit TBB page
        time.sleep(3)
        page_edit.back()    # Quit Stock Music Folder
        time.sleep(3)
        page_edit.back()    # Quit Stock Music Page
        time.sleep(3)
        page_media.select_media_by_text('Downloaded')
        time.sleep(3)
        page_media.add_song_to_timeline_by_name('Acceptance.mp3')
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('200+ Music Tracks')
        self.report.new_result('fd5b3dfb-018b-4ae6-bde1-afce48dbc1bd', result)

        self.report.start_uuid('a94c506a-2d76-4480-8d88-ca98bca5adba')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('200+ Music Tracks')
        self.report.new_result('a94c506a-2d76-4480-8d88-ca98bca5adba', result)

        # CL Sound
        self.report.start_uuid('347a7efa-6dfb-4883-9efa-89f861c7b264')
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)  # Need relaunch to show TBB again
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(10)
        page_edit.click(L.edit.menu.import_media)
        page_media.switch_to_sound_clips_library()
        time.sleep(5)
        page_media.select_media_by_text('Animals')
        time.sleep(3)
        page_media.select_song_by_text('Animal drink')
        time.sleep(3)
        page_media.download_music()
        page_media.click(L.import_media.library_listview.add)
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('500+ Sound Effects')
        self.report.new_result('347a7efa-6dfb-4883-9efa-89f861c7b264', result)

        self.report.start_uuid('598fb4c8-0e63-48a8-830d-1e0c3bb94520')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.back()    # Quit TBB page
        time.sleep(3)
        page_edit.back()    # Quit Stock Sound Folder
        time.sleep(3)
        page_media.select_media_by_text('Downloaded')
        time.sleep(3)
        page_media.add_song_to_timeline_by_name('Animal drink.mp3')
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_subtounlock)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('500+ Sound Effects')
        self.report.new_result('598fb4c8-0e63-48a8-830d-1e0c3bb94520', result)

        self.report.start_uuid('0b609ca5-1fcf-48e4-b0ae-c340f8b37ae4')
        page_edit.back()    # Quit IAP page
        time.sleep(3)
        page_edit.click(L.edit.try_before_buy.btn_tryit)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.produce)
        time.sleep(1)
        result = page_main.check_iap_highlighted_item('500+ Sound Effects')
        self.report.new_result('0b609ca5-1fcf-48e4-b0ae-c340f8b37ae4', result)