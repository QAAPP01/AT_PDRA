import pytest
import allure

import ATFramework_aPDR.pages.locator.locator as L
import ATFramework_aPDR.pages.locator.locator_type as T


@allure.epic('Timeline_Master')
@allure.feature('Video')
@allure.story('Cutout')
class TestMasterVideoCutout:

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, shortcut, driver):
        page_main, page_edit, *_ = shortcut
        click = page_main.h_click

        with allure.step('[Step] Enter launcher'):
            page_main.enter_launcher()
        with allure.step('[Step] New timeline with video'):
            click(L.main.new_project)
            click(L.import_media.media_library.media(index=1))
            click(L.import_media.media_library.apply)

        with allure.step('[Step] Enter Cutout function'):
            click(T.id('item_view_bg'))
            page_edit.click_sub_tool('Cutout')
        yield
        with allure.step('[Step] Back to launcher'):
            page_edit.back_to_launcher()

    @pytest.fixture(autouse=True)
    def function_setup_teardown(self, shortcut, driver):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements

        self.click = self.page_main.h_click
        self.drag = self.page_main.h_drag_element
        yield
