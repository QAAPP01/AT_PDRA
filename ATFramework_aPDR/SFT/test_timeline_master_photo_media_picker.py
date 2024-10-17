import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.SFT.test_file import *


@allure.epic('Timeline Master Photo')
@allure.feature('Media Picker')
class Test_Master_Photo_Media_Picker:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @pytest.fixture(scope="module")
    def data(self):
        data = {'last_result': True}
        yield data

    def last_is_fail(self, data):
        if not data['last_result']:
            data['last_result'] = True
            self.page_main.relaunch()
            return True
        return False

    @allure.story('Local')
    @allure.title('Add mp4')
    def test_add_mp4(self, data):
        try:
            self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_local_video(video_mp4)
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Local')
    @allure.title('Add 3gp')
    def test_add_3gp(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_local_video(video_3gp)
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Local')
    @allure.title('Add mkv')
    def test_add_mkv(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_local_video(video_mkv)
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Getty Images')
    @allure.title('Add Getty Images video')
    def test_add_getty_images_video(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_getty_images_video()
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Getty Images Pro')
    @allure.title('Add Getty Images Pro video')
    def test_add_getty_images_pro_video(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_getty_images_pro_video()
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Giphy')
    @allure.title('Add Giphy')
    def test_add_giphy(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_giphy()
            self.page_media.delete_master_photo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Pexels')
    @allure.title('Add Pexels Video')
    def test_add_pexels_video(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_pexels_video()
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Pixabay')
    @allure.title('Add Pixabay Video')
    def test_add_pixabay_video(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_pixabay_video()
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Google Drive')
    @allure.title('Add Google Drive Video')
    def test_add_google_drive_video(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_google_drive_video()
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Google Photos')
    @allure.title('Add Google Photos Video')
    def test_add_google_photos_video(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_google_photos_video()
            self.page_media.delete_master_video()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise
