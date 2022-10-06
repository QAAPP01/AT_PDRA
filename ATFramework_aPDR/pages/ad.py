import time
# from os.path import dirname

from .locator import locator as L
# from .locator.locator_type import *
from ATFramework.utils.log import logger
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from SFT.conftest import PACKAGE_NAME
import inspect
pdr_package = PACKAGE_NAME

class Ad():
    LANDSCAPE = 0
    PORTRAIT = 1
    
    AD_NORMAL = [1,2,9]
    AD_PROMOTION = [2,6]
    
    AD_LIST = [
        None,                   #0
        L.ad.frame_full_ad,     #1  Full ad (open)
        None,                   #2  Full(b4 produce), promotion 
        L.ad.frame_promote,     #3  Dialog(exit, producing), crospromotion
        L.ad.frame_install_app, #4  Dialog/Project/reverse/stablilizser  ask user install app
        L.ad.frame_leave_app,   #5  Dialog (exit)
        L.ad.frame_phd_promote, #6  PHD promotion
        L.ad.watch_ad_to_unlock,#7  Dialog watch ad to unlock
        None,                   #8
        L.ad.frame_full_ad,     #9  full , others (b4 produce)
        ]
    
    source_page = None
    def __init__(self,super_class):
        self.d = super_class.driver.driver
        self.el = super_class.el
        m_list = inspect.getmembers(super_class,predicate=inspect.ismethod)
        for m , _ in m_list:
            if not m.startswith("__"):
                setattr(self,m,getattr(super_class,m))
    def has_shopping_cart(self):
        return bool(self.exit(L.ad.shopping_cart))
    def has_ad(self,frame_ad=None):
        frame_ad = frame_ad or L.ad.frame
        return bool(self.exist(frame_ad,10))
    def verify_aspect_ratio(self):
        rect = self.exist(L.ad.frame,10).rect
        return rect['width'] / rect['height'] > 1
    def get_aspect_ratio(self):
        logger("get_aspect_ratio for 10 sec now")
        ad_type = self.get_ad_type()
        if ad_type in [1,2,9]: return -1       # full screen mode, return -1
        locator_ad = self.AD_LIST[ad_type]
        try:
            rect = self.exist(locator_ad,10).rect
            return rect['width'] / rect['height']
        except:
            logger('AD is not found!')
            return
    def check_ad_and_ratio(self,orientation=0,target_ad=None):
        timeout = 10
        timer = time.time()
        while time.time()-timer < timeout:
            if target_ad:           # for produce video AD only
                if not self.find_target_ad(target_ad):
                    logger(f"Did NOT find specific ad type: {target_ad}")
                    return False,False
            ratio = self.get_aspect_ratio()
            if ratio:   # fonud ad
                logger(f"found ad type:{ratio}")
                break 
        else:
            logger("No ad is found in {timeout} sec")
        if not ratio:
            result_has_ad = False
            result_ratio = False
        else:
            logger("orientation = %a" % "PORTRAIT" if orientation else "LANDSCAPE")
            result_has_ad = True
            result_ratio = 0 < ratio < 1 if orientation else ratio > 1
            if ratio == -1: result_ratio = True     # special case, ratio = -1 (full screen)
        return result_has_ad, result_ratio
    def find_target_ad(self,target_ad):
        retry = 5
        result = False
        while retry:
            ad = self.get_ad_type()
            if ad in target_ad:
                result = True
                break
            else:
                retry -=1
                logger(f"Not correct AD:{ad}, retry again: {retry}")
                self.d.back()
                cancel = L.produce.facebook.produce_page.cancel
                produce = L.produce.facebook.next
                self.d.find_element(cancel[0],cancel[1]).click()
                self.d.find_element(produce[0],produce[1]).click()
        return result
    
    
    def get_ad_type(self,timeout = 5):
            logger("Checking AD")
            result = 0
            timer = time.time()
            while (not result) and time.time()-timer < timeout:
                self.source_page = self.d.page_source
                if "NO THANKS" in self.source_page:
                    logger("Type 1 AD found")
                    # self.driver.driver.back()
                    result = 1
                elif "[AID]Upgrade_No" in self.source_page:
                    logger("Type 2 AD found (promotion)")
                    # self.el(('accessibility id',"[AID]Upgrade_No")).click()
                    result = 2
                elif "cross_promotion" in self.source_page:
                    logger("Type 3 AD found (cross-promotion)")
                    result = 3
                elif "adMobNativeAppInstallAdView" in self.source_page:
                    logger("Type 4 AD found (project)")
                    result = 4
                elif "leave_app_dialog_ad_container" in self.source_page:
                    logger("Type 5 AD found (exit)")
                    result = 5
                elif "/ad_container" in self.source_page:    #PHD promotion ##ad_container_panel 
                    logger("Type 6 AD found (PHD promotion)")
                    result = 6
                elif "/Rewarded_desc" in self.source_page:  # Watch the ad abd check out the app
                    logger("Type 7 AD found (Watch AD to unlock)")
                    result = 7
                elif self.d.current_activity == "com.google.android.gms.ads.AdActivity":
                    logger("Type 9 AD found (full page)")
                    # self.driver.driver.back()
                    result = 9
            logger(f"Return AD type: {result} / {time.time()-timer} sec")
            return result
    
    def click_ad(self):
        logger("click AD now")
        TIMEOUT = 5 # expect exiting PDR in 5 sec
        ad_type = self.get_ad_type()
        if ad_type in [2,3,6]: 
            self.back()
            return True    #type 2,3,6 can not click, return pass directly
        locator_ad = self.AD_LIST[ad_type]
        self.click(locator_ad)
        timer = time.time()
        result = False
        try:
            while time.time()-timer < TIMEOUT:
                if self.d.current_package != PACKAGE_NAME:
                    logger("Under AD page now")
                    time.sleep(1)
                    self.d.back()
                    if ad_type in [1,9]: self.back()  # full screen ad won't close automatically
                    result = True
                    break
            else:
                logger("Can not enter AD page")
        except Exception as e:
            logger('click AD fail : %s' % str(e))
        return result
    
    def has_x(self):
        if self.is_exist(L.ad.x_button,3):
            logger("Exist: X button")
        else:
            logger("Not Exist: X button")
            return False
        if self.is_vanish(L.ad.x_button,7):
            logger('Vanish: X button')
            return True
        else:
            logger('Not vanish: X button')
            return False
    
    def close_full_page_ad(self):
        timer = time.time()
        while time.time()-timer <  10:
            if self.get_ad_type(1) > 0:
                logger('found ad page')
                if L.produce.facebook.produce_page.progress_bar[1] in self.source_page:
                    logger("found progress bar, exit function now")
                    return
                if self.get_ad_type(1) in [9, 10]:
                    logger('full page countdown ad.')
                    time.sleep(10)
                    self.exist_click(L.ad.close_btn)
                    self.exist_click(L.ad.close_btn2)
                    self.exist_click(L.ad.close_btn3)
                self.d.back()
                continue
        else:
            logger("No AD found.")
        if "help_enable_tip" in self.source_page:
            logger("Found tooltip , closing it")
            time.sleep(1)
            checkbox = self.el(L.produce.facebook.tooltip.show_next_time)
            if checkbox.get_attribute('checked') == 'true':
                logger("uncheck show next time")
                checkbox.click()
            time.sleep(1)
            self.el(L.produce.facebook.tooltip.ok).click()
        '''
        timer = time.time()
        click_back_times = 5
        while time.time() - timer < 3:
            time.sleep(1)
            self.source_page = self.d.page_source
            if "help_enable_tip" in self.source_page:
                logger("Found tooltip , closing it")
                time.sleep(1)
                checkbox = self.el(L.produce.facebook.tooltip.show_next_time)
                if checkbox.get_attribute('checked') == 'true':
                    logger("uncheck show next time")
                    checkbox.click()
                time.sleep(1)
                self.el(L.produce.facebook.tooltip.ok).click()
            if "produce_panel_facebook" in self.source_page:
                logger("in produce page now")
                return True
            else:
                click_back_times -= 1
                logger(f"Press back: remain({click_back_times})")
                self.back()
            raise Exception("close ")
        '''
        
    def close_opening_ads(self):
        timer = time.time()
        logger('close opening ads...')
        for retry in range(5):
            if self.is_exist(L.main.project.new):
                return True
            elif self.is_exist(L.main.setting.ratio_16_9):
                return True
            else:
                self._terminate_app(pdr_package)
                self.d.driver.activate_app(pdr_package)
        # while time.time()-timer < 20:
        #     if self.is_exist(L.main.project.new):
        #         logger('New project button is exist...')
        #         break
        #     self.exist_click(L.ad.close_btn)
        #     self.exist_click(L.ad.close_btn2)
        #     self.exist_click(L.ad.close_btn3)
        #     self.exist_click(L.ad.continue_to_app_btn)
        #     self.exist_click(L.ad.iap_back_btn)
        # if self.is_exist(L.ad.exclusive_offer):
        #     logger('close exclusive offer dialog...')
        #     self.d.back()
        