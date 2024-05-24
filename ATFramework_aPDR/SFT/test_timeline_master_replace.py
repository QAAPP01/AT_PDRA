import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage
from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver


@allure.feature('Replace Video')
class TestMasterReplaceVideo:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, *_ = shortcut
        page_main.enter_launcher()

        click = page_main.h_click
        click(L.main.new_project)
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

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.clip())
        yield

    @allure.story('Replace button function')
    def test_video_replace_button(self, driver: AppiumU2Driver):
        try:
            assert self.page_edit.select_from_bottom_edit_menu('Replace')
            self.click(L.import_media.media_library.back)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace video to video')
    def test_replace_video_to_video(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.click(L.import_media.media_library.media(index=2))
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

    @allure.story('Replace video to color board')
    def test_replace_video_to_color_board(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            driver.implicit_wait(5)
            self.click(L.import_media.media_library.color_board)
            driver.implicit_wait(5)
            self.click(L.import_media.media_library.media(index=5))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

            # teardown
            self.click(L.edit.menu.home)
            self.click(L.main.new_project)
            self.click(L.import_media.media_library.media(index=1))
            self.click(L.import_media.media_library.apply)
            self.click(L.edit.timeline.clip())

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace video to photo')
    def test_replace_video_to_photo(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.media_library.media(index=2))

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


@allure.feature('Replace Photo')
class TestMasterReplacePhoto:

    @pytest.fixture(scope='class', autouse=True)
    def in_class_setup(self, shortcut, driver):
        page_main, _, page_media, _ = shortcut
        click = page_main.h_click

        page_main.enter_launcher()
        click(L.main.new_project)
        page_media.switch_to_photo_library()
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

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.clip())
        yield

    @allure.story('Replace photo to photo')
    def test_replace_photo_to_photo(self):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.media_library.media(index=2))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace photo to color board')
    def test_replace_photo_to_color_board(self, driver):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.click(L.import_media.media_library.color_board)
            self.click(L.import_media.media_library.media(index=5))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

            # teardown
            self.click(L.edit.menu.home)
            self.click(L.main.new_project)
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.media_library.media(index=1))
            self.click(L.import_media.media_library.apply)
            self.click(L.edit.timeline.clip())

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace photo to video')
    def test_replace_photo_to_video(self):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.page_media.switch_to_video_library()
            self.click(L.import_media.media_library.media(index=1))

            if self.element(L.import_media.media_library.dialog_ok):
                self.click(L.import_media.media_library.dialog_ok)
            self.click(L.edit.replace.ok_btn)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')


@allure.feature('Replace color board')
class TestMasterReplaceColorBoard:

    @pytest.fixture(scope='class', autouse=True)
    def in_class_setup(self, shortcut, driver):
        page_main, _, page_media, _ = shortcut
        click = page_main.h_click

        page_main.enter_launcher()
        click(L.main.new_project)
        click(L.import_media.media_library.color_board)
        click(L.import_media.media_library.media(index=5))
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

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.clip())
        yield

    @allure.story('Replace color board to color board')
    def test_replace_color_board_to_color_board(self):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.click(L.import_media.media_library.color_board)
            self.click(L.import_media.media_library.media(index=11))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace color board to photo')
    def test_replace_color_board_to_photo(self):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.media_library.media(index=2))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')

    @allure.story('Replace color board to video')
    def test_replace_color_board_to_video(self):
        try:
            self.page_edit.select_from_bottom_edit_menu('Replace')
            self.page_media.switch_to_video_library()
            self.click(L.import_media.media_library.media(index=1))

            if self.element(L.import_media.media_library.dialog_ok):
                self.click(L.import_media.media_library.dialog_ok)
            self.click(L.edit.replace.ok_btn)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {repr(e)}')
                text = 'Exception'
            pytest.fail(f'[{text}] {repr(e)}]')
