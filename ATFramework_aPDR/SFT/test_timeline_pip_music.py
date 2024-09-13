import traceback
import inspect

import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *

from .conftest import TEST_MATERIAL_FOLDER
test_material_folder = TEST_MATERIAL_FOLDER



@allure.epic("Timeline_PiP")
@allure.feature("Music")
@allure.story("Import Music")
class Test_PiP_Import_Music:
    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

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

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            raise Exception

    @allure.title("Add music to PiP track")
    def test_add_local_music_to_timeline(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            assert self.is_exist(L.edit.timeline.item_view_thumbnail_view)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            raise Exception

@allure.epic("Timeline_PiP")
@allure.feature("Music")
@allure.story("Volume")
class Test_PiP_Music_Volume:

    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

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

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
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

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
            raise Exception

    @allure.title("Maximum")
    def test_sticker_opacity_maximum(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.adjust_sub.progress).send_keys('200')
            value = self.element(L.edit.adjust_sub.number).text
            assert value == '200'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
            raise Exception

    @allure.title("Enable mute")
    def test_music_volume_enable_mute(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.speed.mute_audio)
            assert self.element(L.edit.speed.mute_audio).get_attribute('selected') == 'true'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
            raise Exception

    @allure.title("Disable mute")
    def test_music_volume_disable_mute(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.speed.mute_audio)
            assert self.element(L.edit.speed.mute_audio).get_attribute('selected') == 'false'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
            raise Exception

    @allure.title("Enable Fade in")
    def test_music_volume_enable_fade_in(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.volume.fade_in)
            assert self.element(L.edit.volume.fade_in).get_attribute('selected') == 'true'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
            raise Exception

    @allure.title("Disable Fade in")
    def test_music_volume_disable_fade_in(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.volume.fade_in)
            assert self.element(L.edit.volume.fade_in).get_attribute('selected') == 'false'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
            raise Exception

    @allure.title("Enable Fade out")
    def test_music_volume_enable_fade_out(self, driver):
        try:
            self.click(L.edit.volume.fade_out)
            assert self.element(L.edit.volume.fade_out).get_attribute('selected') == 'true'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('Volume')
            raise Exception

    @allure.title("Disable Fade out")
    def test_music_volume_disable_fade_out(self, driver):
        try:
            self.click(L.edit.volume.fade_out)
            assert self.element(L.edit.volume.fade_out).get_attribute('selected') == 'false'
            self.click(L.edit.sub_tool.back)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            raise Exception


@allure.epic("Timeline_PiP")
@allure.feature("Music")
@allure.story("Split")
class Test_PiP_Music_Split:
    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

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
            self.element(L.edit.timeline.item_view_thumbnail_view).click()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            raise Exception


@allure.epic("Timeline_PiP")
@allure.feature("Music")
@allure.story("AI Audio Tool_AI Voice Changer")
class Test_PiP_Music_AI_Voice_Chagner:
    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

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
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            pic_base = self.page_edit.get_preview_pic(L.edit.ai_audio_tool.ai_voice_changer_panel)
            self.click(L.edit.ai_audio_tool.filter)
            self.elements(L.edit.ai_audio_tool.filter_option)[1].click()
            self.click(L.edit.ai_audio_tool.filter_save)
            pic_after = self.page_edit.get_preview_pic(L.edit.ai_audio_tool.ai_voice_changer_panel)
            assert not HCompareImg(pic_base, pic_after).ssim_compare()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            raise Exception

    @allure.title("Reset AI Voice Changer's filter")
    def test_reset_AI_voice_changer_filter(self, driver):
        try:
            pic_base = self.page_edit.get_preview_pic(L.edit.ai_audio_tool.ai_voice_changer_panel)
            self.click(L.edit.ai_audio_tool.filter)
            self.click(L.edit.ai_audio_tool.filter_reset)
            self.click(L.edit.ai_audio_tool.filter_save)
            pic_after = self.page_edit.get_preview_pic(L.edit.ai_audio_tool.ai_voice_changer_panel)
            assert not HCompareImg(pic_base, pic_after).ssim_compare()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            raise Exception

    @allure.title("Apply AI Voice Changer")
    def test_apply_AI_voice_changer(self, driver):
        try:
            self.click(L.edit.ai_audio_tool.cat_Professional)
            self.click(L.edit.ai_audio_tool.voice(1))
            self.click(L.edit.ai_audio_tool.apply)
            if self.is_exist(L.edit.ai_audio_tool.ok, 30):
                self.click(L.edit.ai_audio_tool.ok)
            assert self.is_exist(L.edit.ai_audio_tool.voice_changer_is_applied)


        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('AI Audio \nTool')
            raise Exception

    @allure.title("AI Voice Changer Switch Off")
    def test_AI_voice_changer_on(self, driver):
        try:
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.voice_changer_on_off)
            assert self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'false'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            raise Exception

    @allure.title("AI Voice Changer Switch Off")
    def test_AI_voice_changer_off(self, driver):
        try:
            self.click(L.edit.ai_audio_tool.voice_changer_on_off)
            assert self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'true'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            raise Exception

    @allure.title("AI Voice Changer Cancel")
    def test_AI_voice_changer_cancel(self, driver):
        try:
            self.click(L.edit.ai_audio_tool.voice_changer.remove)
            self.click(L.edit.ai_audio_tool.cancel)
            assert self.is_exist(L.edit.ai_audio_tool.voice_changer_is_applied)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            raise Exception

    @allure.title("AI Voice Changer Delete")
    def test_AI_voice_changer_delete(self, driver):
        try:
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.voice_changer.remove)
            self.click(L.edit.ai_audio_tool.ok)
            assert not self.is_exist(L.edit.ai_audio_tool.voice_changer_is_applied)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool("Audio")
            self.click(L.import_media.menu.music)
            self.page_main.h_click(L.edit.music.local)
            self.page_main.h_click(find_string(test_material_folder))
            self.element(L.import_media.music_library.add).click()
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.click(L.edit.ai_audio_tool.ai_voice_changer)
            raise Exception
