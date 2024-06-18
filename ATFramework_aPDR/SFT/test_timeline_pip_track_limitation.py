import pytest
import allure

from ATFramework_aPDR.ATFramework.utils import logger
import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T
from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver


@allure.epic('Timeline_PiP')
class TestTrackLimitation:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        self.page_main, *_ = shortcut
        self.page_main.enter_launcher()
        self.page_main.subscribe()  # Sound import needs sub
        self.page_main.enter_timeline()
        yield

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

    @allure.feature('Video')
    @allure.story('Track Limitation')
    def test_timeline_limitation_video_track(self, driver: AppiumU2Driver):
        for i in range(self.VIDEO_LIMITATION + 1):
            with allure.step(f'[Step] Add 1 pip video, currently added {i} video tracks'):
                self.page_edit.click_tool('Overlay')
                self.click(T.find_string('Video'))
                self.click(L.import_media.media_library.media(index=1))
                self.click(L.edit.sub_tool.back)

        assert driver.get_text(L.import_media.device_limit.limit_title) == 'Video Overlay Maximum Exceeded'

        with allure.step('[Click] OK button'):
            self.click(L.import_media.device_limit.btn_remind_ok)

    @allure.feature('Audio')
    @allure.story('Track Limitation')
    def test_timeline_limitation_audio_track(self, driver: AppiumU2Driver):
        for i in range(self.AUDIO_LIMITATION + 1):
            with allure.step(f'[Step] Add 1 pip audio, currently added {i} audio tracks'):
                self.page_edit.enter_audio_library(audio_type='SFX')
                if not self.elements(L.import_media.library_listview.add):
                    self.click(L.import_media.library_listview.frame_song)
                    self.click(L.import_media.library_listview.download_song)
                else:
                    self.click(L.import_media.library_listview.add)
                self.click(T.id('btn_session_back_icon'))

        track = self.elements(T.id('item_view_bg'))
        assert track[0].rect['y'] == track[1].rect['y']
        assert track[2].rect['y'] != track[3].rect['y']

    @allure.feature('PiP')
    @allure.title('Track Limitation')
    def test_timeline_limitation_pip_track(self, driver: AppiumU2Driver):
        self.page_edit.enter_main_tool(name='Sticker')
        self.click(T.find_string('Add Sticker'))
        for i in range(self.PIP_LIMITATION + 1):
            with allure.step(f'[Step] Add 1 pip, currently added {i} pip tracks'):
                self.click(L.edit.main_tool.sticker.item())
        self.click(L.edit.pip.Text.back)

        # Only the first track will have 2 pip clip
        track = self.elements(T.id('item_view_bg'))
        assert track[0].rect['y'] == track[1].rect['y']
        assert track[2].rect['y'] != track[3].rect['y']
