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


class Test_SFT_Scenario_01_04:
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
    def test_sce_01_04_01(self):
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        material_folder = 'Music'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_main.el(L.edit.menu.import_media).click()
        page_media.switch_to_music_library()
        page_media.select_media_by_text(material_folder)
        #[Music server - Background Music] Download and add
        udid = ['3c2b77dd-a778-4756-9ec3-4c7ee6fab4d0', '8d65828e-da4b-453c-ae24-a8a659fedb99',
                '7f73a1a0-5ba6-4e4c-9926-55aacb9bf8cd']
        self.report.start_uuid(udid[1])
        page_media.el(L.import_media.music_server_library.tab_background_music).click()
        time.sleep(3)
        page_media.select_media_by_text('Classical')
        time.sleep(3)
        page_media.select_song_by_text('With Honors')
        time.sleep(3)
        page_media.el(L.import_media.library_listview.download_song).click()
        self.report.new_result(udid[1], page_media.is_exist(L.import_media.library_listview.add, 10))
        self.report.start_uuid(udid[2])
        time.sleep(3)
        page_media.el(L.import_media.library_listview.add).click()
        time.sleep(3)
        self.report.new_result(udid[2], page_edit.timeline_check_media('With Honors.mp3', 'Music'))
        # [Music server - Sound Clip] Download and add
        udid = ['9d6f1ed6-7bf6-4c98-9e3b-e1d2f1377e29', 'fa22176f-4764-45b1-8e88-aaba33ea0fa8',
                'aff2086d-11fc-4f3e-a87c-75dc099ec530']
        self.report.start_uuid(udid[1])
        page_media.el(L.import_media.menu.back).click()
        page_media.el(L.import_media.menu.back).click()
        page_media.select_media_by_text('Sound Clips')
        time.sleep(3)
        #page_media.el(L.import_media.music_server_library.tab_sound_clip).click()
        page_media.select_media_by_text('Animals')
        time.sleep(3)
        page_media.select_song_by_text('Cat01')
        page_media.el(L.import_media.library_listview.download_song).click()
        self.report.new_result(udid[1], page_media.is_exist(L.import_media.library_listview.add, 10))
        self.report.start_uuid(udid[2])
        time.sleep(3)
        page_media.el(L.import_media.library_listview.add).click()
        time.sleep(3)
        self.report.new_result(udid[2], page_edit.timeline_check_media('Cat01.mp3', 'Music'))

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_04_02(self):
        # create new project > set aspect ratio
        # enter music library > [check point] Sorting in Music Library
        udid = ['edc831f1-1a11-441a-af8d-44d4ab965bd7', '2b2608ff-5738-4f1b-a21d-619c2561dba9',
                'a945d807-c98e-472a-8bde-2c2611fd1e86']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        
        # create existed 9_16 project
        project_title = '9_16'
        material_folder = 'Music and Sound Clips'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_main.el(L.edit.menu.import_media).click()
        # switch to video library
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.switch_to_video_library()
        self.report.new_result(udid[0], page_media.check_element_exists(L.import_media.video_category.txt_video_capture))
        # enter folder > PDRa_Testing_Material
        self.report.start_uuid(udid[1])
        page_media.select_media_by_text(self.test_material_folder)
        self.report.new_result(udid[1], page_media.check_element_exists(L.import_media.video_entry.sort))
        self.report.start_uuid(udid[2])
        # check default sorting as date + descending
        page_media.click(L.import_media.video_entry.sort)
        if page_media.is_element_checked(L.import_media.video_entry.sort_menu.by_date):
            if page_media.is_element_checked(L.import_media.video_entry.sort_menu.descending):
                self.report.new_result(udid[2], True)
            else:
                self.report.new_result(udid[2], False)
        else:
            self.report.new_result(udid[2], False)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_04_03(self):
        udid = ['cf903a6d-d248-4cf3-8795-bd1e240cd6a2', 'd5072008-9710-47be-a3da-d4ce6dec1d8b']
        media_list = ['3gp.3GP']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        self.report.new_result(udid[0], page_main.check_existed_project_by_title(project_title))
        self.report.start_uuid(udid[1])
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result(udid[1], page_edit.check_preview_aspect_ratio(project_title))
        page_edit.timeline_select_media(media_list[0], 'Video')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        page_main.el(L.edit.menu.import_media).click()
        # add 2 video to timeline
        udid = ['bb2cdd92-f5b2-41f8-b2c8-68514935557f', '3052a010-441f-4968-ac12-685a67e46c40']
        media_list = ['slow_motion.mp4', 'mp4.mp4']
        page_media.switch_to_video_library()
        page_media.select_media_by_text(self.test_material_folder)
        index = 0
        for media in media_list:
            # add media
            self.report.start_uuid(udid[index])
            page_media.select_media_by_text(media_list[index])
            #page_media.select_media_by_order(index+1)
            page_media.el(L.import_media.library_gridview.add).click()
            self.report.new_result(udid[index], page_edit.timeline_check_media(media_list[index], 'Video'))
            index += 1
        udid = ['ac7da8af-d294-461a-91e6-9bd1037b62c8']
        self.report.start_uuid(udid[0])
        page_edit.timeline_select_media(media_list[1], 'Video')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        #page_edit.driver.driver.back()
        #time.sleep(1)
        #page_edit.driver.driver.back()
        #time.sleep(1)
        #page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        self.report.new_result(udid[0], page_edit.timeline_check_media(media_list[1], 'Video'))

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_04_04(self):
        udid = ['3dbb391c-6f4f-4e69-bea3-0c2ff3b9029e', '6a7a67e9-d347-4fba-9551-4b7342e3e76f', #jpg
                '55e5be09-e419-4d54-9cf5-3e9c0cb65485', 'e3fef0a2-2777-4532-8eac-7b29098e38af', #bmp
                'e32beec3-e4ba-4be0-8bac-0d643acd1bbd'] #pan - OFF
        media_list = ['gif.gif', 'bmp.bmp']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        # Set Pan Zoom [OFF]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('OFF')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        # add 2 photo to timeline
        page_media.switch_to_photo_library()
        index = 0
        index_media = 0
        for media in media_list:
            # add media
            self.report.start_uuid(udid[index])
            page_media.select_media_by_text(self.test_material_folder)
            page_media.click(L.import_media.video_entry.sort)
            page_media.click(L.import_media.video_entry.sort_menu.by_date)
            page_media.click(L.import_media.video_entry.sort_menu.descending)
            page_media.driver.driver.back()
            page_media.select_media_by_text(media_list[index_media])
            #page_media.select_media_by_order(index_media+1)
            page_media.el(L.import_media.library_gridview.add).click()
            self.report.new_result(udid[index], page_edit.timeline_check_media(media_list[index_media], 'Photo'))
            # snapshot > preview > snapshot > check diff.
            self.report.start_uuid(udid[index+1])
            page_edit.timeline_select_media(media_list[index_media], 'Photo')
            pic_before = page_edit.get_preview_pic()
            el_playback = page_edit.el(L.edit.menu.play)
            el_playback.click()
            time.sleep(10)
            pic_after = page_edit.get_preview_pic()
            self.report.new_result(udid[index+1], CompareImage(pic_before, pic_after, 3).compare_image())
            self.report.start_uuid(udid[4])
            if index == 0:
                self.report.new_result(udid[4], CompareImage(pic_before, pic_after, 3).compare_image())
            page_edit.el(L.edit.menu.back).click()
            page_edit.el(L.edit.menu.import_media).click()
            page_media.switch_to_photo_library()
            index += 2
            index_media += 1
        # add 3 music to timeline
        udid = ['422fdd99-3f66-46a7-9187-e4da2b8ed2f5', '59922bde-2b16-4fb7-8f0d-748b6ea44df0',
                'bdd364a7-42d8-4144-9899-dff68561c039']
        media_list = ['m4a.m4a', 'mp3.mp3', 'wav.wav']
        page_media.switch_to_music_library()
        page_media.select_media_by_text(self.test_material_folder)
        index = 0
        for media in media_list:
            # add media
            self.report.start_uuid(udid[index])
            page_media.select_song_by_text(media_list[index])
            # page_media.el(L.import_media.library_listview.add).click()
            page_media.add_selected_song_to_timeline()
            self.report.new_result(udid[index], page_edit.timeline_check_media(media_list[index], 'Music'))
            index += 1

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_04_05(self):
        case_name = 'sce_01_04_05'
        # Sorting in Video Library
        udid = ['3a030a8b-6f08-4455-94c2-50d2705dd3a9', 'c32748f1-3592-4aeb-91f3-9d5c668d5ebe',
                '61d6db66-4d99-4ee2-a9c4-5de8262b8378', 'c75cdda8-6009-4a8b-abb7-db236c9d65b3',
                '8ac077c5-0c3a-4784-b056-15660e87dad1']
        self.report.start_uuid(udid[0])
        material_list = ['3gp.3GP', 'mp4.mp4', 'mkv.mkv', 'slow_motion.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_main.el(L.edit.menu.import_media).click()
        page_media.switch_to_video_library()
        # enter folder > PDRa_Testing_Material
        page_media.select_media_by_text(self.test_material_folder)
        page_media.click(L.import_media.video_entry.sort)
        # case 1: (Ascending) By Name
        page_media.click(L.import_media.video_entry.sort_menu.by_name)
        page_media.click(L.import_media.video_entry.sort_menu.ascending)
        page_media.driver.driver.back()
        self.report.add_result(udid[0], page_media.video_list_check_item(material_list[0], material_list[1]),
                               case_name)
        # case 2: (Ascending) By Date
        self.report.start_uuid(udid[1])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_date)
        page_media.driver.driver.back()
        self.report.add_result(udid[1], page_media.video_list_check_item(material_list[1], material_list[0]),
                               case_name)
        # case 4: (Ascending) By Resolution
        self.report.start_uuid(udid[2])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_resolution)
        page_media.driver.driver.back()
        self.report.add_result(udid[2], page_media.video_list_check_item(material_list[0], material_list[2]),
                               case_name)
        # case 3: (Ascending) By Duration
        self.report.start_uuid(udid[3])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_duration)
        page_media.driver.driver.back()
        self.report.add_result(udid[3], page_media.video_list_check_item(material_list[3], material_list[2]),
                               case_name)
        # case 5: (Ascending) By File size
        self.report.start_uuid(udid[4])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_filesize)
        page_media.driver.driver.back()
        self.report.add_result(udid[4], page_media.video_list_check_item(material_list[3], material_list[0]),
                               case_name)
        # set back to default by Descending + Date
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_date)
        page_media.click(L.import_media.video_entry.sort_menu.descending)
        page_media.driver.driver.back()

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_04_06(self):
        udid = ['c94eddb7-88a0-4d14-b451-d961dfffe69b', '0f11d05a-472e-4e9d-9bc9-5ba9df210f74',
                'b403ad45-8ac7-455e-947d-a69ad3cf05c6']
        material_list = ['h263_3gp.3GP', 'h263_mp4.mp4', 'h264.avc_3gp.3gp', 'h264.avc_mkv.mkv', 'h264.avc_mp4.mp4',
                         'h265.hevc_mp4.mp4', 'mp4.sp_3gp.3GP', 'vp8_mkv.mkv', 'vp8_webm.webm', 'vp9_mkv.mkv',
                         'vp9_webm.webm']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_media.clean_google_drive_cache()
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_main.el(L.edit.menu.import_media).click()
        page_media.switch_to_video_library()
        # enter google drive
        result_google_drive = page_media.enter_google_drive("video",len(material_list) )
        self.report.new_result(udid[0], result_google_drive)
        
        # download files
        self.report.start_uuid(udid[1])
        result_download_file = page_media.google_download_file()
        self.report.new_result(udid[1],result_download_file)
        
        self.report.start_uuid(udid[2])
        result_drag_google_clip = page_media.drag_google_clip()
        self.report.new_result(udid[2], result_drag_google_clip)
