import pytest, inspect, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

class Test_SFT_Scenario_01_06:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report

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

        self.report.set_driver(driver)
        driver.driver.launch_app()
        yield
        driver.driver.close_app()

    def sce_1_6_1(self):
        uuid = 'd013615b-af96-45e6-9131-ebb28cf4e62a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")
            self.click(id("pixabayWebsiteBtn"))

            if self.is_exist(find_string("pixabay.com")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find "pixabay.com"'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_1_6_2(self):
        uuid = 'a7fe71e0-2d94-465d-82d6-0984681d921e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            pic_src = self.page_main.get_picture(id("pickerDeviceLibrary"))
            self.page_main.text_search(L.import_media.media_library.search, "search")
            pic_tgt = self.page_main.get_picture(id("pickerDeviceLibrary"))

            if not HCompareImg(pic_tgt, pic_src).full_compare() == 1:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Image no changed'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_1_6_3(self):
        uuid = '98254f7e-2c56-4758-90fc-569aed52a0d4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.Photo.display_preview):

                self.driver.driver.back()

                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Preview window is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"


    def sce_1_6_4(self):
        uuid = '7259b134-e694-4766-bf01-58d9293aead7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.Photo.display_preview):

                self.driver.driver.back()

                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Preview window is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"


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

    def sce_1_6_6(self):
        uuid = 'ce5575ba-3d33-4522-857b-de58025ac03f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.tap_blank_space()
            self.page_edit.enter_main_tool("Audio")
            self.click(find_string("Music"))
            if not self.page_media.select_music_library(L.import_media.music_library.meta):
                raise Exception('Enter Meta page fail')
            self.click(id("tx_sign_in_to_facebook"))

            if self.is_exist(L.import_media.music_library.category_name(0), 10):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find category page'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)
        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(find_string("Music"))
            self.page_media.select_music_library(L.import_media.music_library.meta)

            return "FAIL"

    def sce_1_6_7(self):
        uuid = '2772d69e-c19f-4410-932f-04aa205ccc05'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            pic_tgt = self.page_main.get_picture(L.import_media.music_library.meta)
            pic_src = path.join(path.dirname(__file__), 'test_material', '01_06', f'{func_name}.png')

            if HCompareImg(pic_tgt, pic_src).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Meta icon is different'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(find_string("Music"))
            self.page_media.select_music_library(L.import_media.music_library.meta)

            return "FAIL"

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

        if self.is_exist(L.import_media.music_library.category_name(0)):
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

        self.click(L.import_media.music_library.category_name(3))
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
        uuid = 'ddd0b988-4bdd-4b92-b08c-3155921dc160'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.music_library.download)
            self.click(L.edit.try_before_buy.try_it, 1)
            while self.is_exist(L.import_media.music_library.downloading, 1):
                time.sleep(1)
            if not self.click(L.import_media.music_library.add):
                raise Exception('No Add button')

            if self.is_exist(xpath(f'//*[contains(@content-desc,"{clip_name}")]')):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Clip is not exist'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)
        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_1_6_12(self):
        uuid = 'd22b9e7c-b34d-492c-96af-f742cc075410'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.click_tool("Audio")
            self.click(find_string("Music"))
            self.page_media.select_music_library(L.import_media.music_library.meta)
            self.click(find_string("Downloaded"))
            self.click(find_string(clip_name))
            if self.element(L.import_media.music_library.favorite).get_attribute('selected') == 'true':
                self.click(L.import_media.music_library.favorite)
            self.click(L.import_media.music_library.back)
            if not self.click(find_string("Favorite")):
                raise Exception('No Favorite category')

            if self.is_exist(find_string(clip_name)):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Cannot find clip {(clip_name)}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)
        except Exception as err:
            logger(f'\n{err}')
            return "FAIL"

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_case(self):
        result = {"sce_1_6_1": self.sce_1_6_1(),
                  "sce_1_6_2": self.sce_1_6_2(),
                  "sce_1_6_3": self.sce_1_6_3(),
                  "sce_1_6_4": self.sce_1_6_4(),
                  "sce_1_6_5": self.sce_01_06_05(),
                  "sce_1_6_6": self.sce_1_6_6(),
                  "sce_1_6_7": self.sce_1_6_7(),
                  "sce_1_6_8": self.sce_01_06_08(),
                  "sce_1_6_9": self.sce_01_06_09(),
                  "sce_1_6_10": self.sce_01_06_10(),
                  "sce_1_6_11": self.sce_01_06_11(),
                  "sce_1_6_12": self.sce_1_6_12()
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
