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


class Test_Import_Stock_Filter:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "cca45508-ad10-4586-99f7-127abe455d27",
            "1a815ebc-ce19-4846-9554-01ea6a0236fd",
            "000fd8ac-b6c7-4c71-ad78-ce1ce2f5ca23",
            "6c138c1e-f0f9-4fc5-aefb-6fdb431a9bf8",
            "6ac19553-691d-4609-8de6-9ac98038a151",
            "66a5b512-8d3f-4bcf-a6f5-1e7eabffb43b",
            "bd0b2364-d3e3-45c3-bb7a-7366e07b4350",
            "5597f3d9-1443-467d-a205-eee5e59e8dee",
            "e6ce5712-3727-461d-b755-90bc5ae93e97",
            "64ab5b20-5a8e-4189-80ec-83b6f5da2c19",
            "42e359c4-59ab-4233-8843-ae916d55ec13",
            "cdd2739c-a665-441d-829c-2e57f5c17a7b",
            "a723250f-6ec0-4842-8c3b-79b4f7efdba7",
            "cd24a995-253a-4e56-a2f1-d5068d422f6a",
            "46d3039e-9ae1-48aa-9322-da5abef5dc8e",
            "d43221de-ac7a-4a6f-820d-ed7b80213af5",
            "4014dadb-0ec9-47db-a6fe-832c75927363",
            "ffca230c-c7ea-46b3-b08b-74aa53a61cee",
            "ce6846df-b88f-4d1d-acfd-9cc9bcab4640",
            "148b306d-35af-4c56-a9c9-0139a5e1bcbc",
            "cccde99c-3c48-4bf1-be35-f57b0ea13b3f",
            "3638dbd9-04ec-45eb-8079-496e76f5053c",
            "dc30b4ef-2731-48e3-87a2-732693f27a7b",
            "503c3238-79e8-4186-b817-d8812850fd42",
            "6eaac833-4e82-477b-acd5-e8d1b3685e5b",
            "39c0da3c-7d35-4031-b501-de998f56fa47",
            "ec9a9973-0c65-4705-8e04-4da068385302",
            "06cc1673-aad7-48a3-8946-1061cb0b0609",
            "7aefd9a0-bd00-4157-96a8-8891d8a7eb15",
            "ece0b838-cd8b-4752-8eb0-b26e7119b288",
            "1dbcb1a2-2e69-4b51-8437-076d5ca08991",
            "ffd5e30a-a2d6-40d9-9290-f9c0ff53325d",
            "a9dbff53-2ed4-44a2-b3d1-8549eba7b30c",
            "8e427bc2-fbed-44b6-9380-96fdb0b212b4",
            "595fd533-ee0d-4ee2-906d-37e45775244c",
            "10a44651-ef3e-47eb-85bb-56704e275fc9"
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
        self.is_not_exist = self.page_main.h_is_not_exist

        report.set_driver(driver)
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def sce_1_8_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            return "FAIL"

    def sce_1_8_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.newest)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.random)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.most_popular)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.best_match)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_8_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_video_library("giphy")
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            pic_search = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            return "FAIL"

    def sce_1_8_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.search_clear)

            if self.element(L.import_media.sort_menu.sort_button).get_attribute("enabled") == "false":
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Sort button not disabled')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_8_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_video_library("pexels")
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            return "FAIL"

    def sce_1_8_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_square)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            self.page_media.scroll_to_top()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_8_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_video_library("pixabay")
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pixabay")
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            return "FAIL"

    def sce_1_8_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.newest)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pixabay")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.best_match)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_8_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_photo_library("getty")
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            return "FAIL"

    def sce_1_8_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.newest)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.random)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.most_popular)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.best_match)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_square)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_panoramic)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            self.page_media.scroll_to_top()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_8_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_photo_library("pexels")
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            return "FAIL"

    def sce_1_8_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_28(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_29(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_square)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_30(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            self.page_media.scroll_to_top()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_8_31(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_photo_library("pixabay")
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()

            return "FAIL"

    def sce_1_8_32(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.newest)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_33(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.best_match)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_34(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_35(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if not HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")
            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")

            return "FAIL"

    def sce_1_8_36(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            self.page_media.scroll_to_top()
            self.page_media.wait_media_change(media)
            pic_after = self.page_main.h_full_screenshot()

            if HCompareImg(self.pic_search, pic_after).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Result not resumed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {
            "sce_1_8_1": self.sce_1_8_1(),
            "sce_1_8_2": self.sce_1_8_2(),
            "sce_1_8_3": self.sce_1_8_3(),
            "sce_1_8_4": self.sce_1_8_4(),
            "sce_1_8_5": self.sce_1_8_5(),
            "sce_1_8_6": self.sce_1_8_6(),
            "sce_1_8_7": self.sce_1_8_7(),
            "sce_1_8_8": self.sce_1_8_8(),
            "sce_1_8_9": self.sce_1_8_9(),
            "sce_1_8_10": self.sce_1_8_10(),
            "sce_1_8_11": self.sce_1_8_11(),
            "sce_1_8_12": self.sce_1_8_12(),
            "sce_1_8_13": self.sce_1_8_13(),
            "sce_1_8_14": self.sce_1_8_14(),
            "sce_1_8_15": self.sce_1_8_15(),
            "sce_1_8_16": self.sce_1_8_16(),
            "sce_1_8_17": self.sce_1_8_17(),
            "sce_1_8_18": self.sce_1_8_18(),
            "sce_1_8_19": self.sce_1_8_19(),
            "sce_1_8_20": self.sce_1_8_20(),
            "sce_1_8_21": self.sce_1_8_21(),
            "sce_1_8_22": self.sce_1_8_22(),
            "sce_1_8_23": self.sce_1_8_23(),
            "sce_1_8_24": self.sce_1_8_24(),
            "sce_1_8_25": self.sce_1_8_25(),
            "sce_1_8_26": self.sce_1_8_26(),
            "sce_1_8_27": self.sce_1_8_27(),
            "sce_1_8_28": self.sce_1_8_28(),
            "sce_1_8_29": self.sce_1_8_29(),
            "sce_1_8_30": self.sce_1_8_30(),
            "sce_1_8_31": self.sce_1_8_31(),
            "sce_1_8_32": self.sce_1_8_32(),
            "sce_1_8_33": self.sce_1_8_33(),
            "sce_1_8_34": self.sce_1_8_34(),
            "sce_1_8_35": self.sce_1_8_35(),
            "sce_1_8_36": self.sce_1_8_36()
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
