import inspect
import time
import traceback

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, TimeoutException
from .base_driver import BaseDriver
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import math
import ATFramework_aPDR.configs.driver_config as DriverConfig
import ATFramework_aPDR.configs.app_config as AppConfig
import os
import uuid

from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L

try:
    import cv2
except:
    print ("**Please install OpenCV module: pip install opencv-python**")
    logger ("**Please install OpenCV module: pip install opencv-python**")
    # sys.exit(-1)

class Borg:
    # The borg design pattern is to share state
    # Src: http://code.activestate.com/recipes/66531/
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def is_first_time(self):
        # Has the child class been invoked before?
        result_flag = False
        if len(self.__dict__) == 0:
            result_flag = True

        return result_flag


class AppiumU2Driver(Borg, BaseDriver):
    DEFAULT_TIMEOUT = 10
    DEFAULT_POLL_TIME = 0.1
    implict_wait_value = 5
    
    # Driver Functions
    def __init__(self,DriverConfig, AppConfig, mode="local", desired_caps={}):
        if mode == "local":
            url_remote = "http://{}:4723/wd/hub".format(DriverConfig.ip_local_appium)
        elif mode == "debug":
            url_remote = "http://{}:4725/wd/hub".format(DriverConfig.ip_local_appium)
        elif mode == 'grid':
            url_remote = "http://{}:4444/wd/hub".format(DriverConfig.ip_grid_hub)
            print('url_remote-', url_remote)

        # Constructor
        Borg.__init__(self)
        if self.is_first_time():
            # Do these actions if this the first time this class is initialized
            pass

        # if desired_caps == {}:
        #     desired_caps.update(DriverConfig.android_device)
        #     desired_caps.update(AppConfig.prod_cap)    #TODO need set parameter for this config

        self.driver = webdriver.Remote(url_remote, desired_caps)
        if not ("_implicitly_wait" in dir(self.driver)):
            self.driver._implicitly_wait = self.driver.implicitly_wait
            self.driver.implicitly_wait = self.implicit_wait 


    # ==================================================================================================================
    # Function: stop_driver
    # Description: Stop current driver
    # Parameters: N/A
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def stop_driver(self):
        try:
            self.driver.quit()
            return True
        except Exception as err:
            raise Exception(err)

    # App Management Functions
    # ==================================================================================================================
    # Function: install_app
    # Description: Install specified app
    # Parameters: apk_path, package
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def install_app(self, apk_path, package):
        try:
            self.driver.install_app(apk_path)
        except Exception as err:
            raise Exception(err)

        return self.driver.is_app_installed(package)

    # ==================================================================================================================
    # Function: remove_app
    # Description: Remove specified app
    # Parameters: package
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def remove_app(self, package):
        try:
            self.driver.remove_app(package)
        except Exception as err:
            raise Exception(err)

        return not self.driver.is_app_installed(package)

    # ==================================================================================================================
    # Function: start_app
    # Description: Start specified app
    # Parameters: package
    # Return: True/False
    # Note: Include verification of app status
    #       0 is not installed.
    #       1 is not running.
    #       2 is running in background or suspended
    #       3 is running in background. /
    #       4 is running in foreground. (number)
    # Author: Bill
    # ==================================================================================================================
    def start_app(self, package):
        try:
            self.driver.launch_app()
        except Exception:
            return False

        return self.driver.query_app_state(package) > 1

    # ==================================================================================================================
    # Function: stop_app
    # Description: Stop specified app
    # Parameters: package
    # Return: True/False
    # Note: Include verification of app status
    #       0 is not installed.
    #       1 is not running.
    #       2 is running in background or suspended
    #       3 is running in background. /
    #       4 is running in foreground. (number)
    # Author: Bill
    # ==================================================================================================================
    def stop_app(self, package):
        try:
            self.driver.close_app()
        except Exception:
            return False

        return self.driver.query_app_state(package) == 1

    # ==================================================================================================================
    # Function: activate_app
    # Description: Activate specified app
    # Parameters: package
    # Return: True/False
    # Note: Include verification of app status
    #       0 is not installed.
    #       1 is not running.
    #       2 is running in background or suspended
    #       3 is running in background. /
    #       4 is running in foreground. (number)
    # Author: Bill
    # ==================================================================================================================
    def activate_app(self, package):
        try:
            self.driver.activate_app(package)
        except Exception:
            return False

        return self.driver.query_app_state(package) == 4

    # ==================================================================================================================
    # Function: background_app
    # Description: Put specified app to background
    # Parameters: package
    # Return: True/False
    # Note: Include verification of app status
    #       0 is not installed.
    #       1 is not running.
    #       2 is running in background or suspended
    #       3 is running in background. /
    #       4 is running in foreground. (number)
    # Author: Bill
    # ==================================================================================================================
    def background_app(self, package):
        try:
            self.driver.close_app()
        except Exception as err:
            raise Exception(err)

        return 2 <= self.driver.query_app_state(package) <= 3

    # ==================================================================================================================
    # Function: reset_app
    # Description: Reset specified app
    # Parameters: package
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def reset_app(self, package):
        # Reset app
        try:
            self.driver.reset()
            return True
        except Exception as err:
            raise Exception(err)

    # Orientation Control Functions
    # ==================================================================================================================
    # Function: get_orientation
    # Description: Return device's current orientation (LANDSCAPE|PORTRAIT)
    # Parameters: N/A
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def get_orientation(self):
        try:
            return self.driver.orientation()
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: set_orientation
    # Description: Set device's current orientation (LANDSCAPE|PORTRAIT)
    # Parameters: orientation (LANDSCAPE|PORTRAIT)
    # Return: True/False
    # Note: Include verification of orientation after setting
    # Author: Bill
    # ==================================================================================================================
    def set_orientation(self, orientation):
        try:
            self.driver.orientation = orientation
        except Exception:
            return False

        return self.get_orientation() == orientation

    # ==================================================================================================================
    # Function: freeze_orientation
    # Description: Freeze device's current orientation
    # Parameters: Enabled (True = Freeze  & False = Unfreeze)
    # Return: False (Appium U2 driver does not support this function)
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def freeze_orientation(self, enabled):
        print("Appium U2 driver does not support freeze_orientation function")
        return False

    # Misc. Operation Functions
    # ==================================================================================================================
    # Function: implicit_wait
    # Description: Set implicit wait time to driver
    # Parameters: time (seconds)
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def implicit_wait(self, time=None):
        try:
            result = self.implict_wait_value
        except:
            logger("<<No default implicitly_wait found, set it as 5>>")
            self.implict_wait_value = 5
        if time == None:
            return result
        else:
            self.implict_wait_value = time
        try:
            # logger("set new implicitly_wait: %s" % time )
            self.driver._implicitly_wait(time)
            return time
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: open_notification
    # Description: Open Android notifications (Emulator Only?)
    # Parameters: N/A
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def open_notification(self):
        try:
            self.driver.open_notifications()
            return True
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: put_file
    # Description: Put local file to mobile device
    # Parameters: path, file
    # Return: True/False
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def put_file(self, path, file):
        try:
            with open(file, 'rb') as selected_file:
                data = str(selected_file.read())
            self.driver.push_file(path, data.encode('base64'))
            return True
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: get_file
    # Description: Get file from mobile device
    # Parameters: path
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def get_file(self, path):
        try:
            self.driver.pull_file(path)
            return True
        except Exception as err:
            raise Exception(err)

    # Element Operation Functions
    # ==================================================================================================================
    # Function: get_text
    # Description: Get the text of a given locator or the 'None' object if the element is not found
    # Parameters: locator
    # Return: Text/None
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def get_text(self, locator):
        try:
            text = self.get_element(locator).text
            return text.encode('utf-8')
        except Exception:
            print("ERROR: %s page cannot get text from %s element" % (self, locator))
        raise Exception

    # ==================================================================================================================
    # Function: set_text
    # Description: Set the text to a given locator or the 'None' object if failed to set text to target element
    # Parameters: locator, text, clear_flag
    # Return: Text/None
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def set_text(self, locator, text, clear_flag=True):
        try:
            text_area = self.get_element(locator)
            if clear_flag is True:
                try:
                    text_area.clear()
                except Exception:
                    print("ERROR: %s page cannot clear the text field: %s" % (self, locator))
                    raise Exception
            try:
                return text_area.send_keys(text)
            except Exception:
                print("ERROR: %s page cannot set the text field: %s" % (self, locator))
                raise Exception
        except Exception:
            print("ERROR: %s page cannot find the text field: %s" % (self, locator))
            raise Exception

    # ==================================================================================================================
    # Function: get_element
    # Description: Get the element of a given locator or the 'None' object if the element is not found
    # Parameters: locator, timeout, poll_frequency
    # Return: Element/None
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def get_element(self, locator, timeout=DEFAULT_TIMEOUT, poll_frequency=DEFAULT_POLL_TIME):
        start = time.time()
        try:
            if type(locator) == tuple:
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
                # logger(f"[Found ({round(time.time() - start, 2)})] {locator}")
                return element
            else:
                return locator
        except TimeoutException:
            logger(f"[No found ({round(time.time()-start, 2)})] {locator}")
            return False

    # ==================================================================================================================
    # Function: get_elements
    # Description: Get the elements of a given locator or the 'None' object if the element is not found
    # Parameters: locator, index, timeout, poll_frequency
    # Return: Element(s)/None
    # Note: N/A
    # Author: Bill, Jim
    # ==================================================================================================================
    def get_elements(self, locator, index=None, timeout=DEFAULT_TIMEOUT, poll_frequency=DEFAULT_POLL_TIME):
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            elements = wait.until(EC.presence_of_all_elements_located(locator), "Element not found with locator: " + str(locator))
            return elements[index] if index else elements
        except TimeoutException:
            print("ERROR: %s page cannot find %s element" % (self, locator))
            raise Exception

    # ==================================================================================================================
    # Function: click_element
    # Description: Click the element of a given locator
    # Parameters: locator
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def click_element(self, locator):
        try:
            self.get_element(locator).click()
            return True
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: tap_coordinate
    # Description: Tap the x, y coordinate
    # Parameters: x, y
    # Return: True/False
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================
    def tap_coordinate(self, x, y):
        try:
            actions = TouchAction(self.driver)
            actions.tap(x=x, y=y)
            actions.perform()
            return True
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: tap_element
    # Description: Tap the element of a given locator
    # Parameters: locator
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def tap_element(self, locator):
        try:
            actions = TouchAction(self.driver)
            actions.tap(self.get_element(locator))
            actions.perform()
            return True
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: long_press_element
    # Description: Long press the element of a given locator
    # Parameters: locator
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def long_press_element(self, locator):
        try:
            actions = TouchAction(self.driver)
            actions.long_press(self.get_element(locator))
            actions.perform()
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: swipe_element
    # Description: Swipe from center of element toward specified direction (May not support swipe to switch page)
    # Parameters: locator, direction (left|right|up|down)
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def swipe_element(self, locator, direction, offset=0.55):
        window_rect = self.driver.get_window_size()
        element_rect = self.get_element(locator).rect
        start_x = element_rect['x'] + element_rect['width'] / 2
        start_y = element_rect['y'] + element_rect['height'] / 2
        end_x = start_x
        end_y = start_y
        if direction == "left":
            end_x = start_x - ( window_rect['width'] * offset if offset < 1 else offset)
        elif direction == "right":
            end_x = start_x + ( window_rect['width'] * offset if offset < 1 else offset)
        elif direction == "up":
            end_y = start_y - ( window_rect['height'] * offset if offset < 1 else offset)
        elif direction == "down":
            end_y = start_y + ( window_rect['height'] * offset if offset < 1 else offset)
        else:
            print("Invalid direction")
            return False
        end_x = end_x if 0 <= end_x <=  window_rect['width'] else window_rect['width'] 
        end_y = end_y if 0 <= end_y <=  window_rect['height'] else window_rect['height']
        # print ("swip=",start_x, start_y, end_x, end_y)
        self.driver.swipe(start_x, start_y, end_x, end_y)
        return True

    # ==================================================================================================================
    # Function: swipe_to_element
    # Description: Swipe from center of element toward specified direction till target displayed
    # Parameters: locator, direction (left|right|up|down), target_locator
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def swipe_to_element(self, locator, direction, target_locator):
        for i in range(100):
            if self.is_element_displayed(locator):
                return True
            else:
                self.swipe_element(locator, direction)
        return False

    # ==================================================================================================================
    # Function: drag_element
    # Description: Drag the element of a given locator to target element
    # Parameters: src_locator, dst_locator
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def drag_element(self, src_locator, dst_locator):
        try:
            src_element = self.get_element(src_locator)
            dst_element = self.get_element(dst_locator)
            self.driver.drag_and_drop(src_element, dst_element)
        except Exception:
            return False

    # ==================================================================================================================
    # Function: pinch_element
    # Description: Pinch the element of a given locator to specified percent and steps
    # Parameters: locator, percent, steps
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def pinch_element(self, locator, percent=200, steps=50):
        try:
            self.driver.pinch(self.get_element(locator), percent, steps)
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: zoom_element
    # Description: Zoom the element of a given locator to specified percent and steps
    # Parameters: locator, percent, steps
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def zoom_element(self, locator, percent=200, steps=50):
        try:
            self.driver.zoom(self.get_element(locator), percent, steps)
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: rotate_element
    # Description: Rotate the element of a given locator to specified angle clockwise
    # Parameters: locator, angle
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def rotate_element(self, locator, angle):
        element_rect = self.get_element(locator).rect
        x1 = element_rect['x'] + element_rect['width'] / 2
        y1 = element_rect['y'] + element_rect['height'] / 2
        y2 = element_rect['y']
        a = angle * math.pi / 180
        ax2 = int((x2 - x1) * math.cos(a) - (y2 - y1) * math.sin(a)) + x1
        ay2 = int((y2 - y1) * math.cos(a) + (x2 - x1) * math.sin(a)) + y1

        try:
            a1 = TouchAction()
            a1.press(x1, y1)
            a1.move_to(x1, y1)
            a1.release()

            a2 = TouchAction()
            a2.press(x1, y2)
            a2.move_to(ax2, ay2)
            a2.release()

            ma = MultiAction(self.driver)
            ma.add(a1, a2)
            ma.perform()
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: set_checkbox
    # Description: Set the checkbox of a given locator to specified status
    # Parameters: locator, status
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def set_checkbox(self, locator, status):
        try:
            if self.get_element(locator).is_selected() != status:
                self.click_element(locator)
        except Exception:
            return False
        return self.get_element(locator).is_selected() == status

    # ==================================================================================================================
    # Function: set_dropdown
    # Description: Set the dopdown value of a given locator to specified item
    # Parameters: locator, status
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def set_dropdown(self, locator, item):
        try:
            self.click_element(locator)
            item_locator = (MobileBy.ANDROID_UIAUTOMATOR, item)
            self.click_element(item_locator)
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: set_slider
    # Description: Set the slider value of a given locator to specified percent
    # Parameters: locator, percent
    # Return: True/False
    # Note: Not Tested
    # Author: Bill
    # ==================================================================================================================
    def set_slider(self, locator, percentage):
        try:
            slider = self.get_element(locator)
            start_x = slider.location["x"]
            start_y = slider.location["y"]
            end_x = start_x + (percentage * slider.size["width"])

            actions = TouchAction(self.driver)
            actions.press(x=start_x,y= start_y)
            actions.move_to(x=end_x, y=start_y)
            actions.release()
            actions.perform()
        except Exception:
            return False

        # ensure value had been set
        value = slider.get_attribute('text')
        if round(int(float(value))/slider.size["width"], 1) == percentage:
            return True
        else:
            return False
    # ==================================================================================================================
    # Function: get_toast_text
    # Description: Get the toast text
    # Parameters: N/A
    # Return: False (Appium U2 driver does not support this function)
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def get_toast_text(self):
        print("Appium U2 driver does not support get_toast_text function")
        return False

    # Check Element Status Functions
    # ==================================================================================================================
    # Function: is_element_displayed
    # Description: Check if the element of a give locator is displayed
    # Parameters: locator
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def is_element_displayed(self, locator):
        return self.get_element(locator).is_displayed()

    # Wait Element Functions
    # ==================================================================================================================
    # Function: wait_until_element_exist
    # Description: Wait until the element of a give locator is exist
    # Parameters: locator, timeout
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def wait_until_element_exist(self, locator, timeout=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator), "Locator still exist: " + str(locator))
            return True
        except Exception:
            print("ERROR: %s page's %s element does not exist" % (self, locator))
        return None

    # ==================================================================================================================
    # Function: wait_until_element_not_exist
    # Description: Wait until the element of a give locator is not exist
    # Parameters: locator, timeout
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def wait_until_element_not_exist(self, locator, timeout=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until_not(EC.presence_of_element_located(locator), "Locator still exist: " + str(locator))
            return True
        except Exception:
            print("ERROR: %s page's %s element still exist" % (self, locator))
        return None

    # ==================================================================================================================
    # Function: wait_until_element_selected
    # Description: Wait until the element of a give locator is selected
    # Parameters: locator, timeout
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def wait_until_element_selected(self, locator, timeout=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.element_located_to_be_selected(locator), "Element is selected: " + str(locator))
            return True
        except Exception:
            print("ERROR: %s page's %s element does not exist" % (self, locator))
        return None

    # ==================================================================================================================
    # Function: wait_until_element_clickable
    # Description: Wait until the element of a give locator is clickable
    # Parameters: locator, timeout
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def wait_until_element_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.element_to_be_clickable(locator), "Element is enabled: " + str(locator))
            return True
        except Exception:
            print("ERROR: %s page's %s element does not exist" % (self, locator))
        return None

    # Mobile Gesture Functions
    # ==================================================================================================================
    # Function: swipe_up
    # Description: Swipe upward
    # Parameters: N/A
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def swipe_up(self):
        try:
            size = self.driver.get_window_size()
            x1 = size['width'] * 0.5
            y1 = size['height'] * 0.75
            y2 = size['height'] * 0.25
            self.driver.swipe(x1, y1, x1, y2)
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: swipe_down
    # Description: Swipe downward
    # Parameters: N/A
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def swipe_down(self):
        try:
            size = self.driver.get_window_size()
            x1 = size['width'] * 0.5
            y1 = size['height'] * 0.25
            y2 = size['height'] * 0.75
            self.driver.swipe(x1, y1, x1, y2)
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: swipe_left
    # Description: Swipe leftward
    # Parameters: N/A
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def swipe_left(self):
        try:
            size = self.driver.get_window_size()
            x1 = size['width'] * 0.9
            y1 = size['height'] * 0.5
            x2 = size['width'] * 0.1
            self.driver.swipe(x1, y1, x2, y1)
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: swipe_right
    # Description: Swipe rightward
    # Parameters: N/A
    # Return: True/False
    # Note: N/A
    # Author: Bill
    # ==================================================================================================================
    def swipe_right(self):
        try:
            size = self.driver.get_window_size()
            x1 = size['width'] * 0.25
            y1 = size['height'] * 0.5
            x2 = size['width'] * 0.75
            self.driver.swipe(x1, y1, x2, y1)
            return True
        except Exception:
            return False

    # ==================================================================================================================
    # Function: tap_by_location
    # Description: tap by location
    # Parameters: N/A
    # Return: True/raise Exception
    # Note: N/A
    # Author: Jim
    # ==================================================================================================================
    def tap_screen_center(self, x_shift=0, y_shift=0):
        try:
            size = self.driver.get_window_size()
            x = int(size['width'] * 0.5) + int(x_shift)
            y = int(size['height'] * 0.5) + int(y_shift)
            TouchAction(self.driver).tap(None, x, y, 1).perform()
        except Exception as err:
            raise Exception(err)
        return True
        
    def save_pic(self,elem=None,last=False,file=None, offset=None):
        '''
            # Function: save_pic
            # Description: save_pic
            # Parameters: (element locator , use last rect directly, file path, \
                          offset:{'w':w,'y':y,'width':width,'height':height})
            # Return: img full path
            # Note: OpenCV must be installed
            # Author: Miti
        '''
        global last_rect
        if type(elem) == tuple: # convert from tuple to elem 
            elem = self.driver.find_element(elem[0],elem[1])
        path = os.getenv('temp', os.path.dirname(__file__))
        path_full = file if file else "%s/temp.png" % path
        if not self.driver.get_screenshot_as_file(path_full):
            raise Exception("Save image error: %s" % path_full)
        
        if elem:
            rect = elem.rect
        else:
            rect = self.driver.get_window_size()
            rect.update({"x":0,"y":0})
        if offset:
            for key in offset.keys():
                rect[key] += offset[key]
        if last:
            rect = last_rect
        last_rect = rect
        im = cv2.imread(path_full)
        im_crop = im[rect['y'] : rect['y']+rect['height'],rect['x']:rect['x']+rect['width']]
        path_crop = "%s/%s.png" % (path,uuid.uuid4())
        cv2.imwrite(path_crop, im_crop)
        return os.path.abspath(path_crop)
        
    def zoom(self,locator=None,start=0.1, end=0.5):
        '''
           locator: if None, target is whole screen
           start : if < 1, percentage of the element. if > 1 ,relative position
           end : as start, 0.5 -> right finger x move left 0.25, left finger move right 0.25. Y as X.
           time : action time (div by 10)
        '''
        logger("Start pinch")
        if not locator:
            width , height = self.driver.get_window_size().values()
            x , y = 0,0
        else:
            elem = self.driver.find_element(locator[0],locator[1])
            height , width , x, y = elem.rect.values()
        
        x_start1 = x + (width*(1-start-end/2) if start < 1 else start)
        y_start1 = y + (height*(start+end/2) if start < 1 else start)
        x_start2 = x + (width*(start+end/2) if start < 1 else start)
        y_start2 = y + (height*(1-start-end/2) if start < 1 else start)

        x_end1 = x + (width*(1-start) if end < 1 else end)
        y_end1 = y + (height*start if end < 1 else end)
        x_end2 = x + (width*start if end < 1 else end)
        y_end2 = y + (height*(1-start) if end < 1 else end)
        
        
        act1=TouchAction(self.driver)
        act2=TouchAction(self.driver)
        zoom=MultiAction(self.driver)
        
        x_step = width * (1-start*2-end)/2/10 if start < 1 else width/10
        y_step = height * (1-start*2-end)/2/10 if start < 1 else height/10
        
        act1.press(x=x_start1, y=y_start1).wait(500)
        act2.press(x=x_start2, y=y_start2).wait(500)
        logger("[pinch] x=%s , y=%s , width=%s , height=%s " % (x,y,width,height))
        logger("act1 = %s,%s -> %s,%s " % (x_start1,y_start1,x_end1,y_end1) )
        logger("act2 = %s,%s -> %s,%s " % (x_start2,y_start2,x_end2,y_end2) )
        logger("x_step = %s , y_step = %s " % (x_step,y_step))
        
        for i in range(1,11):
            act1 = act1.move_to(x=x_start1+i*x_step, y=y_start1-i*y_step).wait(10)
            act2 = act2.move_to(x=x_start2-i*x_step, y=y_start2+i*y_step).wait(10)
        
        act1.release()
        act2.release()
        
        zoom.add(act1,act2)
        zoom.perform()

    def drag_slider_to_left(self):
        try:
            slider = L.edit.sub_tool.slider
            slider_value = L.edit.sub_tool.slider_value
            slider_rect = self.driver.find_element(slider[0],slider[1]).rect
            slider_value_rect = self.driver.find_element(slider_value[0],slider_value[1]).rect
            x_start = slider_value_rect['x'] + slider_value_rect['width'] // 2
            x_end = x_start - slider_rect['width'] // 4
            y_center = slider_rect['y'] + slider_rect['height'] // 2
            TouchAction(self.driver).press(x=x_start, y=y_center, pressure=1).wait(500).move_to(x=x_end, y=y_center).release().perform()
            return True
        except Exception as err:
            raise Exception(err)

    def drag_slider_to_right(self):
        try:
            slider = L.edit.sub_tool.slider
            slider_value = L.edit.sub_tool.slider_value
            slider_rect = self.driver.find_element(slider[0],slider[1]).rect
            slider_value_rect = self.driver.find_element(slider_value[0],slider_value[1]).rect
            x_start = slider_value_rect['x'] + slider_value_rect['width'] // 2
            x_end = x_start + slider_rect['width'] // 4
            y_center = slider_rect['y'] + slider_rect['height'] // 2
            TouchAction(self.driver).press(x=x_start, y=y_center, pressure=1).wait(500).move_to(x=x_end, y=y_center).release().perform()
            return True
        except Exception as err:
            raise Exception(err)


    def drag_slider_from_center_to_left(self, locator):
        try:
            slider_rect = self.driver.find_element(locator[0],locator[1]).rect
            x_center = slider_rect['x'] + int(slider_rect['width'] / 2)
            y_center = slider_rect['y'] + int(slider_rect['height'] / 2)
            TouchAction(self.driver).press(None, x_center, y_center, 1).wait(500).move_to(None, x_center - int(
                slider_rect['width'] / 4), y_center).release().perform()
        except Exception as err:
            raise Exception(err)
        return True

    def drag_slider_from_center_to_right(self, locator):
        try:
            slider_rect = self.driver.find_element(locator[0],locator[1]).rect
            x_center = slider_rect['x'] + int(slider_rect['width'] / 2)
            y_center = slider_rect['y'] + int(slider_rect['height'] / 2)
            TouchAction(self.driver).press(None, x_center, y_center, 1).wait(500).move_to(None, x_center + int(
                slider_rect['width'] / 4), y_center).release().perform()
        except Exception as err:
            raise Exception(err)
        return True

    def drag_slider_from_left_to_right(self, locator=L.edit.sub_tool.slider):
        try:
            slider_rect = self.driver.find_element(locator[0],locator[1]).rect
            y_center = slider_rect['y'] + int(slider_rect['height'] / 2)
            TouchAction(self.driver).press(None, slider_rect['x'], y_center, 1).wait(500).move_to(None, slider_rect['x'] + int(
                slider_rect['width']), y_center).release().perform()
        except Exception as err:
            raise Exception(err)
        return True

    def drag_slider_to_max(self, locator=L.edit.sub_tool.slider):
        try:
            if isinstance(locator, tuple):
                slider = self.driver.find_element(locator[0], locator[1])
            else:
                slider = locator

            slider_rect = slider.rect

            actions = ActionChains(self.driver)
            actions.move_to_element(slider)
            actions.click_and_hold()
            actions.move_by_offset(slider_rect['width'] // 2, 0)
            actions.release()
            actions.perform()

            return True
        except Exception as err:
            raise Exception(err)

    def drag_slider_to_min(self, locator=L.edit.sub_tool.slider):
        try:
            if isinstance(locator, tuple):
                slider = self.driver.find_element(locator[0], locator[1])
            else:
                slider = locator

            slider_rect = slider.rect

            actions = ActionChains(self.driver)
            actions.move_to_element(slider)
            actions.click_and_hold()
            actions.move_by_offset(-slider_rect['width'] // 2, 0)
            actions.release()
            actions.perform()

            return True
        except Exception as err:
            raise Exception(err)

    # ==================================================================================================================
    # Function: click_and_hold_and_screenshot
    # Description: click_and_hold_and_screenshot
    # Note: click_and_hold_and_screenshot
    # Author: Hausen
    # ==================================================================================================================
    def click_and_hold_and_screenshot(self, button, preview=None):
        path = os.getenv('temp', os.path.dirname(__file__))
        file_save = "%s/%s.png" % (path, uuid.uuid4())
        path_save = os.path.abspath(file_save)

        if preview:
            try:
                action_chains = ActionChains(self.driver)
                element = self.driver.find_element(*button)
                action_chains.click_and_hold(element).perform()

                screenshot_area = self.driver.find_element(*preview)
                screenshot_area.screenshot(file_save)

                action_chains = ActionChains(self.driver)
                action_chains.click(element).perform()

            except Exception:
                traceback.print_exc()
                return False
        else:
            self.driver.save_screenshot(file_save)
        logger(f'screenshot saved: {path_save}')

        return path_save

    # ==================================================================================================================
    # Function: double_tap_element
    # Description: double_tap_element
    # Parameters: locator(tuple), (opt) interval=0.2
    # Return: True/False
    # Note: n/a
    # Author: Hausen
    # ==================================================================================================================
    def double_tap_element(self, locator):
        try:
            actions = TouchAction(self.driver)
            element = self.get_element(locator)
            actions.tap(element)
            actions.tap(element)
            actions.perform()
            time.sleep(0.5)
            return True

        except Exception:
            traceback.print_exc()
            return False

    def swipe_element_up(self, locator, x_offset=0, y_offset=0, speed=3):
        try:
            if speed < 1:
                speed = 1

            window = self.driver.get_window_size()
            window_width = window['width']
            widow_height = window['height']
            window_center = [window_width // 2, widow_height // 2]

            element = self.get_element(locator)
            element_rect = element.rect
            element_right_top = [element_rect['x'] + x_offset, element_rect['y'] + y_offset]

            delta_x = element_right_top[0] - window_center[0] / speed
            delta_y = element_right_top[1] - window_center[1] / speed

            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(element_right_top[0], element_right_top[1])
            actions.w3c_actions.pointer_action.pointer_down()

            for i in range(speed):
                element_right_top[0] = int(element_right_top[0] - delta_x)
                element_right_top[1] = int(element_right_top[1] - delta_y)
                actions.w3c_actions.pointer_action.move_to_location(element_right_top[0], element_right_top[1])

            actions.w3c_actions.pointer_action.release()
            actions.perform()

            return True
        except Exception as err:
            logger(f"[Error] {err}")
            raise Exception(err)

    def click_element_top_center(self, locator):
        try:
            element = self.get_element(locator)
            element_rect = element.rect
            x = element_rect['x'] + element_rect['width'] // 2
            y = element_rect['y']

            actions = ActionChains(self.driver)
            touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")

            actions.w3c_actions = ActionBuilder(self.driver, mouse=touch_input)
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pointer_up()

            # 執行動作
            actions.perform()
        except Exception as err:
            raise Exception(err)
        return True
