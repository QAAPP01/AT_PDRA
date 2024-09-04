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




@allure.epic('Timeline_PiP')
@allure.feature('Video')
@allure.story('Filter')
class Test_PiP_Video_Filter:
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

    @allure.title('Enter Filter')
    def test_filter_enter_filter(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            assert self.page_edit.filter.start_with_filter('master photo')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception

    @allure.title('Favorite Empty')
    def test_filter_favorite_empty(self, driver):

        try:
            assert self.page_edit.filter.filter_favorite_empty()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception

    @allure.title('Change Category')
    def test_filter_change_category(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            assert self.page_edit.filter.filter_switch_category(3)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception

    @allure.title('Select Filter')
    def test_filter_select_filter(self, driver):

        try:
            assert self.page_edit.filter.filter_select_filter(2)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            self.page_edit.filter.filter_select_filter(2)
            raise Exception

    @allure.title('Slider')
    def test_filter_slider(self, driver):

        try:
            assert self.page_edit.filter.filter_slider(2)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception

    @allure.title('Add Favorite')
    def test_filter_add_favorite(self, driver):

        try:
            assert self.page_edit.filter.filter_favorite(order=4)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception

    @allure.title('Remove Favorite')
    def test_filter_remove_favorite(self, driver):

        try:
            assert self.page_edit.filter.filter_favorite(order=4, action='remove')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception

    @allure.title('Apply')
    def test_filter_apply(self, driver):

        try:
            assert self.page_edit.filter.filter_apply()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            raise Exception

    @allure.title('None')
    def test_filter_none(self, driver):

        try:
            assert self.page_edit.filter.filter_none()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception

    @allure.title('Cancel')
    def test_filter_cancel(self, driver):

        try:
            assert self.page_edit.filter.filter_cancel()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.filter.start_with_filter('pip video')
            raise Exception