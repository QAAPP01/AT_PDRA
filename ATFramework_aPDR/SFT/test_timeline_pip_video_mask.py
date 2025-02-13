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
@allure.feature('Video')
@allure.story('Mask')
class Test_PiP_Video_Mask:

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

    @allure.title('Enter Mask')
    def test_mask_enter_mask(self, driver):

        try:
            assert self.page_edit.mask.start_with_mask('pip video')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Default is None')
    def test_mask_default(self, driver):

        try:
            assert self.element(L.edit.mask_sub.mask_none).get_attribute('selected') == 'true'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.mask.start_with_mask('pip video')
            raise Exception

    @allure.title('Linear')
    def test_mask_linear(self, driver):

        try:
            assert self.page_edit.mask.click_mask_type("Linear")
            assert self.element(L.edit.mask_sub.mask_linear).get_attribute('selected') == 'true'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.mask.start_with_mask('pip video')
            raise Exception

    @allure.title('Linear_Slider')
    def test_mask_linear_slider(self, driver):

        try:
            assert self.page_edit.mask.set_slider()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.mask.start_with_mask('pip video')
            raise Exception

    @allure.title('Parallel')
    def test_mask_parallel(self, driver):

        try:
            assert self.page_edit.mask.click_mask_type("Parallel")
            assert self.element(L.edit.mask_sub.mask_parallel).get_attribute('selected') == 'true'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.mask.start_with_mask('pip video')
            raise Exception

    @allure.title('Parallel_Slider')
    def test_mask_parallel_slider(self, driver):

        try:
            assert self.page_edit.mask.set_slider()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.mask.start_with_mask('pip video')
            raise Exception

    # @allure.title('Eclipse')
    # def test_mask_eclipse(self, driver):
    #
    #     try:
    #         assert self.page_edit.mask.click_mask_type("Eclipse")
    #         assert self.element(L.edit.mask_sub.mask_eclipse).get_attribute('selected') == 'true'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_edit.mask.start_with_mask('pip video')
    #         raise Exception
    #
    # @allure.title('Eclipse_Slider')
    # def test_mask_eclipse_slider(self, driver):
    #
    #     try:
    #         assert self.page_edit.mask.set_slider()
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_edit.mask.start_with_mask('pip video')
    #         raise Exception
    #
    # @allure.title('Rectangle')
    # def test_mask_rectangle(self, driver):
    #
    #     try:
    #         assert self.page_edit.mask.click_mask_type("Rectangle")
    #         assert self.element(L.edit.mask_sub.mask_rectangle).get_attribute('selected') == 'true'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_edit.mask.start_with_mask('pip video')
    #         raise Exception
    #
    # @allure.title('Rectangle_Slider')
    # def test_mask_rectangle_slider(self, driver):
    #
    #     try:
    #         assert self.page_edit.mask.set_slider()
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_edit.mask.start_with_mask('pip video')
    #         raise Exception
    #
    # @allure.title('Invert')
    # def test_mask_invert(self, driver):
    #
    #     try:
    #         assert self.page_edit.mask.click_mask_type("Invert")
    #         assert self.element(L.edit.mask_sub.switch_invert).get_attribute('selected') == 'true'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_edit.mask.start_with_mask('pip video')
    #         raise Exception
    #
    # @allure.title('Invert_Slider')
    # def test_mask_invert_slider(self, driver):
    #
    #     try:
    #         assert self.page_edit.mask.set_slider()
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_edit.mask.start_with_mask('pip video')
    #         raise Exception
    #
    # @allure.title('Slider Reset')
    # def test_mask_slider_reset(self, driver):
    #
    #     try:
    #         assert self.page_edit.mask.slider_reset()
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_edit.mask.start_with_mask('pip video')
    #         raise Exception
