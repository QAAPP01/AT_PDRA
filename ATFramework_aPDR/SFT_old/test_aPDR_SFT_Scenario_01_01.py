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


class Test_SFT_Scenario_01_01:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver session>============')
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
    def test_sce_01_01_01(self):
        #create new project > set aspect ratio
        udid = ['61aa4cc9-a43d-4736-93f9-668e65b4fd8b', 'f3e277f2-67f0-4da8-80fe-02bb72857123',
                '608be76b-22f7-4dc0-9624-e13d621a075e', '36c5557c-2896-4aba-9df0-f9f6310bd20c',
                '05735d3a-c982-4eb2-bd5a-3f0642c8b94f', 'e6e0e636-f91a-4b89-bc7b-c61c49c05baa']
        video_list = ['mp4.mp4', '3gp.3GP', 'slow_motion.mp4', 'mkv.mkv' ]
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        time.sleep(5)
        page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        self.report.add_result(udid[0], page_main.project_check_default_project_name(), "scenario_01_01")
        self.report.start_uuid(udid[1])
        page_main.project_set_name("01_01_01")
        page_main.project_set_16_9()
        self.report.add_result(udid[1], page_main.check_edit_mode_ready(), "scenario_01_01")
        #add 3 video to timeline
        self.report.start_uuid(udid[2])
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.switch_to_video_library()
        #add 1st media
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(video_list[0])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.add_result(udid[2], page_edit.timeline_check_media(video_list[0]), "scenario_01_01")
        # add 2nd media
        self.report.start_uuid(udid[3])
        page_media.select_media_by_text(video_list[1])
        #page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.add_result(udid[3], page_edit.timeline_check_media(video_list[1]), "scenario_01_01")
        # add 3rd media - slow motion
        self.report.start_uuid(udid[4])
        page_media.select_media_by_text(video_list[2])
        #page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.add_result(udid[4], page_edit.timeline_check_media(video_list[2]), "scenario_01_01")
        ''' move to 01_05
        # Enter stock video
        self.report.start_uuid('2d748d11-432d-489b-bbad-f2f710608992')
        page_media.el(L.import_media.menu.back).click()
        page_media.select_media_by_text('Stock Video')
        page_media.el(L.import_media.video_library.tab_pixabay).click()
        page_media.select_media_by_order(1)
        self.report.new_result('2d748d11-432d-489b-bbad-f2f710608992', page_edit.is_exist(L.import_media.library_gridview.download))        
        '''
        # check project auto save
        #self.report.start_uuid(udid[5])
        page_media.el(L.import_media.menu.back).click()
        page_media.el(L.import_media.menu.back).click()
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, 0, L.edit.menu.timeline_setting, 2)
        page_edit.el(L.edit.menu.back).click()
        page_main.ad.close_full_page_ad()
        #self.report.new_result(udid[5], page_main.check_existed_project_by_title("01_01_01"))


    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_01_02(self):
        # create new project > set aspect ratio
        # enter music library > [check point] Sorting in Music Library
        udid = ['465d472f-f1b4-4993-ac3e-d93cd988efd7', 'bc551d29-ccb1-4a12-a516-266bc6a56b05',
                '2110ecb2-a66a-4257-82d6-b85f4ca7a526', '3d50dd61-af2c-41db-a8e3-e5502fe7b076']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("01_01_02")
        page_main.project_set_16_9()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.switch_to_music_library()
        self.report.new_result(udid[0], page_media.check_element_not_exists(L.import_media.music_library.sort))
        #enter folder > PDRa_Testing_Material
        self.report.start_uuid(udid[1])
        page_media.select_media_by_text(self.test_material_folder)
        self.report.new_result(udid[1], page_media.check_element_exists(L.import_media.music_library.sort))
        #check default sorting as name
        self.report.start_uuid(udid[2])
        page_media.click(L.import_media.music_library.sort)
        if page_media.is_element_checked(L.import_media.music_library.sort_menu.by_name):
            if page_media.is_element_checked(L.import_media.music_library.sort_menu.ascending):
                self.report.new_result(udid[2], True)
            else:
                self.report.new_result(udid[2], False)
        else:
            self.report.new_result(udid[2], False)
        #check No 'Resolution' option in menu
        self.report.start_uuid(udid[3])
        self.report.new_result(udid[3], page_media.check_element_not_exists(L.import_media.music_library.sort_menu.by_resolution))

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_01_03(self):
        #create new project > set aspect ratio
        udid = ['dfa15053-3add-4573-8e05-5acf235f551e', '808d09fb-d074-456b-afcb-be56e5b9bfab', #default image duration
                '57ea0d57-d706-4fdf-8d54-61cdae50bc68',
                'e0073b1a-7276-4987-9aac-d0b0217dc7c1', 'be0f1540-c345-4208-a7f2-eb47030f136c', #bmp
                'df56c95e-cc65-4989-995f-834f834a84f0', '6a1b2d89-4858-4994-b8d4-0f9325cb704c', #jpg
                '601c0b3b-9aed-4391-b9dc-6d7a8f0b9d3f', 'a1bae612-908b-440a-bd94-996d7209f532', #gif
                'af08f535-e1bc-4d0b-8ffe-3a2ad17d9a12', '6a4663b3-5dd2-4914-8f49-0b8906ab29a1'] #png
        media_list = ['bmp.bmp', 'jpg.jpg', 'gif.gif',  'png.png']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("01_01_03")
        page_main.project_set_16_9()
        page_main.el(L.import_media.menu.back).click()
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, 0, L.edit.menu.timeline_setting, 2)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        #case 1: default image duration - 5.0s (default)
        self.report.new_result(udid[0], page_timeline_settings.check_settings_default_image_duration('5.0'))
        self.report.start_uuid(udid[3])
        page_edit.el(L.timeline_settings.settings.back).click()
        # ---- add photo to timeline - bmp
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.new_result(udid[3], page_edit.timeline_check_media(media_list[0], 'Photo'))
        self.report.start_uuid(udid[4])
        photo_width_5s = page_edit.timeline_get_photo_width(media_list[0])
        self.report.new_result(udid[4], True)
        self.report.start_uuid(udid[1])
        page_edit.timeline_select_media(media_list[0], 'Photo')
        # case 2: default image duration - 0.5s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration('0.5')
        self.report.new_result(udid[1], page_timeline_settings.check_settings_default_image_duration('0.5'))
        self.report.start_uuid(udid[5])
        page_edit.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.back).click()
        # ---- add photo to timeline - jpg
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.new_result(udid[5], page_edit.timeline_check_media(media_list[1], 'Photo'))
        self.report.start_uuid(udid[6])
        photo_width_05s = page_edit.timeline_get_photo_width(media_list[1])
        photo_width_5s_after = page_edit.timeline_get_photo_width(media_list[0])
        self.report.new_result(udid[6], lambda: True if int(photo_width_05s) < int(photo_width_5s_after) else False)
        self.report.start_uuid(udid[2])
        page_edit.timeline_select_media(media_list[0], 'Photo')
        # case 3: default image duration - 10.0s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration('10.0')
        self.report.new_result(udid[2], page_timeline_settings.check_settings_default_image_duration('10.0'))
        self.report.start_uuid(udid[7])
        page_edit.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.back).click()
        # ---- add photo to timeline - gif
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[2])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.new_result(udid[7], page_edit.timeline_check_media(media_list[2], 'Photo'))
        self.report.start_uuid(udid[8])
        photo_width_10s = page_edit.timeline_get_photo_width(media_list[2])
        photo_width_05s_after = page_edit.timeline_get_photo_width(media_list[1])
        photo_width_5s_after = page_edit.timeline_get_photo_width(media_list[0])
        self.report.new_result(udid[8], lambda: True if int(photo_width_10s) > int(photo_width_5s_after) and
        int(photo_width_05s) == int(photo_width_05s_after) and int(photo_width_5s) == int(photo_width_5s_after) else False)
        self.report.start_uuid(udid[9])
        page_edit.timeline_select_media(media_list[0], 'Photo')
        # case 4: default image duration - 0.5s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration('0.5')
        page_edit.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.back).click()
        # ---- add photo to timeline - png
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[3])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        self.report.new_result(udid[9], page_edit.timeline_check_media(media_list[3], 'Photo'))
        self.report.start_uuid(udid[10])
        photo_width_05s2 = page_edit.timeline_get_photo_width(media_list[3])
        photo_width_10s_after = page_edit.timeline_get_photo_width(media_list[2])
        photo_width_05s_after = page_edit.timeline_get_photo_width(media_list[1])
        photo_width_5s_after = page_edit.timeline_get_photo_width(media_list[0])
        self.report.new_result(udid[10], lambda: True if int(photo_width_05s2) < int(photo_width_5s_after) and
                                                        int(photo_width_05s) == int(photo_width_05s_after) and int(
            photo_width_5s) == int(photo_width_5s_after) and int(
            photo_width_10s) == int(photo_width_10s_after) else False)
        #set default image duration as 5.0s
        page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.set_default_image_duration('5.0')
        page_edit.el(L.timeline_settings.settings.back).click()


    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_01_04(self):
        case_name = 'sce_01_01_04'
        # Sorting in Music Library
        udid = ['de1e1ed0-45df-4700-b80b-53f68a439c04', 'c90e80db-74b2-4a22-9819-8e33d450dd70',
                '80372617-a42c-4da2-9141-62cd6982b607', 'cf5d1894-f2f9-4fa4-886d-a24892994566',
                '6d352df4-7589-4504-b52e-b14309957ba5', '20cc43dd-b11c-4bb8-b456-c4f769528958']
        material_list = ['aac.aac', 'm4a.m4a', 'mp3.mp3', 'wav.wav']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_main.project_click_new()
        page_main.project_set_name(case_name)
        page_main.project_set_16_9()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.switch_to_music_library()
        # enter folder > PDRa_Testing_Material
        page_media.select_media_by_text(self.test_material_folder)
        page_media.click(L.import_media.music_library.sort)
        # case 1: (Ascending) By Name
        page_media.click(L.import_media.music_library.sort_menu.by_name)
        page_media.click(L.import_media.music_library.sort_menu.ascending)
        page_media.driver.driver.back()
        self.report.add_result(udid[0], page_media.music_list_check_item(material_list[0], material_list[3]),
                               case_name)
        # case 2: (Ascending) By Duration
        self.report.start_uuid(udid[1])
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_duration)
        page_media.driver.driver.back()
        self.report.add_result(udid[1], page_media.music_list_check_item(material_list[2], material_list[3]),
                               case_name)
        # case 3: (Ascending) By File size
        self.report.start_uuid(udid[2])
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_filesize)
        page_media.driver.driver.back()
        self.report.add_result(udid[2], page_media.music_list_check_item(material_list[2], material_list[3]),
                               case_name)
        # case 4: (Descending) By Name
        self.report.start_uuid(udid[3])
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_name)
        page_media.click(L.import_media.music_library.sort_menu.descending)
        page_media.driver.driver.back()
        self.report.add_result(udid[3], page_media.music_list_check_item(material_list[3], material_list[0]),
                               case_name)
        # case 4: (Descending) By Duration
        self.report.start_uuid(udid[4])
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_duration)
        page_media.driver.driver.back()
        self.report.add_result(udid[4], page_media.music_list_check_item(material_list[3], material_list[2]),
                               case_name)
        # case 4: (Descending) By File size
        self.report.start_uuid(udid[5])
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_filesize)
        page_media.driver.driver.back()
        self.report.add_result(udid[5], page_media.music_list_check_item(material_list[3], material_list[2]),
                               case_name)
        #set back to default by Asecending + Name
        page_media.click(L.import_media.music_library.sort)
        page_media.click(L.import_media.music_library.sort_menu.by_name)
        page_media.click(L.import_media.music_library.sort_menu.ascending)
        page_media.driver.driver.back()

        # add 4 music to timeline
        udid = ['7959304e-4588-4810-9e69-b00ae850bce3', '9ab7a343-335e-426f-8813-f64260c29f38',
                'ae18e001-07c8-4009-995f-d3a4c22792b3', '990c2772-b52c-494a-8727-9ce83ec70aca']
        media_list = ['wav.wav', 'aac.aac', 'mp3.mp3', 'm4a.m4a']
        page_edit = PageFactory().get_page_object("edit", self.driver)
        index = 0
        for media in media_list:
            # add media
            self.report.start_uuid(udid[index])
            page_media.select_song_by_text(media_list[index])
            # page_media.el(L.import_media.library_listview.add).click()
            page_media.add_selected_song_to_timeline()
            if  index == 3:
                #self.report.new_result(udid[index], page_edit.is_exist(L.import_media.music_library.iap_back))
                self.report.add_result(udid[index], None, 'remove_item', 'Behavior change') 
                break
            self.report.add_result(udid[index], page_edit.timeline_check_media(media_list[index], 'Music', 120),
                                   case_name)
            index += 1

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_01_05(self):
        #create new project > set aspect ratio
        udid = ['f1a093d3-cc42-468c-94c5-11d804d08ba9', '7d73d3a4-c2ab-46d4-99fd-51f497209bf1']
        media_list = ['jpg.jpg', 'png.png']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("01_01_05")
        page_main.project_set_16_9()
        page_media.el(L.import_media.menu.back).click()
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, 0, L.edit.menu.timeline_setting, 2)
        #Part I - Pan Zoom [ON]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('ON')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #snapshot > preview > snapshot > check diff.
        pic_before = page_edit.get_preview_pic()
        el_playback = page_edit.el(L.edit.menu.play)
        el_playback.click()
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result(udid[0], (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 3).compare_image() == False else False)(pic_before, pic_after))
        # Part II - Pan Zoom [OFF]
        self.report.start_uuid(udid[1])
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
        page_edit.timeline_select_media(media_list[1], 'Photo')
        # snapshot > preview > snapshot > check diff.
        pic_before = page_edit.get_preview_pic()
        el_playback = page_edit.el(L.edit.menu.play)
        el_playback.click()
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result(udid[1], CompareImage(pic_before, pic_after, 3).compare_image())

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_01_06(self):
        udid = ['91574d59-f1ed-4c22-a73d-b449e0123363', '8ae4a086-ad88-4770-8dc7-781919acfa3a',
                'ba51aac6-b4a6-403b-a16e-b2a6f875ba79']
        material_list = ['bmp.bmp', 'gif.gif', 'jpg.jpg', 'png.png']
        self.report.start_uuid(udid[0])
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        page_main.project_click_new()
        page_main.project_set_name("01_01_06")
        page_main.project_set_16_9()
        page_media.el(L.import_media.menu.back).click()
        # Pan Zoom [ON]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_timeline_settings.SetPanZoom('ON')
        page_timeline_settings.el(L.timeline_settings.settings.back).click()
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        # enter google drive
        result_google_drive = page_media.enter_google_drive("photo",len(material_list) )
        self.report.new_result(udid[0], result_google_drive)
        
        # download files
        self.report.start_uuid(udid[1])
        result_download_file = page_media.google_download_file()
        self.report.new_result(udid[1],result_download_file)
        
        # Pan & Zoom setting should be correct
        self.report.start_uuid(udid[2])
        result_pan_zoom_setting = page_media.check_pan_zoom_setting()
        self.report.new_result(udid[2], result_pan_zoom_setting)
