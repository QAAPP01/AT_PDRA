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


class Test_SFT_Scenario_03_05:
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
    def test_sce_03_05_01(self):
        self.report.start_uuid('69f155ae-d39d-40fe-a864-9697ece6835d')
        media_list = ['(255, 153, 204)', '(253, 198, 137)', '01_static.mp4', 'png.png', 'aac.aac']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result('69f155ae-d39d-40fe-a864-9697ece6835d',
                               page_edit.check_preview_aspect_ratio(project_title))
        # add 2 color boards to timeline
        self.report.start_uuid('3e3030e9-b4f7-436e-9a59-7ab991a2a1a3')
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
        self.report.new_result('3e3030e9-b4f7-436e-9a59-7ab991a2a1a3', True if result_1 and result_2 else False)
        # reposition of color board
        self.report.start_uuid('c8212652-5df3-44b8-bf2d-7505cc6b0456')
        self.report.start_uuid('30e05e2e-8637-4fce-aea6-b377679f95e0')
        page_edit.timeline_select_item_by_index_on_track(1, 2)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        el_target = page_edit.timeline_get_item_by_index_on_track(1, 2)
        page_edit.timeline_drag_item(el_target, -400)
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c8212652-5df3-44b8-bf2d-7505cc6b0456',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # edit color properties
        self.report.new_result('30e05e2e-8637-4fce-aea6-b377679f95e0', page_edit.is_exist(L.edit.edit_sub.bottom_edit_menu))
        self.report.start_uuid('28cb23d4-de27-4cba-af4c-65830d95fcc2')
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
        self.report.new_result('28cb23d4-de27-4cba-af4c-65830d95fcc2',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('1c68fa61-0c4b-4f62-bb12-7a1470da721c')
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
        self.report.new_result('1c68fa61-0c4b-4f62-bb12-7a1470da721c', result)
        self.report.start_uuid('e4c50e25-c143-419b-9f90-bd2c49f6b8e4')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e4c50e25-c143-419b-9f90-bd2c49f6b8e4',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        # preview full screen
        self.report.start_uuid('1653a68b-dc29-4d4c-96f7-1b9838f1511f')
        time.sleep(2)
        page_edit.enter_fullscreen_preview()
        time.sleep(1)
        page_edit.tap_screen_center()
        self.report.new_result('1653a68b-dc29-4d4c-96f7-1b9838f1511f',
                               page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        self.report.start_uuid('3cd7ef9f-11cd-4ed1-bef0-227384a2187b')
        time.sleep(8)
        self.report.new_result('3cd7ef9f-11cd-4ed1-bef0-227384a2187b',
                               page_edit.is_exist(L.edit.preview.water_mark))
        self.report.start_uuid('28abfe02-af6b-4afb-a951-975529792584')
        x_axis_center = int(page_edit.driver.driver.get_window_size()['width'] / 2)
        y_axis_center = int(page_edit.driver.driver.get_window_size()['height'] / 2)
        self.report.new_result('28abfe02-af6b-4afb-a951-975529792584',
                               True if page_edit.get_screen_pixel_rgb(x_axis_center,
                                                                      y_axis_center) == (0, 255, 230) else False)
        page_edit.driver.driver.back()
        time.sleep(1)
        # ==================================
        self.report.start_uuid('b963da75-1bdb-4044-81e9-c536e455ab5e')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
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
        self.report.new_result('b963da75-1bdb-4044-81e9-c536e455ab5e', result)
        self.report.start_uuid('357214f0-30ac-4594-8fd8-cd9a5889f0b4')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('357214f0-30ac-4594-8fd8-cd9a5889f0b4',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('55e12fd0-ecc4-4f3d-ba9a-dce9c8fc8057')
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
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        self.report.new_result('55e12fd0-ecc4-4f3d-ba9a-dce9c8fc8057', result)
        self.report.start_uuid('9b18263e-22fd-43f0-828e-d29b0ed5e6fe')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9b18263e-22fd-43f0-828e-d29b0ed5e6fe',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               2).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('7d9e51d8-3688-49b5-a4e2-3d5f1e6b8e51')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> [Duplicate] Title
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        result = page_edit.select_from_bottom_edit_menu('Duplicate')
        self.report.new_result('7d9e51d8-3688-49b5-a4e2-3d5f1e6b8e51', result)
        self.report.start_uuid('9227566d-ddf3-4437-b2b7-1f373b163710')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9227566d-ddf3-4437-b2b7-1f373b163710',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('cfbc6f72-4ec5-4101-af09-260e454fea3f')
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
        self.report.new_result('cfbc6f72-4ec5-4101-af09-260e454fea3f', result)
        self.report.start_uuid('b88db42c-ed7a-4940-9d77-a58985ceb9c4')
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        el_object = page_edit.timeline_get_item_by_index_on_track(3, 1, 'title')
        self.report.new_result('b88db42c-ed7a-4940-9d77-a58985ceb9c4', True if el_object.text == media_list[4] else False)
        # leave and save project
        self.report.start_uuid('81198a63-b637-4938-be51-c241f092cdd1')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(1)
        el_object = page_edit.timeline_get_item_by_index_on_track(3, 1, 'title')
        self.report.new_result('81198a63-b637-4938-be51-c241f092cdd1',
                               True if el_object.text == media_list[4] else False)

