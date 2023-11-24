import os
import traceback

from appium.webdriver.appium_service import AppiumService
from appium import webdriver

from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *

args = [
    "--address", "127.0.0.1",
    "--port", "4725",
    "--base-path", '/wd/hub'
]

# appium = AppiumService()
# appium.start(args=args)

desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'device',
    "appPackage": "com.cyberlink.powerdirector.DRA140225_01",
    "appActivity": "com.cyberlink.powerdirector.splash.SplashActivity",
    'autoGrantPermissions': False,
    "noReset": True,
    "autoLaunch": False,
    'udid': 'R5CW31G76ST'
}
driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)


# ==================================================================================================================
# Function: h_drag_element
# Description: Drag element
# Parameters: locator
# Return: Boolean
# Note: N/A
# Author: Hausen
# ==================================================================================================================
def h_drag_element(locator, end_x, end_y, wait):
    try:
        element_rect = driver.find_element(locator[0], locator[1]).rect
        start_x = element_rect['x'] + element_rect['width'] // 2
        start_y = element_rect['y'] + element_rect['height'] // 2
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(wait)
        actions.w3c_actions.pointer_action.move_to_location((start_x + end_x) // 2, (start_y + end_y) // 2)
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.pause(wait)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return True
    except Exception as err:
        print(f"[Error] {err}")
        return False


def h_tap(x, y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.release()
    actions.perform()


def h_set_slider_value(percentage, slider_draggable_offset=664/762):
    """
    param percentage: 0~1, ex: 0.5
    param slider_draggable_offset: draggable_width/slider_width
    """

    slider = driver.find_element(L.edit.timeline.slider[0], L.edit.timeline.slider[1]).rect
    slider_width = slider["width"]
    slider_range = round(slider_width * slider_draggable_offset)
    # print("slider_range", slider_range)
    slider_unit = round((slider_width - slider_range)/2)
    # print("slider_unit", slider_unit)
    start_x = slider['x'] + slider_unit
    # print("start_x", start_x)
    x = int(start_x + slider_range * percentage)
    print(x)
    y = slider["y"] + slider["height"] / 2
    # print("y", y)
    h_tap(x, y)
    return True

def scroll_playhead(x_offset: int, speed=None):
    """
    # Function: scroll_playhead
    # Description: Scroll the playhead to with x_offset
    # Parameters:
        :param x_offset: Moving distance of x-coordinate
                        - positive: swipe to the left
                        - negative: swipe to the right
        :param speed: 1 is fastest (slower is more accurate)
    # Return: None
    # Note: length of x to trigger swiping is 25
    # Author: Hausen
    """
    try:
        playhead = driver.find_element(*L.edit.timeline.playhead)
        if speed is None:
            speed = x_offset // 30
        x_split = x_offset / speed
        y = playhead.rect['y'] + playhead.rect['height']/2

        touch_action = TouchAction(driver)
        touch_action.press(playhead)
        for times in range(speed):
            x_offset -= x_split
            touch_action.move_to(x=x_offset, y=y)
        touch_action.release().perform()
        return True
    except Exception:
        traceback.print_exc()
        return False


playhead = driver.find_element(*L.edit.timeline.playhead).rect
x_start = playhead['x']
y = playhead['y']
x_end = x_start - 500

driver.swipe(x_start, y, x_end, y, 10000)




# driver.quit()
