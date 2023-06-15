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


import datetime
dt = datetime.datetime.today()

files_by_date = ["bmp.bmp", "gif.gif", "jpg.jpg", "png.png"]
files_by_resolution = ["gif.gif", "bmp.bmp", "jpg.jpg", "png.png"]
files_by_file_size = ["jpg.jpg", "bmp.bmp", "gif.gif", "png.png"]

test_material_folder = TEST_MATERIAL_FOLDER
test_material_folder_01 = TEST_MATERIAL_FOLDER_01
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_SFT_Scenario_01_02:
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
        yield
        driver.driver.close_app()

    def sce_01_02_01(self):
        item_id = '01_02_01'
        uuid = 'c2420360-95d7-4591-afbc-33ae908c62f0'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(skip_media=False)
        self.page_media.select_local_photo(test_material_folder, "9_16.jpg")
        self.click(L.edit.menu.home)
        if self.is_exist(L.main.premium.pdr_premium): # Churn Recovery
            self.driver.driver.back()
        project_name_default = 'Project {:02d}-{:02d}'.format(dt.month, dt.day) + "(1)"
        global project_name
        project_name = self.page_main.h_get_element(L.main.project.project_name()).text
        if project_name == project_name_default:
            result = True
        else:
            result = False
            logger(f'[Info] Project Name: {project_name}')
            logger(f'[Info] Default Project Name: {project_name_default}')
            logger('\n[Fail] Project Name incorrect')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_02(self):
        item_id = '01_02_02'
        uuid = '8522a2ed-042c-4da4-bed6-8fb2512a6b2b'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.main.project.project_name())
        project_ratio = self.page_edit.preview_ratio()
        if project_ratio == '9_16':
            result = True
        else:
            result = False
            logger(f'\n[Fail] Project ratio is {project_ratio}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_03(self):
        item_id = '01_02_03'
        uuid = '0ad5f14b-946f-4668-a3e1-11e24e4883d0'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        duration_result = self.page_edit.check_setting_image_duration(10.0, False)
        timeline_result = self.page_edit.check_timeline_image_duration(False)
        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)

        if timeline_result == duration_result == '10.0 s':
            result = True
        else:
            result = False
            logger(f'\n[Fail] Not synced with sec_1.1.5'
                   f'timeline_result = {timeline_result}, duration_result = {duration_result}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_04(self):
        item_id = '01_02_04'
        uuid = 'df45dd97-c0c2-47cc-9ac1-cf7d473a06b9'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        duration_result = self.page_edit.check_setting_image_duration(0.1)
        timeline_result = self.page_edit.check_timeline_image_duration()
        self.page_main.h_click(L.edit.timeline.item_view_border)
        self.page_main.h_click(L.edit.menu.delete)

        if timeline_result == duration_result == '0.1 s':
            result = True
        else:
            result = False
            logger(f'\n[Fail] timeline_result = {timeline_result}, duration_result = {duration_result}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_05(self):
        item_id = '01_02_05'
        uuid = '810a5752-cfdb-4847-a7cc-f5374ef7a832'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        duration_result = self.page_edit.check_setting_image_duration(10.0)
        timeline_result = self.page_edit.check_timeline_image_duration()
        global clip_width
        clip_width = self.page_main.h_get_element(L.edit.timeline.item_view_border).rect['width']

        if timeline_result == duration_result == '10.0 s':
            result = True
        else:
            result = False
            logger(f'\n[Fail] timeline_result = {timeline_result}, duration_result = {duration_result}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_06(self):
        item_id = '01_02_06'
        uuid = 'f9c26adf-1a64-4799-8677-f0c4a62a1d2f'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

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

    def sce_01_02_07(self):
        item_id = '01_02_07'
        uuid = '850789d6-bd74-41e1-a831-077978e02b13'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.h_click(L.edit.settings.menu)
        self.page_main.h_click(L.edit.settings.preference)
        self.page_main.h_click(L.timeline_settings.settings.default_pan_zoom_effect)
        self.driver.driver.back()
        self.page_main.h_click(L.edit.preview.import_tips_icon)
        self.page_media.select_local_photo(test_material_folder, '9_16.jpg')
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

    def sce_1_2_8(self):
        uuid = 'dd7500a6-e070-48ec-b3bf-68fb668bca80'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.preview.import_tips_icon)
            self.page_media.switch_to_photo_library()

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
            self.page_media.switch_to_photo_library()

            return "FAIL"

    def sce_1_2_9(self):
        uuid = '343131de-0a4c-4e60-9bba-a1a8f694c7d4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            for retry in range(20):
                if not self.is_exist(find_string("jpg.jpg")):
                    self.driver.swipe_element(L.import_media.media_library.frame, 'up', 300)
                else:
                    break

            if self.is_exist(find_string("jpg.jpg")):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find the file "jpg.jpg"'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.switch_to_photo_library()

            return "FAIL"

    def sce_1_2_10(self):
        uuid = '3c73bac0-4dd1-4850-9d6f-4433fa65f6be'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
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
            self.page_media.switch_to_photo_library()
            self.click(L.import_media.sort_menu.sort_button)

            return "FAIL"

    def sce_01_02_09(self):
        item_id = '01_02_09'
        uuid = '4bd10d48-6e33-478a-9cc1-20a70e22cb98'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        if not self.is_exist(find_string("Duration"), 0.1):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Found "Duration')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_10(self):
        item_id = '01_02_10'
        uuid = '33656e1b-fffb-45f6-85b3-f10b0d58bede'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.by_name)
        self.click(L.import_media.sort_menu.ascending)
        self.driver.driver.back()

        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        file_name_order = sorted(files_name)
        if file_name_order == files_name:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_11(self):
        item_id = '01_02_11'
        uuid = '67aefd21-d3c7-42bf-9106-16d71158881e'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_date)
        self.click(L.import_media.sort_menu.ascending)
        self.driver.driver.back()

        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_date:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_date = {files_by_date}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_12(self):
        item_id = '01_02_12'
        uuid = '4c7b42e4-6582-4d80-abe3-496ae6cb6591'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_resolution)
        self.click(L.import_media.sort_menu.ascending)
        self.driver.driver.back()

        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_resolution:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_resolution = {files_by_resolution}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_13(self):
        item_id = '01_02_13'
        uuid = '75b42e34-7a0e-4ec0-befc-c78fa42119a2'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_file_size)
        self.click(L.import_media.sort_menu.ascending)
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

    def sce_01_02_14(self):
        item_id = '01_02_14'
        uuid = '6f5f3752-df90-4614-83ca-2f9270ac0729'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_name)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        files_by_name = sorted(files_name, reverse=True)
        if files_name == files_by_name:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_name = {files_by_name}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_16(self):
        item_id = '01_02_16'
        uuid = 'd8c6c9c0-4ce1-449c-819a-3a7fb28ca1eb'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_resolution)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_by_resolution.reverse()
        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_resolution:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_resolution = {files_by_resolution}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_17(self):
        item_id = '01_02_17'
        uuid = '8ea70fc8-3387-4078-b199-e09757399aa2'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_file_size)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_by_file_size.reverse()
        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_file_size:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_file_size = {files_by_file_size}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_15(self):
        item_id = '01_02_15'
        uuid = 'ddd8f772-876d-449b-9720-558b6af64796'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.sort_menu.sort_button)
        self.click(L.import_media.sort_menu.by_date)
        self.click(L.import_media.sort_menu.descending)
        self.driver.driver.back()

        files_by_date.reverse()
        files_name = []
        files = self.elements(L.import_media.menu.file_name(0))
        for i in files:
            files_name.append(i.text)
        if files_name == files_by_date:
            result = True
        else:
            result = False
            logger(f'\n[Fail] files_name = {files_name}, files_by_date = {files_by_date}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_18(self):
        item_id = '01_02_18'
        uuid = 'b7171c98-b2b0-4d60-8833-85e29c1a1b9b'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(L.import_media.media_library.photo.photo_capture)
        self.click(L.import_media.media_library.photo.take_picture)
        self.click(L.import_media.media_library.photo.camera_ok)
        capture_photo_name = "PDR_" + "{:04}{:02}{:02}".format(dt.year, dt.month, dt.day)
        global capture_1st_file
        capture_1st_file = self.element(L.import_media.media_library.file_name(index=1)).text

        if capture_photo_name in capture_1st_file:
            result = True
        else:
            result = False
            logger(f'\n[Fail] 1st files_name = {capture_1st_file}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_19(self):
        item_id = '01_02_19'
        uuid = '7e39264d-815e-4537-8bb2-b35b69094a00'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.click(find_string(capture_1st_file))
        self.click(L.import_media.media_library.apply, timeout=1)

        if self.element(L.edit.timeline.master_photo(capture_1st_file)).rect['width'] == clip_width:
            result = True
        else:
            result = False
            logger(f'\n[Fail] clip_width is not equal')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_20(self):
        item_id = '01_02_20'
        uuid = 'd77ca83a-8d01-481a-a8f8-0fbe74bdead7'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        file_name = 'gif.gif'
        self.page_edit.add_master_media('photo', test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_photo(file_name)):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "{file_name}"')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_21(self):
        item_id = '01_02_21'
        uuid = 'e7f30451-f1cd-4044-8d0a-ecd0426ed9c5'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        if self.element(L.edit.timeline.master_photo('gif.gif')).rect['width'] == clip_width:
            result = True
        else:
            result = False
            logger(f'\n[Fail] clip_width is not equal')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_22(self):
        item_id = '01_02_22'
        uuid = '536fdf94-419c-4e46-bd0f-74867fbcfb3b'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        self.page_media.select_local_photo(test_material_folder, 'png.png')

        if self.is_exist(L.edit.timeline.master_photo('png.png')):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "png.png"')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_23(self):
        item_id = '01_02_23'
        uuid = 'a1b97f8a-3300-41f7-b4a4-942fbb40c3d1'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        if self.element(L.edit.timeline.master_photo('png.png')).rect['width'] == clip_width:
            result = True
        else:
            result = False
            logger(f'\n[Fail] clip_width is not equal')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_24(self):
        item_id = '01_02_24'
        uuid = '5379c7a2-0041-47ff-a12d-a861a972cbc9'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')

        if self.is_exist(L.edit.timeline.master_photo('jpg.jpg')):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "jpg.jpg"')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_25(self):
        item_id = '01_02_25'
        uuid = 'd083ff85-3ea6-4b05-b8c7-076dc88ff9bd'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        if self.element(L.edit.timeline.master_photo('jpg.jpg')).rect['width'] == clip_width:
            result = True
        else:
            result = False
            logger(f'\n[Fail] clip_width is not equal')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_26(self):
        item_id = '01_02_26'
        uuid = '79c8d498-352b-41bd-88bb-a638cd3b277b'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        self.page_media.select_local_photo(test_material_folder, 'bmp.bmp')

        if self.is_exist(L.edit.timeline.master_photo('bmp.bmp')):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find "bmp.bmp"')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_27(self):
        item_id = '01_02_27'
        uuid = '0acd0622-1ada-4e6c-8413-f54537b22d79'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        if self.element(L.edit.timeline.master_photo('bmp.bmp')).rect['width'] == clip_width:
            result = True
        else:
            result = False
            logger(f'\n[Fail] clip_width is not equal')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_28(self):
        item_id = '01_02_28'
        uuid = '29ac056d-3693-43a4-bc98-1ac3c7b72236'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        self.click(L.import_media.media_library.Video.video_capture)
        self.click(L.import_media.media_library.Video.start_recording)
        time.sleep(1)
        self.click(L.import_media.media_library.Video.stop_recording)
        self.click(L.import_media.media_library.Video.camera_ok)
        capture_video_name = "{:04}{:02}{:02}_".format(dt.year, dt.month, dt.day)
        capture_1st_video = self.element(L.import_media.media_library.file_name(index=1)).text

        if capture_video_name in capture_1st_video:
            result_media_room = True
            self.click(find_string(capture_1st_video))
            self.click(L.import_media.media_library.apply, timeout=1)
            self.click(find_string('Use Original'), 3)
            if self.is_exist(L.edit.timeline.master_video(capture_1st_video)):
                result_timeline = True
            else:
                result_timeline = False
                logger(f'\n[Fail] Cannot find {capture_1st_video} in timeline')

        else:
            result_media_room = False
            result_timeline = False
            logger(f'\n[Fail] 1st capture_video_name in media room = {capture_1st_video}')

        if result_media_room and result_timeline:
            result = True
        else:
            result = False
            logger(f'\n[Fail] result_media_room = {result_media_room}, result_timeline = {result_timeline}')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_29(self):
        uuid = '39b042b6-26d2-4730-b738-f02121f1862e'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        file_name = "mp4.mp4"
        self.page_media.select_local_video(test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find {file_name} on master track')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_30(self):
        uuid = '22b27d9e-e0b7-4f95-b27b-7824132587b4'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        file_name = "3gp.3gp"
        self.page_media.select_local_video(test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find {file_name} on master track')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_31(self):
        item_id = '01_02_31'
        uuid = '3170f572-9bc6-4dbd-93db-4326054b3d76'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media()
        file_name = "mkv.mkv"
        self.page_media.select_local_video(test_material_folder, file_name)

        if self.is_exist(L.edit.timeline.master_video(file_name)):
            result = True
        else:
            result = False
            logger(f'\n[Fail] Cannot find {file_name} on master track')

        self.report.new_result(uuid, result)
        return "PASS" if result else "FAIL"

    def sce_01_02_32(self):
        item_id = '01_02_32'
        uuid = '23c3f114-a298-47db-8532-104790d36694'
        logger(f"\n[Start] sce_{item_id}")
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
        result = {"sce_01_02_01": self.sce_01_02_01(),
                  "sce_01_02_02": self.sce_01_02_02(),
                  "sce_01_02_03": self.sce_01_02_03(),
                  "sce_01_02_04": self.sce_01_02_04(),
                  "sce_01_02_05": self.sce_01_02_05(),
                  "sce_01_02_06": self.sce_01_02_06(),
                  "sce_01_02_07": self.sce_01_02_07(),
                  "sce_1_2_8": self.sce_1_2_8(),
                  "sce_1_2_9": self.sce_1_2_9(),
                  "sce_1_2_10": self.sce_1_2_10(),
                  "sce_01_02_09": self.sce_01_02_09(),
                  "sce_01_02_10": self.sce_01_02_10(),
                  "sce_01_02_11": self.sce_01_02_11(),
                  "sce_01_02_12": self.sce_01_02_12(),
                  "sce_01_02_13": self.sce_01_02_13(),
                  "sce_01_02_14": self.sce_01_02_14(),
                  "sce_01_02_16": self.sce_01_02_16(),
                  "sce_01_02_17": self.sce_01_02_17(),
                  "sce_01_02_15": self.sce_01_02_15(),
                  "sce_01_02_18": self.sce_01_02_18(),
                  "sce_01_02_19": self.sce_01_02_19(),
                  "sce_01_02_20": self.sce_01_02_20(),
                  "sce_01_02_21": self.sce_01_02_21(),
                  "sce_01_02_22": self.sce_01_02_22(),
                  "sce_01_02_23": self.sce_01_02_23(),
                  "sce_01_02_24": self.sce_01_02_24(),
                  "sce_01_02_25": self.sce_01_02_25(),
                  "sce_01_02_26": self.sce_01_02_26(),
                  "sce_01_02_27": self.sce_01_02_27(),
                  "sce_01_02_28": self.sce_01_02_28(),
                  "sce_01_02_29": self.sce_01_02_29(),
                  "sce_01_02_30": self.sce_01_02_30(),
                  "sce_01_02_31": self.sce_01_02_31(),
                  "sce_01_02_32": self.sce_01_02_32(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
