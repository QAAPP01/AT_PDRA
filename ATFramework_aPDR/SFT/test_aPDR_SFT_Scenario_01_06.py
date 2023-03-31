import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from main import deviceName
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

file_video = 'video.mp4'
file_photo = 'photo.jpg'


class Test_SFT_Scenario_01_06:
    @pytest.fixture(autouse=True)
    def initial(self):

        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger("[Start] Init driver session")
        desired_caps = {}
        desired_caps.update(app_config.cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        if desired_caps['udid'] == 'auto':
            desired_caps['udid'] = deviceName
        logger(f"[Info] caps={desired_caps}")
        self.report = report
        self.device_udid = desired_caps['udid']
        # ---- local mode > end ----
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

        # retry 3 time if create driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                                       desired_caps)
                if self.driver:
                    logger("\n[Done] Driver created!")
                    break
                else:
                    raise Exception("\n[Fail] Create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)
        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        self.report.set_driver(self.driver)
        self.driver.driver.start_recording_screen()
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(0.1)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Stop] Teardown")
        self.driver.stop_driver()

    def sce_01_06_01(self):
        item_id = '01_06_01'
        uuid = 'd013615b-af96-45e6-9131-ebb28cf4e62a'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(skip_media=False)
        self.page_media.select_photo_library("pixabay")
        self.click(id("pixabayWebsiteBtn"))
        if self.is_exist(find_string("pixabay.com")):
            self.driver.driver.back()
            result = True
        else:
            self.driver.driver.back()
            result = False
            logger('\n[Fail] Cannot find "pixabay.com"')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_02(self):
        item_id = '01_06_02'
        uuid = 'a7fe71e0-2d94-465d-82d6-0984681d921e'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        pic_base = self.page_main.get_picture(id("pickerDeviceLibrary"))
        self.page_main.text_search(L.import_media.media_library.search, "search")
        while self.is_exist(L.import_media.media_library.waiting_cursor, 1):
            time.sleep(1)
        pic_after = self.page_main.get_picture(id("pickerDeviceLibrary"))
        if not CompareImage(pic_base, pic_after).h_total_compare() > 0.9:
            result = True
        else:
            result = False
            logger('\n[Fail] Image no change')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_03(self):
        item_id = '01_06_03'
        uuid = '98254f7e-2c56-4758-90fc-569aed52a0d4'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.media_library.btn_preview())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)
        if self.is_exist(L.import_media.media_library.Photo.display_preview):
            self.driver.driver.back()
            result = True
        else:
            result = False
            logger('\n[Fail] Preview window is not exist')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_04(self):
        item_id = '01_06_04'
        uuid = '7259b134-e694-4766-bf01-58d9293aead7'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.long_press(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.loading_circle, 1):
            time.sleep(1)
        if self.is_exist(L.import_media.media_library.Photo.display_preview):
            self.driver.driver.back()
            result = True
        else:
            result = False
            logger('\n[Fail] Preview window is not exist')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_05(self):
        item_id = '01_06_05'
        uuid = '3e807c53-7c96-428d-b127-950f5caaed50'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.media_library.media())
        while self.is_exist(L.import_media.media_library.downloading, 1):
            time.sleep(1)
        self.click(L.import_media.media_library.apply)
        if self.is_exist(L.edit.timeline.item_view_border):
            result = True
        else:
            result = False
            logger('\n[Fail] No Master clip')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_06(self):
        item_id = '01_06_06'
        uuid = 'ce5575ba-3d33-4522-857b-de58025ac03f'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_tool("Audio")
        self.click(find_string("Music"))
        self.page_media.select_music_library(L.import_media.music_library.meta)
        self.click(id("tx_sign_in_to_facebook"))

        if self.is_exist(L.import_media.music_library.category_name, 10):
            result = True
        else:
            result = False
            logger('\n[Fail] Cannot find category_name')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_07(self):
        try:
            uuid = '2772d69e-c19f-4410-932f-04aa205ccc05'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            pic_tgt = self.page_main.get_picture(L.import_media.music_library.meta)
            pic_src = path.join(path.dirname(__file__), 'test_material', '01_06', case_id + '.png')

            if HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Meta icon is different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_01_06_08(self):
        item_id = '01_06_08'
        uuid = 'df832d9e-82a4-493b-8720-4a7bc2a37107'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.music_library.meta)
        if self.is_exist(find_string("sound/collection/terms")):
            result = True
            self.driver.driver.back()
        else:
            result = False
            logger('\n[Fail] Cannot find "sound/collection/terms"')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_09(self):
        item_id = '01_06_09'
        uuid = '2a34361c-1eb6-4f27-89c4-054668707b7c'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.music_library.filter_genres)

        if self.is_exist(L.import_media.music_library.category_name):
            result = True
        else:
            result = False
            logger('\n[Fail] Cannot find category_name')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_10(self):
        item_id = '01_06_10'
        uuid = 'df48c34f-a04e-4ae4-a19f-f4b245087b86'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.music_library.category_name)
        clip = self.element(L.import_media.music_library.clip())
        global clip_name
        clip_name = clip.text
        clip.click()
        result_prelisten = True if self.is_exist(L.import_media.music_library.stop) else False
        result_search = True if self.is_exist(L.import_media.music_library.search) else False
        if result_prelisten and result_search:
            result = True
        else:
            result = False
            logger(f'\n[Fail] result_prelisten = {result_prelisten}, result_search = {result_search}')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_11(self):
        item_id = '01_06_11'
        uuid = 'ddd0b988-4bdd-4b92-b08c-3155921dc160'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.music_library.download)
        while self.is_exist(L.import_media.music_library.downloading, 1):
            time.sleep(1)
        self.click(L.import_media.music_library.add)
        if self.is_exist(id("item_view_thumbnail_host")):
            result = True
        else:
            result = False
            logger('\n[Fail] id "item_view_thumbnail_host" is not exist')
        self.report.new_result(uuid, result)
        return result

    def sce_01_06_12(self):
        item_id = '01_06_12'
        uuid = 'd22b9e7c-b34d-492c-96af-f742cc075410'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_tool("Audio")
        self.click(find_string("Music"))
        self.page_media.select_music_library(L.import_media.music_library.meta)
        self.click(find_string("Downloaded"))
        self.click(find_string(clip_name))
        self.click(L.import_media.music_library.favorite)
        self.click(L.import_media.music_library.back)
        self.click(find_string("Favorite"))
        if self.is_exist(find_string(clip_name)):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find clip {(clip_name)}')
        self.report.new_result(uuid, result)
        return result

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_06_01_to_12(self):
        result = {
            "sce_01_06_01": self.sce_01_06_01(),
            "sce_01_06_02": self.sce_01_06_02(),
            "sce_01_06_03": self.sce_01_06_03(),
            "sce_01_06_04": self.sce_01_06_04(),
            "sce_01_06_05": self.sce_01_06_05(),
            "sce_01_06_06": self.sce_01_06_06(),
            "sce_01_06_07": self.sce_01_06_07(),
            "sce_01_06_08": self.sce_01_06_08(),
            "sce_01_06_09": self.sce_01_06_09(),
            "sce_01_06_10": self.sce_01_06_10(),
            "sce_01_06_11": self.sce_01_06_11(),
            "sce_01_06_12": self.sce_01_06_12()
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
