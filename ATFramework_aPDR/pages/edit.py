import sys,time
import os
import shutil
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from os.path import dirname
from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.ATFramework.utils.extra import element_exist_click
from ATFramework.utils.log import logger
from ATFramework.utils.compare_Mac import CompareImage

from .locator import locator as L
from .locator.locator_type import *
from .locator.locator import edit as E

from SFT.conftest import PACKAGE_NAME

class Sub_item():
    def __init__(self,driver,item):
        dict_max = {
            "Brightness" : 200,
            "Contrast" : 200,
            "Saturation" : 200,
            "Hue" : 200,
            "Skin Brightness" : 60,
            "Opacity" : 100,
        }
        self.driver = driver
        self.item = item
        self.max = dict_max.get(item,100)
        self.el = lambda id: driver.find_element(id[0], id[1])
        self.els = lambda id: driver.find_elements(id[0], id[1])

    def update(self):
        implicitly_previous = self.driver.implicitly_wait()
        self.driver.implicitly_wait(0.5)
        time.sleep(1)
        retry = 3
        frames = None
        while (retry > 0):
            try:
                logger("finding Frame:" + str(L.edit.color_sub.adjust_sub.frames))
                frames = self.els(L.edit.color_sub.adjust_sub.frames)
                frames_chroma = self.els(L.edit.color_sub.chromakey_sub.frames)
                logger("Frame found!")
                is_found = False
                for frame in frames:
                    logger("find string: %s" % str(find_string(self.item)))
                    try:
                        if  frame.find_element(*L.edit.color_sub.adjust_sub.progress):
                            logger("string found!")
                            self.elem_number = frame.find_element(*L.edit.color_sub.adjust_sub.number)
                            self.elem_progress = frame.find_element(*L.edit.color_sub.adjust_sub.progress)
                            is_found = True
                            logger("exit for now")
                            break   # break for loop if found the number & progress
                        else:
                            logger('Name: [%s] is not found' % self.item)
                    except:
                        logger("number/progress  is not found")
                for frame in frames_chroma:
                    logger("find string: %s" % str(find_string(self.item)))
                    try:
                        if  frame.find_element(*L.edit.color_sub.chromakey_sub.progress):
                            logger("string found!")
                            self.elem_number = frame.find_element(*L.edit.color_sub.chromakey_sub.number)
                            self.elem_progress = frame.find_element(*L.edit.color_sub.chromakey_sub.progress)
                            is_found = True
                            logger("exit for now")
                            break   # break for loop if found the number & progress
                        else:
                            logger('Name: [%s] is not found' % self.item)
                    except:
                        logger("number/progress  is not found")                                
                if is_found:
                    logger("exit while now")
                    break # break while if no exception
                else:
                    logger("string/number/progress is not found.")
                    raise
            except:
                logger('"%s" is not found! Swipe up and try again! %d'% (str(L.edit.color_sub.adjust_sub.frames),retry))
                w,h = self.driver.get_window_size().values()
                self.driver.swipe( w*0.5, h*0.8, w*0.5, h*0.5)
                retry -= 1
        
        self.driver.implicitly_wait(implicitly_previous)
        return
    def set_slider(self, slider, percentage):
        start_x = slider.location["x"]
        start_y = slider.location["y"]
        end_y = start_y + (percentage * slider.size["height"])  # slider is vertical in new UI
        actions = TouchAction(self.driver)
        actions.press(x=start_x,y= start_y) \
        .wait(ms=100) \
        .move_to(x=start_x, y=end_y) \
        .release().perform()
    def set_number(self,number):
        logger("set_number : %s" % number)
        self.update()
        self.elem_number.click()
        self.elem_number.send_keys(str(number))
        time.sleep(1)
        self.driver.back()
    def set_progress(self,percentage):
        logger("set_progress : %s" % percentage)
        self.update()
        self.elem_progress.set_text(percentage*self.max)
    def get_number(self):
        self.update()
        return self.elem_number.text
    def get_progress(self):
        self.update()
        return self.elem_progress.text
    def is_number(self,number):
        self.update()
        logger("%s / %s / %s"  % (number,self.elem_number.text,float(self.elem_number.text) == number))
        return float(self.elem_number.text) == number
    def is_progress(self,percentage):
        self.update()
        logger("%s / %s / %s"  % ((percentage*self.max),self.elem_progress.text,float(self.elem_progress.text) == (percentage*self.max)))
        return float(self.elem_progress.text) == (percentage*self.max)


class Audio_Denoise_Sub_item(Sub_item):
    def __init__(self, driver, item, item_max):
        super(Audio_Denoise_Sub_item, self).__init__(driver, item)
        self.max = item_max

class Audio_Denoise():
    def __init__(self,driver):
        self.el = lambda id: driver.find_element(id[0], id[1])
        self.els = lambda id: driver.find_elements(id[0], id[1])
        self.driver = driver
        self.strength = Audio_Denoise_Sub_item(driver,"Strength", 100)

    def get_strength_value(self):
        try:
            element = self.el(L.edit.audio_denoise.denoise_value)
            logger(f'value = {element.text}')
            return element.text 
        except Exception:
            logger("exception occurs")
            raise Exception
    
    def set_slider(self, percentage):
        try:
            slider = self.el(L.edit.audio_denoise.slider)
            start_x = slider.location["x"]
            start_y = slider.location["y"]
            end_y = start_y + (percentage * slider.size["height"])  # slider is vertical in new UI
            actions = TouchAction(self.driver)
            actions.press(x=start_x,y= start_y) \
            .wait(ms=100) \
            .move_to(x=start_x, y=end_y) \
            .release().perform()
        except Exception:
            logger("exception occurs")
            raise Exception
        
class Different_fx_Sub_item(Sub_item):
    def __init__(self, driver, item, item_max):
        super(Different_fx_Sub_item, self).__init__(driver, item)
        self.max = item_max

class Sharpness_Sub_item(Sub_item):
    def __init__(self, driver, item, item_max):
        super(Sharpness_Sub_item, self).__init__(driver, item)
        self.max = item_max
        
class Opacity_Sub_item(Sub_item):
    def __init__(self, driver, item, item_max):
        super(Opacity_Sub_item, self).__init__(driver, item)
        self.max = item_max

class ChromaKey_Sub_item(Sub_item):
    def __init__(self, driver, item, item_max):
        super(ChromaKey_Sub_item, self).__init__(driver, item)
        self.max = item_max

    def is_enabled(self):
        self.update()
        return True if self.elem_number.get_attribute('enabled') == 'true' else False

class Color():
    def __init__(self,driver):
        class Adjust():
            def __init__(self,driver):
                self.brightness = Sub_item(driver,"Brightness")
                self.contrast = Sub_item(driver,"Contrast")
                self.saturation = Sub_item(driver,"Saturation")
                self.hue = Sub_item(driver,"Hue")
        class White_balance():
            def __init__(self,driver):
                self.color_temperature = Sub_item(driver,"Color Temperature")
                self.tint = Sub_item(driver,"Tint")
        self.adjust = Adjust(driver)
        self.white_balance = White_balance(driver)

class Color_Selector():
    def __init__(self, driver):
        self.el = lambda id: driver.find_element(id[0], id[1])
        self.els = lambda id: driver.find_elements(id[0], id[1])
        self.driver = driver

    def set_red_number(self, number):
        logger("start >> set_red_number <<")
        logger(f"number={number}")
        try:
            el = self.el(L.edit.color_selector.red_number)
            el.set_text(str(number))
            time.sleep(2)
            if not el.text == str(number):
                logger("red_number set FAIL.")
                raise Exception
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_green_number(self, number):
        logger("start >> set_green_number <<")
        logger(f"number={number}")
        try:
            el = self.el(L.edit.color_selector.green_number)
            el.set_text(str(number))
            time.sleep(1)
            if not el.text == str(number):
                logger("red_number set FAIL.")
                raise Exception
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_blue_number(self, number):
        logger("start >> set_blue_number <<")
        logger(f"number={number}")
        try:
            el = self.el(L.edit.color_selector.blue_number)
            el.set_text(str(number))
            time.sleep(1)
            if not el.text == str(number):
                logger("red_number set FAIL.")
                raise Exception
        except Exception:
            logger("exception occurs")
            raise Exception
        return True
    
    def set_hue_slider(self, value):
        logger("start >> set_hue_slider <<")
        try:
            slider = self.el(L.edit.backdrop.hue_slider)
            slider.set_text(value)
        except Exception:
            logger("exception occurs")
            raise Exception
        return True      
    
    def set_saturation_slider(self, value):
        logger("start >> set_saturation_slider <<")
        try:
            slider = self.el(L.edit.backdrop.saturation_slider)
            slider.set_text(value)
        except Exception:
            logger("exception occurs")
            raise Exception
        return True    
        

class Skin_smoothener():
    def __init__(self,driver):
        self.skin_brightness = Sub_item(driver,"Skin Brightness")
        self.skin_smoothness = Sub_item(driver,"Skin Smoothness")

class Different_fx():
    def __init__(self,driver):
        self.beating_frequency = Different_fx_Sub_item(driver,"Frequency", 35)
        self.beating_strength = Different_fx_Sub_item(driver,"Strength", 40)
        self.bloom_sample_weight = Different_fx_Sub_item(driver,"Sample Weight", 200)
        self.bloom_light_number = Different_fx_Sub_item(driver,"Light Number", 2)
        self.bloom_angle = Different_fx_Sub_item(driver, "Angle", 200)
        self.black_and_white_degree = Different_fx_Sub_item(driver, "Degree", 200)

class Sharpness_effect():
    def __init__(self,driver):
        self.sharpness = Sharpness_Sub_item(driver,"Sharpness", 200)

class Chroma_Key():
    def __init__(self,driver):
        self.color_range = ChromaKey_Sub_item(driver,"Color Range", 200)
        self.denoise = ChromaKey_Sub_item(driver,"Denoise", 200)

class Opacity_effect():
    def __init__(self,driver):
        self.opacity = Opacity_Sub_item(driver,"Opacity", 100)
        
