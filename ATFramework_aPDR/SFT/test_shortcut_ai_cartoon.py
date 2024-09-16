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


@allure.epic("Shortcut - AI Cartoon")
class Test_Shortcut_AI_Cartoon:
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

    def compare_crop(self, data):
        preview = self.page_edit.get_preview_pic()
        result = not HCompareImg(preview, data['pic_before_crop']).ssim_compare()
        data['pic_before_crop'] = preview
        return result

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Enter from AI creation")
    def test_entry_from_ai_creation(self, data):
        try:
            assert self.page_shortcut.enter_ai_feature('AI Cartoon')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise


    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Back to AI creation")
    def test_back_to_ai_creation(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_ai_feature('AI Cartoon')

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Enter from Shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            assert self.page_shortcut.enter_shortcut('AI Cartoon')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Back to Shortcut")
    def test_back_to_shortcut(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Cartoon')

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Don't show again")
    def test_demo_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.demo_dont_show_again('AI Cartoon')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Enter")
    @allure.title("Enter media picker")
    def test_enter_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Cartoon')

            assert self.page_shortcut.enter_media_picker()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Back")
    @allure.title("From media picker")
    def test_back_from_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Cartoon')

            assert self.page_shortcut.back_from_media_picker()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Import")
    @allure.title("Photo")
    def test_import_photo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Cartoon')

            assert self.page_shortcut.enter_editor(shortcut_name='AI Cartoon', media_type='photo', file=photo_9_16)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Back")
    @allure.title("From editor")
    def test_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Cartoon', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Style")
    @allure.title("Generate")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            data["pic_history"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("Style")
    @allure.title("Regenerate")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Enabled")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            data["pic_before_compare"] = self.page_edit.get_preview_pic()

            self.click(L.main.shortcut.ai_art.compare)

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Preview change")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            self.click(L.main.shortcut.ai_art.compare)
            data["pic_after_compare"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("Compare")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            self.click(L.main.shortcut.ai_art.compare)

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Disable")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))
            data["pic_before_compare"] = self.page_edit.get_preview_pic()

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Preview resume")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()

            self.page_main.shortcut.waiting_generated(L.main.shortcut.ai_art.style_name(2))

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("History")
    @allure.title("Enter generate history")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            self.click(L.main.shortcut.ai_art.history)

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("History")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_media.waiting_loading()
            self.click(L.main.shortcut.ai_art.history)

            pytest.fail(f"{str(e)}")

    @allure.feature("Editor")
    @allure.story("History")
    @allure.title("Close history")
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
            self.page_shortcut.enter_ai_feature('AI Cartoon')
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
    def test_crop_reset(self, data):
        try:
            self.click(L.main.shortcut.ai_sketch.crop)
            self.click(L.edit.crop.reset)
            self.page_main.shortcut.waiting_generated(L.edit.crop.apply)
            preview = self.page_edit.get_preview_pic()

            assert not HCompareImg(preview, data['pic_before_crop']).ssim_compare()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise


    @allure.feature("Export")
    @allure.story("Cancel")
    @allure.title("Close panel")
    def test_export_cancel(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Cartoon', media_type='photo', file=photo_9_16)
                self.page_shortcut.style_generate()

            assert self.page_shortcut.export_cancel()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Save")
    @allure.title("Save image")
    def test_export_save_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Cartoon', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.export_save_image()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Back")
    @allure.title("To editor")
    def test_export_back_to_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Cartoon', media_type='photo', file=photo_9_16)
                self.page_shortcut.export_save_image()

            assert self.page_shortcut.export_back_to_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Back")
    @allure.title("To launcher")
    def test_export_back_to_launcher(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Cartoon', media_type='photo', file=photo_9_16)

            self.page_shortcut.export_save_image()

            assert self.page_shortcut.export_back_to_launcher()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise
