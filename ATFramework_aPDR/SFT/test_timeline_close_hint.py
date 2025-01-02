import time
import traceback
import pytest
import allure
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.ATFramework.utils.log import logger


@allure.epic("Timeline - Close Hints")
class Test_Timeline_Close_Hint:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut, driver):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

        self.driver = driver

    @pytest.fixture(scope="module")
    def data(self):
        data = {'last_result': True}
        yield data

    def last_is_fail(self, data):
        if not data['last_result']:
            data['last_result'] = True
            self.page_main.relaunch()
            return True
        return False

    @allure.feature("Close new timeline mode hint")
    def test_close_new_timeline_mode_hint(self, data):
        try:
            self.page_main.enter_timeline()
            self.click(id('top_toolbar_back'))
            self.click(id('set_default'))
            self.click(id('tv_continue'))
            self.click(id('tv_hint'))

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Close overlay hint")
    def test_close_overlay_hint(self, data):
        try:
            self.page_edit.add_pip_media('photo')
            self.click(id('iv_hint'))
        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Close transition hint")
    def test_close_transition_hint(self, data):
        try:
            if not self.click(L.edit.preview.import_tips_icon, timeout=1):
                if not self.click(L.edit.timeline.main_track_import, timeout=1):
                    if not self.click(L.edit.timeline.main_track_import_float, timeout=1):
                        logger('[Warning] No import button')
            self.click(find_string('Overlay'))
            self.click(find_string('Photo'))
            self.click(xpath('(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[1]'))
            self.click(xpath('(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[2]'))
            self.click(L.import_media.media_library.apply)
            self.click(id('transition_hint'))
        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Close full screen hint")
    def test_close_full_screen_hint(self, data):
        try:
            self.click(L.edit.menu.play)
            self.click(L.edit.preview.help_not_show_tip_again)
            self.driver.driver.back()
        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise