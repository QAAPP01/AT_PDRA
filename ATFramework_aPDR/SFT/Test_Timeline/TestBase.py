from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver
from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.pages.main_page import MainPage


class TestBase:

    @staticmethod
    def exception_handler(e: Exception, driver: AppiumU2Driver, page_main: MainPage):
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

        driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
        driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')
        page_main.enter_launcher()
        page_main.enter_timeline()