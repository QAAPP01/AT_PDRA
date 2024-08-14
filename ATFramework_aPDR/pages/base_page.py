# dummy module
import shutil
import time, os
import traceback
import uuid

import cv2
from os.path import dirname

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction

from PIL import Image

from ATFramework_aPDR.ATFramework.pages.base_page import *
from .locator import locator as L
from .locator.locator_type import *
from ATFramework_aPDR.ATFramework.utils.log import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ATFramework_aPDR.SFT.conftest import PACKAGE_NAME
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage
from ATFramework_aPDR.ATFramework.utils.compare import *
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER_01

class BasePage(BasePage):
    def __init__(self,*args,**kwargs):
        super(BasePage, self).__init__(*args, **kwargs)
        self.el = lambda id: self.driver.driver.find_element(id[0],id[1])
        self.els = lambda id: self.driver.driver.find_elements(id[0],id[1])
        self.el_find_string = lambda id: self.driver.driver.find_element('xpath','//*[contains(@text,"' + id + '")]')
        self.driver.driver.update_settings({"waitForIdleTimeout": 300})
        self.app_package = PACKAGE_NAME
        self.udid = self.driver.driver.desired_capabilities['deviceUDID']
        self.package_name = self.app_package
        # logger("PackageName = %s" % PACKAGE_NAME)

    def click(self, locator, timeout=5):
        try:
            element = self.element(locator, timeout)
            if element:
                element.click()
                logger(f"[Click] {locator}")
                return True
        except Exception:
            traceback.print_exc()
        return False

    def h_screenshot(self, locator=L.edit.preview.preview, crop=None):
        try:
            path = os.getenv('temp', os.path.dirname(__file__))
            file_save = "%s/%s.png" % (path, uuid.uuid4())

            element = self.h_get_element(locator)
            element.screenshot(file_save)

            if crop:
                rect = element.rect
                rect.update({"x": 0, "y": 0})

                with Image.open(file_save) as im:
                    for key in crop.keys():
                        rect.update({key: crop[key]})

                    im_crop = im.crop((rect['x'], rect['y'], rect['x'] + rect['width'], rect['y'] + rect['height']))
                    im_crop.save(file_save)

            path_save = os.path.abspath(file_save)
            logger(path_save)
            return path_save

        except Exception as err:
            logger(f"[Error] {err}")
            return False

    def h_full_screenshot(self):
        try:
            path = os.getenv('temp', os.path.dirname(__file__))
            file_save = "%s/%s.png" % (path, uuid.uuid4())

            screenshot = self.driver.driver.get_screenshot_as_png()
            with open(file_save, 'wb') as f:
                f.write(screenshot)

            path_save = os.path.abspath(file_save)
            logger(path_save)
            return path_save

        except Exception as err:
            logger(f"[Error] {err}")
            return False

    def get_picture(self, locator):
        path = os.getenv('temp', os.path.dirname(__file__))
        file_save = "%s/%s.png" % (path, uuid.uuid4())
        self.h_get_element(locator).screenshot(file_save)
        path_save = os.path.abspath(file_save)
        logger(path_save)
        return path_save

    def get_preview_pic(self, locator=L.edit.preview.preview):
        time.sleep(1)
        element = self.h_get_element(locator)
        for i in range(60):
            if not element.get_attribute('displayed') == 'true':
                time.sleep(2)
                element = self.h_get_element(locator)
        return self.get_picture(locator)

    def get_boundary_preview(self, locator=L.edit.pip_library.pip_object):
        time.sleep(1)
        element = self.h_get_element(locator)
        for i in range(60):
            if not element.get_attribute('displayed') == 'true':
                time.sleep(2)
                element = self.h_get_element(locator)
        return self.get_picture(locator)

    def get_library_pic(self):
        elem = self.el(L.import_media.library_gridview.library_rooms)
        logger("elem = %s" % str(elem.rect) )
        result = self.driver.save_pic(elem)
        return result
    def get_timeline_pic(self):
        elem = self.el(L.edit.timeline.timeline_area)
        logger("elem = %s" % str(elem.rect) )
        result = self.driver.save_pic(elem)
        return result
    def exist(self, locator, timeout=5):
        implicitly = self.driver.driver.implicitly_wait()
        self.driver.driver.implicitly_wait(0.1)
        wait = WebDriverWait(self.driver.driver, timeout)
        try:
            elem =  wait.until(EC.presence_of_element_located(locator), "Element is selected: " + str(locator))
        except:
            elem = None
            logger("ERROR: %s element does not exist" % str(locator))
        implicitly = self.driver.driver.implicitly_wait(implicitly)
        return elem
    def exist_click(self,locator,timeout=5):
        logger("locator / timeout = %s / %s" % (locator,timeout))
        elem = self.exist(locator,timeout)
        if elem: 
            elem.click()
            return elem
        return None
    def is_exist(self, locator, timeout=3):
        start = time.time()
        try:
            WebDriverWait(self.driver.driver, timeout).until(EC.presence_of_element_located(locator))
            # logger(f"[Found ({round(time.time()-start, 2)})] {locator}")
            return True
        except TimeoutException:
            logger(f"[No found ({round(time.time()-start, 2)})] {locator}")
            return False
        
    def is_not_exist(self,locator,timeout=5):
        logger("start is_not_exist")
        retry = 3
        while retry:
            try:
                implicitly = self.driver.driver.implicitly_wait()
                self.driver.driver.implicitly_wait(0.1)
                wait = WebDriverWait(self.driver.driver, timeout)
                break
            except Exception as e:
                logger(f"exception={e}")
                time.sleep(1)
        timer_start = time.time()
        result = False
        while time.time() - timer_start < timeout:
            try:
                elem = wait.until_not(EC.presence_of_element_located(locator), "Locator still exist: " + str(locator))
                result = True
                logger("[is_not_exist] Vanished:" + str(time.time() - timer_start))
                break
            except Exception as e:
                logger("is_not_exist] not Vanished:" + str(time.time() - timer_start))
                logger(f"exception: {e}")
        self.driver.driver.implicitly_wait(implicitly)
        return result
    def is_vanish(self,element,timeout=5):
        implicitly = self.driver.driver.implicitly_wait()
        self.driver.driver.implicitly_wait(0.1)
        result = self.driver.wait_until_element_not_exist(element,timeout)
        self.driver.driver.implicitly_wait(implicitly)
        return result
    def back(self):
        self.driver.driver.back()
    def is_in_page(self,targets,timeout = 5, interval=0.1):
        if type(targets[1]) == str: # if it is locator, change it to list(locator)
            targets = (targets,)    
        timer_start = time.time()
        while time.time()-timer_start < timeout:
            page_source = self.driver.driver.page_source
            for target in targets:
                if target[1] in page_source:
                    return True
            time.sleep(interval)
        return False
    def is_not_in_page(self,targets,timeout = 5, interval=0.5):
        if type(targets[1]) == str: # if it is locator, change it to list(locator)
            targets = (targets,)    
        timer_start = time.time()
        while time.time()-timer_start < timeout:
            page_source = self.driver.driver.page_source
            all_vanish=True
            for target in targets:
                if target[1] in page_source:
                    all_vanish = False
                    break
            if all_vanish:
                return True
            time.sleep(interval)
        return False
    def is_subscription_page(self):
        SUBSCRIPTION_PAGE = 'com.cyberlink.powerdirector.StorePageActivity'
        result = self.driver.driver.current_activity == SUBSCRIPTION_PAGE
        result |= self.is_exist(L.main.subscribe.three_month)
        return result
        
    def wait_tile_enabled(self,locator,timeout=5,interval=0.5):
        element = self.el(locator)
        timer_start = time.time()
        while time.time()-timer_start < timeout:
            if element.is_enabled():
                return True
            time.sleep(interval)
        return False
    def adb_check_file_exists(self, device_id, file_path):
        import subprocess
        logger("start >> adb_check_file_exists <<")
        logger(f'file_path={file_path}')
        command = f'adb -s {device_id} shell ls {file_path}'
        try:
            out_bytes = subprocess.check_output(command)
        except Exception:
            logger('file not exists')
            return False
        return True
    def clean_movie_cache(self):
        logger("clean movie cache")
        return self.remove_folder_list([
            'storage/emulated/0/PowerDirector/stabilized',
            'storage/emulated/0/PowerDirector/reversed',
            'storage/emulated/0/PowerDirector/converted',
            'storage/emulated/0/PowerDirector/color_preset',
            '/sdcard/DCIM/100PDR_Capture',
            '/sdcard/DCIM/Camera',
            ])
    def clean_projects(self):
        logger("clean projects")
        return self.remove_folder_list(["storage/emulated/0/PowerDirector/projects"])
        
    def clean_google_drive_cache(self):
        logger("clean_google_drive_cache")
        return self.remove_folder_list(["storage/emulated/0/PowerDirector/GoogleDrive"])
        
    def copy_produced_video(self):
        logger('copy one video to produced video path')
        gt_path = f"{os.path.abspath(dirname(dirname(__file__)))}\\SFT\\test_material\\{TEST_MATERIAL_FOLDER_01}"
        # command = f'adb -s {DRIVER_DESIRED_CAPS["udid"]} shell "mkdir -p {list_folder[0]};" & \
            # adb -s {DRIVER_DESIRED_CAPS["udid"]} push {gt_path}\\photo_color_preset_16_9.mp4 {list_folder[0]}/'
        # logger(command)
        # subprocess.call(command)
        target_path = f'/sdcard/Movies/cyberlink/PowerDirector/'
        self.shell(f'adb shell mkdir -p {target_path}')
        self.copy_folder_list([(f'{gt_path}\\photo_color_preset_16_9.mp4',target_path)])
    def copy_project(self,project_name):
        source_full_path = r'%s\SFT\projects\%s\.'% (dirname(dirname(__file__)),project_name)
        destination_path = '/sdcard/PowerDirector/projects/'
        self.shell('adb shell mkdir -p ' + destination_path)
        logger('copy project from %s ' % (source_full_path))
        return self.copy_folder_list([
            (source_full_path,"/sdcard/PowerDirector/projects/"),
            ])
    def copy_folder_list(self,list):
        try:
            for source, destination in list:
                command = f'adb -s {self.udid} push "{source}" {destination}'
                logger('copy file from "%s" --> %s'  % (source, destination ))
                self.shell(command)
            return True
        except Exception as e:
            logger("Remove files exception: %s" % str(e))
            return False
    def remove_folder_list(self,list):
        try:
            for folder in list:
                command = f'adb -s {self.udid} shell rm -r {folder}'
                logger('Remove folder = %s' % folder)
                self.shell(command)
            return True
        except Exception as e:
            logger("Remove files exception: %s" % str(e))
            return False
    def shell(self,command):
        import subprocess
        try:
            if not "adb -s " in command: command = command.replace("adb","adb -s %s" % self.udid)
            logger("shell: %s" % command)
            subprocess.call(command)
            return True
        except Exception as e:
            logger("shell fail : %s" % str(e))
            return False
    def shell_typeII(self, command):
        import subprocess
        try:
            if not "adb -s " in command: command = command.replace("adb", "adb -s %s" % self.udid)
            logger("shell_typeII: %s" % command)
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (stdoutput, erroutput) = p.communicate()
            return stdoutput.decode('UTF-8').replace('\r\n', '')
        except Exception as e:
            logger(f"shell fail : {str(e)}, erroutput: {erroutput}")
            return False
    def _terminate_app(self,package_name):
        retry = 10
        while retry > 0:
                try:
                    is_exist = self.driver.driver.terminate_app(package_name)
                    if not is_exist:
                        break
                except:
                    time.sleep(0.3)
                    retry -= 1
        logger('[Terminate] %s : %s' %(package_name , not is_exist ))
        return not is_exist
        
    def get_screen_pixel_rgb(self, x, y):
        '''
        from PIL import Image  # for python 3.x > pip install Pillow
        from io import BytesIO
        import base64
        try:
            screenshotBase64 = self.driver.driver.get_screenshot_as_base64()
            im = Image.open(BytesIO(base64.b64decode(screenshotBase64)))
            pix = im.load()
        except Exception:
            return False
        return pix[x, y]
        '''
        import base64
        import numpy as np
        import cv2
        try:
            screenshotBase64 = self.driver.driver.get_screenshot_as_base64()
            img_b64decode = base64.b64decode(screenshotBase64) 
            img_array = np.frombuffer(img_b64decode,np.uint8)
            img=cv2.imdecode(img_array,cv2.IMREAD_COLOR)[:,:,::-1]
            color_rgb = tuple(img[y,x])
            logger("screen pixel (%s,%s)= %s" % (x,y, str(color_rgb)))
        except Exception as e:
            logger("Exception : %s" % str(e))
            return None
        return color_rgb

    # def download_media(self,name,name2=None):
    #     logger(f"start download_media: {name} / {name2}")
    #     implicitly = self.driver.driver.implicitly_wait()
    #     self.driver.driver.implicitly_wait(3)
    #     try:
    #         self.click(find_string("Get More"))
    #     except:
    #         self.el_find_string("Music and Sound Clips").click()
    #     self.driver.driver.implicitly_wait(implicitly)
    #     time.sleep(1)
    #     retry = 3
    #     while retry:
    #         try:
    #             self.el_find_string(name).click()
    #             time.sleep(1)
    #             break
    #         except:
    #             retry -=1
    #             logger("Unable to click element, try again! {retry}")
    #     if retry == 0: raise Exception("Find elememt errpr.")
    #     if name2:   # download music/sound case
    #         self.el_find_string(name2).click()
    #         elems = self.els(L.import_media.library_listview.download_song)
    #         for elem in elems:
    #             if elem.get_attribute("enabled") == "true":
    #                 elem.click()
    #                 break
    #         result_has_subscription = bool(self.ad.get_ad_type())
    #         self.back()
    #         result_has_unlock_ad = bool(self.ad.get_ad_type())
    #         #if result_has_unlock_ad: self.back() # close watch ad to unlock
    #         return result_has_subscription, result_has_unlock_ad
    #     result_has_subscription = bool(self.ad.get_ad_type())
    #     time.sleep(1)
    #     self.back() # cancel subscription
    #     result_has_unlock_ad = 0 if not result_has_subscription else bool(self.ad.get_ad_type())
    #     ''' ## **unnecessary to download**
    #     import_media.click(L.ad.watch_ad_to_unlock)
    #     import_media.is_vanish(L.ad.count_down , 60) # AD should be 30sec only
    #     import_media.back()
    #     import_media.is_vanish(L.ad.progress_bar , 60) # wait till DL complete
    #     result_dl_package = bool (self.el_find_string("Disturbance"))
    #     '''
    #     if result_has_unlock_ad: self.back() # exit unload ad page
    #     time.sleep(1)
    #     self.back() # exit more page
    #     return result_has_subscription , result_has_unlock_ad

    def copy_custom_font(self,font_name):
        source_full_path = r'%s\SFT\custom_font\%s'% (dirname(dirname(__file__)),font_name)
        destination_path = 'storage/emulated/0/PowerDirector/fonts/custom/'
        self.shell('adb shell mkdir -p ' + destination_path)
        logger('copy project from %s ' % (source_full_path))
        return self.copy_folder_list([
            (source_full_path,"storage/emulated/0/PowerDirector/fonts/custom/"),
            ])

    def get_chrome_url(self):
        logger("start get_chrome_url")
        implicitly = self.driver.driver.implicitly_wait()
        self.driver.driver.implicitly_wait(10)
        is_exception = 0
        try:
            url = self.el(('id', 'com.android.chrome:id/url_bar')).text
        except Exception:
            logger("get url from chrome FAIL.")
            is_exception = 1
        self.driver.driver.implicitly_wait(implicitly)
        if is_exception == 1:
            raise Exception
        return url

    def ground_truth_photo(self,source,target,rate=7):
        _dir = dirname
        logger("start ground_truth")
        if isinstance(source, tuple): source = self.el(source) # convert to element
        source_path = self.driver.save_pic(source)
        gt_path = f"{os.path.abspath(_dir(_dir(__file__)))}\\SFT\\test_material\\{TEST_MATERIAL_FOLDER_01}\\"
        result = CompareImage(source_path, gt_path + target,rate).compare_image()
        logger(f"result = {result}" )
        return result
        
    def ground_truth_video(self,target,timeout = 60):
        _dir = dirname
        MOVIE_PATH = '/sdcard/Movies/cyberlink/PowerDirector/'
        gt_path = f"{os.path.abspath(_dir(_dir(__file__)))}\\SFT\\test_material\\{TEST_MATERIAL_FOLDER_01}\\"
        logger("start ground_truth_video")
        progress = self.el(L.produce.gallery.produce_page.progress_bar)
        _timeout = timeout * 1000 # 60min
        timer = time.time()
        while time.time()-timer < _timeout:
            if progress.text == "100.0" : break
            logger(f"progress: {progress.text}")
            time.sleep(3)
        else:
            logger( f"Produce video time out - {timeout} sec")
            raise Exception(f"Produce video time out - {timeout} sec")
        name= self.el(L.produce.gallery.produce_page.file_name).text
        temp_path = os.getenv('temp', os.path.dirname(__file__))
        command = f'adb pull "{MOVIE_PATH}/{name}" {temp_path}/'
        self.shell(command)
        logger(f"compare video: {temp_path}/{name} vs. gt_path+{target}")
        result = compare_video(f'{temp_path}/{name}' , gt_path + target)
        return result
        
    def timeline_select_media(self, file_name, type='Video'): # type=Video/ Photo/ Color/ Music
        logger("start >> timeline_select_media <<")
        logger(f"input - {file_name}")
        # noinspection PyBroadException
        try:
            if type == 'Video' or type == 'Photo':
                logger(f"media_aid=[AID]TimeLine{type}_{file_name}")
                self.get_element(aid(f'[AID]TimeLine{type}_{file_name}')).click()
            else:
                list_element = self.els(L.edit.timeline.clip_title)
                is_found = 0
                for element in list_element:
                    if element.get_attribute('text') == file_name:
                        element.click()
                        is_found = 1
                        break
                if is_found == 0:
                    return False
        except Exception:
            logger('get elements fail')
            return False
        return True

    def timeline_check_media(self, file_name, type='video', timeout=30): # type=Video/ Photo/ Music
        logger("start >> timeline_check_media <<")
        logger(f"input - {file_name}")
        # noinspection PyBroadException
        try:
            if type == 'video' or type == 'photo':
                logger(f"media_aid=[AID]TimeLine{type}_{file_name}")
                return self.h_is_exist(aid(f'[AID]TimeLine{type}_{file_name}'))
            else:
                for retry in range(timeout):
                    list_element = self.els(L.edit.timeline.clip_title)
                    is_found = 0
                    for element in list_element:
                        if element.get_attribute('text') == file_name:
                            is_found = 1
                            break
                    if is_found == 1:
                        break
                    else:
                        time.sleep(1)
        except Exception:
            logger('get elements fail')
            return False
        return True
        
    
    def get_video_information(self, file_name):
        logger(f'start get_video_information target = {file_name}')
        try:
            MOVIE_PATH = '/storage/emulated/0/Movies/cyberlink/PowerDirector'
            temp_path = f"{os.path.abspath(dirname(dirname(__file__)))}\\ProfileScan\\temp"
            command = f'adb pull "{MOVIE_PATH}/{file_name}" "{temp_path}\"'
            self.shell(command)
            time.sleep(10)
            target_video = f'{temp_path}/{file_name}'
            
            cv2video = cv2.VideoCapture(target_video)
            height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
            width  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH)
            logger(f"Video Dimension: height:{height} width:{width}")

            framecount = cv2video.get(cv2.CAP_PROP_FRAME_COUNT) 
            frames_per_sec = cv2video.get(cv2.CAP_PROP_FPS)
            duration = framecount / frames_per_sec
            logger(f"Video fps: {frames_per_sec}")
            logger(f"Video duration (sec): {duration}")
            
            logger(f"Deleting video on device...")
            self.remove_folder_list([MOVIE_PATH])
            time.sleep(10)
            
            return height, width, frames_per_sec
        except Exception:
            logger("Exception occurs")
            raise Exception

    # ==================================================================================================================
    # Function: h_get_element
    # Description: Get element with locator
    # Parameters: locator
    # Return: Located element of type WebElement
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================

    def h_get_element(self, locator, timeout=5):
        start = time.time()
        try:
            if type(locator) == tuple:  # convert from tuple to WebElement
                element = WebDriverWait(self.driver.driver, timeout).until(EC.presence_of_element_located(locator))
                # logger(f"[Found ({round(time.time() - start, 2)})] {locator}")
                return element
            else:
                return locator
        except TimeoutException:
            logger(f"[No found ({round(time.time()-start, 2)})] {locator}")
            return False

    def element(self, locator, timeout=5):
        start = time.time()
        try:
            if type(locator) == tuple:
                element = WebDriverWait(self.driver.driver, timeout).until(EC.presence_of_element_located(locator))
                # logger(f"[Found ({round(time.time() - start, 2)})] {locator}")
                return element
            else:
                return locator
        except TimeoutException:
            logger(f"[No found ({round(time.time()-start, 2)})] {locator}")
            return False

    # ==================================================================================================================
    # Function: h_get_elements
    # Description: Get elements with non-unique locator
    # Parameters: locator
    # Return: Located elements of type WebElement
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================
    def h_get_elements(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver.driver, timeout).until(EC.presence_of_element_located(locator))
            elements = self.driver.driver.find_elements(locator[0], locator[1])
            return elements
        except TimeoutException:
            logger(f"[Info] Cannot find {locator}")
            return False

    def elements(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver.driver, timeout).until(EC.presence_of_element_located(locator))
            elements = self.driver.driver.find_elements(locator[0], locator[1])
            return elements
        except TimeoutException:
            logger(f"[Info] Cannot find {locator}")
            return False

    def h_click(self, locator, timeout=5):
        try:
            element = self.h_get_element(locator, timeout)
            if not element:
                return False
            else:
                element.click()
                logger(f"[Click] {locator}")
                return True
        except Exception as err:
            logger(f'[Error] {err}')

    def h_is_exist(self, locator, timeout=3):
        start = time.time()
        try:
            # logger(locator)
            WebDriverWait(self.driver.driver, timeout).until(EC.presence_of_element_located(locator))
            logger(f"[Found ({round(time.time()-start, 2)})] {locator}")
            return True
        except TimeoutException:
            logger(f"[No found ({round(time.time()-start, 2)})] {locator}")
            return False

    def h_is_not_exist(self, locator, timeout=120):
        start = time.time()
        try:
            WebDriverWait(self.driver.driver, timeout).until_not(EC.presence_of_element_located(locator))
            logger(f"[Disappear ({round(time.time() - start, 2)})] {locator}")
            return True
        except TimeoutException:
            logger(f"[Still Exist ({round(time.time() - start, 2)})] {locator}")
            return False

    def h_is_child_id_exist(self, parent, child, timeout=3):
        start = time.time()
        try:
            elem_parent = self.h_get_element(parent)
            if not elem_parent:
                logger(f"[No found parent element({round(time.time() - start, 2)})] {parent}")
                return False
            else:
                WebDriverWait(elem_parent, timeout).until(EC.presence_of_element_located(child))
            return True
        except TimeoutException:
            logger(f"[No found ({round(time.time()-start, 2)})] {child}")
            return False

    # ==================================================================================================================
    # Function: h_tap
    # Description: Tap location
    # Parameters: x axis, y axis
    # Return: N/A
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================
    def h_tap(self, x, y):
        actions = ActionChains(self.driver.driver)
        actions.w3c_actions = ActionBuilder(self.driver.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    # ==================================================================================================================
    # Function: h_long_press
    # Description: Long press element
    # Parameters: element or locator
    # Return: N/A
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================
    def h_long_press(self, locator, duration=1):
        try:
            element_rect = self.h_get_element(locator).rect
            x = element_rect["x"] + element_rect['width'] / 2
            y = element_rect["y"] + element_rect['height'] / 2
            actions = ActionChains(self.driver.driver)
            actions.w3c_actions = ActionBuilder(self.driver.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(duration)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        except Exception as err:
            logger(f'[Error] {err}')

    # ==================================================================================================================
    # Function: h_swipe_element
    # Description: Swipe from element_B to element_A
    # Parameters: locator or WebElement (returned from find_element), speed (1 is fastest)
    # Return: True/False
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================
    def h_swipe_element(self, element_b, element_a, speed=10):
        element_b = self.h_get_element(element_b)
        element_a = self.h_get_element(element_a)
        try:
            if speed < 1:
                speed = 1
            element_b_rect = element_b.rect
            start_x = element_b_rect['x']
            start_y = element_b_rect['y']
            element_a_rect = element_a.rect
            end_x = element_a_rect['x']
            end_y = element_a_rect['y']

            x_offset = (start_x - end_x) / speed
            y_offset = (start_y - end_y) / speed

            actions = ActionChains(self.driver.driver)
            actions.w3c_actions = ActionBuilder(self.driver.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
            actions.w3c_actions.pointer_action.pointer_down()

            for i in range(speed):
                start_x = int(start_x - x_offset)
                start_y = int(start_y - y_offset)
                actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            return True
        except Exception as err:
            logger(f"[Error] {err}")
            return False

    def h_swipe_location(self, start_x, start_y, end_x, end_y, speed=10, duration=0):
        """
        # Function: h_swipe_location
        # Description: Swipe from location to location
        # Parameters: start_x: x-coordinate at which to start
        #             start_y: y-coordinate at which to start
        #             end_x: x-coordinate at which to stop
        #             end_y: y-coordinate at which to stop
        #             speed: 1 is fastest
        #             duration: Waiting time to take the swipe, in ms.
        #             x_offset: offset of x-coordinate to away from the edge
        # Return: None
        # Note: N/A
        # Author: Hausen
        """
        try:
            actions = ActionChains(self.driver.driver)
            actions.w3c_actions = ActionBuilder(self.driver.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
            # TODO: speed

            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(duration / 1000)
            actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
            actions.w3c_actions.pointer_action.pause(duration / 1000)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            return self  # type: ignore
        except Exception as err:
            logger(f"[Error] {err}")
            return False

    def h_swipe_element_to_location(self, locator, end_x, end_y=None, speed=2, duration=0):
        """
        # Function: h_swipe_element_to_location
        # Description: Swipe element to location
        # Parameters:
            :param locator: element going to swipe
            :param end_x: x-coordinate at which to stop
            :param end_y: y-coordinate at which to stop
            :param speed: 1 is fastest
            :param duration: Waiting time to take the swipe, in s.
        # Return: Boolean
        # Note: N/A
        # Author: Hausen
        """
        try:
            element = self.h_get_element(locator)
            element_rect = element.rect
            start_x = element_rect['x'] + element_rect['width'] / 2
            start_y = element_rect['y'] + element_rect['height'] / 2
            if end_y is None:
                end_y = start_y

            actions = ActionChains(self.driver.driver)
            actions.w3c_actions = ActionBuilder(self.driver.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(duration)
            actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
            actions.w3c_actions.pointer_action.pause(duration)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            return True
        except Exception as err:
            logger(f"[Error] {err}")
            return False

    def h_swipe_playhead(self, x: int, speed=15):
        """
        # Function: h_swipe_playhead
        # Description: Swipe the playhead to location
        # Parameters:
            :param x: x-coordinate of destination
            :param speed: speed: 1 is fastest
        # Return: None
        # Note: length of x to trigger swiping is 25
        # Author: Hausen
        """
        try:
            if speed < 1:
                speed = 1
            playhead = self.h_get_element(L.edit.timeline.playhead).rect
            playhead_x = playhead["x"]+playhead["width"]//2
            ruler = self.h_get_element(L.edit.timeline.timeline_ruler).rect
            y = ruler["y"]+ruler["height"]//2
            temp_x = x

            x_split = (x - playhead_x) // speed

            actions = ActionChains(self.driver.driver)
            actions.w3c_actions = ActionBuilder(self.driver.driver,
                                                mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x, y).pointer_down()

            for i in range(speed):
                temp_x = int(temp_x - x_split)
                actions.w3c_actions.pointer_action.move_to_location(temp_x, y)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            return True
        except Exception as err:
            logger(f"[Error] {err}")
            return False

    # ==================================================================================================================
    # Function: h_drag_element
    # Description: Drag element
    # Parameters: locator
    # Return: Boolean
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================
    def h_drag_element(self, locator, end_x, end_y):
        try:
            element_rect = self.h_get_element(locator).rect
            start_x = element_rect['x'] + element_rect['width'] // 2
            start_y = element_rect['y'] + element_rect['height'] // 2
            actions = ActionChains(self.driver.driver)
            actions.w3c_actions = ActionBuilder(self.driver.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location((start_x + end_x)//2, (start_y + end_y)//2)
            actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            return True
        except Exception as err:
            logger(f"[Error] {err}")
            return False


    def copy_file(self, source_file, dest):
        """
        # Function: copy_database_file
        # Description: Copy file
        # Parameters:
            :param source_file
            :param dest: destination
        # Returns: bool

        """
        try:
            tgt_folder = os.path.dirname(dest)
            if not os.path.exists(tgt_folder):
                os.makedirs(tgt_folder)
            shutil.copy(source_file, dest)
            return True
        except Exception as err:
            logger(f'\n[Error]{err}')
            return False


