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
test_material_folder = TEST_MATERIAL_FOLDER


class Test_SFT_Scenario_03_06:
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
        self.test_material_folder = test_material_folder
                                                              
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
    def test_sce_03_06_01(self):
        video_list = ['3gp.3GP']
        self.report.start_uuid('539e5679-acaf-493d-b49c-6c07dbb91a15')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result('539e5679-acaf-493d-b49c-6c07dbb91a15', page_edit.check_preview_aspect_ratio(project_title))
        #split clip
        self.report.start_uuid('caf337f9-1324-4f7c-af6d-0f7073d90911')
        self.report.start_uuid('998bc2e1-79ad-4edb-82f5-16a70fc50d87')
        page_edit.click(L.edit.timeline.clip)
        page_edit.swipe_element(L.edit.timeline.playhead, "left", 300)        
        #page_edit.click(L.edit.menu.split)
        page_edit.select_from_bottom_edit_menu('Split') 
        element = page_edit.timeline_get_split_media(video_list[0], 'Video')
        element.click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.speed).click()
        page_edit.select_from_bottom_edit_menu('Speed')
        self.report.new_result('caf337f9-1324-4f7c-af6d-0f7073d90911', page_edit.is_exist(L.edit.speed.slider, 5))
        self.report.new_result('998bc2e1-79ad-4edb-82f5-16a70fc50d87', page_edit.is_exist(L.edit.preview.water_mark, 5))
        #set speed as 0.125
        self.report.start_uuid('1e3a31aa-4a48-4b7f-a473-a21becf3ccd1')
        #self.report.start_uuid('3630a987-f5f9-45a3-8033-94a8b9abe857')
        video_width_base = element.rect['width']
        page_edit.el(L.edit.speed.slider).set_text('2')
        page_edit.el(L.edit.speed.slider).set_text('0')
        time.sleep(1)
        self.report.new_result('1e3a31aa-4a48-4b7f-a473-a21becf3ccd1',page_edit.speed.check_speed_toast_text('0.125'))
        #self.report.new_result('3630a987-f5f9-45a3-8033-94a8b9abe857', True if page_edit.el(L.edit.speed.mute_audio).get_attribute('checked') == 'true' else False)
        self.report.start_uuid('130efa8c-7223-49ce-a486-54e9daa869d6')
        page_edit.speed.set_mute_audio('OFF')
        self.report.new_result('130efa8c-7223-49ce-a486-54e9daa869d6',
                               True if page_edit.el(L.edit.speed.mute_audio).get_attribute(
                                   'selected') == 'false' else False)
        self.report.start_uuid('24d2f7b8-c0cb-4fbc-9b1f-299f453e1a23')
        #self.report.start_uuid('720c7ed3-4183-461f-8f6a-d7f001e772f9')
        video_width_curr = element.rect['width']
        self.report.new_result('24d2f7b8-c0cb-4fbc-9b1f-299f453e1a23', True if video_width_curr != video_width_base else False)
        #self.report.new_result('720c7ed3-4183-461f-8f6a-d7f001e772f9', True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        # set speed as 0.50
        self.report.start_uuid('5e1f52dd-e86c-4b77-ba09-427e2cd6fbc8')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('6.0')
        self.report.new_result('5e1f52dd-e86c-4b77-ba09-427e2cd6fbc8', page_edit.speed.check_speed_toast_text('0.50'))
        self.report.start_uuid('1149348c-35cb-47c5-8045-d1f013034389')
        #self.report.start_uuid('a85fc2ac-25fb-464b-b186-ea425e55e130')
        video_width_curr = element.rect['width']
        self.report.new_result('1149348c-35cb-47c5-8045-d1f013034389',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('a85fc2ac-25fb-464b-b186-ea425e55e130',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        # set speed as 1.50
        self.report.start_uuid('36799ab2-7886-425d-8228-df4b9429b1e7')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('26')
        self.report.new_result('36799ab2-7886-425d-8228-df4b9429b1e7', page_edit.speed.check_speed_toast_text('1.50'))
        self.report.start_uuid('c344b6ef-5fdc-43db-805e-c78c2215b4eb')
        #self.report.start_uuid('c49b131d-18ac-4d46-8085-5a5dbe676142')
        video_width_curr = element.rect['width']
        self.report.new_result('c344b6ef-5fdc-43db-805e-c78c2215b4eb',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('c49b131d-18ac-4d46-8085-5a5dbe676142',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        # set speed as 2.00
        self.report.start_uuid('ac366da7-66c9-4863-be49-ce85cc6008bc')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('36')
        self.report.new_result('ac366da7-66c9-4863-be49-ce85cc6008bc', page_edit.speed.check_speed_toast_text('2'))
        self.report.start_uuid('61095beb-4591-45b0-9f34-2ca2d5122d9e')
        #self.report.start_uuid('3aff10d6-fc3a-4c4c-8c21-b1fc6ad7c8df')
        video_width_curr = element.rect['width']
        self.report.new_result('61095beb-4591-45b0-9f34-2ca2d5122d9e',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('3aff10d6-fc3a-4c4c-8c21-b1fc6ad7c8df',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip())  else False)
        # set speed as 4.00
        self.report.start_uuid('c5ac107c-94b3-4aa2-8cc5-1d1d9739596e')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('38')
        self.report.new_result('c5ac107c-94b3-4aa2-8cc5-1d1d9739596e', page_edit.speed.check_speed_toast_text('4'))
        self.report.start_uuid('ce2d00b0-5b2c-4ede-94c6-6716b09c3367')
        #self.report.start_uuid('d87c6263-80c7-4ee0-8cdf-bdbf60588706')
        video_width_curr = page_edit.timeline_get_video_width(video_list[0])
        self.report.new_result('ce2d00b0-5b2c-4ede-94c6-6716b09c3367',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('d87c6263-80c7-4ee0-8cdf-bdbf60588706',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        #ease in and out
        self.report.start_uuid('8d7d9448-cedf-4ca8-8055-8a43e755c932')
        page_edit.speed.set_ease_in('ON')
        page_edit.speed.set_ease_out('ON')
        self.report.new_result('8d7d9448-cedf-4ca8-8055-8a43e755c932', True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'true') and
                               (page_edit.el(L.edit.speed.ease_out).get_attribute('selected') == 'true') else False)
        self.report.start_uuid('3be64053-3425-42ae-90fb-081a62cd4210')
        page_edit.speed.set_ease_in('ON')
        page_edit.speed.set_ease_out('OFF')
        self.report.new_result('3be64053-3425-42ae-90fb-081a62cd4210',
                               True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'true') and
                                       (page_edit.el(L.edit.speed.ease_out).get_attribute(
                                           'selected') == 'false') else False)
        self.report.start_uuid('f93478f8-6505-4a81-9baa-9d52346c49a0')
        page_edit.speed.set_ease_in('OFF')
        page_edit.speed.set_ease_out('ON')
        self.report.new_result('f93478f8-6505-4a81-9baa-9d52346c49a0',
                               True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'false') and
                                       (page_edit.el(L.edit.speed.ease_out).get_attribute(
                                           'selected') == 'true') else False)
        self.report.start_uuid('a1f7e375-1f63-426b-be05-d6518434f0a5')
        page_edit.speed.set_ease_in('OFF')
        page_edit.speed.set_ease_out('OFF')
        self.report.new_result('a1f7e375-1f63-426b-be05-d6518434f0a5',
                               True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'false') and
                                       (page_edit.el(L.edit.speed.ease_out).get_attribute(
                                           'selected') == 'false') else False)
        #preview to check timecode
        self.report.start_uuid('b354527d-bd73-4fc2-b9af-1c3fae1cbc60')
        page_edit.driver.driver.back()
        #element = page_edit.timeline_get_split_media(video_list[0], 'Video', 1)
        #element.click()
        page_edit.timeline_select_item_by_index_on_track(1, 2)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.speed).click()
        page_edit.select_from_bottom_edit_menu('Speed')
        time.sleep(5)
        page_edit.el(L.edit.menu.play).click()
        self.report.new_result('b354527d-bd73-4fc2-b9af-1c3fae1cbc60', page_edit.is_exist(L.edit.timeline.playhead_timecode, 30))
        self.report.start_uuid('b59ea12d-b16d-4823-bde6-7bda2917035e')
        #page_edit.driver.driver.back()
        #leave and save project
        page_main.back_to_leave_and_save_project(3)
        self.report.new_result('b59ea12d-b16d-4823-bde6-7bda2917035e', True)
    
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_06_02(self):
        video_list = ['3gp.3GP']

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

        self.report.start_uuid('dddbbcac-44ab-466a-a336-02baf372eac5')
        page_edit.click(L.edit.timeline.clip)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        time.sleep(10)
        page_media.click(L.edit.effect_sub.video)
        time.sleep(5)
        page_media.select_media_by_text(test_material_folder)
        page_media.select_media_by_text('mp4.mp4')
        time.sleep(5)
        page_media.click(L.import_media.library_gridview.add)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Speed')
        time.sleep(5)
        value = page_edit.get_opacity_value()
        self.report.new_result('dddbbcac-44ab-466a-a336-02baf372eac5', True if value == '1.00x' else False)
        
        self.report.start_uuid('9026b23c-3b2c-458d-bd02-170d88e24556')
        page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(5)
        value = page_edit.get_opacity_value()
        self.report.new_result('9026b23c-3b2c-458d-bd02-170d88e24556', True if value == '0.125x' else False)        
                
        self.report.start_uuid('1e846d45-25ad-4d81-8544-3b439554c89f')
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        value = page_edit.get_opacity_value()
        self.report.new_result('1e846d45-25ad-4d81-8544-3b439554c89f', True if value == '8x' else False)        
        
        # Mute
        self.report.start_uuid('26db2f94-d439-4112-898c-691769265003')
        result = page_edit.check_bottom_edit_menu_select_status('Mute')
        self.report.new_result('26db2f94-d439-4112-898c-691769265003', True if result == 'false' else False)  
        
        self.report.start_uuid('624e9789-c1e2-4d8f-8718-04f51b113b6e3')
        page_edit.select_from_bottom_edit_menu('Mute')
        result = page_edit.check_bottom_edit_menu_select_status('Mute')
        self.report.new_result('624e9789-c1e2-4d8f-8718-04f51b113b6e', True if result == 'true' else False)         
        
        # Keep Pitch
        self.report.start_uuid('c521b517-5913-4694-b67b-22fd6e337ec7')
        result = page_edit.check_bottom_edit_menu_select_status('Keep Pitch')
        self.report.new_result('c521b517-5913-4694-b67b-22fd6e337ec7', True if result == 'false' else False)  
        
        self.report.start_uuid('889d8eca-ab4e-4d85-98d5-3ffd69ddebeb')
        page_edit.select_from_bottom_edit_menu('Keep Pitch')
        result = page_edit.check_bottom_edit_menu_select_status('Keep Pitch')
        self.report.new_result('889d8eca-ab4e-4d85-98d5-3ffd69ddebeb', True if result == 'true' else False)       
        
        # Ease In
        self.report.start_uuid('8b805359-d509-4b5d-86e9-a8852ea5564c')
        result = page_edit.check_bottom_edit_menu_select_status('Ease In')
        self.report.new_result('8b805359-d509-4b5d-86e9-a8852ea5564c', True if result == 'false' else False)  
        
        self.report.start_uuid('51def8b6-57c7-4c2c-bcc5-f35d60433971')
        page_edit.select_from_bottom_edit_menu('Ease In')
        result = page_edit.check_bottom_edit_menu_select_status('Ease In')
        self.report.new_result('51def8b6-57c7-4c2c-bcc5-f35d60433971', True if result == 'true' else False) 
        
        # Ease Out
        self.report.start_uuid('1068cdd1-9068-4207-af25-ad2ee23de581')
        result = page_edit.check_bottom_edit_menu_select_status('Ease Out')
        self.report.new_result('1068cdd1-9068-4207-af25-ad2ee23de581', True if result == 'false' else False)  
        
        self.report.start_uuid('3254c3d0-3e29-42bc-bcd0-ab3986024d76')
        page_edit.select_from_bottom_edit_menu('Ease Out')
        result = page_edit.check_bottom_edit_menu_select_status('Ease Out')
        self.report.new_result('3254c3d0-3e29-42bc-bcd0-ab3986024d76', True if result == 'true' else False)        
        



