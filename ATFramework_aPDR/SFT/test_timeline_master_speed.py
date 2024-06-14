import pytest
import allure
from random import randint
from math import floor

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T
from ATFramework_aPDR.ATFramework.utils import logger

original_video_length: float = 0

def get_clip_seconds(raw_time:str) -> int:
    # input: 00:00/2:00:03
    time = raw_time.split('/')[-1].split(':')[::-1] # return [3(s), 0(m), 2(h)]
    return sum([int(t) * 60**i for i, t in enumerate(time)])

@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Speed')
class TestMasterVideoVolume:


    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut

        # page_main.enter_launcher()
        # click = page_main.h_click
        # click(L.main.new_project)
        # click(L.import_media.media_library.media(index=1))
        # click(L.import_media.media_library.apply)
        #
        # click(T.id('item_view_bg'))
        # page_edit.click_sub_tool('Speed')
        # yield
        # page_edit.back_to_launcher()

        yield
        page_main.h_click(L.edit.speed.reset)


    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element
        yield

    @pytest.mark.skip
    @allure.title('Speed default value')
    def test_speed_default(self):
        assert self.element(L.edit.speed.preview_toast_text).text == '1x'

    @pytest.mark.skip
    @allure.title('Speed max value')
    def test_max_speed(self):
        self.element(L.edit.speed.slider).send_keys(9999)
        assert self.element(L.edit.speed.preview_toast_text).text == '8x'

    @pytest.mark.skip
    @allure.title('Speed min value')
    def test_min_speed(self):
        self.element(L.edit.speed.slider).send_keys(-9999)
        assert self.element(L.edit.speed.preview_toast_text).text == '0.125x'

    @allure.title('Set to smaller magnification')
    def test_slower_speed(self):
        global original_video_length
        original_video_length = get_clip_seconds(self.element(L.edit.preview.time_code).text)
        self.element(L.edit.speed.slider).send_keys(randint(0, 24))  # 1x is 25
        value = float(self.element(L.edit.speed.preview_toast_text).text[:-1])
        assert value < 1

    @allure.title('Slower clip time should be correct')
    def test_slower_video_length(self):
        global original_video_length

        current_video_length = get_clip_seconds(self.element(L.edit.preview.time_code).text)
        shown_value = float(self.element(L.edit.speed.preview_toast_text).text[:-1])

        logger(f'{original_video_length=}', log_level='warn')
        logger(f'{shown_value=}', log_level='warn')
        logger(f'{current_video_length=}', log_level='warn')
        logger(f'{original_video_length / shown_value}', log_level='warn')

        assert current_video_length == floor(original_video_length / shown_value)

    @allure.title('Set to bigger magnification')
    def test_faster_speed(self):
        global original_video_length
        original_video_length = get_clip_seconds(self.element(L.edit.preview.time_code).text)
        self.element(L.edit.speed.slider).send_keys(randint(26, 100))  # 1x is 25
        value = float(self.element(L.edit.speed.preview_toast_text).text[:-1])
        assert value > 1

    @allure.title('Faster clip time should be correct')
    def test_faster_video_length(self):
        global original_video_length

        current_video_length = get_clip_seconds(self.element(L.edit.preview.time_code).text)
        shown_value = float(self.element(L.edit.speed.preview_toast_text).text[:-1])

        assert current_video_length == floor(original_video_length / shown_value)




