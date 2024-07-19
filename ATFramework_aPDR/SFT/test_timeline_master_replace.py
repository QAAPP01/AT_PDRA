import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T
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


@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Replace')
class TestMasterReplaceVideo:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut

        page_main.enter_launcher()
        page_main.subscribe()
        click = page_main.h_click
        click(L.main.new_project)
        click(L.import_media.media_library.media(index=1))
        click(L.import_media.media_library.apply)
        click(L.edit.timeline.track)
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(L.edit.timeline.track)
        self.replace_to_video = replace_to_video
        yield

    @allure.title('Replace video to video')
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

    @allure.title('Replace video to color board')
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
            self.click(L.edit.timeline.track)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.title('Replace video to photo')
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


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Replace')
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
        click(T.id('item_view_bg'))
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.replace_to_video = replace_to_video

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(T.id('item_view_bg'))
        yield

    @allure.title('Replace photo to photo')
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

    @allure.title('Replace photo to color board')
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
            self.click(T.id('item_view_bg'))

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')

    @allure.title('Replace photo to video')
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


@allure.epic('Timeline_Master')
@allure.feature('Color Board')
@allure.story('Replace')
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
        click(T.id('item_view_bg'))
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.replace_to_video = replace_to_video

        self.original_preview = self.page_edit.get_preview_pic()
        self.click(T.id('item_view_bg'))
        yield

    @allure.title('Replace color board to color board')
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

    @allure.title('Replace color board to photo')
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

    @allure.title('Replace color board to video')
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
