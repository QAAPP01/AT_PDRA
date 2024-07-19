import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T
from random import randint


def replace_video(shortcut):
    main, edit, *_ = shortcut
    click = main.h_click

    click(T.id('item_view_bg'))
    edit.click_sub_tool('Replace')
    click(L.import_media.media_library.media(index=2))

    click(L.edit.replace.ok_btn, timeout=1)
    click(L.edit.replace.btn_replace_anyway, timeout=1)
    click(L.import_media.media_library.dialog_ok, timeout=1)


@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Replace')
class TestMasterReplaceVideoAfterApply:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut

        page_main.enter_launcher()
        page_main.subscribe()
        page_main.enter_timeline()
        yield
        page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.replace_video = replace_video

        self.click(L.edit.preview.import_tips_icon)
        self.click(L.import_media.media_library.media(index=1))
        self.click(L.import_media.media_library.apply)
        self.click(T.id('item_view_bg'))
        yield
        self.click(L.edit.menu.delete)

    @allure.title('Replace after setting volume')
    def test_replace_video_adjusted_volume(self, driver, shortcut):
        self.page_edit.click_sub_tool('Volume')
        self.element(L.edit.speed.slider).send_keys(randint(1, 200))
        self.click(L.edit.speed.ease_in)
        self.click(L.edit.speed.ease_out)
        self.click(L.edit.sub_tool.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Volume')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Volume')

    @allure.title('Replace after setting audio tool')
    def test_replace_video_adjusted_audio_tool(self, driver, shortcut):
        self.page_edit.click_sub_tool('AI Audio \nTool')
        self.click(L.edit.ai_audio_tool.ai_voice_changer)
        self.click(T.id('iv_voice_name'))
        self.click(L.edit.ai_audio_tool.apply)
        self.click(L.edit.ai_audio_tool.ok)
        self.click(L.edit.sub_tool.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('AI Audio \nTool')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('AI Audio \nTool')

    @allure.title('Replace after setting filter')
    def test_replace_video_adjusted_filter(self, driver, shortcut):
        self.page_edit.click_sub_tool('Filter')
        self.page_edit.click_effect('A06', L.edit.master.ai_effect.effect())
        self.click(L.edit.ai_audio_tool.apply)
        self.click(L.edit.ai_audio_tool.ok)
        self.click(L.edit.sub_tool.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Filter')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Filter')

    @allure.title('Replace after setting adjustment')
    def test_replace_video_adjusted_adjustment(self, driver, shortcut):
        self.page_edit.click_sub_tool('Adjustment')
        self.click(L.edit.adjust_sub)
        self.click(T.find_string('Brightness'))
        self.element(L.edit.speed.slider).send_keys(randint(1, 200))
        self.click(L.edit.sub_tool.back)
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Adjustment')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Adjustment')

    @allure.title('Replace after setting speed')
    def test_replace_video_adjusted_speed(self, driver, shortcut):
        self.page_edit.click_sub_tool('Speed')
        self.element(L.edit.speed.slider).send_keys(randint(1, 100))
        self.click(L.edit.sub_tool.back)
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Speed')
        assert not self.page_edit.check_bottom_edit_menu_item_apply_status('Speed')

    @allure.title('Replace after setting effect')
    def test_replace_video_adjusted_effect(self, driver, shortcut):
        self.page_edit.click_sub_tool('Effect')
        self.page_edit.click_effect('Beating', L.edit.master.effect.effect())
        self.click(L.edit.ai_audio_tool.ok)

        self.replace_video(shortcut)

        self.page_edit.click_sub_tool('Effect')
        self.click(L.edit.sub_tool.filter.cancel)
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Effect')

    @allure.title('Replace after setting stabilizer')
    def test_replace_video_adjusted_stabilizer(self, driver, shortcut):
        self.page_edit.click_sub_tool('Stabilizer')
        self.element(L.edit.speed.slider).send_keys(randint(1, 100))
        self.click(L.edit.sub_tool.back)
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Stabilizer')
        assert not self.page_edit.check_bottom_edit_menu_item_apply_status('Stabilizer')

    @allure.title('Replace after setting smoothener')
    def test_replace_video_adjusted_skin_smoothener(self, driver, shortcut):
        self.page_edit.click_sub_tool('Skin Smoothener')
        self.click(T.find_string('Brightness'))
        self.element(L.edit.speed.slider).send_keys(randint(40, 100))
        self.click(T.find_string('Smoothness'))
        self.element(L.edit.speed.slider).send_keys(randint(0, 100))
        self.click(L.edit.sub_tool.back)
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Skin Smoothener')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Skin Smoothener')

    @allure.title('Replace after setting fit and fill')
    def test_replace_video_adjusted_skin_fit_fill(self, driver, shortcut):
        self.page_edit.click_sub_tool('Fit & Fill')
        self.click(L.edit.fit_and_fill.btn_fill)
        self.click(L.edit.sub_tool.back)
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Fit & Fill')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Fit & Fill')

    @allure.title('Replace after setting pan and zoom')
    def test_replace_video_adjusted_pan_zoom(self, driver, shortcut):
        self.page_edit.click_sub_tool('Pan & Zoom')
        self.click(T.find_string('Custom'))
        self.page_edit.h_swipe_element_to_location(T.id('resizable_master_view'), 100)
        self.click(L.edit.sub_tool.apply)
        self.click(L.edit.sub_tool.back)
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Pan & Zoom')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Pan & Zoom')

    @allure.title('Replace after setting crop')
    def test_replace_video_adjusted_crop(self, driver, shortcut):
        self.page_edit.click_sub_tool('Crop')
        self.click(L.edit.crop.btn_16_9)
        self.click(L.edit.crop.apply)
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Crop')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Crop')

    @allure.title('Replace after setting rotate')
    def test_replace_video_adjusted_rotate(self, driver, shortcut):
        self.page_edit.click_sub_tool('Rotate')
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Rotate')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Rotate')

    @allure.title('Replace after setting flip')
    def test_replace_video_adjusted_flip(self, driver, shortcut):
        self.page_edit.click_sub_tool('Flip')
        self.click(L.edit.toolbar.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Flip')
        assert self.page_edit.check_bottom_edit_menu_item_apply_status('Flip')

    @allure.title('Replace after setting reverse')
    def test_replace_video_adjusted_reverse(self, driver, shortcut):
        self.page_edit.click_sub_tool('Reverse')
        self.click(L.edit.reverse.dialog_ok)
        self.page_main.is_not_in_page([L.edit.reverse.ad, L.edit.reverse.ad_promotion], 3 * 60)
        self.click(L.edit.sub_tool.back)

        self.replace_video(shortcut)

        self.page_edit.is_sub_tool_exist('Reverse')
        assert not self.page_edit.check_bottom_edit_menu_item_apply_status('Reverse')
