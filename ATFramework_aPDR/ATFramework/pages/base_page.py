# This is the base page which defines attributes and methods that all other pages will share

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


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



class BasePage(Borg, unittest.TestCase):
    DEFAULT_TIMEOUT = 5
    DEFAULT_POLL_TIME = 0.1
    default_wait = 5
    default_timeout = 30

    def __init__(self, driver):
        Borg.__init__(self)
        self.driver = driver

    # Driver Functions
    def get_driver(self):
        return self.driver

    def set_driver(self, driver):
        self.driver = driver

    def stop_driver(self):
        return self.driver.stop_driver()

    # App Management Functions
    def install_app(self, path, package):
        return self.driver.install_app(path, package)

    def remove_app(self, package):
        return self.driver.remove_app(package)

    def start_app(self, package):
        return self.driver.start_app(package)

    def stop_app(self, package):
        return self.driver.stop_app(package)

    def activate_app(self, package):
        return self.driver.activate_app(package)

    def background_app(self, package):
        return self.driver.background_app(package)

    def reset_app(self, package):
        return self.driver.reset_app(package)

    # Orientation Control Functions
    def get_orientation(self):
        return self.driver.get_orientation()

    def set_orientation(self, orientation):
        return self.driver.set_orientation(orientation)

    def freeze_orientation(self):
        return self.driver.freeze_orientation()

    # Misc. Operation Functions
    def implicit_wait(self, time):
        return self.driver.implicit_wait(time)

    def open_notification(self):
        return self.driver.open_notification()

    def put_file(self, path, file):
        return self.driver.put_file(path, file)

    def get_file(self, path):
        return self.driver.get_file(path)

    def get_snapshot(self, path):
        return self.driver.get_snapshot(path)

    # Mobile Gesture Functions
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # Element Operation Functions
    def get_text(self, locator):
        return self.driver.get_text(locator)

    def set_text(self, locator, text, clear_flag=0):
        return self.driver.set_text(locator, text, clear_flag)

    def get_element(self, locator, timeout=DEFAULT_TIMEOUT, options=None):
        return self.driver.get_element(locator, timeout, options)

    def get_elements(self, locator, index, timeout=DEFAULT_TIMEOUT, options=None):
        return self.driver.get_elements(locator, index, timeout, options)

    def click_element(self, locator):
        return self.driver.click_element(locator)

    def tap_element(self, locator):
        return self.driver.tap_element(locator)

    def tap(self, pos):
        return self.driver.tap(pos)

    def tap_screen_center(self, x=0, y=0):
        return self.driver.tap_screen_center(x, y)

    def double_tap_element(self, locator, interval=0.2):
        return self.driver.double_tap_element(locator, interval)

    def long_press_element(self, locator):
        return self.driver.long_press_element(locator)

    def swipe_element(self, locator, direction,offset=0.55):
        return self.driver.swipe_element(locator, direction,offset)

    def swipe_to_element(self, locator, direction, target_locator):
        return self.driver.swipe_to_element(locator, direction, target_locator)

    def drag_element(self, src_locator, dst_locator):
        return self.driver.drag_element(src_locator, dst_locator)

    def pinch_element(self, locator, percentage, steps):
        return self.driver.pinch_element(locator, percentage, steps)

    def zoom_element(self, locator, percentage, steps):
        return self.driver.zoom_element(locator, percentage, steps)

    def pinch_zoom_element(self, locator, scale):
        return self.driver.pinch_zoom_element(locator, scale)

    def rotate_element(self, locator, angle):
        return self.driver.rotate_element(locator, angle)

    def set_checkbox(self, locator, status):
        return self.driver.set_checkbox(locator, status)

    def set_dropdown(self, locator, item):
        return self.driver.set_combobox(locator, item)

    def set_slider(self, locator, percentage):
        return self.driver.set_slider(locator, percentage)

    def get_toast_text(self):
        return self.driver.get_toast_text()

    def handle_alert(self, flag):
        return self.driver.handle_alert(flag)

    # Check Element Status Functions
    def is_element_displayed(self, locator):
        return self.driver.is_element_displayed(locator)

    def is_element_highlighted(self, locator):
        return self.driver.is_element_highlighted(locator)

    def is_element_enabled(self, locator):
        return self.driver.is_element_enabled(locator)

    # Wait Element Functions
    def wait_until_element_exist(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.driver.wait_until_element_exist(locator, timeout)

    def wait_until_element_not_exist(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.driver.wait_until_element_not_exist(locator, timeout)

    def wait_until_element_selected(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.driver.wait_until_element_selected(locator, timeout)

    def wait_until_element_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.driver.wait_until_element_clickable(locator, timeout)

    def drag_slider_from_center_to_left(self, locator):
        return self.driver.drag_slider_from_center_to_left(locator)

    def drag_slider_from_center_to_right(self, locator):
        return self.driver.drag_slider_from_center_to_right(locator)

    def drag_slider_from_left_to_right(self, locator):
        return self.driver.drag_slider_from_left_to_right(locator)
