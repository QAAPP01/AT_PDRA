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
ori_preview = None
order = 3

@allure.epic('Timeline_PiP')
@allure.feature('Video')
@allure.story('Effect')
class Test_PiP_Video_Effect:

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

    @allure.title('Enter Effect')
    def test_effect_enter_effect(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            assert self.page_edit.effect.start_with_effect('pip video')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Favorite Empty')
    def test_effect_favorite_empty(self, driver):

        try:
            assert self.page_edit.effect.effect_favorite_empty()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Change Category')
    def test_effect_change_category(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            assert self.page_edit.effect.effect_switch_category('Retro')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    # select old movie
    @allure.title('Select Effect')
    def test_effect_select_effect(self, driver):

        try:
            assert self.page_edit.effect.effect_select_effect(order)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            self.page_edit.effect.effect_select_effect(2)
            raise Exception

    @allure.title('Old Movie_Parameter_Front Color')
    def test_effect_parameter_front_color(self, driver):

        try:
            assert self.page_edit.effect.effect_parameter_front_color(order)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Old Movie_Parameter_Background Color')
    def test_effect_parameter_background_color(self, driver):

        try:
            assert self.page_edit.effect.effect_parameter_background_color()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Old Movie_Parameter_Slider_Artifact Quantity')
    def test_effect_parameter_slider_artifact_quantity(self, driver):

        try:
            assert self.page_edit.effect.effect_parameter_slider(0)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Old Movie_Parameter_Slider_Degree')
    def test_effect_parameter_slider_degree(self, driver):

        try:
            assert self.page_edit.effect.effect_parameter_slider(1)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Old Movie_Parameter_Slider_Noise')
    def test_effect_parameter_slider_noise(self, driver):

        try:
            assert self.page_edit.effect.effect_parameter_slider(2)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Old Movie_Parameter_Slider_Jitter')
    def test_effect_parameter_slider_jitter(self, driver):

        try:
            assert self.page_edit.effect.effect_parameter_slider(3)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Old Movie_Parameter_Slider_Flicker')
    def test_effect_parameter_slider_flicker(self, driver):

        try:
            assert self.page_edit.effect.effect_parameter_slider(4)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Parameter_Reset')
    def test_effect_parameter_reset(self, driver):

        try:
            assert self.page_edit.effect.parameter_reset()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Add Favorite')
    def test_effect_add_favorite(self, driver):

        try:
            self.click(L.edit.sub_tool.effect.back)
            assert self.page_edit.effect.effect_favorite(order=order)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Remove Favorite')
    def test_effect_remove_favorite(self, driver):

        try:
            assert self.page_edit.effect.effect_favorite(order=order, action='remove')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Apply')
    def test_effect_apply(self, driver):

        try:
            assert self.page_edit.effect.effect_apply(order)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            raise Exception

    @allure.title('None')
    def test_effect_none(self, driver):

        try:
            assert self.page_edit.effect.effect_none(order)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception

    @allure.title('Cancel')
    def test_effect_cancel(self, driver):

        try:
            assert self.page_edit.effect.effect_cancel(order)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.effect.start_with_effect('pip video')
            raise Exception
