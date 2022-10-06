"""
DriverFactory uses the factory design pattern.
get_mobile_driver_object() returns the appropriate mobile driver object.
get_web_driver_object() returns the appropriate web driver object.
Add elif clauses as and when you implement new drivers.
"""

from selenium import webdriver
from ATFramework.drivers.appium_driver import AppiumU2Driver
from ATFramework.drivers.xcuitest_driver import AppiumXCUITestDriver
# from appium_driver import AppiumU2Driver
# from drivers.appium_driver import AppiumXCUITestDriver
# from drivers.atx_driver import ATXU2Driver
# from xcuitest_driver import AppiumXCUITestDriver


class DriverFactory:
    """ DriverFactory uses the factory design pattern.  """

    @staticmethod
    def get_mobile_driver_object(driver_name, driver_config, app_config, test_mode='local', desired_caps={}, device_name="", package_name=""):
        # Return the appropriate driver object based on driver_name
        driver_obj = None
        driver_name = driver_name.lower()
        device_name = device_name.lower()
        package_name = package_name.lower()
        if driver_name == "appium u2":
            driver_obj = AppiumU2Driver(driver_config, app_config, test_mode, desired_caps)
        elif driver_name == "appium xcui":
            driver_obj = AppiumXCUITestDriver(driver_config, app_config, test_mode, desired_caps)
        # elif driver_name == "atx":
        #    driver_obj = ATXU2Driver()
        return driver_obj

    @staticmethod
    def get_web_driver_object(driver_name):
        # Return the appropriate driver object based on driver_name
        driver_obj = None
        driver_name = driver_name.lower()
        if driver_name == "chrome":
            driver_obj = webdriver.Chrome()
        elif driver_name == "firefox":
            driver_obj = webdriver.Firefox()
        elif driver_name == "chrome":
            driver_obj = webdriver.Ie()
        return driver_obj
