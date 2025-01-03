import traceback
import inspect

import pytest
import allure
from random import randint

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg, CompareImage
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
# from test_file import *


from .conftest import TEST_MATERIAL_FOLDER, driver

test_material_folder = TEST_MATERIAL_FOLDER

@allure.epic('Timeline_PiP')
@allure.feature('Video')
@allure.story('Auto Caption')
class Test_PiP_Video_Auto_Caption:

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

    @allure.title('Enter Auto Caption')
    def test_auto_caption_enter_auto_caption(self, driver):

        try:
            assert self.page_edit.auto_caption.start_with_auto_caption('pip video')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    # Default language is device language
    @allure.title('Default language')
    def test_auto_caption_default_language(self, driver):

        try:
            assert self.element(L.edit.auto_caption.selected_language).get_attribute('text') == 'English'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Change language')
    def test_auto_caption_change_language(self, driver):

        try:
            assert self.page_edit.auto_caption.change_language('Chinese')

        except Exception:

            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Sound source from selected video')
    def default_sound_source(self, driver):
        try:
            assert self.element(L.edit.auto_caption.sound_source).get_attribute('text') == 'Clip Selected'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Select style template')
    def test_auto_caption_select_style_template(self, driver):
        try:
            assert self.page_edit.auto_caption.select_template()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Generate captions')
    def test_auto_caption_generate_caption(self, driver):
        try:
            assert self.page_edit.auto_caption.generate_caption()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Replace and regenerate caption')
    def test_auto_caption_replace_caption(self, driver):
        try:
            self.page_edit.click_sub_tool('Auto\n Captions')
            assert self.page_edit.auto_caption.generate_caption(replace='on')

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Close button')
    def test_auto_caption_setting_close(self, driver):
        try:
            self.page_edit.click_sub_tool('Auto\n Captions')
            self.page_edit.click(L.edit.auto_caption.back)
            assert not self.page_edit.is_exist(L.edit.auto_caption.title)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Caption list - Enter caption list')
    def test_auto_caption_enter_caption_list(self, driver):
        try:
            self.elements(L.edit.timeline.item_view_bg)[1].click()
            assert self.page_edit.auto_caption.enter_caption_list()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Caption List_Edit Caption')
    def test_auto_caption_caption_list_edit_caption(self, driver):
        try:
            assert self.page_edit.auto_caption.caption_list_edit_caption()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Caption List_Add Caption')
    def test_auto_caption_caption_list_add_caption(self, driver):
        try:
            self.page_edit.auto_caption.enter_caption_list()
            self.click(L.edit.auto_caption.more)
            assert self.page_edit.auto_caption.caption_list_add_caption()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Caption List_Delete Caption')
    def test_auto_caption_caption_list_delete_caption(self, driver):
        try:
            assert self.page_edit.auto_caption.caption_list_delete_caption()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Caption List_Select')
    def test_auto_caption_select(self, driver):
        try:
            assert self.page_edit.auto_caption.caption_list_select()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    @allure.title('Edit Text')
    def test_auto_caption_edit_text(self, driver):
        try:
            self.click(L.edit.auto_caption.back)
            self.click(L.edit.auto_caption.caption_list_doen)
            self.element(L.edit.timeline.clip_title).click()
            assert self.page_edit.auto_caption.edit_text()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.auto_caption.start_with_auto_caption('pip video')
            raise Exception

    # @allure.title('Template')
    # def test_auto_caption_template(self, driver):
    #     try:


    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()

    #         self.page_edit.auto_caption.start_with_auto_caption('pip video')
    #         raise Exception