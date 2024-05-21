import pytest
import allure

from ATFramework_aPDR.ATFramework.utils import logger
import ATFramework_aPDR.pages.locator as L
from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver

"""
allure levels:
- Feature (class)
-- Story (feature)
--- title (step)
---- steps (X)
"""


@allure.feature('Track Limitation')
class TestTrackLimitation:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
        self.page_main, *_ = shortcut
        self.page_main.enter_launcher()
        self.page_main.subscribe()
        self.page_main.enter_timeline()
        yield
        driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.page_main.enter_timeline()
        yield
        self.click(L.edit.menu.home)

    VIDEO_LIMITATION = 3
    AUDIO_LIMITATION = 9
    PIP_LIMITATION = 20

    @pytest.mark.skip
    @allure.story("Video Track Limitation")
    def test_timeline_limitation_video_track(self, driver: AppiumU2Driver):
        try:
            allure.title(f'Add {self.VIDEO_LIMITATION} + 1 video(s) to PiP track')
            for i in range(self.VIDEO_LIMITATION + 1):
                self.page_edit.add_pip_media(media_type='Video')

            allure.title('Should pop dialog if trying to add video while reaching track limitation')
            assert driver.get_text(L.import_media.device_limit.limit_title) == 'Video Overlay Maximum Exceeded'

            self.click(L.import_media.device_limit.btn_remind_ok)

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
            else:
                logger(f'[Exception] {repr(e)}')
            pytest.fail(f'[Exception] {repr(e)}]')

    @allure.story("Audio Track Limitation")
    def test_timeline_limitation_audio_track(self, driver: AppiumU2Driver):
        try:
            allure.title(f'Add {self.AUDIO_LIMITATION} + 1 audio(s) to PiP track')
            for _ in range(self.AUDIO_LIMITATION + 1):
                self.page_edit.enter_audio_library(audio_type='SFX')
                if not self.elements(L.import_media.library_listview.add):
                    self.click(L.import_media.library_listview.frame_song)
                    self.click(L.import_media.library_listview.download_song)
                else:
                    self.click(L.import_media.library_listview.add)
                self.click(L.search.id('btn_session_back_icon'))

            # Only the first track will have 2 audio clip
            allure.title(f'Only the first track will have 2 audio clip')
            assert type(y1 := self.element(L.edit.timeline.clip_audio(index=1)).rect['y']) is int
            assert type(y2 := self.element(L.edit.timeline.clip_audio(index=2)).rect['y']) is int
            assert y1 == y2

            assert type(y3 := self.element(L.edit.timeline.clip_audio(index=3)).rect['y']) is int
            assert type(y4 := self.element(L.edit.timeline.clip_audio(index=4)).rect['y']) is int
            assert y3 != y4

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
            else:
                logger(f'[Exception] {repr(e)}')
            pytest.fail(f'[Exception] {repr(e)}]')

    @allure.story("PiP Track Limitation")
    def test_timeline_limitation_pip_track(self, driver: AppiumU2Driver):
        try:
            allure.title(f'Add {self.PIP_LIMITATION} + 1 sticker(s) to PiP track')
            self.page_edit.enter_main_tool(name='Sticker')
            self.click(L.search.find_string('Add Sticker'))
            for _ in range(self.PIP_LIMITATION + 1):
                self.click(L.edit.main_tool.sticker.item())
            self.click(L.edit.pip.Text.back)

            # Only the first track will have 2 pip clip
            allure.title(f'Only the first track will have 2 pip clip')
            assert type(y1 := self.element(L.edit.pip.clip(index=1)).rect['y']) is int
            assert type(y2 := self.element(L.edit.pip.clip(index=2)).rect['y']) is int
            assert y1 == y2

            assert type(y3 := self.element(L.edit.pip.clip(index=3)).rect['y']) is int
            assert type(y4 := self.element(L.edit.pip.clip(index=4)).rect['y']) is int
            assert y3 != y4

        except Exception as e:
            if type(e) is AssertionError:
                logger(f'[AssertionError] {repr(e)}]')
            else:
                logger(f'[Exception] {repr(e)}')
            pytest.fail(f'{repr(e)}]')
