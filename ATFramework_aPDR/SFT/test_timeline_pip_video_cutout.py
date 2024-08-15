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

@pytest.fixture(scope='module', autouse=True)
def driver_init(driver):
    logger("==== Start driver session ====")
    driver.driver.launch_app()
    yield
    driver.driver.close_app()

@allure.epic('Timeline_PiP')
@allure.feature('Video')
@allure.story('Cutout_Remove_Background')
class Test_PiP_Video_Cutout_Change_Background:
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

    @allure.title('Cutout Default Selection')
    def test_cutout_default_selection(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            assert self.page_edit.cutout.start_with_cutout('pip video')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            raise Exception

    @allure.title('Remove Background')
    def test_cutout_remove_background(self, driver):

        try:
            assert self.page_edit.cutout.cutout_remove_background()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            raise Exception

    @allure.title('No Effect')
    def test_cutout_no_effect(self, driver):
        try:
            assert self.page_edit.cutout.cutout_no_effect()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            raise Exception

@allure.epic('Timeline_PiP')
@allure.feature('Video')
@allure.story('Cutout_Chroma_Key')
class Test_PiP_Video_Cutout_chroma_key:
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

    @allure.title('Enter Chroma Key')
    def test_enter_chroma_kay(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            assert self.page_edit.a_chroma_key.enter_chroma_key()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Click Preview')
    def test_chroma_key_click_preview(self, driver):
        try:
            assert self.page_edit.a_chroma_key.chroma_key_click_preview()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Picker Slider')
    def test_chroma_key_picker_slider(self, driver):
        try:
            assert self.page_edit.a_chroma_key.chroma_key_picker_slider()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Range Slider')
    def test_chroma_key_range_slider(self, driver):
        try:
            assert self.page_edit.a_chroma_key.chroma_key_range_slider()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Denoise Slider')
    def test_chroma_key_denoise_slider(self, driver):
        try:
            assert self.page_edit.a_chroma_key.chroma_key_denoise_slider()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Reset')
    def test_chroma_key_reset(self, driver):
        try:
            assert self.page_edit.a_chroma_key.chroma_key_reset()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Cancel')
    def test_chroma_key_cancel(self, driver):
        try:
            assert self.page_edit.a_chroma_key.chroma_key_cancel()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Apply')
    def test_chroma_key_apply(self, driver):
        try:
            assert self.page_edit.a_chroma_key.chroma_key_apply()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(TEST_MATERIAL_FOLDER, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception
