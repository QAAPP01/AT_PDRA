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


@pytest.fixture(scope="class", autouse=True)
def class_setup_teardown(driver: AppiumU2Driver):
    logger("[Start] Init driver session")

    driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
    driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
    driver.implicit_wait(30)  # Wait to app to start
    yield
    driver.driver.stop_recording_screen()
    driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')

class Test:
    def test_01(self):
        assert 1==1