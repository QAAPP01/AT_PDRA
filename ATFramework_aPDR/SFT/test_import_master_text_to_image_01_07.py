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


class Test_Import_Master_TTI:
    @pytest.fixture(autouse=True)
    def initial(self, driver): 
        logger(f"[Start] {__name__}")

        self.driver = driver
        self.uuid = [
            "42dbc99f-7383-4035-9652-2cf32e2e041d",
            "0ea8afb9-cc8f-4710-ae49-a2f63c066fef",
            "ccc051d2-d00a-4c8a-a268-f062338ee015",
            "c981ff88-0bc6-4946-988b-17c563c5edbe",
            "a9769289-65be-4f86-9f87-4394928adf6f",
            "b417cc6d-c7fc-449d-8b07-742cffe9b3df",
            "3325f2ff-0a61-445a-bb0f-4146ae4e2c46",
            "85e98570-7d67-494a-8583-6e23a7543353",
            "60da5579-fed5-4cb6-90c4-aea66015b4fd",
            "682bea5b-5c88-4bf4-8e98-074b17089c15",
            "8fdad527-324b-4ce4-a8ad-ae6e74149fdf",
            "481127b8-14a4-4acf-8338-ee9784a237e9",
            "bf845d5d-edab-4eca-8697-d15217ea7324",
            "326c2da1-ad2b-4954-a3f0-d87f22dab27d",
            "5c01b8b9-cba4-4d4c-bd3d-673b83da031f",
            "3725a733-60ac-4083-bc6c-f73dced04ede",
            "4f8fde81-901e-4eb2-83be-309b823fc611",
            "cedffd0a-2adc-4686-a0e7-7990ddcf6bb7",
            "70e08488-d9ea-43b0-b088-95631fc37f8c",
            "496741bd-1e6a-4b1c-94d4-14fa20345a41",
            "b5d111da-bc7c-4079-b22d-5fade1a5ded1",
            "a8550be5-598d-43f6-a20d-fd57b7729b2c",
            "5caa5b59-95a1-451a-9847-5eeb146c7741",
            "6a4a8ddf-6605-4337-a03b-9927564df639",
            "3593c586-973c-4ef0-ba8d-b0ec69dac27e",
            "5e5fe612-4ebb-47ad-90fd-bdf0a5cb2761",
            "bdad7a03-17b0-45e4-a173-aea94c16da12",
            "194eae85-4e8c-4a60-bddb-2a1043adae0b",
            "c034e11f-8f34-45c5-a2c4-be382a7e0da2",
            "f7127ecf-d325-4e1f-9aa9-8fb580f9fa5e",
            "6cd3868c-ea3d-46ec-8456-f9af6d94d86d",
            "f142a290-4c40-4a68-ad1c-2134a72fa476",
            "cf9b4d5d-30fe-4643-a5ca-ea4d054ac615",
            "06e5a5cf-67cf-4918-a360-59bbf2930a58",
            "e1efef6f-75e3-4d0b-b91c-6ce63070d91b",
            "abfba9ee-8070-4dea-8612-b332dbbab7b7",
            "dddf7bc3-0814-4a84-9ebc-343ec15aa4b4",
            "47a0293f-b107-4e56-af61-fbb68d04c882",
            "7c702cf8-7d98-483c-be68-8db90a015712",
            "bde17692-5d6b-494b-89a1-43f937f1ef05",
            "fd27973c-a732-4c93-b4e3-9c28918e26d0",
            "6b02522e-017a-49b2-ac33-2999264aeca2",
            "00b2304e-003a-47ce-9f48-bff6cf4af89b",
            "8d0a4176-f1ec-4d18-854c-e2f8a588c300",
            "3e74e616-b173-493d-ad95-e96a84f4e7d8",
            "afa130e8-ff89-43e5-9605-fe3d072f64ba",
            "37217e83-5109-46a4-a5af-1d17dc871f16",
            "2482f11f-ccf0-4589-8f3e-2bf08eab6148",
            "d68204af-51ea-4558-93f7-27479d1da277",
            "99ecb243-0ec7-4ce5-a91c-2030b2e61d74"
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

    def sce_1_7_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)

            if self.element(L.import_media.media_library.tti.title).text == "Text to Image":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Enter TTI fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti)

            return "FAIL"

    def sce_1_7_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.tti.close)

            if self.is_exist(L.import_media.media_library.media(0)):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Return media picker fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_7_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            input_box = self.element(L.import_media.media_library.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.import_media.media_library.tti.done)

            if self.element(L.import_media.media_library.tti.prompt).text == "x"*401:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Enter prompt fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            input_box = self.element(L.import_media.media_library.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            if self.is_exist(L.import_media.media_library.tti.exceed_hint):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] No found warning message')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            input_box = self.element(L.import_media.media_library.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            if self.element(L.import_media.media_library.tti.generate).get_attribute("enabled") == "false":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Generate button is not disabled')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            input_box = self.element(L.import_media.media_library.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.element(L.import_media.media_library.tti.prompt).click()
            input_box = self.element(L.import_media.media_library.tti.input_box)
            input_box.send_keys('sexy')
            self.click(L.import_media.media_library.tti.done)

            if not self.is_exist(L.import_media.media_library.tti.sensitive):
                self.click(L.import_media.media_library.tti.generate)
                time.sleep(1)

            if self.is_exist(L.import_media.media_library.tti.sensitive):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] No found warning message')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            input_box = self.element(L.import_media.media_library.tti.input_box)
            input_box.send_keys('sexy')
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            if self.element(L.import_media.media_library.tti.generate).get_attribute("enabled") == "false":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Generate button is not disabled')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            input_box = self.element(L.import_media.media_library.tti.input_box)
            input_box.send_keys('sexy')
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.tti.prompt)
            self.click(L.import_media.media_library.tti.clear)
            self.click(L.import_media.media_library.tti.done)

            if self.element(L.import_media.media_library.tti.prompt).text == "Type more than 10 words, describing the object, colors, composition, lighting, painting styles, etc.":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Prompt is not cleared')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()

            return "FAIL"

    def sce_1_7_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.input = self.element(L.import_media.media_library.tti.input_box).text
            self.click(L.import_media.media_library.tti.done)

            if self.element(L.import_media.media_library.tti.prompt).text == self.input:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Prompt is incorrect')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.input = self.element(L.import_media.media_library.tti.input_box).text
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            select = self.element(xpath('//*[contains(@resource-id,"view_is_selected")]/../*[contains(@resource-id,"tv_name")]')).text

            if select == "None":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Default incorrect: {select}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(xpath('//*[contains(@resource-id,"card_view")]//*[contains(@resource-id,"iv_premium")]'))

            if self.click(L.main.subscribe.back_btn):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP Back fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(xpath('(//*[contains(@resource-id,"card_view") and not(.//*[contains(@resource-id,"iv_premium")])])[2]'))
            time.sleep(0.5)
            select = self.element(xpath('//*[contains(@resource-id,"view_is_selected")]/../*[contains(@resource-id,"tv_name")]')).text

            if select != "None":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Select stlye fail: {select}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(xpath('//*[contains(@resource-id,"cv_sticker")]/*[contains(@resource-id,"iv_premium")]'))

            if self.click(L.main.subscribe.back_btn):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP Back fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.import_media.media_library.tti.overwrite_cancel)

            if self.element(L.import_media.media_library.tti.prompt).text == self.input:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Prompt is incorrect')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    def sce_1_7_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.import_media.media_library.tti.overwrite_ok)
            prompt = self.element(L.import_media.media_library.tti.prompt).text

            if prompt != self.input:
                report.new_result(uuid, True)

                self.input = prompt

                return "PASS"
            else:
                raise Exception('[Fail] Prompt is incorrect')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.import_media.media_library.tti.done)
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.import_media.media_library.tti.overwrite_ok)
            self.input = self.element(L.import_media.media_library.tti.prompt).text

            return "FAIL"

    def sce_1_7_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.tti.generate)

            if self.is_exist(L.import_media.media_library.tti.remove_watermark):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] No found remove watermark')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.tti.entry)
            self.element(L.import_media.media_library.tti.prompt).click()
            self.click(L.import_media.media_library.tti.prompt)
            tags = self.elements(L.import_media.media_library.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.import_media.media_library.tti.done)

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_1_7_1": self.sce_1_7_1(),
                  "sce_1_7_2": self.sce_1_7_2(),
                  "sce_1_7_3": self.sce_1_7_3(),
                  "sce_1_7_4": self.sce_1_7_4(),
                  "sce_1_7_5": self.sce_1_7_5(),
                  "sce_1_7_6": self.sce_1_7_6(),
                  "sce_1_7_7": self.sce_1_7_7(),
                  "sce_1_7_8": self.sce_1_7_8(),
                  "sce_1_7_9": self.sce_1_7_9(),
                  "sce_1_7_10": self.sce_1_7_10(),
                  "sce_1_7_11": self.sce_1_7_11(),
                  "sce_1_7_12": self.sce_1_7_12(),
                  "sce_1_7_13": self.sce_1_7_13(),
                  "sce_1_7_14": self.sce_1_7_14(),
                  "sce_1_7_15": self.sce_1_7_15(),
                  "sce_1_7_16": self.sce_1_7_16(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
