import time
import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as S
from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage
from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver


@pytest.fixture(scope="module", autouse=True)
def module_setup(driver):
    driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
    yield
    driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')


@allure.feature('Replace Video')
class TestMasterReplaceVideo:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, *_ = shortcut
        page_main.enter_launcher()
        page_main, page_edit, *_ = shortcut
        click = page_main.h_click
        click(L.main.main.new_project)
        click(L.import_media.media_library.media(index=1))
        click(L.import_media.media_library.apply)
        click(L.edit.timeline.clip())
        yield
        click(L.edit.menu.home)

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.click(L.main.main.new_project)
        self.click(L.import_media.media_library.media(index=3))
        self.click(L.import_media.media_library.apply)
        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.clip())
        yield
        self.click(L.edit.menu.home)

    @allure.story('Replace button function')
    def test_video_replace_button(self, driver: AppiumU2Driver):
        try:
            assert 0
            assert self.page_edit.select_from_bottom_edit_menu('Replace')

        except Exception as e:
            if type(e) is AssertionError:
                logger(Exception)
                #logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace video to video')
    def test_replace_video_to_video(self, driver):
        try:
            driver.implicit_wait(5)
            self.click(L.import_media.media_library.media(index=1))
            driver.implicit_wait(5)
            if self.element(L.edit.replace.ok_btn, timeout=3):
                self.click(L.edit.replace.ok_btn)
            if self.element(L.edit.replace.btn_replace_anyway, timeout=3):
                self.click(L.edit.replace.btn_replace_anyway)
            if self.element(L.import_media.media_library.dialog_ok):
                self.click(L.import_media.media_library.dialog_ok)

            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(),
                                    7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @pytest.mark.skip
    @allure.story('Replace video to photo')
    def test_replace_video_to_photo(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            driver.implicit_wait(5)
            self.page_media.switch_to_photo_library()
            driver.implicit_wait(5)
            self.click(L.import_media.media_library.media(index=2))
            time.sleep(5)

            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(),
                                    7).compare_image()

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

    @pytest.mark.skip
    @allure.story('Replace video to colorboard')
    def test_replace_video_to_colorboard(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            driver.implicit_wait(5)
            self.click(L.import_media.media_library.color_board)
            driver.implicit_wait(5)
            self.click(L.import_media.media_library.media(index=5))
            time.sleep(5)
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')


@pytest.mark.skip
@allure.feature('Replace Photo')
class TestMasterReplacePhoto:

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
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')


@pytest.mark.skip
@allure.feature('Replace Colorboard')
class TestMasterReplaceColorbaord:

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
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')
