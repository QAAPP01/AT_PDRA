import pprint
import time
import uuid
import os

import cv2
import pytest
from appium import webdriver
from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory


desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'device',
    "appPackage": "com.cyberlink.powerdirector.DRA140225_01",
    'autoGrantPermissions': False,
    "noReset": True,
    "autoLaunch": False,
    'udid': 'RFCW2198L7B'
    # 'udid': "R5CT32Q3WQN"
}
driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)

x = driver.find_element('xpath', f'//*[contains(@text,"No Effect")]/preceding-sibling::android.widget.ImageView')
print(x.get_attribute('enabled'))
y = driver.find_element('xpath', )
print(y.get_attribute('xpath'))