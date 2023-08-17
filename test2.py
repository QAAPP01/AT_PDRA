import os

from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# from ATFramework_aPDR.pages.locator import locator as L
# from ATFramework_aPDR.pages.locator.locator_type import *

# 創建WebDriver實例，連接至Appium Server
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'device',
    "appPackage": "com.cyberlink.powerdirector.DRA140225_01",
    "appActivity": "com.cyberlink.powerdirector.splash.SplashActivity",
    'autoGrantPermissions': False,
    "noReset": False,
    "autoLaunch": True,
    'udid': 'RFCW2198L7B'
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


is_audio_playing = driver.execute_script(
    'const ctx = context;'
    'const am = ctx.getSystemService(ctx.AUDIO_SERVICE); '
    'return am.isMusicActive();')

print(is_audio_playing)

# # 關閉WebDriver連線
# driver.quit()
