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


@pytest.fixture(scope="class", autouse=True)
def init(driver):
    logger("[Start] Init driver session")

    driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
    driver.driver.launch_app()
    yield
    driver.driver.stop_recording_screen()
    driver.driver.close_app()


@allure.feature("SFX Scan")
class Test_SFX:
    def initial(self, driver):

        self.driver = driver

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

    @allure.story("Download Meta SFX")
    def test_sfx_meta(self):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

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

            assert self.is_exist(L.import_media.music_library.add)

        except Exception:
            traceback.print_exc()
            self.driver.driver.stop_recording_screen()
            self.driver.driver.close_app()
            self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_audio_library('SFX')
            self.page_media.click_sfx_tab('meta')
            raise Exception(f'[Exception] {func_name}')

    @allure.story("Download CL SFX")
    def test_sfx_cl(self):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

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
            assert self.is_exist(L.import_media.music_library.add)

        except Exception:
            traceback.print_exc()
            self.driver.driver.stop_recording_screen()
            self.driver.driver.close_app()

            raise Exception(f'[Exception] {func_name}')
