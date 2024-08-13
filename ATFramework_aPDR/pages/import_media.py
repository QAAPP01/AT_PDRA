import sys,time
from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.ATFramework.utils.extra import element_exist_click
from ATFramework_aPDR.ATFramework.utils.log import logger
import random
from appium.webdriver.common.touch_action import TouchAction
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage
from pathlib import Path

from ATFramework_aPDR.pages.locator import locator as L
from .locator.locator import edit as E

from ATFramework_aPDR.SFT.conftest import PACKAGE_NAME
from .locator.locator_type import find_string, aid, id, xpath
from ATFramework_aPDR.pages.page_factory import PageFactory

google_drive_account = 'clt.qaat@gmail.com'

class MediaPage(BasePage):

    def __init__(self, *args, **kwargs):
        BasePage.__init__(self, *args, **kwargs)
        self.el = lambda id: self.driver.driver.find_element(id[0], id[1])
        self.els = lambda id: self.driver.driver.find_elements(id[0], id[1])
        self.udid = self.driver.driver.desired_capabilities['deviceUDID']

    def sort_date_descend(self, timeout=60):
        try:
            self.click(L.import_media.media_library.sort_button)
            self.click(L.import_media.sort_menu.by_date)
            self.click(L.import_media.sort_menu.descending)
            self.driver.driver.back()
            if self.waiting_loading(timeout):
                return True
            else:
                return False
        except Exception as err:
            logger(f'[Error] {err}')

    def select_local_folder(self, folder):
        try:
            if not self.element(L.import_media.video_library.folder_name(1)).text == folder:
                self.click(L.import_media.video_library.select_folder)
                while not self.click(find_string(folder)):
                    folders = self.elements(L.import_media.video_library.folder_name(0))
                    last_folder = folders[-1].text
                    self.h_swipe_element(folders[-1], folders[1], speed=3)
                    folders = self.elements(L.import_media.video_library.folder_name(0))
                    if folders[-1].text == last_folder:
                        raise Exception(f'No found folder: {folder}')
            return True
        except Exception as err:
            raise Exception(err)

    def select_local_file(self, media_type, folder, file_name):
        try:
            media_type = media_type[0].upper() + media_type[1:].lower()
            if media_type not in ['Video', 'Photo']:
                media_type = 'Video'
                logger('[Warning] Did not assign media type')
            if media_type == 'Video':
                if not self.switch_to_video_library():
                    raise Exception('Click video library fail')
            elif media_type == 'Photo':
                if not self.switch_to_photo_library():
                    raise Exception('Click photo library fail')
            if not self.select_local_folder(folder):
                raise Exception('Open folder fail')
            if not self.select_media_by_text(file_name):
                raise Exception('Select file fail')
            return True
        except Exception as err:
            raise Exception(err)
            return False

    def select_local_video(self, folder, file_name):
        try:
            if not self.switch_to_video_library():
                logger('Click video library fail')
            if not self.select_local_folder(folder):
                logger('Open folder fail')
            if not self.select_media_by_text(file_name):
                raise Exception('Select file fail')
            return True
        except Exception as err:
            logger(err)
            return False


    def select_local_photo(self, folder, file_name):
        try:
            if not self.switch_to_photo_library():
                raise Exception('Click photo library fail')
            if not self.select_local_folder(folder):
                raise Exception('Open folder fail')
            if not self.select_media_by_text(file_name):
                raise Exception('Select file fail')
            return True
        except Exception as err:
            raise Exception(err)

    def select_video_library(self, stock_name):
        stock = [
            "shutterstock",
            "getty",
            "getty_pro",
            "giphy",
            "pexels",
            "pixabay",
            "google_drive",
        ]
        try:
            if stock_name not in stock:
                logger(f'[Fail] Invalid stock name: {stock_name}')
                return False

            self.click(L.import_media.video_library.video_entry, 2)
            tab = ('xpath', '//android.widget.LinearLayout/android.view.ViewGroup')
            if not self.click(L.import_media.media_library.stock(stock_name), 1):
                for retry in range(60):
                    if not self.is_exist(L.import_media.video_library.local_folder, 1):
                        tabs = self.elements(tab)
                        self.h_swipe_element(tabs[0], tabs[-1], 3)
                        if self.click(L.import_media.media_library.stock(stock_name), 1):
                            return True
                    else:
                        break
            end = ""
            for retry in range(60):
                if not self.click(L.import_media.media_library.stock(stock_name), 1):
                    tabs = self.elements(tab)
                    last = tabs[-1].get_attribute("resource-id")
                    if last == end:
                        logger(f'[Fail] Stock {stock_name} is not found')
                        return False
                    else:
                        end = last
                        self.h_swipe_element(tabs[-1], tabs[0], 3)
                else:
                    return True
            else:
                raise Exception("out of retry")
        except Exception as err:
            logger(f'\n[Error] {err}')
            return False

    def select_photo_library(self, stock_name):
        stock = [
            "shutterstock",
            "getty",
            "getty_pro",
            "giphy",
            "pexels",
            "pixabay",
            "google_drive",
        ]
        try:
            if stock_name not in stock:
                logger(f'[Fail] Invalid stock name: {stock_name}')
                return False

            self.click(L.import_media.media_library.photo_entry, 2)
            tab = ('xpath', '//android.widget.LinearLayout/android.view.ViewGroup')
            if not self.click(L.import_media.media_library.stock(stock_name), 1):
                for retry in range(60):
                    if not self.is_exist(L.import_media.video_library.local_folder, 1):
                        tabs = self.elements(tab)
                        self.h_swipe_element(tabs[0], tabs[-1], 3)
                        if self.click(L.import_media.media_library.stock(stock_name), 1):
                            return True
                    else:
                        break
            end = ""
            for retry in range(60):
                if not self.click(L.import_media.media_library.stock(stock_name), 1):
                    tabs = self.elements(tab)
                    last = tabs[-1].get_attribute("resource-id")
                    if last == end:
                        logger(f'[Fail] Stock {stock_name} is not found')
                        return False
                    else:
                        end = last
                        self.h_swipe_element(tabs[-1], tabs[0], 3)
                else:
                    return True
            else:
                raise Exception("out of retry")
        except Exception as err:
            logger(f'\n[Error] {err}')
            return False

    def select_media_by_text(self, file_name, retry=10, speed=7):
        for i in range(retry):
            clips = self.elements(L.import_media.media_library.file_name(0))
            if any(clip.get_attribute('text') == file_name for clip in clips):
                self.click(find_string(file_name))
                self.h_click(L.import_media.media_library.apply, timeout=0.5)
                return True
            self.h_swipe_element(clips[-1], clips[0], speed)
        logger(f'[Fail] Cannot find "{file_name}" within {retry} times')
        return False

    def find_local_file(self, file_name, speed=7, retry=10):
        for i in range(retry):
            clips = self.elements(L.import_media.media_library.file_name(0))
            if any(clip.get_attribute('text') == file_name for clip in clips):
                return True
            self.h_swipe_element(clips[-1], clips[0], speed)
        logger(f'[Fail] Cannot find "{file_name}" within {retry} times')
        return False

    def text_search(self, text, locator=L.import_media.media_library.search):
        try:
            element = self.element(locator)
            element.click()
            element.send_keys(text)
            self.driver.driver.press_keycode(66)

            if self.h_is_not_exist(L.import_media.media_library.waiting_cursor, 10):
                return True
            else:
                raise Exception("Search timeout")
        except Exception as err:
            logger(f"[Error] {err}")
            return False

    def wait_media_change(self, old_element, locator=L.import_media.media_library.media(), timeout=10):
        for i in range(timeout):
            if self.element(locator) != old_element:
                break
            time.sleep(1)
        else:
            logger("Loading timeout")
            return False

    def subscribe_getty_pro(self):
        if self.click(L.import_media.media_library.getty_iap_monthly, 2):
            self.click(L.import_media.media_library.getty_iap_continue)
            self.click(('class name', 'android.widget.Button'))
            self.click(find_string('Not now'), 1)
            if self.is_not_exist(aid('Google Play'), 30):
                if self.is_exist(L.import_media.media_library.media(), 10) or self.is_exist(L.import_media.music_library.music) :
                    return True
                else:
                    raise Exception("Doesn't return to media picker")
            else:
                raise Exception("Subscribe timeout")
        else:
            return False


    def scroll_to_top(self):
        for i in range(60):
            clip = self.elements(L.import_media.media_library.media(0))
            self.h_swipe_element(clip[0], clip[-1], 1)
            new_clip = self.elements(L.import_media.media_library.media(0))
            if new_clip[0] == clip[0]:
                return True
        else:
            raise Exception("Scroll to top timeout")

    def select_music_library(self, stock):
        try:
            end = ""
            if not self.is_exist(stock):
                while not self.h_click(stock, 1):
                    tabs = self.h_get_elements(('xpath', '//android.widget.LinearLayout/android.widget.RelativeLayout'))
                    last = tabs[-1].get_attribute("resource-id")
                    if last == end:
                        logger(f'[Fail] No stock: {stock}')
                        return False
                    else:
                        end = last
                        self.h_swipe_element(tabs[-1], tabs[0], 5)
                return True
            else:
                if self.element(stock).get_attribute('selected') == 'false':
                    self.h_click(stock, 1)
                return True
        except Exception as err:
            logger(f'\n[Error] {err}')

    def waiting(self, timeout=60):
        for i in range(timeout):
            if self.h_is_exist(find_string('Cancel'), 1):
                continue
            else:
                return True
        logger("[Warning] waiting timeout")
        return False

    def waiting_loading(self, timeout=120):
        if self.h_is_exist(L.import_media.media_library.percentage, 5):
            while 1:
                percentage = self.element(L.import_media.media_library.percentage).text
                if self.h_is_not_exist(L.import_media.media_library.percentage, timeout):
                    return True
                else:
                    if percentage != self.element(L.import_media.media_library.percentage).text:
                        continue
                    else:
                        logger("[Warning] loading timeout", log_level="warn")
                        return False

    def waiting_download(self, timeout=120):
        self.waiting_loading(timeout)

    def import_last_folder(self):
        logger ("start >> import_last_folder <<")
        # self.click_element(self._project_empty)
        self.click_element(L.library_gridview.last)
        return self.wait_until_element_exist(L.library_gridview.first,10)

    def import_first_file(self):
        # logger ("start >> import_first_file <<")
        self.h_click(L.library_gridview.first)
        self.h_click(L.library_gridview.add)
        self.h_click(L.library_gridview.apply, 1)
        result = self.h_is_exist(L.timeline.clip, 5)
        return result

    def click_music_tab(self, tab):
        """
        Click music tab
        :param tab: 'local' or 'meta' or 'mixtape' or 'getty' or 'cl'
        :return: Boolean of success or not
        """
        tabs = {
            'local': id('tab_music_local'),
            'meta': id('tab_meta_sound'),
            'mixtape': id('tab_mix_tape_sound_clip'),
            'getty': id('tab_sound_stripe'),
            'cl': id('tab_bgm_sound_clip'),
        }
        if tab not in tabs:
            logger(f'[Fail] Invalid tab: {tab}')
            return False
        if not self.element(tabs[tab]).get_attribute('selected') == 'true':
            if self.click(tabs[tab], 1):
                logger(f'Clicked {tab}')
                return True
            else:
                logger(f"[Fail] Click {tab}")
                return False

    def click_sfx_tab(self, tab):
        """
        Click sound fx tab
        :param tab: 'meta' or 'cl'
        :return: Boolean of success or not
        """
        tabs = {
            'meta': id('tab_meta_sound_effect'),
            'getty': id('tab_sound_stripe'),
            'cl': id('tab_sound_fx'),
        }
        if tab not in tabs:
            logger(f'[Fail] Invalid tab: {tab}')
            return False
        if not self.element(tabs[tab]).get_attribute('selected') == 'true':
            if self.click(tabs[tab], 1):
                logger(f'Clicked {tab}')
                return True
            else:
                logger(f"[Fail] Click {tab}")
                return False


        
    def get_music_name(self, index, timeout=10):
        logger("start >> get_music_name<<")
        logger(f"input - {index}")
        try:
            self.is_exist(L.library_listview.frame, timeout)
            frame = self.el(L.library_listview.frame)
            element = frame.find_element_by_xpath(f'//*[contains(@resource-id,"library_unit_caption")][{index}]')
        except Exception:
            logger(f"Fail to locate element")
            raise Exception
        return element.text
        
    # media name in library is removed in new version, use order to select.
    # Note the order will be like: 
    #   1   2   
    #   3
    #   4
    def select_media_by_order(self, order, timeout=10):
        logger("start >> select_media_by_order<<")
        logger(f"input - {order}")
        try:
            if self.is_exist(L.library_gridview.frame, timeout):
                frame = self.el(L.library_gridview.frame)
                element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"library_unit_thumbnail")])[{order}]')
                element.click()
            elif self.is_exist(L.library_gridview.library_recycler_gridview, timeout):
                frame = self.el(L.library_gridview.library_recycler_gridview)
                element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"library_unit_thumbnail")])[{order}]')
                element.click()
            else:
                logger(f"Fail to locate library")
                raise Exception
        except Exception:
            logger(f"Fail to select - {order}")
            raise Exception
        return True

    def select_effect_layer_by_order(self, order, timeout=10):
        logger("start >> select_effect_layer_by_order<<")
        logger(f"input - {order}")
        try:
            self.is_exist(L.library_gridview.library_recycler_gridview, timeout)
            frame = self.el(L.library_gridview.library_recycler_gridview)
            element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"fx_layer_library_item")])[{order}]')
            element.click()
        except Exception:
            logger(f"Fail to locate element")
            raise Exception
        return True

    def select_sticker_by_order(self, order, timeout=20):
        logger("start >> select_sticker_by_order<<")
        logger(f"input - {order}")
        try:
            self.is_exist(L.import_media.media_library.recycler_view, timeout)
            frame = self.el(L.import_media.media_library.recycler_view)
            element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"cms_sticker_library_item")])[{order}]')
            element.click()
        except Exception:
            logger(f"Fail to locate element")
            raise Exception
        return True


    def select_list_media_by_order(self, order, timeout=10):
        logger("start >> select_list_media_by_order<<")
        logger(f"input - {order}")
        try:
            self.is_exist(L.library_listview.frame, timeout)
            frame = self.el(L.library_listview.frame)
            element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"library_unit_background")])[{order}]')
            element.click()
        except Exception:
            logger(f"Fail to locate element - {order}")
            raise Exception
        return True

    def select_title_by_order(self, order, timeout=10):
        logger("start >> select_media_by_order<<")
        logger(f"input - {order}")
        try:
            self.is_exist(L.library_gridview.frame, timeout)
            frame = self.el(L.library_gridview.frame)
            element = frame.find_element_by_xpath(f'(//*[contains(@resource-id,"layout_title_item")])[{order}]')
            element.click()
        except Exception:
            logger(f"Fail to locate element - {order}")
            raise Exception
        return True    

    def check_media_exists_by_text(self, name):
        logger("start >> check_media_exists_by_text<<")
        logger(f"input - {name}")
        try:
            frame = self.el(L.library_gridview.frame)
            element = frame.find_element_by_xpath(f'//*[contains(@text,"{name}")]')
        except Exception:
            logger("Fail to locate element")
            return False
        return True

    def get_first_media(self, timeout=10): # for Video/Photo
        logger("start >> select_first_media<<")
        try:
            element = self.el(L.library_gridview.first)
            element.click()
            #text = element.get_attribute('text')
            #logger(f"select media={text}")
            logger("select first media")
        except Exception:
            logger("Fail to locate element")
            raise Exception
        return True

    def select_song_by_text(self, name):
        logger("start >> select_song_by_text<<")
        logger(f"input - {name}")
        frame = self.el(L.library_listview.frame)
        locator = ("xpath", f'//*[contains(@text,"{name}")]')
        for retry in range(30):
            if not self.is_exist(locator):
                self.driver.swipe_element(L.library_listview.frame, 'up', 300)
                self.driver.swipe_element(L.library_listview.frame, 'up', 300)
            else:
                self.driver.swipe_element(L.library_listview.frame, 'up', 100)
                break
        element = frame.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]')
        element.click()

    def check_song_exists_by_text(self, name):
        logger("start >> check_media_exists_by_text<<")
        logger(f"input - {name}")
        try:
            frame = self.el(L.library_listview.frame)
            element = frame.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]')
        except Exception:
            logger("Fail to locate element")
            return False
        return True

    def add_selected_song_to_timeline(self):
        logger("start >> add_selected_song_to_timeline<<")
        frame = self.el(L.library_listview.frame)
        # element = frame.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]')
        # element.click()
        elements = frame.find_elements_by_id(PACKAGE_NAME+":id/library_unit_add")
        is_found = 0
        for element in elements:
            if element.get_attribute('enabled') == 'true':
                is_found = 1
                element.click()
                break
        if is_found == 0:
            raise Exception
        return True

    def add_song_to_timeline_by_name(self, name):
        logger(f"start >> add_selected_song_to_timeline = {name}<<")
        frame = self.el(L.library_listview.frame)
        element = frame.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]/..')
        btn_add = element.find_element_by_xpath("//android.widget.ImageView[contains(@resource-id,'library_unit_add')]")
        btn_add.click()

    def switch_to_video_library(self):
        try:
            return True if self.h_click(L.import_media.video_library.video_entry) else False
        except Exception as err:
            raise Exception(err)
    def switch_to_photo_library(self):
        try:
            return True if self.h_click(L.import_media.photo_library.photo_entry) else False
        except Exception as err:
            raise Exception(err)

    def switch_to_pip_video_library(self):
        logger("start >> switch_to_pip_video_library <<")
        time.sleep(10)
        self.tap_element(L.menu.pip_video_library)


    def switch_to_title_library(self):
        logger("start >> switch_to_title_library <<")
        time.sleep(10)
        self.tap_element(L.menu.title_library)

    def switch_to_pip_photo_library(self):
        logger("start >> switch_to_pip_photo_library <<")
        time.sleep(10)
        self.tap_element(L.menu.pip_photo_library)

    def switch_to_music_library(self):
        logger("start >> switch_to_music_library <<")
        time.sleep(10)
        self.tap_element(L.menu.music_library)

    def switch_to_sound_clips_library(self):
        logger("start >> switch_to_sound_clips_library <<")
        time.sleep(10)
        self.tap_element(L.menu.sound_clips_library)

    def switch_to_template_library(self):
        logger("start >> switch_to_template_library <<")
        time.sleep(10)
        self.tap_element(L.menu.template_library)

    def switch_to_overlay_library(self):
        logger("start >> switch_to_overlay_library <<")
        time.sleep(10)
        self.tap_element(L.menu.overlay_library)

    def switch_to_effect_layer_library(self):
        logger("start >> switch_to_effect_layer_library <<")
        time.sleep(10)
        self.tap_element(L.menu.effect_layer_library)

    def switch_to_sticker_library(self):
        logger("start >> switch_to_sticker_library <<")
        time.sleep(10)
        self.tap_element(L.menu.sticker_library)

    def check_element_exists(self, locator):
        logger("start >> check_element_exists <<")
        # noinspection PyBroadException
        try:
            self.get_element(locator)
        except Exception:
            return False
        return True

    def check_element_not_exists(self, locator):
        logger("start >> check_element_not_exists <<")
        # noinspection PyBroadException
        try:
            self.get_element(locator)
        except Exception:
            return True
        return False

    def is_element_checked(self, locator):
        logger("start >> check_element_not_exists <<")
        try:
            value = self.el(locator).get_attribute('checked')
            logger(f"{locator} is checked:{value}")
            if value == 'true':
                return True
        except Exception:
            raise Exception
        return False
    
      
    def video_list_check_item(self, first_item, last_item): #check the list after sorted
        logger("start >> video_list_check_item <<")
        logger(f'fist element={self.get_element(L.library_gridview.first_caption).get_attribute("text")}')
        if self.get_element(L.library_gridview.first_caption).get_attribute('text') == first_item:
            logger(f'last element={self.get_element(L.library_gridview.last_caption).get_attribute("text")}')
            if self.get_element(L.library_gridview.last_caption).get_attribute('text') == last_item:
                return True
            else:
                return False
        else:
            return False
        '''# media name in library is removed in new version, use video duration to check items order.  
        logger(f'fist element={self.get_element(L.library_gridview.first_duration).get_attribute("text")}')
        if self.get_element(L.library_gridview.first_duration).get_attribute("text") == first_item:
            logger(f'last element={self.get_element(L.library_gridview.last_duration).get_attribute("text")}')
            if self.get_element(L.library_gridview.last_duration).get_attribute("text") == last_item:               
                return True
            else:
                return False
        else:
            return False
        '''

    
    def photo_list_check_item(self, first_item, last_item): #check the list after sorted
        logger("start >> photo_list_check_item <<")
        logger(f'fist element={self.get_element(L.library_gridview.first_caption).get_attribute("text")}')
        if self.get_element(L.library_gridview.first_caption).get_attribute('text') == first_item:
            logger(f'last element={self.get_element(L.library_gridview.last_caption).get_attribute("text")}')
            if self.get_element(L.library_gridview.last_caption).get_attribute('text') == last_item:
                return True
            else:
                return False
        else:
            return False
        
        '''# media name in library is removed in new version, add photo to timeline to check order. 
        first_item = f'[AID]TimeLinePhoto_{first_item}'
        last_item = f'[AID]TimeLinePhoto_{last_item}'
        self.el(L.library_gridview.first).click()
        logger('select first item in library')
        self.el(L.library_gridview.add).click()
        logger('add it to timeline')
        time.sleep(5)
        logger('sleep 5 sec')
        first_title = self.get_element(L.timeline.last_photo).get_attribute("content-desc")
        logger(f'fist element={first_title}')
        self.el(L.library_gridview.last).click()
        logger('select last item in library')
        self.el(L.library_gridview.add).click()
        logger('add it to timeline')
        time.sleep(5)
        logger('sleep 5 sec')
        last_title = self.get_element(L.timeline.last_photo).get_attribute("content-desc")
        logger(f'last element={last_title}')
        if first_title == first_item and last_title == last_item:   
            logger('items match expect')
            return True
        else:
            logger('items not match expect')
            return False
        '''

    def music_list_check_item(self, first_item, last_item): #check the list after sorted
        logger("start >> music_list_check_item <<")
        logger(f'fist element={self.get_element(L.library_listview.first_caption).get_attribute("text")}')
        if self.get_element(L.library_listview.first_caption).get_attribute('text') == first_item:
            logger(f'last element={self.get_element(L.library_listview.last_caption).get_attribute("text")}')
            if self.get_element(L.library_listview.last_caption).get_attribute('text') == last_item:
                return True
            else:
                return False
        else:
            return False

    def random_select_list_element(self, list):
        logger("start >> random_select_list_element <<")
        try:
            element = random.choice(list)
            logger(f"element: {element}")
        except Exception:
            logger("Random an element from list FAIL")
            raise Exception
        return element

    def google_drive_download_media(self, timeout=30): #use it after selected video/photo
        logger("start >> google_drive_download_media <<")
        try:
            self.el(L.library_gridview.download).click()
            time.sleep(2)
            is_complete = 0
            for retry in range(timeout-2):
                if not self.is_exist(L.library_gridview.cancel_download, 1):
                    is_complete = 1
                    break
                time.sleep(1)
            if is_complete == 0:
                logger("cancel_download still exists. Timeout.")
                raise Exception
        except Exception as e:
            logger(f"download media FAIL - {e}")
            raise Exception
        return True

    def google_drive_download_song(self, timeout=120): #use it after selected music
        logger("start >> google_drive_download_media <<")
        try:
            is_found = 0
            elm_target = ''
            elms = self.els(L.library_gridview.download)
            for elm in elms:
                if elm.get_attribute('enabled') == 'true':
                    is_found = 1
                    elm_target = elm
                    break
            if is_found == 0:
                logger("download button is not found")
                raise Exception
            elm_target.click()
            time.sleep(2)
            is_complete = 0
            for retry in range(timeout-2):
                if not self.is_exist(L.library_gridview.cancel_download, 1):
                    is_complete = 1
                    break
                time.sleep(1)
            if is_complete == 0:
                logger("cancel_download still exists. Timeout.")
                raise Exception
        except Exception as e:
            logger(f"download media FAIL - {e}")
            raise Exception
        return True

    def google_drive_check_download_file(self, device_id, name):
        import os
        logger("start >> google_drive_check_download_file <<")
        file_path = f'storage/emulated/0/PowerDirector/GoogleDrive/{google_drive_account}/{name}'
        logger(f'file = {file_path}')
        if not self.adb_check_file_exists(device_id, file_path):
            return False
        return True

    def google_drive_check_sign_in(self):
        logger("start >> google_drive_check_sign_in <<")
        try:
            self.el(("id", "com.google.android.gms:id/account_name")).click()
        except Exception:
            logger("google account has been sign in")
        return True

    def media_library_get_clips_amount(self):
        logger("start >> media_library_get_clips_amount <<")
        try:
            elms = self.els(L.library_listview.caption_song)
            amount = len(elms)
            logger(f"clips amount={amount}")
        except Exception:
            logger("get clips amount FAIL")
            raise Exception
        return amount

    def library_drag_video_clip_to_audio_track(self, name, track=1):
        logger("start >> library_drag_video_clip_to_audio_track <<")
        logger(f"clip name={name}, audio_track={track}")
        try:
            # audio track
            target_locator = E.timeline.track
            els_track = self.els(target_locator)
            el_target = els_track[track]
            logger("Get audio track ok")
            # media
            self.is_exist(L.library_gridview.frame, 30)
            frame = self.el(L.library_gridview.frame)
            el_media = frame.find_element_by_xpath(f'//*[contains(@text,"{name}")]')
            logger("Get media ok")
            action = TouchAction(self.driver.driver).long_press(el_media, x=0, y=0, duration=2000).wait(5000).move_to(el_target).release()
            action.perform()
        except Exception:
            logger("operation FAIL")
            raise Exception
        return True
        
    def get_picture_from_camera(self):
        logger("get picture from physical camera")
        aid = lambda id: ("accessibility id", id)
        xpath = lambda id: ("xpath", id)
        
        self.click(L.library_gridview.photo_capture)
        # depended on each device
        if self.udid == "ENU7N15B09000259":  # Nexus P6
            # locator
            shutter = aid('Shutter')
            done = aid('Done')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                if self.is_exist(shutter):
                    self.click(shutter)
                    time.sleep(3)
                if self.is_exist(done):
                    self.click(done)
                    time.sleep(5)
                if self.is_exist(L.library_gridview.add, 5):
                    is_complete = True
                    break
            return is_complete        
        elif self.udid == "ENU7N15B06006012":  # Nexus P6
            # locator
            shutter = aid('Shutter')
            done = aid('Done')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                if self.is_exist(shutter):
                    self.click(shutter)
                    time.sleep(3)
                if self.is_exist(done):
                    self.click(done)
                    time.sleep(5)
                if self.is_exist(L.library_gridview.add, 5):
                    is_complete = True
                    break
            return is_complete
        elif self.udid == '03157df3238b340f': # Samsung S6
            #locator
            shutter = xpath('(//GLButton[@content-desc="NONE"])[3]')
            done = ('id', 'com.sec.android.app.camera:id/okay')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                if self.is_exist(shutter):
                    self.click(shutter)
                    time.sleep(3)
                if self.is_exist(done):
                    self.click(done)
                    time.sleep(5)
                if self.is_exist(L.library_gridview.add, 5):
                    is_complete = True
                    break
            logger(f'is_complete={is_complete}')
            return is_complete
        elif self.udid == '463658535a423098': # Samsung S9+
            #locator
            shutter = xpath('(//GLButton[@content-desc="NONE"])[2]')
            done = ('id', 'com.sec.android.app.camera:id/okay')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                if self.is_exist(shutter):
                    self.click(shutter)
                    time.sleep(3)
                if self.is_exist(done):
                    self.click(done)
                    time.sleep(5)
                if self.is_exist(L.library_gridview.add, 5):
                    is_complete = True
                    break
            logger(f'is_complete={is_complete}')
            return is_complete              
        else:
            logger("Unable to get media from this device. : %s" % self.udid)
        raise Exception("[Error] Porting this device(%s) is required." % self.udid)

    def get_video_from_camera(self):
        logger("get video from physical camera")
        aid = lambda id: ("accessibility id", id)
        xpath = lambda id: ("xpath", id)
        
        #self.click(L.library_gridview.video_capture)
        # depended on each device
        if self.udid == "ENU7N15B09000259":  # Nexus P6
            # locator
            start = aid('Start Recording')
            stop = aid('Stop Recording')
            done = aid('Done')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                try:
                    if self.is_exist(start):
                        self.click(start)
                        time.sleep(10)
                    if self.is_exist(stop):
                        self.click(stop)
                        # time.sleep(3)
                    if self.is_exist(done, 10):
                        self.click(done)
                        # time.sleep(5)
                    if self.is_exist(L.library_gridview.add, 10):
                        is_complete = True
                        break
                except:
                    logger('While loop - exception. Retry.')
                    pass
            logger(f'is_complete={is_complete}')
            time.sleep(3)
            return is_complete        
        elif self.udid == "ENU7N15B06006012":  # Nexus P6
            # locator
            start = aid('Start Recording')
            stop = aid('Stop Recording')
            done = aid('Done')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                try:
                    if self.is_exist(start):
                        self.click(start)
                        time.sleep(10)
                    if self.is_exist(stop):
                        self.click(stop)
                        # time.sleep(3)
                    if self.is_exist(done, 10):
                        self.click(done)
                        # time.sleep(5)
                    if self.is_exist(L.library_gridview.add, 10):
                        is_complete = True
                        break
                except:
                    logger('While loop - exception. Retry.')
                    pass
            logger(f'is_complete={is_complete}')
            time.sleep(3)
            return is_complete
        elif self.udid == '03157df3238b340f':  # Samsung S6
            # locator
            record = xpath('(//GLButton[@content-desc="NONE"])[1]')
            stop_record = xpath('(//GLButton[@content-desc="NONE"])[2]')
            done = ('id', 'com.sec.android.app.camera:id/okay')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                try:
                    if self.is_exist(record):
                        self.click(record)
                        time.sleep(10)
                    if self.is_exist(stop_record):
                        self.click(stop_record)
                        # time.sleep(3)
                    if self.is_exist(done, 10):
                        self.click(done)
                        # time.sleep(5)
                    if self.is_exist(L.library_gridview.add, 10):
                        is_complete = True
                        break
                except:
                    logger('While loop - exception. Retry.')
                    pass
            logger(f'is_complete={is_complete}')
            time.sleep(3)
            return is_complete
        elif self.udid == '463658535a423098':  # Samsung S9+
            # locator
            record = xpath('(//GLButton[@content-desc="NONE"])[1]')
            stop_record = xpath('(//GLButton[@content-desc="NONE"])[2]')
            done = ('id', 'com.sec.android.app.camera:id/okay')
            # actions
            time.sleep(10)
            timer = time.time()
            is_complete = False
            while time.time() - timer < 60:
                try:
                    if self.is_exist(record):
                        self.click(record)
                        time.sleep(10)
                    if self.is_exist(stop_record):
                        self.click(stop_record)
                        # time.sleep(3)
                    if self.is_exist(done, 10):
                        self.click(done)
                        # time.sleep(5)
                    if self.is_exist(L.library_gridview.add, 10):
                        is_complete = True
                        break
                except:
                    logger('While loop - exception. Retry.')
                    pass
            logger(f'is_complete={is_complete}')
            time.sleep(3)
            return is_complete
        else:
            logger("Unable to get media from this device. : %s" % self.udid)
        raise Exception("[Error] Porting this device(%s) is required." % self.udid)

    def enter_google_drive(self,category = "photo",number = 3):
        logger('start enter_google_drive')
        self.select_media_by_text('Google Drive')
        self.google_drive_check_sign_in()
        if not self._in_google_driver(): return False
        self.select_media_by_text(category)
        clip_amount = self.media_library_get_clips_amount()
        return clip_amount == number

    def google_download_file(self):
        if not self._in_google_driver(): return False
        elm = self.get_first_media()
        # self.select_media_by_text(elm)
        self.google_drive_download_media()
        # return self.google_drive_check_download_file(self.device_udid, elm)
        return elm

    def check_pan_zoom_setting(self,category = "photo"):
        if not self._in_google_driver(): return False
        # add photo to timeline check pan zoom
        elm = self.get_first_media()
        # self.select_media_by_text(elm)
        self.el(L.library_gridview.add).click()
        self.timeline_select_media(elm, category)
        # snapshot > preview > snapshot > check diff.
        pic_before = self.get_preview_pic()
        el_playback = self.el(E.menu.play)
        el_playback.click()
        time.sleep(10)
        pic_after = self.get_preview_pic()
        result_different = CompareImage(pic_before, pic_after, 3).compare_image() == False
        return result_different

    def drag_google_clip(self,category = "Music"):
        if not self._in_google_driver(): return False
        elm = self.get_first_media()
        self.library_drag_video_clip_to_audio_track(elm)
        return self.timeline_check_media(elm, category)

    def _in_google_driver(self,timeout = 5):
        # if self.is_not_exist(L.library_gridview.refresh,timeout):
        if self.is_exist(L.menu.video_entry, timeout):
            logger('this is not google driver folder')
            return False
        return True
        
    def check_downloadable_music_name(self, name):
        logger('start >>>check_downloadable_music_name<<<')
        logger(f'try to find input: {name}')
        try:
            frame = self.el(L.library_listview.frame)
            element = frame.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]')
        except Exception:
            logger(f"Fail to locate element - {name}")
            raise Exception
        return True
        
    def search_video(self, name):
        logger("start search_video")
        logger(f"input name={name}")
        try:
            self.el(L.video_library.searchText).click()
            self.el(L.video_library.searchText).set_text(name)
            time.sleep(3)
            # TouchAction(self.driver.driver).press(None, 2215, 1360, 1).release().perform()
            # TouchAction(self.driver.driver).press(None, 1650, 1000, 1).release().perform()
            self.driver.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        except Exception:
            logger('exception occurs')
            raise Exception
        return True
        
    def download_video(self, timeout=120):
        logger("start download_video")
        try:
            for retry in range(20):
                if self.is_exist(L.library_gridview.download):
                    logger('Click Download...')
                    self.el(L.library_gridview.download).click()
                elif self.is_exist(L.library_gridview.add):
                    logger('Add button exist, already downloaded.')
                    return True
                else:
                    logger('Download button not exist...')
                    return False
                if self.is_exist(L.library_gridview.cancel_download, 5):
                    logger('Cancel Download button shows, wait downloading...')
                    if self.is_vanish(L.library_gridview.cancel_download, timeout):
                        logger('Download complete.')
                        return True
                    else:
                        logger('Timeout.')
                        return False
                else:
                    logger('Fail to start Download, retry again...')
            logger('Fail to download...')
            return False
        except Exception:
            logger('exception occurs')
            raise Exception

    def download_music(self, timeout=120):
        logger("start download_music")
        try:
            for retry in range(10):
                if not self.is_exist(L.library_listview.download_song, 1):
                    if self.is_exist(L.library_listview.add, 1):
                        logger('Add button is exist, no need to download.')
                        return True
                self.el(L.library_listview.download_song).click()
                logger('Click download...')
                if self.is_exist(L.library_gridview.cancel_download, 5):
                    logger('cancel_download shows, wait download complete...')
                    if self.is_vanish(L.library_gridview.cancel_download, timeout):
                        logger('cancel_download disappear, download complete.')
                        return True
                    else:
                        logger("cancel_download still exists. Timeout.")
                        return False
                else:
                    logger('Cannot start download process, retry again')
            logger('Fail to download_music')
            return False
        except Exception:
            logger('exception occurs')
            raise Exception

    def select_title_category(self,name, timeout=10):
        logger("start >> select_title_category<<")
        logger(f"input - {name}")
        try:
            self.is_exist(L.library_gridview.title_library_category_list, timeout)
            frame = self.el(L.library_gridview.title_library_category_list)
            locator = ("xpath", f'//*[contains(@text,"{name}")]')
            for retry in range(20):
                if not self.is_exist(locator):
                    self.driver.swipe_element(L.library_gridview.title_library_category_list, 'left', 300)
                else:
                    self.driver.swipe_element(L.library_gridview.title_library_category_list, 'left', 100)
                    break
            element = frame.find_element_by_xpath(f'//*[contains(@text,"{name}")]')
            if element.text != name:
                logger(f"locate incorrect element - {name}")
                raise Exception
            element.click()
        except Exception:
            logger(f"Fail to locate element - {name}")
            raise Exception
        return True       

    def search_template_by_image(self, name, timeout=30):
        logger("start search_template_by_image")
        logger(f"input - {name}")
        try:
            self.is_exist(L.library_gridview.frame)
            actions = TouchAction(self.driver.driver)
            template_img = f"{Path(__file__).parent.parent.absolute()}\\SFT\\template\\{self.udid}\\{name}.png"
            for retry in range(timeout):
                canvas = self.driver.save_pic()
                result = CompareImage(canvas, template_img, 9).search_image(order=2)
                if not result:
                    self.driver.swipe_element(L.library_gridview.frame, 'left', 300)
                    self.driver.swipe_element(L.library_gridview.frame, 'left', 300)
                    self.driver.swipe_element(L.library_gridview.frame, 'left', 300)
                    time.sleep(1)
                else:
                    logger(f"found template img match at: {result}")
                    actions.press(x=result[0],y= result[1]).release().perform()
                    break
            if self.is_exist(L.library_gridview.add):
                logger("Select template success")
                return True
            elif self.is_exist(L.library_gridview.download):
                logger('Download icon shows, Select template success')
                return True
            elif self.is_exist(L.library_gridview.icon_try_sticker):
                logger('Sticker frame shows, Select template success')
                return True
            elif self.is_exist(L.library_gridview.add_sticker):
                logger('Sticker add btn shows, Select template success')
                return True
            else:
                logger("No Add button, Select template Fail.")
                raise Exception
        except Exception:
            logger(f"Fail to search template")
            raise Exception
    
    def search_add_template_by_image(self, name, timeout=30):
        logger("start search_add_template_by_image")
        logger(f"input - {name}")
        try:
            self.is_exist(L.library_gridview.frame)
            actions = TouchAction(self.driver.driver)
            template_img = f"{Path(__file__).parent.parent.absolute()}\\SFT\\template\\{self.udid}\\{name}.png"
            is_complete = 0
            for retry in range(timeout):
                canvas = self.driver.save_pic()
                result = CompareImage(canvas, template_img, 9).search_image(order=2)
                if not result:
                    self.driver.swipe_element(L.library_gridview.frame, 'left', 300)
                    self.driver.swipe_element(L.library_gridview.frame, 'left', 300)
                    self.driver.swipe_element(L.library_gridview.frame, 'left', 300)
                    time.sleep(1)
                else:
                    logger(f"found template img match at: {result}")
                    actions.press(x=result[0],y= result[1]).release().perform()
                    is_complete = 1
                    break
            if is_complete == 1:
                logger("Select template success")
                return True
            else:
                logger("Search template Fail.")
                raise Exception
        except Exception:
            logger(f"Fail to search template")
            raise Exception

    def select_template_category(self,name, timeout=10):
        logger("start >> select_template_category<<")
        logger(f"input - {name}")
        try:
            self.is_exist(L.library_gridview.template_library_category_list, timeout)
            frame = self.el(L.library_gridview.template_library_category_list)
            locator = ("xpath", f'//*[contains(@text,"{name}")]')
            for retry in range(30):
                if not self.is_exist(locator, 1):
                    self.driver.swipe_element(L.library_gridview.template_library_category_list, 'left', 300)
                    self.driver.swipe_element(L.library_gridview.template_library_category_list, 'left', 300)
                else:
                    self.driver.swipe_element(L.library_gridview.template_library_category_list, 'left', 100)
                    break
            element = frame.find_element_by_xpath(f'//*[contains(@text,"{name}")]')
            if element.text != name:
                logger(f"locate incorrect element - {name}")
                raise Exception
            element.click()
        except Exception:
            logger(f"Fail to locate element - {name}")
            raise Exception
        return True

    def check_category_is_highlighted(self, name):
        logger("start >> check_category_is_highlighted <<")
        try:
            elm = self.el(L.library_gridview.template_library_category_list)
            locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
            for retry in range(10):
                if self.is_exist(locator):
                    result = elm.find_element_by_xpath(
                        f'//android.widget.TextView[contains(@text,"{name}")]').get_attribute('selected')
                    logger(f"Found {name} category = {result}")
                    return result
                else:
                    # elm.driver.swipe_left()
                    self.swipe_element(L.library_gridview.template_library_category_list, 'left', 300)
                    time.sleep(1)
            logger(f"Didn't find {name} category")
            raise Exception
        except Exception:
            raise Exception

    def add_video_template_to_timeline(self, target):
        logger(f"start >> add_video_template_to_timeline <<: {target}")
        try:
            is_premium = False
            if target == 'intro':
                locator = L.menu.add_as_intro
            else:
                locator = L.menu.add_as_outro
            self.el(L.library_gridview.add).click()
            time.sleep(5)
            if self.is_exist(L.menu.add_as_premium_warning):
                logger('Premium text shows.')
                is_premium = True
            if self.is_exist(locator):
                logger(f'click {target} button.')
                self.el(locator).click()
                return True, is_premium
            else:
                logger('Add template dialog not show.')
                raise Exception
        except Exception:
            raise Exception

    def play_music_in_library(self):
        logger(f"start >> play_music_in_library <<")
        try:
            if self.is_exist(L.library_listview.stop, 1):
                logger('Now playing, Stop first.')
                self.el(L.library_listview.stop).click()
            time.sleep(3)
            self.el(L.library_listview.play).click()
            if self.is_exist(L.library_listview.stop, 10):
                logger('Stop button shows, now playing.')
                return True
            else:
                logger('Stop button not shows.')
                return False
        except Exception:
            logger('play_music_in_library fail.')
            raise Exception
            
            
    def tap_favorite(self, index=0):    # tap favorite icon in music library by order (start from 0)
        logger("start >> tap_favorite <<")
        try:
            pic_old = self.driver.save_pic(self.el(L.library_listview.frame))
            fav_icons = self.els(L.library_listview.fav_icon)
            el_target = fav_icons[index]     
            el_target.click()
            time.sleep(3)
            pic_new = self.driver.save_pic(self.el(L.library_listview.frame))
            compare_result = CompareImage(pic_old,pic_new,7).compare_image()
            is_changed = True if not compare_result or compare_result == 100 else False
            return is_changed
        except Exception:
            raise Exception
            
    
    def check_gi_library_order(self):
        logger(f'start check_gi_library_order')
        try:
            elms = self.els(L.library_gridview.library_unit_layout)
            if len(elms) == 0:
                logger("list library fail")
                raise Exception
            width = int(len(elms)/3)
            logger(f"visible library items in list={len(elms)}, each row have {width} clips")
            elms_icon = self.els(L.gettyimages_premium.library_unit_purchasable)
            num = int(len(elms_icon))
            if num == 0:
                logger("list purchasable icons fail")
                raise Exception
            logger(f"visible purchasable icons={num}")
            for index in range(num):                    # Check $ icon is in correct thumbnail
                thumbnail_rect = elms[index+2].rect     # first 2 should be free
                icon_rect = elms_icon[index].rect
                if icon_rect['x'] > thumbnail_rect['x'] and icon_rect['x'] < (thumbnail_rect['x']+thumbnail_rect['width']) \
                        and icon_rect['y'] > thumbnail_rect['y'] and icon_rect['y'] < (thumbnail_rect['y']+thumbnail_rect['height']):
                    logger(f'Check icon {index} position OK.')
                else:
                    logger(f'Check icon {index} position FAIL.')
                    return False
            return True
        except Exception:
            raise Exception
    
    def check_filter_button_status(self):
        logger("start >> check_filter_button_status<<")
        try:
            element = self.el(L.library_gridview.btn_stock_filter)
            if element.get_attribute('enabled') == 'true':
                logger('Filter button is enabled.')
                return True
            else:
                logger('Filter button is not enabled.')
                return False
        except Exception:
            logger("check_filter_button_status fail")
            raise Exception
            
    def select_stock_category(self, name):
        logger(f"start >> select_stock_category<< {name}")
        try:
            frame = self.el(L.library_gridview.library_tabs_content)
            if name == 'shutterstock':
                locator = L.video_library.tab_video_shutterstock
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'right', 150)
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'right', 150)
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'right', 150)
            elif name == 'gettyimage':
                locator = L.video_library.tab_video_gettyimages
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'right', 150)
            elif name == 'gettyimage_premium':
                locator = L.video_library.tab_video_gettyimages_premium
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'left', 150)
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'left', 150)
            elif name == 'pixabay': 
                locator = L.video_library.tab_pixabay
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'left', 150)
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'left', 150)
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'left', 150)
                self.driver.swipe_element(L.library_gridview.library_tabs_content, 'left', 150)
            else:
                logger('incorrect name.')
                raise Exception
            self.el(locator).click()
            return True
        except Exception:
            logger(f"Fail to locate element - {name}")
            raise Exception
        