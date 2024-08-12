import sys, time, os
import traceback
from telnetlib import EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from ATFramework_aPDR.pages.base_page import BasePage
from ATFramework_aPDR.ATFramework.utils.extra import element_exist_click
from ATFramework_aPDR.ATFramework.utils.log import logger
import subprocess
from pathlib import Path
from appium.webdriver.common.touch_action import TouchAction
from ATFramework_aPDR.pages.locator import locator as L
from .locator.locator_type import *
from .locator.locator import edit as E
from .locator.locator import import_media as I
from ATFramework_aPDR.SFT.conftest import PACKAGE_NAME

pdr_package = PACKAGE_NAME


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        BasePage.__init__(self, *args, **kwargs)
        self.shortcut = Shortcut(self)

    def initial(self):
        logger("Waiting for permission_file_ok")
        print("driver = ", self.driver)
        element_exist_click(self.driver, L.main.permission.file_ok, 2)
        logger("Waiting for permission_photo_allow")
        element_exist_click(self.driver, L.main.permission.photo_allow, 2)

    def subscribe(self):
        self.click(L.main.menu.menu)
        if self.is_exist(L.main.menu.iap_banner, 1):
            self.click(L.main.menu.back)
            self.click(L.main.subscribe.entry)
            self.click(L.main.subscribe.continue_btn)
            self.click(('class name', 'android.widget.Button'))
            self.click(find_string('Not now'), 5)
            self.click(id('iv_close'), 2)  # close the credit dialog
            if self.is_exist(L.main.new_project, 10):
                return True
            else:
                raise

        else:
            self.click(L.main.menu.back)
        return True

    def enter_launcher(self):
        try:
            # 1st Launch
            if self.click(L.main.permission.gdpr_accept, 1):
                self.click(L.main.premium.iap_back, 15)
                self.click(id('iv_close'))  # close the credit dialog
                if self.is_exist(L.main.launcher.home):
                    logger('Enter Launcher Done')
                else:
                    logger('Enter Launcher Fail', log_level='error')
                    return False
            # 2nd Launch
            else:
                if self.is_exist(L.main.permission.loading_bar, 1):
                    self.h_is_not_exist(L.main.permission.loading_bar, 120)
                if self.is_exist(L.main.tutorials.close_open_tutorial, 1):
                    self.h_click(L.main.tutorials.close_open_tutorial)
                    self.click(L.main.premium.iap_back, 1)
                else:
                    # Churn Recovery
                    if self.h_is_exist(L.main.premium.pdr_premium, 1):
                        self.driver.driver.back()
                    else:
                        # IAP
                        self.click(L.main.premium.iap_back, 1)

            self.subscribe()
            logger('Enter Launcher Done')
            return True

        except Exception:
            traceback.print_exc()
            return False

    def relaunch(self):
        try:
            self.driver.close_app()
            self.driver.launch_app()
            self.enter_launcher()
            return True
        except Exception:
            traceback.print_exc()
            return False

    def enter_shortcut(self, name):

        if not self.is_exist(L.main.shortcut.shortcut_name(name), 1):
            self.click(xpath('//*[@text="More"]'))
        if self.click(L.main.shortcut.shortcut_name(name)):
            return True
        else:
            logger(f'[Error] Cannot find the shortcut "{name}"', 'error')
            return False

    def enter_ai_feature(self, name):
        if self.click(find_string(name), 2):
            return True
        else:
            last = ""
            while 1:
                features = self.elements(L.main.ai_creation.feature_name(0))
                if features[-1].text == last:
                    logger(f'No feature "{name}"', log_level='error')
                    return False
                else:
                    last = features[-1].text
                    self.h_swipe_element(features[-1], features[0], 3)
                    if self.click(find_string(name), 2):
                        return True

    def shortcut_produce(self):
        try:
            self.click(L.main.shortcut.export)
            self.click(L.main.shortcut.produce)
            for i in range(120):
                if self.is_exist(L.main.shortcut.produce_progress_bar, 1):
                    time.sleep(1)
                else:
                    break
            if self.is_exist(L.main.shortcut.produce_full_editor):
                return True
            else:
                logger("Produce uncompleted")
                return False
        except:
            traceback.print_exc()
            return False

    def change_UI_mode(self, mode):
        try:
            mode = mode.lower()
            if mode not in ["portrait", "landscape", "auto-rotate"]:
                raise ValueError
            self.h_click(L.main.menu.menu)
            self.h_click(L.main.menu.preference)
            current_mode = self.h_get_element(L.timeline_settings.preference.current_UI_mode_text).text.lower()
            if current_mode != mode:
                self.h_click(L.timeline_settings.preference.current_UI_mode_text)
                self.h_click(L.timeline_settings.preference.UI_mode(mode))
                self.h_click(L.timeline_settings.preference.back)
                current_mode = self.h_get_element(L.timeline_settings.preference.current_UI_mode_text).text.lower()
            self.h_click(L.timeline_settings.preference.back)
            self.h_click(L.main.menu.back)
            return current_mode

        except ValueError:
            logger('[Error] UI mode input is incorrect')
        except Exception as err:
            logger(f'[Error] {err}')

    def enter_timeline(self, project_name=None, skip_media=True):
        def enter_exist_project():
            if self.click(find_string(project_name), 2):
                logger(f'[Info] Enter project: {project_name}')
                return True
            else:
                project_displayed = self.h_get_elements(L.main.project.project_name(0))
                for retry in range(30):
                    last = project_displayed[-1].text
                    self.h_swipe_element(project_displayed[-1], project_displayed[0], 3)
                    if self.click(find_string(project_name), 2):
                        logger(f'[Info] Enter project: {project_name}')
                        return True
                    else:
                        project_displayed = self.h_get_elements(L.main.project.project_name(0))
                        if project_displayed[-1].text == last:
                            logger(f'[Warning] Cannot find the project: {project_name}')
                            logger(f'[Info] New a project')
                            self.click(L.main.project.new_project, 2)
                            return False
                logger(f'[Warning] Reach the maximum setting for search project')
                logger(f'[Info] New a project')
                self.click(L.main.project.new_project, 2)
                return False

        try:
            if project_name:
                self.click(L.main.project.entry)
                enter_exist_project()
            else:
                self.h_click(L.main.project.new_project, 2)
            if skip_media:
                self.h_click(L.import_media.media_library.back)
                if self.h_is_exist(L.edit.preview.movie_view, 1):
                    logger('[Done] Enter Timeline Done')

                    return True
                else:
                    logger('\n[Fail] Enter Timeline Fail')
                    return False
            else:
                if self.h_is_exist(L.edit.preview.movie_view, 2):
                    logger('[Done] Enter Timeline Done')

                    return True
                else:
                    if self.h_is_exist(L.import_media.media_library.media(0)):
                        logger('[Done] Enter Timeline Done')

                        return True
                    else:
                        logger('\n[Fail] Enter Timeline Fail')
                        return False

        except Exception as err:
            logger(f"[Error] {err}")
            return False

    def project_click_empty(self):
        # self.click_element(self._project_empty)
        self.click_element(L.project.empty)
        return self.wait_until_element_exist(L.project.name, 10)

    def project_click_created(self, index):
        self.get_elements(L.project_created)[index].click()
        return self.wait_until_element_not_exist(L.project.new)

    def project_click_new(self):
        try:
            logger("start >> project_click_new <<")
            for retry in range(5):
                if self.is_exist(L.project.header_exclusive_offer, 5):
                    logger("exclusive_offer dialog show, try relaunch app")
                    self._terminate_app(pdr_package)
                    self.driver.driver.activate_app(pdr_package)
                    time.sleep(5)
                if self.is_exist(L.project.new, 30):
                    logger("new project button exists")
                    self.click(L.project.new)
                    if self.is_exist(L.project.name, 10):
                        break
                    else:
                        logger("L.project.name does not show, try relaunch app")
                        self._terminate_app(pdr_package)
                        self.driver.driver.activate_app(pdr_package)
                        time.sleep(5)
                else:
                    logger("L.project.new does not exist, try relaunch app")
                    self._terminate_app(pdr_package)
                    self.driver.driver.activate_app(pdr_package)
                    time.sleep(5)
            if not self.is_exist(L.project.name, 10):
                logger("L.project.name does not exist")
                raise Exception
        except Exception as err:
            logger(f"[Exception Error] {err}")
            raise Exception
        return True

    def project_select_with_correct_setting(self, name, duration=None):
        logger("start select project: %s " % name)
        self.select_existed_project_by_title(name)
        time.sleep(2)
        result = self.el(L.project_info.project_title).text == name
        if duration:
            result &= self.el(L.project_info.duration).text == duration
        if not result: raise  # wrong projects?
        self.el(L.project_info.btn_edit_project).click()
        return result

    def project_set_name(self, name):
        # logger("start >> project_set_name <<")
        # self.h_get_element(L.main.project.name).send_keys(name)
        pass

    def project_set_ratio(self, ratio='16_9'):
        if ratio == '9_16':
            self.h_click(L.main.project.ratio_9_16)
        elif ratio == '1_1':
            self.h_click(L.main.project.ratio_1_1)
        elif ratio == '21_9':
            self.h_click(L.main.project.ratio_21_9)
        elif ratio == '4_5':
            self.h_click(L.main.project.ratio_4_5)
        else:
            self.h_click(L.main.project.ratio_16_9)

    def project_set_16_9(self):
        logger("start >> project_set_16_9 <<")
        self.tap_element(L.setting.ratio_16_9)

    def project_set_9_16(self):
        logger("start >> project_set_9_16 <<")
        self.tap_element(L.setting.ratio_9_16)

    def project_set_1_1(self):
        logger("start >> project_set_1_1 <<")
        self.tap_element(L.setting.ratio_1_1)

    def project_click_ok(self):
        logger("start >> project_click_ok <<")
        self.tap_element(L.setting.ok)

    def project_set_to_landscape_mode(self, dont_ask=True):
        logger("start >> project_set_to_landscape_mode <<")
        if dont_ask == True:
            self.tap_element(L.project.dont_ask_mode)
        self.tap_element(L.project.landscape_mode)
        time.sleep(3)
        self.tap_element(L.project.btn_ok)

    def project_set_to_portrait_mode(self, dont_ask=True):
        logger("start >> project_set_to_portrait_mode <<")
        if dont_ask == True:
            self.tap_element(L.project.dont_ask_mode)
        self.tap_element(L.project.portrait_mode)
        time.sleep(3)
        self.tap_element(L.project.btn_ok)

    def check_edit_mode_ready(self):
        logger("start >> check_edit_mode_ready <<")
        if self.wait_until_element_exist(I.menu.back, 5) is None:
            return False
        return True

    def project_check_default_project_name(self):
        import datetime
        # logger("start >> get_default_project_name <<")
        dt = datetime.datetime.today()
        project_name_default = 'Project {:02d}-{:02d}'.format(dt.month, dt.day)
        project_name = self.get_text(L.main.project.name).decode("utf-8")
        if project_name != project_name_default:
            logger(f'[Info] Project Name: {project_name}')
            logger(f'[Info] Default Project Name: {project_name_default}')
            logger('\n[Fail] Project Name incorrect')
            return False
        else:
            logger(f'[Pass] Project Name: {project_name}')
            return True

    def project_create_new(self, ratio="16:9", type="video"):
        from pages.page_factory import PageFactory
        from .locator.locator import import_media as L_media
        import_media = PageFactory().get_page_object("import_media", self.driver)
        edit = PageFactory().get_page_object("edit", self.driver)

        for retry in range(3):
            if self.is_exist(L.project.new, 30):
                logger("new project button exists")
                break
            else:
                logger("L.project.new does not exist, try relaunch app")
                self._terminate_app(pdr_package)
                self.driver.driver.activate_app(pdr_package)
                time.sleep(5)

        if not self.is_exist(L.project.new):
            logger('Not found New Project button')
            retry = 0
            while (retry < 4):
                if self.is_exist(L.project.new, 3):
                    logger("Found New Project button")
                    break
                else:
                    logger("try to swipe up")
                    edit.swipe_element(L.project.new_launcher_scroll, "down", 200)
                    retry += 1
        elem = self.is_exist(L.project.empty)
        time.sleep(2)
        if elem:  # No created project case
            logger("No created project is found")
            self.exist(L.project.empty).click()
        else:  # With created project case
            logger("Found created project")
            self.click(L.project.new_existed_created)
        if ratio == "9:16":
            self.click(L.setting.ratio_9_16)
        else:
            self.click(L.setting.ratio_16_9)
        if type.lower() == "photo":
            logger("Select Photo: %s" % str(L_media.menu.photo_entry))
            import_media.click(L_media.menu.photo_entry)
            import_media.select_media_by_text("00PDRa_Testing_Material")
            # import_media.select_media_by_text("jpg.jpg")
            import_media.select_media_by_order(2)
            import_media.click(L_media.library_gridview.add)
            photo = self.el(E.timeline.clip_photo)
            photo.click()
            edit.adjust_clip_length(E.timeline.clip_photo, "end", "right", 500)
            photo.click()
            edit.swipe_element(E.timeline.clip_photo, "right", photo.rect['width'])
        elif type.lower() == "audio":
            logger("Select Audio : %s" % str(L_media.menu.music_library))
            import_media.click(L_media.menu.music_library)
            import_media.select_media_by_text("00PDRa_Testing_Material")
            import_media.select_song_by_text("mp3.mp3")
            elems_add = self.els(L_media.library_gridview.add)
            for elem in elems_add:
                if elem.get_attribute("enabled").lower() == 'true':
                    elem.click()
            analyzing_timeout = 10 * 60  # 10 min
            analyzing_timer = time.time()
            while True:
                clip_name = self.el(E.timeline.item_view_title).text
                analyzing = "%" in clip_name
                logger("clip name / analyzing= %s / %s" % (clip_name, str(analyzing)))
                if not analyzing: break
                time.sleep(5)
                time_elapsed = time.time() - analyzing_timer
                if time_elapsed > analyzing_timeout: raise "*Analyzing clip timeout* - %s" % str(time_elapsed)
            logger("return to edit page")
            self.driver.driver.back()
            self.driver.driver.back()
        else:
            import_media.select_media_by_text("00PDRa_Testing_Material")
            if ratio == "16:9":  # select different clip to force execute stabilizer & reverser
                # import_media.select_media_by_text("slow_motion.mp4")
                import_media.select_media_by_order(3)
            else:
                # import_media.select_media_by_text("mp4.mp4")
                import_media.select_media_by_order(1)
            import_media.click(L_media.library_gridview.add)

    # Menu
    def enable_file_name(self):
        self.h_click(L.main.menu.menu)
        self.h_click(L.main.menu.preference)
        while not self.h_is_exist(L.main.menu.display_file_name_switch, 1):
            elements = self.h_get_elements(('xpath', '//android.widget.LinearLayout'))
            self.h_swipe_element(elements[len(elements) - 1], elements[0])
        if self.h_get_element(L.main.menu.display_file_name_switch).get_attribute('checked') == 'false':
            self.h_click(L.main.menu.display_file_name_switch)

    def new_launcher_enter_tutorials(self):
        logger("start >>new_launcher_enter_tutorials<<")
        # find tutorials & scroll up  max 4 times
        for retry in range(3):
            if self.is_exist(L.project.new, 30):
                logger("L.project.new is exist, continue")
                break
            else:
                logger("L.project.new does not exist, try relaunch app")
                self._terminate_app(pdr_package)
                self.driver.driver.activate_app(pdr_package)
                time.sleep(5)

        for retry in range(4):
            if self.is_exist(L.project.tutorials, 3):
                logger("Found tutorials entry")
                self.click(L.project.tutorials)
                time.sleep(10)
                return True
            else:
                logger("swipe up")
                self.driver.swipe_up()
                retry += 1
        return False

    def new_launcher_enter_produced_video(self):
        logger("start >>new_launcher_enter_produced_video<<")
        # find tutorials & scroll up  max 4 times
        for retry in range(3):
            if self.is_exist(L.project.new, 30):
                logger("L.project.new is exist, continue")
                break
            else:
                logger("L.project.new does not exist, try relaunch app")
                self._terminate_app(pdr_package)
                self.driver.driver.activate_app(pdr_package)
                time.sleep(5)
        for retry in range(4):
            if self.is_exist(L.project.btn_produced_videos, 3):
                logger("Found entry")
                self.click(L.project.btn_produced_videos)
                return True
            else:
                logger("swipe up")
                self.driver.swipe_up()
                retry += 1
        return False

    def click_tutorials(self, name):
        logger("[%s] " % name)

        # find tutorials & scroll left  max 3 times
        retry = 0
        while (retry < 3):
            locator = ('xpath', '//*[contains(@text,"' + name + '")]')
            if self.is_exist(locator, 3):
                logger("Found [%s]" % name)
                break
            else:
                logger("swipe left")
                self.driver.swipe_left()
                retry += 1

        self.click(find_string(name))
        if name == "Frequently asked questions":
            logger("#Browser case#")
            el = self.el_find_string('cyberlink.com/faq')
            self.driver.driver.back()
            return True if el else False

        logger("#Youtube case#")
        time.sleep(4)
        youtube_view = self.el(L.tutorials.youtube_view)
        result_youtube = True if youtube_view else False
        self.driver.driver.back()

        result_no_network = False
        try:
            self.driver.driver.set_network_connection(4)
            time.sleep(10)
            logger("<no network>")
            self.click(find_string(name))
            time.sleep(10)
            check_no_network = self.el_find_string('No connection')
            result_no_network = True if check_no_network else False
        except:
            logger('error found, resume network status')
            self.driver.driver.set_network_connection(6)
            time.sleep(10)
            self.driver.driver.back()
            raise
        self.driver.driver.set_network_connection(6)
        time.sleep(3)
        self.driver.driver.back()
        time.sleep(1)
        return result_youtube, result_no_network

    def check_existed_project_by_title(self, title):
        logger("start >> check_existed_project_by_title <<")
        try:
            elements = self.els(L.project.txt_project_title)
            is_found = 0
            for item in elements:
                if item.get_attribute("text") == title:
                    is_found = 1
                    break
        except Exception:
            logger(f"Search project by title-{title} FAIL")
            return False
        if is_found == 0:
            logger(f"Search project by title-{title} FAIL. No match item")
            return False
        return True

    def select_existed_project_by_title(self, title):
        logger("start >> select_existed_project_by_title <<")
        try:
            elements = self.els(L.project.txt_project_title)
            is_found = 0
            for item in elements:
                if item.get_attribute("text") == title:
                    is_found = 1
                    item.click()
                    break
        except Exception:
            logger(f"Select project by title-{title} FAIL")
            raise Exception
        if is_found == 0:
            logger(f"Select project by title-{title} FAIL. No match item")
            raise Exception
        return True

    def reset_project_list(self, device_udid, package, project_name, under_android_11=False):  # project_name=16_9, 9_16, 1_1
        logger("start >> reset_project_list <<")
        try:
            self.driver.stop_app(package)
            logger("stop app <<")
            if under_android_11:
                # remove project folder
                command = f'adb -s {device_udid} shell rm -r "storage/emulated/0/PowerDirector/projects"'
                subprocess.call(command)
                # mkdir project folder
                command = f'adb -s {device_udid} shell mkdir "storage/emulated/0/PowerDirector/projects"'
                subprocess.call(command)
                # push project file
                list_file = ['.projlist', f'{project_name}.pdrproj']
                for file in list_file:
                    file_path = f"{Path(__file__).parent.parent.absolute()}\\SFT\\projects\\{project_name}\\{file}"
                    command = f'adb -s {device_udid} push "{file_path}" "/storage/emulated/0/PowerDirector/projects/"'
                    print(command)
                    subprocess.call(command)

            else:
                # remove project folder
                command = f'adb -s {device_udid} shell rm -r "storage/emulated/0/Android/data/com.cyberlink.powerdirector.DRA140225_01/files/projects"'
                subprocess.call(command)
                # mkdir project folder
                command = f'adb -s {device_udid} shell mkdir "storage/emulated/0/Android/data/com.cyberlink.powerdirector.DRA140225_01/files/projects"'
                subprocess.call(command)
                # push project file
                list_file = ['.projlist', f'{project_name}.pdrproj']
                for file in list_file:
                    file_path = f"{Path(__file__).parent.parent.absolute()}\\SFT\\projects\\{project_name}\\{file}"
                    command = f'adb -s {device_udid} push "{file_path}" "/storage/emulated/0/Android/data/com.cyberlink.powerdirector.DRA140225_01/files/projects/"'
                    print(command)
                    subprocess.call(command)
        except Exception:
            raise Exception
        logger("re-start app <<")
        self.driver.start_app(package)
        return True

    def add_project_list(self, device_udid, package, project_name):  # project_name=16_9, 9_16, 1_1
        logger("start >> reset_project_list <<")
        try:
            self.driver.stop_app(package)
            logger("stop app <<")

            # pull .projlist
            device_path = 'storage/emulated/0/Android/data/com.cyberlink.powerdirector.DRA140225_01/files/projects/'
            temp_folder = os.getenv('temp', os.path.dirname(__file__))
            command = f'adb -s {device_udid} pull {device_path}.projlist {temp_folder}'
            subprocess.call(command)

            temp_projlist = os.path.join(temp_folder, ".projlist")
            projlist_file = open(temp_projlist, mode='r')
            projlist = projlist_file.read()[:-3]
            projlist_file.close()

            file_path = f'{Path(__file__).parent.parent.absolute()}\\SFT\\projects\\{project_name}'
            old_projlist_file = open(os.path.join(file_path, ".projlist"), mode='r')
            old_projlist = "," + old_projlist_file.read()[9:]
            old_projlist_file.close()

            new_projlist = projlist + old_projlist
            projlist_file = open(temp_projlist, mode='w')
            projlist_file.write(new_projlist)
            projlist_file.close()

            # push project file
            command = f'adb -s {device_udid} push {temp_projlist} {device_path}'
            subprocess.call(command)

            command = f'adb -s {device_udid} push {os.path.join(file_path, project_name+".pdrproj")} {device_path}'
            subprocess.call(command)

        except Exception:
            raise Exception
        logger("re-start app <<")
        self.driver.start_app(package)
        return True

    def put_voiceover_file(self, device_udid, package):
        logger("start >> put_voiceover_file <<")
        try:
            self.driver.stop_app(package)
            logger("stop app <<")
            # remove voiceover folder
            command = f'adb -s {device_udid} shell rm -r "storage/emulated/0/Music/Recorded_Voices"'
            subprocess.call(command)
            # mkdir voiceover folder
            command = f'adb -s {device_udid} shell mkdir "storage/emulated/0/Music/Recorded_Voices"'
            subprocess.call(command)
            # push voiceover file
            file_path = f"{Path(__file__).parent.parent.absolute()}\\SFT\\template\\Recorded_Voices\\VoiceOver.wav"
            command = f'adb -s {device_udid} push "{file_path}" "/storage/emulated/0/Music/Recorded_Voices/"'
            print(command)
            subprocess.call(command)
        except Exception:
            raise Exception
        logger("re-start app <<")
        self.driver.start_app(package)
        return True

    def remove_video_templates(self, device_udid, package):
        logger("start >> remove_video_templates <<")
        try:
            self.driver.stop_app(package)
            logger("stop app <<")
            # remove video_templates folder
            command = f'adb -s {device_udid} shell rm -r "storage/emulated/0/PowerDirector/VideoTemplate"'
            subprocess.call(command)
            # mkdir project folder
            command = f'adb -s {device_udid} shell mkdir "storage/emulated/0/PowerDirector/VideoTemplate"'
            subprocess.call(command)
        except Exception:
            raise Exception
        return True

    def import_custom_font_list(self, package, font_name_list):
        logger("start >> import_custom_font_list <<")
        try:
            self.driver.stop_app(package)
            logger("stop app <<")
            for file in font_name_list:
                self.copy_custom_font(file)
        except Exception:
            logger("Exception occurs")
            return False
        logger("re-start app <<")
        self.driver.start_app(package)
        return True

    def project_reload(self, project_name):
        logger("Load project: %s" % project_name)
        if not self._terminate_app(self.package_name): return False
        self.clean_projects()
        self.copy_project(project_name)
        self.driver.driver.activate_app(self.package_name)
        self.is_exist(L.project.txt_project_title, 8)

    def relaunch_app(self, package):
        logger('Relaunch app')
        self._terminate_app(package)
        time.sleep(5)
        self.driver.driver.activate_app(package)
        time.sleep(15)
        # self.exist(L.project.tutorials,8)

    def back_to_leave_and_save_project(self, back_times=1):
        logger("start >> back_to_leave_and_save_project <<")
        try:
            for repeat in range(back_times):
                self.driver.driver.back()
                time.sleep(1)

            is_complete = 0
            for repeat in range(5):
                if self.is_exist(L.project.exit_toast):
                    logger("exit_toast pop, tap back again to exit")
                    self.driver.driver.back()
                    is_complete = 1

                    break
                elif self.is_exist(L.project.btn_exit):
                    self.el(L.project.btn_exit).click()
                    is_complete = 1
                    is_complete = 1
                    break
                self.driver.driver.back()
                time.sleep(1)

            if is_complete == 0:
                logger("btn_exit cannot be located - timeout")
                raise Exception

            for repeat in range(10):
                if self.driver.driver.query_app_state(self.app_package) != 4:
                    is_complete = 1
                    break
                time.sleep(1)

            if is_complete == 0:
                logger("leave app fail")
                raise Exception
        except Exception:
            logger("Exception occurs")
            raise Exception
        logger("leave app complete")
        return True

    def back_main(self):
        logger("back main page")
        retry = 5
        while retry:
            self.back()
            time.sleep(1)
            source = self.driver.driver.page_source
            if "btn_help_img" in source:
                logger("in main page now")
                return True
            else:
                retry -= 1
                logger(f"not in main page, retry: {retry}")
        else:
            logger("out of retry,relaunch directly")
            self.relaunch_app(PACKAGE_NAME)

    # def search_contact(self, text):
    # self.set_text(self.txt_search, text)
    # return self.get_text(self.txt_search) == text

    # def open_contact(self, _locator):
    # self.click_element(locator)
    # return self.wait_until_element_not_exist(_locator)

    # def click_chat(self):
    # self.click_element(self.btn_chat)

    # def chat_via_context(self):
    # self.long_press_element(self.item_one)
    # self.tap_element(self.menu_chat)

    def check_open_tutorial(self):
        logger("start check_open_tutorial")
        if self.exist(L.tutorials.open_tutorial, 15):
            logger("Open tutorial is exist.")
            retry = 0
            while not (self.is_exist(L.tutorials.close_open_tutorial)):
                self.driver.swipe_left()
                self.driver.swipe_left()
                retry = retry + 1
                if retry > 6:
                    logger('Fail to swipe to cancel button.')
                    return False
            self.exist_click(L.tutorials.close_open_tutorial)
            time.sleep(5)
            self.exist_click(L.subscribe.back_btn)
            return True
        else:
            logger("Open tutorial is not exist.")
            return False

    def enter_settings_from_main(self):
        # logger('start enter_settings_from_main')
        try:
            if self.is_exist(L.main.project.new_launcher_scroll):
                for swipe_time in range(5):
                    self.driver.swipe_up()
                    if self.is_exist(L.main.project.btn_settings):
                        break
                    time.sleep(1)
                self.el(L.main.project.btn_settings).click()
                time.sleep(5)
                if self.is_exist(L.main.cse.account_entry):
                    logger('Enter Settings page success!')
                    return True
                else:
                    logger('Enter Settings page Fail?')
                    return False
            else:
                logger('Not in main page')
                raise Exception
        except Exception:
            logger("Exception occurs")
            raise Exception

    def sign_in_cyberlink_account(self):
        logger('start sign_in_cyberlink_account')
        try:
            account = 'cltest.qaapp1+vl01@gmail.com'
            pw = '123456'
            for swipe_time in range(5):
                if self.is_exist(L.cse.login_entry):
                    break
                if self.is_exist(L.cse.btn_logout):
                    logger('Alreay logged in')
                    return True
                self.driver.swipe_up()
                time.sleep(1)
            self.el(L.cse.login_entry).click()
            if not self.is_exist(L.cse.login_page):
                logger('Login page not show.')
                raise Exception
            time.sleep(5)
            time.sleep(5)
            self.set_text(L.cse.email_field, account, True)
            self.set_text(L.cse.password_field, pw, True)
            time.sleep(5)
            self.el(L.cse.btn_login).click()
            time.sleep(10)
            self.exist_click(L.cse.btn_continue)
            time.sleep(10)
            if self.is_exist(L.cse.btn_logout):
                logger('Sign in Success!')
                return True
            else:
                logger('Sign in Fail?')
                return False
        except Exception:
            logger("Exception occurs")
            raise Exception

    def sign_out_cyberlink_account(self):
        logger('start sign_out_cyberlink_account')
        try:
            for swipe_time in range(5):
                if self.is_exist(L.cse.btn_logout):
                    break
                self.driver.swipe_up()
                time.sleep(1)
            self.el(L.cse.btn_logout).click()
            time.sleep(10)
            # self.driver.swipe_up()
            # time.sleep(1)
            if self.is_exist(L.setting.layout_premium):
                logger('Sign out Success!')
                return True
            else:
                logger('Sign out Fail?')
                return False
        except Exception:
            logger("Exception occurs")
            raise Exception

    def swipe_main_page(self, direction, swipe_time=5):
        for retry in range(swipe_time):
            if direction == 'up':
                self.driver.swipe_up()
            elif direction == 'down':
                self.driver.swipe_down()
            time.sleep(1)

    def swipe_sample_projects_list(self, direction, swipe_time=5):
        for retry in range(swipe_time):
            self.swipe_element(L.sample_projects.list, direction, 300)
            time.sleep(1)

    def check_sample_projects_thumbnails(self):
        try:
            frame = self.el(L.sample_projects.list)
            if frame.find_element_by_xpath('(//*[contains(@resource-id,"thumbnail")])'):
                logger('Video preview is exist.')
                return True
            else:
                logger('No Video preview')
                return False
        except Exception:
            logger("Exception occurs")
            raise Exception

    def select_sample_project(self, name):
        logger(f'start select_sample_project : {name}')
        try:
            self.is_exist(L.sample_projects.list)
            frame = self.el(L.sample_projects.list)
            locator = ("xpath", f'//android.widget.TextView[contains(@text,"{name}")]')
            for retry in range(15):
                if self.is_exist(locator):
                    frame.find_element_by_xpath(f'//android.widget.TextView[contains(@text,"{name}")]').click()
                    logger(f"Found {name} project, click it.")
                    break
                else:
                    self.swipe_element(L.sample_projects.list, 'left', 350)
                    self.swipe_element(L.sample_projects.list, 'left', 350)
                    self.swipe_element(L.sample_projects.list, 'left', 350)
                    time.sleep(1)
            return self.wait_until_element_exist(E.preview.movie_view, 30)
        except Exception:
            logger("Exception occurs")
            raise Exception

    def calculate_sample_projects_amount(self):
        logger("start calculate_sample_projects_amount")
        try:
            caption_list = set()
            caption_list_count = len(caption_list)
            caption_list_count_prev = -1
            while caption_list_count != caption_list_count_prev:
                logger(
                    f"Count Start - caption_list_count={caption_list_count}, caption_list_count_prev={caption_list_count_prev}")
                if caption_list_count_prev != -1:
                    self.swipe_element(L.sample_projects.list, 'left', 300)
                    time.sleep(1)
                caption_list_count_prev = caption_list_count
                els_item_list = self.els(L.sample_projects.project_title)
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

    def enter_gamification(self):
        logger("start >>enter_gamification<<")
        if self.is_exist(L.gamification.btn_entry, 3):
            logger("Found entry")
            self.click(L.gamification.btn_entry)
            if self.is_exist(L.gamification.btn_check_rewards, 5):
                logger("check_rewards dialog pop")
                self.click(L.gamification.btn_check_rewards)
            if self.is_exist(L.gamification.tab_active, 5):
                logger("Enter gamification page success")
                return True
        else:
            logger("No entry")
        return False

    def check_gamification_titles(self, text):
        logger(f"start check_gamification_titles")
        try:
            elsm = self.els(L.gamification.quest_title)
            for index in range(len(elsm)):
                if str(elsm[index].text) == str(text):
                    logger(f'Found text: {text}')
                    return True
            logger(f"Didn't found text: {text}")
            return False
        except Exception:
            logger('exception occurs')
            raise Exception

    def check_gamification_mission_description(self):
        logger(f"start check_gamification_mission_description")
        try:
            description_list = set()
            description_list_count = len(description_list)
            description_list_count_prev = -1
            while description_list_count != description_list_count_prev:
                logger(
                    f"Count Start - description_list_count={description_list_count}, description_list_count_prev={description_list_count_prev}")
                if description_list_count_prev != -1:
                    self.swipe_element(L.gamification.scroller, 'up', 300)
                    self.swipe_element(L.gamification.scroller, 'up', 300)
                    time.sleep(1)
                description_list_count_prev = description_list_count
                els_item_list = self.els(L.gamification.mission_description)
                logger(f'current description count={len(els_item_list)}')
                if len(els_item_list) > 0:
                    logger('enter update set')
                    for el_item in els_item_list:
                        description_list.add(el_item.text)
                description_list_count = len(description_list)
                logger(f'set count={description_list_count}')
            logger(f'description amount={description_list_count}')
            return description_list
            # for index in range(description_list_count):
            #     if str(description_list[index].text) == str(text):
            #         logger(f'Found text: {text}')
            #         return True
            # logger(f"Didn't found text: {text}")
            # return False
        except Exception:
            logger('exception occurs')
            raise Exception

    def check_gamification_reward_content(self, text):
        logger(f"start check_gamification_reward_content")
        try:
            elm = self.el(L.gamification.claim_dialog.description)
            if str(elm.text) == str(text):
                logger(f'Found text: {text}')
                return True
            else:
                return False
        except Exception:
            logger('exception occurs')
            raise Exception

    def check_gamification_claim_countdown(self):
        logger(f"start check_gamification_claim_countdown")
        try:
            elms = self.els(L.gamification.btn_claim)
            for index in range(len(elms)):
                if str(elms[index].text) != 'Claim':
                    logger(f'Counting down: {elms[index].text}')
                    return True
            logger(f"Didn't found countdown")
            return False
        except Exception:
            logger('exception occurs')
            raise Exception

    def select_gamification_claim_by_order(self, index):
        logger(f"start select_gamification_claim_by_order: {index}")
        try:
            elsm = self.els(L.gamification.btn_claim)
            elsm[index].click()
            if self.is_exist(L.gamification.claim_dialog.description):
                logger('Completed claim dialog opened')
                return True
            elif self.is_exist(L.gamification.claim_dialog.title_not_complete):
                logger('Uncompleted claim dialog opened')
                return True
            return False
        except Exception:
            logger('exception occurs')
            raise Exception

    def close_gamification_claim_dialog(self):
        logger(f"start close_gamification_claim_dialog")
        if self.is_exist(L.gamification.claim_dialog.btn_ok):
            self.el(L.gamification.claim_dialog.btn_ok).click()
            if not self.is_exist(L.gamification.claim_dialog.btn_ok):
                logger('Claim dialog closed')
                return True
        elif self.is_exist(L.gamification.claim_dialog.description):
            self.driver.driver.back()
            if not self.is_exist(L.gamification.claim_dialog.description):
                logger('Claim dialog closed')
                return True
        return False

    def check_premium_label(self):
        logger(f"start check_premium_label")
        self.el(L.premium.btn_premium).click()
        time.sleep(5)
        elm = self.el(L.premium.dialog_title)
        if str(elm.text) == 'Premium':
            logger(f'Found title: {elm.text}')
            self.el(L.premium.iap_back).click()
            return True
        logger(f"Didn't found title")
        return False

    def check_video_overlay_limit_message(self):
        logger(f"start check_video_overlay_limit_message")
        elm = self.el(L.premium.message)
        if str(elm.text) == "No more videos can be added to the overlay track at the current time because you've reached your device’s allowed limit (2).":
            logger(f'Found message: {elm.text}')
            self.el(L.premium.btn_remind_ok).click()
            return True
        logger(f"Didn't found message")
        return False

    def check_iap_feature_items(self, name):
        logger("start check_iap_feature_items")
        try:
            caption_list = set()
            caption_list_count = len(caption_list)
            caption_list_count_prev = -1
            for retry in range(5):
                self.swipe_element(L.subscribe.feature_list, 'right', 300)
                self.swipe_element(L.subscribe.feature_list, 'right', 300)
                self.swipe_element(L.subscribe.feature_list, 'right', 300)
            while caption_list_count != caption_list_count_prev:
                logger(
                    f"Count Start - caption_list_count={caption_list_count}, caption_list_count_prev={caption_list_count_prev}")
                if caption_list_count_prev != -1:
                    self.swipe_element(L.subscribe.feature_list, 'left', 300)
                    self.swipe_element(L.subscribe.feature_list, 'left', 300)
                    self.swipe_element(L.subscribe.feature_list, 'left', 300)
                    self.swipe_element(L.subscribe.feature_list, 'left', 300)
                    time.sleep(1)
                caption_list_count_prev = caption_list_count
                els_item_list = self.els(L.subscribe.feature_name)
                logger(f'current clips count={len(els_item_list)}')
                if len(els_item_list) > 0:
                    logger('enter update caption set')
                    for el_item in els_item_list:
                        caption_list.add(el_item.text)
                caption_list_count = len(caption_list)
                logger(f'caption set count={caption_list_count}')
            result = True if name in caption_list else False
        except Exception:
            logger('exception occurs')
            raise Exception
        logger(f'content amount={caption_list_count}')
        return result

    def wait_subscribe_expire(self):
        logger("start check_iap_feature_items")
        try:
            for retry in range(10):
                if self.is_exist(L.project.shopping_cart):
                    logger('Shopping cart is exist, end waiting.')
                    break
                else:
                    logger('Shopping cart not exist, relaunch app and wait...')
                    self._terminate_app(pdr_package)
                    self.driver.driver.activate_app(pdr_package)
                    time.sleep(20)
                    time.sleep(20)
                    time.sleep(20)
        except Exception:
            logger('exception occurs')
            raise Exception

    def check_iap_highlighted_item(self, name):
        logger(f'start check_iap_highlighted_item = {name}')
        try:
            self.swipe_element(L.subscribe.feature_list, 'right', 100)
            elm = self.el(L.subscribe.feature_list)
            parent = elm.find_element_by_xpath('//android.widget.ImageView[contains(@resource-id,"highlight")]/..')
            item = parent.find_element_by_xpath('//android.widget.TextView[contains(@resource-id,"text_view")]')
            string = item.text
            string = string.replace('\r', ' ').replace('\n', ' ')  # Replace linebreak with space
            logger(f'item text = {string}')
            if string == name:
                logger('Highlighted item name matched!')
                return True
            else:
                logger('Highlighted item name not match.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception

    def click_no_ads(self):
        logger(f'start click_no_ads')
        try:
            if not self.is_exist(L.project.ads):
                logger('Ads not exist.')
                return False
            elm = self.el(L.project.ads)
            x = int(elm.rect['x'] + elm.rect['width'] * 0.8)
            y = int(elm.rect['y'] - elm.rect['height'] * 0.1)
            logger(f"touch x={x}, y={y}")
            actions = TouchAction(self.driver.driver)
            actions.press(x=x, y=y).release().perform()
            if self.is_exist(L.subscribe.feature_list):
                logger('IAP opened')
                return True
            else:
                logger('IAP not open.')
                return False
        except Exception:
            logger("exception occurs")
            raise Exception

    def set_device_date(self, device_udid, package):
        logger("start >> set_device_date <<")
        try:
            self.driver.stop_app(package)
            logger("stop app <<")
            # remove video_templates folder
            command = f'adb -s {device_udid} shell rm -r "storage/emulated/0/PowerDirector/VideoTemplate"'
            subprocess.call(command)
            # mkdir project folder
            command = f'adb -s {device_udid} shell mkdir "storage/emulated/0/PowerDirector/VideoTemplate"'
            subprocess.call(command)
        except Exception:
            raise Exception
        return True


class Shortcut:
    def __init__(self, main):
        self.main = main

        self.click = self.main.h_click
        self.long_press = self.main.h_long_press
        self.element = self.main.h_get_element
        self.elements = self.main.h_get_elements
        self.is_exist = self.main.h_is_exist
        self.is_not_exist = self.main.h_is_not_exist

    def click_style(self, name):
        style = find_string(name)
        try:
            if self.is_exist(style, 2):
                self.click(style)
            else:
                last = ""
                while 1:
                    items = self.elements(L.main.shortcut.ai_art.style_name(0))
                    if items[-1].text == last:
                        logger("Not found style")
                        return False
                    else:
                        last = items[-1].text
                        self.main.h_swipe_element(items[-1], items[0], 3)
                        if self.click(style):
                            break
            return True
        except Exception:
            traceback.print_exc()
            return False

    def click_paid_style(self):
        try:
            last = None
            while 1:
                if self.click(L.main.shortcut.ai_sketch.paid_style, 1):
                    return True
                else:
                    styles = self.elements(L.main.shortcut.ai_sketch.style(0))
                    if styles[-1] == last:
                        logger("Not found paid style")
                        return False
                    else:
                        last = styles[-1]
                        self.main.h_swipe_element(styles[-1], styles[0], 3)
        except Exception:
            traceback.print_exc()
            return False

    def click_free_style(self):
        try:
            last = None
            while 1:
                styles = self.elements(L.main.shortcut.ai_sketch.style(0))
                for style in styles:
                    try:
                        style.find_element(id("itemPremium"))
                    except NoSuchElementException:
                        style.click()
                        print("Clicked on a non-premium style.")
                        return True
                else:
                    if styles[-1] == last:
                        logger("Not found free style")
                        return False
                    else:
                        last = styles[-1]
                        self.main.h_swipe_element(styles[-1], styles[0], 3)

        except Exception:
            traceback.print_exc()
            return False

    def waiting_generated(self, gen_btn=None, retry=30, timeout=120):
        try:
            for i in range(retry):
                if gen_btn:
                    self.click(gen_btn)
                self.click(aid('[AID]ConfirmDialog_No'), 1)

                if self.is_exist(L.main.shortcut.ai_art.generating, 1):
                    self.is_not_exist(L.main.shortcut.ai_art.generating, timeout)

                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

        except Exception:
            traceback.print_exc()
            raise

