import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

photo_9_16 = 'photo_9_16.jpg'


@allure.epic("Shortcut")
@allure.feature("AI Sketch")
class Test_Shortcut_AI_Sketch:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @pytest.fixture(scope="module")
    def shared_data(self):
        data = {}
        yield data

    @allure.story("Entry")
    @allure.title("From AI creation")
    def test_entry_from_ai_creation(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')

            assert self.is_exist(find_string('AI Sketch'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            pytest.fail(f"{str(e)}")

    @allure.story("Entry")
    @allure.title("Back to AI creation")
    def test_back_to_ai_creation(self, driver):
        try:
            self.click(L.main.shortcut.demo_back)

            assert self.is_exist(find_string('AI Creation'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            pytest.fail(f"{str(e)}")

    @allure.story("Media Picker")
    @allure.title("Recommendation close")
    def test_recommendation_close(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.main.shortcut.ai_sketch.close)

            assert self.is_exist(find_string('AI Creation'))

        except Exception as e:
            traceback.print_exc()

            pytest.fail(f"{str(e)}")

    @allure.story("Media Picker")
    @allure.title("Recommendation continue")
    def test_recommendation_continue(self, driver):
        try:
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.main.shortcut.ai_sketch.continue_btn)

            assert self.is_exist(find_string('Add Media'))

        except Exception as e:
            traceback.print_exc()

            pytest.fail(f"{str(e)}")

    @allure.story("Media Picker")
    @allure.title("Recommendation dont show again")
    def test_recommendation_dont_show(self, driver):
        try:
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.main.shortcut.ai_sketch.dont_show_again)
            self.click(L.main.shortcut.ai_sketch.continue_btn)

            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)

            assert not self.is_exist(L.main.shortcut.ai_sketch.continue_btn)

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            pytest.fail(f"{str(e)}")

    @allure.story("Media Picker")
    @allure.title("Back from media picker")
    def test_back_from_media(self, driver):
        try:
            self.click(L.import_media.media_library.back)

            assert self.is_exist(find_string('AI Creation'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            pytest.fail(f"{str(e)}")

    @allure.story("Media Picker")
    @allure.title("Import photo")
    def test_import_photo(self, driver):
        try:
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            assert self.is_exist(find_string('Export'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Back to media picker")
    def test_back_to_media_picker(self, driver):
        try:
            self.click(L.main.shortcut.editor_back)

            assert self.is_exist(find_string('Add Media'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Generate style")
    def test_gen_style(self, driver):
        try:
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

            preview = self.page_edit.get_preview_pic()
            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Regenerate style")
    def test_regenerate_style(self, driver):
        try:
            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.regenerate)
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

            preview = self.page_edit.get_preview_pic()
            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare button enabled")
    def test_compare_button_enabled(self, driver, shared_data):
        try:
            shared_data["pic_before_compare"] = self.page_edit.get_preview_pic()
            self.click(L.main.shortcut.ai_art.compare)

            assert self.element(L.main.shortcut.ai_art.compare).get_attribute('selected') == 'true' and self.element(
                L.main.shortcut.ai_art.compare).text == "Compare On"

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")
            shared_data["pic_before_compare"] = self.page_edit.get_preview_pic()

            self.click(L.main.shortcut.ai_art.compare)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare preview display")
    def test_compare_preview(self, driver, shared_data):
        try:
            shared_data["pic_after_compare"] = self.page_edit.get_preview_pic()

            assert not HCompareImg(shared_data["pic_before_compare"], shared_data["pic_after_compare"]).ssim_compare()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")
            self.click(L.main.shortcut.ai_art.compare)
            shared_data["pic_after_compare"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Move compare line")
    def test_move_compare_line(self, driver, shared_data):
        try:
            thumb = self.element(L.main.shortcut.photo_enhance.compare_thumb)
            rect = thumb.rect
            x = rect['x']
            y = rect['y']
            self.page_main.h_drag_element(thumb, x - 100, y)
            pic_after_drag = self.page_main.get_preview_pic()

            assert not HCompareImg(pic_after_drag, shared_data["pic_after_compare"]).ssim_compare()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")
            self.click(L.main.shortcut.ai_art.compare)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare button disabled")
    def test_compare_button_disabled(self, driver, shared_data):
        try:
            self.click(L.main.shortcut.ai_art.compare)

            assert self.element(L.main.shortcut.ai_art.compare).get_attribute('selected') == 'false' and self.element(
                L.main.shortcut.ai_art.compare).text == "Compare Off"

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")
            shared_data["pic_before_compare"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare preview not display")
    def test_compare_preview_not_display(self, driver, shared_data):
        try:
            pic_preview = self.page_edit.get_preview_pic()

            assert HCompareImg(pic_preview, shared_data["pic_before_compare"]).ssim_compare()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.style_name(2))
                self.click(aid('[AID]ConfirmDialog_No'), 1)
                self.page_main.shortcut.waiting_generated()
                if not self.click(id('ok_button'), 1):
                    break
            else:
                raise Exception(f"Exceeded retry limit: {retry}")

            pytest.fail(f"{str(e)}")