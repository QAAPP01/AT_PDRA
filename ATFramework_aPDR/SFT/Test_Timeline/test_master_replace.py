import time
import pytest
import allure

from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage
import ATFramework_aPDR.pages.locator as L
from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver
from ATFramework_aPDR.SFT.Test_Timeline.TestBase import TestBase


@pytest.fixture(scope='class', autouse=True)
def class_setup(shortcut, driver):
    driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
    page_main, *_ = shortcut
    page_main.enter_launcher()
    page_main.subscribe()
    page_main.enter_timeline()
    yield
    driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')


@allure.feature('Replace Video')
class TestMasterReplaceVideo(TestBase):

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.page_main.enter_timeline(skip_media=False)
        self.original_preview = self.page_edit.get_preview_pic()
        yield
        self.click(L.edit.menu.home)

    @allure.story('Replace button function')
    def test_video_replace_button(self, driver: AppiumU2Driver):
        try:
            driver.implicit_wait(5)
            assert self.page_edit.select_from_bottom_edit_menu('Replace')
            self.click(L.import_media.media_library.back)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace video to video')
    def test_replace_video_to_video(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.page_media.select_media_by_order(order=2)
            driver.implicit_wait(5)
            if self.element(L.edit.replace.ok_btn):
                self.click(L.edit.replace.ok_btn)
            if self.element(L.edit.replace.btn_replace_anyway):
                self.click(L.edit.replace.btn_replace_anyway)
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace video to photo')
    def test_replace_video_to_photo(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            driver.implicit_wait(5)
            self.page_media.switch_to_photo_library()
            driver.implicit_wait(5)
            self.page_media.select_media_by_order(order=2)
            time.sleep(5)
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace video to colorboard')
    def test_replace_video_to_colorboard(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            driver.implicit_wait(5)
            self.page_media.switch_to_photo_library()
            driver.implicit_wait(5)
            self.page_media.select_media_by_order(order=2)
            time.sleep(5)
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')


@allure.feature('Replace Photo')
class TestMasterReplacePhoto(TestBase):

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.page_main.enter_timeline()
        yield
        self.click(L.edit.menu.home)

    @allure.story('Replace photo to video')
    def test_replace_photo_to_video(self):
        try:
            pass

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace photo to photo')
    def test_replace_photo_to_photo(self):
        try:
            pass

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace photo to colorboard')
    def test_replace_photo_to_colorboard(self):
        try:
            pass

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')


@allure.feature('Replace Colorboard')
class TestMasterReplaceColorbaord(TestBase):

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.page_main.enter_timeline()
        yield
        self.click(L.edit.menu.home)

    @allure.story('Replace colorboard to video')
    def test_replace_photo_to_video(self):
        try:
            pass

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace colorboard to photo')
    def test_replace_photo_to_photo(self):
        try:
            pass

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace colorboard to video')
    def test_replace_photo_to_colorboard(self):
        try:
            pass

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {repr(e)}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')
