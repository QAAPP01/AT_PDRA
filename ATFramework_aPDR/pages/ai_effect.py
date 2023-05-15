from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


class AIEffect(BasePage):
    def __init__(self, *args, **kwargs):
        BasePage.__init__(self, *args, **kwargs)
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.click = self.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

    def enter_template_library(self, skip_launch=False):
        if not skip_launch:
            self.page_main.enter_launcher()
        self.click(L.ai_effect.launcher.ai_effect_entry)

    def enter_template_full_preview(self, skip_enter_template_library=False, skip_launch=False):
        if not skip_enter_template_library:
            self.enter_template_library(skip_launch)
        self.click(L.main.ai_effect.template())

    def enter_free_template_media_picker(self, skip_enter_template_library=False, skip_launch=False, clip=1):
        self.enter_template_full_preview(skip_enter_template_library, skip_launch)
        if clip == 1:
            clip = "1 clip"
        else:
            clip = f"{clip} clips"

        # swipe up to free template for export test and 1 clip required
        while self.is_exist(L.main.ai_effect.premium, 1) or self.element(L.main.ai_effect.template_clip_number()).text != clip:
            page_before = self.element(L.main.ai_effect.full_preview)
            self.driver.swipe_up()
            if page_before == self.element(L.main.ai_effect.full_preview):
                logger('[FAIL] Template End')
                return False
        self.click(L.main.ai_effect.try_now)
        return True

    def enter_editor(self, skip_enter_template_library=False, skip_launch=False, clip=1):
        self.enter_free_template_media_picker(skip_enter_template_library, skip_launch, clip)
        j = 1
        for i in range(clip):
            clip_duration = self.element(L.ai_effect.editor.media_picker.clip_duration(i + 1))
            clip_duration = float(clip_duration.split("s")[0])
            media_duration = self.element(L.import_media.media_library.duration(j)).text
            media_duration = float(media_duration.split(":")[0])*60 + float(media_duration.split(":")[1])
            for k in range(len(self.elements(L.import_media.media_library.duration(0)))):
                if media_duration < clip_duration:
                    j += 1
                    media_duration = self.element(L.import_media.media_library.duration(j)).text
                    media_duration = float(media_duration.split(":")[0]) * 60 + float(media_duration.split(":")[1])
                else:
                    self.click(L.import_media.media_library.duration(j))
                    j += 1
                    break
        self.click(L.import_media.media_library.next)
        self.page_media.waiting_download()
        if self.is_exist(L.main.ai_effect.produce):
            return True
        else:
            logger('[FAIL] No produce button')

    def leave_editor_to_library(self, reenter=False, clip=1):
        self.click(L.main.ai_effect.close)
        self.click(L.main.ai_effect.leave)
        if reenter:
            if self.enter_editor(skip_enter_template_library=True, clip=clip):
                return True
            else:
                return False
        else:
            if self.is_exist(L.main.ai_effect.template()):
                return True
            else:
                logger('No template')
                return False
