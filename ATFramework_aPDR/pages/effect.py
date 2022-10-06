import sys,time
from pages.base_page import BasePage
from ATFramework.utils.log import logger
#import unittest
from appium.webdriver.common.touch_action import TouchAction

from SFT.conftest import PACKAGE_NAME
from .locator.locator_type import *
from .locator import locator as L

class EffectPage(BasePage):
    
    
    _effect_tab =("accessibility id","[AID]TimeLine_Layer")
    _effect_title =("accessibility id","[AID]FloatingMenu_Title")
    _effect_title_assembyline =("xpath" , '(//*[contains(@resource-id,"library_unit_thumbnail")])[2]')
    _effect_add= ("id","library_unit_add")
    _effect_back = ("accessibility id","[AID]Library_Back")
    _effect_1 =("xpath" , "(//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout)[2]")
    _effect_set_font= ("accessibility id","[AID]TitleDesign_RightTop")
    _effect_font_rgb = ("accessibility id","[AID]TextEdit_Color")
    _effect_font_saturation = ("accessibility id","[AID]TextEdit_Pick")
    _effect_font_transparent= ("accessibility id","[AID]TextEdit_Opcity_Pick")
    _effect_font_type= ("accessibility id","[AID]Item_InputText")
    _effect_font_type_5 = ("xpath" , '(//android.widget.TextView[@content-desc="[AID]Item_InputText"])[5]')
    # _title_rotate = ("id", "rz_control_corner_right_bottom")
    _title_rotate = ("id", "control_point_corner_right_bottom")
    # _title_size =("id" , "rz_control_corner_left_bottom" )
    _title_size =("id" , "control_point_corner_left_top" )
    # _title_object = ("id", "rz_content")
    _title_object = ("id", "resizable_boundary")
    _effect_rotate = ("id", "control_point_corner_right_bottom")
    # _effect_size =("id" , "control_point_corner_left_bottom" )
    _effect_size =("id" , "control_point_corner_left_top" )
    _effect_object = ("id", "view_auto_resize")
    _mask_rotate_right_point = id("rotate_right_point")
    _effect_layer_rotate = ("id", "rotate_point")
    _effect_layer_size = ("id", "resize_point_left_top")
    _effect_layer_object = ("id", "rectangle_mask_border")

    def __init__(self,*args,**kwargs):
        BasePage.__init__(self,*args,**kwargs)
        
    def add_title(self):
        logger ("start >> add_title <<")
        # self.click_element(self._project_empty)
        self.click_element(self._effect_tab)
        self.click_element(self._effect_title)
        return True
    def select_title_assembyline(self):
        logger ("start >> select_title_assembyline <<")
        self.click_element(self._effect_title_assembyline)
        self.click_element(self._effect_add)
        self.click_element(self._effect_back)
        return True
    def modify_first_effect(self):
        logger ("start >> modify_first_effect <<")
        self.click_element(self._effect_1)
        self.click_element(self._effect_set_font)
        self.driver.set_slider(self._effect_font_rgb,0.3)
        self.driver.set_slider(self._effect_font_saturation,0.6)
        self.driver.set_slider(self._effect_font_transparent,0.9)
        logger ("start >> change font <<")
        self.click_element(self._effect_font_type)
        time.sleep(1)
        self.click_element(self._effect_font_type_5)
        self.driver.driver.back()
        logger ("start >> rotate <<")
        self.driver.swipe_element(self._effect_rotate,"up",30)
        logger ("start >> resize <<")
        self.driver.swipe_element(self._effect_size,"left",20)

    def modify_effect_rotate(self, direction="down"):
        logger("start >> modify_effect_rotate <<")
        self.driver.swipe_element(self._effect_rotate, direction, 50)

    def modify_title_rotate(self, direction="down"):
        logger("start >> modify_title_rotate <<")
        self.driver.swipe_element(self._title_rotate, direction, 50)
        
    def modify_mask_rotate(self, direction="down"):
        logger("start >> modify_mask_rotate <<")
        self.driver.swipe_element(self._mask_rotate_right_point, direction, 50)

    def modify_effect_layer_rotate(self):
        logger("start >> modify_effect_layer_rotate <<")
        self.driver.swipe_element(self._effect_layer_rotate, "down", 50)

    def modify_effect_size(self):
        logger("start >> modify_effect_size <<")
        self.driver.swipe_element(self._effect_size, "left", 50)    
        
    def modify_title_size(self):
        logger("start >> modify_title_size <<")
        self.driver.swipe_element(self._title_size, "left", 50)

    def modify_effect_layer_size(self):
        logger("start >> modify_effect_layer_size <<")
        self.driver.swipe_element(self._effect_layer_size, "left", 50)

    def move_effect_layer(self):
        logger("start >> move_effect_layer <<")
        self.driver.swipe_element(self._effect_layer_object, "right", 50)

    def snap_effect_to_boundary(self):
        logger("start >> snap_effect_to_boundary <<")
        try:
            el_effect = self.el(self._effect_object)
            x_center = int(el_effect.rect['x']+el_effect.rect['width']/2)
            y_center = int(el_effect.rect['y'] + el_effect.rect['height'] / 2)
            preview_wnd = self.el(L.edit.preview.movie_view)
            TouchAction(self.driver.driver).press(None, x_center, y_center).wait(2500).move_to(None, preview_wnd.rect[
                'x'] + 1 + int(el_effect.rect['width'] / 2), y_center).release().perform()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True    
        
    def snap_title_to_boundary(self):
        logger("start >> snap_title_to_boundary <<")
        try:
            el_effect = self.el(self._title_object)
            x_center = int(el_effect.rect['x']+el_effect.rect['width']/2)
            y_center = int(el_effect.rect['y'] + el_effect.rect['height'] / 2)
            preview_wnd = self.el(L.edit.preview.movie_view)
            TouchAction(self.driver.driver).press(None, x_center, y_center).wait(2500).move_to(None, preview_wnd.rect[
                'x'] + 1 + int(el_effect.rect['width'] / 2), y_center).release().perform()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True        
    
    def move_title(self):
        logger("start >> move_title <<")
        try:
            el_effect = self.el(self._title_object)
            x_center = int(el_effect.rect['x']+el_effect.rect['width']/2)
            y_center = int(el_effect.rect['y'] + el_effect.rect['height'] / 2)
            preview_wnd = self.el(L.edit.preview.movie_view)
            TouchAction(self.driver.driver).press(None, x_center, y_center).wait(2500).move_to(None, preview_wnd.rect[
                'x'] + 1 + int(el_effect.rect['width'] / 2), preview_wnd.rect[
                'y'] + 1 + int(el_effect.rect['height'] / 2)).release().perform()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def move_effect_to_center(self):
        logger("start >> move_effect_to_center <<")
        try:
            el_effect = self.el(self._effect_object)
            x_center = int(el_effect.rect['x']+el_effect.rect['width']/2)
            y_center = int(el_effect.rect['y'] + el_effect.rect['height'] / 2)
            preview_wnd = self.el(L.edit.preview.movie_view)
            x_center_preview = int(preview_wnd.rect['x']+preview_wnd.rect['width']/2)
            y_center_preview = int(preview_wnd.rect['y'] + preview_wnd.rect['height'] / 2)
            TouchAction(self.driver.driver).press(None, x_center, y_center).wait(1000).move_to(None, x_center_preview,
                                                                                   y_center_preview).release().perform()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True    
        
    def move_title_to_center(self):
        logger("start >> move_title_to_center <<")
        try:
            el_effect = self.el(self._title_object)
            x_center = int(el_effect.rect['x']+el_effect.rect['width']/2)
            y_center = int(el_effect.rect['y'] + el_effect.rect['height'] / 2)
            preview_wnd = self.el(L.edit.preview.movie_view)
            x_center_preview = int(preview_wnd.rect['x']+preview_wnd.rect['width']/2)
            y_center_preview = int(preview_wnd.rect['y'] + preview_wnd.rect['height'] / 2)
            TouchAction(self.driver.driver).press(None, x_center, y_center).wait(1000).move_to(None, x_center_preview,
                                                                                   y_center_preview).release().perform()
        except Exception:
            logger("exception occurs")
            raise Exception
        return True

    def check_effect_snap_to_boundary(self):
        logger("start >> snap_effect_to_boundary <<")
        try:
            #verify the coordinate of effect object
            el_effect = self.el(self._effect_object)
            preview_wnd = self.el(L.edit.preview.movie_view)
            logger(f"x-axis of effect object={el_effect.rect['x']}")
            logger(f"x-axis of preview window={preview_wnd.rect['x']}")
            if el_effect.rect['x'] != preview_wnd.rect['x']:
                return False
        except Exception:
            logger("exception occurs")
            raise Exception
        return True    
        
    def check_title_snap_to_boundary(self):
        logger("start >> check_title_snap_to_boundary <<")
        try:
            #verify the coordinate of effect object
            el_effect = self.el(self._title_object)
            preview_wnd = self.el(L.edit.preview.movie_view)
            logger(f"x-axis of effect object={el_effect.rect['x']}")
            logger(f"x-axis of preview window={preview_wnd.rect['x']}")
            if el_effect.rect['x'] != preview_wnd.rect['x']:
                return False
        except Exception:
            logger("exception occurs")
            raise Exception
        return True
