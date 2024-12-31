import time
import traceback

from allure import step

from .locator import locator as L
from .locator.locator_type import *
from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.pages.main_page import MainPage
from ATFramework_aPDR.pages.edit import EditPage
from ATFramework_aPDR.pages.import_media import MediaPage
from ATFramework_aPDR.ATFramework.utils.log import logger
from ..ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.SFT.test_file import *


class Shortcut(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_main = MainPage(driver)
        self.page_edit = EditPage(driver)
        self.page_media = MediaPage(driver)
        self.driver = driver

    def __repr__(self):
        return f"<Shortcut Page class >"

    def back_from_all_shortcut_page(self):
        self.click(id('back_button'))
        self.click(id('layout_home'))

        if self.is_exist(id('iv_menu')):
            return True
        else:
            logger(f'[Error] all_shortcut_page_back fail', log_level='error')
            return False

    def enter_shortcut(self, shortcut_name, demo_title=None, audio_tool=None, check=True):
        try:
            demo_title = demo_title or shortcut_name.replace('\n', ' ')

            if not self.is_exist(L.main.shortcut.shortcut_name(), 1):
                if not self.click(L.main.launcher.home, 1):
                    self.click(L.main.shortcut.produce_home, 1)

            if not self.is_exist(L.main.shortcut.shortcut_name(shortcut_name), 1):
                self.click(L.main.shortcut.shortcut_name("More"))

                last_text = ""
                while True:
                    if self.is_exist(L.main.shortcut.all_shortcut_name(shortcut_name), 1):
                        break

                    else:
                        shortcuts_name = self.elements(L.main.shortcut.all_shortcut_name(0))
                        if shortcuts_name[-1].text == last_text:
                            self.driver.swipe_element(shortcuts_name[-1], 'up', 10)
                            shortcuts_name = self.elements(L.main.shortcut.all_shortcut_name(0))
                            if shortcuts_name[-1].text == last_text:
                                logger(f'Last item: {last_text}')
                                logger(f'[Error] Cannot find {shortcut_name} in More page', log_level='error')
                                return False
                        else:
                            last_text = shortcuts_name[-1].text
                            self.h_swipe_element(shortcuts_name[-1], shortcuts_name[0], 3)

            if self.click(L.main.shortcut.shortcut_name(shortcut_name), 1):
                if audio_tool:
                    audio_tool = audio_tool.lower()
                    if audio_tool == 'speech enhance':
                        self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
                    elif audio_tool == 'ai denoise':
                        self.click(L.main.shortcut.audio_tool.demo_ai_denoise)
                    else:
                        logger(f'[Warning] {audio_tool} is not found', log_level='warn')

                else:
                    self.click(id('ok_button'), 1)

                if check:
                    time.sleep(0.5)
                    if (self.is_exist(xpath(f'//*[contains(@resource-id,"tv_title") and contains(@text,"{demo_title}")]')) or
                            self.is_exist(L.import_media.media_library.title) or
                            self.is_exist(id("tv_recommendation"))):
                        return True
                    else:
                        logger(f'[Error] enter_shortcut fail', log_level='error')
                        return False
                return True

            logger(f'[Error] Cannot find {shortcut_name}', log_level='error')
            return False

        except Exception as e:
            traceback.print_exc()
            logger(e)
            return False

    @step("Enter from AI Creation: {name}")
    def enter_ai_feature(self, name, demo_title=None, check=True):
        demo_title = demo_title or name

        self.click(L.main.ai_creation.entry)
        if not self.click(find_string(name), 2):
            last = ""
            while 1:
                features = self.elements(L.main.ai_creation.feature_name(0))
                if features[-1].text == last:
                    logger(f'No feature "{name}"', log_level='error')
                    return False
                else:
                    last = features[-1].text
                    self.h_swipe_element(features[-1], features[0], 3)
                    if self.click(find_string(name), 2):
                        break
        if check:
            if (self.is_exist(xpath(f'//*[contains(@resource-id,"tv_title") and @text="{demo_title}"]')) or
                    self.is_exist(L.import_media.media_library.title) or
                    self.is_exist(id("tv_recommendation"))):
                return True
            else:
                logger(f'[Error] enter_ai_feature fail', log_level='error')
                return False
        return True

    @step("Back from demo page")
    def back_from_demo(self):
        if not self.click(L.main.shortcut.demo_back, 1):
            self.click(L.main.shortcut.close)

        if self.is_exist(L.main.shortcut.shortcut_name(0)) or self.element(L.main.ai_creation.title).text == 'AI Creation':
            return True

        else:
            logger(f'[Error] back_from_demo fail', log_level='error')
            return False

    def mute_demo(self):
        before = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)
        self.click(L.main.shortcut.demo_mute)
        after = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)

        if not HCompareImg(before, after).ssim_compare():
            return "PASS"
        else:
            logger(f'[Error] mute_demo fail', log_level='error')
            return False

    def demo_dont_show_again(self, shortcut_name):
        if not self.is_exist(L.main.shortcut.dont_show_again, 1):
            self.enter_shortcut(shortcut_name, check=False)

        self.click(L.main.shortcut.dont_show_again)
        self.click(L.main.shortcut.try_it_now)

        self.page_main.relaunch(subscribe=False)
        if not self.enter_shortcut(shortcut_name, check=False):
            self.enter_ai_feature(shortcut_name, check=False)

        if self.is_exist(L.main.shortcut.dont_show_again, 1):
            logger(f'[Error] demo_dont_show_again fail', log_level='error')
            return False

        if self.is_exist(find_string('Add Media')):
            return True
        else:
            logger(f'[Error] demo_dont_show_again fail', log_level='error')
            return False

    def reset_dont_show_again(self, shortcut_name):
        self.back_from_media_picker()
        self.back_from_all_shortcut_page()

        self.page_main.enter_setting_in_preferences('Enable All Default Tips')

        self.click(id('iv_back'))
        self.click(id('iv_back'))

        if not self.enter_shortcut(shortcut_name, check=False):
            self.enter_ai_feature(shortcut_name, check=False)

        if self.is_exist(L.main.shortcut.dont_show_again, 1):
            return True
        else:
            logger(f'[Error] reset_dont_show_again fail', log_level='error')
            return False

    def demo_sample_video(self, shortcut_name=None):
        if shortcut_name:
            self.enter_shortcut(shortcut_name, check=False)

        self.click(L.main.shortcut.try_it_now)
        self.click(id('confirm_btn'))
        self.page_edit.waiting_import()
        if self.is_exist(L.edit.menu.export):
            self.click(L.edit.menu.home)
            return True
        else:
            logger(f'[Error] enter_editor fail', log_level='error')
            return False


    def recommendation_close(self, shortcut_name=None):
        if not self.click(L.main.shortcut.ai_sketch.close, 1):
            if not self.click(L.main.shortcut.try_it_now, 1):
                self.enter_shortcut(shortcut_name, check=False)
                self.click(L.main.shortcut.try_it_now, 1)
                self.click(L.main.shortcut.ai_sketch.close)

        if self.is_exist(L.main.shortcut.shortcut_name(0)) or self.element(L.main.ai_creation.title).text == 'AI Creation':
            return True
        else:
            logger(f'[Error] recommendation_close fail', log_level='error')
            return False

    def recommendation_continue(self, shortcut_name=None):
        if shortcut_name:
            self.enter_shortcut(shortcut_name)
            self.click(L.main.shortcut.try_it_now, 1)

        self.click(L.main.shortcut.btn_continue)

        if self.is_exist(L.import_media.media_library.title):
            return True
        else:
            logger(f'[Error] recommendation_continue fail', log_level='error')
            return False
        
    def recommendation_dont_show_again(self, shortcut_name):
        self.enter_shortcut(shortcut_name)

        if not self.is_exist(L.main.shortcut.ai_sketch.close, 1):
            self.click(L.main.shortcut.try_it_now, 1)

        if self.click(L.main.shortcut.ai_sketch.dont_show_again):
            self.click(L.main.shortcut.btn_continue)
            self.page_main.relaunch(subscribe=False)
            self.enter_shortcut(shortcut_name, check=False)
            self.click(L.main.shortcut.try_it_now, 1)
            self.click(id('tv_continue'), 1)
            if self.is_exist(L.import_media.media_library.title):
                return True
            else:
                logger(f'[Error] recommendation_continue fail', log_level='error')
                return False
        else:
            logger(f'[Error] Cannot find dont show again', log_level='error')
            return False

    def enter_media_picker(self, shortcut_name=None, audio_tool=None):
        try:
            if shortcut_name:
                if not self.enter_shortcut(shortcut_name, audio_tool=audio_tool, check=False):
                    self.enter_ai_feature(shortcut_name, check=False)

            self.click(L.main.shortcut.try_it_now, 1)
            self.click(aid('[AID]Upgrade_No'), 1)

            if self.is_exist(find_string('Add Media')):
                return True
            else:
                logger(f'[Error] enter_media_picker fail', log_level='error')
                return False
        except Exception as e:
            traceback.print_exc()
            logger(e)
            return False

    def back_from_media_picker(self):
        with step("Click back button"):
            back_button = xpath('//*[contains(@resource-id,"top_toolbar_back") or contains(@resource-id,"iv_close") or contains(@resource-id,"iv_back")]')
            assert self.click(back_button, 2), 'Click back button failed'

        home_button = xpath('//*[contains(@resource-id,"btn_home") or contains(@resource-id,"iv_back")]')
        if self.is_exist(home_button, 1):
            with step("Click home button"):
                assert self.click(home_button), 'Click home button failed'

        if self.click(L.main.launcher.home):
            return True
        else:
            logger(f'[Error] back_from_media_picker fail', log_level='error')
            return False

    def check_editor(self):
        if self.is_exist(L.edit.menu.export) or self.is_exist(L.main.shortcut.save) or self.is_exist(id('btn_save_menu')) or self.is_exist(find_string('Export')):
            return True
        else:
            logger(f'[Error] check_editor fail', log_level='error')
            return False

    def enter_editor(self, shortcut_name=None, media_type='video', folder=test_material_folder, file=video_9_16, audio_tool=None):
        if shortcut_name or audio_tool:
            self.enter_media_picker(shortcut_name, audio_tool=audio_tool)

        media_type = media_type.lower()
        if media_type not in ['video', 'photo']:
            logger(f'[Error] media_type {media_type} is not found', log_level='error')
            media_type = 'video'

        if media_type == 'video':
            if not self.page_media.select_local_video(folder, file):
                self.page_media.select_local_photo(folder, photo_9_16)
        else:
            self.page_media.select_local_photo(folder, file)

        self.page_edit.waiting()

        if self.check_editor():
            return True
        else:
            logger(f'[Error] enter_editor fail', log_level='error')
            return False

    def back_from_editor(self):
        if not self.click(L.edit.menu.home, 1):
            self.click(id('iv_close'))
            self.click(id('top_toolbar_back'))

        if self.click(L.main.launcher.home):
            return True
        else:
            logger(f'[Error] back_from_editor fail', log_level='error')
            return False

    def back_from_shortcut_editor(self):
        self.click(L.main.shortcut.editor_back)

        if self.is_exist(find_string('Add Media')):
            return True
        else:
            logger(f'[Error] back_from_editor fail', log_level='error')
            return False

    def leave_project(self):
        self.click(L.main.shortcut.editor_home)

        if self.is_exist(L.main.shortcut.shortcut_name(0)):
            return True
        else:
            title = self.element(L.main.ai_creation.title)
            if title:
                if title.text == 'AI Creation':
                    return True
            else:
                logger(f'[Error] leave_project fail', log_level='error')
                return False

    def enter_trim_before_edit(self, shortcut_name=None, audio_tool=None):
        if shortcut_name or audio_tool:
            self.enter_media_picker(shortcut_name, audio_tool=audio_tool)

        for retry in range(12):
            self.click(L.import_media.media_library.btn_preview(retry + 1))
            if self.is_exist(L.import_media.media_library.warning):
                self.click(id('btn_ok'))
            else:
                break
        else:
            logger(f'[Error] enter_trim_before_edit fail', log_level='error')
            return False

        if self.is_exist(L.import_media.media_library.trim_next):
            return True
        else:
            logger(f'[Error] enter_trim_before_edit fail', log_level='error')
            return False

    def back_from_trim(self):
        self.click(L.import_media.media_library.trim_back)

        if self.is_exist(find_string("Add Media")):
            return True
        else:
            logger(f'[Error] back_from_trim fail', log_level='error')
            return False

    def trim_and_import(self, start=100, end=100, shortcut_name=None, audio_tool=None):
        self.enter_trim_before_edit(shortcut_name, audio_tool=audio_tool)

        if start:
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', start)
        if end:
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', end)
        self.click(L.import_media.media_library.trim_next)

        self.page_edit.waiting()

        self.click(id('btn_upgrade'), 1)  # for auto cations

        if self.is_exist(L.edit.menu.export) and self.element(L.edit.menu.export).text == 'Export':
            return True
        else:
            logger(f'[Error] trim_video fail', log_level='error')
            return False

    def timecode(self, is_total_time=False):
        def extract_timecode(element_text):
            """處理 timecode 的提取邏輯"""
            timecode = element_text.strip()
            if '/' in timecode:
                return timecode.split('/')[1 if is_total_time else 0].strip()
            return timecode

        # 嘗試從第一個元素提取 timecode
        timecode_element = self.element(L.edit.menu.timecode) or self.element(id('time_code_text'))
        if timecode_element:
            return extract_timecode(timecode_element.text)

        # 如果找不到元素，記錄錯誤並返回 None
        logger('[Error] timecode element not found')
        return None

    def get_timecode(self):
        return self.timecode()

    def get_total_time(self):
        return self.timecode(is_total_time=True)

    @step('Pause the video if it is currently playing')
    def pause_if_play(self):
        """Pause the video if it is currently playing."""
        def pause_playing():
            timecode_1 = self.get_timecode()
            logger(f'Timecode 1: {timecode_1}')
            time.sleep(0.5)

            timecode_2 = self.get_timecode()
            logger(f'Timecode 2: {timecode_2}')

            if timecode_2 != timecode_1:
                self.click(L.edit.menu.play)
                logger('Pause playing')
            else:
                logger('Preview is not playing')
        pause_playing()
        pause_playing()

    @step('Play the video and verify timecode updates')
    def preview_play(self):
        """Play the video and verify timecode updates."""
        try:
            self.pause_if_play()

            initial_timecode = self.get_timecode()
            if initial_timecode is None:
                logger('[Error] preview_play failed: Initial timecode is None')
                return False

            self.click(L.edit.menu.play)
            if self.click(id('help_not_show_tip_again'), 0.5):
                self.click(id('btn_close'))

            self.pause_if_play()

            updated_timecode = self.get_timecode()
            if updated_timecode is None:
                logger('[Error] preview_play failed: Updated timecode is None')
                return False

            logger(f'Timecode after playing: {updated_timecode}')
            if updated_timecode != initial_timecode:
                return True
            else:
                raise Exception('[Error] preview_play failed: Timecode did not update')
        except Exception as e:
            traceback.print_exc()
            logger(e)
            return False

    @step('Pause the video and verify timecode does not update')
    def preview_pause(self):
        """Pause the video and verify timecode does not update."""
        try:
            self.click(L.edit.menu.play)
            self.pause_if_play()

            timecode_before = self.get_timecode()
            if timecode_before is None:
                logger('[Error] preview_pause failed: Initial timecode is None')
                return False
            logger(f'Timecode before pause: {timecode_before}')

            time.sleep(1)

            timecode_after = self.get_timecode()
            if timecode_after is None:
                logger('[Error] preview_pause failed: Updated timecode is None')
                return False
            logger(f'Timecode after pause: {timecode_after}')

            if timecode_after == timecode_before:
                return True
            else:
                logger('[Error] preview_pause failed: Timecode changed after pause')
                return False
        except Exception as e:
            traceback.print_exc()
            logger(e)
            return False


    def preview_beginning(self):
        try:
            self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
            timecode = self.get_timecode()
            if timecode is None:
                return False

            if timecode == '00:00':
                return True
            else:
                logger('[Error] preview_beginning failed: Timecode is not 00:00')
                return False

        except Exception as e:
            traceback.print_exc()
            logger(e)
            return False

    def preview_ending(self):
        try:
            self.driver.drag_slider_to_max(L.main.shortcut.playback_slider)
            timecode = self.get_timecode()
            if timecode is None:
                return False

            total_time = self.get_total_time()
            if total_time is None:
                return False

            if timecode == total_time:
                return True
            else:
                logger('[Error] preview_ending failed: Timecode does not match total time')
                return False
        except Exception as e:
            traceback.print_exc()
            logger(e)
            return False

    def custom_enter_prompt(self, prompt='Apple'):
        self.click(find_string('Custom'))
        self.element(L.main.shortcut.ai_art.prompt).send_keys(prompt)
        text = self.element(L.main.shortcut.ai_art.prompt).text

        if text == prompt:
            return True
        else:
            logger(f'[Error] custom_enter_prompt fail', log_level='error')
            return False

    def custom_clear_prompt(self):
        self.click(L.main.shortcut.ai_art.clear)
        text = self.element(L.main.shortcut.ai_art.prompt).text

        if 'Please provide a description' in text:
            return True
        else:
            logger(f'[Error] custom_clear_prompt fail', log_level='error')
            return False

    def custom_generate(self):
        self.custom_enter_prompt()

        retry = 30
        for _ in range(retry):
            self.click(L.main.shortcut.ai_art.apply)
            self.click(aid('[AID]ConfirmDialog_No'), 1)
            self.page_main.shortcut.waiting_generated()
            if not self.click(id('ok_button'), 1):
                break
        else:
            raise Exception(f"Exceeded retry limit: {retry}")

        preview = self.page_edit.get_preview_pic()
        if HCompareImg(preview).is_not_black():
            return True
        else:
            logger(f'[Error] custom_generate fail', log_level='error')
            return False

    def custom_enter_prompt_history(self):
        self.click(find_string('Custom'), 1)
        time.sleep(0.5)
        self.click(L.main.shortcut.ai_art.custom_history)

        if self.element(L.main.shortcut.ai_art.page_title).text == 'History':
            return True
        else:
            logger(f'[Error] custom_enter_prompt_history fail', log_level='error')
            return False

    def custom_import_history_prompt(self):
        prompt = self.element(L.main.shortcut.ai_art.history_prompt(0)).text
        self.click(L.main.shortcut.ai_art.history_prompt(0))

        if self.element(L.main.shortcut.ai_art.prompt).text == prompt:
            return True
        else:
            logger(f'[Error] custom_import_prompt_history fail', log_level='error')
            return False

    def custom_regenerate_history_prompt(self):
        retry = 30
        for _ in range(retry):
            self.click(L.main.shortcut.ai_art.apply)
            self.click(aid('[AID]ConfirmDialog_No'), 1)
            self.page_main.shortcut.waiting_generated()
            if not self.click(id('ok_button'), 1):
                break
        else:
            raise Exception(f"Exceeded retry limit: {retry}")

        preview = self.page_edit.get_preview_pic()
        if HCompareImg(preview).is_not_black():
            return True
        else:
            logger(f'[Error] custom_generate fail', log_level='error')
            return False

    def custom_delete_prompt_history(self):
        self.custom_enter_prompt_history()
        self.click(id("tv_select_cancel"))
        self.click(id("tv_select_clear_all"))
        self.click(id('tv_delete'))
        self.click(id("delete_button"))

        if self.is_exist(id("btn_generate_now")):
            self.custom_leave_prompt_history()
            return True
        else:
            self.custom_leave_prompt_history()
            logger(f'[Error] custom_delete_prompt_history fail', log_level='error')
            return False

    def custom_leave_prompt_history(self):
        self.click(L.main.shortcut.ai_art.close)

        if self.is_exist(L.main.shortcut.ai_art.prompt):
            return True
        else:
            logger(f'[Error] custom_leave_prompt_history fail', log_level='error')
            return False

    def style_generate(self):
        self.click(id("empty_area"))
        retry = 30
        for _ in range(retry):
            self.click(L.main.shortcut.ai_art.style_name(2))
            self.click(aid('[AID]ConfirmDialog_No'), 1)

            if self.is_exist(L.main.shortcut.ai_art.generating, 1):
                self.is_not_exist(L.main.shortcut.ai_art.generating, 120)

            if not self.click(id('ok_button'), 1):
                break
        else:
            logger(f'[Error] Exceeded retry limit', log_level='error')
            return False
        return True

    def style_regenerate(self):
        retry = 30
        for _ in range(retry):
            self.click(L.main.shortcut.ai_art.regenerate)
            self.click(aid('[AID]ConfirmDialog_No'), 1)

            if self.is_exist(L.main.shortcut.ai_art.generating, 1):
                self.is_not_exist(L.main.shortcut.ai_art.generating, 120)

            if not self.click(id('ok_button'), 1):
                break
        else:
            logger(f'[Error] Exceeded retry limit', log_level='error')
            return False
        return True

    def compare_enabled(self):
        self.click(L.main.shortcut.ai_art.compare)

        if (self.element(L.main.shortcut.ai_art.compare).get_attribute('selected') == 'true' and
                self.element(L.main.shortcut.ai_art.compare).text == "Compare On"):
            return True
        else:
            logger(f'[Error] compare_enabled fail', log_level='error')
            return False

    def compare_move_line(self):
        thumb = self.element(L.main.shortcut.photo_enhance.compare_thumb)
        rect = thumb.rect
        y = rect['y']

        window_width = self.driver.driver.get_window_size()['width']
        x_end = window_width * 0.7
        self.page_main.h_drag_element(thumb, x_end, y)

    def compare_disable(self):
        self.click(L.main.shortcut.ai_art.compare)

        if (self.element(L.main.shortcut.ai_art.compare).get_attribute('selected') == 'false'
                and self.element(L.main.shortcut.ai_art.compare).text == "Compare Off"):
            return True
        else:
            logger(f'[Error] compare_disable fail', log_level='error')
            return False

    def enter_history(self):
        self.click(L.main.shortcut.ai_art.history)

        return True if self.element(id("title")).text == "History" else False

    def close_history(self):
        self.click(L.main.shortcut.ai_art.close_history)

        return True if not self.is_exist(find_string('History'), 1) else False

    def reopen_history_image(self, history_image):
        self.click(L.main.shortcut.ai_art.history_image(2))
        preview = self.page_edit.get_preview_pic()

        return HCompareImg(preview, history_image).ssim_compare()

    def enter_crop(self):
        self.click(L.main.shortcut.crop)

        if self.element(L.main.shortcut.crop_title).text == 'Crop Photo':
            return True
        else:
            logger(f'[Error] enter_crop fail', log_level='error')
            return False

    def leave_crop(self):
        self.click(L.main.shortcut.crop_close)

        if self.is_exist(L.main.shortcut.ai_art.style_name()):
            return True
        else:
            logger(f'[Error] leave_crop fail', log_level='error')
            return False

    def crop_ratio(self, ratio):
        ratio = ratio.lower()
        ratio_dir = {
            'original': L.edit.crop.btn_original,
            'free': L.edit.crop.btn_free,
            '9:16': L.edit.crop.btn_9_16,
            '1:1': L.edit.crop.btn_1_1,
            '4:5': L.edit.crop.btn_4_5,
            '16:9': L.edit.crop.btn_16_9,
            '4:3': L.edit.crop.btn_4_3,
            '3:4': L.edit.crop.btn_3_4,
            '21:9': L.edit.crop.btn_21_9,
        }

        if ratio_dir.get(ratio) is None:
            logger(f'[Error] crop_ratio {ratio} is not found', log_level='error')
            return False

        # preview = self.element(L.edit.preview.preview)
        #
        # if ratio == 'original' or ratio == 'free':
        #     width = preview.size.get('width')
        #     height = preview.size.get('height')

        self.click(L.main.shortcut.crop)
        crop_buttons = self.elements(xpath('//*[contains(@resource-id, "btn_crop")]'))

        if ratio == 'original':
            self.h_swipe_element(crop_buttons[0], crop_buttons[-1], 3)
        if not self.click(ratio_dir[ratio], 1):
            self.h_swipe_element(crop_buttons[-1], crop_buttons[0], 3)
            if not self.click(ratio_dir[ratio], 1):
                logger(f'[Error] crop_ratio {ratio} fail', log_level='error')
                return False

        self.page_edit.drag_crop_boundary()
        self.page_main.shortcut.waiting_generated(L.edit.crop.apply)

        return True

        # preview = self.element(L.edit.preview.preview)
        # new_width = preview.size.get('width')
        # new_height = preview.size.get('height')

        # if ratio == 'original':
        #     if new_width == width and new_height == height:
        #         return True
        #     else:
        #         logger(f'[Error] crop_ratio {ratio} fail', log_level='error')
        #         return False
        # elif ratio == 'free':
        #     if new_width != width or new_height != height:
        #         return True
        #     else:
        #         logger(f'[Error] crop_ratio {ratio} fail', log_level='error')
        #         return False
        # else:
        #     preview_ratio = new_width / new_height
        #     parts = ratio.split(':')
        #     numerator = float(parts[0])
        #     denominator = float(parts[1])
        #     if denominator == 0:
        #         logger('Denominator cannot be zero')
        #         return False
        #     new_ratio = numerator / denominator
        #     if abs(preview_ratio - new_ratio) < 0.1:
        #         return True
        #     else:
        #         logger(f'[Error] crop_ratio {ratio} fail', log_level='error')
        #         return False

    def crop_reset(self):
        self.click(L.main.shortcut.crop)
        self.click(L.edit.crop.reset)
        self.page_main.shortcut.waiting_generated(L.edit.crop.apply)


    def add_background_photo(self, folder=test_material_folder, file=photo_9_16):
        pass

    def remove_background(self):
        self.click(find_string("Image"))
        self.click(L.main.shortcut.item(2))

    def export(self):
        return self.page_edit.export()

    def export_cancel(self):
        self.click(L.edit.menu.export)
        self.click(L.main.shortcut.export_close)

        if not self.is_exist(L.main.shortcut.save_image, 1):
            return True
        else:
            logger(f'[Error] export_cancel fail', log_level='error')
            return False

    def export_back(self):
        with step('Click export button'):
            assert self.click(L.edit.menu.export), 'Click export button failed'
        with step('Click back button'):
            assert self.click(L.edit.menu.produce_sub_page.back), 'Click back button failed'

        time.sleep(1)

        if not self.is_exist(L.edit.menu.produce_sub_page.produce, 1):
            return True
        else:
            logger(f'[Error] export_back fail', log_level='error')
            return False

    def export_save_image(self):
        self.click(xpath('//*[contains(@resource-id,"btn_save_menu") or @text="Export"]'))
        self.click(L.main.shortcut.save_image)

        if self.is_exist(L.main.shortcut.save_to_camera_roll):
            return True
        else:
            logger(f'[Error] export_save_image fail', log_level='error')
            return False

    def export_back_to_editor(self):
        self.click(L.main.shortcut.produce_back)
        self.click(find_string('Not Now'), 1)

        if self.check_editor():
            return True
        else:
            logger(f'[Error] export_back_to_editor fail', log_level='error')
            return False

    def export_back_to_launcher(self):
        self.click(L.main.shortcut.produce_home)

        if self.is_exist(L.main.shortcut.shortcut_name(0)) or self.element(L.main.ai_creation.title).text == 'AI Creation':
            return True
        else:
            logger(f'[Error] export_back_to_launcher fail', log_level='error')
            return False

    def save_image(self):
        self.click(L.main.shortcut.save)

        if self.is_exist(L.main.shortcut.save_to_camera_roll):
            return True
        else:
            logger(f'[Error] save_image fail', log_level='error')
            return False

    def tti_enter_prompt(self, prompt="x" * 401):
        if not self.click(L.main.shortcut.tti.input_box, 1):
            if not self.click(L.main.shortcut.tti.prompt):
                self.enter_shortcut('Text to Image')
                self.click(L.main.shortcut.tti.prompt)
                if not self.click(L.main.shortcut.tti.input_box):
                    logger(f'[Error] Cannot find input box', log_level='error')
                    return False

        input_box = self.element(L.main.shortcut.tti.input_box, 1)
        input_box.send_keys(prompt)
        self.click(L.main.shortcut.tti.done)

        if self.element(L.main.shortcut.tti.prompt).text == prompt:
            return True
        else:
            logger(f'[Error] tti_enter_prompt fail', log_level='error')
            return False

    def tti_clear_prompt(self):
        self.click(L.main.shortcut.tti.prompt)
        self.click(L.main.shortcut.tti.clear)
        self.click(L.main.shortcut.tti.done)

        if "Type more than 10 words" in self.element(L.main.shortcut.tti.prompt).text:
            return True
        else:
            logger(f'[Error] tti_clear_prompt fail', log_level='error')
            return False

    def tti_recommend_prompt(self):
        self.click(L.main.shortcut.tti.prompt)

        tags = self.elements(L.main.shortcut.tti.recommend)
        for tag in tags:
            tag.click()

        prompt = self.element(L.main.shortcut.tti.input_box).text
        self.click(L.main.shortcut.tti.done)

        if self.element(L.main.shortcut.tti.prompt).text == prompt:
            return prompt
        else:
            logger(f'[Error] tti_recommend_prompt fail', log_level='error')
            return False

    def tti_generate(self, prompt=None):
        if prompt:
            self.tti_enter_prompt(prompt)

        self.click(L.main.shortcut.tti.generate)
        self.click(L.main.shortcut.tti.generate_ok)

        if self.is_exist(L.main.shortcut.tti.select):
            return True
        else:
            logger(f'[Error] tti_generate fail', log_level='error')
            return False

    def tti_wait_generated(self):
        if self.is_exist(L.main.shortcut.tti.generating, 1):
            self.is_not_exist(L.main.shortcut.tti.generating, 120)

        if self.is_exist(L.main.shortcut.tti.generated_image(), 1):
            return True
        else:
            logger(f'[Error] tti_wait_generated fail', log_level='error')
            return False