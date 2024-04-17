import traceback
import inspect
import pytest
import sys

from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import REPORT_INSTANCE as report

sys.path.insert(0, (path.dirname(path.dirname(__file__))))


class Test_Media:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "02f3c058-7e69-4c30-ba59-f32dc4eb697b",
            "dadd062f-e543-493f-ab1b-7ee25c1c8d5b",
            "7e17cd4b-e253-4762-8ca8-83bae712949a",
            "7866965e-6799-4574-afdd-457b8d6c93ef",
            "68f8343c-e43c-4947-af97-db42d0142b2c",
            "f55936a7-2566-46a1-8a07-a8a234fd2d19",
            "b4f3507f-0df6-4a37-aa27-8268b84ea0fd",
            "ad8bfbd2-2b76-4b05-b464-23c6cc65c16b",
            "763e09d0-364b-4aa9-b02b-087cd932ab9c",
            "56c47079-147c-4994-a27d-dfafd586e969",
            "1b27f382-aea1-4ac7-a361-4330ad8e1e60",
            "2e8ed499-6d4e-4ec0-a883-3cd85cadf19d",
            "041e27f1-4e7d-46e5-b467-6d4a6f29a33e",
            "cb46cbb6-a497-4e66-8608-be92fd94bdfb",
            "aa09c4ca-2bfb-4fd0-b3d1-65a608b278ef",
            "0e11dd3f-9111-49fe-83b5-52970c4e9136",
            "927b60a8-e4a4-4ae0-b631-6cf7dd9819be",
            "4b800851-2915-473d-a51b-d8b0c7811d38",
            "276c90ae-e627-4052-b2db-2a529a8a7c00",
            "4879f997-715f-4496-9bf3-e34bad05800c",
            "4f798ef8-c6bd-4041-841e-efcc189a4a4e",
            "969e8b70-19b9-4e7b-8074-3570393007b1",
            "ae4f2f3d-9d1b-48eb-ae5b-39ee0ce106e9",
            "1de8d937-6ba0-4969-981d-77140d1ab477",
            "c397401b-228e-4c2d-a3d8-f6e3af15e291",
            "a90d6f6a-380a-4b0e-89b0-80be9c5fe28b"
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

    def sce_1_1_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.subscribe()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.display_preview)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            return "FAIL"

    def sce_1_1_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            return "FAIL"

    def sce_1_1_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_video_library("getty_pro")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.display_preview)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty_pro")

            return "FAIL"

    def sce_1_1_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            if self.page_media.subscribe_getty_pro():
                self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty_pro")

            return "FAIL"

    def sce_1_1_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_video_library("giphy")
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("giphy")

            return "FAIL"

    def sce_1_1_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_video_library("pexels")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.videoDisplay)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")

            return "FAIL"

    def sce_1_1_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")

            return "FAIL"

    def sce_1_1_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_video_library("pixabay")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.display_preview)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pixabay")

            return "FAIL"

    def sce_1_1_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pixabay")

            return "FAIL"

    def sce_1_1_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_photo_library("getty")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")

            return "FAIL"

    def sce_1_1_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")

            return "FAIL"

    def sce_1_1_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_photo_library("getty_pro")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty_pro")

            return "FAIL"

    def sce_1_1_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            if self.page_media.subscribe_getty_pro():
                self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty_pro")

            return "FAIL"

    def sce_1_1_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_photo_library("pexels")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")

            return "FAIL"

    def sce_1_1_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")

            return "FAIL"

    def sce_1_1_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    def sce_1_1_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_media.select_photo_library("pixabay")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            if HCompareImg(img).is_not_black():
                report.new_result(uuid, True)

                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Preview is black')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_1_1_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            if self.click(L.import_media.media_library.delete_selected):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Download failed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_1_1_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            if not HCompareImg(self.pic_search, pic_default).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Thumbnails not changed')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {
            "sec_1_1_1": self.sce_1_1_1(),
            "sec_1_1_2": self.sce_1_1_2(),
            "sec_1_1_3": self.sce_1_1_3(),
            "sec_1_1_4": self.sce_1_1_4(),
            "sec_1_1_5": self.sce_1_1_5(),
            "sec_1_1_6": self.sce_1_1_6(),
            "sec_1_1_7": self.sce_1_1_7(),
            "sec_1_1_8": self.sce_1_1_8(),
            "sec_1_1_9": self.sce_1_1_9(),
            "sec_1_1_10": self.sce_1_1_10(),
            "sec_1_1_11": self.sce_1_1_11(),
            "sec_1_1_12": self.sce_1_1_12(),
            "sec_1_1_13": self.sce_1_1_13(),
            "sec_1_1_14": self.sce_1_1_14(),
            "sec_1_1_15": self.sce_1_1_15(),
            "sec_1_1_16": self.sce_1_1_16(),
            "sec_1_1_17": self.sce_1_1_17(),
            "sec_1_1_18": self.sce_1_1_18(),
            "sec_1_1_19": self.sce_1_1_19(),
            "sec_1_1_20": self.sce_1_1_20(),
            "sec_1_1_21": self.sce_1_1_21(),
            "sec_1_1_22": self.sce_1_1_22(),
            "sec_1_1_23": self.sce_1_1_23(),
            "sec_1_1_24": self.sce_1_1_24(),
            "sec_1_1_25": self.sce_1_1_25(),
            "sec_1_1_26": self.sce_1_1_26()
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
