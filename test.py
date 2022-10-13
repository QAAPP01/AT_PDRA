from os import popen

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


# def swipe_element(element_b, element_a, speed=5):
#     try:
#         if speed < 1:
#             speed = 1
#         element_b_rect = element_b.rect
#         start_x = element_b_rect['x'] + element_b_rect['width'] / 2
#         start_y = element_b_rect['y'] + element_b_rect['height'] / 2
#         element_a_rect = element_a.rect
#         end_x = element_a_rect['x'] + element_a_rect['width'] / 2
#         end_y = element_a_rect['y'] + element_a_rect['height'] / 2
#
#         x_offset = (start_x - end_x) / speed
#         y_offset = (start_y - end_y) / speed
#         end_x = start_x
#         end_y = start_y
#         for i in range(speed):
#             start_x = end_x
#             start_y = end_y
#             end_x = int(end_x - x_offset)
#             end_y = int(end_y - y_offset)
#             driver.swipe(start_x, start_y, end_x, end_y)
#         return True
#     except Exception as err:
#         logger(f"[Error] {err}")
#         return False

def swipe_element(element_b, element_a, speed=10):
    try:
        if speed < 1:
            speed = 1
        element_b_rect = element_b.rect
        start_x = element_b_rect['x']
        start_y = element_b_rect['y']
        element_a_rect = element_a.rect
        end_x = element_a_rect['x']
        end_y = element_a_rect['y']

        x_offset = (start_x - end_x) / speed
        y_offset = (start_y - end_y) / speed

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()

        for i in range(speed):
            start_x = int(start_x - x_offset)
            start_y = int(start_y - y_offset)
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return True
    except Exception as err:
        logger(f"[Error] {err}")
        return False


locator = Intro_Video.intro_category
for i in range(10):
    category = driver.find_elements(locator[0], locator[1])
    swipe_element(category[2], category[0])



