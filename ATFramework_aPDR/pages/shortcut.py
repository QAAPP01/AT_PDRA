import traceback

from .locator import locator as L
from .locator.locator_type import *
from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.pages.main_page import MainPage
from ATFramework_aPDR.pages.edit import EditPage
from ATFramework_aPDR.pages.import_media import MediaPage
from ATFramework_aPDR.ATFramework.utils.log import logger

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
        if not self.is_exist(L.main.shortcut.shortcut_name(shortcut_name), 1):
            self.click(xpath('//*[@text="More"]'))

        if self.click(L.main.shortcut.shortcut_name(shortcut_name)):
            return True
        else:
            logger(f'[Error] enter_shortcut fail', log_level='error')
            return False

    def back_from_demo(self):
        self.click(L.main.shortcut.demo_back)

        if self.is_exist(L.main.shortcut.shortcut_name(0)):
            return True
        else:
            logger(f'[Error] back_from_demo fail', log_level='error')
            return False

    def enter_media_picker(self, shortcut_name=None):
        try:
            if shortcut_name:
                self.enter_shortcut(shortcut_name)
            self.click(L.main.shortcut.try_it_now, 1)

            if self.is_exist(find_string('Add Media')):
                return True
            else:
                logger(f'[Error] enter_media_picker fail', log_level='error')
                return False
        except Exception:
            traceback.print_exc()


    def back_from_media_picker(self):
        self.click(L.import_media.media_library.back)

        if self.is_exist(L.main.shortcut.shortcut_name(0)):
            return True
        else:
            logger(f'[Error] back_from_media_picker fail', log_level='error')
            return False

    def enter_editor(self, shortcut_name=None, folder=test_material_folder, file=video_9_16):
        if shortcut_name:
            self.enter_media_picker(shortcut_name)
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

    def enter_trim_before_edit(self, shortcut_name=None):
        if shortcut_name:
            self.enter_media_picker(shortcut_name)
        self.click(L.import_media.media_library.btn_preview())

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

    def trim_and_edit(self, start=100, end=100):
        self.click(L.import_media.media_library.btn_preview())
        if start:
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', start)
        if end:
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', end)
        self.click(L.import_media.media_library.trim_next)
        self.page_edit.waiting()

        if self.is_exist(L.main.shortcut.export) and self.element(L.main.shortcut.trimmed_video).text == 'Export':
            return True
        else:
            logger(f'[Error] trim_video fail', log_level='error')
            return False

    def export(self):
        self.click(L.main.shortcut.export)
        self.click(L.main.shortcut.produce)
        self.page_edit.waiting_produce()

        if self.is_exist(L.main.shortcut.save_to_camera_roll):
            return True
        else:
            logger(f'[Error] export fail', log_level='error')
            return False
