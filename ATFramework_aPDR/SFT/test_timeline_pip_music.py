import traceback
import inspect
import time

import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *

from .conftest import TEST_MATERIAL_FOLDER
test_material_folder = TEST_MATERIAL_FOLDER


@allure.epic("Timeline_PiP")
@allure.feature("Audio")
@allure.story("Music")
class Test_PiP_Import_Music:
    @pytest.fixture(scope='session', autouse=True)
    def driver_init(self, driver):
        logger("[Start] Init driver session")
        driver.driver.launch_app()
        yield
        # driver.driver.close_app()

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
        self.set_slider = self.page_edit.h_set_slider

    @allure.title("Enter Music Library")
    def test_enter_music_library(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)

            assert self.is_exist(L.import_media.media_library.recycler_view)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            raise Exception

    @allure.title("Add to PiP track")
    def test_add_local_music_to_timeline(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()

            assert self.is_exist(L.edit.timeline.item_view_thumbnail_view)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception


@allure.epic("Timeline_PiP")
@allure.feature("Audio")
@allure.story("Music")
class Test_PiP_Music_Volume:

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
        self.set_slider = self.page_edit.h_set_slider

    @allure.title("Default Value")
    def test_sticker_opacity_default_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.click_sub_tool('Volume')
            value = self.element(L.edit.adjust_sub.number).text

            assert value == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception


    @allure.title("Minimum")
    def test_sticker_opacity_minimum(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.adjust_sub.progress).send_keys('1.0')
            self.element(L.edit.adjust_sub.progress).send_keys('0')
            value = self.element(L.edit.adjust_sub.number).text

            assert value == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Maximum")
    def test_sticker_opacity_maximum(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.adjust_sub.progress).send_keys('200')
            value = self.element(L.edit.adjust_sub.number).text

            assert value == '200'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Enable mute")
    def test_music_volume_mute(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.speed.mute_audio)

            assert self.element(L.edit.speed.mute_audio).get_attribute('selected')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Enable Fade in")
    def test_music_volume_fade_in(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.speed.ease_in)

            assert self.element(L.edit.speed.ease_in).get_attribute('selected')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Enable Fade out")
    def test_music_volume_fade_out(self, driver):
        try:
            self.click(L.edit.speed.ease_out)

            assert self.element(L.edit.speed.ease_out).get_attribute('selected')
            self.click(L.edit.sub_tool.back)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception


@allure.epic("Timeline_PiP")
@allure.feature("Audio")
@allure.story("Music")
class Test_PiP_Music_Split:
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
        self.set_slider = self.page_edit.h_set_slider

    @allure.title("Split Music")
    def test_split_music(self, driver):

        try:
            self.page_edit.scroll_playhead()
            self.click(L.edit.menu.split)
            clip = self.elements(L.edit.timeline.item_view_thumbnail_view)

            assert len(clip) == 2

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception


@allure.epic("Timeline_PiP")
@allure.feature("Audio")
@allure.story("Music")
class Test_PiP_Music_AI_Voice_Chagner:
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
        self.set_slider = self.page_edit.h_set_slider

    @allure.title("Apply AI Voice Changer's filter")
    def test_apply_AI_voice_changer_filter(self, driver):
        try:
            self.page_edit.click_sub_tool('AI Voice Changer')
            self.click(L.edit.ai_voice_changer.filter)

            assert self.is_exist(L.edit.ai_voice_changer.filter_list)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception