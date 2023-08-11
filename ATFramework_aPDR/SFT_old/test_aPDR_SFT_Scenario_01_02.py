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


class Test_SFT_Scenario_01_02:
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

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_01(self):
        # create new project > set aspect ratio
        udid = ['c2420360-95d7-4591-afbc-33ae908c62f0', '8522a2ed-042c-4da4-bed6-8fb2512a6b2b',
                '23c3f114-a298-47db-8532-104790d36694']
        video_list = ['mp4.mp4', '3gp.3GP', 'slow_motion.mp4', 'mkv.mkv']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        self.report.new_result(udid[0], page_main.project_check_default_project_name())
        self.report.start_uuid(udid[1])
        page_main.project_set_name("01_02_01")
        page_main.project_set_9_16()
        self.report.new_result(udid[1], page_main.check_edit_mode_ready())
        #add a video to timeline
        self.report.start_uuid(udid[2])
        page_media.switch_to_video_library()
        # add 1st media
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(video_list[0])
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_check_media(video_list[0])
        # check project auto save
        page_media.el(L.import_media.menu.back).click()
        page_media.el(L.import_media.menu.back).click()
        page_edit.el(L.edit.menu.back).click()
        page_produce.ad.close_opening_ads()
        time.sleep(5)
        self.report.new_result(udid[2], page_main.check_existed_project_by_title("01_02_01"))
        page_main.select_existed_project_by_title("01_02_01")


    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_02(self):
        udid = ['dd7500a6-e070-48ec-b3bf-68fb668bca80', '343131de-0a4c-4e60-9bba-a1a8f694c7d4',
                '3c73bac0-4dd1-4850-9d6f-4433fa65f6be']
        media_list = ['gif.gif', 'png.png', 'jpg.jpg', 'bmp.bmp']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        page_main.project_set_name("01_02_02")
        page_main.project_set_9_16()
        time.sleep(5)
        page_media.switch_to_photo_library()
        self.report.new_result(udid[0], page_media.check_element_not_exists(L.import_media.photo_entry.sort))
        # enter folder > PDRa_Testing_Material
        self.report.start_uuid(udid[1])
        page_media.select_media_by_text(self.test_material_folder)
        self.report.new_result(udid[1], page_media.check_element_exists(L.import_media.photo_entry.sort))
        # check default sorting is by date and descending
        self.report.start_uuid(udid[2])
        page_media.click(L.import_media.photo_entry.sort)
        if page_media.is_element_checked(L.import_media.photo_entry.sort_menu.by_date):
            if page_media.is_element_checked(L.import_media.photo_entry.sort_menu.descending):
                self.report.new_result(udid[2], True)
            else:
                self.report.new_result(udid[2], False)
        else:
            self.report.new_result(udid[2], False)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_03(self):
        # add 4 photo to timeline
        udid = ['d77ca83a-8d01-481a-a8f8-0fbe74bdead7', 'e7f30451-f1cd-4044-8d0a-ecd0426ed9c5',
                '536fdf94-419c-4e46-bd0f-74867fbcfb3b', 'a1b97f8a-3300-41f7-b4a4-942fbb40c3d1',
                '5379c7a2-0041-47ff-a12d-a861a972cbc9', 'd083ff85-3ea6-4b05-b8c7-076dc88ff9bd',
                '79c8d498-352b-41bd-88bb-a638cd3b277b', '0acd0622-1ada-4e6c-8413-f54537b22d79']
        media_list = ['gif.gif', 'bmp.bmp', 'jpg.jpg', 'png.png' ]
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        page_main.project_set_name('01_02_03')
        page_main.project_set_9_16()
        
        page_media.el(L.import_media.menu.back).click()
        # Set Pan Zoom [ON]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('ON')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        time.sleep(5)
        page_media.switch_to_photo_library()
        # A. add 4 photo to timeline ====================
        index = 0
        index_media = 0
        for media in media_list:
            # PartI: check add media to timeline
            self.report.start_uuid(udid[index])
            page_media.select_media_by_text(self.test_material_folder)
            #page_media.select_media_by_text(media_list[index_media])
            page_media.select_media_by_order(index_media+1)
            page_media.el(L.import_media.library_gridview.add).click()
            self.report.new_result(udid[index], page_edit.timeline_check_media(media_list[index_media], 'Photo'))
            # Part II: check Pan/ Zoom [ON]
            self.report.start_uuid(udid[index+1])
            page_edit.timeline_select_media(media_list[index_media], 'Photo')
            pic_before = page_edit.get_preview_pic()
            el_playback = page_edit.el(L.edit.menu.play)
            el_playback.click()
            time.sleep(10)
            pic_after = page_edit.get_preview_pic()
            self.report.new_result(udid[index+1], (
                lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                               9).compare_image() == False else False)(
                pic_before, pic_after))
            page_edit.el(L.edit.menu.back).click()
            page_edit.el(L.edit.menu.import_media).click()
            time.sleep(5)
            page_media.switch_to_photo_library()
            index += 2
            index_media += 1
        # B. add 3 videos to timeline ============================
        udid = ['39b042b6-26d2-4730-b738-f02121f1862e', '22b27d9e-e0b7-4f95-b27b-7824132587b4',
                '3170f572-9bc6-4dbd-93db-4326054b3d76']
        media_list = ['slow_motion.mp4', 'mp4.mp4', '3gp.3GP']
        page_media.switch_to_video_library()
        page_media.select_media_by_text(self.test_material_folder)
        index = 0

        for media in media_list:
            self.report.start_uuid(udid[index])
            #page_media.select_media_by_text(media_list[index])
            page_media.select_media_by_order(index+1)
            page_media.el(L.import_media.library_gridview.add).click()
            self.report.new_result(udid[index], page_edit.timeline_check_media(media_list[index], 'Video'))
            index += 1


    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_04(self):
        # Sorting in Photo Library
        udid = ['33656e1b-fffb-45f6-85b3-f10b0d58bede', '67aefd21-d3c7-42bf-9106-16d71158881e',
                '4c7b42e4-6582-4d80-abe3-496ae6cb6591', '75b42e34-7a0e-4ec0-befc-c78fa42119a2',
                '6f5f3752-df90-4614-83ca-2f9270ac0729', 'ddd8f772-876d-449b-9720-558b6af64796',
                'd8c6c9c0-4ce1-449c-819a-3a7fb28ca1eb', '8ea70fc8-3387-4078-b199-e09757399aa2',
                '4bd10d48-6e33-478a-9cc1-20a70e22cb98']
        material_list = ['bmp.bmp', 'jpg.jpg', 'gif.gif', 'png.png']
        self.report.start_uuid(udid[8])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("01_02_04")
        page_main.project_set_9_16()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        time.sleep(5)
        page_media.switch_to_photo_library()
        # enter folder > PDRa_Testing_Material
        page_media.select_media_by_text(self.test_material_folder)
        page_media.click(L.import_media.photo_entry.sort)
        # case 0: check no 'Duration' in menu
        self.report.new_result(udid[8], page_media.is_not_exist(L.import_media.photo_entry.sort_menu.by_duration))
        # case 1: (Ascending) By Name
        self.report.start_uuid(udid[0])
        page_media.click(L.import_media.photo_entry.sort_menu.by_name)
        page_media.click(L.import_media.photo_entry.sort_menu.ascending)
        page_media.driver.driver.back()
        self.report.new_result(udid[0], page_media.photo_list_check_item(material_list[0], material_list[1]))
        # case 2: (Ascending) By Date
        self.report.start_uuid(udid[1])
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_date)
        page_media.driver.driver.back()
        self.report.new_result(udid[1], page_media.photo_list_check_item(material_list[0], material_list[1]))
        # case 3: (Ascending) By Resolution
        self.report.start_uuid(udid[2])
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_resolution)
        page_media.driver.driver.back()
        self.report.new_result(udid[2], page_media.photo_list_check_item(material_list[2], material_list[1]))
        # case 4: (Ascending) By File size
        self.report.start_uuid(udid[3])
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_filesize)
        page_media.driver.driver.back()
        self.report.new_result(udid[3], page_media.photo_list_check_item(material_list[1], material_list[2]))
        # case 5: (Descending) By Name
        self.report.start_uuid(udid[4])
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_name)
        page_media.click(L.import_media.photo_entry.sort_menu.descending)
        page_media.driver.driver.back()
        self.report.new_result(udid[4], page_media.photo_list_check_item(material_list[3], material_list[2]))
        # case 6: (Descending) By Date
        self.report.start_uuid(udid[5])
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_date)
        page_media.driver.driver.back()
        self.report.new_result(udid[5], page_media.photo_list_check_item(material_list[2], material_list[3]))
        # case 7: (Descending) By Resolution
        self.report.start_uuid(udid[6])
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_resolution)
        page_media.driver.driver.back()
        self.report.new_result(udid[6], page_media.photo_list_check_item(material_list[3], material_list[0]))
        # case 8: (Descending) By File size
        self.report.start_uuid(udid[7])
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_filesize)
        page_media.driver.driver.back()
        self.report.new_result(udid[7], page_media.photo_list_check_item(material_list[3], material_list[0]))
        # set back to default by Descending + Date
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_date)
        page_media.click(L.import_media.photo_entry.sort_menu.descending)
        page_media.driver.driver.back()

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_05(self):
        # create new project > set aspect ratio
        udid = ['f9c26adf-1a64-4799-8677-f0c4a62a1d2f', '850789d6-bd74-41e1-a831-077978e02b13']
        media_list = ['jpg.jpg', 'png.png']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        page_main.project_set_name("01_02_05")
        page_main.project_set_9_16()
        page_media.el(L.import_media.menu.back).click()
        # Part I - Pan Zoom [ON]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('ON')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        time.sleep(5)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        # snapshot > preview > snapshot > check diff.
        pic_before = page_edit.get_preview_pic()
        el_playback = page_edit.el(L.edit.menu.play)
        el_playback.click()
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result(udid[0], (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 3).compare_image() == False else False)(
            pic_before, pic_after))
        # Part II - Pan Zoom [OFF]
        self.report.start_uuid(udid[1])
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('OFF')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        time.sleep(5)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[1])
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.timeline_select_media(media_list[1], 'Photo')
        page_edit.timeline_select_item_by_index_on_track(1, 2)
        # snapshot > preview > snapshot > check diff.
        pic_before = page_edit.get_preview_pic()
        el_playback = page_edit.el(L.edit.menu.play)
        el_playback.click()
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result(udid[1], CompareImage(pic_before, pic_after, 3).compare_image())

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_06(self):
        udid = ['7b1f6785-307a-43e9-a0a5-4393a2b4af17', '97f9dc96-6a54-4867-936c-54d221e06a1c']
        material_list = ['wav.wav', 'mp3.mp3', 'm4a.m4a', 'aac.aac']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        page_main.project_set_name("01_02_06")
        page_main.project_set_9_16()
        page_media.switch_to_music_library()
        # enter google drive
        result_google_drive = page_media.enter_google_drive("Music",len(material_list) )
        self.report.new_result(udid[0], result_google_drive)
        
        # download files
        self.report.start_uuid(udid[1])
        result_download_file = page_media.google_download_file()
        self.report.new_result(udid[1],result_download_file)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_07(self):
        # create new project > set aspect ratio
        udid = ['0ad5f14b-946f-4668-a3e1-11e24e4883d0', 'df45dd97-c0c2-47cc-9ac1-cf7d473a06b9', # default image duration
                '810a5752-cfdb-4847-a7cc-f5374ef7a832']
        media_list = ['bmp.bmp', 'jpg.jpg', 'gif.gif', 'png.png']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        page_main.project_set_name("01_02_07")
        page_main.project_set_9_16()
        page_main.el(L.import_media.menu.back).click()
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        # case 1: default image duration - 5.0s (default)
        self.report.new_result(udid[0], page_timeline_settings.check_settings_default_image_duration('5.0'))
        self.report.start_uuid(udid[1])
        page_edit.el(L.timeline_settings.settings.back).click()
        # ---- add photo to timeline - bmp
        page_edit.el(L.edit.menu.import_media).click()
        time.sleep(5)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.click(L.import_media.photo_entry.sort)
        page_media.click(L.import_media.photo_entry.sort_menu.by_date)
        page_media.click(L.import_media.photo_entry.sort_menu.descending)
        page_media.driver.driver.back()
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        photo_width_5s = page_edit.timeline_get_photo_width(media_list[0])
        page_edit.timeline_select_media(media_list[0], 'Photo')
        # case 2: default image duration - 0.5s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration('0.5')
        page_edit.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.back).click()
        # ---- add photo to timeline - jpg
        page_edit.el(L.edit.menu.import_media).click()
        time.sleep(5)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[1])
        page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        photo_width_05s = page_edit.timeline_get_photo_width(media_list[1])
        photo_width_5s_after = page_edit.timeline_get_photo_width(media_list[0])
        self.report.new_result(udid[1], lambda: True if int(photo_width_05s) < int(photo_width_5s_after) else False)
        self.report.start_uuid(udid[2])
        page_edit.timeline_select_media(media_list[0], 'Photo')
        # case 3: default image duration - 10.0s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration('10.0')
        page_edit.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.back).click()
        # ---- add photo to timeline - gif
        page_edit.el(L.edit.menu.import_media).click()
        time.sleep(5)
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[2])
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        photo_width_10s = page_edit.timeline_get_photo_width(media_list[2])
        photo_width_05s_after = page_edit.timeline_get_photo_width(media_list[1])
        photo_width_5s_after = page_edit.timeline_get_photo_width(media_list[0])
        self.report.new_result(udid[2], lambda: True if int(photo_width_10s) > int(photo_width_5s_after) and
                                                        int(photo_width_05s) == int(photo_width_05s_after) and int(
            photo_width_5s) == int(photo_width_5s_after) else False)
        # set default image duration as 5.0s
        page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration('5.0')
        page_edit.el(L.timeline_settings.settings.back).click()
