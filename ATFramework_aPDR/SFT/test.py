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
# udid = "R5CT32Q3WQN"
udid = "9596423546005V8"

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


def h_swipe_playhead(sec=1, dx=47, x_offset=25):
    """
    # Function: h_swipe_playhead
    # Description: Swipe the playhead to the second after
    # Parameters:
        :param sec: Swipe to seconds after
        :param dx: delta x of 1s
        :param x_offset: length of x to trigger swiping is 25
    # Return: None
    # Note: N/A
    # Author: Hausen
    """
    playhead = driver.find_element("id", L.edit.timeline.playhead[1]).rect
    playhead_x = playhead["x"] + playhead["width"] // 2
    ruler = driver.find_element("id", L.edit.timeline.timeline_ruler[1]).rect
    y = ruler["y"] + ruler["height"] // 2

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

    delta = 9
    delta_x = (dx + x_offset) // delta
    for i in range(sec):
        actions.w3c_actions.pointer_action.move_to_location(playhead_x, y).pointer_down()
        start_x = playhead_x
        for j in range(delta):
            start_x -= delta_x
            actions.w3c_actions.pointer_action.move_to_location(start_x, y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()



def swipe_without_release(driver, x1, y1, x2, y2):
    action = TouchAction(driver)
    action.long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()


h_swipe_playhead(10)

