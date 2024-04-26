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
video_speech = 'speech_noise_1.mp4'
video_20min = '20min.mp4'


class Test_Edit_Pip_Video:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "78ab1470-6a1c-4bea-a701-2f5c5b3e3309",
            "f21f643d-1dfd-4e60-9a3a-4e3c35636fc7",
            "cb7cdc34-8977-414a-9327-bae3026daa56",
            "4c0705b2-575e-4623-aee4-e21cd6b547db",
            "7ece52ad-4414-4520-8d09-9e55b6ee1243",
            "b3d55388-2a9f-4953-950a-48b533f12343",
            "cab94ed5-8ac1-4aa4-9ac3-97f917056430",
            "a3c5fccb-79bb-4e2b-a651-9747a9654cc2",
            "ff44ecfb-8c25-4101-ad8b-e0ddc56ebb15",
            "63c59b46-ae9a-4748-a94d-9b8ecd444e29",
            "a8631a6a-47a8-4a9d-a38d-fb1ce9c5cb70",
            "7fca2456-6aa8-41b3-bdbc-d1f289176b39",
            "810ab717-b468-41cf-988c-8b281e08292d",
            "a94717e2-4b86-4a21-8dd7-97823ca9736e",
            "9cf25121-7076-4c87-884a-63c93b4e5356",
            "876bcf73-a9f2-4c3e-bc2f-96059f888c49",
            "31b9e76f-619c-4f94-811c-0b0900496e61",
            "4e21ec7f-449e-486b-aad5-0ee1bc5846f8",
            "7d7df364-38c2-4d45-9fa9-ce3cae6bfe38",
            "f97da3a6-0d64-45b3-8201-2e7e2336c2fa",
            "bca6fb9f-5ce7-44b6-980d-065fcdafd61a",
            "ea51d65a-55c5-4eb0-b8e6-43015d6ccc3a",
            "095b754e-12bd-4632-bb6c-7a1ecdc42cac",
            "1df35c8c-b0f1-4fba-b1af-735859fb5636",
            "4513adcd-71ae-4216-b964-b5b3b7ac93a0",
            "1704628e-aaf1-427c-b338-0b7b8d35a14e",
            "c4ba980f-4fd9-4f56-8c84-afc284195d42",
            "52acb456-a6dc-41cd-aaff-cdcbd88e1b13",
            "94cf4fdb-08b6-4a23-aa1f-364f2d6e786f",
            "a1053119-8585-4449-891b-1838f01b34ee",
            "9f23587c-8ab6-4ea3-9459-4d467e0cd29f",
            "8eb18770-bb22-476c-9671-39bf8bbc1cf6",
            "b57c6831-5385-42cd-9fb8-af4cb4e3e7c2",
            "104f947d-4961-405d-aa6e-4d6ac4cc9e67",
            "7e0777e4-6eb7-42fc-8163-a8f0c9f25ed6",
            "9f6a090b-7abc-4580-8748-99004a32fc2c",
            "6fbea7d8-1d14-48ef-89f6-86200b1aba2f",
            "58af193d-c40c-4f17-bfa0-51bb68edacbf",
            "c255c56d-098c-4666-94c9-0df6f1356bfa",
            "98c3a9d2-ce1e-4315-ae5a-6c76ba9f8051",
            "938a20c3-a928-42c6-b6b1-42c60e235451",
            "43f56073-1ecc-4cf5-b468-e371cacb6683",
            "c7845402-869d-4288-a38b-7e58610a0b0f",
            "f24b2d4f-40db-40ce-aa3a-a3bcaac94459",
            "7266a587-627d-4cb6-8199-1b470b7ff19d",
            "3842593b-e784-4acd-a0e8-24715a6b879c",
            "8d6ee320-ef40-433c-8736-b31e543ce398",
            "dd05d8d6-0af3-42ef-93f5-dad7710ce4bf",
            "e6ad83c3-5243-4d72-a133-ae807742b630",
            "100fc579-75a9-4806-8bc2-72c727771931",
            "00ec0622-77a5-4f68-a03a-0807b843cb42",
            "da02a1ac-f2a1-4273-8868-ce6f51bdad3f",
            "0b007f38-f986-4657-9eb4-40f20c6d6254",
            "12f1c8d8-722f-43d1-84d8-d5041977e833",
            "63a33e02-9f1e-4232-9a65-06f53e5d0c1f",
            "8181f989-8d8e-44f8-af47-b5a62eb34f98",
            "f3de9467-4e4d-477d-99b5-d7b46ffed2b7",
            "c1c9864d-1077-4edd-ad20-dec2d4352738",
            "e5d29f7b-d475-4fbe-8b21-5ef244fce9ab",
            "306b214b-79ca-4374-8a9e-743f82a9e3f7",
            "235d7957-8cc8-4063-8d0d-598321c1925a",
            "73f3b9a3-b4e4-48d3-90d4-7e1b0da3982e",
            "71747c37-0060-456e-b505-571749e421ee",
            "8c39c877-58e4-4a85-9129-f007047da218",
            "9f56056e-6b8f-4b81-9e96-4dadb806c016",
            "22214050-b97b-461f-8d89-1e31d4829de3",
            "bc00fa21-69b1-4e6b-acab-2a130dd6d264",
            "3e125a66-75d9-4bed-9b4d-0addc54e14d6",
            "05ecea70-570e-4ca4-8823-ef58caa911c7",
            "d8d0290f-559f-4911-8482-4e0aa95b2adb",
            "4e734c83-4be7-43a3-99e6-304adf9e772d",
            "a31bcc34-8f1c-4f3b-9ae8-c54f2eb675cb",
            "1556c077-a904-4b49-85ff-a6a3ab8cfe34",
            "c4d6243c-2cdd-4ae8-9c84-79cb60e99b6f",
            "3aee482e-f94c-4a57-81f7-2253b8777d04",
            "fef0ac7b-fff0-4951-98a9-e38063b25cb0",
            "494445f7-82ec-4085-8e5b-1610c5b4ebea",
            "b84a46b9-5911-46cf-8040-72008f428db8",
            "105b669a-645f-437f-9f3a-f7437d1e635f",
            "b4253a0a-c392-4334-b5fc-20119c17f4a1",
            "01a32a8c-161f-48e3-a4ed-ffb330c2ad86",
            "9b7b8b97-ce50-4091-8230-f3e00cdaf17e",
            "715476a1-4f1d-4364-a61e-4040d362b2df",
            "393f107c-494d-430c-980c-73ae3f411592",
            "7ef130d8-fbbd-440b-936e-7b4825a29652",
            "c1005ef7-ce2c-47fa-8d87-6522fbe5ce57",
            "2f6a9ad5-6d17-4a58-9ed4-d41a4005c3fe",
            "26be50e4-83af-45f4-ae1c-e713cd4b9260"
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

    def sce_8_4_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('video', test_material_folder, video_9_16)

            if self.is_exist(L.edit.pip.clip()):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Clip is not exist')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('video', test_material_folder, video_9_16)

            return "FAIL"

    def sce_8_4_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            x = self.element(L.edit.pip.clip()).rect['width']//2
            self.page_edit.scroll_playhead(-x)
            self.page_edit.click_sub_tool('Split')

            if self.is_exist(L.edit.pip.clip(2)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] 2nd Clip is not exist')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media('video', test_material_folder, video_9_16)
            self.page_edit.click_sub_tool('Split')

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        for func in dir(self):
            if func.startswith('sce_'):
                if getattr(self, func)() != "PASS":
                    print(f'[{func}] FAIL')
