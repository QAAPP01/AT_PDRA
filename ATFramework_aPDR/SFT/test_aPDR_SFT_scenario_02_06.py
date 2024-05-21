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


pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER


class Test_SFT_Scenario_02_06:
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

    #@pytest.mark.skip
    
    def test_sce_02_06_01(self):
        video_list = ['mp4.mp4']
        self.report.start_uuid('2dc7baec-750d-4dd8-8d61-2d39132e263b')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result('2dc7baec-750d-4dd8-8d61-2d39132e263b', page_edit.check_preview_aspect_ratio(project_title))
        #split clip
        self.report.start_uuid('ed95f627-1912-49e6-b415-dd3315f49eb8')
        self.report.start_uuid('c5a7f413-bad4-4dcc-b2b6-3457d0a0641a')
        page_edit.click(L.edit.timeline.clip)
        page_edit.swipe_element(L.edit.timeline.playhead, "left", 300)        
        #page_edit.click(L.edit.menu.split)
        page_edit.select_from_bottom_edit_menu('Split') 
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 300)
        page_edit.driver.driver.back()
        element = page_edit.timeline_get_split_media(video_list[0], 'Video')
        element.click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.speed).click()
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Speed')
        self.report.new_result('ed95f627-1912-49e6-b415-dd3315f49eb8', page_edit.is_exist(L.edit.speed.slider, 5))
        self.report.new_result('c5a7f413-bad4-4dcc-b2b6-3457d0a0641a', page_edit.is_exist(L.edit.preview.water_mark, 5))
        #set speed as 0.125
        self.report.start_uuid('5fe625f7-ab58-42fc-8f82-008357f06d3a')
        #self.report.start_uuid('f22787bf-7bf6-4fa4-aa3e-7c071f0e0193')
        video_width_base = element.rect['width']
        page_edit.el(L.edit.speed.slider).set_text('2')
        page_edit.el(L.edit.speed.slider).set_text('0')
        time.sleep(3)
        self.report.new_result('5fe625f7-ab58-42fc-8f82-008357f06d3a',page_edit.speed.check_speed_toast_text('0.125'))
        #self.report.new_result('f22787bf-7bf6-4fa4-aa3e-7c071f0e0193', True if page_edit.el(L.edit.speed.mute_audio).get_attribute('selected') == 'true' else False)
        self.report.start_uuid('944a0c80-ded3-464e-af60-789bec9c947f')
        page_edit.speed.set_mute_audio('OFF')
        self.report.new_result('944a0c80-ded3-464e-af60-789bec9c947f',
                               True if page_edit.el(L.edit.speed.mute_audio).get_attribute(
                                   'selected') == 'false' else False)
        self.report.start_uuid('98f3b121-b037-44fc-9098-6ca51ed1cffc')
        #self.report.start_uuid('90cc79d0-5cff-4401-9906-2e0463756d95')
        video_width_curr = element.rect['width']
        self.report.new_result('98f3b121-b037-44fc-9098-6ca51ed1cffc', True if video_width_curr != video_width_base else False)
        #self.report.new_result('90cc79d0-5cff-4401-9906-2e0463756d95', True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        # set speed as 0.50
        self.report.start_uuid('61d743cf-a25d-4918-be13-df17dd7f2537')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('6.0')
        self.report.new_result('61d743cf-a25d-4918-be13-df17dd7f2537', page_edit.speed.check_speed_toast_text('0.50'))
        self.report.start_uuid('e528221b-562c-44b2-90d3-665069a018b2')
        #self.report.start_uuid('1fb50575-5977-4eab-b8a6-2aff2490ff92')
        video_width_curr = element.rect['width']
        self.report.new_result('e528221b-562c-44b2-90d3-665069a018b2',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('1fb50575-5977-4eab-b8a6-2aff2490ff92',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        # set speed as 1.50
        self.report.start_uuid('3ce7d543-b9d0-4452-bf83-7ec8d19df9b2')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('26')
        self.report.new_result('3ce7d543-b9d0-4452-bf83-7ec8d19df9b2', page_edit.speed.check_speed_toast_text('1.50'))
        self.report.start_uuid('67105810-656f-4dc4-9182-b130d90a27f1')
        #self.report.start_uuid('c5b806cc-cbdd-424a-918b-be447e5402a2')
        video_width_curr = element.rect['width']
        self.report.new_result('67105810-656f-4dc4-9182-b130d90a27f1',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('c5b806cc-cbdd-424a-918b-be447e5402a2',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        # set speed as 2.00
        self.report.start_uuid('a76d6079-472b-4628-9840-82e6e8c94372')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('36')
        self.report.new_result('a76d6079-472b-4628-9840-82e6e8c94372', page_edit.speed.check_speed_toast_text('2'))
        self.report.start_uuid('edb6d9de-adf5-4498-a92b-e21b1706fc3a')
        #self.report.start_uuid('20f521d2-0e20-43bc-b8c1-dd5c2eb4f40a')
        video_width_curr = element.rect['width']
        self.report.new_result('edb6d9de-adf5-4498-a92b-e21b1706fc3a',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('20f521d2-0e20-43bc-b8c1-dd5c2eb4f40a',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        # set speed as 4.00
        self.report.start_uuid('445d99e0-ef34-429f-84d2-47127556371d')
        video_width_base = video_width_curr
        page_edit.el(L.edit.speed.slider).set_text('38')
        self.report.new_result('445d99e0-ef34-429f-84d2-47127556371d', page_edit.speed.check_speed_toast_text('4'))
        self.report.start_uuid('3db15e0a-f6db-4f9e-b08d-b1723eb9259d')
        #self.report.start_uuid('5f31c8cd-d9fb-4d4c-8738-c075dd01d05e')
        video_width_curr = page_edit.timeline_get_video_width(video_list[0])
        self.report.new_result('3db15e0a-f6db-4f9e-b08d-b1723eb9259d',
                               True if video_width_curr != video_width_base else False)
        #self.report.new_result('5f31c8cd-d9fb-4d4c-8738-c075dd01d05e',
        #                       True if (not page_edit.check_if_trim_indicator_of_selected_clip()) else False)
        #ease in and out
        self.report.start_uuid('405a9ab6-c844-47fb-af7c-1af8d28abe39')
        page_edit.speed.set_ease_in('ON')
        page_edit.speed.set_ease_out('ON')
        self.report.new_result('405a9ab6-c844-47fb-af7c-1af8d28abe39', True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'true') and
                               (page_edit.el(L.edit.speed.ease_out).get_attribute('selected') == 'true') else False)
        self.report.start_uuid('952f0736-c907-4e24-b09f-716345cafd23')
        page_edit.speed.set_ease_in('ON')
        page_edit.speed.set_ease_out('OFF')
        self.report.new_result('952f0736-c907-4e24-b09f-716345cafd23',
                               True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'true') and
                                       (page_edit.el(L.edit.speed.ease_out).get_attribute(
                                           'selected') == 'false') else False)
        self.report.start_uuid('9ba31d95-19f8-4192-a9da-20128384a1d0')
        page_edit.speed.set_ease_in('OFF')
        page_edit.speed.set_ease_out('ON')
        self.report.new_result('9ba31d95-19f8-4192-a9da-20128384a1d0',
                               True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'false') and
                                       (page_edit.el(L.edit.speed.ease_out).get_attribute(
                                           'selected') == 'true') else False)
        self.report.start_uuid('2b0ce467-86a0-4450-b0d7-a0de6456a99b')
        page_edit.speed.set_ease_in('OFF')
        page_edit.speed.set_ease_out('OFF')
        self.report.new_result('2b0ce467-86a0-4450-b0d7-a0de6456a99b',
                               True if (page_edit.el(L.edit.speed.ease_in).get_attribute('selected') == 'false') and
                                       (page_edit.el(L.edit.speed.ease_out).get_attribute(
                                           'selected') == 'false') else False)
        #preview to check timecode
        self.report.start_uuid('6ec7d5b8-0cf1-4fa1-9fd8-768a3a23f61d')
        page_edit.driver.driver.back()
        #element = page_edit.timeline_get_split_media(video_list[0], 'Video', 1)
        #element.click()
        page_edit.timeline_select_item_by_index_on_track(1, 2)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.speed).click()
        page_edit.select_from_bottom_edit_menu('Speed') 
        time.sleep(5)
        page_edit.el(L.edit.menu.play).click()
        self.report.new_result('6ec7d5b8-0cf1-4fa1-9fd8-768a3a23f61d', page_edit.is_exist(L.edit.timeline.playhead_timecode, 30))
        self.report.start_uuid('8ee02d66-a7f2-4115-878a-83acdc383197')
        #page_edit.driver.driver.back()
        #leave and save project
        page_main.back_to_leave_and_save_project(3)
        self.report.new_result('8ee02d66-a7f2-4115-878a-83acdc383197', True)
