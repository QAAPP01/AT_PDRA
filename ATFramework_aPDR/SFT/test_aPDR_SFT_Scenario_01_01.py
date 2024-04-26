import inspect
import sys, os, glob
from os.path import dirname
from os import path
import subprocess
from pprint import pprint
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *

from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.ATFramework.utils.log import logger
import pytest
import time

from main import deviceName
from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_01_01:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

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
        yield
        driver.driver.close_app()

    def sce_1_1_1(self):
        try:
            uuid = '61aa4cc9-a43d-4736-93f9-668e65b4fd8b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_local_photo(TEST_MATERIAL_FOLDER, "16_9.jpg")
            self.click(L.edit.menu.home)
            if self.is_exist(L.main.premium.pdr_premium):  # Churn Recovery
                self.driver.driver.back()
            import datetime
            dt = datetime.datetime.today()
            project_name_default = 'Project {:02d}-{:02d}'.format(dt.month, dt.day)
            global project_name
            self.click(L.main.project.entry)
            project_name = self.element(L.main.project.project_name()).text

            if project_name == project_name_default:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Project Name incorrect: {project_name} != {project_name_default}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_2(self):
        try:
            uuid = 'f3e277f2-67f0-4da8-80fe-02bb72857123'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.main.project.entry)
            self.page_main.enter_timeline(project_name)
            project_ratio = self.page_edit.preview_ratio()

            if project_ratio == '16:9':
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Project ratio is {project_ratio} != 16:9'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_3(self):
        try:
            uuid = '4291a9f9-9d66-43f6-87ed-752f9ef0d2fb'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.add_pip_media('photo', self.test_material_folder, '9_16.jpg')
            self.page_edit.click_tool("Edit")

            if self.page_edit.is_sub_tool_exist("Fit & Fill"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Tool menu of master clip is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_4(self):
        try:
            uuid = '8bbac0e0-6c1c-4f45-8fcb-f8b70e593208'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.menu.delete)
            self.page_edit.click_tool("Edit")

            if self.page_edit.is_sub_tool_exist("Opacity"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Tool menu of pip clip is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_5(self):
        try:
            uuid = '30ba9ee9-7129-4961-9856-294eea4ab179'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.menu.delete)
            self.page_edit.click_tool("Edit")
            toast_default = 'Insert at least one media file.'
            toast = self.element(xpath('/hierarchy/android.widget.Toast[1]')).text

            if toast == toast_default:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Toast incorrect: {toast}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_6(self):
        try:
            uuid = 'd2fb39a7-d1a2-41c7-8b55-9f69005d2d7d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.driver.swipe_element(L.edit.timeline.timeline_ruler, 'left', 100)
            self.page_edit.add_pip_media('photo', self.test_material_folder, '9_16.jpg')
            self.click(L.edit.sub_tool.back, timeout=0.1)
            self.driver.swipe_element(L.edit.timeline.timeline_ruler, 'right')
            self.page_edit.click_tool("Edit")

            toast_default = 'Insert at least one media file.'
            toast = self.element(xpath('/hierarchy/android.widget.Toast[1]')).text

            if toast == toast_default:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Toast incorrect: {toast}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_7(self):
        try:
            uuid = 'dfa15053-3add-4573-8e05-5acf235f551e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.timeline.clip())
            self.click(L.edit.menu.delete)
            duration_result = self.page_edit.check_setting_image_duration(5.0, False)
            timeline_result = self.page_edit.check_timeline_image_duration(file_name='16_9.jpg')
            self.page_main.h_click(L.edit.timeline.item_view_border)
            self.page_main.h_click(L.edit.menu.delete)

            if timeline_result == duration_result == '5.0 s':
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] timeline_result = {timeline_result}, duration_result = {duration_result}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_8(self):
        try:
            uuid = '808d09fb-d074-456b-afcb-be56e5b9bfab'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            duration_result = self.page_edit.check_setting_image_duration(0.1)
            timeline_result = self.page_edit.check_timeline_image_duration(file_name='16_9.jpg')
            self.page_main.h_click(L.edit.timeline.item_view_border)
            self.page_main.h_click(L.edit.menu.delete)

            if timeline_result == duration_result == '0.1 s':
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] timeline_result = {timeline_result}, duration_result = {duration_result}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_9(self):
        try:
            uuid = '57ea0d57-d706-4fdf-8d54-61cdae50bc68'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            duration_result = self.page_edit.check_setting_image_duration(10.0)
            timeline_result = self.page_edit.check_timeline_image_duration(file_name='16_9.jpg')
            global clip_width
            clip_width = self.element(L.edit.timeline.item_view_border).rect['width']

            if timeline_result == duration_result == '10.0 s':
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] timeline_result = {timeline_result}, duration_result = {duration_result}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_11(self):
        try:
            uuid = '7d73d3a4-c2ab-46d4-99fd-51f497209bf1'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.timeline.master_clip)
            pic_base = self.page_main.get_preview_pic()
            rect = self.element(L.edit.timeline.master_clip).rect
            dx = rect["x"] + rect["width"]
            self.page_main.swipe_element(L.edit.timeline.timeline_ruler, 'left', dx)
            self.click(L.edit.menu.play)
            time.sleep(10)
            pic_after = self.page_main.get_preview_pic()
            self.page_main.h_click(L.edit.timeline.item_view_border)
            self.page_main.h_click(L.edit.menu.delete)

            if CompareImage(pic_base, pic_after).h_total_compare() > 0.98:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_10(self):
        try:
            uuid = 'f1a093d3-cc42-468c-94c5-11d804d08ba9'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.edit.settings.menu)
            self.page_main.h_click(L.edit.settings.preference)
            self.page_main.h_click(L.timeline_settings.settings.default_pan_zoom_effect)
            self.click(L.timeline_settings.preference.back)
            self.page_edit.add_master_media('photo', self.test_material_folder, '16_9.jpg')
            self.click(L.edit.timeline.master_clip)
            pic_base = self.page_main.get_preview_pic()
            self.page_main.h_click(L.edit.menu.play)
            time.sleep(10)
            pic_after = self.page_main.get_preview_pic()
            self.page_main.h_click(L.edit.timeline.item_view_border)
            self.page_main.h_click(L.edit.menu.delete)

            if not CompareImage(pic_base, pic_after).h_total_compare() > 0.98:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_12(self):
        uuid = '465d472f-f1b4-4993-ac3e-d93cd988efd7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)

            if self.page_main.h_is_exist(find_string(self.test_material_folder)):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find test folder'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_13(self):
        try:
            uuid = 'bc551d29-ccb1-4a12-a516-266bc6a56b05'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(find_string(self.test_material_folder))

            if self.page_main.h_is_exist(find_string('aac.aac')):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find test file'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_14(self):
        try:
            uuid = '2110ecb2-a66a-4257-82d6-b85f4ca7a526'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.import_media.music_library.sort)
            result_name = self.element(L.import_media.music_library.by_name).get_attribute("checked")
            result_ascending = self.element(L.import_media.music_library.by_ascending).get_attribute("checked")

            if result_name == 'true' and result_ascending == 'true':
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Default_name: {result_name}, Default_ascending: {result_ascending}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_15(self):
        try:
            uuid = '3d50dd61-af2c-41db-a8e3-e5502fe7b076'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if not self.page_main.h_is_exist(find_string("Resolution")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Resolution is exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_16(self):
        try:
            uuid = 'de1e1ed0-45df-4700-b80b-53f68a439c04'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.by_name)
            self.page_main.h_click(L.import_media.music_library.by_ascending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.music_library.file_name)
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Files = {files_name}, re-order = {file_name_order}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_17(self):
        try:
            uuid = 'c90e80db-74b2-4a22-9819-8e33d450dd70'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_duration)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration)

            if files_duration_order == files_duration:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_18(self):
        try:
            uuid = '80372617-a42c-4da2-9141-62cd6982b607'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_file_size)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration)

            if files_duration_order == files_duration:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_19(self):
        try:
            uuid = 'cf5d1894-f2f9-4fa4-886d-a24892994566'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_name)
            self.page_main.h_click(L.import_media.music_library.by_descending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.music_library.file_name)
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name, reverse=True)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Files = {files_name}, re-order = {file_name_order}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_20(self):
        try:
            uuid = '6d352df4-7589-4504-b52e-b14309957ba5'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_duration)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration, reverse=True)

            if files_duration_order == files_duration:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_21(self):
        try:
            uuid = '20cc43dd-b11c-4bb8-b456-c4f769528958'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_file_size)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration, reverse=True)

            if files_duration_order == files_duration:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_22(self):
        try:
            uuid = '7959304e-4588-4810-9e69-b00ae850bce3'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_file_size)
            self.driver.driver.back()

            global files_name
            files_name = []
            files = self.elements(L.import_media.music_library.file_name)
            for i in files:
                files_name.append(i.text)

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[0])
            locator = aid("[AID]TimeLineAudio_" + files_name[0])

            if self.page_main.h_is_exist(locator):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] {files_name[0]} is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_23(self):
        try:
            uuid = '9ab7a343-335e-426f-8813-f64260c29f38'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)
            self.page_main.h_click(find_string(self.test_material_folder))

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[1])
            locator = aid("[AID]TimeLineAudio_" + files_name[1])

            if self.page_main.h_is_exist(locator):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] {files_name[1]} is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_24(self):
        try:
            uuid = 'ae18e001-07c8-4009-995f-d3a4c22792b3'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)
            self.page_main.h_click(find_string(self.test_material_folder))

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[2])
            locator = aid("[AID]TimeLineAudio_" + files_name[2])

            if self.page_main.h_is_exist(locator):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] {files_name[2]} is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_1_1_25(self):
        try:
            uuid = '990c2772-b52c-494a-8727-9ce83ec70aca'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)
            self.page_main.h_click(find_string(self.test_material_folder))

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[3])
            locator = aid("[AID]TimeLineAudio_" + files_name[3])

            if self.page_main.h_is_exist(locator):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] {files_name[3]} is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_01_01_12_to_25(self):
        try:
            result = {}

            # sce_01_01_08
            item_id = '01_01_08'
            uuid = '465d472f-f1b4-4993-ac3e-d93cd988efd7'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)
            result[item_id] = self.page_main.h_is_exist(find_string(self.test_material_folder))

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_09
            item_id = '01_01_09'
            uuid = 'bc551d29-ccb1-4a12-a516-266bc6a56b05'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(find_string(self.test_material_folder))
            result[item_id] = self.page_main.h_is_exist(find_string('aac.aac'))

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_10
            item_id = '01_01_10'
            uuid = '2110ecb2-a66a-4257-82d6-b85f4ca7a526'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            result_name = self.element(L.import_media.music_library.by_name).get_attribute("checked")
            result_ascending = self.element(L.import_media.music_library.by_ascending).get_attribute(
                "checked")
            if result_name == 'false' or result_ascending == 'false':
                logger(f'\n[Fail] Default_name: {result_name}, Default_ascending: {result_ascending}')
            result[item_id] = True if result_name == 'true' and result_ascending == 'true' else False

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_11
            item_id = '01_01_11'
            uuid = '3d50dd61-af2c-41db-a8e3-e5502fe7b076'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            result[item_id] = not self.page_main.h_is_exist(find_string("Resolution"))

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_12
            item_id = '01_01_12'
            uuid = 'de1e1ed0-45df-4700-b80b-53f68a439c04'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.by_name)
            self.page_main.h_click(L.import_media.music_library.by_ascending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.music_library.file_name)
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name)
            result[item_id] = file_name_order == files_name
            if not result[item_id]:
                logger(f'\n[Fail] Files = {files_name}, re-order = {file_name_order}')

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_13
            item_id = '01_01_13'
            uuid = 'c90e80db-74b2-4a22-9819-8e33d450dd70'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_duration)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration)
            result[item_id] = files_duration_order == files_duration
            if not result[item_id]:
                logger(f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}')

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_14
            item_id = '01_01_14'
            uuid = '80372617-a42c-4da2-9141-62cd6982b607'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_file_size)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration)
            result[item_id] = files_duration_order == files_duration
            if not result[item_id]:
                logger(f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}')

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_15
            item_id = '01_01_15'
            uuid = 'cf5d1894-f2f9-4fa4-886d-a24892994566'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_name)
            self.page_main.h_click(L.import_media.music_library.by_descending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.music_library.file_name)
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name, reverse=True)
            result[item_id] = file_name_order == files_name
            if not result[item_id]:
                logger(f'\n[Fail] Files = {files_name}, re-order = {file_name_order}')

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_16
            item_id = '01_01_16'
            uuid = '6d352df4-7589-4504-b52e-b14309957ba5'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_duration)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration, reverse=True)
            result[item_id] = files_duration_order == files_duration
            if not result[item_id]:
                logger(f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}')

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_17
            item_id = '01_01_17'
            uuid = '20cc43dd-b11c-4bb8-b456-c4f769528958'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_click(L.import_media.music_library.sort)
            self.page_main.h_click(L.import_media.music_library.by_file_size)
            self.driver.driver.back()

            files_duration = []
            durations = self.elements(L.import_media.music_library.file_duration)
            for i in durations:
                files_duration.append(i.text)
            files_duration_order = sorted(files_duration, reverse=True)
            result[item_id] = files_duration_order == files_duration
            if not result[item_id]:
                logger(f'\n[Fail] Files duration = {files_duration}, re-order = {files_duration_order}')

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_18
            item_id = '01_01_18'
            uuid = '7959304e-4588-4810-9e69-b00ae850bce3'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            files_name = []
            files = self.elements(L.import_media.music_library.file_name)
            for i in files:
                files_name.append(i.text)

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[0])
            locator = aid("[AID]TimeLineAudio_" + files_name[0])
            result[item_id] = self.page_main.h_is_exist(locator)

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_19
            item_id = '01_01_19'
            uuid = '9ab7a343-335e-426f-8813-f64260c29f38'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)
            self.page_main.h_click(find_string(self.test_material_folder))

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[1])
            locator = aid("[AID]TimeLineAudio_" + files_name[1])
            result[item_id] = self.page_main.h_is_exist(locator)

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_24
            item_id = '01_01_24'
            uuid = 'ae18e001-07c8-4009-995f-d3a4c22792b3'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)
            self.page_main.h_click(find_string(self.test_material_folder))

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[2])
            locator = aid("[AID]TimeLineAudio_" + files_name[2])
            result[item_id] = self.page_main.h_is_exist(locator)

            self.report.new_result(uuid, result[item_id])

            # sce_01_01_25
            item_id = '01_01_25'
            uuid = '990c2772-b52c-494a-8727-9ce83ec70aca'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_edit.click_tool("Audio")
            self.page_main.h_click(find_string("Music"))
            self.page_main.h_click(L.import_media.music_library.local)
            self.page_main.h_click(find_string(self.test_material_folder))

            add = self.elements(L.import_media.music_library.add)
            self.page_main.h_click(add[3])
            locator = aid("[AID]TimeLineAudio_" + files_name[3])
            result[item_id] = self.page_main.h_is_exist(locator)

            self.report.new_result(uuid, result[item_id])

            for key, value in result.items():
                if value != "PASS":
                    print(f"\n[FAIL] {key}")

        except Exception as err:
            logger(f'[Error] {err}')

    def sce_1_1_26(self):
        uuid = 'e0073b1a-7276-4987-9aac-d0b0217dc7c1'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'bmp.bmp'
        self.page_edit.add_master_media('photo', self.test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_photo(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find "{file_name}" on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_27(self):
        uuid = 'be0f1540-c345-4208-a7f2-eb47030f136c'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'bmp.bmp'

        if self.element(L.edit.timeline.master_photo(file_name)).rect['width'] == clip_width:
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] clip_width is not equal'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_28(self):
        uuid = 'df56c95e-cc65-4989-995f-834f834a84f0'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'jpg.jpg'
        self.page_edit.add_master_media('photo', self.test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_photo(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find "{file_name}" on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_29(self):
        uuid = '6a1b2d89-4858-4994-b8d4-0f9325cb704c'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'jpg.jpg'

        if self.element(L.edit.timeline.master_photo(file_name)).rect['width'] == clip_width:
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] clip_width is not equal'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_30(self):
        uuid = '601c0b3b-9aed-4391-b9dc-6d7a8f0b9d3f'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'gif.gif'
        self.page_edit.add_master_media('photo', self.test_material_folder, file_name)
        if self.is_exist(L.edit.timeline.master_photo(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find "{file_name}" on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_31(self):
        uuid = 'a1bae612-908b-440a-bd94-996d7209f532'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'gif.gif'

        if self.element(L.edit.timeline.master_photo(file_name)).rect['width'] == clip_width:
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] clip_width is not equal'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_32(self):
        uuid = 'af08f535-e1bc-4d0b-8ffe-3a2ad17d9a12'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'png.png'
        self.page_edit.add_master_media('photo', self.test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_photo(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find "{file_name}" on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_33(self):
        uuid = '6a4663b3-5dd2-4914-8f49-0b8906ab29a1'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'png.png'

        if self.element(L.edit.timeline.master_photo(file_name)).rect['width'] == clip_width:
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] clip_width is not equal'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_34(self):
        uuid = '608be76b-22f7-4dc0-9624-e13d621a075e'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = "mp4.mp4"
        self.page_edit.add_master_media('video', self.test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find {file_name} on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_35(self):
        uuid = '36c5557c-2896-4aba-9df0-f9f6310bd20c'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = "3gp.3gp"
        self.page_edit.add_master_media('video', self.test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find {file_name} on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_36(self):
        uuid = '05735d3a-c982-4eb2-bd5a-3f0642c8b94f'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        file_name = 'slow_motion.mp4'
        self.page_edit.add_master_media('video', self.test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Cannot find {file_name} on master track'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_1_1_37(self):
        uuid = 'e6e0e636-f91a-4b89-bc7b-c61c49c05baa'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.back_to_launcher()
        self.click(L.main.project.entry)

        if self.page_main.enter_timeline(project_name):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] Can not enter {project_name}'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def test_sce_1_1_1_to_37(self):
        result = {
            "sce_1_1_1": self.sce_1_1_1(),
            "sce_1_1_2": self.sce_1_1_2(),
            "sce_1_1_3": self.sce_1_1_3(),
            "sce_1_1_4": self.sce_1_1_4(),
            "sce_1_1_5": self.sce_1_1_5(),
            "sce_1_1_6": self.sce_1_1_6(),
            "sce_1_1_7": self.sce_1_1_7(),
            "sce_1_1_8": self.sce_1_1_8(),
            "sce_1_1_9": self.sce_1_1_9(),
            "sce_1_1_11": self.sce_1_1_11(),
            "sce_1_1_10": self.sce_1_1_10(),
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

    def test_music(self):
        result = {
            "sce_1_1_12": self.sce_1_1_12(),
            "sce_1_1_13": self.sce_1_1_13(),
            "sce_1_1_14": self.sce_1_1_14(),
            "sce_1_1_15": self.sce_1_1_15(),
            "sce_1_1_16": self.sce_1_1_16(),
            "sce_1_1_17": self.sce_1_1_17(),
            "sce_1_1_18": self.sce_1_1_18(),
            "sce_1_1_19": self.sce_1_1_19(),
            "sce_1_1_20": self.sce_1_1_20(),
            "sce_1_1_21": self.sce_1_1_21(),
            "sce_1_1_22": self.sce_1_1_22(),
            "sce_1_1_23": self.sce_1_1_23(),
            "sce_1_1_24": self.sce_1_1_24(),
            "sce_1_1_25": self.sce_1_1_25(),
            "sce_1_1_26": self.sce_1_1_26(),
            "sce_1_1_27": self.sce_1_1_27(),
            "sce_1_1_28": self.sce_1_1_28(),
            "sce_1_1_29": self.sce_1_1_29(),
            "sce_1_1_30": self.sce_1_1_30(),
            "sce_1_1_31": self.sce_1_1_31(),
            "sce_1_1_32": self.sce_1_1_32(),
            "sce_1_1_33": self.sce_1_1_33(),
            "sce_1_1_34": self.sce_1_1_34(),
            "sce_1_1_35": self.sce_1_1_35(),
            "sce_1_1_36": self.sce_1_1_36(),
            "sce_1_1_37": self.sce_1_1_37()
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

