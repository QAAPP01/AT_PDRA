import time

import pytest
import allure

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
    VIDEO_LIMITATION = 3
    AUDIO_LIMITATION = 9
    PIP_LIMITATION = 9

    """
    self.page_preference = shortcut # not found
    """

    @allure.story("Video Track Limitation")
    def test_timeline_video_track_limitation(self, driver: AppiumU2Driver,
                                             page_edit, page_main):
        try:
            for i in range(self.VIDEO_LIMITATION):
                allure.title('Add a video to PiP track')
                page_edit.add_pip_media(media_type='Video')

            allure.title('Add another video after reaching track limitation')
            page_edit.add_pip_media(media_type='Video')
            allure.title('Should pop dialog if trying to add video while reaching track limitation')
            assert driver.get_text(L.import_media.device_limit.limit_title) == 'Video Overlay Maximum Exceeded'
            driver.click_element(L.import_media.device_limit.btn_remind_ok)

        except Exception as e:
            self.exception_handler(e, driver, page_main)

    @allure.story("Audio Track Limitation")
    def test_timeline_audio_track_limitation(self, driver: AppiumU2Driver,
                                             page_edit, page_main, import_media):

        try:
            page_edit.enter_audio_library(audio_type='SFX')
            import_media.select_music_library()
            time.sleep(20)

        except Exception as e:
            self.exception_handler(e, driver, page_main)

    @allure.story("PiP Track Limitation")
    def test_timeline_video_track_limitation(self, driver: AppiumU2Driver,
                                             page_edit, page_main):

        try:
            pass

        except Exception as e:
            self.exception_handler(e, driver, page_main)
