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


class Test_Shortcut_Text_to_Image:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "d3d8322a-edb0-4b4f-89b7-f7cf8e0a71aa",
            "aa600f94-7c6b-41d9-8e0a-9c9bbc963935",
            "e912437c-d514-4c1f-b4f4-47e1f0234ce1",
            "bea37caf-40cd-47d2-a316-b12c0441c927",
            "021083a5-f982-400f-8fb3-87863c848e79",
            "ee4968d4-2d29-4f72-9ba0-d2588f007b9e",
            "b8ae49ed-701a-4698-92d7-c602c80cc4d2",
            "6577e71f-5e19-4ff4-82ac-69e76975caca",
            "4640a4ea-5dbc-4013-858c-5fab0bf3c2d4",
            "c6f6ba9e-25a9-4c11-8599-3876a3d9c512",
            "9781f780-93e6-40a6-8f3e-d1e618ae0df8",
            "ade9fd49-f8fe-47d8-929a-0fd3f8d945bf",
            "a3cddf7b-1830-4015-9273-1441948bddbe",
            "66a915d7-3796-4965-bc26-73ebc40fe249",
            "a6b46d18-8cf4-4797-92c3-f1744276a404",
            "3f43ff74-8a33-4aca-a8d7-50cbd6d76f69",
            "61a7dfb3-b497-447f-8f91-5e21d63b39e5",
            "578fdd8c-695e-427e-b752-54cbf331d8b1",
            "d3f0568b-09b8-411e-840e-4be7c5f64964",
            "4e766536-a85b-4ac4-841a-d87866b7adc7",
            "c5250e6d-7670-4013-9173-0e32ab48752d",
            "79f30a32-5db4-4dc8-b199-c32fa42ba1ea",
            "90d7e6e6-ce49-4bdd-8e3e-6db310c9c09c",
            "9dd68858-362e-4df8-a67d-aee1543176ae",
            "899bb49b-7957-4742-90f6-51062e9f142d",
            "f27e41fb-95df-4b17-b425-3bf8f466a1c2",
            "836e88ae-89e2-4de3-afe0-94f6e17aee35",
            "7ad05c14-5abd-48d1-9670-cc6909e29c16",
            "0b2e4098-63a3-4119-831e-6b30e25b84d7",
            "514960bf-5e10-4a54-8686-8938bd64e8f6",
            "24d477eb-6a3c-4d74-869f-b879a05acaa6",
            "7b7c28ce-588a-47b7-aee4-2ec0cd271c4b",
            "9600575e-a806-4903-a293-b3b0fc6c7a34",
            "19de822c-1e2e-4ecd-a688-5f4737fadc04",
            "b52c76bb-d465-4701-bfbd-a300616d1726",
            "15e8f785-1fa6-4bc0-a30c-09825c1aa6a9",
            "ca333b88-d91f-4f1e-a994-a4b9ce1bd931",
            "8c0de644-21de-43ef-8357-8d524ce54603",
            "6e3f9ef7-6e66-4fa5-aaf5-23a6a3237ced",
            "d1f8c78c-f260-4c25-bede-18ff3475564a",
            "d51d0cea-474f-48c1-ae2e-dd77e23185dd",
            "937e3459-953b-4793-bcde-3d2f912a0f1f",
            "521761a3-9924-4b1c-9dd9-35089b47b673",
            "de6dea1d-b679-44d4-9655-5180079af64d",
            "fa7a2c88-8444-4a41-9f43-9107669461cc",
            "287d6bab-e7ba-4420-b646-d9bc1600bd17",
            "3a3b1509-c432-4642-a1e9-397c0d585e61",
            "eb9a40fb-469f-4c9f-a0cb-51ce10dae102",
            "28c16b62-dd84-419a-8947-76dffe8e29e4",
            "cfc3e7ad-c20a-4bef-b9b9-cbfb233234d3",
            "c6b63217-d1c8-4488-b4f1-70af679841f5",
            "a4f2173c-244a-46eb-a964-8619f7141975",
            "1b833935-2be3-4083-8a89-5226a10d1d19",
            "d1bcc7b4-8497-4b83-856c-0ef7ab9841b2",
            "20ce2890-6bf1-42ea-8672-bd24c2f1daf3"
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

    def sce_6_13_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')

            if self.is_exist(find_string('Text to Image')):
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
            self.page_main.enter_shortcut('Text to Image')

            return "FAIL"

    def sce_6_13_2(self):
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

    def sce_6_13_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Text to Image')
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
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.btn_continue)

            return "FAIL"

    def sce_6_13_4(self):
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

    def sce_6_13_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Text to Image')
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
                raise Exception('[Fail] Cannot enter Text to Image')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.btn_continue)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            return "FAIL"

    def sce_6_13_6(self):
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
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.btn_continue)

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_6_13_1": self.sce_6_13_1(),
                  "sce_6_13_2": self.sce_6_13_2(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")