from os import popen, path

from appium.webdriver import Remote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from ATFramework_aPDR.pages.locator.edit import Intro_Video

from ATFramework_aPDR.ATFramework.utils.log import logger

deviceName = popen("adb devices").read().strip().split('\n')[1].split('\t')[0]

device = {
    "deviceName": deviceName,
    "platformName": "Android",
    "settings[waitForIdleTimeout]": 10,
    "newCommandTimeout": 1800,
    "language": "en",
    "locale": "US",
    # "localeScript": "Hant",
    "appPackage": "com.cyberlink.powerdirector.DRA140225_01",
    "appActivity": "com.cyberlink.powerdirector.splash.SplashActivity",
    'autoGrantPermissions': True,
    "noReset": True,  # Delete app data: False
    "autoLaunch": False
}
driver = Remote("http://127.0.0.1:4723/wd/hub", device)


x = r'C:\Users\hausen_lin\PycharmProjects\PDRA\PDRa_portrait_3118\ATFramework_aPDR\SFT\test_material\material.jpg'
print(x)

