import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T
from ATFramework_aPDR.ATFramework.utils import logger


@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Split')
class TestMasterSplitVideo:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut
        click = page_main.h_click

        with allure.step('[Step] Enter launcher'):
            page_main.enter_launcher()
        with allure.step('[Step] New timeline with video'):
            click(L.main.new_project)
            click(L.import_media.media_library.media(index=1))
            click(L.import_media.media_library.apply)

        with allure.step('[Swipe] timeline to left'):
            driver.swipe_element(L.edit.timeline.playhead, 'left', offset=0.1)
        with allure.step('[Click] Split'):
            click(T.id('item_view_bg'))
            page_edit.click_sub_tool('Split')
        yield
        with allure.step('[Step] Back to launcher'):
            page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element
        yield

    @allure.title('Video has split')
    def test_video_split(self, driver, shortcut):
        assert len(self.elements(T.id('item_view_bg'))) > 1

    @allure.title('Splitting are correct')
    def test_splitting(self, driver, shortcut):
        start, end = self.elements(T.id('item_view_bg'))

        first_clip_end_x = start.rect['x'] + start.rect['width']
        second_clip_start_x = end.rect['x']

        timeline_indicator = self.element(L.edit.timeline.playhead)
        timeline_indicator_x = timeline_indicator.rect['x'] + timeline_indicator.rect['width']/2

        assert first_clip_end_x == second_clip_start_x == timeline_indicator_x


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Split')
class TestMasterSplitPhoto:

    @pytest.fixture(scope='class', autouse=True)
    def in_class_setup(self, shortcut, driver):
        page_main, page_edit, page_media, *_ = shortcut
        click = page_main.h_click

        with allure.step('[Step] Enter launcher'):
            page_main.enter_launcher()
        with allure.step('[Step] New timeline with photo'):
            click(L.main.new_project)
            page_media.switch_to_photo_library()
            click(L.import_media.media_library.media(index=1))
            click(L.import_media.media_library.apply)

        with allure.step('[Swipe] timeline to left'):
            driver.swipe_element(L.edit.timeline.playhead, 'left', offset=0.1)
        with allure.step('[Click] Split'):
            click(T.id('item_view_bg'))
            page_edit.click_sub_tool('Split')
        yield
        with allure.step('[Step] Back to launcher'):
            page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.original_preview = self.page_edit.get_preview_pic()
        yield

    @allure.title('Photo has split')
    def test_photo_split(self, driver, shortcut):
        assert len(self.elements(T.id('item_view_bg'))) > 1

    @allure.title('Splitting are correct')
    def test_splitting(self, driver, shortcut):
        start, end = self.elements(T.id('item_view_bg'))

        first_clip_end_x = start.rect['x'] + start.rect['width']
        second_clip_start_x = end.rect['x']

        timeline_indicator = self.element(L.edit.timeline.playhead)
        timeline_indicator_x = timeline_indicator.rect['x'] + timeline_indicator.rect['width'] / 2

        assert first_clip_end_x == second_clip_start_x == timeline_indicator_x

