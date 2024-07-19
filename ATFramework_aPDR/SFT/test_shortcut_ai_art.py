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
@allure.feature("AI Art")
class Test_Shortcut_AI_Art:
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
    def shared_data(self):
        data = {}
        yield data

    @allure.story("Entry")
    @allure.title("From shortcut")
    def test_entry_from_shortcut(self, driver):
        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Art')

            assert self.is_exist(find_string('AI Art'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_ai_feature('AI Art')
            pytest.fail(f"{str(e)}")

    @allure.story("Entry")
    @allure.title("Back to launcher")
    def test_back_to_launcher(self, driver):
        try:
            self.click(L.main.shortcut.demo_back)

            assert self.is_exist(L.main.shortcut.shortcut_name(0))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            pytest.fail(f"{str(e)}")

    @allure.story("Entry")
    @allure.title("From AI creation")
    def test_entry_from_ai_creation(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')

            assert self.is_exist(find_string('AI Art'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
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
    @allure.title("Enter media picker")
    def test_enter_media_picker(self, driver):
        try:
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)

            assert self.is_exist(find_string('Add Media'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
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
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            assert self.is_exist(L.main.shortcut.export)

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
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Enter prompt")
    def test_enter_prompt(self, driver):
        try:
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            self.click(find_string('Custom'))
            self.element(L.main.shortcut.ai_art.prompt).send_keys('Apple')
            text = self.element(L.main.shortcut.ai_art.prompt).text

            assert text == 'Apple'

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
            self.click(find_string('Custom'))
            self.element(L.main.shortcut.ai_art.prompt).send_keys('Apple')
            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Clear prompt")
    def test_clear_prompt(self, driver):
        try:
            self.click(L.main.shortcut.ai_art.clear)
            text = self.element(L.main.shortcut.ai_art.prompt).text

            assert 'Please provide a description' in text

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
            self.click(find_string('Custom'))

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Generate custom prompt")
    def test_gen_custom_prompt(self, driver):
        try:
            self.element(L.main.shortcut.ai_art.prompt).send_keys('Apple')

            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.apply)
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

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Enter custom history")
    def test_enter_custom_history(self, driver):
        try:
            self.click(find_string('Custom'))
            self.is_exist(L.main.shortcut.ai_art.prompt, 5)
            self.click(L.main.shortcut.ai_art.custom_history)

            assert self.element(L.main.shortcut.ai_art.page_title).text == 'History'

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
            self.click(find_string('Custom'))
            self.click(L.main.shortcut.ai_art.custom_history)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Leave custom history")
    def test_leave_custom_history(self, driver):
        try:
            self.click(L.main.shortcut.ai_art.close)

            assert self.is_exist(L.main.shortcut.ai_art.prompt)

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
            self.click(find_string('Custom'))

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Import prompt history")
    def test_import_prompt_history(self, driver):
        try:
            self.click(find_string('Custom'))
            self.click(L.main.shortcut.ai_art.custom_history)
            prompt = self.element(L.main.shortcut.ai_art.history_prompt(0)).text
            self.click(L.main.shortcut.ai_art.history_prompt(0))

            assert self.element(L.main.shortcut.ai_art.prompt).text == prompt

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
            self.click(find_string('Custom'))
            self.click(L.main.shortcut.ai_art.custom_history)
            self.click(L.main.shortcut.ai_art.history_prompt(0))

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Regenerate history prompt")
    def test_regenerate_history_prompt(self, driver):
        try:
            retry = 30
            for i in range(retry):
                self.click(L.main.shortcut.ai_art.apply)
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

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Generate style")
    def test_gen_style(self, driver, shared_data):
        try:
            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            preview = self.page_edit.get_preview_pic()
            shared_data["pic_history"] = preview
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
            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            shared_data["pic_history"] = self.page_edit.get_preview_pic()

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
            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare button enabled")
    def test_compare_button_enabled(self, driver, shared_data):
        try:
            shared_data["pic_before_compare"] = self.page_edit.get_preview_pic()
            self.click(L.main.shortcut.ai_art.compare)

            assert self.element(L.main.shortcut.ai_art.compare).get_attribute('selected') == 'true' and self.element(L.main.shortcut.ai_art.compare).text == "Compare On"

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

            self.page_main.shortcut.waiting_generated()
            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            self.click(L.main.shortcut.ai_art.compare)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare button disabled")
    def test_compare_button_disabled(self, driver, shared_data):
        try:
            self.click(L.main.shortcut.ai_art.compare)

            assert self.element(L.main.shortcut.ai_art.compare).get_attribute('selected') == 'false' and self.element(L.main.shortcut.ai_art.compare).text == "Compare Off"

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            shared_data["pic_before_compare"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare preview resume")
    def test_compare_preview_resume(self, driver, shared_data):
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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Enter history")
    def test_enter_history(self, driver):
        try:
            self.click(L.main.shortcut.ai_art.history)

            assert self.is_exist(find_string('History'))

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
            self.click(L.main.shortcut.ai_art.history)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Reopen history image")
    def test_reopen_history_image(self, driver, shared_data):
        try:
            self.click(L.main.shortcut.ai_art.history)
            self.click(L.main.shortcut.ai_art.history_image(2))
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview, shared_data["pic_history"]).ssim_compare()

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
            self.click(L.main.shortcut.ai_art.history)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Leave history")
    def test_leave_history(self, driver):
        try:
            self.click(L.main.shortcut.ai_art.close_history)

            assert not self.is_exist(find_string('History'))

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

            pytest.fail(f"{str(e)}")

    @allure.story("Export")
    @allure.title("Save Image")
    def test_save_image(self, driver):
        try:
            self.click(L.main.shortcut.export)
            self.click(find_string('Save Image'))

            assert self.is_exist(L.main.shortcut.save_to_camera_roll)

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            self.click(L.main.shortcut.export)
            self.click(find_string('Save Image'))

            pytest.fail(f"{str(e)}")

    @allure.story("Export")
    @allure.title("Back to editor")
    def test_back_to_editor(self, driver):
        try:
            self.click(L.main.shortcut.produce_back)

            assert self.is_exist(L.main.shortcut.editor_back)

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")
