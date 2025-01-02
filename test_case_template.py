import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'

@allure.epic("Shortcut - AI Scene")
class Test_Shortcut_AI_Scene:
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

    @allure.feature("Entry")
    @allure.story("Enter")
    @allure.title("From Shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            if self.last_is_fail(data): # 第一個test case 可放可不放
                pass

            data["傳遞資料"] = "可以跨function傳遞資料"

            assert self.page_shortcut.enter_shortcut('AI Scene')

        # except 固定格式不用改
        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Recommendation")
    @allure.title("Close")
    def test_recommendation_close(self, data):
        try:
            # 一定要放，檢查上一個Result是不是fail，為了判斷需不需要重開app
            if self.last_is_fail(data):
                pass    # 如果下面步驟是從launcher開始，直接加pass略過

            share = data["傳遞資料"]
            print(share)

            assert self.page_shortcut.recommendation_close()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Back")
    @allure.title("From media picker")
    def test_back_from_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Scene')   # 這裡放從launcher開始的步驟，直到銜接下面步驟

            assert self.page_shortcut.back_from_media_picker()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise
