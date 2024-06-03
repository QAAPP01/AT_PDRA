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
class TestMasterReplaceVideoAfterApplyVolume:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut

        page_main.enter_launcher()
        page_main.enter_timeline()
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

        self.click(L.edit.preview.import_tips_icon)
        self.click(L.import_media.media_library.media(index=1))
        self.click(L.import_media.media_library.apply)
        self.click(L.edit.timeline.clip())
        yield
        self.click(L.edit.menu.delete)

    @allure.story('Video')
    @allure.title('Replace')
    @allure.step('Replace video after setting Volume (Slide bar, Fade in, Fade out)')
    def test_replace_video_adjusted_volume(self, driver, shortcut):
        from random import randint
        slider_int = randint(1, 200)

        try:

            self.page_edit.click_sub_tool('Volume')
            self.element(L.edit.speed.slider).send_keys(slider_int)
            self.click(L.edit.speed.ease_in)
            self.click(L.edit.speed.ease_out)

            self.page_edit.click_sub_tool('Replace')
            self.click(L.import_media.media_library.media(index=2))
            self.replace_to_video(shortcut)
            self.click(L.edit.timeline.clip())

            self.page_edit.click_sub_tool('Volume')
            assert self.element(L.edit.speed.slider).get_text() == slider_int
            assert self.element(L.edit.speed.ease_in).get_attribute('selected') == 'true'
            assert self.element(L.edit.speed.ease_out).get_attribute('selected') == 'true'

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
    @allure.step('Replace video after setting Audio tool (Voice Changer)')
    def test_replace_video_adjusted_audioTool(self, driver, shortcut):
        try:

            self.page_edit.click_sub_tool('Audio Tool')
            self.page_edit.click_sub_tool('Voice Changer')
            self.page_edit.click_sub_tool('Radio 1')
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.ai_audio_tool.ok)

            self.page_edit.click_sub_tool('Replace')
            self.click(L.import_media.media_library.media(index=2))
            self.replace_to_video(shortcut)
            self.click(L.edit.timeline.clip())

            self.page_edit.click_sub_tool('Voice Effects')
            assert self.page_edit.check_bottom_edit_menu_item_apply_status('Audio Tool')

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
    @allure.step('Replace video after setting Filter')
    def test_replace_video_adjusted_filter(self, driver, shortcut):
        try:

            self.page_edit.click_sub_tool('Filter')
            self.page_edit.click_effect('A06', L.edit.master.ai_effect.effect())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.ai_audio_tool.ok)

            self.page_edit.click_sub_tool('Replace')
            self.click(L.import_media.media_library.media(index=2))
            self.replace_to_video(shortcut)
            self.click(L.edit.timeline.clip())

            self.page_edit.click_sub_tool('Voice Effects')
            assert self.page_edit.check_bottom_edit_menu_item_apply_status('Filter')

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {e}]')
                text = 'AssertionError'
            else:
                logger(f'[Exception] {e}')
                text = 'Exception'
            pytest.fail(f'[{text}] {e}]')


