import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from appium.webdriver.common.touch_action import TouchAction

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import REPORT_INSTANCE as report
from .conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_Shortcut_AI_Art:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "48d19908-e282-41d9-add5-90ce1567f138",
            "80cdfb23-03af-4464-855f-fb9a77d59cff",
            "8d4e61e9-9aad-42fa-9ba7-91dad2fd7b5e",
            "0f8703b9-5db7-4ec6-8bb2-09edaee35c02",
            "667ae341-b459-46af-b61c-663ef5ca053e",
            "25bc62cb-8803-4db1-b0f8-ae9c86cd9f06",
            "fb9398e2-6458-4f36-a4f4-14e32487b4eb",
            "3d60edab-0124-4832-8fff-a794ac340a10",
            "ceb40aa8-3476-4166-8bd2-773bdc78054c",
            "b46e6f52-3f2d-4e58-8e8a-9687bd56b07d",
            "bc9b8d2c-ec5b-4e71-8f1a-5da9c43be4a6",
            "ccbfd867-fe98-4469-b1e4-7b87ba09ae98",
            "635d86b3-42bf-4456-ada1-3fdc37fe9dbc",
            "07b23bb0-3f43-42b2-822e-643bb4f6d602",
            "ed6c0971-fac8-44a1-9f0c-07990192b8ad",
            "4a170597-3750-4a1b-b706-1adfc49a1537",
            "3e98b7b2-8ff3-4aa5-a3bd-a7115cc6cf60",
            "fb7ee301-2025-4635-93bb-20c192f1aa10",
            "f5558c01-e90a-4338-8f2d-7abc58821b23",
            "984ba6f4-3225-4ebe-8f23-2e897b68dffa",
            "99ef39e1-fa00-40ee-bbb6-f408610f41ee",
            "c26e0639-34fa-440d-9f41-f17b48fae60b",
            "3e688024-9635-4d85-93ff-a010ffeed223",
            "8c32ebbb-5c9a-4a02-9fea-4ee5911696c6",
            "84f04677-65ef-4018-a629-805d9749d70a",
            "7613f991-1604-4454-92b1-b003ab1f9c4f",
            "ab5b9165-51da-412c-b3cb-e3c94ee6ba80",
            "bcd0c102-cf99-4264-a934-8c75484e5116",
            "f8a784ed-e06a-4d6b-b5a9-4ea7422c2f23",
            "117ed5c0-7149-4ede-a7fa-fbc68305dc2c",
            "b698fb43-206b-4a84-b182-7b48ce5894dd",
            "5b456175-2a3f-4ce3-a3af-7cc87838cbf6",
            "d4f46875-2448-4ab8-885e-e70d20b6561e",
            "651ca599-92b2-4b86-82a7-9f35efc74756",
            "e3561a22-3b60-4b5a-9c87-37c80d599771",
            "ae65ee50-ef45-4f57-8223-7f466fdfe956",
            "96abb18e-c705-4db9-a0e7-6db4578f7dd4",
            "57f6fe29-f049-47d9-9319-672606f60591",
            "5e99d345-7d6a-49cf-8e7d-f4cd95b8e8c0",
            "dd2d455f-fdf1-4ea0-be19-9be59fc75402"
        ]

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

        report.set_driver(driver)
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='medium', video_fps=30)

    def sce_6_11_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Art')

            if self.is_exist(find_string('AI Art')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Demo page')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Art')

            return "FAIL"

    def sce_6_11_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.demo_back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_11_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Art')
            self.click(L.main.shortcut.try_it_now)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Art')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_11_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_11_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            for wait in range(60):
                if self.is_exist(find_string('Cancel')):
                    time.sleep(2)
                else:
                    break

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter AI Art')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            return "FAIL"

    def sce_6_11_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.editor_back)

            if self.is_exist(find_string('Add Media')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Art')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_6_11_1": self.sce_6_11_1(),
                  "sce_6_11_2": self.sce_6_11_2(),
                  "sce_6_11_3": self.sce_6_11_3(),
                  "sce_6_11_4": self.sce_6_11_4(),
                  "sce_6_11_5": self.sce_6_11_5(),
                  "sce_6_11_6": self.sce_6_11_6(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")