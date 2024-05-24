import time

import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage
from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver


@allure.feature('Drag clip from master to pip track')
class TestDragClipToPip:

    # @pytest.fixture(scope='class', autouse=True)
    # def class_setup(self, shortcut, driver):
    #     page_main, *_ = shortcut
    #     page_main.enter_launcher()
    #
    #     click = page_main.h_click
    #     click(L.main.new_project)
    #     yield
    #     click(L.edit.menu.home)

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

    def test_drag_master_video_to_pip(self):
        try:
            # Setup
            #self.click(L.import_media.media_library.media(index=1))
            #self.click(L.import_media.media_library.apply)

            pic_base = self.page_edit.get_timeline_pic()

            #self.click(L.edit.timeline.clip())
            #time.sleep(5)
            self.page_edit.drag_timeline_clip('down')

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')




@allure.feature('Drag clip from pip track to master')
class TestDragClipToMaster:
    pass