import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage


def replace_to_video(shortcut):
    page_main, *_ = shortcut
    click = page_main.h_click
    element = page_main.h_get_element
    if element(L.edit.replace.ok_btn, timeout=3):
        click(L.edit.replace.ok_btn)
    if element(L.edit.replace.btn_replace_anyway, timeout=3):
        click(L.edit.replace.btn_replace_anyway)
    if element(L.import_media.media_library.dialog_ok):
        click(L.import_media.media_library.dialog_ok)


@allure.epic('Timeline')
@allure.feature('Master')
class TestMasterReplaceVideo:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut

        page_main.enter_launcher()
        click = page_main.h_click
        click(L.main.new_project)
        click(L.import_media.media_library.media(index=1))
        click(L.import_media.media_library.apply)
        click(L.edit.timeline.clip())
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.clip())
        self.replace_to_video = replace_to_video
        yield

    @allure.story('Video')
    @allure.title('Replace')
    @allure.step('Video to Video')
    def test_replace_video_to_video(self, driver, shortcut):
        try:
            self.page_edit.click_sub_tool('Replace')
            self.click(L.import_media.media_library.media(index=2))
            self.replace_to_video(shortcut)

            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(),
                                    7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.story('Video')
    @allure.title('Replace')
    @allure.step('Video to Color board')
    def test_replace_video_to_color_board(self, driver):
        try:
            self.page_edit.click_sub_tool('Replace')
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
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.story('Video')
    @allure.title('Replace')
    @allure.step('Video to Photo')
    def test_replace_video_to_photo(self, driver):
        try:
            self.page_edit.click_sub_tool('Replace')
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.media_library.media(index=2))

            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(),
                                    7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            elif type(e) is ValueError:
                logger(f'[UnitTestError] {e}]')
                text = 'UnitTestError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')


@allure.epic('Timeline')
@allure.feature('Master')
class TestMasterReplacePhoto:

    @pytest.fixture(scope='class', autouse=True)
    def in_class_setup(self, shortcut, driver):
        page_main, page_edit, page_media, _ = shortcut
        click = page_main.h_click

        page_main.enter_launcher()
        click(L.main.new_project)
        page_media.switch_to_photo_library()
        click(L.import_media.media_library.media(index=1))
        click(L.import_media.media_library.apply)
        click(L.edit.timeline.clip())
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.replace_to_video = replace_to_video

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.clip())
        yield

    @allure.story('Photo')
    @allure.title('Replace')
    @allure.step('Photo to Photo')
    def test_replace_photo_to_photo(self):
        try:
            self.page_edit.click_sub_tool('Replace')
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.media_library.media(index=2))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.story('Photo')
    @allure.title('Replace')
    @allure.step('Photo to Color board')
    def test_replace_photo_to_color_board(self, driver):
        try:
            self.page_edit.click_sub_tool('Replace')
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
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.story('Photo')
    @allure.title('Replace')
    @allure.step('Photo to Video')
    def test_replace_photo_to_video(self, shortcut):
        try:
            self.page_edit.click_sub_tool('Replace')
            self.page_media.switch_to_video_library()
            self.click(L.import_media.media_library.media(index=1))

            self.replace_to_video(shortcut)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')


@allure.epic('Timeline')
@allure.feature('Master')
class TestMasterReplaceColorBoard:

    @pytest.fixture(scope='class', autouse=True)
    def in_class_setup(self, shortcut, driver):
        page_main, page_edit, page_media, _ = shortcut
        click = page_main.h_click

        page_main.enter_launcher()
        click(L.main.new_project)
        click(L.import_media.media_library.color_board)
        click(L.import_media.media_library.media(index=5))
        click(L.import_media.media_library.apply)
        click(L.edit.timeline.clip())
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.replace_to_video = replace_to_video

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.clip())
        yield

    @allure.story('Color board')
    @allure.title('Replace')
    @allure.step('Color board to Color board')
    def test_replace_color_board_to_color_board(self):
        try:
            self.page_edit.click_sub_tool('Replace')
            self.click(L.import_media.media_library.color_board)
            self.click(L.import_media.media_library.media(index=11))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.story('Color board')
    @allure.title('Replace')
    @allure.step('Color board to Photo')
    def test_replace_color_board_to_photo(self):
        try:
            self.page_edit.click_sub_tool('Replace')
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.media_library.media(index=2))
            assert not CompareImage(self.original_preview, self.page_edit.get_preview_pic(), 7).compare_image()

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.story('Color board')
    @allure.title('Replace')
    @allure.step('Color board to Video')
    def test_replace_color_board_to_video(self, shortcut):
        try:
            self.page_edit.click_sub_tool('Replace')
            self.page_media.switch_to_video_library()
            self.click(L.import_media.media_library.media(index=1))

            self.replace_to_video(shortcut)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')
