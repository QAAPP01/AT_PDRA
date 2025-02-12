import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.SFT.test_file import *


@allure.epic("Shortcut - AI Sketch")
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
            assert self.page_shortcut.enter_ai_feature('AI Sketch')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Back to AI creation")
    def test_back_to_ai_creation(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_ai_feature('AI Sketch')

            assert self.page_shortcut.back_from_demo()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    # @allure.feature("Entry")
    # @allure.story("Demo")
    # @allure.title("Enter from Shortcut")
    # def test_entry_from_shortcut(self, data):
    #     try:
    #         assert self.page_shortcut.enter_shortcut('AI Sketch')
    #
    #     except Exception:
    #         traceback.print_exc()
    #         data['last_result'] = False
    #         raise
    #
    # @allure.feature("Entry")
    # @allure.story("Demo")
    # @allure.title("Back to Shortcut")
    # def test_back_to_shortcut(self, data):
    #     try:
    #         if self.last_is_fail(data):
    #             pytest.skip('[Skip] due to enter from shortcut failed')
    #
    #         assert self.page_shortcut.back_from_demo()
    #
    #     except Exception:
    #         traceback.print_exc()
    #         data['last_result'] = False
    #         raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Don't show again")
    def test_demo_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.demo_dont_show_again('AI Sketch')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Demo")
    @allure.title("Reset don't show again")
    def test_reset_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_ai_feature('AI Sketch', check=False)

            assert self.page_shortcut.reset_dont_show_again('AI Sketch')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Recommendation")
    @allure.title("Close")
    def test_recommendation_close(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_ai_feature('AI Sketch')

            assert self.page_shortcut.recommendation_close()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Recommendation")
    @allure.title("Continue")
    def test_recommendation_continue(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.recommendation_continue('AI Sketch')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Back")
    @allure.title("From media picker")
    def test_back_from_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Sketch')

            assert self.page_shortcut.back_from_media_picker()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Recommendation")
    @allure.title("Don't show again")
    def test_recommendation_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.recommendation_dont_show_again('AI Sketch')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Recommendation")
    @allure.title("Reset don't show again")
    def test_recommendation_reset_dont_show_again(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.recommendation_reset('AI Sketch')

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Import")
    @allure.title("Photo")
    def test_import_photo(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_editor(shortcut_name='AI Sketch', media_type='photo', file=photo_9_16)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Back")
    @allure.title("From editor")
    def test_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor(shortcut_name='AI Sketch', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.back_from_editor()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Style")
    @allure.title("Generate")
    def test_style_generate(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Sketch')

            self.page_shortcut.enter_editor(media_type='photo', file=photo_9_16)
            
            self.page_shortcut.style_generate()

            preview = self.page_edit.get_preview_pic()
            data["pic_history"] = preview

            assert HCompareImg(preview).is_not_black()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Style")
    @allure.title("Regenerate")
    def test_style_regenerate(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.style_generate()

            self.page_shortcut.style_regenerate()

            preview = self.page_edit.get_preview_pic()
            assert HCompareImg(preview).is_not_black()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Enabled")
    def test_compare_enabled(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            data["pic_before_compare"] = self.page_edit.get_preview_pic()

            assert self.page_shortcut.compare_enabled()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Preview change")
    def test_compare_preview_change(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.compare_enabled()

            data["pic_after_compare"] = self.page_edit.get_preview_pic()

            assert not HCompareImg(data["pic_before_compare"], data["pic_after_compare"]).ssim_compare()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Move compare line")
    def test_compare_move_line(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.compare_enabled()

            self.page_shortcut.compare_move_line()

            pic_after_drag = self.page_main.get_preview_pic()
            assert not HCompareImg(pic_after_drag, data["pic_after_compare"]).ssim_compare()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Disable")
    def test_compare_disable(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.compare_enabled()

            assert self.page_shortcut.compare_disable()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Compare")
    @allure.title("Preview resume")
    def test_compare_preview_resume(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.compare_enabled()
                self.page_shortcut.compare_disable()

            pic_preview = self.page_edit.get_preview_pic()

            assert HCompareImg(pic_preview, data["pic_before_compare"]).ssim_compare()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("History")
    @allure.title("Enter generate history")
    def test_history_enter(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.enter_history()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise
        
    @allure.feature("Editor")
    @allure.story("History")
    @allure.title("Reopen history image")
    def test_history_reopen_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.enter_history()

            assert self.page_shortcut.reopen_history_image(data["pic_history"])

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("History")
    @allure.title("Close history")
    def test_history_close(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.enter_history()

            assert self.page_shortcut.close_history()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise
            
    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Enter")
    def test_enter_crop(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.enter_crop()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Leave")
    def test_leave_crop(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.enter_crop()

            assert self.page_shortcut.leave_crop()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Original")
    def test_crop_original(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            data['pic_before_crop'] = self.page_edit.get_preview_pic()

            self.page_shortcut.crop_ratio('original')

            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Free")
    def test_crop_free(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('free')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("9:16")
    def test_crop_9_16(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('9:16')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("1:1")
    def test_crop_1_1(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('1:1')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("4:5")
    def test_crop_4_5(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('4:5')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("16:9")
    def test_crop_16_9(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('16:9')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("4:3")
    def test_crop_4_3(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('4:3')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("3:4")
    def test_crop_3_4(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('3:4')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("21:9")
    def test_crop_21_9(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_ratio('21:9')
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.story("Editor")
    @allure.title("Crop")
    @allure.step("Reset")
    def test_crop_reset(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.crop_reset()
            assert self.compare_crop(data)

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Cancel")
    @allure.title("Close panel")
    def test_export_cancel(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.style_generate()

            assert self.page_shortcut.export_cancel()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Save")
    @allure.title("Save image")
    def test_export_save_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.export_save_image()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Back")
    @allure.title("To editor")
    def test_export_back_to_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)
                self.page_shortcut.export_save_image()

            assert self.page_shortcut.export_back_to_editor()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Back")
    @allure.title("To launcher")
    def test_export_back_to_launcher(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Sketch', media_type='photo', file=photo_9_16)

            self.page_shortcut.export_save_image()

            assert self.page_shortcut.export_back_to_launcher()

        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise
        