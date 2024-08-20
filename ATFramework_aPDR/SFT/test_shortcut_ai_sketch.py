import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

photo_9_16 = 'photo_9_16.jpg'


@allure.epic("Shortcut")
@allure.feature("AI Sketch")
class Test_Shortcut_AI_Sketch:
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

    @allure.story("Entry")
    @allure.title("From AI creation")
    def test_entry_from_ai_creation(self, driver):
        try:
            self.page_main.enter_launcher()

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
    def test_import_photo(self, data):
        try:
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            assert self.is_exist(find_string('Export'))

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Play preview")
    def test_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch')

            assert self.page_shortcut.play_preview()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

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
    def test_gen_style(self, driver, data):
        try:
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            preview = self.page_edit.get_preview_pic()
            data["pic_history"] = preview
            assert HCompareImg(preview).is_not_black()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            data["pic_history"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Regenerate style")
    def test_regenerate_style(self, driver):
        try:
            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.regenerate)
            preview = self.page_edit.get_preview_pic()
            assert HCompareImg(preview).is_not_black()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare button enabled")
    def test_compare_button_enabled(self, driver, data):
        try:
            data["pic_before_compare"] = self.page_edit.get_preview_pic()
            self.click(L.main.shortcut.ai_art.compare)

            assert self.element(L.main.shortcut.ai_art.compare).get_attribute('selected') == 'true' and self.element(
                L.main.shortcut.ai_art.compare).text == "Compare On"

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            data["pic_before_compare"] = self.page_edit.get_preview_pic()

            self.click(L.main.shortcut.ai_art.compare)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare preview display")
    def test_compare_preview(self, driver, data):
        try:
            data["pic_after_compare"] = self.page_edit.get_preview_pic()

            assert not HCompareImg(data["pic_before_compare"], data["pic_after_compare"]).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            self.click(L.main.shortcut.ai_art.compare)
            data["pic_after_compare"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Move compare line")
    def test_move_compare_line(self, driver, data):
        try:
            thumb = self.element(L.main.shortcut.photo_enhance.compare_thumb)
            rect = thumb.rect
            x = rect['x']
            y = rect['y']
            self.page_main.h_drag_element(thumb, x - 100, y)
            pic_after_drag = self.page_main.get_preview_pic()

            assert not HCompareImg(pic_after_drag, data["pic_after_compare"]).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            self.click(L.main.shortcut.ai_art.compare)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare button disabled")
    def test_compare_button_disabled(self, driver, data):
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
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            data["pic_before_compare"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Compare preview resume")
    def test_compare_preview_resume(self, driver, data):
        try:
            pic_preview = self.page_edit.get_preview_pic()

            assert HCompareImg(pic_preview, data["pic_before_compare"]).ssim_compare()

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
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            self.click(L.main.shortcut.ai_art.history)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Reopen history image")
    def test_reopen_history_image(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_art.history)
            self.click(L.main.shortcut.ai_art.history_image(2))
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview, data["pic_history"]).ssim_compare()

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
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            pytest.fail(f"{str(e)}")
            
    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Enter")
    def test_enter_crop(self, driver):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)

            assert self.is_exist(find_string('Crop Photo'))

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

            self.click(L.main.shortcut.ai_sketch.crop)

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Leave")
    def test_leave_crop(self, driver):
        try:
            self.click(L.edit.crop.cancel)

            assert self.is_exist(L.main.shortcut.ai_art.style_name())

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Original")
    def test_crop_original(self, driver, data):
        try:
            data['pic_crop_original'] = self.page_edit.get_preview_pic()
            self.click(L.main.shortcut.ai_sketch.crop)
            self.page_main.h_swipe_element(L.edit.crop.btn_free, L.edit.crop.btn_9_16, 3)
            time.sleep(1)
            self.click(L.edit.crop.btn_original)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_crop_original']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Free")
    def test_crop_free(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.btn_free)
            self.page_edit.drag_crop_boundary(0.6, 0.9)
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("9:16")
    def test_crop_9_16(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.btn_9_16)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("1:1")
    def test_crop_1_1(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.btn_1_1)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("4:5")
    def test_crop_4_5(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.btn_4_5)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("16:9")
    def test_crop_16_9(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.btn_16_9)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("4:3")
    def test_crop_4_3(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.btn_4_3)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("3:4")
    def test_crop_3_4(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.page_main.h_swipe_element(L.edit.crop.btn_4_3, L.edit.crop.btn_free, 3)
            time.sleep(1)
            self.click(L.edit.crop.btn_3_4)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("21:9")
    def test_crop_21_9(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.page_main.h_swipe_element(L.edit.crop.btn_4_3, L.edit.crop.btn_free, 3)
            time.sleep(1)
            self.click(L.edit.crop.btn_21_9)
            self.page_edit.drag_crop_boundary()
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            preview = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

        finally:
            data['pic_before_crop'] = preview

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Reset")
    def test_crop_reset(self, driver, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.reset)
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

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

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

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
            self.page_main.enter_ai_feature('AI Sketch')
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
            self.page_main.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")
            