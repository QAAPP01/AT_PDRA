import traceback
import inspect

import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg, CompareImage
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


from .conftest import TEST_MATERIAL_FOLDER, driver

test_material_folder = TEST_MATERIAL_FOLDER



@allure.epic('Timeline_PiP_Photo')
@allure.feature('Adjust')
class Test_PiP_Photo_Adjustment:
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

    @allure.story('AI Color')
    @allure.title('Open adjustment options')
    def test_open_Adjustment_panel(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            assert self.is_exist(L.edit.edit_sub.option_list)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            raise Exception

    @allure.story('AI Color')
    @allure.title('Default Value')
    def test_AI_Color_default_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.select_adjustment_from_bottom_edit_menu('AI Color')
            assert self.element(L.edit.sub_tool.slider_value).text == '50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('AI Color')
            raise Exception

    @allure.story('AI Color')
    @allure.title('Maximum')
    def test_AI_Color_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(100)
            assert self.element(L.edit.sub_tool.slider_value).text == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('AI Color')
            raise Exception

    @allure.story('AI Color')
    @allure.title('Minimum')
    def test_AI_Color_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(1)
            self.element(L.edit.sub_tool.slider).send_keys(0)
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('AI Color')
            raise Exception

    @allure.story('AI Color')
    @allure.title('Preview_Change')
    def test_AI_Color_preview_change(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            pic_base = self.page_edit.get_preview_pic()
            self.element(L.edit.sub_tool.slider).send_keys(43)
            pic_after = self.page_edit.get_preview_pic()
            assert not CompareImage(pic_base, pic_after, 7).compare_image()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('AI Color')
            raise Exception

    @allure.story('AI Color')
    @allure.title('Reset')
    def test_AI_Color_reset(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.timeline.reset)
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            raise Exception

    @allure.story('Brightness')
    @allure.title('Default Value')
    def test_brightness_default_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
            raise Exception

    @allure.story('Brightness')
    @allure.title('Maximum')
    def test_brightness_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(200)
            assert self.element(L.edit.sub_tool.slider_value).text == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
            raise Exception

    @allure.story('Brightness')
    @allure.title('Minimum')
    def test_brightness_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(1)
            self.element(L.edit.sub_tool.slider).send_keys(0)
            assert self.element(L.edit.sub_tool.slider_value).text == '-100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
            raise Exception

    @allure.story('Brightness')
    @allure.title('Preview_Change')
    def test_brightness_preview_change(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            pic_base = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
            self.element(L.edit.sub_tool.slider).send_keys(20, 100)
            pic_after = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
            assert not HCompareImg(pic_base, pic_after).histogram_compare(1)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
            raise Exception

    @allure.story('Brightness')
    @allure.title('Reset')
    def test_brightness_reset(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.timeline.reset)
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            raise Exception

    @allure.story('Contrast')
    @allure.title('Default Value')
    def test_contrast_default_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.select_adjustment_from_bottom_edit_menu('Contrast')
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Contrast')
            raise Exception

    @allure.story('Contrast')
    @allure.title('Maximum')
    def test_contrast_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(199)
            self.element(L.edit.sub_tool.slider).send_keys(200)
            assert self.element(L.edit.sub_tool.slider_value).text == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Contrast')
            raise Exception

    @allure.story('Contrast')
    @allure.title('Minimum')
    def test_contrast_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(1)
            self.element(L.edit.sub_tool.slider).send_keys(0)
            assert self.element(L.edit.sub_tool.slider_value).text == '-100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Contrast')
            raise Exception

    @allure.story('Contrast')
    @allure.title('Preview_Change')
    def test_contrast_preview_change(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            pic_base = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
            self.element(L.edit.sub_tool.slider).send_keys(20, 100)
            pic_after = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
            assert not HCompareImg(pic_base, pic_after).histogram_compare(1)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Contrast')
            raise Exception

    @allure.story('Contrast')
    @allure.title('Reset')
    def test_contrast_reset(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.timeline.reset)
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            raise Exception

    @allure.story('Saturation')
    @allure.title('Default Value')
    def test_saturation_default_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.select_adjustment_from_bottom_edit_menu('Saturation')
            assert self.element(L.edit.sub_tool.slider_value).text == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Saturation')
            raise Exception

    @allure.story('Saturation')
    @allure.title('Maximum')
    def test_saturation_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(199)
            self.element(L.edit.sub_tool.slider).send_keys(200)
            assert self.element(L.edit.sub_tool.slider_value).text == '200'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Saturation')
            raise Exception

    @allure.story('Saturation')
    @allure.title('Minimum')
    def test_saturation_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(1)
            self.element(L.edit.sub_tool.slider).send_keys(0)
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Saturation')
            raise Exception

    @allure.story('Saturation')
    @allure.title('Preview_Change')
    def test_saturation_preview_change(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            pic_base = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
            self.element(L.edit.sub_tool.slider).send_keys(20, 100)
            pic_after = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
            assert not HCompareImg(pic_base, pic_after).histogram_compare(1)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Saturation')
            raise Exception

    @allure.story('Saturation')
    @allure.title('Reset')
    def test_saturation_reset(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.timeline.reset)
            assert self.element(L.edit.sub_tool.slider_value).text == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_can_be_tap/selected')
    def test_green_can_be_tap(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            self.click(L.edit.adjustment.view_green)
            assert self.element(L.edit.adjustment.view_green).get_attribute('selected') == 'true'


        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Hue_Default_Value')
    def test_hsl_green_hue_default_value(self):
        try:
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            assert self.element(L.main.shortcut.hsl.hue_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Hue_Maximum')
    def test_hsl_green_hue_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.main.shortcut.hsl.hue_slider).send_keys(100)
            assert self.element(L.main.shortcut.hsl.hue_value).text == '50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Hue_Minimum')
    def test_hsl_green_hue_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.main.shortcut.hsl.hue_slider).send_keys(1)
            self.element(L.main.shortcut.hsl.hue_slider).send_keys(0)
            assert self.element(L.main.shortcut.hsl.hue_value).text == '-50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Saturation_Default_Value')
    def test_hsl_green_saturation_default_value(self):
        try:
            assert self.element(L.main.shortcut.hsl.saturation_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Saturation_Maximum')
    def test_hsl_green_saturation_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.main.shortcut.hsl.saturation_slider).send_keys(100)
            assert self.element(L.main.shortcut.hsl.saturation_value).text == '50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Saturation_Minimum')
    def test_hsl_green_saturation_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.main.shortcut.hsl.saturation_slider).send_keys(1)
            self.element(L.main.shortcut.hsl.saturation_slider).send_keys(0)
            assert self.element(L.main.shortcut.hsl.saturation_value).text == '-50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Lightness_Default_Value')
    def test_hsl_green_luminance_default_value(self):
        try:
            assert self.element(L.main.shortcut.hsl.luminance_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Luminance_Maximum')
    def test_hsl_green_luminance_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.main.shortcut.hsl.luminance_slider).send_keys(100)
            assert self.element(L.main.shortcut.hsl.luminance_value).text == '50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Green_Luminance_Minimum')
    def test_hsl_green_luminance_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.main.shortcut.hsl.luminance_slider).send_keys(1)
            self.element(L.main.shortcut.hsl.luminance_slider).send_keys(0)
            assert self.element(L.main.shortcut.hsl.luminance_value).text == '-50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('HSL')
            raise Exception

    @allure.story('HSL')
    @allure.title('Reset')
    def test_hsl_green_reset(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.timeline.reset)
            assert self.element(L.main.shortcut.hsl.hue_value).text == '0'
            assert self.element(L.main.shortcut.hsl.saturation_value).text == '0'
            assert self.element(L.main.shortcut.hsl.luminance_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            raise Exception

    # @allure.story('Hue')
    # @allure.title('Default Value')
    # def test_hue_default_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.click(L.edit.master.effect.back)
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Hue')
    #         assert self.element(L.edit.sub_tool.slider_value).text == '100'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Hue')
    #         raise Exception
    #
    # @allure.story('Hue')
    # @allure.title('Maximum')
    # def test_hue_maximum_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.element(L.edit.sub_tool.slider).send_keys(199)
    #         self.element(L.edit.sub_tool.slider).send_keys(200)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '200'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Hue')
    #         raise Exception
    #
    # @allure.story('Hue')
    # @allure.title('Minimum')
    # def test_hue_minimum_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.element(L.edit.sub_tool.slider).send_keys(1)
    #         self.element(L.edit.sub_tool.slider).send_keys(0)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '0'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Hue')
    #         raise Exception
    #
    # @allure.story('Hue')
    # @allure.title('Preview_Change')
    # def test_hue_preview_change(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         pic_base = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
    #         self.element(L.edit.sub_tool.slider).send_keys(145)
    #         pic_after = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
    #         assert not HCompareImg(pic_base, pic_after).histogram_compare(1)
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Hue')
    #         raise Exception
    #
    # @allure.story('Hue')
    # @allure.title('Reset')
    # def test_hue_reset(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.click(L.edit.timeline.reset)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '100'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         raise Exception

    # @allure.story('Temp')
    # @allure.title('Default Value')
    # def test_temp_default_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Temp')
    #         assert self.element(L.edit.sub_tool.slider_value).text == '50'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Temp')
    #         raise Exception
    #
    # @allure.story('Temp')
    # @allure.title('Maximum')
    # def test_temp_maximum_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.element(L.edit.sub_tool.slider).send_keys(99)
    #         self.element(L.edit.sub_tool.slider).send_keys(100)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '100'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Temp')
    #         raise Exception
    #
    # @allure.story('Temp')
    # @allure.title('Minimum')
    # def test_temp_minimum_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.element(L.edit.sub_tool.slider).send_keys(1)
    #         self.element(L.edit.sub_tool.slider).send_keys(0)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '0'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Temp')
    #         raise Exception
    #
    # @allure.story('Temp')
    # @allure.title('Preview_Change')
    # def test_temp_preview_change(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         pic_base = self.page_edit.get_preview_pic()
    #         self.element(L.edit.sub_tool.slider).send_keys(76)
    #         pic_after = self.page_edit.get_preview_pic()
    #         assert not CompareImage(pic_base, pic_after, 7).compare_image()
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Temp')
    #         raise Exception
    #
    # @allure.story('Temp')
    # @allure.title('Reset')
    # def test_temp_reset(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.click(L.edit.timeline.reset)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '50'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         raise Exception

    @allure.story('Tint')
    @allure.title('Default Value')
    def test_tint_default_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_edit.select_adjustment_from_bottom_edit_menu('Tint')
            assert self.element(L.edit.sub_tool.slider_value).text == '50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Tint')
            raise Exception

    @allure.story('Tint')
    @allure.title('Maximum')
    def test_tint_maximum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(99)
            self.element(L.edit.sub_tool.slider).send_keys(100)
            assert self.element(L.edit.sub_tool.slider_value).text == '100'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Tint')
            raise Exception

    @allure.story('Tint')
    @allure.title('Minimum')
    def test_tint_minimum_value(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.element(L.edit.sub_tool.slider).send_keys(1)
            self.element(L.edit.sub_tool.slider).send_keys(0)
            assert self.element(L.edit.sub_tool.slider_value).text == '0'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Tint')
            raise Exception

    @allure.story('Tint')
    @allure.title('Preview_Change')
    def test_tint_preview_change(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            pic_base = self.page_edit.get_preview_pic()
            self.element(L.edit.sub_tool.slider).send_keys(55)
            pic_after = self.page_edit.get_preview_pic()
            assert not CompareImage(pic_base, pic_after, 7).compare_image()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            self.page_edit.select_adjustment_from_bottom_edit_menu('Tint')
            raise Exception

    @allure.story('Tint')
    @allure.title('Reset')
    def test_tint_reset(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.click(L.edit.timeline.reset)
            assert self.element(L.edit.sub_tool.slider_value).text == '50'

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Overlay')
            self.click(L.import_media.menu.overlay_photo)
            self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
            self.page_edit.click_sub_tool('Adjust')
            raise Exception

    # @allure.story('Sharpness')
    # @allure.title('Default Value')
    # def test_sharpness_default_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
    #         assert self.element(L.edit.sub_tool.slider_value).text == '0'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
    #         raise Exception
    #
    # @allure.story('Sharpness')
    # @allure.title('Maximum')
    # def test_sharpness_maximum_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.element(L.edit.sub_tool.slider).send_keys(199)
    #         self.element(L.edit.sub_tool.slider).send_keys(200)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '200'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
    #         raise Exception
    #
    # @allure.story('Sharpness')
    # @allure.title('Minimum')
    # def test_sharpness_minimum_value(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.element(L.edit.sub_tool.slider).send_keys(1)
    #         self.element(L.edit.sub_tool.slider).send_keys(0)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '0'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
    #         raise Exception
    #
    # @allure.story('Sharpness')
    # @allure.title('Preview_Change')
    # def test_tint_preview_change(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         pic_base = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
    #         self.element(L.edit.sub_tool.slider).send_keys(20, 100)
    #         pic_after = self.page_edit.get_preview_pic(L.edit.pip_library.pip_object)
    #         assert not HCompareImg(pic_base, pic_after).histogram_compare(1)
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         self.page_edit.select_adjustment_from_bottom_edit_menu('Tint')
    #         raise Exception
    #
    # @allure.story('Sharpness')
    # @allure.title('Reset')
    # def test_sharpness_reset(self, driver):
    #     func_name = inspect.stack()[0][3]
    #     logger(f"\n[Start] {func_name}")
    #
    #     try:
    #         self.click(L.edit.timeline.reset)
    #         assert self.element(L.edit.sub_tool.slider_value).text == '0'
    #
    #     except Exception:
    #         traceback.print_exc()
    #         driver.driver.close_app()
    #         driver.driver.launch_app()
    #
    #         self.page_main.enter_launcher()
    #         self.page_main.enter_timeline()
    #         self.page_edit.enter_main_tool('Overlay')
    #         self.click(L.import_media.menu.overlay_photo)
    #         self.page_media.select_local_photo(test_material_folder, 'jpg.jpg')
    #         self.page_edit.click_sub_tool('Adjust')
    #         raise Exception
