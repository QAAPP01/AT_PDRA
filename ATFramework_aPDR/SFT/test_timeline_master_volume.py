import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T


@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Volume')
class TestMasterVideoVolume:

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

        with allure.step('[Step] Enter Volume function'):
            click(T.id('item_view_bg'))
            page_edit.click_sub_tool('Volume')
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

    @allure.title('Volume default value')
    def test_default_volume(self):
        assert float(self.element(L.edit.volume.slider).text) == 100

    @allure.title('Volume max value')
    def test_max_value(self):
        with allure.step('[Set] Slider max value'):
            self.element(L.edit.volume.slider).send_keys(9999)
        assert float(self.element(L.edit.volume.slider).text) == 200

    @allure.title('Volume min value')
    def test_min_value(self):
        with allure.step('[Set] Slider min value'):
            self.element(L.edit.volume.slider).send_keys(-9999)
        assert float(self.element(L.edit.volume.slider).text) == 0

    @allure.title('Mute button can enable')
    def test_mute_enable(self):
        with allure.step('[Click] Mute'):
            mute = self.element(L.edit.volume.mute)
            mute.click()
        assert mute.get_attribute('selected') == 'true'

    @allure.title('Volume cannot adjusted when muted')
    def test_mute_volume_slider_disable(self):
        assert self.element(L.edit.volume.slider).get_attribute('enabled') == 'false'

    @allure.title('Mute button can disable')
    def test_mute_disable(self):
        with allure.step('[Click] Mute'):
            mute = self.element(L.edit.volume.mute)
            mute.click()
        assert mute.get_attribute('selected') == 'false'

    @allure.title('Volume slider will enable and can adjust when not mute')
    def test_slider_recover(self):
        from random import randint

        assert self.element(L.edit.volume.slider).get_attribute('enabled') == 'true'

        value = self.element(L.edit.volume.slider).text
        with allure.step('[Set] Slider to random value'):
            self.element(L.edit.volume.slider).send_keys(randint(0, 200))
        assert float(self.element(L.edit.volume.slider).text) != float(value)

    @allure.title('Fade in button can enable')
    def test_fade_in_enable(self):
        with allure.step('[Click] Fade in'):
            fade_in = self.element(L.edit.volume.fade_in)
            fade_in.click()
        assert fade_in.get_attribute('selected') == 'true'

    @allure.title('Fade in button can disable')
    def test_fade_in_disable(self):
        with allure.step('[Click] Fade in'):
            fade_in = self.element(L.edit.volume.fade_in)
            fade_in.click()
        assert fade_in.get_attribute('selected') == 'false'

    @allure.title('Fade out button can enable')
    def test_fadeout_enable(self):
        with allure.step('[Click] Fade out'):
            fade_out = self.element(L.edit.volume.fade_out)
            fade_out.click()
        assert fade_out.get_attribute('selected') == 'true'

    @allure.title('Fade out button can disable')
    def test_fadeout_disable(self):
        with allure.step('[Click] Fade out'):
            fade_out = self.element(L.edit.volume.fade_out)
            fade_out.click()
        assert fade_out.get_attribute('selected') == 'false'
