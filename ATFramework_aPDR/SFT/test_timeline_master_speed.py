import pytest
import allure
from random import randint

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T

original_video_length: float = 0


@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Speed')
class TestMasterVideoSpeed:

    @pytest.fixture(scope='class', autouse=True)
    def test_setup(self, shortcut, driver):
        global original_video_length
        page_main, page_edit, *_ = shortcut
        click = page_main.h_click

        with allure.step('[Step] Enter launcher'):
            page_main.enter_launcher()
        with allure.step('[Step] New timeline with video'):
            click(L.main.new_project)
            click(L.import_media.media_library.media(index=1))
            click(L.import_media.media_library.apply)

        with allure.step('[Step] Enter Speed function'):
            click(T.id('item_view_bg'))
            page_edit.click_sub_tool('Speed')
        original_video_length = page_main.element(T.id('item_view_bg')).rect['width']
        yield
        with allure.step('[Step] Back to launcher'):
            page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def define_vars(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        yield

    @allure.title('Speed default value')
    def test_speed_default(self):
        assert self.element(L.edit.speed.preview_toast_text).text == '1x'

    @allure.title('Speed max value')
    def test_max_speed(self):
        with allure.step('[Set] Slider max value'):
            self.element(L.edit.speed.slider).send_keys(9999)
        assert self.element(L.edit.speed.preview_toast_text).text == '8x'

    @allure.title('Speed min value')
    def test_min_speed(self):
        with allure.step('[Set] Slider min value'):
            self.element(L.edit.speed.slider).send_keys(-9999)
        assert self.element(L.edit.speed.preview_toast_text).text == '0.125x'

    @allure.title('Set to smaller magnification')
    def test_slower_speed(self):
        with allure.step('[Set] Slider smaller value'):
            self.element(L.edit.speed.slider).send_keys(randint(0, 24))  # 1x is 25
        assert float(self.element(L.edit.speed.preview_toast_text).text[:-1]) < 1

    @allure.title('Slower clip time should be correct')
    def test_slower_video_length(self):
        global original_video_length
        assert self.element(T.id('item_view_bg')).rect['width'] >= original_video_length

    @allure.title('Set to bigger magnification')
    def test_faster_speed(self):
        with allure.step('[Set] Slider bigger value'):
            self.element(L.edit.speed.slider).send_keys(randint(26, 100))  # 1x is 25
        assert float(self.element(L.edit.speed.preview_toast_text).text[:-1]) > 1

    @allure.title('Faster clip time should be correct')
    def test_faster_video_length(self):
        global original_video_length
        assert self.element(T.id('item_view_bg')).rect['width'] <= original_video_length

    @allure.title('Mute button can be enable')
    def test_mute_enabled(self):
        with allure.step('[Set] Slider bigger value'):
            self.element(L.edit.speed.slider).send_keys(randint(26, 100))
        with allure.step('[Click] mute'):
            mute = self.element(L.edit.speed.mute_audio)
            mute.click()
        assert mute.get_attribute('selected') == 'true'

    @allure.title('Mute button can be disable')
    def test_mute_disabled(self):
        with allure.step('[Click] mute'):
            mute = self.element(L.edit.speed.mute_audio)
            mute.click()
        assert mute.get_attribute('selected') == 'false'

    @allure.title('Keep pitch button can be enable')
    def test_keep_pitch_enabled(self):
        with allure.step('[Click] Keep pitch'):
            keep_pitch = self.element(L.edit.speed.keep_pitch)
            keep_pitch.click()
        assert keep_pitch.get_attribute('selected') == 'true'

    @allure.title('Keep pitch button can be disable')
    def test_keep_pitch_disabled(self):
        with allure.step('[Click] Keep pitch'):
            keep_pitch = self.element(L.edit.speed.keep_pitch)
            keep_pitch.click()
        assert keep_pitch.get_attribute('selected') == 'false'

    @allure.title('Ease in button can be enable')
    def test_ease_in_enabled(self):
        with allure.step('[Click] Ease in'):
            ease_in = self.element(L.edit.speed.ease_in)
            ease_in.click()
        assert ease_in.get_attribute('selected') == 'true'

    @allure.title('Ease in button can be disable')
    def test_ease_in_disabled(self):
        with allure.step('[Click] Ease in'):
            ease_in = self.element(L.edit.speed.ease_in)
            ease_in.click()
        assert ease_in.get_attribute('selected') == 'false'

    @allure.title('Ease out button can be enable')
    def test_ease_out_enabled(self):
        with allure.step('[Click] Ease out'):
            ease_out = self.element(L.edit.speed.ease_out)
            ease_out.click()
        assert ease_out.get_attribute('selected') == 'true'

    @allure.title('Ease out button can be disable')
    def test_ease_out_disabled(self):
        with allure.step('[Click] Ease out'):
            ease_out = self.element(L.edit.speed.ease_out)
            ease_out.click()
        assert ease_out.get_attribute('selected') == 'false'

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        with allure.step('[Click] Reset'):
            self.click(L.edit.speed.reset)
        assert self.element(L.edit.speed.preview_toast_text).text == '1x'
        assert self.element(L.edit.speed.mute_audio).get_attribute('selected') == 'false'
        assert self.element(L.edit.speed.keep_pitch).get_attribute('selected') == 'false'
        assert self.element(L.edit.speed.ease_in).get_attribute('selected') == 'false'
        assert self.element(L.edit.speed.ease_out).get_attribute('selected') == 'false'

    @allure.title('Tapping reset button when not modified will not change settings')
    def test_reset_again(self):
        with allure.step('[Click] Reset'):
            self.click(L.edit.speed.reset)
        assert self.element(L.edit.speed.preview_toast_text).text == '1x'
        assert self.element(L.edit.speed.mute_audio).get_attribute('selected') == 'false'
        assert self.element(L.edit.speed.keep_pitch).get_attribute('selected') == 'false'
        assert self.element(L.edit.speed.ease_in).get_attribute('selected') == 'false'
        assert self.element(L.edit.speed.ease_out).get_attribute('selected') == 'false'
