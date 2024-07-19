import pytest
import allure
from random import randint

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

original_preview = None


@pytest.fixture(scope='class')
def module_setup(shortcut, driver, driver_init):
    global original_preview
    page_main, page_edit, page_media, _ = shortcut

    page_main.enter_launcher()
    page_main.subscribe()

    click = page_main.h_click
    click(L.main.new_project)
    page_media.switch_to_photo_library()
    click(L.import_media.media_library.media(index=1))
    click(L.import_media.media_library.apply)

    original_preview = page_edit.get_preview_pic()
    click(T.id('item_view_bg'))
    page_edit.click_sub_tool('Adjustment')
    yield
    page_edit.back_to_launcher()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_AI Color')
class TestMasterPhotoAdjustment_AIColor:

    MIN = '0'
    DEFAULT = '50'
    MAX = '100'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('AI Color')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(100)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_Brightness')
class TestMasterPhotoAdjustment_Brightness:

    MIN = '-100'
    DEFAULT = '0'
    MAX = '100'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_Contrast')
class TestMasterPhotoAdjustment_Contrast:

    MIN = '-100'
    DEFAULT = '0'
    MAX = '100'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('Contrast')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(1)
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_Saturation')
class TestMasterPhotoAdjustment_Saturation:

    MIN = '0'
    DEFAULT = '100'
    MAX = '200'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('Saturation')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(1)
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_HSL')
class TestMasterPhotoAdjustment_HSL:

    MIN = '-50'
    DEFAULT = '0'
    MAX = '50'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut

        page_edit.select_adjustment_from_bottom_edit_menu('HSL')
        yield
        page_main.h_click(L.edit.master.ai_effect.back)

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Test color can be tap/selected')
    def test_color(self):
        self.click(T.id('view_pink'))
        assert self.element(T.id('view_pink')).get_attribute('selected') == 'true'
        self.click(T.id('view_red'))
        assert self.element(T.id('view_red')).get_attribute('selected') == 'true'
        self.click(T.id('view_orange'))
        assert self.element(T.id('view_orange')).get_attribute('selected') == 'true'
        self.click(T.id('view_yellow'))
        assert self.element(T.id('view_yellow')).get_attribute('selected') == 'true'
        self.click(T.id('view_green'))
        assert self.element(T.id('view_green')).get_attribute('selected') == 'true'
        self.click(T.id('view_blue_light'))
        assert self.element(T.id('view_blue_light')).get_attribute('selected') == 'true'
        self.click(T.id('view_blue'))
        assert self.element(T.id('view_blue')).get_attribute('selected') == 'true'
        self.click(T.id('view_purple'))
        assert self.element(T.id('view_purple')).get_attribute('selected') == 'true'

    @allure.title('Hue bar default value')
    def test_hue_default_value(self):
        assert self.element(L.main.shortcut.hsl.hue_value).text == self.DEFAULT

    @allure.title('Hue bar max value')
    def test_hue_max_value(self):
        self.element(L.main.shortcut.hsl.hue_slider).send_keys(999)
        assert self.element(L.main.shortcut.hsl.hue_value).text == self.MAX

    @allure.title('Hue bar min value')
    def test_hue_min_value(self):
        self.element(L.main.shortcut.hsl.hue_slider).send_keys(-999)
        assert self.element(L.main.shortcut.hsl.hue_value).text == self.MIN

    @allure.title('Saturation bar default value')
    def test_saturation_default_value(self):
        assert self.element(L.main.shortcut.hsl.saturation_value).text == self.DEFAULT

    @allure.title('Saturation max value')
    def test_saturation_max_value(self):
        self.element(L.main.shortcut.hsl.saturation_slider).send_keys(999)
        assert self.element(L.main.shortcut.hsl.saturation_value).text == self.MAX

    @allure.title('Saturation min value')
    def test_saturation_min_value(self):
        self.element(L.main.shortcut.hsl.saturation_slider).send_keys(-999)
        assert self.element(L.main.shortcut.hsl.saturation_value).text == self.MIN

    @allure.title('Lightness bar default value')
    def test_lightness_default_value(self):
        assert self.element(L.main.shortcut.hsl.luminance_value).text == self.DEFAULT

    @allure.title('Lightness max value')
    def test_lightness_max_value(self):
        self.element(L.main.shortcut.hsl.luminance_slider).send_keys(999)
        assert self.element(L.main.shortcut.hsl.luminance_value).text == self.MAX

    @allure.title('Lightness min value')
    def test_lightness_min_value(self):
        self.element(L.main.shortcut.hsl.luminance_slider).send_keys(-999)
        assert self.element(L.main.shortcut.hsl.luminance_value).text == self.MIN

    @allure.title('Reset button')
    def test_reset(self):
        self.click(L.edit.sub_tool.reset)
        assert self.element(L.main.shortcut.hsl.hue_value).text == self.DEFAULT
        assert self.element(L.main.shortcut.hsl.saturation_value).text == self.DEFAULT
        assert self.element(L.main.shortcut.hsl.luminance_value).text == self.DEFAULT


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_Hue')
class TestMasterPhotoAdjustment_Hue:

    MIN = '0'
    DEFAULT = '100'
    MAX = '200'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('Hue')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(1)
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_Temp')
class TestMasterPhotoAdjustment_Temp:

    MIN = '0'
    DEFAULT = '50'
    MAX = '100'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('Temp')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(1)
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT


    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_Tint')
class TestMasterPhotoAdjustment_Tint:

    MIN = '0'
    DEFAULT = '50'
    MAX = '100'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('Tint')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(1)
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()


@allure.epic('Timeline_Master')
@allure.feature('Photo')
@allure.story('Adjustment_Sharpness')
class TestMasterPhotoAdjustment_Sharpness:

    MIN = '0'
    DEFAULT = '0'
    MAX = '200'

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver, module_setup):
        page_main, page_edit, *_ = shortcut
        page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element

        self.original_preview = original_preview
        yield

    @allure.title('Slider default value')
    def test_default_slider(self):
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Slider max value')
    def test_max_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(1)
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MAX

    @allure.title('Slider min value')
    def test_min_slider(self):
        self.element(L.edit.sub_tool.slider).send_keys(-9999)
        assert self.element(L.edit.sub_tool.slider_value).text == self.MIN

    @allure.title('Can set value')
    def test_random_slider(self):
        assert self.element(L.edit.sub_tool.slider).send_keys(randint(0, 100))

    @allure.title('Tapping reset button can reset all option')
    def test_reset_button(self):
        self.click(L.edit.speed.reset)
        assert self.element(L.edit.sub_tool.slider_value).text == self.DEFAULT

    @allure.title('Will change preview when set')
    def test_change_preview(self):
        global original_preview
        self.element(L.edit.sub_tool.slider).send_keys(1)
        self.element(L.edit.sub_tool.slider).send_keys(9999)
        assert not CompareImage(self.original_preview,
                                self.page_edit.get_preview_pic(),
                                7).compare_image()
