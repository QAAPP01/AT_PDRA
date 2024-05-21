import pytest

from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver
from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.pages.main_page import MainPage


class TestBase:

    @staticmethod
    def exception_handler(e: Exception, driver: AppiumU2Driver, last: bool = False):
        """
        Can Handle Exception and log different log level when the exception is from assertion or others,
        and will reopen app to timeline after logging.
        e: Exception instance
        driver: AppiumU2Driver
        page_main: MainPage
        """
        if type(e) is AssertionError:
            logger(f'[Assertion Error] {repr(e)}]', log_level='error')
        else:
            logger(f'[Exception] {repr(e)}', log_level='critical')
            pytest.fail(f'[Exception] {repr(e)}]')

        if not last:
            driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
            driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')
            MainPage(driver).enter_launcher()
            MainPage(driver).enter_timeline()
