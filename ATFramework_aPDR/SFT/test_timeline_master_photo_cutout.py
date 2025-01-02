import inspect
import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.SFT.test_file import *

@allure.epic('Timeline Master Photo')
@allure.feature('Cutout')
class Test_Master_Photo_Cutout:
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

    @allure.story('Back')
    @allure.title('Toolbar back')
    def test_toolbar_back(self, data):
        try:
            self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)
            self.click(L.edit.toolbar.sub_tool_back)

            assert self.is_exist(L.edit.master.sub_tool('Cutout'))
            self.page_edit.click_sub_tool('Cutout')


        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Remove Background')
    @allure.title('Apply')
    def test_cutout_remove_background(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.remove_background()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('No Effect')
    @allure.title('Apply')
    def test_cutout_no_effect(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)
                self.page_edit.cutout.remove_background()

            assert self.page_edit.cutout.no_effect()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Default Image')
    def test_cutout_image_default_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.image_default_image()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('CL Image')
    def test_cutout_image_change_cl_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.image_change_cl_image(7)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('None')
    def test_cutout_image_none(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.image_none()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Custom Image')
    def test_cutout_custom_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.custom_image()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Enter Text to Image')
    def test_cutout_text_to_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.enter_TTI()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Animated Background')
    def test_text_to_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.animated_background()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Animated None')
    def test_animated_none(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.animated_none()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Color Background')
    def test_color_background(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.color_background()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Color None')
    def test_color_none(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)
                self.page_edit.cutout.color_background()

            assert self.page_edit.cutout.color_none()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Apply')
    def test_change_background_apply(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)
                self.page_edit.cutout.image_default_image()

            assert self.page_edit.cutout.change_background_apply()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Cancel')
    def test_change_background_cancel(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout", media_type="photo", file_name=photo_9_16)

            assert self.page_edit.cutout.change_background_cancel()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise