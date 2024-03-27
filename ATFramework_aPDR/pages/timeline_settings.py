import sys,time
from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.utils.extra import element_exist_click
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage
from appium.webdriver.common.touch_action import TouchAction

from .locator import locator as L
from .locator.locator_type import *
from .locator.locator import edit as E


class TimelineSettingsPage(BasePage):

    def __init__(self, *args, **kwargs):
        BasePage.__init__(self, *args, **kwargs)
        self.test_material_folder = '00PDRa_Testing_Material'
        self.page_media = PageFactory().get_page_object("import_media", self.driver)

    def check_setting(self, locator):
        max_swipe_time = 20
        last = L.timeline_settings.preference.reset_all_tips
        try:
            for i in range(max_swipe_time):
                if not self.is_exist(locator, 1):
                    if self.is_exist(last, 1):
                        break
                    else:
                        self.driver.swipe_element(L.timeline_settings.preference.scroll_view, 'up')
                else:
                    return True if self.element(locator).get_attribute('checked') == 'true' else False
            raise Exception(f'No found "{locator}"')
        except Exception as err:
            raise Exception(f'[Error] {err}')

    def click_setting(self, locator):
        max_swipe_time = 20
        last = L.timeline_settings.preference.reset_all_tips
        try:
            for i in range(max_swipe_time):
                if not self.click(locator, 1):
                    if self.is_exist(last, 1):
                        break
                    else:
                        self.driver.swipe_element(L.timeline_settings.preference.scroll_view, 'up')
                else:
                    return True
            raise Exception(f'No found "{locator}"')
        except Exception as err:
            raise Exception(f'[Error] {err}')



    def enter_advanced_page(self):
        logger("start >> enter_advanced_page <<")
        try:
            is_complete = 0
            for retry in range(4):
                if self.is_exist(L.timeline_settings.settings.advanced_setting):
                    self.el(L.timeline_settings.settings.advanced_setting).click()
                    time.sleep(1)
                    is_complete = 1
                    break
                else:
                    self.driver.swipe_element(L.edit.settings.scroll_view, 'up', 500)
                    time.sleep(1)
            if is_complete == 0:
                logger("operation fail")
                raise Exception
        except Exception:
            logger("find element fail")
            raise Exception

    def SetPanZoom(self, status='ON'): #status=ON/ OFF
        logger("start >> SetPanZoom <<")
        try:
            self.enter_advanced_page()
            element = self.el(L.timeline_settings.settings.default_pan_zoom_effect)
            if element.get_attribute('text') != str(status):
                element.click()
                logger(f"SetPanZoom as {status} OK")
            self.driver.driver.back()
        except Exception:
            logger("find element fail")
            raise Exception
        return True

    def h_setting_duration(self, percentage, offset=0.055):  # percentage: 0~1  ex: 0.5
        slider = self.h_get_element(L.edit.settings.DefaultImageDuration.slider).rect
        width = slider["width"]
        offset_width = width - 2 * width * offset
        start_x = slider["x"] + width * offset
        y = slider["y"] + slider["height"] / 2
        end_x = start_x + percentage * offset_width
        self.h_tap(end_x, y)
        return True

    def set_default_image_duration(self, expect_duration='5.0'):
        logger("start >> set_default_image_duration <<")
        logger(f"expect_duration={expect_duration}")
        try:
            self.enter_advanced_page()
            self.el(L.timeline_settings.settings.default_image_duration).click()
            el_slider = self.el(L.timeline_settings.default_image_duration.slider)
            time.sleep(3)
            el_slider.set_text(str(float(expect_duration)*10-1))
            time.sleep(3)
            txt_duration = self.el(L.timeline_settings.default_image_duration.txt_duration).get_attribute('text')
            time.sleep(3)
            if txt_duration != f'{expect_duration} s':
                logger(f"Fail to set duration as {expect_duration} s, current duration is {txt_duration}")
                raise Exception
            self.el(L.timeline_settings.default_image_duration.ok).click()
            time.sleep(5)
            self.driver.driver.back()
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True



    def set_default_transition_duration(self, expect_duration='2.0'):
        logger("start >> set_default_transition_duration <<")
        logger(f"expect_duration={expect_duration}")
        try:
            self.enter_advanced_page()
            logger("entered advanced pate")
            self.el(L.timeline_settings.settings.default_transition_duration).click()
            logger("click on duration")
            txt_duration = self.el(L.timeline_settings.default_transition_duration.txt_duration).get_attribute('text')
            logger(f"get duration = {txt_duration}")
            if txt_duration != f'{expect_duration} s':
                el_slider = self.el(L.timeline_settings.default_transition_duration.slider)
                el_slider.set_text(str(float(expect_duration)*10-1))
                txt_duration = self.el(L.timeline_settings.default_transition_duration.txt_duration).get_attribute('text')
                if txt_duration != f'{expect_duration} s':
                    logger(f"Fail to set duration as {expect_duration} s, current duration is {txt_duration}")
                    raise Exception
            self.el(L.timeline_settings.default_transition_duration.ok).click()
            logger(f"apply change")
            self.driver.driver.back()
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True

    def set_default_title_duration(self, expect_duration='5.0'):
        logger("start >> set_default_title_duration <<")
        logger(f"expect_duration={expect_duration}")
        try:
            self.enter_advanced_page()
            self.el(L.timeline_settings.settings.default_title_duration).click()
            txt_duration = self.el(L.timeline_settings.default_title_duration.txt_duration).get_attribute('text')
            if txt_duration != f'{expect_duration} s':
                el_slider = self.el(L.timeline_settings.default_title_duration.slider)
                el_slider.set_text(str(float(expect_duration)*10-5))
                txt_duration = self.el(L.timeline_settings.default_title_duration.txt_duration).get_attribute('text')
                if txt_duration != f'{expect_duration} s':
                    logger(f"Fail to set duration as {expect_duration} s, current duration is {txt_duration}")
                    raise Exception
            self.el(L.timeline_settings.default_title_duration.ok).click()
            self.driver.driver.back()
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True

    def reset_all_tips(self):
        logger("start >> reset_all_tips <<")
        try:
            self.enter_advanced_page()
            is_complete = 0
            for retry in range(4):
                if self.is_exist(L.timeline_settings.settings.reset_all_tips):
                    self.el(L.timeline_settings.settings.reset_all_tips).click()
                    time.sleep(1)
                    is_complete = 1
                    break
                self.swipe_up()
                time.sleep(1)
            self.driver.driver.back()
            if is_complete == 0:
                logger("operation fail")
                raise Exception
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True
    
    def open_tool_menu_when_selecting(self, status='ON'): #status=ON/ OFF
        logger("start >> open_tool_menu_when_selecting <<")
        try:
            element = self.el(L.timeline_settings.settings.open_tool_menu_switch)
            if element.get_attribute('text') != str(status):
                element.click()
                logger(f"set open_tool_menu_when_selecting as {status} OK")
        except Exception:
            logger("find element fail")
            raise Exception
        return True

    def tap_remove_watermark(self):
        logger("start >> tap_remove_watermark <<")
        try:
            element = self.el(L.timeline_settings.settings.remove_watermark)
            element.click()
            return True
        except Exception:
            logger("find element fail")
            raise Exception

    def display_file_name_in_library(self, status='ON'):    # status=ON/ OFF
        logger("start >> display_file_name_in_library <<")
        try:
            element = self.el(L.timeline_settings.settings.display_file_name_switch)
            if element.get_attribute('text') != str(status):
                element.click()
                logger(f"set display_file_name_in_library as {status} OK")
        except Exception:
            logger("find element fail")
            raise Exception
        return True

    def select_default_video_quality(self, quality='fhd'):  # quality= uhd/fhd/hd/sd
        logger("start >> select_default_video_quality <<")
        try:
            element = self.el(L.timeline_settings.settings.text_video_quality)
            element.click()
            locator = id(f'radio_btn_{quality}')
            radio_button = self.el(locator)
            radio_button.click()
        except Exception:
            logger("find element fail")
            raise Exception
        return True

    def get_settings_default_video_quality(self):
        logger("start >> get_settings_default_video_quality <<")
        try:
            txt_quality = self.el(L.timeline_settings.settings.text_video_quality).get_attribute('text')
            logger(f"get_settings_default_video_quality={txt_quality}")
        except Exception:
            logger("Exception occurs")
            return False
        return txt_quality

    def select_settings_video_quality_radio(self, target):
        logger("start >> select_settings_video_quality_radio <<")
        try:
            if target == 'uhd':
                self.el(L.timeline_settings.default_video_quality.radio_btn_uhd).click()
            elif target == 'fhd':
                self.el(L.timeline_settings.default_video_quality.radio_btn_fhd).click()
            elif target == 'hd':
                self.el(L.timeline_settings.default_video_quality.radio_btn_hd).click()
            elif target == 'sd':
                self.el(L.timeline_settings.default_video_quality.radio_btn_sd).click()
            else:
                logger("Can't find elements")
                return False
            return True
        except Exception:
            logger("Exception occurs")
            return False

    def get_settings_video_quality_radio_is_checked(self):
        logger("start >> get_settings_video_quality_radio_is_checked <<")
        try:
            if self.el(L.timeline_settings.default_video_quality.radio_btn_uhd).get_attribute('checked') == 'true':
                logger(f"UHD is checked.")
                return 'uhd'
            elif self.el(L.timeline_settings.default_video_quality.radio_btn_fhd).get_attribute('checked') == 'true':
                logger(f"FHD is checked.")
                return 'fhd'
            elif self.el(L.timeline_settings.default_video_quality.radio_btn_hd).get_attribute('checked') == 'true':
                logger(f"HD is checked.")
                return 'hd'
            elif self.el(L.timeline_settings.default_video_quality.radio_btn_sd).get_attribute('checked') == 'true':
                logger(f"SD is checked.")
                return 'sd'
            else:
                logger("Can't find elements")
                return False
        except Exception:
            logger("Exception occurs")
            return False

    def select_ui_mode_radio(self, target):
        logger("start >> select_ui_mode_radio <<")
        try:
            self.el(L.timeline_settings.settings.settings_edit_mode).click()
            if target == 'Portrait':
                self.el(L.timeline_settings.settings.radio_btn_portrait).click()
            elif target == 'Landscape':
                self.el(L.timeline_settings.settings.radio_btn_landscape).click()
            elif target == 'Auto-rotate':
                self.el(L.timeline_settings.settings.radio_btn_auto).click()
            else:
                logger("Can't find elements")
                return False
            return True
        except Exception:
            logger("Exception occurs")
            return False

    def get_selected_ui_mode(self):
        logger("start >> get_selected_ui_mode <<")
        try:
            txt_mode = self.el(L.timeline_settings.settings.current_UI_mode_text).get_attribute('text')
            logger(f"get_selected_ui_mode={txt_mode}")
        except Exception:
            logger("Exception occurs")
            return False
        return txt_mode