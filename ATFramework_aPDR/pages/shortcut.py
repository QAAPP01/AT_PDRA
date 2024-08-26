import time
import traceback

from .locator import locator as L
from .locator.locator_type import *
from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.pages.main_page import MainPage
from ATFramework_aPDR.pages.edit import EditPage
from ATFramework_aPDR.pages.import_media import MediaPage
from ATFramework_aPDR.ATFramework.utils.log import logger
from ..ATFramework.utils.compare_Mac import HCompareImg

test_material_folder = '00PDRa_Testing_Material'
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Shortcut(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_main = MainPage(driver)
        self.page_edit = EditPage(driver)
        self.page_media = MediaPage(driver)
        self.driver = driver

    def enter_shortcut(self, shortcut_name):
        self.click(L.main.shortcut.produce_home, 0.5)
        if not self.is_exist(L.main.shortcut.shortcut_name(shortcut_name), 1):
            self.click(xpath('//*[@text="Expand"]'))

        if self.click(L.main.shortcut.shortcut_name(shortcut_name)):
            return True
        else:
            logger(f'[Error] enter_shortcut fail', log_level='error')
            return False

    def back_from_demo(self):
        self.click(L.main.shortcut.demo_back)

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

    def enter_media_picker(self, shortcut_name=None, audio_tool=None):
        try:
            if shortcut_name:
                if not self.enter_shortcut(shortcut_name):
                    self.page_main.enter_ai_feature(shortcut_name)

            if audio_tool:
                audio_tool = audio_tool.lower()
                if audio_tool == 'speech enhance':
                    self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
                elif audio_tool == 'ai denoise':
                    self.click(L.main.shortcut.audio_tool.demo_ai_denoise)
                else:
                    logger(f'[Warning] {audio_tool} is not found', log_level='warn')

            self.click(L.main.shortcut.try_it_now, 1)

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
        self.click(L.import_media.media_library.back)

        if self.is_exist(L.main.shortcut.shortcut_name(0)):
            return True
        else:
            logger(f'[Error] back_from_media_picker fail', log_level='error')
            return False

    def enter_editor(self, shortcut_name=None, folder=test_material_folder, file=video_9_16, audio_tool=None):
        if shortcut_name or audio_tool:
            self.enter_media_picker(shortcut_name, audio_tool=audio_tool)

        self.page_media.select_local_video(folder, file)
        self.page_edit.waiting()

        if self.is_exist(L.main.shortcut.export):
            return True
        else:
            logger(f'[Error] enter_editor fail', log_level='error')
            return False

    def back_from_editor(self):
        self.click(L.main.shortcut.editor_back)

        if self.is_exist(find_string('Add Media')):
            return True
        else:
            logger(f'[Error] back_from_editor fail', log_level='error')
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

    def trim_and_edit(self, start=100, end=100, shortcut_name=None, audio_tool=None):
        self.enter_trim_before_edit(shortcut_name, audio_tool=audio_tool)

        if start:
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', start)
        if end:
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', end)
        self.click(L.import_media.media_library.trim_next)
        self.page_edit.waiting()

        self.click(id('btn_upgrade'), 1)  # for auto cations

        if self.is_exist(L.main.shortcut.export) and self.element(L.main.shortcut.export).text == 'Export':
            return True
        else:
            logger(f'[Error] trim_video fail', log_level='error')
            return False

    def play_preview(self):
        try:
            time.sleep(1)
            timecode = self.element(L.main.shortcut.timecode).text
            if timecode != '00:00':
                self.click(L.main.shortcut.play)
                timecode = self.element(L.main.shortcut.timecode).text
            self.click(L.main.shortcut.play)
            time.sleep(2)
            self.click(L.main.shortcut.play)
            if self.element(L.main.shortcut.timecode).text != timecode:
                return True
            else:
                raise '[Error] play_preview fail'
        except Exception as e:
            traceback.print_exc()
            logger(e)
            return False

    def play_position_start(self):
        self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
        timecode = self.element(L.main.shortcut.timecode).text

        if timecode == '00:00':
            return True
        else:
            logger(f'[Error] play_position_start fail', log_level='error')
            return False

    def play_position_end(self):
        self.driver.drag_slider_to_max(L.main.shortcut.playback_slider)
        timecode = self.element(L.main.shortcut.timecode).text

        if timecode == self.element(L.main.shortcut.total_time).text:
            return True
        else:
            logger(f'[Error] play_position_end fail', log_level='error')
            return False

    def add_background_photo(self, folder=test_material_folder, file=photo_9_16):
        pass

    def remove_background(self):
        self.click(find_string("Image"))
        self.click(L.main.shortcut.item(2))

    def export(self):
        self.click(L.main.shortcut.export)
        self.click(L.main.shortcut.produce)
        self.page_edit.waiting_produce()

        if self.is_exist(L.main.shortcut.save_to_camera_roll):
            return True
        else:
            logger(f'[Error] export fail', log_level='error')
            return False

    def tti_back(self):
        self.click(L.main.shortcut.close)
