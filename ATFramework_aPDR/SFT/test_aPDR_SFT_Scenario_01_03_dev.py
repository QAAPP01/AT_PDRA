from main import deviceName
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

import inspect
import sys
import time
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

# global value
files_by_date = ["3gp.3gp", "slow_motion.mp4", "mp4.mp4", "mkv.mkv"]
files_by_resolution = ["mkv.mkv", "mp4.mp4", "slow_motion.mp4", "3gp.3gp"]
files_by_file_size = ["mkv.mkv", "3gp.3gp", "mp4.mp4", "slow_motion.mp4"]

test_material_folder = TEST_MATERIAL_FOLDER
test_material_folder_01 = TEST_MATERIAL_FOLDER_01
files_list = []
project_name = ""
clip_width = ""


class Test_SFT_Scenario_01_03:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        self.report.set_driver(driver)
        driver.driver.launch_app()

    def sce_01_03_01(self):
        uuid = 'c023139e-c9cc-4328-8712-3ee02658fbaa'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        global project_name
        project_name = '16_9'
        self.page_main.add_project_list(deviceName, pdr_package, project_name)
        self.page_main.enter_launcher()

        if self.page_main.enter_timeline(project_name):
            result = True
        else:
            result = False
            logger('\n[Fail] Cannot find timeline canvas')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_02(self):
        uuid = 'a5217615-8e5b-45c0-9926-7a590329f261'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        project_ratio = self.page_edit.preview_ratio()
        if project_ratio == '16_9':
            result = True
        else:
            result = False
            logger(f'\n[Fail] Project ratio is {project_ratio}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_03(self):
        uuid = 'd04019c0-bdb6-4237-a3d4-7571a7f5e54d'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)
        duration_result = self.page_preference.check_setting_image_duration(10.0, False)
        timeline_result = self.page_preference.check_timeline_image_duration(file_name='16_9.jpg')
        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)

        if timeline_result == duration_result == '10.0 s':
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Not synced with sec_1.2.5, timeline_result = {timeline_result}, duration_result = {duration_result}'
            logger(fail_log)

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_03_04(self):
        uuid = '0015cf16-0a05-4bdd-ab05-3bb7a4427f1b'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        duration_result = self.page_preference.check_setting_image_duration(0.1)
        timeline_result = self.page_preference.check_timeline_image_duration(file_name='16_9.jpg')
        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)

        if timeline_result == duration_result == '0.1 s':
            result = True
        else:
            result = False
            logger(f'\n[Fail] timeline_result = {timeline_result}, duration_result = {duration_result}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_05(self):
        uuid = '217c88ad-6b65-4410-be29-b94d805facf0'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        duration_result = self.page_preference.check_setting_image_duration(10.0)
        timeline_result = self.page_preference.check_timeline_image_duration(file_name='16_9.jpg')
        global clip_width
        clip_width = self.page_main.h_get_element(L.edit.timeline.item_view_border).rect['width']

        if timeline_result == duration_result == '10.0 s':
            result = True
        else:
            result = False
            logger(f'\n[Fail] timeline_result = {timeline_result}, duration_result = {duration_result}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_06(self):
        uuid = 'd525ef8a-7a27-42f3-ac90-5e1783510720'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)
        self.page_main.h_click(L.edit.settings.menu)
        self.page_main.h_click(L.edit.settings.preference)
        self.page_main.h_click(L.timeline_settings.settings.default_pan_zoom_effect)
        self.driver.driver.back()
        self.page_main.h_click(L.edit.preview.import_tips_icon)
        self.page_media.select_local_photo(test_material_folder, '16_9.jpg')
        pic_base = self.page_main.get_preview_pic()
        self.page_main.h_click(L.edit.menu.play)
        time.sleep(10)
        pic_after = self.page_main.get_preview_pic()
        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)

        if not CompareImage(pic_base, pic_after).h_total_compare() > 0.98:
            result = True
        else:
            result = False
            logger(f'\n[Fail] Image are the same')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_07(self):
        uuid = 'f0925727-013a-4f85-9263-185913bef854'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_main.h_click(L.edit.settings.menu)
        self.page_main.h_click(L.edit.settings.preference)
        self.page_main.h_click(L.timeline_settings.settings.default_pan_zoom_effect)
        self.driver.driver.back()
        self.page_main.h_click(L.edit.preview.import_tips_icon)
        self.page_media.select_local_photo(test_material_folder, '16_9.jpg')
        pic_base = self.page_main.get_preview_pic()
        self.page_main.h_click(L.edit.menu.play)
        time.sleep(10)
        pic_after = self.page_main.get_preview_pic()
        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)

        if CompareImage(pic_base, pic_after).h_total_compare() > 0.98:
            result = True
        else:
            result = False
            logger(f'\n[Fail] Image are not the same')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_1_3_8(self):
        uuid = '8b96e410-9567-43bd-9318-e708588c121f'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.preview.import_tips_icon)
            self.page_media.switch_to_video_library()
            
            if self.page_media.select_local_folder(test_material_folder_01):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Cannot find the folder{test_material_folder_01}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_3_9(self):
        uuid = '8c798524-1b86-45d2-8817-b571a2d24744'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        try:
            for retry in range(20):
                if not self.is_exist(find_string("mp4.mp4")):
                    self.driver.swipe_element(L.import_media.media_library.frame, 'up', 300)
                else:
                    break

            if self.is_exist(find_string("mp4.mp4")):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find the file "mp4.mp4"'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_3_10(self):
        uuid = 'e86a08d6-ef03-489f-9c25-0cb1129c7ec7'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.sort_menu.sort_button)
            result_date = self.element(L.import_media.sort_menu.by_date).get_attribute("checked")
            result_descending = self.element(L.import_media.sort_menu.descending).get_attribute("checked")

            if result_date == "true" and result_descending == "true":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] result_date = {result_date}, result_descending = {result_descending}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.sort_menu.sort_button)

            return "FAIL"

    def sce_01_03_11(self):
        try:
            uuid = '6915774e-803f-4bdc-b3e2-801265ab092d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.descending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name, reverse=True)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_01_03_13(self):
        uuid = 'f94ff455-5b41-48e5-8fbb-ae82e1a0f06c'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_resolution)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_name = []
        files = self.elements(L.import_media.media_library.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_resolution:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_resolution = {files_by_resolution}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_14(self):
        uuid = '4c7a3ee8-3583-48ff-93d8-0a419c93bdaf'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_duration)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_duration = []
        files = self.elements(L.import_media.media_library.duration(0))

        for i in files:
            files_duration.append(i.text)
        duration_order = sorted(files_duration, reverse=True)

        if duration_order == files_duration:
            result = True
        else:
            result = False
            logger(f'\n[Fail] Order of files_duration incorrect: {files_duration}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_15(self):
        uuid = 'e561ab86-9b2f-448a-95ac-da9316b0364d'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_file_size)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_file_size:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_12(self):
        uuid = '98a791b5-7722-4d7c-a1a2-1950fbc8a8cd'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_date)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_name = []
        files = self.elements(L.import_media.media_library.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_date:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_date = {files_by_date}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_16(self):
        uuid = '821b99cf-c7e8-49dd-939b-3e42ea3e2a78'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = "mp4.mp4"
        self.page_media.select_local_video(test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find {file_name} on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_03_17(self):
        uuid = 'e59a01fc-8854-4779-b324-acd2bbff1d43'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        file_name = "mkv.mkv"
        self.page_media.select_local_video(test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find {file_name} on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_03_18(self):
        uuid = '40a15d6a-2366-4e3d-8e1a-6d15c08b5eec'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        file_name = 'gif.gif'
        self.page_media.select_local_photo(test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_photo(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find "{file_name}" on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_03_19(self):
        uuid = 'be427fb7-345f-42f5-9b9a-d6b8478b48d0'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        if self.element(L.edit.timeline.master_photo('gif.gif')).rect['width'] == clip_width:
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] clip_width is not equal'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_01_03_20(self):
        uuid = '26c0fd29-ebbf-4bc8-b11e-bf5ccd6e208a'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        file_name = 'png.png'
        self.page_media.select_local_photo(test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_photo(file_name)):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "{file_name}" on master track')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_21(self):
        uuid = '6c59047f-90f0-4b4d-a3fb-a4ab45040524'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        if self.element(L.edit.timeline.master_photo('png.png')).rect['width'] == clip_width:
            result = True
        else:
            result = False
            logger(f'\n[Fail] clip_width is not equal')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_22(self):
        uuid = 'ea56db50-2b0d-48d9-9feb-f91203f6a31e'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.click_tool("Audio")
        self.page_main.h_click(find_string("Music"))
        self.page_main.h_click(L.import_media.music_library.local)
        self.page_main.h_click(find_string(test_material_folder))
        global files_list
        files = self.page_main.h_get_elements(L.import_media.music_library.file_name)
        for i in files:
            files_list.append(i.text)

        add = self.page_main.h_get_elements(L.import_media.music_library.add)
        file_name = 'm4a.m4a'
        index = files_list.index(file_name)
        self.page_main.h_click(add[index])
        locator = aid(f"[AID]TimeLineAudio_{file_name}")

        if self.page_main.h_is_exist(locator):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "{file_name}" on master track')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_23(self):
        uuid = '9ee4f99d-b3ec-4274-90fb-b71567c64b9b'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.click_tool("Audio")
        self.page_main.h_click(find_string("Music"))
        self.page_main.h_click(L.import_media.music_library.local)
        self.page_main.h_click(find_string(test_material_folder))

        add = self.page_main.h_get_elements(L.import_media.music_library.add)
        file_name = 'mp3.mp3'
        index = files_list.index(file_name)
        self.page_main.h_click(add[index])
        locator = aid(f"[AID]TimeLineAudio_{file_name}")

        if self.page_main.h_is_exist(locator):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "{file_name}" on master track')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_24(self):
        uuid = '9877d20c-9521-41eb-9554-bda13a6a837f'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.click_tool("Audio")
        self.page_main.h_click(find_string("Music"))
        self.page_main.h_click(L.import_media.music_library.local)
        self.page_main.h_click(find_string(test_material_folder))

        add = self.page_main.h_get_elements(L.import_media.music_library.add)
        file_name = 'wav.wav'
        index = files_list.index(file_name)
        self.page_main.h_click(add[index])
        locator = aid(f"[AID]TimeLineAudio_{file_name}")

        if self.page_main.h_is_exist(locator):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "{file_name}" on master track')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_03_34(self):
        uuid = 'dd672f53-f444-4562-ae07-a38499322f04'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.h_click(L.edit.menu.home)
        # Churn Recovery
        if self.page_edit.h_is_exist(L.main.premium.pdr_premium):
            self.driver.driver.back()
        first_project_name = self.page_main.h_get_element(L.main.project.project_name()).text

        if first_project_name == project_name:
            result = True
        else:
            result = False
            logger(f'\n[Fail] first_project_name is {first_project_name}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"


    def test_case(self):
        result = {"sce_01_03_01": self.sce_01_03_01(),
                  "sce_01_03_02": self.sce_01_03_02(),
                  "sce_01_03_03": self.sce_01_03_03(),
                  "sce_01_03_04": self.sce_01_03_04(),
                  "sce_01_03_05": self.sce_01_03_05(),
                  "sce_01_03_06": self.sce_01_03_06(),
                  "sce_01_03_07": self.sce_01_03_07(),
                  "sce_1_3_8": self.sce_1_3_8(),
                  "sce_1_3_9": self.sce_1_3_9(),
                  "sce_1_3_10": self.sce_1_3_10(),
                  "sce_01_03_11": self.sce_01_03_11(),
                  "sce_01_03_13": self.sce_01_03_13(),
                  "sce_01_03_14": self.sce_01_03_14(),
                  "sce_01_03_15": self.sce_01_03_15(),
                  "sce_01_03_12": self.sce_01_03_12(),
                  "sce_01_03_16": self.sce_01_03_16(),
                  "sce_01_03_17": self.sce_01_03_17(),
                  "sce_01_03_18": self.sce_01_03_18(),
                  "sce_01_03_19": self.sce_01_03_19(),
                  "sce_01_03_20": self.sce_01_03_20(),
                  "sce_01_03_21": self.sce_01_03_21(),
                  "sce_01_03_22": self.sce_01_03_22(),
                  "sce_01_03_23": self.sce_01_03_23(),
                  "sce_01_03_24": self.sce_01_03_24(),
                  "sce_01_03_34": self.sce_01_03_34()
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
