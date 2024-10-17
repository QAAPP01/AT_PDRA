import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.SFT.test_file import *


@allure.epic('Timeline Master Video')
@allure.feature('Split')
class Test_Master_Video_Split:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

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

