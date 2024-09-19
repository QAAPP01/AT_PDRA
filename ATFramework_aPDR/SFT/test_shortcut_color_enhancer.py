import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.SFT.test_aPDR_SFT_Scenario_06_01 import file_photo
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


@allure.epic("Shortcut - Color Enhancer")
class Test_Shortcut_HSL:
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

    @allure.feature("Media Picker")
    @allure.story("Enter")
    @allure.title("Enter media picker")
    def test_entry_media_picker(self, data):
        try:
            assert self.page_shortcut.enter_media_picker('Color\nEnhancer')

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
                self.page_shortcut.enter_media_picker('Color\nEnhancer')

            assert self.page_shortcut.back_from_media_picker()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Enter Trim")
    def test_video_entry_trim(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_trim_before_edit('Color\nEnhancer')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Back from trim")
    def test_video_back_from_trim(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_trim_before_edit('Color\nEnhancer')

            assert self.page_shortcut.back_from_trim()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Video")
    @allure.title("Trim and import")
    def test_video_trim_and_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Color\nEnhancer')

            assert self.page_shortcut.trim_and_import()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Back from editor")
    def test_video_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Import video")
    def test_video_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Color\nEnhancer')

            assert self.page_shortcut.enter_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview play")
    def test_video_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.preview_play()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview pause")
    def test_video_pause_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.preview_pause()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview beginning")
    def test_video_preview_beginning(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.preview_beginning()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Video")
    @allure.title("Preview ending")
    def test_video_preview_ending(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.preview_ending()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Video")
    @allure.title("Back from export")
    def test_video_back_from_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.export_back()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Video")
    @allure.title("Produce Save")
    def test_video_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.export()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Produced")
    @allure.title("Back to editor")
    def test_export_back_to_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')
                self.page_shortcut.export()

            assert self.page_shortcut.export_back_to_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Import photo")
    def test_photo_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Color\nEnhancer')

            self.page_shortcut.back_from_editor()

            assert self.page_shortcut.enter_editor(media_type='photo', file=photo_9_16)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Back from editor")
    def test_photo_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer')

            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview play")
    def test_photo_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('Color\nEnhancer')

            self.page_shortcut.enter_editor(media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_play()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview pause")
    def test_photo_pause_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_pause()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview beginning")
    def test_photo_preview_beginning(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_beginning()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Editor")
    @allure.story("Photo")
    @allure.title("Preview ending")
    def test_photo_preview_ending(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.preview_ending()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Photo")
    @allure.title("Back from export")
    def test_photo_back_from_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.export_back()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Photo")
    @allure.title("Produce save")
    def test_photo_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer', media_type='photo', file=photo_9_16)

            assert self.page_shortcut.export()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Export")
    @allure.story("Produced")
    @allure.title("Back to launcher")
    def test_export_back_to_launcher(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('Color\nEnhancer', media_type='photo', file=photo_9_16)

            self.page_shortcut.export()

            assert self.page_shortcut.export_back_to_launcher()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise
        
    def sce_6_1_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.main.shortcut.hsl.hue_value).text

            if value == '0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.hue_slider)
            value = self.element(L.main.shortcut.hsl.hue_value).text

            if value == '-50':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.hue_slider)

            return "FAIL"

    def sce_6_1_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.hue_slider)
            value = self.element(L.main.shortcut.hsl.hue_value).text

            if value == '50':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.hue_slider)

            return "FAIL"

    def sce_6_1_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.saturation_slider)
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '-50':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.saturation_slider)

            return "FAIL"

    def sce_6_1_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.saturation_slider)
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '50':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.saturation_slider)

            return "FAIL"

    def sce_6_1_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.main.shortcut.hsl.luminance_value).text

            if value == '0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.luminance_slider)
            value = self.element(L.main.shortcut.hsl.luminance_value).text

            if value == '-50':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_min(L.main.shortcut.hsl.luminance_slider)

            return "FAIL"

    def sce_6_1_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_1_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.luminance_slider)
            value = self.element(L.main.shortcut.hsl.saturation_value).text

            if value == '50':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)
            self.original = self.page_edit.get_preview_pic()
            self.driver.drag_slider_to_max(L.main.shortcut.hsl.luminance_slider)

            return "FAIL"

    def sce_6_1_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            after = self.page_edit.get_preview_pic()

            if not HCompareImg(after, self.original).histogram_compare():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Color\nEnhancer')
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.click(L.main.shortcut.hsl.red)

            return "FAIL"

    def sce_6_4_37(self):
        uuid = 'bb17a360-fce3-444f-976c-9e0022ce648b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.switch_to_photo_library()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.descending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name, reverse=True)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()

            return "FAIL"

    def sce_6_4_38(self):
        uuid = 'e2848afa-8649-4064-8649-db1da9d1dec4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.ascending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_39(self):
        uuid = 'e571055b-e737-4284-9b5c-cc698238afa1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            file_name = "jpg.jpg"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_40(self):
        uuid = 'bdb051bd-5092-4e9e-9430-1dee5a391f4f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            file_name = "gif.gif"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_41(self):
        uuid = 'a4302371-48b7-4cac-86c2-7a85889d793b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            file_name = "png.png"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_42(self):
        uuid = '7f2aeaf7-62d2-4348-b7a5-b4c377cb3ea6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            if not self.is_exist(L.import_media.media_library.color_board):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Can find color_board'

            self.click(L.main.ai_effect.back)

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_43(self):
        uuid = '47039469-aa7c-4628-bd2a-03729c325a41'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_44(self):
        uuid = '70dd1f07-5aea-403a-9029-9419f42d4edc'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_45(self):
        uuid = '0591683c-e463-4e99-88ef-3a74cce46e17'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_46(self):
        uuid = '37c652fe-f97f-451f-a0e3-63d53e859ac3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_47(self):
        uuid = '41c0c860-9e5a-4545-ad54-57fea2dbf769'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_48(self):
        uuid = 'fa743ffe-22c0-485a-adfb-2975d16b5537'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.main.ai_effect.try_now)

            self.page_media.select_photo_library("getty")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_49(self):
        uuid = '041fcba0-af79-439f-9378-009fc9e08c9f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_50(self):
        uuid = 'f7e26440-d1b1-4704-b76e-88117bf520ba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_51(self):
        uuid = 'c2ad3af3-00a1-4e6e-8d0c-4cacb75e98b5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_52(self):
        uuid = 'a11cb1b4-cd8d-4f2f-8c28-7a4a7cae5aed'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_53(self):
        uuid = 'afa2ced7-bdb2-4054-982c-99c3a06fb899'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("getty_pro")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_54(self):
        uuid = '7718ae03-38e7-4989-8861-9ecc98bd6b23'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_55(self):
        uuid = '4d1a50ad-1226-41fd-9695-9bfd0e531b1d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_56(self):
        uuid = 'ee83ed66-bb25-4843-aad0-545fe8c5d624'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_57(self):
        uuid = 'ebe7c158-bf56-4984-9646-d3e5e59dbb26'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.gettyimages_premium.buy_dialog.btn_buy)
            self.click(find_string("1-tap buy"), 10)
            self.click(L.import_media.media_library.media(), 10)
            self.click(L.import_media.media_library.next)

            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_58(self):
        uuid = '0597ea98-5cae-4b2a-8714-8289bb624ca2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("pexels")
            self.click(L.import_media.media_library.pexels_link)

            if self.is_exist(find_string("pexels.com")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Not find "pexels.com"'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_59(self):
        uuid = 'c9683ebd-c159-4c88-9a96-3cdcf4a637e4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            pic_src = self.page_main.h_full_screenshot()
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_60(self):
        uuid = '9df4e187-e974-4c26-ba04-fa308832c0a9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_61(self):
        uuid = 'e964df3f-8d0a-4eac-b898-49be83ac472c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_62(self):
        uuid = '5f904d0e-7fb8-48b2-9eed-18806a334f2b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_63(self):
        uuid = '83c6529e-f81b-4f31-a726-82f5cb4b3df5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("pixabay")
            self.click(L.import_media.media_library.pixabay_link)

            if self.is_exist(find_string("pixabay.com")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Not find "pixabay.com"'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_64(self):
        uuid = 'ffe5e33c-17cd-4856-b6f1-18898714f950'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            pic_src = self.page_main.h_full_screenshot()
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_65(self):
        uuid = '50ebb786-fa6b-4ac7-9f12-34feb0b6a0fe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_66(self):
        uuid = '68727700-ba6e-4be4-a988-386898963aba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_67(self):
        uuid = '57850b35-b48c-4a3f-affc-1e87a89763c7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_68(self):
        uuid = 'f683a635-e229-4ce7-8fee-3f34ff839c7a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.click(L.import_media.media_library.video.video_capture)
            self.click(L.import_media.media_library.video.start_recording)
            time.sleep(5)
            self.click(L.import_media.media_library.video.stop_recording)
            self.click(L.import_media.media_library.video.camera_ok)
            self.page_media.sort_date_descend()
            self.click(L.import_media.media_library.media())
            self.click(L.import_media.media_library.next)
            import_timeout = self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce) and import_timeout:
                result = True
                fail_log = None
            elif not import_timeout:
                result = False
                fail_log = '\n[Fail] Media import timeout'
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_69(self):
        uuid = '6b4b4ae3-2d24-4914-aebe-688bb2424c75'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.photo.photo_capture)
            self.click(L.import_media.media_library.photo.take_picture)
            self.click(L.import_media.media_library.photo.camera_ok)
            self.click(L.import_media.media_library.media())
            self.click(L.import_media.media_library.next)
            import_timeout = self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce) and import_timeout:
                result = True
                fail_log = None
            elif not import_timeout:
                result = False
                fail_log = '\n[Fail] Media import timeout'
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_70(self):
        uuid = '19a47ca2-91a4-40cb-a7ed-481baa667804'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)
            self.page_media.select_video_library("google_drive")
            self.click(('id', 'com.google.android.gms:id/account_name'))
            self.page_media.waiting_loading()
            self.click(L.import_media.media_library.google_folder())
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_71(self):
        uuid = '4bcad19b-ad8b-48c8-a2bb-1ba5c9ec4be6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)
            self.page_media.select_photo_library("google_drive")
            self.click(('id', 'com.google.android.gms:id/account_name'), 3)
            self.page_media.waiting_loading()
            self.click(L.import_media.media_library.google_folder())
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_72(self):
        uuid = 'e424e887-0930-4d95-b868-aa69a8d9371f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.play_btn)
            playing_time = self.element(L.ai_effect.editor.playing_time).text

            if playing_time != "00:00":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] playing time is not increase: {playing_time}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()
            return "FAIL"

    def sce_6_4_73(self):
        uuid = '2be47a53-4aa2-4337-8415-d54d12f9e7a6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True, clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            selected_num = len(self.elements(L.import_media.media_library.media_order(0)))

            if selected_num == 2:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] media order number incorrect: {selected_num}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            return "FAIL"

    def sce_6_4_74(self):
        uuid = '07286423-8bf8-4644-a21a-d2e7d07b15f9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            if self.element(L.import_media.media_library.next).get_attribute("enabled") == "true":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] "Next" button is not clickable'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            return "FAIL"

    def sce_6_5_1(self):
        uuid = '5f7ad02b-21bd-49bd-9981-4bdf351b12ff'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.next)

            if self.is_exist(L.import_media.media_library.downloading):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] downloading bar is not exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            self.click(L.import_media.media_library.next)
            return "FAIL"

    def sce_6_5_2(self):
        uuid = 'eaaadb38-b1d0-4554-9c21-2352d30cd212'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.cancel)

            if self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] "Next" button is not exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)

            return "FAIL"

    def sce_6_6_1(self):
        uuid = '6cbfa1ad-7017-4fba-83da-ce0d89d04513'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.page_ai_effect.leave_editor_to_library:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] back to library fail'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_template_library()
            return "FAIL"

    def sce_6_6_2(self):
        uuid = '6c2a7cab-5d78-418b-abd4-b35f9d53aad3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.enter_editor(skip_enter_template_library=True, clip=2)
            time.sleep(2)

            if self.element(L.ai_effect.editor.playing_time).text != "00:00":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Playing time = "00:00"'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_3(self):
        uuid = '485634cf-42c7-4821-998c-7cd85c29d18e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.replace_all)

            if self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No "Next" button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_4(self):
        uuid = '2b98fc6b-6ce5-45d0-9362-89b7f3c2ce68'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.back)
            self.click(L.ai_effect.editor.volume_entry)
            volume = self.element(L.ai_effect.editor.slider_text).text

            if volume == "100":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Volume not 100: {volume}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_5(self):
        uuid = 'eb0b0f9b-30bb-446f-b2fa-9ee61e81475a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.volume.play)

            if not self.is_exist(L.ai_effect.editor.volume.play, 2):
                self.click(L.ai_effect.editor.preview)
                if self.is_exist(L.ai_effect.editor.volume.play):
                    result = True
                    fail_log = None
                else:
                    result = False
                    fail_log = f'\n[Fail] Preview is not stopped after tapped'
            else:
                result = False
                fail_log = f'\n[Fail] Play btn is not disappear tapped'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_6(self):
        uuid = '3994d2ce-a9a4-4ab4-a917-b655ef53e227'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.volume.cancel)

            if self.is_exist(L.ai_effect.editor.volume_entry):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No volume entry'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_7(self):
        uuid = '12304abd-5541-48f7-9d50-1489c5460bd1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_main.drag_element(L.ai_effect.editor.volume.slider_text, L.ai_effect.editor.volume.slider)
            self.click(L.ai_effect.editor.volume.apply)

            if self.is_exist(L.ai_effect.editor.volume_entry):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No volume entry'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_8(self):
        uuid = '3a6192b7-3212-441e-8f7e-eb1b97563169'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            playing_time = self.click(L.ai_effect.editor.playing_time).text
            self.click(L.ai_effect.editor.play_btn)
            time.sleep(2)

            if self.click(L.ai_effect.editor.playing_time).text != playing_time:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Playing time no change'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_9(self):
        uuid = '59c63a35-fbec-4df1-8745-a42cb81c9f40'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_main.drag_slider_from_center_to_left(L.ai_effect.editor.playing_bar)
            preview_before = self.page_main.get_picture(L.ai_effect.editor.preview)
            self.page_main.drag_slider_from_center_to_right(L.ai_effect.editor.playing_bar)
            preview_after = self.page_main.get_picture(L.ai_effect.editor.preview)

            if not HCompareImg(preview_after, preview_before).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are the same after dragged slider'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_10(self):
        uuid = 'e9988c06-7a3c-49cd-955b-4ba45e5fa138'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Replace"))

            if not self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Exist "Next" button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_11(self):
        uuid = '77d3f699-a355-484a-a7f7-3a4f26362519'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.back)
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Crop & Range"))
            self.driver.zoom(L.ai_effect.editor.preview)
            self.driver.drag_slider_from_center_to_left(L.ai_effect.editor.crop_range.trim_bar)
            pic_src = self.page_main.get_picture(L.ai_effect.editor.preview)
            self.click(L.ai_effect.editor.crop_range.done)
            self.page_media.waiting_download()
            pic_tgt = self.page_main.get_picture(L.ai_effect.editor.preview)

            if HCompareImg(pic_tgt, pic_src).full_compare() >= 0.9:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Similarity < 0.9'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_12(self):
        uuid = '7747da3f-31f6-4c19-8eae-a9fc1bf052b3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Volume"))
            volume = self.element(L.ai_effect.editor.slider_text).text

            if not self.is_exist(L.ai_effect.editor.volume.play, 2):
                self.click(L.ai_effect.editor.preview)
                if self.is_exist(L.ai_effect.editor.volume.play):
                    if volume == "0":
                        result = True
                        fail_log = None
                    else:
                        result = False
                        fail_log = f'\n[Fail] Volume not 100: {volume}'
                else:
                    result = False
                    fail_log = f'\n[Fail] Preview is not stopped after tapped'
            else:
                result = False
                fail_log = f'\n[Fail] Play btn is not disappear tapped'

            self.driver.drag_slider_from_left_to_right()
            self.click(L.ai_effect.editor.volume.apply)

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_13(self):
        uuid = '2776fd95-8f2d-4019-99c9-4217435a9171'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.export)

            if self.is_exist(L.ai_effect.editor.produce.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_1(self):
        uuid = '74673b45-4847-48f8-b55e-2395b40dd80d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.produce.back)

            if not self.is_exist(L.ai_effect.editor.produce.back):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_7_2(self):
        uuid = '6f5aca48-62ff-49be-a11e-0569569e8116'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.export)
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_1)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "0.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_3(self):
        uuid = '4fe8c038-5eac-41a3-8cfa-d6d4b973ebe1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_2)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "1.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_4(self):
        uuid = '52b6104e-32de-4807-971c-9d37ad05737d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_3)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "2.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_5(self):
        uuid = '1fb7010d-3f70-46a1-97d8-b7af71614290'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_4)

            if self.is_exist(L.produce.iap_back):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No IAP page'

            self.click(L.produce.iap_back)

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_6(self):
        uuid = '855995da-c1ed-455f-b4bc-0932fee039d4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.produce.produce)

            if self.is_exist(L.ai_effect.producing.progress_bar):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No progress bar'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            return "FAIL"

    def sce_6_7_7(self):
        uuid = '4167881a-77ab-42c0-b923-9922bf7f2656'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.producing.cancel)
            self.click(L.ai_effect.editor.producing.cancel_ok)

            if self.is_exist(L.ai_effect.editor.export):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No export button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break
            return "FAIL"

    def sce_6_8_1(self):
        uuid = '1f876e02-b413-4a06-9147-e8c9f3535988'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.produce.produced_back)

            if self.is_exist(L.ai_effect.editor.export):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No export button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_8_2(self):
        uuid = '60f0b428-a199-432a-a07a-4cf49e43aa38'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break

            self.click(L.ai_effect.producing.save_to_file)
            current_pack = self.driver.driver.current_package

            if current_pack != pdr_package:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] current_package is still pdr: {current_pack}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break
            return "FAIL"

    def sce_6_8_3(self):
        uuid = 'edde24ab-5aa4-49c9-b9ea-b68018b17148'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.driver.activate_app(pdr_package)
            self.click(L.ai_effect.producing.share_app_name())
            self.click(L.ai_effect.producing.share_ok, 2)
            current_pack = self.driver.driver.current_package

            if current_pack != pdr_package:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] current_package is still pdr: {current_pack}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break

            return "FAIL"

    def sce_6_8_4(self):
        uuid = '3d8d3218-05f2-4306-8187-82b87155a3bb'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.driver.back()
            self.click(L.ai_effect.producing.done)

            if self.is_exist(L.ai_effect.template.template()):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No template'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"
