import inspect
import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.SFT.test_file import *


@allure.epic('Timeline Master Video')
@allure.feature('Cutout')
class Test_Master_Video_Cutout:
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

    @allure.story('Back')
    @allure.title('Toolbar back')
    def test_toolbar_back(self, data):
        try:
            self.page_edit.create_project_and_enter_function("Cutout")
            self.click(L.edit.toolbar.sub_tool_back)

            assert self.is_exist(L.edit.master.sub_tool('Cutout'))
            self.page_edit.click_sub_tool('Cutout')


        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Remove Background')
    @allure.title('Apply')
    def test_cutout_remove_background(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout")

            assert self.page_edit.cutout.cutout_remove_background()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('No Effect')
    @allure.title('Apply')
    def test_cutout_no_effect(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout")
                self.page_edit.cutout.cutout_remove_background()

            assert self.page_edit.cutout.cutout_no_effect()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Default Image')
    def test_cutout_image_default_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout")

            assert self.page_edit.cutout.cutout_image_default_image()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('CL Image')
    def test_cutout_image_change_cl_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout")

            assert self.page_edit.cutout.cutout_image_change_cl_image(7)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('None')
    def test_cutout_image_none(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout")

            assert self.page_edit.cutout.cutout_image_none()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Custom Image')
    def test_cutout_custom_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout")

            assert self.page_edit.cutout.cutout_custom_image()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story('Change Background')
    @allure.title('Enter Text to Image')
    def test_cutout_text_to_image(self, data):
        try:
            if self.last_is_fail(data):
                self.page_edit.create_project_and_enter_function("Cutout")

            assert self.page_edit.cutout.cutout_enter_TTI()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise


@allure.story('Cutout_Remove_Background')
class Test_Master_Video_Cutout_Change_Background:
    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

    @allure.title('Cutout Default Selection')
    def test_cutout_default_selection(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            assert self.page_edit.cutout.start_with_cutout('master video')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_edit.cutout.start_with_cutout('master video')
            raise Exception

    @allure.title('Remove Background')
    def test_cutout_remove_background(self, driver):

        try:
            assert self.page_edit.cutout.cutout_remove_background()

        except Exception:
            self.page_edit.cutout.start_with_cutout('master video')
            raise Exception

    @allure.title('No Effect')
    def test_cutout_no_effect(self, driver):
        try:
            assert self.page_edit.cutout.cutout_no_effect()

        except Exception:
            self.page_edit.cutout.start_with_cutout('master video')
            raise Exception

@allure.epic('Timeline_PiP')
@allure.feature('Video')
@allure.story('Cutout_Change Background')
class Test_PiP_Video_Cutout_Change_Background_:
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

    @allure.title('Image_Default Image')
    def test_image_default_image(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.cutout.start_with_cutout('master video')
            assert self.page_edit.cutout.cutout_image_default_image()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline(skip_media=False)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.click(L.import_media.media_library.apply)
            self.click(L.edit.timeline.master_clip)
            self.page_edit.click_sub_tool('Cutout')
            raise Exception

    @allure.title('Image_Enter Change Background')
    def test_enter_change_background(self, driver):
        try:
            assert self.is_exist(L.edit.sub_tool.cutout.image)
            assert self.is_exist(L.edit.sub_tool.cutout.animated)
            assert self.is_exist(L.edit.sub_tool.cutout.color)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Image_Change to another CL image')
    def test_change_cl_image(self, driver):
        try:
            assert self.page_edit.cutout.cutout_image_change_cl_image(7)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Image_None Background')
    def test_none_background(self, driver):
        try:
            assert self.page_edit.cutout.cutout_image_none()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Image_Custom Image')
    def test_custom_image(self, driver):
        try:
            assert self.page_edit.cutout.cutout_custom_image()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    '''
    @allure.title('Text to Image')
    def test_text_to_image(self, driver):
        try:
            pic_base = self.page_edit.get_preview_pic()
            self.elements(L.edit.sub_tool.cutout.item)[2].click()
            self.element(L.main.shortcut.tti.editor_choice).click()
            self.click(L.main.shortcut.tti.generate)
            pic_after = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.cutout.color_picker.apply)
            assert not HCompareImg(pic_base, pic_after).histogram_compare(1)
            assert self.is_exist(L.edit.sub_tool.cutout.color_picker.picker_btn)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception
    '''

    @allure.title('Animated_Background')
    def test_animated_background(self, driver):
        try:
            assert self.page_edit.cutout.cutout_animated_background()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Animated_None')
    def test_animated_none(self, driver):
        try:
            assert self.page_edit.cutout.cutout_animated_none()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Background')
    def test_color_background(self, driver):
        try:
            assert self.page_edit.cutout.cutout_color_background()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_None')
    def test_color_background_none(self, driver):
        try:
            assert self.page_edit.cutout.cutout_color_none()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_ Color Picker_Dropper')
    def test_color_picker_dropper(self, driver):
        try:
            assert self.page_edit.color_picker.color_picker_dropper()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Color Picker_Color Map')
    def test_color_picker_color_map(self, driver):
        try:
            assert self.page_edit.color_picker.color_picker_color_map()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Color Picker_Slider')
    def test_color_picker_slider(self, driver):
        try:
            assert self.page_edit.color_picker.color_picker_slider()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Color Picker_Red Text')
    def test_color_picker_red_text(self, driver):
        try:
            assert self.page_edit.color_picker.color_picker_rgb_text('red')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Color Picker_Green Text')
    def test_color_picker_green_text(self, driver):
        try:
            assert self.page_edit.color_picker.color_picker_rgb_text('green')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Color Picker_Blue Text')
    def test_color_picker_blue_text(self, driver):
        try:
            assert self.page_edit.color_picker.color_picker_rgb_text('blue')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Color Picker_Apply')
    def test_color_picker_apply(self, driver):
        try:
            assert self.page_edit.color_picker.color_picker_apply()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Color_Color Picker_Cancel')
    def test_color_picker_cancel(self, driver):
        try:
            self.page_edit.color_picker.enter_color_picker()
            assert self.page_edit.color_picker.color_picker_cancel()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Change Background_Apply')
    def test_change_background_apply(self, driver):
        try:
            assert self.page_edit.cutout.cutout_change_background_apply()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception

    @allure.title('Change Background_Cancel')
    def test_change_background_cancel(self, driver):
        try:
            assert self.page_edit.cutout.cutout_change_background_cancel()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_video)
            self.page_media.select_local_video(test_folder, 'mkv.mkv')
            self.page_edit.click_sub_tool('Cutout')
            self.element(L.edit.sub_tool.cutout.chroma_key).click()
            raise Exception