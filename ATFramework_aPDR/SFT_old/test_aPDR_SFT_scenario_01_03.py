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


class Test_SFT_Scenario_01_03:
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
    def test_sce_01_03_01(self):
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        #material_folder = 'Music and Sound Clips'
        material_folder = 'Music'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_main.el(L.edit.menu.import_media).click()
        page_media.switch_to_music_library()
        page_media.select_media_by_text(material_folder)
        # [Music server - Background Music] Download and add
        udid = ['edc3a0c2-4c2e-41ae-87d7-3aa7844b21df', '41433a2d-08aa-4685-9cdb-8fe4c2ff81a4',
                'c61fbccc-5e91-42e6-bc53-c0557a4b8b74']
        self.report.start_uuid(udid[1])
        page_media.el(L.import_media.music_server_library.tab_background_music).click()
        page_media.select_media_by_text('Classical')
        time.sleep(10)
        page_media.select_song_by_text('With Honors')
        time.sleep(2)
        page_media.el(L.import_media.library_listview.download_song).click()
        self.report.new_result(udid[1], page_media.is_exist(L.import_media.library_listview.add, 60))
        self.report.start_uuid(udid[2])
        time.sleep(5)
        page_media.el(L.import_media.library_listview.add).click()
        time.sleep(5)
        self.report.new_result(udid[2], page_edit.timeline_check_media('With Honors.mp3', 'Music'))
        # [Music server - Sound Clip] Download and add
        udid = ['2d38ece5-b483-4dd0-86ae-1684e1dbd665', '60905267-ada9-44eb-8251-ef9a87a7cc81',
                '5f41a746-0dd3-40d9-88ad-d72e8ab3bb61']
        self.report.start_uuid(udid[1])
        page_media.el(L.import_media.menu.back).click()
        page_media.el(L.import_media.menu.back).click()
        #page_media.el(L.import_media.music_server_library.tab_sound_clip).click()
        page_media.select_media_by_text('Sound Clips')
        time.sleep(3)
        page_media.select_media_by_text('Animals')
        time.sleep(10)
        page_media.select_song_by_text('Cat01')
        time.sleep(2)
        page_media.el(L.import_media.library_listview.download_song).click()
        self.report.new_result(udid[1], page_media.is_exist(L.import_media.library_listview.add, 10))
        self.report.start_uuid(udid[2])
        time.sleep(5)
        page_media.el(L.import_media.library_listview.add).click()
        time.sleep(5)
        self.report.new_result(udid[2], page_edit.timeline_check_media('Cat01.mp3', 'Music'))

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_03_02(self):
        case_name = 'sce_01_03_02'
        udid = ['8b96e410-9567-43bd-9318-e708588c121f', '8c798524-1b86-45d2-8817-b571a2d24744',
                'e86a08d6-ef03-489f-9c25-0cb1129c7ec7']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_main.el(L.edit.menu.import_media).click()
        page_media.switch_to_video_library()
        self.report.new_result(udid[0], page_media.check_element_not_exists(L.import_media.video_entry.sort))
        # enter folder > PDRa_Testing_Material
        self.report.start_uuid(udid[1])
        page_media.select_media_by_text(self.test_material_folder)
        self.report.new_result(udid[1], page_media.check_element_exists(L.import_media.video_entry.sort))
        # check default sorting is by date and descending
        self.report.start_uuid(udid[2])
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
    def test_sce_01_03_03(self):
        case_name = 'sce_01_03_03'
        #add 2 video to timeline
        udid = ['821b99cf-c7e8-49dd-939b-3e42ea3e2a78', 'e59a01fc-8854-4779-b324-acd2bbff1d43']
        media_list = ['mp4.mp4', 'mkv.mkv']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_main.el(L.edit.menu.import_media).click()
        page_media.switch_to_video_library()
        # enter folder > PDRa_Testing_Material
        page_media.select_media_by_text(self.test_material_folder)
        # add media
        self.report.start_uuid(udid[0])
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(2)
        time.sleep(2)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.add_result(udid[0], page_edit.timeline_check_media(media_list[0], 'Video'), case_name)        
        # add media
        self.report.start_uuid(udid[1])
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(4)
        time.sleep(2)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.add_result(udid[1], page_edit.timeline_check_media(media_list[1], 'Video'), case_name)
        

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_03_04(self):
        udid = ['c023139e-c9cc-4328-8712-3ee02658fbaa', 'a5217615-8e5b-45c0-9926-7a590329f261']
        media_list = ['m4a.m4a', 'mp3.mp3', 'wav.wav']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        time.sleep(10)
        self.report.new_result(udid[0], page_main.check_existed_project_by_title(project_title))
        self.report.start_uuid(udid[1])
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result(udid[1], page_edit.check_preview_aspect_ratio(project_title))
        page_main.el(L.edit.menu.import_media).click()
        # add 3 music to timeline
        udid = ['ea56db50-2b0d-48d9-9feb-f91203f6a31e', '9ee4f99d-b3ec-4274-90fb-b71567c64b9b',
                '9877d20c-9521-41eb-9554-bda13a6a837f']
        page_media.switch_to_music_library()
        page_media.select_media_by_text(self.test_material_folder)
        index = 0
        for media in media_list:
            # add media
            self.report.start_uuid(udid[index])
            page_media.select_song_by_text(media_list[index])
            page_media.add_selected_song_to_timeline()
            page_edit.swipe_element(L.edit.timeline.playhead, 'up', 20)
            self.report.new_result(udid[index], page_edit.timeline_check_media(media_list[index], 'Music'))
            index += 1
        udid = ['dd672f53-f444-4562-ae07-a38499322f04']
        self.report.start_uuid(udid[0])
        '''
        retry = 0
        while not(page_edit.is_exist(L.main.project.new_launcher_scroll)):
            page_edit.driver.driver.back()
            retry = retry+1
            if retry > 6:
                break     
        '''
        page_media.el(L.import_media.menu.back).click()
        page_media.el(L.import_media.menu.back).click()
        page_edit.el(L.edit.menu.back).click()
        #page_main.el(L.main.project_info.btn_back).click()
        self.report.new_result(udid[0], page_main.check_existed_project_by_title(project_title))
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_03_05(self):
        case_name = 'sce_01_03_05'
        # Sorting in Video Library
        udid = ['6915774e-803f-4bdc-b3e2-801265ab092d', '98a791b5-7722-4d7c-a1a2-1950fbc8a8cd',
                'f94ff455-5b41-48e5-8fbb-ae82e1a0f06c', '4c7a3ee8-3583-48ff-93d8-0a419c93bdaf',
                'e561ab86-9b2f-448a-95ac-da9316b0364d']
        material_list = ['3gp.3GP', 'mp4.mp4', 'mkv.mkv', 'slow_motion.mp4']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
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
        # case 1: (Descending) By Name
        page_media.click(L.import_media.video_entry.sort_menu.by_name)
        page_media.click(L.import_media.video_entry.sort_menu.descending)
        page_media.driver.driver.back()
        self.report.add_result(udid[0], page_media.video_list_check_item(material_list[3], material_list[2]),
                               case_name)
        # case 2: (Descending) By Date
        self.report.start_uuid(udid[1])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_date)
        page_media.driver.driver.back()
        self.report.add_result(udid[1], page_media.video_list_check_item(material_list[3], material_list[2]),
                               case_name)
        # case 2: (Descending) By Duration
        self.report.start_uuid(udid[2])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_duration)
        page_media.driver.driver.back()
        self.report.add_result(udid[2], page_media.video_list_check_item(material_list[0], material_list[1]),
                               case_name)
        # case 3: (Descending) By Resolution
        self.report.start_uuid(udid[3])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_resolution)
        page_media.driver.driver.back()
        self.report.add_result(udid[3], page_media.video_list_check_item(material_list[2], material_list[3]),
                               case_name)
        # case 4: (Descending) By File size
        self.report.start_uuid(udid[4])
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_filesize)
        page_media.driver.driver.back()
        self.report.add_result(udid[4], page_media.video_list_check_item(material_list[2], material_list[1]),
                               case_name)
        # set back to default by Descending + Date
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_date)
        page_media.click(L.import_media.video_entry.sort_menu.descending)
        page_media.driver.driver.back()

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_03_06(self):
        # create new project > set aspect ratio
        udid = ['d525ef8a-7a27-42f3-ac90-5e1783510720', 'f0925727-013a-4f85-9263-185913bef854', #pan - on/off
                '40a15d6a-2366-4e3d-8e1a-6d15c08b5eec', 'be427fb7-345f-42f5-9b9a-d6b8478b48d0', #gif
                '26c0fd29-ebbf-4bc8-b11e-bf5ccd6e208a', '6c59047f-90f0-4b4d-a3fb-a4ab45040524'] #png
        media_list = ['gif.gif', 'png.png']
        self.report.start_uuid(udid[2])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        # Part I - Pan Zoom [ON]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('ON')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_date)
        page_media.click(L.import_media.video_entry.sort_menu.descending)
        page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.new_result(udid[2], page_edit.timeline_check_media(media_list[0], 'Photo'))
        self.report.start_uuid(udid[0])
        self.report.start_uuid(udid[3])
        page_edit.timeline_select_media(media_list[0], 'Photo')
        # snapshot > preview > snapshot > check diff.
        pic_before = page_edit.get_preview_pic()
        el_playback = page_edit.el(L.edit.menu.play)
        el_playback.click()
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result(udid[0], (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                        3).compare_image() == False else False)(
            pic_before, pic_after))
        self.report.new_result(udid[3], (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                        3).compare_image() == False else False)(
            pic_before, pic_after))
        # Part II - Pan Zoom [OFF]
        self.report.start_uuid(udid[4])
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('OFF')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.new_result(udid[4], page_edit.timeline_check_media(media_list[1], 'Photo'))
        self.report.start_uuid(udid[1])
        self.report.start_uuid(udid[5])
        page_edit.timeline_select_media(media_list[1], 'Photo')
        # snapshot > preview > snapshot > check diff.
        pic_before = page_edit.get_preview_pic()
        el_playback = page_edit.el(L.edit.menu.play)
        el_playback.click()
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result(udid[1], CompareImage(pic_before, pic_after, 3).compare_image())
        self.report.new_result(udid[5], CompareImage(pic_before, pic_after, 3).compare_image())

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_03_07(self):
        udid = ['c9786160-b40f-4506-a527-eb716f4f2aed', '863b54d8-104f-4404-9fe7-864c1b118bc3']
        material_list = ['h263_3gp.3GP', 'h263_mp4.mp4', 'h264.avc_3gp.3gp', 'h264.avc_mkv.mkv', 'h264.avc_mp4.mp4',
                         'h265.hevc_mp4.mp4', 'mp4.sp_3gp.3GP', 'vp8_mkv.mkv', 'vp8_webm.webm', 'vp9_mkv.mkv',
                         'vp9_webm.webm']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
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

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_03_08(self):
        udid = ['d04019c0-bdb6-4237-a3d4-7571a7f5e54d', '0015cf16-0a05-4bdd-ab05-3bb7a4427f1b',
                '217c88ad-6b65-4410-be29-b94d805facf0']
        media_list = ['bmp.bmp', 'jpg.jpg', 'gif.gif', 'png.png']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        
        page_edit.timeline_select_media('mp4.mp4', 'Video')
        page_edit.el(L.edit.menu.delete).click()
        
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        # case 1: default image duration - 5.0s (default)
        default_image_duration = page_timeline_settings.get_settings_default_image_duration()
        self.report.new_result(udid[0], page_timeline_settings.check_settings_default_image_duration(default_image_duration))
        self.report.start_uuid(udid[1])
        page_edit.el(L.timeline_settings.settings.back).click()
        # ---- add photo to timeline - bmp
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.click(L.import_media.video_entry.sort)
        page_media.click(L.import_media.video_entry.sort_menu.by_date)
        page_media.click(L.import_media.video_entry.sort_menu.descending)
        page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(2)
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
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(3)
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
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[2])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        photo_width_10s = page_edit.timeline_get_photo_width(media_list[2])
        photo_width_05s_after = page_edit.timeline_get_photo_width(media_list[1])
        photo_width_5s_after = page_edit.timeline_get_photo_width(media_list[0])
        self.report.new_result(udid[2], lambda: True if int(photo_width_10s) > int(photo_width_5s_after) and
                                                        int(photo_width_05s) == int(photo_width_05s_after) and int(
            photo_width_5s) == int(photo_width_5s_after) else False)
        # set default image duration as default (5.0s)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration(default_image_duration)
        page_edit.el(L.timeline_settings.settings.back).click()
