import pytest
import allure

from ATFramework_aPDR.ATFramework.utils import logger
from ATFramework_aPDR.SFT.Test_Timeline.TestBase import TestBase
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
class TestTrackLimitation(TestBase):

    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    VIDEO_LIMITATION = 3
    AUDIO_LIMITATION = 9
    PIP_LIMITATION = 9

    @pytest.mark.skip
    @allure.story("Video Track Limitation")
    def test_timeline_video_track_limitation(self, driver: AppiumU2Driver):
        try:
            allure.title(f'Add {self.VIDEO_LIMITATION} video(s) to PiP track')
            for i in range(self.VIDEO_LIMITATION):
                self.page_edit.add_pip_media(media_type='Video')

            self.page_edit.add_pip_media(media_type='Video')
            allure.title('Should pop dialog if trying to add video while reaching track limitation')
            assert driver.get_text(L.import_media.device_limit.limit_title) == 'Video Overlay Maximum Exceeded'

            self.click(L.import_media.device_limit.btn_remind_ok)

        except Exception as e:
            self.exception_handler(e, driver, self.page_main)

    @allure.story("Audio Track Limitation")
    def test_timeline_audio_track_limitation(self, driver: AppiumU2Driver):

        def add_audio_track() -> None:
            self.page_edit.enter_audio_library(audio_type='SFX')
            self.click(L.import_media.library_listview.frame_song)
            if self.elements(L.import_media.library_listview.download_song):
                self.click(L.import_media.library_listview.download_song)
            else:
                self.click(L.import_media.library_listview.add)

        def get_first_two_track_y_value() -> tuple:
            """
            Return the first two track y values, can use to check if the two tracks are in the same tracks
            """
            y1 = self.element(L.edit.timeline.clip_audio(index=1)).rect['y']  # Return int
            y2 = self.element(L.edit.timeline.clip_audio(index=2)).rect['y']  # Return int
            return y1, y2

        try:
            allure.title(f'Add {self.AUDIO_LIMITATION} audio(s) to PiP track')
            for _ in range(self.AUDIO_LIMITATION):
                add_audio_track()

            # The ninth audio track should not be on the first audio track,
            audio1_y, audio2_y = get_first_two_track_y_value()
            assert audio1_y != audio2_y

            # The tenth audio track should be on the first audio track
            allure.title(f'The new audio should be on the '
                         f'first track if already have {self.AUDIO_LIMITATION} audio tracks')
            add_audio_track()
            audio1_y, audio2_y = get_first_two_track_y_value()
            assert audio1_y == audio2_y

        except Exception as e:
            self.exception_handler(e, driver, self.page_main)

    @pytest.mark.skip
    @allure.story("PiP Track Limitation")
    def test_timeline_video_track_limitation(self, driver: AppiumU2Driver):

        try:
            pass

        except Exception as e:
            self.exception_handler(e, driver, self.page_main)
