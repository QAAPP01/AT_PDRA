from lxml import etree
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


@allure.epic('Timeline - PiP')
class Test_Track_Limitation:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut, driver):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

        self.driver = driver.driver

    @pytest.fixture(scope="module")
    def data(self):
        data = {'last_result': True}
        yield data

    def get_target_elements(self, xpath):
        try:
            page_source = self.driver.page_source
            root = etree.fromstring(page_source.encode('utf-8'))
            return root.xpath(xpath)
        except Exception as e:
            logger(f"Error parsing XML or finding elements: {str(e)}")
            return []

    VIDEO_LIMITATION = 3
    AUDIO_LIMITATION = 9
    PIP_LIMITATION = 20

    @allure.feature('Video')
    @allure.story('Track Limitation')
    def test_timeline_limitation_video_track(self):
        for i in range(1, self.VIDEO_LIMITATION + 2):
            with allure.step(f'[Step] Add 1 pip video, currently added {i} video tracks'):
                self.page_edit.click_tool('Overlay')
                self.click(find_string('Video'))
                self.click(L.import_media.media_library.media(index=1))
                self.click(L.edit.sub_tool.back)

        assert driver.get_text(L.import_media.device_limit.limit_title) == 'Video Overlay Maximum Exceeded'

        with allure.step('[Click] OK button'):
            self.click(L.import_media.device_limit.btn_remind_ok)

    @allure.feature('Audio')
    @allure.story('Music')
    @allure.title('Track Limitation')
    def test_timeline_limitation_audio_track(self, data):
        self.page_main.enter_timeline()

        TRACKS_XPATH = '//*[contains(@resource-id, "tracks_container_of_not_main")]/android.widget.LinearLayout'

        for i in range(1, self.AUDIO_LIMITATION + 1):
            with allure.step(f'[Step] Add {i} audio tracks'):
                self.page_edit.enter_audio_library(audio_type='SFX')
                if not self.elements(L.import_media.library_listview.add):
                    self.click(L.import_media.library_listview.frame_song)
                    self.click(L.import_media.library_listview.download_song)
                else:
                    self.click(L.import_media.library_listview.add)
                self.click(id('btn_session_back_icon'))

        target_elements = self.get_target_elements(TRACKS_XPATH)
        assert target_elements[-1].attrib['index'] == str(self.AUDIO_LIMITATION), f"Got {target_elements[-1].attrib['index']}"

        with allure.step(f'[Step] Add 1 more audio'):
            self.page_edit.enter_audio_library(audio_type='SFX')
            if not self.elements(L.import_media.library_listview.add):
                self.click(L.import_media.library_listview.frame_song)
                self.click(L.import_media.library_listview.download_song)
            else:
                self.click(L.import_media.library_listview.add)
            self.click(id('btn_session_back_icon'))

        target_elements = self.get_target_elements(TRACKS_XPATH)
        assert target_elements[0].attrib['index'] == '1', f"Got {target_elements[0].attrib['index']}"

    @allure.feature('PiP')
    @allure.story('Track Limitation')
    def test_timeline_limitation_pip_track(self):
        self.page_edit.enter_main_tool(name='Sticker')
        self.click(find_string('Add Sticker'))
        for i in range(1, self.PIP_LIMITATION + 2):
            with allure.step(f'[Step] Add 1 pip, currently added {i} pip tracks'):
                self.click(L.edit.main_tool.sticker.item())
        self.click(L.edit.pip.Text.back)

        # Only the first track will have 2 pip clip
        track = self.elements(id('item_view_bg'))
        assert track[0].rect['y'] == track[1].rect['y']
        assert track[2].rect['y'] != track[3].rect['y']
