import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T
from ATFramework_aPDR.ATFramework.utils import logger


@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Volume')
class TestMasterVideoVolume:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut

        page_main.enter_launcher()
        page_main.subscribe()
        click = page_main.h_click
        click(L.main.new_project)
        click(L.import_media.media_library.media(index=1))
        click(L.import_media.media_library.apply)

        click(T.id('item_view_bg'))
        page_edit.click_sub_tool('Volume')
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element
        yield

    @allure.title('Volume default value')
    def test_default_volume(self):
        pass

    @allure.title('Volume max value')
    def test_max_value(self):
        pass

    @allure.title('Volume min value')
    def test_min_value(self):
        pass

    @allure.title('Mute button can enable')
    def test_mute_able(self):
        pass

    @allure.title('Volume cannot adjusted when muted')
    def test_mute_volume_slider_disable(self):
        pass

    @allure.title('Mute button can disable')
    def test_mute_enable(self):
        pass

    @allure.title('Volume slider will enable when not mute')
    def test_slider_recover(self):
        pass

    @allure.title('Fade in button can disable')
    def test_fade_in_disable(self):
        pass

    @allure.title('Fade in button can enable')
    def test_fade_in_enable(self):
        pass

    @allure.title('Fade out button can disable')
    def test_fadeout_disable(self):
        pass

    @allure.title('Fade out button can enable')
    def test_fadeout_enable(self):
        pass
