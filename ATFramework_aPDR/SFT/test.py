import pprint
import time
import uuid
import os

import cv2
from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory

TEST_MATERIAL_FOLDER = '00PDRa_Testing_Material'
TEST_MATERIAL_FOLDER_01 = '01PDRa_Testing_Material'

# udid = os.popen("adb devices").read().strip().split('\n')[1].split('\t')[0]
udid = "R5CT32Q3WQN"
# udid = "9596423546005V8"

device = {
    "udid": udid,
    "deviceName": "deviceName",
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



# shortcut
# self.test_material_folder = TEST_MATERIAL_FOLDER
# self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01
# self.page_main = PageFactory().get_page_object("main_page", self.driver)
# self.page_edit = PageFactory().get_page_object("edit", self.driver)
# self.page_media = PageFactory().get_page_object("import_media", self.driver)
# self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)
# self.click = self.page_main.h_click
# self.long_press = self.page_main.h_long_press
# self.element = self.page_main.h_get_element
# self.elements = self.page_main.h_get_elements
# self.is_exist = self.page_main.h_is_exist


def h_swipe_playhead(timecode='00:01.0', x_offset=30):
    """
    # Function: h_swipe_playhead
    # Description: Swipe the playhead to location
    # Parameters: x: x-coordinate of destination
    #             speed: 1 is fastest
    #             x_offset: length of x to trigger swiping
    # Return: None
    # Note: N/A
    # Author: Hausen
    """
    ruler = driver.find_element("id", L.edit.timeline.timeline_ruler[1]).rect
    y = ruler["y"] + ruler["height"] // 2
    x = ruler["x"] + ruler["width"] - 10

    action = TouchAction(driver)
    action.long_press(x=x, y=y)

    timecode_flag = True
    while timecode_flag:
        x = int(x - x_offset)
        print(f'move to {x}, {y}')
        action.move_to(x=x, y=y).perform()
        playhead = driver.find_element("id", L.edit.timeline.timecode[1]).text
        print(playhead)
        action.press(x=x, y=y)

        if playhead == timecode:
            timecode_flag = False
            print('exit')

    action.release().perform()
    return True

def swipe_without_release(driver, x1, y1, x2, y2):
    action = TouchAction(driver)
    action.long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()


driver.quit()


