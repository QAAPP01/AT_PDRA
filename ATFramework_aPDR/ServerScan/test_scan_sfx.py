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


@allure.feature("SFX Scan")
class Test_SFX:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "bf7398d4-902f-4b6f-a24e-53b6fa49f59c",
            "44aa61a0-82b4-4f39-b156-c16cc157a4c6",
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
        # self.driver.driver.stop_recording_screen()
        # driver.driver.close_app()

    @allure.story("Download Meta SFX")
    def sce_1_3_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_audio_library('SFX')
            self.page_media.click_sfx_tab('meta')

            music = self.elements(L.import_media.music_library.music(0))
            for i in music:
                i.click()
                if self.click(L.import_media.music_library.download, 2):
                    self.click(L.edit.try_before_buy.try_it_first, 1)
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
            self.page_edit.enter_audio_library('SFX')
            self.page_media.click_sfx_tab('meta')

            return "FAIL"

    @allure.story("Download CL SFX")
    def sce_1_3_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.click_sfx_tab('cl')

            self.click(L.import_media.music_library.category(3))
            music = self.elements(L.import_media.music_library.music(0))
            for i in music:
                i.click()
                if self.click(L.import_media.music_library.download, 2):
                    self.click(L.edit.try_before_buy.try_it_first, 1)
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

            return "FAIL"


    @report.exception_screenshot
    def test_case(self):
        result = {
            "sec_1_3_1": self.sce_1_3_1(),
            "sec_1_3_2": self.sce_1_3_2(),
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
