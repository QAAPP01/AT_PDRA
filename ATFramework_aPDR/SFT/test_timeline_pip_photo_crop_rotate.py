import traceback
import inspect

import pytest
import allure
from random import randint

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg, CompareImage
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


from .conftest import TEST_MATERIAL_FOLDER, driver

test_material_folder = TEST_MATERIAL_FOLDER

@allure.epic('Timeline_PiP')
@allure.feature('Photo')
@allure.story('Crop & Rotate')
class Test_PiP_Photo_Crop_Rotate:

    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist
        self.set_slider = self.page_edit.h_set_slider

    @allure.title('Enter Crop & Rotate')
    def test_enter_crop_rotate(self, driver):

        try:
            assert self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip photo')
            raise Exception

    @allure.title('Crop_9:16')
    def test_crop_9_16(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('9:16')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_1:1')
    def test_crop_1_1(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('1:1')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_4:5')
    def test_crop_4_5(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('4:5')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_16:9')
    def test_crop_16_9(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('16:9')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_4:3')
    def test_crop_4_3(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('4:3')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_3:4')
    def test_crop_3_4(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('3:4')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_21:9')
    def test_crop_21_9(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('21:9')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_Original')
    def test_crop_original(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('Original')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Crop_Freeform')
    def test_crop_freeform(self, driver):

        try:
            assert self.page_edit.crop_rotate.crop('Freeform')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Rotate Ruler')
    def test_crop_rotate_ruler(self, driver):

        try:
            assert self.page_edit.crop_rotate.rotate_ruler()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Switch to Rotate')
    def test_crop__rotate_switch_to_rotate(self, driver):

        try:
            assert self.page_edit.crop_rotate.switch_to_rotate()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Rotate')
    def test_crop_rotate_rotate(self, driver):

        try:
            assert self.page_edit.crop_rotate.rotate()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Flip')
    def test_crop_rotate_flip(self, driver):

        try:
            assert self.page_edit.crop_rotate.flip()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Apply')
    def test_crop_rotate_apply(self, driver):

        try:
            assert self.page_edit.crop_rotate.apply()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Reset')
    def test_crop_rotate_reset(self, driver):

        try:
            assert self.page_edit.crop_rotate.reset()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception

    @allure.title('Cancel')
    def test_crop_rotate_cancel(self, driver):

        try:
            assert self.page_edit.crop_rotate.cancel()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.crop_rotate.start_with_crop_rotate('pip photo')
            raise Exception
