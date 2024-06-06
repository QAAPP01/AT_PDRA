import traceback
import inspect
import time

import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


@allure.epic("Timeline_PiP")
@allure.feature("Sticker")
@allure.story("Opacity")
class Test_PiP_Sticker_Opacity:
    @pytest.fixture(scope='session', autouse=True)
    def driver_init(self, driver):
        logger("[Start] Init driver session")
        driver.driver.launch_app()
        yield
        # driver.driver.close_app()

    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist
        self.set_slider = self.page_edit.h_set_slider

    @allure.story("Sticker")
    @allure.title("Add to PiP track")
    def test_add_sticker(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.click(L.import_media.media_library.color_board)
            self.click(L.import_media.media_library.media(5))
            self.click(L.import_media.media_library.next)
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)

            assert self.is_exist(L.edit.timeline.item_view_thumbnail_view)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Default Value")
    def test_sticker_opacity_default_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.click_sub_tool('Opacity')
            value = self.element(L.edit.adjust_sub.number).text

            assert value == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Adjust opacity")
    def test_adjust_sticker_opacity(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            pic_base = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)
            self.element(L.edit.adjust_sub.progress).send_keys('50.0')
            pic_after = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)

            assert HCompareImg(pic_base, pic_after).full_compare() < 1

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Minimum")
    def test_sticker_opacity_minimum(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.adjust_sub.progress).send_keys('1.0')
            self.element(L.edit.adjust_sub.progress).send_keys('0')
            value = self.element(L.edit.adjust_sub.number).text

            assert value == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Opacity')
            raise Exception

    @allure.title("Maximum")
    def test_sticker_opacity_maximum(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.adjust_sub.progress).send_keys('100.0')
            value = self.element(L.edit.adjust_sub.number).text
            self.click(L.edit.sub_tool.back)
            assert value == '100'

        except Exception:
            traceback.print_exc()

            raise Exception


@pytest.mark.PiP
@allure.epic("Timeline_PiP")
@allure.feature("Sticker")
@allure.story("Fade")
class Test_PiP_Sticker_Fade:
    # @pytest.fixture(scope='class', autouse=True)
    # def driver_init(self, driver):
    #     logger("[Start] Init driver session")
    #     driver.driver.launch_app()
    #     yield
    #     driver.driver.close_app()

    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist
        self.set_slider = self.page_edit.h_set_slider

    @allure.title("Enter fade panel")
    def test_sticker_show_fade_in_out(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            # self.page_main.enter_launcher()
            # self.page_main.enter_timeline()
            # self.page_edit.enter_sticker_library("Sticker")
            # self.page_media.select_sticker_by_order(order=3)
            # self.page_media.waiting_download()
            # self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Fade')

            assert self.is_exist(L.edit.fade.fade_in) and self.is_exist(L.edit.fade.fade_out)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Fade')
            raise Exception

    @allure.title("Fade in")
    def test_sticker_fade_in(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.fade.fade_in)
            pic_base = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)
            self.click(L.edit.menu.play)
            time.sleep(2)
            self.click(L.edit.menu.play)
            pic_after = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)

            assert HCompareImg(pic_base, pic_after).full_compare() < 1

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Fade')
            raise Exception

    @allure.title("Fade out")
    def test_sticker_fade_out(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.fade.fade_out)
            pic_base = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)
            self.click(L.edit.menu.play)
            time.sleep(2.3)
            self.click(L.edit.menu.play)
            pic_after = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)
            self.click(L.edit.fade.fade_in)
            self.click(L.edit.fade.fade_out)
            self.click(L.edit.sub_tool.back)

            assert HCompareImg(pic_base, pic_after).full_compare() < 1

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Fade')
            raise Exception


@allure.epic("Timeline_PiP")
@allure.feature("Sticker")
@allure.story("Blending")
class Test_PiP_Sticker_Blending:
    # @pytest.fixture(scope='class', autouse=True)
    # def driver_init(self, driver):
    #     logger("[Start] Init driver session")
    #     driver.driver.launch_app()
    #     yield
    #     driver.driver.close_app()

    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist
        self.set_slider = self.page_edit.h_set_slider

    @allure.title("Enter blending panel")
    def test_sticker_enter_blending_panel(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            # self.page_main.enter_launcher()
            # self.page_main.enter_timeline()
            # self.page_edit.enter_sticker_library("Sticker")
            # self.page_media.select_sticker_by_order(order=3)
            # self.page_media.waiting_download()
            # self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Blending')

            assert self.is_exist(L.edit.fx_layer.filter.item(1))

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Blending')
            raise Exception

    @allure.title("Apply blending")
    def test_sticker_apply_blending(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            pic_base = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)
            self.click(L.edit.fx_layer.filter.item(3))
            pic_after = self.page_edit.get_preview_pic(L.edit.preview.pip_preview)

            assert HCompareImg(pic_base, pic_after).full_compare() < 1

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library("Sticker")
            self.page_media.select_sticker_by_order(order=3)
            self.page_media.waiting_download()
            self.click(L.edit.sticker.close)
            self.page_edit.click_sub_tool('Blending')
            raise Exception
