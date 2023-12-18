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


class Test_Shortcut_Mosaic:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "c32ebb34-3d67-4daf-8bcc-5ee7f2cc30d2",
            "a2b0b503-fde8-4486-9ce4-6f0cec0815d6",
            "25d484be-443f-4927-9b34-e38d30847844",
            "7be796ed-7501-41e9-a3e6-bfd47ea4c748",
            "b666f8b3-e12f-40d3-b16c-2140d7105351",
            "3288daa5-1074-4330-8d20-7fcfc789d397",
            "19f971c8-dd05-4c2e-8aae-0874a01d9abf",
            "8bcdee9e-5fb0-4450-bd3b-3059de2692c4",
            "a124093b-8b20-4d64-beb2-0cd4a58c14ce",
            "9f23eb3b-9d2d-4ce3-8d07-2830ee4742d0",
            "0736e756-acca-4a5e-94a8-35ab5c5a5b58",
            "f20eed0f-bd2a-4468-8120-dca8e1d74fc5",
            "8f36ae33-54b5-42da-b9fe-8bc2b844a5a0",
            "4ee67e41-e137-4776-8514-a64ff279c122",
            "e6c78f7a-ad05-48c1-af13-999609b0e28c",
            "b18bbf3e-0e17-406a-a12c-4c401131b08c",
            "a3f13592-2a62-47ff-968f-8d23312f5436",
            "f73ba642-1205-46d4-b3f9-046479b74c10",
            "b6996ebd-88bd-4123-986e-3a4ded2e742c",
            "7ffdb2e9-6768-4c66-a602-7bf2c3821ec6",
            "37b1ff30-4581-4f0b-abeb-8ae6047447ea",
            "49b5c012-0324-4b5b-952b-ac83865dda73",
            "200ed7e3-f218-452d-b667-471a04b94b6a",
            "7ce44a58-0257-4fce-8a99-676900545b93",
            "cd80a733-f0a9-4513-abe1-fc9e2c3cb21a",
            "49b5c60e-f55f-41dc-8e5f-29497dd96396",
            "7101da2c-430c-4515-9d20-62ecca25d53d",
            "b609fbb3-fa70-4831-a55f-1871ebbb51e1",
            "ae042021-7423-499c-b346-d5e32f4cc1b3",
            "c7d0adcd-9533-4706-b997-8276d9454c65",
            "b72ef20a-dece-4e49-b969-f24ff17944bb",
            "d39baa3b-edf7-47be-9ed9-60e99c01dc34",
            "b0658ed5-66b3-4a8a-93f6-34087163136d",
            "a0fac691-9ec7-4a82-b9a6-643db14db2a4",
            "034e09de-fc51-46fb-af58-254678f43a3c",
            "c14e60eb-8d70-4b51-ad50-898da23bc7e5",
            "a916b26b-9d2e-4790-95ac-eea6a5d1d5c1",
            "6ab16a30-b159-40ed-a1a1-2edec62866a6",
            "2ad56cfa-63d5-4d28-abee-0f76f45c1dd2",
            "f809e0c3-3c79-496a-a5e4-981e9009fe3b",
            "014ea2ac-8eaa-4127-99bc-edb421cc8a92",
            "0f1b9260-7680-455b-a377-cf019cb48369",
            "615e2722-b492-48fe-a029-9f679f12e81e",
            "4fff43c9-a724-4102-bd1e-54646b4aeac7",
            "c137b369-9dda-4551-8270-6fc30a58987c",
            "24d598eb-2ae5-4b4a-b25d-c613fdc02c0d",
            "8c766d23-1abc-4ab8-8076-4796ca14b8b9",
            "aed6836e-9636-4dff-993c-e6f0818d0241",
            "6e8deacf-1989-4be3-8333-68fe86863cf1",
            "4034396c-2d45-4b1b-8ec0-08de5b8b7c1e",
            "2e749601-63d0-4ad9-880d-7896aefcdafa",
            "f5f2b997-b107-4972-9226-526b536ee205",
            "9c507824-11de-425e-aba7-8260eb1feb22",
            "d1b612de-dd7c-43fb-9e82-4b6ba930f3fd",
            "576fc13e-a595-4b0a-89e1-27e3cf0ed391",
            "4eaa269e-639c-4bba-9e49-6e2c32177f06",
            "7ebfcc49-0602-4fa6-809c-3a730aefcd75",
            "099e1cf1-d8bd-4f08-b774-a7ff6b5d9428",
            "6374bb9b-3e4c-4db1-8f43-e6c1a3652bd2",
            "805d17e7-b563-4998-b2b8-754c8781452d",
            "6daf140a-e134-4b40-94f0-6246b52bf7b5",
            "0c4cc430-46af-4e55-8520-08431b481dc5",
            "a3f54bd0-0cfb-41b7-b3ee-e3661c50e4e2",
            "4280c922-8444-4e3f-809a-e3c899816608",
            "66e83d57-f633-4d6e-89d7-76ea1b57c71a",
            "f9cbafd6-c8e9-44a5-8eb4-b9e09c2b3b24",
            "5bc1fe50-9136-4f45-ab88-55066f968813",
            "7deabf4a-ab62-43f8-b367-6c2211c35ecb",
            "0ad81d6a-d5d9-4ed2-b895-189ac2577a4d",
            "0d1e7daa-f94e-4481-9a53-c58e9e946fed",
            "735662e8-14f8-4edc-a757-6281108c32a1",
            "d3f5cb9f-f869-4c5f-a292-5b838243d6bb",
            "d6218f33-0086-4f58-b984-7a4719189029",
            "ad7b7fe0-3fc1-49ac-897a-cff26b851adc",
            "942c59c4-f8d0-4a8b-afc8-87abaf8e0794",
            "7cfb070a-7639-462e-9b34-fbb6f6dae7ff",
            "533c3b67-6dda-4798-a4f6-b60372299bc6",
            "01e44b14-a80e-4fdf-a68d-cb62a800ba41",
            "67beb990-791d-47cc-9b98-0632d56ef483",
            "1931e26b-6f5a-4f57-b926-4cc58505586e",
            "d8fdfa0a-0171-4854-9587-bd6bd8ccf476",
            "f098d25a-595f-400f-ad7d-fc1c86bd2172",
            "29e6948d-8552-4be0-9614-27a3b80639c4",
            "a2630256-d404-4107-a9ef-8c47632d054b",
            "92b02a02-3db8-4d35-81a0-68132defa0e4"
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

    def sce_6_9_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Mosaic')

            if self.is_exist(find_string('Mosaic')):
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
            self.page_main.enter_shortcut('Mosaic')

            return "FAIL"

    def sce_6_9_2(self):
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

    def sce_6_9_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Mosaic')
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
            self.page_main.enter_shortcut('Mosaic')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_9_4(self):
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

    def sce_6_9_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_shortcut('Mosaic')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_back)

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
            self.page_main.enter_shortcut('Mosaic')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_9_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.driver.swipe_element(L.import_media.media_library.left_indicator, 'right', 50)
            self.driver.swipe_element(L.import_media.media_library.right_indicator, 'left', 50)
            self.click(L.import_media.media_library.trim_next)

            for wait in range(60):
                if self.is_exist(find_string('Cancel')):
                    time.sleep(2)
                else:
                    break

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Mosaic')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Mosaic')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)

            return "FAIL"

    def sce_6_9_7(self):
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
            self.page_main.enter_shortcut('Mosaic')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_9_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_local_video(test_material_folder, video_9_16)

            for wait in range(60):
                if self.is_exist(find_string('Cancel')):
                    time.sleep(2)
                else:
                    break

            if self.is_exist(find_string('Export')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Mosaic')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Mosaic')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)

            return "FAIL"

    @report.exception_screenshot
    def test_sce_6_1_1_to_135(self):
        result = {"sce_6_9_1": self.sce_6_9_1(),
                  "sce_6_9_2": self.sce_6_9_2(),
                  "sce_6_9_3": self.sce_6_9_3(),
                  "sce_6_9_4": self.sce_6_9_4(),
                  "sce_6_9_5": self.sce_6_9_5(),
                  "sce_6_9_6": self.sce_6_9_6(),
                  "sce_6_9_7": self.sce_6_9_7(),
                  "sce_6_9_8": self.sce_6_9_8(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
