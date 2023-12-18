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


class Test_Shortcut_AI_Scene:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "2225910e-0b45-47f4-add9-16e82a9f12d8",
            "88f114db-88bf-41df-b265-37dbd0be8993",
            "2b4a5bda-4905-4daf-978e-e4c026a046e8",
            "8abf8dc2-26ad-4a98-a943-78e16ff2a242",
            "848b15a3-1177-41f2-8dc8-7863d1fe78bf",
            "dccd057d-c64c-4be1-a0be-5c5599dc8069",
            "d88087b3-0292-4a9f-9c0a-bb1b5030436c",
            "46fd8f72-3f29-453e-bddc-a8e661a002f3",
            "a978935c-f110-4d57-b863-c1c3981a438e",
            "cd8409d7-4f89-4055-9e77-13c5d05d5776",
            "e26842e9-d5f4-4e6b-ae25-d10ba67927e3",
            "22bf3eec-5456-44fd-b0a2-af40225595b0",
            "8d78d81a-0557-4a24-b53a-3e0ac70ecf22",
            "21d37605-68c3-4d40-b091-7e63b1288f5e",
            "fb452667-21cc-45f7-badb-319c05206ade",
            "d61761ed-d79f-4c35-a4b2-84d470b88efa",
            "ed702687-2e82-4e51-a582-ae947e57bd5b",
            "dd9eaadc-7f67-4a46-9c90-ebd998d15574",
            "93671fe4-14dc-4133-be17-319bb41ab067",
            "beecdfde-6877-49d7-9e64-118901b0471f",
            "de1ec679-3185-49de-b8b6-148ec3b56925",
            "0f2138e4-28d3-4a27-b3bf-3a01891c52d3",
            "420f5473-5d47-46f7-aed8-f24da27e23cb",
            "6b0dea3c-70df-47c7-b887-b80c417b4b91",
            "e1dfb1c1-f1c1-4435-b431-e03f20002757",
            "b4fc5ef0-bb27-4fef-b1f8-320ade7cbf38",
            "c3561b94-0d4d-4c19-aea4-dcead96f791c",
            "6ce49e58-42a9-4ebe-b3d3-caa02e1f82ca",
            "8beb7076-d0cb-4cef-8317-578e4de27d13",
            "2f234a60-b2d2-4bcf-8020-1f66fc6ce2d8",
            "7e7bf030-2d6d-4fa5-ba6d-d53eded5602a",
            "6c0c7590-610e-4e13-b37a-a2a153c040d7",
            "5f9a7247-6b48-4be3-9978-40b548f66ffd",
            "da1ec180-9a87-4f14-9703-04ce963716e2",
            "ba03e0ea-0826-42ac-91da-13b32e2f8335",
            "9560441c-28f5-43db-b97b-a3a0c55a32c3",
            "4dbfa18f-5cdc-466d-8437-a7a78847a1e3",
            "f82219cd-3069-4a75-aac7-49a82ebe644b",
            "c625e6af-cc6f-4948-a85a-ff15c79009bd",
            "78fa71c0-6b38-4660-aa91-0fae41b1ef35"
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

    def sce_6_12_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Scene')

            if self.is_exist(find_string('Recommendation')):
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
            self.page_main.enter_shortcut('AI Scene')

            return "FAIL"

    def sce_6_12_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.main.shortcut.close)

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

    def sce_6_12_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)

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
            self.page_main.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)

            return "FAIL"

    def sce_6_12_4(self):
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

    def sce_6_12_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)
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
                raise Exception('[Fail] Cannot enter AI Scene')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            return "FAIL"

    def sce_6_12_6(self):
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
            self.page_main.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_6_12_1": self.sce_6_12_1(),
                  "sce_6_12_2": self.sce_6_12_2(),
                  "sce_6_12_3": self.sce_6_12_3(),
                  "sce_6_12_4": self.sce_6_12_4(),
                  "sce_6_12_5": self.sce_6_12_5(),
                  "sce_6_12_6": self.sce_6_12_6(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")