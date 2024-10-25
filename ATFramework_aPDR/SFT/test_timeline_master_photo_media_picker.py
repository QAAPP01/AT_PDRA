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
    @allure.title('Add png')
    def test_add_png(self, data):
        try:
            self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_local_photo(photo_png)
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Local')
    @allure.title('Add jpg')
    def test_add_jpg(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_local_photo(photo_jpg)
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Local')
    @allure.title('Add gif')
    def test_add_gif(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_local_photo(photo_gif)
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Local')
    @allure.title('Add bmp')
    def test_add_bmp(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_local_photo(photo_bmp)
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Getty Images')
    @allure.title('Add Getty Images photo')
    def test_add_getty_images_photo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_getty_images_photo()
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Getty Images Pro')
    @allure.title('Add Getty Images Pro photo')
    def test_add_getty_images_pro_photo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_getty_images_pro_photo()
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Pexels')
    @allure.title('Add Pexels photo')
    def test_add_pexels_photo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_pexels_photo()
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Pixabay')
    @allure.title('Add Pixabay photo')
    def test_add_pixabay_photo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_pixabay_photo()
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Google Drive')
    @allure.title('Add Google Drive photo')
    def test_add_google_drive_video(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_google_drive_photo()
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise

    @allure.story('Google Photos')
    @allure.title('Add Google Photos photo')
    def test_add_google_photos_photo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_main.enter_timeline(skip_media=False)

            assert self.page_media.add_google_photos_photo()
            self.page_media.delete_master_photo()

        except Exception as e:
            logger(f'\n[Error] {e}\n{traceback.format_exc()}')
            data['last_result'] = False
            raise