class Speed():
    def __init__(self, driver):
        self.el = lambda id: driver.find_element(id[0], id[1])
        self.els = lambda id: driver.find_elements(id[0], id[1])

    def set_slider(self, value):
        logger("start >> [Speed] set_slider] <<")
        try:
            slider = self.el(L.edit.speed.slider)
            slider.set_text(value)
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_ease_in(self, status="ON"):
        logger("start >> [Speed] set_ease_in] <<")
        logger(f"input={status}")
        try:
            element = self.el(L.edit.speed.ease_in)
            is_checked = element.get_attribute('selected')
            if (status == 'ON' and is_checked == 'false') or (status == 'OFF' and is_checked == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_ease_out(self, status="ON"):
        logger("start >> [Speed] set_ease_out] <<")
        logger(f"input={status}")
        try:
            element = self.el(L.edit.speed.ease_out)
            is_checked = element.get_attribute('selected')
            if (status == 'ON' and is_checked == 'false') or (status == 'OFF' and is_checked == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_mute_audio(self, status="ON"):
        logger("start >> [Speed] set_mute_audio] <<")
        logger(f"input={status}")
        try:
            element = self.el(L.edit.speed.mute_audio)
            is_checked = element.get_attribute('selected')
            if (status == 'ON' and is_checked == 'false') or (status == 'OFF' and is_checked == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def check_speed_toast_text(self, expect_value):
        logger("start >> [Speed] get_speed_toast_text] <<")
        try:
            element = self.el(L.edit.speed.preview_toast_text)
            toast_text = element.text
            logger(f"toast_text={toast_text}")
            if f'{expect_value}x' != toast_text:
                return False
        except Exception:
            logger("exception occurs")
            return False
        return True


class Title_Designer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_tab(self, name):
        logger(f"start select_tab - {name}")
        elm = self.el(L.edit.title_designer.tab_list)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(3):
            if self.is_exist(locator, 1):
                elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                logger(f"Found {name}, click it.")
                return True
            else:
                # elm.driver.swipe_left()
                self.swipe_element(L.edit.title_designer.tab_list, 'left', 300)
                time.sleep(1)
        logger(f"Didn't find {name}")
        return False

    def set_font_face(self, status='ON'):
        logger("start >> set_font_face <<")
        try:
            element = self.el(L.edit.title_designer.switch_font_face)
            is_checked = element.get_attribute('checked')
            if (status == 'ON' and is_checked == 'false') or (status == 'OFF' and is_checked == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_font_bold(self, status='ON'):
        logger("start >> set_font_bold <<")
        try:
            element = self.el(L.edit.title_designer.bold)
            is_selected = element.get_attribute('selected')
            if (status == 'ON' and is_selected == 'false') or (status == 'OFF' and is_selected == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_font_italic(self, status='ON'):
        logger("start >> set_font_italic <<")
        try:
            element = self.el(L.edit.title_designer.italic)
            is_selected = element.get_attribute('selected')
            if (status == 'ON' and is_selected == 'false') or (status == 'OFF' and is_selected == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_font_by_index(self, index=1, entry = 'designer'):
        logger("start >> set_font_by_index <<")
        logger(f'index={index}')
        try:
            if entry == 'designer':
                self.el(L.edit.title_designer.btn_font).click()
                time.sleep(5)
            
            elements = self.els(L.edit.title_designer.font_item)

            if len(elements) == 0:
                logger("list font fail")
                raise Exception
            logger(f"visible font in list={len(elements)}")
            elements[index].click()
        except Exception:
            logger("find element fail")
            raise Exception
        return True

    def set_custom_font_by_name(self, name, swipe_to_bottom='Yes'):
        logger("start >> set_custom_font_by_name <<")
        logger(f'name={name}')
        try:
            self.el(L.edit.title_designer.btn_font).click()
            time.sleep(5)
            #swipe list to bottom first
            if swipe_to_bottom == 'Yes':
                logger("swipe list to bottom")
                for times in range(70):
                    self.driver.swipe_element(L.edit.title_designer.font_list_body, 'up', 300)
            elements = self.els(L.edit.title_designer.font_list)
            if len(elements) == 0:
                logger("list font fail")
                raise Exception
            logger(f"usable font in list={len(elements)}")
            is_found = 0
            for el_font in elements:
                if el_font.text == name:
                    is_found = 1
                    el_font.click()
                    break
            if is_found == 0:
                logger("match font fail")
                raise Exception
        except Exception:
            raise Exception
        return True

    def select_font_by_name(self, name):
        logger("start >> select_font_by_name <<")
        logger(f'name={name}')
        try:
            elm = self.el(L.edit.title_designer.font_recyclerview)
            locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
            for retry in range(30):
                if self.is_exist(locator, 1):
                    elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                    logger(f"Found {name} font, click it.")
                    return True
                else:
                    self.driver.swipe_element(L.edit.title_designer.font_list_body, 'up', 300)
                    time.sleep(1)
            logger(f"Didn't find {name} font")
            return False
        except Exception:
            raise Exception

    def set_border(self, status='ON'):
        logger("start >> set_border <<")
        try:
            element = self.el(L.edit.title_designer.switch_border)
            is_checked = element.get_attribute('checked')
            if (status == 'ON' and is_checked == 'false') or (status == 'OFF' and is_checked == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_shadow(self, status='ON'):
        logger("start >> set_border <<")
        try:
            element = self.el(L.edit.title_designer.switch_shadow)
            is_checked = element.get_attribute('checked')
            if (status == 'ON' and is_checked == 'false') or (status == 'OFF' and is_checked == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_fill_shadow(self, status='ON'):
        logger("start >> set_border <<")
        try:
            element = self.el(L.edit.title_designer.switch_fill_shadow)
            is_checked = element.get_attribute('checked')
            if (status == 'ON' and is_checked == 'false') or (status == 'OFF' and is_checked == 'true'):
                element.click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True
        
    def download_font(self, timeout=120):
        logger("start >> download_font <<")
        # self.el(L.edit.title_designer.btn_font).click()
        # swipe list to bottom first
        for times in range(5):
            if self.is_exist(L.edit.title_designer.font_download_btn):
                break
            self.driver.swipe_element(L.edit.title_designer.font_list_body, 'up', 300)
        element = self.el(L.edit.title_designer.font_download_btn)
        element.click()
        
        is_complete = 0
        for retry in range(timeout-2):
            if not self.is_exist(L.edit.title_designer.font_download_btn, 1):
                is_complete = 1
                break
            time.sleep(1)
        if is_complete == 0:
            logger("download btn still exists. Timeout.")
            return False
        return True

    def download_premium_font(self):
        logger("start >> download_premium_font <<")
        # self.el(L.edit.title_designer.btn_font).click()
        for times in range(15):
            self.driver.swipe_element(L.edit.title_designer.font_list_body, 'up', 300)
            if self.is_exist(L.edit.title_designer.premium_font_icon):
                break
        element = self.el(L.edit.title_designer.premium_font_icon)
        element.click()
        time.sleep(5)
        return True

    def mgt_download_font(self, timeout=120):
        logger("start >> mgt_download_font <<")
        # swipe list to bottom first
        for times in range(15):
            self.driver.swipe_element(L.edit.motion_graphic_title.font_list_body, 'up', 300)
            if self.is_exist(L.edit.title_designer.font_download_btn):
                break
        element = self.el(L.edit.title_designer.font_download_btn)
        element.click()

        is_complete = 0
        for retry in range(timeout-2):
            if not self.is_exist(L.edit.title_designer.font_download_btn, 1):
                is_complete = 1
                break
            time.sleep(1)
        if is_complete == 0:
            logger("download btn still exists. Timeout.")
            return False
        return True

    def mgt_download_premium_font(self, timeout=120):
        logger("start >> mgt_download_premium_font <<")
        for times in range(15):
            self.driver.swipe_element(L.edit.motion_graphic_title.font_list_body, 'up', 300)
            if self.is_exist(L.edit.motion_graphic_title.premium_font_icon):
                break
        element = self.el(L.edit.motion_graphic_title.premium_font_icon)
        element.click()
        time.sleep(5)
        return True

    def select_color_by_order(self, index):
        logger(f'start select_color_by_order = {index}')
        try:
            elements = self.els(L.edit.title_designer.color_item)
            if len(elements) == 0:
                logger("list color fail")
                raise Exception
            logger(f"visible color in list={len(elements)}")
            elements[index].click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def select_color_palette_by_order(self, index):
        logger(f'start select_color_palette_by_order = {index}')
        try:
            elements = self.els(L.edit.title_designer.color_palette_item)
            if len(elements) == 0:
                logger("list color fail")
                raise Exception
            logger(f"visible color in list={len(elements)}")
            elements[index].click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def set_slider(self, slider, percentage):
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            frame = self.el(slider)
            elm = frame.find_element_by_xpath('(//*[contains(@resource-id,"seekbar")])')
            start_x = elm.location["x"]
            start_y = elm.location["y"]
            end_x = start_x + (percentage * elm.size["width"])
            actions = TouchAction(self.driver.driver)
            actions.press(x=start_x, y=start_y) \
                .wait(ms=100) \
                .move_to(x=end_x, y=start_y) \
                .release().perform()
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old, canvas_new, 8).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return is_changed

    def get_slider_value(self, slider):
        try:
            frame = self.el(slider)
            elm = frame.find_element_by_xpath('(//*[contains(@resource-id,"value")])')
            logger(f'value = {elm.text}')
            return elm.text
        except Exception:
            logger("exception occurs")
            raise Exception

    def set_hue_slider(self, percentage):
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            slider = self.el(L.edit.title_designer.colorpicker.slider_hue)
            start_x = slider.location["x"]
            start_y = slider.location["y"]
            end_y = start_y + (percentage * slider.size["height"])  # slider is vertical in new UI
            actions = TouchAction(self.driver.driver)
            actions.press(x=start_x, y=start_y).wait(ms=100).move_to(x=start_x, y=end_y).release().perform()
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old, canvas_new, 8).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return is_changed

    def tap_color_map(self, percentage_x, percentage_y):
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            elm = self.el(L.edit.title_designer.colorpicker.color_map)
            start_x = elm.location["x"]
            start_y = elm.location["y"]
            end_x = start_x + (percentage_x * elm.size["width"])
            end_y = start_y + (percentage_y * elm.size["height"])
            actions = TouchAction(self.driver.driver)
            actions.press(x=end_x, y=end_y).wait(ms=100).move_to(x=end_x, y=end_y).release().perform()
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old, canvas_new, 8).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return is_changed

    def select_color_dropper(self, percentage_x, percentage_y):
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            self.el(L.edit.title_designer.colorpicker.btn_dropper).click()
            time.sleep(3)
            elm = self.el(L.edit.preview.movie_view)
            start_x = elm.location["x"]
            start_y = elm.location["y"]
            end_x = start_x + (percentage_x * elm.size["width"])
            end_y = start_y + (percentage_y * elm.size["height"])
            actions = TouchAction(self.driver.driver)
            actions.press(x=1200, y=150).wait(ms=100).release().perform()
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old, canvas_new, 8).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return is_changed

    def set_RGB_number(self, target, number):
        logger(f"start >> set_RGB_number = {target} <<")
        logger(f"number={number}")
        try:
            if target == 'red':
                el = self.el(L.edit.title_designer.colorpicker.text_red)
            elif target == 'green':
                el = self.el(L.edit.title_designer.colorpicker.text_green)
            elif target == 'blue':
                el = self.el(L.edit.title_designer.colorpicker.text_blue)
            else:
                logger('target incorrect.')
                raise Exception
            el.set_text(str(number))
            time.sleep(2)
            if not el.text == str(number):
                logger("RGB_number set FAIL.")
                raise Exception
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def swipe_slider_area(self, direction):
        logger(f'start swipe_slider_area "{direction}"')
        self.swipe_element(L.edit.title_designer.title_slider_area, direction, 100)
        time.sleep(1)


class Pan_Zoom():
    def __init__(self, driver):
        self.el = lambda id: driver.find_element(id[0], id[1])
        self.els = lambda id: driver.find_elements(id[0], id[1])
        self.driver = driver

    def set_custom_motion(self):
        logger("start >> set_custom_motion <<")
        start_position = self.el(L.edit.pan_zoom_effect.custom_motion_start)
        end_position = self.el(L.edit.pan_zoom_effect.custom_motion_end)
        try:
            #set start position
            x_axis_center = int(start_position.rect['x'] + start_position.rect['width']/2)
            y_axis_center = int(start_position.rect['y'] + start_position.rect['height']/2)
            TouchAction(self.driver).press(None, x_axis_center, y_axis_center).wait(1000).move_to(None,
                                                                                                  x_axis_center + 200,
                                                                                                  y_axis_center).release().perform()
            #set end position
            x_axis_center = int(end_position.rect['x'] + end_position.rect['width'] / 2)
            y_axis_center = int(end_position.rect['y'] + end_position.rect['height'] / 2)
            TouchAction(self.driver).press(None, x_axis_center, y_axis_center).wait(1000).move_to(None,
                                                                                                  x_axis_center - 200,
                                                                                                  y_axis_center).release().perform()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

class Transition():
    def __init__(self, driver):
        self.el = lambda id: driver.find_element(id[0], id[1])
        self.els = lambda id: driver.find_elements(id[0], id[1])
        self.driver = driver

    def set_duration(self, expect_duration='2.0', apply_to_all=0):
        logger("start >> set_duration <<")
        logger(f"expect_duration={expect_duration}")
        try:
            # self.el(L.edit.transition.btn_show_transition_duration).click()
            txt_duration = self.el(L.timeline_settings.default_transition_duration.txt_duration).get_attribute('text')
            if txt_duration != f'{expect_duration} s':
                logger(f'enter set duration - current:{txt_duration}')
                el_slider = self.el(L.timeline_settings.default_transition_duration.slider)
                el_slider.set_text(str(float(expect_duration)*10-1))
                txt_duration = self.el(L.timeline_settings.default_transition_duration.txt_duration).get_attribute('text')
                if txt_duration != f'{expect_duration} s':
                    logger(f"Fail to set duration as {expect_duration} s, current duration is {txt_duration}")
                    raise Exception
            if (apply_to_all == 1 and self.el(L.edit.transition.apply_to_all).get_attribute(
                    'checked') == 'false') or (
                    apply_to_all == 0 and self.el(L.edit.transition.apply_to_all).get_attribute(
                    'checked') == 'true'):
                logger("enable apply to all")
                self.el(L.edit.transition.apply_to_all).click()
            # self.el(L.timeline_settings.default_transition_duration.ok).click()
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True

class Fade():
    def __init__(self, driver):
        self.el = lambda id: driver.find_element(id[0], id[1])
        self.els = lambda id: driver.find_elements(id[0], id[1])
        self.driver = driver

    def set_fade_in(self, value='ON'):
        logger("start >> set_fade_in <<")
        logger(f"input value={value}")
        try:
            if ((value == 'ON') and (self.el(L.edit.fade.fade_in).get_attribute('checked') == 'false')) or (
                    (value == 'OFF') and (self.el(L.edit.fade.fade_in).get_attribute('checked') == 'true')):
                self.el(L.edit.fade.fade_in).click()

            time.sleep(1)
            if ((value == 'ON') and (self.el(L.edit.fade.fade_in).get_attribute('checked') == 'false')) or (
                    (value == 'OFF') and (self.el(L.edit.fade.fade_in).get_attribute('checked') == 'true')):
                logger("set_fade_in FAIL.")
                raise Exception
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True

    def set_fade_out(self, value='ON'):
        logger("start >> set_fade_out <<")
        logger(f"input value={value}")
        try:
            if ((value == 'ON') and (self.el(L.edit.fade.fade_out).get_attribute('checked') == 'false')) or (
                    (value == 'OFF') and (self.el(L.edit.fade.fade_out).get_attribute('checked') == 'true')):
                self.el(L.edit.fade.fade_out).click()

            time.sleep(1)
            if ((value == 'ON') and (self.el(L.edit.fade.fade_out).get_attribute('checked') == 'false')) or (
                    (value == 'OFF') and (self.el(L.edit.fade.fade_out).get_attribute('checked') == 'true')):
                logger("set_fade_out FAIL.")
                raise Exception
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True

class Settings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def swipe_to_option(self, option):
        logger("start >> swipe_to_option <<")
        logger(f"input value={option}")
        try:
            is_found = 0
            for retry in range(5):
                self.driver.swipe_element(L.edit.settings.scroll_view, 'up', 500)
                time.sleep(1)
                if self.is_exist(find_string(option), 2):
                    is_found = 1
                    break
            if is_found == 0:
                logger("Cannot found item")
                return False
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True

    def scroll_list(self, times):
        logger("start >> scroll_list <<")
        logger(f"input value={times}")
        try:
            for retry in range(times):
                self.driver.swipe_element(L.edit.settings.scroll_view, 'up', 300)
                time.sleep(1)
        except Exception:
            logger("Exception occurs")
            raise Exception
        return True

    def get_device_model(self):
        logger("start >> get_device_model <<")
        try:
            model = self.shell_typeII('adb shell getprop ro.product.model')
            logger(f"device_model={model}")
        except Exception:
            logger("Exception occurs")
            raise Exception
        return model

    def get_os_version(self):
        logger("start >> get_os_version <<")
        try:
            model = self.shell_typeII('adb shell getprop ro.build.version.release')
            logger(f"device_model={model}")
        except Exception:
            logger("Exception occurs")
            raise Exception
        return model
        
class Keyframe(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def get_transform_keyframe_value(self): # return x, y, scale, rotation
        logger("start >> check_transform_keyframe_value <<")
        try:
            x = self.el(L.edit.keyframe.transform_keyframe.text_x).text
            y = self.el(L.edit.keyframe.transform_keyframe.text_y).text
            scale = self.el(L.edit.keyframe.transform_keyframe.text_scale).text
            rotation = self.el(L.edit.keyframe.transform_keyframe.text_rotation).text
            rotation = rotation[:-1]
            logger(f"get value: x={x}, y={y}, scale={scale}, rotation={rotation}")
        except Exception:
            logger("Exception occurs")
            raise Exception
        return x, y, scale, rotation
        
    def add_remove_keyframe(self):
        logger("start >> add_remove_keyframe <<")
        pic_old = self.driver.save_pic(self.el(L.edit.timeline.trim_indicator))
        self.click(L.edit.keyframe.btn_keyframe)
        time.sleep(3)    # to wait device to apply effect
        pic_new = self.driver.save_pic(self.el(L.edit.timeline.trim_indicator))       
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed
    
    def get_keyframe_pic(self):
        logger("start >> get_keyframe_pic <<")
        return self.driver.save_pic(self.el(L.edit.timeline.trim_indicator))
        
    def get_add_keyframe_btn_status(self):  # return False if button is grayed out
        logger("start >> get_add_keyframe_btn_status <<")
        if  self.el(L.edit.keyframe.btn_keyframe_img).get_attribute('enabled') == 'true':
            return True
        else:
            return False
    
    def longpress_keyframe(self, target = 'remove'):
        logger(f'start >> longpress_keyframe <<, target = {target}')
        el_keyframe = self.el(L.edit.keyframe.btn_keyframe)
        x_center = int(el_keyframe.rect['x'] + el_keyframe.rect['width']/2)
        y_center = int(el_keyframe.rect['y'] + el_keyframe.rect['height'] / 2)
        TouchAction(self.driver.driver).press(None, x_center, y_center).wait(2500).release().perform()
        time.sleep(1)
        if target == 'remove':
            locator = L.edit.keyframe.remove_all
        elif target == 'previous':
            locator = L.edit.keyframe.duplicate_previous
        elif target == 'next':
            locator = L.edit.keyframe.duplicate_next
        self.click(locator)

class Fit_and_Fill(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def apply_fit(self):
        logger(f"start apply_fit")
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            self.click(L.edit.fit_and_fill.btn_fit)
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger('apply_fit fail')
            raise Exception
        return is_changed

    def apply_fill(self):
        logger(f"start apply_fill")
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            self.click(L.edit.fit_and_fill.btn_fill)
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger('apply_fill fail')
            raise Exception
        return is_changed
    
    def zoom_preview(self):
        logger(f"start zoom_preview")
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            self.driver.zoom(L.edit.preview.movie_view)
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger('zoom_preview fail')
            raise Exception
        return is_changed
    
    def enter_background(self):
        logger(f"start enter_background")
        try:
            self.click(L.edit.fit_and_fill.btn_background)
            time.sleep(5)
            if self.is_exist(L.edit.fit_and_fill.btn_none, 2):
                return True
            else: 
                return False
        except Exception:
            logger('enter_background fail')
            raise Exception

    def set_slider(self, percentage):
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            slider = self.el(L.edit.fit_and_fill.blur_slider)
            start_x = slider.location["x"]
            start_y = slider.location["y"]
            end_y = start_y + (percentage * slider.size["height"])  # slider is vertical in new UI
            actions = TouchAction(self.driver.driver)
            actions.press(x=start_x,y= start_y) \
            .wait(ms=100) \
            .move_to(x=start_x, y=end_y) \
            .release().perform()
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return is_changed
        
    def get_value(self):
        try:
            element = self.el(L.edit.fit_and_fill.blur_text)
            logger(f'value = {element.text}')
            return element.text 
        except Exception:
            logger("exception occurs")
            raise Exception

    def select_color_by_order(self, order, swipe_times=0):
        logger("start select_color_by_order")
        canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        for retry in range(int(swipe_times)):
            self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'left', 400)
            time.sleep(1)   
        frame = self.el(L.edit.edit_sub.bottom_edit_menu)
        element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"card_color")])[{order}]')
        element.click()
        time.sleep(5)
        canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    
    def select_color_by_colorpicker(self):
        logger("start select_color_by_colorpicker")
        canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        #elm = self.el(L.edit.edit_sub.bottom_edit_menu)
        #locator = L.edit.fit_and_fill.color_picker
        for retry in range(10):
            if  self.is_exist(L.edit.fit_and_fill.color_picker):
                self.el(L.edit.fit_and_fill.color_picker).click()
                break
            else:            
                self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'right', 400)
                time.sleep(1)   
        time.sleep(5)
        self.el(L.edit.preview.movie_view).click()
        time.sleep(5)
        canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed
    

    def select_pattern_by_order(self, order, swipe_times=0):
        logger("start select_pattern_by_order")
        canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        for retry in range(int(swipe_times)):
            self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'left', 400)
            time.sleep(1)   
        frame = self.el(L.edit.edit_sub.bottom_edit_menu)
        element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"pattern_layout")])[{order}]')
        element.click()
        time.sleep(10)
        canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed


class Replace(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_replace_trim_view(self):
        logger("start check_replace_trim_view")
        try:
            # Enter Trim View
            result_trim_page = self.is_exist(L.edit.replace.bottom_area)
            # Trim View Description
            result_trim_text = self.is_exist(L.edit.replace.drag_text)
            # Repalced Clip Duration
            result_duration = self.is_exist(L.edit.replace.duration_text)
            return result_trim_page, result_trim_text, result_duration
        except Exception:
            raise Exception
            
            
    def move_trim_area(self):
        logger('start move_trim_area')
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            # Move Trim Area
            self.swipe_element(L.edit.replace.trim_view, 'right', 400)
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
            return is_changed
        except Exception:
            raise Exception
            
    def seek_by_indicator(self):
        logger('start seek_by_indicator')
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            self.swipe_element(L.edit.replace.seek_bar, 'right', 400)
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
            return is_changed
        except Exception:
            raise Exception

    def move_trim_area_audio(self):
        logger('start move_trim_area_audio')
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.replace.trim_view))
            # Move Trim Area
            self.swipe_element(L.edit.replace.trim_view, 'right', 400)
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.replace.trim_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
            return is_changed
        except Exception:
            raise Exception

    def seek_by_indicator_audio(self):
        logger('start seek_by_indicator_audio')
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.replace.trim_view))
            self.swipe_element(L.edit.replace.seek_bar, 'right', 400)
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.replace.trim_view))
            compare_result = CompareImage(canvas_old,canvas_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
            return is_changed
        except Exception:
            raise Exception

    def get_indicator_pos(self):
        logger('start get_indicator_pos')
        try:
            if self.is_exist(L.edit.replace.seek_bar, 15):
                elm = self.el(L.edit.replace.seek_bar)
                logger(f'rect = {elm.rect}')
                return elm.rect['x']
            else:
                logger("indicator not exist")
                raise Exception
        except Exception:
            logger("exception occurs")
            raise Exception

class Duration(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def set_duration_slider(self, percentage):
        try:
            slider = self.el(L.edit.duration.slider)
            start_x = slider.location["x"]
            start_y = slider.location["y"]
            end_x = start_x + (percentage * slider.size["width"]) 
            actions = TouchAction(self.driver.driver)
            actions.press(x=start_x,y= start_y) \
            .wait(ms=100) \
            .move_to(x=end_x, y=start_y) \
            .release().perform()
            time.sleep(5)
        except Exception:
            logger("exception occurs")
            raise Exception

    def get_duration_text(self):
        try:
            element = self.el(L.edit.duration.text_duration)
            logger(f'get_duration_text = {element.text}')
            return element.text 
        except Exception:
            logger("exception occurs")
            raise Exception


class Border_and_Shadow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_slider(self, target, percentage):
        try:
            canvas_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            if target == 'border_size':
                locator = L.edit.border_and_shadow.border_size
            elif target == 'border_opacity':
                locator = L.edit.border_and_shadow.border_opacity
            elif target == 'shadow_blur':
                self.swipe_element(L.edit.border_and_shadow.slider_area, 'up', 50)
                locator = L.edit.border_and_shadow.shadow_blur
            elif target == 'shadow_opacity':
                locator = L.edit.border_and_shadow.shadow_opacity
            elif target == 'shadow_angle':
                self.swipe_element(L.edit.border_and_shadow.slider_area, 'down', 50)
                locator = L.edit.border_and_shadow.shadow_angle
            elif target == 'shadow_distance':
                locator = L.edit.border_and_shadow.shadow_distance
            else:
                logger('parameter wrong')
                return False
            elem = self.el(locator)
            slider = elem.find_element_by_xpath("//android.widget.SeekBar[contains(@resource-id,'seekbar')]")
            start_x = slider.location["x"]
            start_y = slider.location["y"]
            end_x = start_x + (percentage * slider.size["width"])  # slider is vertical in new UI
            actions = TouchAction(self.driver.driver)
            actions.press(x=start_x, y=start_y).wait(ms=100).move_to(x=end_x, y=start_y).release().perform()
            time.sleep(5)
            canvas_new = self.driver.save_pic(self.el(L.edit.preview.movie_view))
            compare_result = CompareImage(canvas_old, canvas_new, 7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return is_changed

    def get_value(self, target):
        try:
            if target == 'border_size':
                locator = L.edit.border_and_shadow.border_size
            elif target == 'border_opacity':
                locator = L.edit.border_and_shadow.border_opacity
            elif target == 'shadow_blur':
                self.swipe_element(L.edit.border_and_shadow.slider_area, 'up', 50)
                locator = L.edit.border_and_shadow.shadow_blur
            elif target == 'shadow_opacity':
                locator = L.edit.border_and_shadow.shadow_opacity
            elif target == 'shadow_angle':
                self.swipe_element(L.edit.border_and_shadow.slider_area, 'down', 50)
                locator = L.edit.border_and_shadow.shadow_angle
            elif target == 'shadow_distance':
                locator = L.edit.border_and_shadow.shadow_distance
            else:
                logger('parameter wrong')
                return False
            elem = self.el(locator)
            value = elem.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'value')]").text
            logger(f'get_value = {value}')
            return value
        except Exception:
            logger("exception occurs")
            raise Exception

    def select_color_by_order(self, index):
        logger(f'start select_color_by_order = {index}')
        try:
            elements = self.els(L.edit.border_and_shadow.color_item)
            if len(elements) == 0:
                logger("list color fail")
                raise Exception
            logger(f"visible color in list={len(elements)}")
            elements[index].click()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def tap_border_reset(self):
        logger(f'start tap_border_reset')
        try:
            self.el(L.edit.border_and_shadow.btn_reset).click()
            time.sleep(5)
            result_color = True if self.el(L.edit.border_and_shadow.slider_area).get_attribute('enabled') == 'false' else False
            result_size = True if self.get_value('border_size') == '3.0' else False
            result_opacity = True if self.get_value('border_opacity') == '100' else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return result_color, result_size, result_opacity
   
    def tap_shadow_reset(self):
        logger(f'start tap_shadow_reset')
        try:
            self.el(L.edit.border_and_shadow.btn_reset).click()
            time.sleep(5)
            result_color = True if self.el(L.edit.border_and_shadow.slider_area).get_attribute('enabled') == 'false' else False
            result_blur = True if self.get_value('shadow_blur') == '5.0' else False
            result_opacity = True if self.get_value('shadow_opacity') == '100' else False
        except Exception:
            logger("exception occurs")
            raise Exception
        return result_color, result_blur, result_opacity

class Intro_Video(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def enter_intro(self, timeout=15):
        try:
            self.h_click(L.edit.intro_video.intro_video_entry)
            if self.h_is_exist(L.edit.intro_video.top_toolbar_back):
                logger("\n[Done] Enter Intro")
                return True
            else:
                logger("\n[Fail] Enter Intro Fail")
                return False
        except Exception as err:
            logger(f"\n[Error] enter_intro\n{err}")
            return False

    def enter_intro_video_library(self, timeout=10):
        logger(f'start enter_intro_video_library')
        try:
            self.el(L.edit.intro_video.intro_video_entry).click()
            time.sleep(3)
            for retry in range(timeout):
                if self.is_exist(L.edit.intro_video.loading_icon, 6):
                    time.sleep(6)
                else:
                    break
            if self.is_exist(L.edit.intro_video.list_template):
                logger('Load complete.')
                return True
            else:
                logger('Loading timeout.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception        
    
    def enter_intro_video_designer(self, timeout=10):
        logger(f'start enter_intro_video_designer')
        try:
            self.el(L.edit.intro_video.edit_in_designer).click()
            time.sleep(10)
            for retry in range(timeout):
                if self.is_exist(L.edit.intro_video.loading_designer, 6):
                    time.sleep(6)
                elif self.is_exist(L.edit.intro_video.btn_save_menu):
                    break
                else:
                    time.sleep(6)
            if self.is_exist(L.edit.intro_video.list_libraryEntry):
                logger('Load complete.')
                return True
            else:
                logger('Loading timeout.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception     
    
    def apply_to_project(self, timeout=10):
        logger(f'start apply_to_project')
        try:
            self.el(L.edit.intro_video.btn_save_menu).click()
            time.sleep(3)
            self.el(L.edit.intro_video.btn_apply_to_timeline).click()
            for retry in range(timeout):
                if self.is_exist(L.edit.intro_video.loading_designer, 6):
                    time.sleep(6)
                elif self.is_exist(L.edit.intro_video.intro_video_entry):
                    break
                else:
                    time.sleep(6)
            if self.is_exist(L.edit.intro_video.intro_video_entry):
                logger('Add complete.')
                return True
            else:
                logger('Loading timeout.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception  
    
    def switch_tabs(self, tab='discover', timeout=10):
        logger(f'start switch_tabs')
        try:
            if tab == 'discover':
                self.el(L.edit.intro_video.tab_discover).click()
            else:
                self.el(L.edit.intro_video.tab_cyberlink).click()
            time.sleep(3)
            for retry in range(timeout):
                if self.is_exist(L.edit.intro_video.loading_icon, 6):
                    time.sleep(6)
                else:
                    break
            if self.is_exist(L.edit.intro_video.list_template):
                logger('Load complete.')
                return True
            else:
                logger('Loading timeout.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception
            
    def compare_thumbnail_to_get_order(self, target_image):
        logger('start compare_thumbnail_to_get_order')
        try:
            thumbnails = self.els(L.edit.intro_video.template_thumbnail)
            logger(f'Get {len(thumbnails)} items')
            i = 0
            for retry in range(len(thumbnails)):
                compare_base = self.driver.save_pic(thumbnails[i])
                i = i+1
                if CompareImage(target_image, compare_base, 4).compare_image():
                    logger(f'Found image at index {i}')
                    return i
            logger('Not Found.')
            return False
        except Exception:
            logger(f"Fail to compare_thumbnail_to_get_order")
            raise Exception 
    
    def save_thumbnail_image_by_index(self, index):
        logger('start save_thumbnail_image_by_index')
        try:
            thumbnails = self.els(L.edit.intro_video.template_thumbnail)
            logger(f'Get {len(thumbnails)} items')
            if index > len(thumbnails):
                logger(f"items are less than index.")
                return False
            else:
                return self.driver.save_pic(thumbnails[index-1])    # start from 0, so -1
        except Exception:
            logger(f"Fail to save_thumbnail_image_by_index")
            return False
    
    def get_template_list_pic(self):
        logger('start get_template_list_pic')
        try:
            pic = self.el(L.edit.intro_video.list_template)
            return self.driver.save_pic(pic)
        except Exception:
            logger(f"Fail to get_template_list_pic")
            raise Exception 
    
    def select_template_by_index(self, index, timeout=10):
        logger("start >> select_template_by_index<<")
        logger(f"input - {index}")
        try:
            thumbnails = self.els(L.edit.intro_video.template_thumbnail)
            logger(f'Get {len(thumbnails)} items')
            if index > len(thumbnails):
                logger(f"items are less than index.")
                return False
            if self.is_exist(L.edit.intro_video.list_template, timeout):
                frame = self.el(L.edit.intro_video.list_template)
                element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"video_template_thumbnail")])[{index}]')
                element.click()
            else:
                logger(f"Fail to locate library")
                return False
            return True
        except Exception:
            logger(f"Fail to select - {index}")
            return False
        
    def select_category(self, name):
        logger(f"start select_category - {name}")
        elm = self.el(L.edit.intro_video.list_category)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(10):
            if  self.is_exist(locator, 1):
                elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                logger(f"Found {name}, click it.") 
                return True
            else:
                #elm.driver.swipe_left()
                self.swipe_element(L.edit.intro_video.list_category, 'left', 300)
                time.sleep(1)
        logger(f"Didn't find {name}")
        return False        
    
    def scroll_template_list(self, page=1):
        logger(f"start scroll_template_list")
        elm = self.el(L.edit.intro_video.list_template)
        for retry in range(page):
            # compare_base = self.driver.save_pic(L.edit.intro_video.list_template)
            self.swipe_element(L.edit.intro_video.list_template, 'up', 300)
            self.swipe_element(L.edit.intro_video.list_template, 'up', 300)
            self.swipe_element(L.edit.intro_video.list_template, 'up', 300)
            self.swipe_element(L.edit.intro_video.list_template, 'up', 300)
            self.swipe_element(L.edit.intro_video.list_template, 'up', 150)
            time.sleep(1)
        # compare_after = self.driver.save_pic(L.edit.intro_video.list_template)
        # if CompareImage(compare_base, compare_after, 4).compare_image():
        #     logger(f'Compare result is same, scroll to the end.')
        #     return False
        # else:
        #     return True
        return True

    def move_pic(self, target_image, category, result):
        pass_path = f"{os.path.abspath(dirname(dirname(__file__)))}\\TemplateScan\\temp\\PASS\\{category}\\"
        fail_path = f"{os.path.abspath(dirname(dirname(__file__)))}\\TemplateScan\\temp\\FAIL\\{category}\\"
        if result == True:
            logger('move_pic to Pass folder')
            os.makedirs(pass_path, exist_ok=True)
            shutil.copy(target_image, pass_path)
        else:
            logger('move_pic to Fail folder')
            os.makedirs(fail_path, exist_ok=True)
            shutil.copy(target_image, fail_path)

    def select_library_entry(self, name):
        logger("start select_library_entry")
        if self.is_exist(L.edit.intro_video.libraryEntryList):
            logger('Menu is exist.')
        else:
            logger('Menu not exist.')
            return False
        elm = self.el(L.edit.intro_video.libraryEntryList)
        elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
        logger(f"Found {name} function, click it.")
        return True

    def tap_back_button(self, target='no'):
        logger("start tap_back_button")
        try:
            self.el(L.edit.menu.back).click()
            if target == 'no':
                self.el(L.edit.intro_video.btn_no).click()
            else:
                self.el(L.edit.intro_video.btn_leave).click()

            if self.is_exist(L.edit.intro_video.list_template, 15):
                logger('Load template list complete.')
                return True
            else:
                logger('Loading timeout.')
                return False
        except Exception:
            logger(f"Fail to tap_back_button")
            raise Exception

class EditPage(BasePage):
    def __init__(self, *args, **kwargs):
        BasePage.__init__(self, *args, **kwargs)
        self.el = lambda id: self.driver.driver.find_element(id[0], id[1])
        self.els = lambda id: self.driver.driver.find_elements(id[0], id[1])
        self.color = Color(self.driver.driver)
        self.skin_smoothener = Skin_smoothener(self.driver.driver)
        self.speed = Speed(self.driver.driver)
        self.title_designer = Title_Designer(self.driver)
        self.different_fx = Different_fx(self.driver.driver)
        self.sharpness_effect = Sharpness_effect(self.driver.driver)
        self.pan_zoom = Pan_Zoom(self.driver.driver)
        self.transition = Transition(self.driver.driver)
        self.fade = Fade(self.driver.driver)
        self.chroma_key = Chroma_Key(self.driver.driver)
        self.color_selector = Color_Selector(self.driver.driver)
        self.settings = Settings(self.driver)
        self.opacity_effect = Opacity_effect(self.driver)
        self.keyframe = Keyframe(self.driver)
        self.audio_denoise = Audio_Denoise(self.driver.driver)
        self.fit_and_fill = Fit_and_Fill(self.driver)
        self.replace = Replace(self.driver)
        self.duration = Duration(self.driver)
        self.border_and_shadow = Border_and_Shadow(self.driver)
        self.intro_video = Intro_Video(self.driver)

    def timeline_swipe(self, direction, distance):
        logger(f"start timeline_swipe to {direction} with {distance}")
        self.swipe_element(L.edit.timeline.playhead_timecode, direction, distance)
        time.sleep(1)

    def timeline_get_photo_width(self, file_name):
        logger("start >> timeline_check_media <<")
        logger(f"input - {file_name}")
        # noinspection PyBroadException
        try:
            logger(f"media_aid=[AID]TimeLinePhoto_{file_name}")
            el_width = self.get_element(aid(f'[AID]TimeLinePhoto_{file_name}')).rect['width']
            logger(f"element width={el_width}")
        except Exception:
            logger('get elements fail')
            raise Exception
        return el_width

    def timeline_get_video_width(self, file_name):
        logger("start >> timeline_check_media <<")
        logger(f"input - {file_name}")
        # noinspection PyBroadException
        try:
            logger(f"media_aid=[AID]TimeLineVideo_{file_name}")
            el_width = self.get_element(aid(f'[AID]TimeLineVideo_{file_name}')).rect['width']
            logger(f"element width={el_width}")
        except Exception:
            logger('get elements fail')
            raise Exception
        return el_width

    def timeline_select_item_on_track(self, name, track=1, type=''):  # type=Video/ Photo/Music
        logger("start >> timeline_select_media <<")
        logger(f"input - name:{name}, track={track}, type={type}")
        # noinspection PyBroadException
        try:
            els_track = self.els(L.edit.timeline.track_content)
            logger(f'els_track count={len(els_track)}')
            if type == 'Video' or type == 'Photo':
                logger(f"media_aid=[AID]TimeLine{type}_{name}")
                locator = aid(f'[AID]TimeLine{type}_{name}')
                # self.get_element(aid(f'[AID]TimeLine{type}_{file_name}')).click()
                # els_track[track-1].get_element(aid(f'[AID]TimeLine{type}_{name}')).click()
                self.el(locator).click()
            else:
                list_element = els_track[track-1].find_elements_by_id(PACKAGE_NAME+':id/item_view_title')
                logger(f'list_element count={len(list_element)}')
                is_found = 0
                for element in list_element:
                    if element.get_attribute('text') == name:
                        element.click()
                        is_found = 1
                        break
                if is_found == 0:
                    logger('match element fail')
                    raise Exception
        except Exception:
            logger('get elements fail')
            raise Exception
        return True

    def timeline_select_audio(self, name):
        logger("start >> timeline_select_audio <<")
        logger(f"input - name:{name}")
        try:
            locator = aid(f'[AID]TimeLineAudio_{name}')
            self.el(locator).click()
        except Exception:
            logger('get elements fail')
            raise Exception
        return True

    def timeline_select_item_by_index_on_track(self, track=1, index=1):  # main track=1
        logger("start >> timeline_select_item_by_index_on_track <<")
        logger(f"input - track={track}, index={index}")
        # noinspection PyBroadException
        try:
            els_track = self.els(L.edit.timeline.track_content)
            logger(f"track count={len(els_track)}")
            els_item = els_track[track-1].find_elements_by_id(PACKAGE_NAME+':id/item_view_thumbnail_host')
            logger(f"elements on track{track}={len(els_item)}")
            els_item[index-1].click()
        except Exception:
            logger('get elements fail')
            raise Exception
        return True

    def timeline_get_item_by_index_on_track(self, track=1, index=1, id_type='thumbnail_host'): #main track=1, id_type='thumbnail_host'/ 'title'
        logger("start >> timeline_get_item_by_index_on_track <<")
        logger(f"input - track={track}, index={index}, id_type={id_type}")
        # noinspection PyBroadException
        try:
            els_track = self.els(L.edit.timeline.track_content)
            logger(f"track count={len(els_track)}")
            els_item = els_track[track-1].find_elements_by_id(PACKAGE_NAME+f':id/item_view_{id_type}')
            logger(f"elements on track{track}={len(els_item)}")
        except Exception:
            logger('get elements fail')
            raise Exception
        return els_item[index-1]

    def timeline_drag_item(self, el_target, shift_x=0): # shift_x > 0, drag to right; < 0, drag to left
        logger("start >> timeline_drag_item <<")
        logger(f"input - el_target={el_target}, shift_x={shift_x}")
        try:
            x_center = int(el_target.rect['x']+el_target.rect['width']/2)
            y_center = int(el_target.rect['y'] +el_target.rect['height']/2)
            TouchAction(self.driver.driver).long_press(None, x_center, y_center).wait(3).move_to(None, x_center+shift_x,
                                                                                     y_center).release().perform()
        except Exception:
            logger('Exception occurs')
            raise Exception
        return True

    def timeline_select_transition_effect(self, index=1):
        logger("start >> timeline_select_transition_effect <<")
        logger(f"input - index:{index}")
        try:
            els_transition = self.els(L.edit.transition.timeline_transition)
            logger(f'els_transition effect count={len(els_transition)}')
            els_transition[index-1].click()
        except Exception:
            logger('Exception occurs')
            raise Exception
        return True

    def timeline_get_transition_effect(self, index=1):
        logger("start >> timeline_get_transition_effect <<")
        logger(f"input - index:{index}")
        try:
            els_transition = self.els(L.edit.transition.timeline_transition)
            logger(f'els_transition effect count={len(els_transition)}')
        except Exception:
            logger('Exception occurs')
            raise Exception
        return els_transition[index-1]

    def timeline_check_item_on_track(self, name, track=1, type=''):
        logger("start >> timeline_select_media <<")
        logger(f"input - name:{name}, track={track}")
        # noinspection PyBroadException
        try:
            els_track = self.els(L.edit.timeline.track_content)
            logger(f'els_track count={len(els_track)}')
            if type == 'Video' or type == 'Photo':
                logger(f"media_aid=[AID]TimeLine{type}_{name}")
                # self.get_element(aid(f'[AID]TimeLine{type}_{file_name}')).click()
                els_track[track-1].get_element(aid(f'[AID]TimeLine{type}_{name}'))
            else:
                list_element = els_track[track-1].find_elements_by_id(PACKAGE_NAME + ':id/item_view_title')
                logger(f'list_element count={len(list_element)}')
                is_found = 0
                for element in list_element:
                    if element.get_attribute('text') == name:
                        # element.click()
                        is_found = 1
                        break
                if is_found == 0:
                    return False
        except Exception:
            logger('check element fail')
            return False
        return True

    def timeline_get_split_media(self, file_name, type='Video', index=0): # type=Video/ Photo/ Music
        logger("start >> timeline_get_split_media <<")
        logger(f"input - {file_name}")
        # noinspection PyBroadException
        element_list = []
        try:
            if type == 'Video' or type == 'Photo':
                logger(f"media_aid=[AID]TimeLine{type}_{file_name}")
                element_list = self.els(aid(f'[AID]TimeLine{type}_{file_name}'))
            else:
                list_el = self.els(("id", PACKAGE_NAME + ':id/item_view_title'))
                is_found = 0
                for element in list_el:
                    if element.get_attribute('text') == file_name:
                        element_list.append(element)
                        is_found = 1
                        break
                if is_found == 0:
                    logger('no match media')
                    raise Exception
        except Exception:
            logger('get elements fail')
            raise Exception
        return element_list[index]

    def force_uncheck_help_enable_tip_to_Leave(self, tap_x_shift=0, tap_y_shift=0, locator_verify=E.menu.timeline_setting, click=1):
        logger("start >> force_uncheck_help_enable_tip_to_Leave <<")
        try:
            if self.el(E.tips.chx_enable).get_attribute('checked') == 'true':
                time.sleep(0.5)
                self.el(E.tips.chx_enable).click()
                time.sleep(0.5)
            logger("uncheck help_enable_tip OK")
            for i in range(3):
                if i == 0:
                    for click_time in range(click):
                        self.tap_screen_center(tap_x_shift, tap_y_shift)
                        time.sleep(1)
                else:
                    self.tap_screen_center(tap_x_shift, tap_y_shift)
                logger("tap on screen")
                try:
                    self.el(locator_verify)
                    logger("help_enable_tip is gone")
                    break
                except:
                    logger("help_enable_tip exists")
                    #break
        except:
            logger("help_enable_tip is not found - skip it<<")
        return True

    def check_help_enable_tip_visible(self):
        logger("start >> check_help_enable_tip_visible <<")
        try:
            self.el(E.tips.chx_enable)
        except Exception:
            logger("help_enable_tip is not visible")
            return False
        return True

    def wait_for_stabilizing_complete(self):
        logger("start >> wait_for_stabilizing_complete <<")
        is_complete = 0
        for i in range(30):
            try:
                # self.el(E.stabilizer_correction.mask_button)
                self.el(E.opacity.slider)
                is_complete = 1
                break
            except Exception:
                pass
        if is_complete == 0:
            logger("Fail to correct clip. Timeout.")
            raise Exception
        return True

    def split_clip(self,locator):
        logger("start split_clip")
        thumbnail_old = self.driver.save_pic(self.el(locator),offset={"x":25,"y":30,"width":-25-40,"height":-30}) # for thumbnail compare
        # self.click(L.edit.menu.split)
        self.select_from_bottom_edit_menu('Split')
        playhead_rect = self.el(L.edit.timeline.playhead).rect
        playhead_middle = playhead_rect['x']+int(playhead_rect['width']/2)
        tx_ins = self.els(L.edit.timeline.tx_in)
        logger("playhead rect=" + str(playhead_rect))
        logger("tx_in rect=" + str(tx_ins[0].rect))
        
        thumbnail_new = self.driver.save_pic(last=True)
        is_change_thumbnail = not CompareImage(thumbnail_old,thumbnail_new,5).compare_image()
        for tx_in in tx_ins:
            if tx_in.rect['x'] - playhead_middle < 10: # magic number: normal gap between 2 clips
                return True , is_change_thumbnail
        return False , False

    def split_music(self,locator):
        logger("start split_music")
        # self.click(L.edit.menu.split)
        self.select_from_bottom_edit_menu('Split')
        playhead_rect = self.el(L.edit.timeline.playhead).rect
        playhead_middle = playhead_rect['x']+int(playhead_rect['width']/2)
        clips = self.els(L.edit.timeline.clip_audio)
        split_correct_position = False
        for clip in clips:
            logger('Playhead / clip.x = %s / %s' % (playhead_middle , clip.rect['x']))
            if clip.rect['x'] < playhead_middle: continue
            if clip.rect['x'] - playhead_middle < 10: # magic number: normal gap between 2 clips
                split_correct_position = True
                break
        has_thumbnail = bool(clips[1].find_elements_by_class_name("android.widget.ImageView"))
        return split_correct_position , has_thumbnail
        
    def _click_effect(self,locator):
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(locator)
        time.sleep(3)    # to wait device to apply effect
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed
        
    def click_rotate(self):
        logger("start click_rotate")
        return self.select_from_bottom_edit_menu('Rotate')
        
    def click_flip(self):
        logger("start click_flip")
        return self.select_from_bottom_edit_menu('Flip')
        
    def click_crop(self):
        logger("start click_crop")
        self.select_from_bottom_edit_menu('Crop')
        if  self.is_exist(L.edit.edit_sub.crop_hint):
            logger("hint pop, click to close it.")
            self.click(L.edit.edit_sub.crop_hint)
        self.exist_click(L.edit.show_timeline_pannel,3)     # v6.5 will close timeline pannel on Nexus 6P
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.pan_and_zoom_preview))
        time.sleep(1)
        self.driver.zoom(L.edit.preview.pan_and_zoom_preview)
        self.driver.zoom(L.edit.preview.pan_and_zoom_preview)
        time.sleep(5)    # to wait device to apply effect
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        self.click(L.edit.menu.back)
        return is_changed
        
    def click_reverse(self):
        logger("start click_reverse")
        self.select_from_bottom_edit_menu('Reverse')
        time.sleep(2)
        self.click(L.edit.reverse.dialog_ok)
        has_ad = self.is_in_page([L.edit.reverse.ad,L.edit.reverse.ad_promotion],30)
        if has_ad:
            logger("[reverse]AD found")
            self.is_not_in_page([L.edit.reverse.ad,L.edit.reverse.ad_promotion],3*60) #3min
            logger("[reverse]AD vanished")
        else:
            logger("[reverse]AD NOT found")
        # self.click(L.edit.menu.edit)
        # self.click(L.edit.edit_sub.reverse)
        self.select_from_bottom_edit_menu('Reverse')
        time.sleep(2)
        self.click(L.edit.reverse.dialog_ok)
        remove_success = self.is_exist(L.edit.edit_sub.bottom_edit_menu)
        return has_ad, remove_success        
    
    def click_reverse_noremove(self):
        logger("start click_reverse_noremove")
        self.select_from_bottom_edit_menu('Reverse')
        time.sleep(2)
        self.click(L.edit.reverse.dialog_ok)
        is_complete = 0
        for retry in range(100):
            if self.is_exist(L.edit.reverse.progress_bar):
                time.sleep(10)
            else:
                logger('Reverse procress done!')
                is_complete = 1
                break
        return is_complete
        
    def click_sharpness(self):
        logger("click_sharpness")
        # self.click(L.edit.edit_sub.sharpness)
        self.select_from_bottom_edit_menu('Adjustment')
        self.select_adjustment_from_bottom_edit_menu('Sharpness')
        sharpness_default_value = self.sharpness_effect.sharpness.get_number()
        result_default_value = sharpness_default_value == '0'
        logger ("sharpness_level=" + sharpness_default_value)
        return result_default_value
        
    def set_sharpness(self,value):
        logger("set_sharpness")
        # sharpness_level  = self.el(L.edit.sharpness.sharpness_level)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        # sharpness_level.set_text(value)
        self.sharpness_effect.sharpness.set_progress(value)
        time.sleep(1)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def click_stabilizer(self):
        logger("start click_stabilizer")
        # self.click(L.edit.edit_sub.stabilizer)
        self.select_from_bottom_edit_menu('Stabilizer')
        result_default_value = '0'
        has_ad = False
        has_iap = False
        if self.is_exist(L.edit.stabilizer.iap_back):
            logger("iap page pop")
            self.click(L.edit.stabilizer.iap_back)
            has_iap = True
        else:    
            has_ad = self.is_in_page([L.edit.reverse.ad,L.edit.reverse.ad_promotion],30)
            if has_ad:
                logger("[stabilizer]AD found")
                self.is_not_in_page([L.edit.reverse.ad,L.edit.reverse.ad_promotion],3*60) #3min
                logger("[stabilizer]AD vanished")
            else:
                logger("[stabilizer]AD *NOT* found")
            motion_level_vaule = self.el(L.edit.stabilizer.motion_level).text
            result_default_value = motion_level_vaule == "50.0"
            logger ("motion_level=" + motion_level_vaule)
        return result_default_value , has_ad , has_iap
        
    def click_stabilizer_wait(self):
        logger("start click_stabilizer_wait")
        self.select_from_bottom_edit_menu('Stabilizer')
        time.sleep(2)
        is_complete = 0
        for retry in range(100):
            if self.is_exist(L.edit.reverse.progress_bar):
                time.sleep(10)
            else:
                logger('Reverse procress done!')
                is_complete = 1
                break
        return is_complete
    
    def click_preview(self):
        logger("start click_preview")
        self.wait_tile_enabled(L.edit.menu.play)
        self.click(L.edit.menu.play)
        time.sleep(5)
        retry = 3
        while retry:
            try:
                pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
                break
            except:
                retry -= 1
                logger(f'snapshot fail, retry: {retry}')
        else:
            logger('unable to snapshot, return false directly')
            return False
        
        time.sleep(3)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def set_stabilizer(self,value):
        logger("start set_stabilizer")
        motion_level = self.el(L.edit.stabilizer.motion_level)
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        motion_level.set_text(value)
        time.sleep(1)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed
        
    def select_preset(self):
        logger("setart set preset")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(aid("[AID]ColorPresetThumbnail_3"))
        time.sleep(2)
        self.click(aid("[AID]ColorPresetThumbnail_8"))
        time.sleep(1)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old, pic_new, 7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding0(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending0)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old, pic_new, 7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding1(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending1)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding2(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending2)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding3(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending3)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding4(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending4)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding5(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending5)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding6(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending6)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding7(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending7)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding8(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending8)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding9(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending9)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_Blanding10(self):
        logger("setart set Blanding")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Blending_Sub.Blending10)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_mask_none(self):
        logger("setart set mask_none")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Mask_Sub.mask_none)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_mask_linear(self):
        logger("setart set mask_linear")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Mask_Sub.mask_linear)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_mask_parallel(self):
        logger("setart set mask_parallel")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Mask_Sub.mask_parallel)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_mask_eclipse(self):
        logger("setart set mask_eclipsel")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Mask_Sub.mask_eclipse)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed

    def select_mask_rectangle(self):
        logger("setart set mask_rectangle")
        time.sleep(1)
        pic_old = self.driver.save_pic(self.el(L.edit.preview.movie_view))
        self.click(L.edit.Mask_Sub.mask_rectangle)
        time.sleep(2)
        pic_new = self.driver.save_pic(last=True)
        compare_result = CompareImage(pic_old,pic_new,7).compare_image()
        is_changed = True if not compare_result or compare_result == 100 else False
        return is_changed


    def adjust_clip_length(self,locator,swipe_from,direction,pixel):
        logger("Adjust clip length")
        elem = self.el(locator)
        if not self.is_exist(L.edit.timeline.trim_indicator,3):
            elem.click()
        trim_indicator = self.el(L.edit.timeline.trim_indicator)
        buttons = trim_indicator.find_elements_by_xpath("//android.view.View")
        if len(buttons) == 2:
            if float(buttons[0].rect['x']) > float(buttons[1].rect['x']):
                button_end, button_start = buttons
            else:
                button_start, button_end = buttons

        elif len(buttons) == 1:
            logger("indicator.x= %s / button[0].x = %s" % (trim_indicator.rect['x'],buttons[0].rect['x']))
            is_start_button = True if trim_indicator.rect['x'] == buttons[0].rect['x'] else False
            if is_start_button:
                button_start, button_end = buttons[0], None
            else:
                button_start, button_end = None,buttons[0]
        else:
            raise Exception("Error when find start/end buttons")
        #logger("before - start_btn=%s , end_btn=%s" % (button_start.rect['x'],button_end.rect['x'] ) )
        length_org = elem.rect['width']
        logger("before - Length = %s" % length_org)
        from_where = button_end if swipe_from.lower() == "end" else button_start
        self.swipe_element_el_version(from_where,direction, pixel) #swipe
        time.sleep(1)
        logger("length diff = %s" % (elem.rect['width'] - length_org) )
        return elem.rect['width'] - length_org # length diff 

    def trim_video(self,locator):
        logger("start trim_video")
        elem = self.el(locator)
        result = self.adjust_clip_length(locator,"start","right",30)
        if result >= 0:  # video should be reduced
            logger(f"Error: swipe right 30 pixel, but only [{result}] pixel changed")
            return False ,None 
        result = self.adjust_clip_length(locator,"end","left",30)
        if result >= 0: # video should be reduced
            logger(f"Error: swipe Left 30 pixel, but only [{result}] pixel changed")
            return False , None
        has_thumbnail = elem.find_elements_by_xpath("//android.widget.LinearLayout[contains(@resource-id,'item_view_thumbnail_host')]")
        logger("thumbnail = %s" % has_thumbnail)
        return True , True if has_thumbnail else False

    def swipe_element_el_version(self, element, direction,offset=0.55):
        window_rect = self.driver.driver.get_window_size()
        element_rect = element.rect
        start_x = element_rect['x'] + element_rect['width'] / 2
        start_y = element_rect['y'] + element_rect['height'] / 2
        end_x = start_x
        end_y = start_y
        if direction == "left":
            end_x = start_x - ( window_rect['width'] * offset if offset < 1 else offset)
        elif direction == "right":
            end_x = start_x + ( window_rect['width'] * offset if offset < 1 else offset)
        elif direction == "up":
            end_y = start_y - ( window_rect['height'] * offset if offset < 1 else offset)
        elif direction == "down":
            end_y = start_y - ( window_rect['height'] * offset if offset < 1 else offset)
        else:
            print("Invalid direction")
            return False
        end_x = end_x if 0 <= end_x <=  window_rect['width'] else window_rect['width'] 
        end_y = end_y if 0 <= end_y <=  window_rect['height'] else window_rect['height']
        # print ("swip=",start_x, start_y, end_x, end_y)
        self.driver.driver.swipe(start_x, start_y, end_x, end_y)
        return True
        
    def check_timeline_gap(self,type = "Video"):
        logger("check [%s] gap" % type)
        media_type = {
        "video" : L.edit.timeline.clip,
        "photo" : L.edit.timeline.clip_photo,
        "audio" : L.edit.timeline.clip_audio
        }
        clip_all = self.els(media_type[type.lower()])
        found_error = False
        x_end_of_last_clip = clip_all[0].rect['x'] # for first clip only
        for clip in clip_all:
            logger("x_end_of_last_clip=" + str(x_end_of_last_clip))
            gap = clip.rect['x'] - x_end_of_last_clip
            logger("gap = %s" % str(gap))
            if gap < 14:   # magic number: normal gap between 2 clips
                x_end_of_last_clip = clip.rect['x'] + clip.rect['width']
            elif type.lower() == "audio": # audio & gap > 14 : pass directly
                logger("[check_timeline_gap] Audio - gap: %s (>14)" % str(gap))
                break
            else:                   # non-audio & gap > 14  : fail directly
                logger("[check_timeline_gap] Error Found.")
                found_error = True
                break
        return not found_error
    
    def check_if_trim_indicator_of_selected_clip(self):
        logger("start check_if_trim_indicator_of_selected_clip")
        try:
            trim_indicator = self.el(L.edit.timeline.trim_indicator)
            buttons = trim_indicator.find_elements_by_xpath("//android.view.View")
        except Exception:
            logger("exception occurs")
            return False
        if len(buttons) == 0:
            return False
        return True

    def check_preview_aspect_ratio(self, aspect_ratio): #aspect_ratio: 16_9/ 9_16/ 1_1
        logger("start check_preview_aspect_ratio")
        logger(f"aspect_ratio = {aspect_ratio}")
        is_pass = 0
        try:
            elem = self.el(L.edit.preview.movie_view)
            logger(f"rect = {elem.rect}")
            ratio = elem.rect['width']/elem.rect['height']
            logger(f"ratio = {ratio}")
            if aspect_ratio == '16_9':
                if ratio > 1:
                    is_pass = 1
            elif aspect_ratio == '9_16':
                if ratio < 1:
                    is_pass = 1
            elif aspect_ratio == '1_1':
                if ratio == 1:
                    is_pass = 1
            else:
                logger('invalid aspect ratio')
                raise Exception
        except Exception:
            logger("check aspect ratio FAIL")
            raise Exception
        if is_pass != 1:
            raise False
        return True

    def click_on_preview_area(self, x=0, y=0): #x, y: -1 ~ 1 (x=0, y=0 > center)
        logger("start check_preview_aspect_ratio")
        logger(f"x={x}, y={y}")
        try:
            elem = self.el(L.edit.preview.movie_view)
            logger(f"rect = {elem.rect}")
            x_center = elem.rect['x']+int(elem.rect['width']/2)
            y_center = elem.rect['y'] + int(elem.rect['height'] / 2)
            x_axis = x_center + int(elem.rect['width']/2*x)
            y_axis = y_center + int(elem.rect['height']/2*y)
            TouchAction(self.driver.driver).press(None, x_axis, y_axis, 1).release().perform()
        except Exception:
            logger('exception occurs')
            raise Exception
        return True

    def is_auto_save(self):
        from datetime import date
        
        logger("Start is_auto_save")
        logger("wait 2min")
        time.sleep(5)
        logger("killing app")
        retry = 3
        while retry > 0:
            logger("try: %s" %retry)
            try:
                result = self.driver.driver.terminate_app(PACKAGE_NAME)
                logger("Kill app success (app exist?): %s" % result)
                break
            except:
                time.sleep(2)
                retry -= 1
                logger("Kill app failed, try again: %s" % retry)
        logger("restart app")
        self.driver.driver.activate_app(PACKAGE_NAME)
        try:
            if  self.is_exist(L.edit.preview.movie_view):
                logger("Project is auto re-opened.")
                return True
            else:
                project_name = self.exist(L.main.project.txt_project_title,20).text
        except:
            logger("Project name is not found")
            return False
        today = date.today()
        expect_name = today.strftime("Project %m-%d")
        result = expect_name in project_name
        logger(f"project name = [{project_name}] / expect name = [{expect_name}] / {result}")
        return True if result else False

    def enter_fullscreen_preview(self):
        logger("start enter_fullscreen_preview")
        try:
            is_complete = 0
            for retry in range(5):
                if not self.is_exist(L.edit.preview.movie_view):
                    continue
                preview_rect = self.el(L.edit.preview.movie_view).rect
                logger(f"preview_rect = {preview_rect}")
                #x_axis = preview_rect['x'] + 30
                #y_axis = preview_rect['y'] + 30                
                x_axis = preview_rect['x'] + preview_rect['width']/2
                y_axis = preview_rect['y'] + 10
                TouchAction(self.driver.driver).tap(None, x_axis, y_axis, 3).perform()
                if not self.is_exist(L.edit.menu.import_media):
                    if self.is_not_exist(L.edit.preview.fullscreen_current_position, 10):
                        is_complete = 1
                        break
            if is_complete == 0:
                logger('Enter full screen preview FAIL. Retry 3 times.')
                raise Exception
        except Exception:
            logger('exception occurs')
            raise Exception
        return True    
        
    def search_text(self,text):
        logger("start text")
        found = False
        retry = 3
        while retry > 0:
            if text in self.driver.driver.page_source:
                found = True
                break
            else:
                self.driver.swipe_up()
            retry -= 1

    def calculate_library_content_amount(self):
        logger("start calculate_library_content_amount")
        try:
            caption_list = set()
            caption_list_count = len(caption_list)
            caption_list_count_prev = -1
            while caption_list_count != caption_list_count_prev:
                logger(f"Count Start - caption_list_count={caption_list_count}, caption_list_count_prev={caption_list_count_prev}")
                if caption_list_count_prev != -1:
                    self.driver.swipe_left()
                    time.sleep(1)
                caption_list_count_prev = caption_list_count
                els_item_list = self.els(L.import_media.library_gridview.caption_media)
                logger(f'current clips count={len(els_item_list)}')
                if len(els_item_list) > 0:
                    logger('enter update caption set')
                    for el_item in els_item_list:
                        caption_list.add(el_item.text)
                caption_list_count = len(caption_list)
                logger(f'caption set count={caption_list_count}')
        except Exception:
            logger('exception occurs')
            raise Exception
        logger(f'content amount={caption_list_count}')
        return caption_list_count
    
    def calculate_transition_amount(self):
        logger("start calculate_transition_amount")
        try:
            caption_list = set()
            caption_list_count = len(caption_list)
            caption_list_count_prev = -1
            while caption_list_count != caption_list_count_prev:
                logger(f"Count Start - caption_list_count={caption_list_count}, caption_list_count_prev={caption_list_count_prev}")
                if caption_list_count_prev != -1:
                    self.swipe_element(L.import_media.transition_list.transition_list, 'left', 300)
                    time.sleep(1)
                    self.swipe_element(L.import_media.transition_list.transition_list, 'left', 300)
                    time.sleep(1)
                caption_list_count_prev = caption_list_count
                els_item_list = self.els(L.import_media.transition_list.tx_name)
                logger(f'current clips count={len(els_item_list)}')
                if len(els_item_list) > 0:
                    logger('enter update caption set')
                    for el_item in els_item_list:
                        caption_list.add(el_item.text)
                caption_list_count = len(caption_list)
                logger(f'caption set count={caption_list_count}')
        except Exception:
            logger('exception occurs')
            raise Exception
        logger(f'content amount={caption_list_count}')
        return caption_list_count

    def calculate_music_library_content_amount(self):
        logger("start calculate_music_library_content_amount")
        try:
            caption_list = set()
            caption_list_count = len(caption_list)
            caption_list_count_prev = -1
            while caption_list_count != caption_list_count_prev:
                logger(f"Count Start - caption_list_count={caption_list_count}, caption_list_count_prev={caption_list_count_prev}")
                if caption_list_count_prev != -1:
                    #self.driver.swipe_up()
                    self.swipe_element(L.import_media.library_listview.frame, 'up', 400)
                    self.swipe_element(L.import_media.library_listview.frame, 'up', 250)
                    time.sleep(1)
                caption_list_count_prev = caption_list_count
                els_item_list = self.els(L.import_media.library_listview.caption_song)
                #logger(f'current clips count={len(els_item_list)}')
                if len(els_item_list) > 0:
                    #logger('enter update caption set')
                    for el_item in els_item_list:
                        caption_list.add(el_item.text)
                caption_list_count = len(caption_list)
                logger(f'caption set count={caption_list_count}')
        except Exception:
            logger('exception occurs')
            raise Exception
        logger(f'content amount={caption_list_count}')
        return caption_list_count

    '''
    def audio_mixing_set_volume(self, track_name, value): # track_name: main, pip_1, pip_2, music_1, music_2, #value = '0' - '100'
        logger(f"start audio_mixing_set_volume on {track_name}")
        track_dict = {'main': 0, 'pip_1': 1, 'pip_2': 2, 'music_1': 3, 'music_2': 4}
        try:
            if not track_name in track_dict:
                logger(f'Invalid track_name={track_name}')
                raise Exception
            #elsm = self.els(L.edit.audio_configuration.audio_mixing.edit_text)
            
            elsm = self.els(L.edit.audio_configuration.audio_mixing.volume_text)
            #if len(elsm) < 5:
            #    logger(f'incorrect track count as ={len(elsm)}')
            #    raise Exception

            if str(int(float(elsm[track_dict[track_name]].text))) != str(value):
                elsm[track_dict[track_name]].set_text(str(value))
        except Exception:
            logger('exception occurs')
            raise Exception
        return True
    '''
    def audio_mixing_set_volume(self, track_number, value): # track_name: main, pip_1, pip_2, music_1, music_2, #value = '0' - '100'
        logger(f"start audio_mixing_set_volume on Track{track_number}")
        try:
            elsm = self.els(L.edit.audio_configuration.audio_mixing.slider_volume)
            if str(int(float(elsm[track_number].text))) != str(value):
                elsm[track_number].set_text(str(value))
        except Exception:
            logger('exception occurs')
            raise Exception
        return True
    '''
    def audio_mixing_check_volume(self, track_name, value): # track_name: main, pip_1, pip_2, music_1, music_2, #value = '0' - '100'
        logger(f"start audio_mixing_check_volume on {track_name}")
        track_dict = {'main': 0, 'pip_1': 1, 'pip_2': 2, 'music_1': 3, 'music_2': 4}
        try:
            if not track_name in track_dict:
                logger(f'Invalid track_name={track_name}')
                raise Exception
            #elsm = self.els(L.edit.audio_configuration.audio_mixing.edit_text)
            elsm = self.els(L.edit.audio_configuration.audio_mixing.volume_text)
            
            #if len(elsm) < 5:
            #    logger(f'incorrect track count as ={len(elsm)}')
            #    raise False
            logger(f'result ={elsm[track_dict[track_name]].text}, expect is {str(value)}')
            if elsm[track_dict[track_name]].text != str(value):    
                return False
        except Exception:
            logger('exception occurs')
            raise False
        return True
    '''
    def audio_mixing_check_volume(self, track_number, value): # track_name: main, pip_1, pip_2, music_1, music_2, #value = '0' - '100'
        logger(f"start audio_mixing_check_volume on Track{track_number}")
        try:
            elsm = self.els(L.edit.audio_configuration.audio_mixing.volume_text)

            logger(f'result ={elsm[track_number].text}, expect is {str(value)}')
            if elsm[track_number].text != str(value):    
                return False
        except Exception:
            logger('exception occurs')
            raise False
        return True

    def audio_configration_set_clip_volume(self, value): #value = '0' - '200'
        logger("start audio_configration_set_clip_volume")
        try:
            elm = self.el(L.edit.audio_configuration.volume_seekbar)
            if str(int(float(elm.text))) != str(value):
                elm.set_text(str(value))
        except Exception:
            logger('exception occurs')
            raise Exception
        return True

    def audio_configration_check_clip_volume(self, value): #value = '0' - '200'
        logger("start audio_configration_check_clip_volume")
        try:
            elm = self.el(L.edit.audio_configuration.volume_seekbar)
            if str(int(float(elm.text))) != str(value):
                return False
        except Exception:
            logger('exception occurs')
            raise False
        return True

    def select_main_video(self,index):
        logger("start select main video")
        self.els(L.edit.timeline.clip)[index].click()

    def select_from_bottom_edit_menu(self, name, from_head=1):
        logger("start select_from_bottom_edit_menu")
        if self.is_exist(L.edit.edit_sub.bottom_edit_menu):
            logger('Edit menu is exist.')
        else:
            logger('Edit menu not exist, try click edit button')
            self.el(L.edit.menu.edit).click()
        if from_head == 1:
            for retry in range(7):
                self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'right', 400)
        elm = self.el(L.edit.edit_sub.bottom_edit_menu)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(10):
            if self.is_exist(locator, 1):
                elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                logger(f"Found {name} function, click it.") 
                return True
            else:
                #elm.driver.swipe_left()
                self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'left', 400)
                time.sleep(1)
        logger(f"Didn't find {name} element")        
        return False    
    
    def select_from_bottom_edit_menu_by_order(self, index):
        logger("start select_from_bottom_edit_menu_by_order")
        elm = self.el(L.edit.edit_sub.bottom_edit_menu)
        locator = ("xpath", f'//*[contains(@resource-id,"tool_entry_layout")][{index}]')
        for retry in range(10):
            if  self.is_exist(locator):
                elm.find_element_by_xpath(f'//*[contains(@resource-id,"tool_entry_layout")][{index}]').click()
                return True
            else:
                #elm.driver.swipe_left()
                self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'left', 400)
                time.sleep(1)     
        return False
    
    def select_transition_from_bottom_menu(self, name):
        logger(f"start select_transition_from_bottom_menu - {name}")
        elm = self.el(L.import_media.transition_list.transition_list)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(10):
            if  self.is_exist(locator):
                elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                logger(f"Found {name}, click it.") 
                return True
            else:
                #elm.driver.swipe_left()
                self.swipe_element(L.import_media.transition_list.transition_list, 'left', 300)
                time.sleep(1)
        logger(f"Didn't find {name}")        
        return False    
    
    def select_transition_category(self, name):
        logger(f"start select_transition_category - {name}")
        elm = self.el(L.import_media.transition_list.category_list)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(10):
            if  self.is_exist(locator):
                elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                logger(f"Found {name}, click it.") 
                return True
            else:
                #elm.driver.swipe_left()
                self.swipe_element(L.import_media.transition_list.category_list, 'left', 300)
                time.sleep(1)
        logger(f"Didn't find {name}")        
        return False
    
    def check_transition_exists_in_list(self, name):
        logger(f"start check_transition_exists_in_list - {name}")
        try:
            frame = self.el(L.import_media.transition_list.transition_list)
            element = frame.find_element_by_xpath(f'//*[contains(@text,"{name}")]')
        except Exception:
            logger("Fail to locate element")
            return False
        return True

    def swipe_bottom_edit_menu(self, direction='left'):
        logger(f"start swipe_bottom_edit_menu to {direction}")
        self.swipe_element(L.edit.edit_sub.bottom_edit_menu, direction, 300)
        time.sleep(1)
        
    def is_exist_in_bottom_edit_menu(self, name):
        logger("start is_exist_in_bottom_edit_menu")
        elm = self.el(L.edit.edit_sub.bottom_edit_menu)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(5):
            if self.is_exist(locator, 1):
                logger(f"Found {name} in bottom edit menu")
                return True
            else:
                self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'left', 300)
                time.sleep(1)
        logger(f"Didn't find {name} element")        
        return False    
    
    def select_adjustment_from_bottom_edit_menu(self, name):
        logger("start select_adjustment_from_bottom_edit_menu")
        elm = self.el(L.edit.edit_sub.adjustment_menu)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(5):
            if  self.is_exist(locator):
                elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                return True
            else:
                #elm.driver.swipe_left()
                self.swipe_element(L.edit.edit_sub.adjustment_menu, 'left', 300)
                time.sleep(1)
        logger(f"Didn't find {name} element")        
        return False    
        
    def select_effect_from_bottom_edit_menu(self, name):
        logger("start select_effect_from_bottom_edit_menu")
        elm = self.el(L.edit.edit_sub.effect_menu)
        locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
        for retry in range(5):
            if  self.is_exist(locator):
                elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                return True
            else:
                #elm.driver.swipe_left()
                self.swipe_element(L.edit.edit_sub.effect_menu, 'left', 300)
                time.sleep(1)
        logger(f"Didn't find {name} element")        
        return False     
        
    def opacity_set_slider(self, percentage): # percentage: 0~1  ex: 0.5
        logger("start opacity_set_slider")
        elem = self.el(L.edit.color_sub.adjust_sub.frames)
        slider = elem.find_element_by_xpath("//android.widget.SeekBar[contains(@resource-id,'adjustable_parameter_seek_bar')]")
        start_x = slider.location["x"] + (slider.size["width"]/2)
        start_y = slider.location["y"] + slider.size["height"]
        end_y = start_y - (percentage * slider.size["height"])
        logger(f"touch x={start_x}, y={end_y}")
        actions = TouchAction(self.driver.driver)
        actions.press(x=start_x,y= end_y).release().perform()   
        return True        
    
    def get_opacity_value(self):
        logger("start get_opacity_value")
        elem = self.el(L.edit.color_sub.adjust_sub.frames)
        value = elem.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'adjustTextNow')]").text
        logger(f"value={value}")
        return value
        
    def title_animation_get_duration(self):
        logger('start title_animation_get_duration')
        elm = self.el(L.edit.color_sub.adjust_sub.number)
        duration = str(float(elm.text))
        logger(f'duration = {duration}')
        return duration

    def get_motion_title_text_number(self):
        logger("start get_motion_title_text_number")
        try:
            caption_list = set()
            caption_list_count = len(caption_list)
            els_item_list = self.els(L.edit.motion_graphic_title.dropdownmenu_text)
            if len(els_item_list) > 0:
                for el_item in els_item_list:
                    caption_list.add(el_item.text)
            caption_list_count = len(caption_list)
            logger(f'caption set count={caption_list_count}')
        except Exception:
            logger('exception occurs')
            raise Exception
        logger(f'content amount={caption_list_count}')
        return caption_list_count    
        
    def mgt_set_font_by_name(self, name, swipe_to_bottom='Yes'):
        logger("start >> mgt_set_font_by_name <<")
        logger(f'name={name}')
        try:
            #swipe list to bottom first
            if swipe_to_bottom == 'Yes':
                logger("swipe list to bottom")
                for times in range(70):
                    self.driver.swipe_element(L.edit.motion_graphic_title.font_list_body, 'up', 300)
            else:
                logger("swipe list to top")
                for times in range(10):
                    self.driver.swipe_element(L.edit.motion_graphic_title.font_list_body, 'down', 300)
            time.sleep(5)
            elements = self.els(L.edit.motion_graphic_title.font_list)
            if len(elements) == 0:
                logger("list font fail")
                raise Exception
            logger(f"usable font in list={len(elements)}")
            is_found = 0
            for el_font in elements:
                if el_font.text == name:
                    is_found = 1
                    el_font.click()
                    break
            if is_found == 0:
                logger("match font fail")
                raise Exception
        except Exception:
            raise Exception
        return True
        
    def mgt_select_title_from_menu(self, index):
        logger(f"start >> mgt_select_title_from_menu <<, index = {index}")
        try:
            elements = self.els(L.edit.motion_graphic_title.dropdownmenu_text)
            if len(elements) == 0:
                logger("list text fail")
                raise Exception
            logger(f"visible text in list={len(elements)}")
            elements[index].click()
            for retry in range(5):
                if  self.is_exist(L.edit.edit_sub.bottom_edit_menu):
                    return True
                else:
                    logger("click fail, try again")
                    elements[index].click()
                    time.sleep(1)
        except Exception:
            logger("find element fail")
            raise Exception
        return True
        
    def import_video_select_got_it(self):
        logger("start >> import_video_select_got_it <<")
        try:
            #swipe list on dialog
            if self.is_exist(L.edit.tutorial_bubble.dialog):
                logger("Tips dialog exist, swipe left.")
                self.driver.swipe_left()
            time.sleep(3)
            self.el(L.edit.tutorial_bubble.dialog_got_it).click()
            if self.is_exist(L.edit.tutorial_bubble.dialog):
                return False
        except Exception:
            raise Exception
        return True
    
    def check_premium_features_used(self):
        logger("start >> check_premium_features_used <<")
        try:
            if self.is_exist(L.edit.try_before_buy.premium_features_used_bubble):
                logger("premium_features_used_bubble exist.")
                return True
            else:
                logger("premium_features_used_bubble is not exist.")
                return False
        except Exception:
            raise Exception
        return True
    
    def trying_premium_content(self, action='try'):
        logger("start >> trying_premium_content <<")
        try:
            if self.is_exist(L.edit.try_before_buy.btn_tryit):
                logger("trying_premium_content dialog exist.")
                if action == 'try':
                    logger('Click try button')
                    self.el(L.edit.try_before_buy.btn_tryit).click()
                elif action == 'sub':
                    logger('Click Sub to unlock button')
                    self.el(L.edit.try_before_buy.btn_subtounlock).click()
                else:
                    logger('Parameter wrong')
                    raise Exception
            else:
                logger("trying_premium_content dialog is not exist.")
                return False
        except Exception:
            raise Exception
        return True
    
    def check_bottom_edit_menu_select_status(self, name):
        logger("start check_bottom_edit_menu_select_status")
        try:
            if self.is_exist(L.edit.edit_sub.bottom_edit_menu):
                logger('Edit menu is exist.')
            else:
                logger('Edit menu not exist, try click edit button')
                self.el(L.edit.menu.edit).click()
        
            elm = self.el(L.edit.edit_sub.bottom_edit_menu)
            locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
            for retry in range(10):
                if  self.is_exist(locator):
                    result = elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').get_attribute('selected')
                    logger(f"Found {name} function = {result}") 
                    return result
                else:
                    #elm.driver.swipe_left()
                    self.swipe_element(L.edit.edit_sub.bottom_edit_menu, 'left', 400)
                    time.sleep(1)
            
            logger(f"Didn't find {name} element")   
            raise Exception
        except Exception:
            raise Exception

    def select_title_from_timeline(self, name):
        logger(f"start >> select_title_from_timeline <<, name = {name}")
        try:
            timeline = self.el(L.edit.timeline.overlaytrack_container)
            element = timeline.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]')
            element.click()
            return True
        except Exception:
            logger("find element fail")
            raise Exception

    def snapshot_bottom_menu(self):
        logger(f'start snapshot_bottom_menu')
        try:
            return self.driver.save_pic(self.el(L.edit.edit_sub.bottom_edit_menu))
        except Exception:
            logger("exception occurs")
            raise Exception
            
    def check_bottom_edit_menu_item_apply_status(self, name):
        logger(f'start check_edit_menu_item_is_applied = {name}')
        try:
            elm = self.el(L.edit.edit_sub.bottom_edit_menu)
            item = elm.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]/..')
            apply_icon = item.find_elements_by_xpath("//android.widget.ImageView[contains(@resource-id,'tool_entry_has_apply_icon')]")
            # logger(f'apply_icon = {apply_icon}')
            if apply_icon != []:
                logger('Found applied icon!')
                return True
            else:
                logger('Applied icon not found.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception

    def get_facilitate_usage_position(self):
        logger('start get_facilitate_usage_position')
        try:
            if self.is_exist(L.edit.timeline.btn_import, 15):
                elm = self.el(L.edit.timeline.btn_import)
                logger(f'rect = {elm.rect}')
                return elm.rect['x']
            elif self.is_exist(L.edit.timeline.btn_import2, 15):
                elm = self.el(L.edit.timeline.btn_import2)
                logger(f'rect = {elm.rect}')
                return elm.rect['x']
            else:
                logger("facilitate usage button not exist")
                raise Exception
        except Exception:
            logger("exception occurs")
            raise Exception
        
    def enter_library_from_facilitate_usage(self):
        logger('start enter_library_from_facilitate_usage')
        try:
            if self.is_exist(L.edit.timeline.btn_import, 15):
                self.el(L.edit.timeline.btn_import).click()
            elif self.is_exist(L.edit.timeline.btn_import2, 15):
                self.el(L.edit.timeline.btn_import2).click()
            if self.is_exist(L.import_media.menu.video_library):
                logger('Open library success.')
                return True
            else:
                logger('Open library failed.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception

    def pinch_timeline(self):
        logger('start pinch_timeline')
        try:
            self.driver.pinch_element(L.edit.timeline.track_of_ruler)
        except Exception:
            logger("exception occurs")
            raise Exception

    def drag_timeline_clip(self, direction='up'):
        logger(f'start drag_timeline_clip {direction}')
        try:
            if self.is_exist(L.edit.timeline.item_view_thumbnail_host, 15):
                element = self.el(L.edit.timeline.item_view_thumbnail_host)
            else:
                logger('element not exist')
                return False
            start_x = element.rect['x'] + element.rect['width'] / 2
            start_y = element.rect['y'] + element.rect['height'] / 2
            if direction == 'up':
                end_y = start_y - int(element.rect['height']*1.5)
            else:
                end_y = start_y + int(element.rect['height']*1.5)
            actions = TouchAction(self.driver.driver)
            actions.press(x=start_x, y=start_y).wait(ms=5000).move_to(x=start_x, y=end_y).release().perform()
            logger(f'drag from ({start_x}, {start_y}) to ({start_x}, {end_y})')
        except Exception:
            logger("exception occurs")
            raise Exception


    def close_full_screen_preview_tip(self):
        logger('start close_full_screen_preview_tip ')
        try:
            if self.is_exist(L.edit.preview.help_not_show_tip_again, 15):
                element = self.el(L.edit.preview.help_not_show_tip_again)
            else:
                logger('element not exist')
                return False
            element.click()
            self.el(L.edit.preview.btn_close).click()
            return True
        except Exception:
            logger("exception occurs")
            raise Exception

    def temp_function(self):
        logger('start temp_function ')
        try:
            element = self.el(L.edit.timeline.selected_item_frame)
            element_rect = element.rect
        except Exception:
            logger("exception occurs")
            raise Exception
