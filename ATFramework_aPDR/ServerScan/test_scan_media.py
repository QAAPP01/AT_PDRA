import time
import traceback
import inspect
import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


@allure.epic("Server Scan")
@allure.feature("Media")
class Test_Scan_Media:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.story("Video")
    @allure.title("Getty Video Preview")
    def test_getty_video_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            raise Exception

    @allure.story("Video")
    @allure.title("Getty Video Download")
    def test_getty_video_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected, 60)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty")

            raise Exception

    @allure.story("Video")
    @allure.title("Getty Video Search/Thumbnail")
    def test_getty_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Video")
    @allure.title("Getty Pro Video Preview")
    def test_getty_pro_video_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_video_library("getty_pro")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty_pro")

            raise Exception

    @allure.story("Video")
    @allure.title("Getty Pro Video Download")
    def test_getty_pro_video_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            if self.page_media.subscribe_getty_pro():
                self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("getty_pro")

            raise Exception

    @allure.story("Video")
    @allure.title("Getty Pro Video Search/Thumbnail")
    def test_getty_pro_video_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Video")
    @allure.title("Giphy Video Download")
    def test_giphy_video_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_video_library("giphy")
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("giphy")

            raise Exception

    @allure.story("Video")
    @allure.title("Giphy Video Search/Thumbnail")
    def test_giphy_video_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception as err:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Video")
    @allure.title("Pexels Video Preview")
    def test_pexels_video_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_video_library("pexels")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.videoDisplay)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")

            raise Exception

    @allure.story("Video")
    @allure.title("Pexels Video Download")
    def test_pexels_video_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pexels")

            raise Exception

    @allure.story("Video")
    @allure.title("Pexels Video Search/Thumbnail")
    def test_pexels_video_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Video")
    @allure.title("Pixabay Video Preview")
    def test_pixabay_video_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_video_library("pixabay")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.video.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pixabay")

            raise Exception

    def check_download_media(self):
        for retry in range(9):
            self.click(L.import_media.media_library.media(retry+1))
            self.page_media.waiting_download()
            if self.is_exist(L.import_media.media_library.delete_selected):
                return True
        else:
            return False

    @allure.story("Video")
    @allure.title("Pixabay Video Download")
    def test_pixabay_video_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.check_download_media()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_video_library("pixabay")

            raise Exception

    @allure.story("Video")
    @allure.title("Pixabay Video Search/Thumbnail")
    def test_pixabay_video_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Photo")
    @allure.title("Getty Photo Preview")
    def test_getty_photo_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_photo_library("getty")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")

            raise Exception

    @allure.story("Photo")
    @allure.title("Getty Photo Download")
    def test_getty_photo_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty")

            raise Exception

    @allure.story("Photo")
    @allure.title("Getty Photo Search/Thumbnail")
    def test_getty_photo_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Photo")
    @allure.title("Getty Pro Photo Preview")
    def test_getty_pro_photo_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_photo_library("getty_pro")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty_pro")

            raise Exception

    @allure.story("Photo")
    @allure.title("Getty Pro Photo Download")
    def test_getty_pro_photo_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            if self.page_media.subscribe_getty_pro():
                self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("getty_pro")

            raise Exception

    @allure.story("Photo")
    @allure.title("Getty Pro Photo Search/Thumbnail")
    def test_getty_pro_photo_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Photo")
    @allure.title("Pexels Photo Preview")
    def test_pexels_photo_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_photo_library("pexels")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")

            raise Exception

    @allure.story("Photo")
    @allure.title("Pexels Photo Download")
    def test_pexels_photo_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pexels")

            raise Exception

    @allure.story("Photo")
    @allure.title("Pexels Photo Search/Thumbnail")
    def test_pexels_photo_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)

            raise Exception

    @allure.story("Photo")
    @allure.title("Pixabay Photo Preview")
    def test_pixabay_photo_preview(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.select_photo_library("pixabay")

            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_download()
            img = self.page_main.get_picture(L.import_media.media_library.photo.display_preview)

            assert HCompareImg(img).is_not_black()
            driver.driver.back()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")

            raise Exception

    @allure.story("Photo")
    @allure.title("Pixabay Photo Download")
    def test_pixabay_photo_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()

            assert self.click(L.import_media.media_library.delete_selected)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_photo_library("pixabay")

            raise Exception

    @allure.story("Photo")
    @allure.title("Pixabay Photo Search/Thumbnail")
    def test_pixabay_photo_thumbnail(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            media = self.element(L.import_media.media_library.media())
            pic_default = self.page_main.h_full_screenshot()

            self.click(L.import_media.media_library.search)
            self.page_media.text_search("cat")
            self.page_media.wait_media_change(media)
            self.pic_search = self.page_main.h_full_screenshot()
            self.click(L.import_media.media_library.search_clear)

            assert not HCompareImg(self.pic_search, pic_default).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()

            raise Exception