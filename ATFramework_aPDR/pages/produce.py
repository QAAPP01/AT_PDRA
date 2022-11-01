import sys, time
from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.ATFramework.utils.extra import element_exist_click
from ATFramework_aPDR.ATFramework.utils.log import logger
import subprocess
from pathlib import Path



from .locator import locator as L

class _Settings(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.el = lambda id: self.driver.driver.find_element(id[0],id[1])
        self.els = lambda id: self.driver.driver.find_elements(id[0],id[1])
        self.el_find_string = lambda id: self.driver.driver.find_element('xpath','//*[contains(@text,"' + id + '")]')
    def set_save_location(self):
        pass # no case need it
    
    def set_bitrate(self,profile):
        list = [
            L.produce.facebook.setting_page.better_quality,
            L.produce.facebook.setting_page.standard,
            L.produce.facebook.setting_page.smaller_size,
        ]
        time.sleep(1)
        self.el(L.produce.facebook.setting_page.bitrate).click()
        time.sleep(1)
        self.el(list[profile]).click()
    def set_framerate(self,profile):
        list = [
            L.produce.facebook.setting_page.fps_24,
            L.produce.facebook.setting_page.fps_30,
            L.produce.facebook.setting_page.fps_60,
            L.produce.facebook.setting_page.fps_25,
            L.produce.facebook.setting_page.fps_50,
        ]
        time.sleep(1)
        self.el(L.produce.facebook.setting_page.framerate).click()
        time.sleep(1)
        self.el(list[profile]).click()


class ProducePage(BasePage):
    def __init__(self,*args,**kwargs):
        BasePage.__init__(self,*args,**kwargs)
        self.setting = _Settings(self.driver)
    
    def set_resolution(self,profile):
        list = [
            L.produce.facebook.ultra_hd,
            L.produce.facebook.full_hd,
            L.produce.facebook.hd,
            L.produce.facebook.sd,
        ]
        self.el(list[profile]).click()
        time.sleep(1)
        
    
    def close_produce_page(self):
        self.exist_click(L.main.subscribe.back_btn)
        self.exist_click(L.produce.facebook.ad.cancel)
        self.exist_click(L.produce.facebook.ad.close)   
        self.exist_click(L.produce.facebook.ad.close_btn2)   
        page_source = self.driver.driver.page_source
        if "help_enable_tip" in page_source:
            logger("Found tooltip ")
            result = self.close_tooltip()
        try:
            progress = self.el(L.produce.facebook.produce_page.progress_bar)
            logger("Producing video now")
            timer = time.time()
            while  time.time() -timer < 60 *3:  # wait 3min to produce
                if float(progress.text) == 100.0: 
                    logger("Produce finish.")
                    break
                time.sleep(3)
            else:
                logger("Produce checking - Time Out (3min)")
                raise Exception("Produce checking - Time Out (3min)")
        except:
            logger("progress bar is gone.")
        self.click(L.produce.facebook.produce_page.to_facebook)
        click_back_times = 5
        while click_back_times:
            page_source = self.driver.driver.page_source
            self.exist_click(L.produce.facebook.produce_page.to_facebook, 3)
            self.exist_click(L.produce.facebook.rate_us, 3)
            if "produce_panel_facebook" in page_source:
                time.sleep(1.5)
                if "produce_panel_facebook" in self.driver.driver.page_source: # double check, sometimes share page popup slowly
                    logger("in produce page now")
                    return True
                else:
                    logger("double check fail")
                    continue
            elif "help_enable_tip" in page_source:
                logger("Found tooltip ")
                result = self.close_tooltip()
                if not result:
                    continue
            else:
                click_back_times -= 1
                logger(f"Press back: remain({click_back_times})")
                self.back()
                time.sleep(0.5)
                if self.is_exist(L.main.project.new):
                    logger("Now in main page")
                    return True
        else:
            logger('Can not back produce page')
            raise Exception("Can not back produce page")
    
    def close_tooltip(self):
        logger("start close_tooltip")
        try:
            checkbox = self.el(L.produce.facebook.tooltip.show_next_time)
            if checkbox.get_attribute('checked') == 'true':
                logger("uncheck show next time")
                # checkbox.click()
            time.sleep(1)
            self.el(L.produce.facebook.tooltip.ok).click()
            time.sleep(0.5)
            return True
        except:
            logger("unable to close tooltip, retry now")
            return False
    
    def select_cloud(self):
        time.sleep(1)
        self.driver.swipe_left()
        self.el(L.produce.tab.cloud).click()
        
    def check_produce_ad(self,type="full_hd"):
        if type.lower() == "ultra_hd":
            self.click(L.produce.facebook.ultra_hd)
        else:
            self.click(L.produce.facebook.full_hd)
        result_has_subscription = bool(self.ad.get_ad_type())
        self.back() # cancel subscription
        result_has_unlock_ad = bool(self.ad.get_ad_type())
        self.back() # exit unload ad page
        return result_has_subscription , result_has_unlock_ad

    def select_produce_type(self, target):
        logger(f"start >> select_produce_type = {target}<<")
        try:
            if target == 'gallery':
                locator = L.produce.tab.gallery
            elif target == 'ig':
                locator = L.produce.tab.ig
            elif target == 'tiktok':
                locator = L.produce.tab.tiktok
            elif target == 'facebook':
                locator = L.produce.tab.facebook
            elif target == 'youtube':
                locator = L.produce.tab.youtube
            elif target == 'share':
                locator = L.produce.tab.share
            elif target == 'cloud':
                locator = L.produce.tab.cloud
            else:
                logger(f'parameter {target} is incorrect.')
                raise Exception
            
            self.el(locator).click()
            time.sleep(3)
            if self.is_exist(L.produce.gallery.btn_next):
                return True
            else:
                logger("Next button is not exist.")
                return False
        except Exception:
            raise Exception


    def start_produce(self, timeout=100):
        logger("start >> start_produce<<")
        try:
            self.el(L.produce.gallery.btn_next).click()
            self.exist_click(L.produce.iap_back)
            is_complete = 0
            for retry in range(int(timeout)):
                if self.is_exist(L.main.gamification.btn_produce_page_claim):
                    logger('Gamification task complete dialog pop, tap back.')
                    self.back()
                if self.is_exist(L.produce.gallery.produce_page.save_to_camera_roll):
                    logger('Save to Camera roll text shows, end waiting.')
                    is_complete = 1
                    break
            if is_complete == 1:
                return True
            else:
                logger('Produce not complete before timeout.')
                raise Exception  
        except Exception:
            raise Exception

    def preview_produced_video(self):
        logger("start >> preview_produced_video<<")
        try:
            self.el(L.produce.gallery.produce_page.btn_play).click()
            time.sleep(5)
            if self.is_exist(L.produce.gallery.produce_page.full_screen_preview):
                logger('Enter full screen preview.')
                self.back()
                return True
            else:
                logger("Didn't enter full screen preview.")
                raise Exception
        except Exception:
            raise Exception

    def check_produce_progress(self, timeout=400):
        logger("start >> check_produce_progress<<")
        try:
            self.el(L.produce.gallery.btn_next).click()
            self.exist_click(L.produce.iap_back)
            is_complete = 0
            result_progress = False
            result_thumbnail = False  
            result_ad = False
            result_back = False
            result_cancel = False
            
            if self.is_exist(L.produce.gallery.produce_page.progress_bar):
                result_progress = True 
            
            if self.is_exist(L.produce.gallery.produce_page.project_thumbnail):
                result_thumbnail = True     
            
            if self.is_exist(L.produce.gallery.produce_page.ad_frame):
                result_ad = True
            
            if self.is_exist(L.produce.gallery.produce_page.btn_back):
                result_back = True 
                
            if self.is_exist(L.produce.gallery.produce_page.btn_cancel):
                result_cancel = True   
                
            for retry in range(int(timeout)):
                if self.is_exist(L.produce.gallery.produce_page.save_to_camera_roll):
                    logger('Save to Camera roll text shows, end waiting.')
                    is_complete = 1
                    break
            if is_complete == 1:
                return result_progress, result_thumbnail, result_ad, result_back, result_cancel
            else:
                logger('Produce not complete before timeout.')
                raise Exception
        except Exception:
            raise Exception
 
    def share_to_ig(self):
        logger("start >> share_to_ig<<")
        try:
            self.el(L.produce.gallery.produce_page.btn_share_to).click()
            time.sleep(5)
            if self.is_exist(L.produce.gallery.produce_page.ig_share_menu):
                logger('IG share menu shows.')
                self.back()
                return True
            else:
                logger("Didn't enter IG share menu.")
                raise Exception
        except Exception:
            raise Exception  
    
    def share_to_tiktok(self):
        logger("start >> share_to_tiktok<<")
        try:
            tiktok_package = 'com.ss.android.ugc.trill'
            self.el(L.produce.gallery.produce_page.btn_share_to).click()
            time.sleep(5)
            if tiktok_package == self.driver.driver.current_package:
                logger('tiktok opened.')
                # self.driver.driver.terminate_app(tiktok_package)
                # self.back()
                return True
            else:
                logger("Didn't open tiktok.")
                raise Exception
        except Exception:
            raise Exception

    def get_video_quality_radio_is_checked(self):
        logger("start >> get_video_quality_radio_is_checked <<")
        try:
            if self.el(L.produce.gallery.ultra_hd).get_attribute('checked') == 'true':
                logger(f"UHD is checked.")
                return 'uhd'
            elif self.el(L.produce.gallery.full_hd).get_attribute('checked') == 'true':
                logger(f"FHD is checked.")
                return 'fhd'
            elif self.el(L.produce.gallery.hd).get_attribute('checked') == 'true':
                logger(f"HD is checked.")
                return 'hd'
            elif self.el(L.produce.gallery.sd).get_attribute('checked') == 'true':
                logger(f"SD is checked.")
                return 'sd'
            else:
                logger("Can't find elements")
                return False
        except Exception:
            logger("Exception occurs")
            return False
            
    
    def select_produce_resolution(self, target):
        logger(f"start >> select_produce_resolution = {target}<<")
        try:
            if target == 'fhd':
                locator = L.produce.gallery.fhd1080p
            elif target == 'hd':
                locator = L.produce.gallery.hd720p
            elif target == 'hd540p':
                locator = L.produce.gallery.hd540p
            elif target == 'sd':
                locator = L.produce.gallery.sd360p
            elif target == '4k':
                locator = L.produce.gallery.uhd_4k
            else:
                logger(f'parameter {target} is incorrect.')
                raise Exception
            self.el(locator).click()
            time.sleep(5)
        except Exception:
            raise Exception