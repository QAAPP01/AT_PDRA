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


class Test_SFT_Scenario_02_05:
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

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_05_01(self):
        self.report.start_uuid('9f03b46b-b52d-4a19-b03b-e28edd3c0438')
        media_list = ['(255, 153, 204)', '(253, 198, 137)', '01_static.mp4', 'png.png', 'aac.aac']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result('9f03b46b-b52d-4a19-b03b-e28edd3c0438',
                               page_edit.check_preview_aspect_ratio(project_title))
        # add 2 color boards to timeline
        self.report.start_uuid('ce063c0e-6ff1-4753-add1-21603aabf351')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.import_media).click()
        page_edit.el(L.import_media.menu.photo_entry).click()
        page_media.select_media_by_text('Color Board')
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        x_axis_timeline_indicator = int(page_edit.el(L.edit.timeline.playhead).rect['x'])
        result_1 = True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(1, 1).rect['x']) else False
        #page_media.select_media_by_text(media_list[1])
        page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        result_2 = True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(1, 2).rect['x']) else False
        self.report.new_result('ce063c0e-6ff1-4753-add1-21603aabf351', True if result_1 and result_2 else False)
        # reposition of color board
        self.report.start_uuid('49da0270-b083-4907-930a-39ccf3fd23e1')
        page_edit.timeline_select_item_by_index_on_track(1, 2)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        el_target = page_edit.timeline_get_item_by_index_on_track(1, 2)
        page_edit.timeline_drag_item(el_target, -400)
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('49da0270-b083-4907-930a-39ccf3fd23e1',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # edit color properties
        self.report.start_uuid('2f848a29-a8bd-4e15-b9d9-3ffda723a873')
        self.report.new_result('2f848a29-a8bd-4e15-b9d9-3ffda723a873', page_edit.is_exist(L.edit.edit_sub.bottom_edit_menu))
        self.report.start_uuid('a8bc63a7-98c7-4a8f-806f-4b2483ed98f3')
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color_selector).click()
        page_edit.select_from_bottom_edit_menu('Color Selector')
        time.sleep(2)
        page_edit.color_selector.set_red_number(0)
        page_edit.color_selector.set_green_number(255)
        page_edit.color_selector.set_blue_number(230)
        page_edit.driver.driver.back()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('a8bc63a7-98c7-4a8f-806f-4b2483ed98f3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('ad6e2460-9ab3-4253-896e-fa3c88d6aafe')
        page_edit.timeline_select_item_by_index_on_track(1, 2)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> [Duplicate] Color Board
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        time.sleep(1)
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        self.report.new_result('ad6e2460-9ab3-4253-896e-fa3c88d6aafe',  result)
        self.report.start_uuid('ed585b19-f1ef-41ec-b0d2-5ce6aa1fb3e3')
        #page_edit.el(L.edit.edit_sub.duplicate).click()       
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('ed585b19-f1ef-41ec-b0d2-5ce6aa1fb3e3',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        # preview full screen
        # self.report.start_uuid('c947799e-17fa-43c6-a40a-b5bbf0f13d4b')
        # time.sleep(2)
        # page_edit.enter_fullscreen_preview()
        # page_edit.click(L.edit.preview.movie_view)
        # time.sleep(1)
        # page_edit.tap_screen_center()
        # self.report.new_result('c947799e-17fa-43c6-a40a-b5bbf0f13d4b',
        #                        page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        # time.sleep(8)
        # self.report.start_uuid('cf96ee5a-8ff0-4d43-92f1-65e1ca58501a')
        # self.report.new_result('cf96ee5a-8ff0-4d43-92f1-65e1ca58501a',
        #                        page_edit.is_exist(L.edit.preview.water_mark))
        # self.report.start_uuid('90a3e3c4-6666-45a8-93ab-381ab380c0c2')
        # x_axis_center = int(page_edit.driver.driver.get_window_size()['width'] / 2)
        # y_axis_center = int(page_edit.driver.driver.get_window_size()['height'] / 2)
        # self.report.new_result('90a3e3c4-6666-45a8-93ab-381ab380c0c2',
        #                        True if page_edit.get_screen_pixel_rgb(x_axis_center - 50,
        #                                                               y_axis_center - 50) == (
        #                                0, 255, 230) else False)
        # page_edit.driver.driver.back()
        # time.sleep(1)
        # ==================================
        self.report.start_uuid('c87c97c4-9052-4b29-9179-2d36ad87335a')
        # page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> [Duplicate] Video
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_video_library()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[2])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        self.report.new_result('c87c97c4-9052-4b29-9179-2d36ad87335a', result)
        self.report.start_uuid('6aefdca2-1855-4235-ba55-888895ab7c69')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('6aefdca2-1855-4235-ba55-888895ab7c69',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('f3f8d1cb-b35a-414b-858b-0cb3fa44ceaf')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> [Duplicate] Photo
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[3])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        self.report.new_result('f3f8d1cb-b35a-414b-858b-0cb3fa44ceaf',result)
        self.report.start_uuid('f8927a1f-5b33-48f3-bb24-4c04d8584287')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('f8927a1f-5b33-48f3-bb24-4c04d8584287',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('b264cf0a-7577-4e27-a5c1-621e740f34c6')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> [Duplicate] Title
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        #page_edit.driver.swipe_left()
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        self.report.new_result('b264cf0a-7577-4e27-a5c1-621e740f34c6',result)
        self.report.start_uuid('5cedabac-32bd-4874-94f2-3d1597bb278c')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('5cedabac-32bd-4874-94f2-3d1597bb278c',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('0716b728-1a89-48ec-a13c-5e37e33447ff')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> [Duplicate] Music
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_music_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_song_by_text(media_list[4])
        page_media.add_selected_song_to_timeline()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead, 'left', 200)
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(3, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.split).click()
        page_edit.select_from_bottom_edit_menu('Split')    
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(3, 2)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(3, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        self.report.new_result('0716b728-1a89-48ec-a13c-5e37e33447ff', result)
        self.report.start_uuid('dcec3cb0-8751-4d5d-82d7-a7e6f444bba1')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        el_object = page_edit.timeline_get_item_by_index_on_track(3, 1, 'title')
        self.report.new_result('dcec3cb0-8751-4d5d-82d7-a7e6f444bba1',
                               True if el_object.text == media_list[4] else False)
        # leave and save project
        self.report.start_uuid('ee45a2e5-dc42-4766-8bc8-feafa75fbfed')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(1)
        el_object = page_edit.timeline_get_item_by_index_on_track(3, 1, 'title')
        self.report.new_result('ee45a2e5-dc42-4766-8bc8-feafa75fbfed',
                               True if el_object.text == media_list[4] else False)

