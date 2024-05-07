import traceback
import inspect
import pytest
import sys
import allure
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import REPORT_INSTANCE as report

sys.path.insert(0, (path.dirname(path.dirname(__file__))))


@allure.feature("Music Scan")
class Test_Media:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "5a037e93-6bae-4630-a83d-c2dad6f8da6e",
            "872ad7b3-bcb3-4ddc-99ce-09a0ddc2682e",
            "a07a8287-a5c3-4e8a-a4af-8b0cf5b9eb31",
        ]

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
        self.is_not_exist = self.page_main.h_is_not_exist

        report.set_driver(driver)
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    @allure.story("Download Meta Music")
    def sce_1_2_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_music_library()
            self.page_media.click_audio_tab('meta')

            self.click(L.import_media.music_library.category(3))
            music = self.elements(L.import_media.music_library.music(0))
            for i in music:
                i.click()
                if self.click(L.import_media.music_library.download):
                    self.click(L.edit.try_before_buy.try_it_first, 0.5)
                    if self.is_exist(L.import_media.music_library.download_cancel, 1):
                        self.is_not_exist(L.import_media.music_library.download_cancel)
                    break

            if self.is_exist(L.import_media.music_library.add):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_music_library()
            self.page_media.click_audio_tab('meta')

            return "FAIL"

    @allure.story("Download Mixtape Music")
    def sce_1_2_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.click_audio_tab('mixtape')
            self.page_media.waiting_download()

            self.click(L.import_media.music_library.category(3))
            music = self.elements(L.import_media.music_library.music(0))
            for i in music:
                i.click()
                if self.click(L.import_media.music_library.download):
                    self.click(L.edit.try_before_buy.try_it_first, 0.5)
                    if self.is_exist(L.import_media.music_library.download_cancel, 1):
                        self.is_not_exist(L.import_media.music_library.download_cancel)
                    break
            if self.is_exist(L.import_media.music_library.add):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')
            
        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_music_library()
            self.page_media.click_audio_tab('mixtape')

            return "FAIL"

    @allure.story("Download CL Music")
    def sce_1_2_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.click_audio_tab('cl')
            self.page_media.waiting_download()

            self.click(L.import_media.music_library.category(3))
            music = self.elements(L.import_media.music_library.music(0))
            for i in music:
                i.click()
                if self.click(L.import_media.music_library.download):
                    if self.is_exist(L.import_media.music_library.download_cancel):
                        self.is_not_exist(L.import_media.music_library.download_cancel)
                    break

            if self.is_exist(L.import_media.music_library.add):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {
            "sec_1_2_1": self.sce_1_2_1(),
            "sec_1_2_2": self.sce_1_2_2(),
            "sec_1_2_3": self.sce_1_2_3(),
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
