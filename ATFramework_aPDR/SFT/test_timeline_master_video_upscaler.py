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


@allure.epic('Timeline Master Video')
@allure.feature('Video Upscaler')
class Test_Master_Video_Upscaler:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @pytest.fixture(scope="module")
    def data(self):
        data = {'last_result': True}
        yield data

    def last_is_fail(self, data):
        if not data['last_result']:
            data['last_result'] = True
            self.page_main.relaunch()
            return True
        return False

    @allure.story('Dialog')
    @allure.title('Cancel')
    def test_cancel(self, data):
        try:
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.add_local_video(video_9_16)
            self.click(L.edit.timeline.clip())
            self.page_edit.click_sub_tool('Video\nUpscaler')
            self.click(id('cancel_button'))

            assert not self.is_exist(id('cancel_button'))

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Dialog')
    @allure.title('Continue')
    def test_continue(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)
                self.page_media.add_local_video(video_9_16)

            self.click(L.edit.timeline.clip())
            self.page_edit.click_sub_tool('Video\nUpscaler')
            self.click(id('confirm_button'))

            assert self.is_exist(xpath(f'//*[contains(@resource-id,"tv_title") and contains(@text,"AI Video Upscaler")]'))

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise
