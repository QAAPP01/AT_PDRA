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
from ..ATFramework.drivers.appium_driver import AppiumU2Driver

"""
allure levels:
- Feature (class)
-- Story (feature)
--- title (step)
---- steps (X)
"""


@pytest.fixture(scope="class", autouse=True)
def class_setup_teardown(driver: AppiumU2Driver):
    logger("[Start] Init driver session")

    driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
    driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
    driver.implicit_wait(30)  # Wait to app to start
    # Will open to main menu
    yield
    driver.driver.stop_recording_screen()
    driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')


@allure.feature('')
class Test:
    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.story("Getty Video Preview")
    def test_getty_video_preview(self, driver):
        logger(f"\n[Start] {inspect.stack()[0][3]}")

        try:
            self.page_main.enter_launcher()
            self.page_main.subscribe()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")
            raise Exception

    @allure.story("Getty Video Download")
    def test_getty_video_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected, 60)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")
            raise Exception
