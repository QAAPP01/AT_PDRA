import time
import pytest
import allure
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.ATFramework.utils.log import logger


@allure.epic("App initial")
class TestInit:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.feature("New project")
    def new_project(self):
        self.click(L.main.project.new_project, 2)
        
    @allure.feature('Accept permission')
    def accept_permission(self):
        self.click(L.main.permission.file_ok, 2)
        self.click(L.main.permission.photo_allow, 2)
        self.click(('id', 'top_toolbar_back'))
    
    @allure.feature("Expand pip track")
    def expand_pip_track(self):
        self.click(L.edit.menu.settings)
        self.click(find_string('Expand Track Height'), 2)

    @allure.feature("Close overlay tip")
    def close_overlay_tip(self):
        self.page_edit.add_pip_media('photo')
        self.click(id('iv_hint'))

    def test_app_init(self, driver):
        for retry in range(3):
            try:
                self.new_project()
                self.accept_permission()
                # self.expand_pip_track()
                self.close_overlay_tip()

                if not self.click(L.edit.preview.import_tips_icon, timeout=1):
                    if not self.click(L.edit.timeline.main_track_import, timeout=1):
                        if not self.click(L.edit.timeline.main_track_import_float, timeout=1):
                            logger('[Warning] No import button')
                self.click(find_string('Photo'))
                self.click(("xpath", '(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[1]'))
                self.click(("xpath", '(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[2]'))
                self.click(L.import_media.media_library.apply)

                self.page_edit.preference.trigger_fileName(enable=True)

                self.click(('id', 'transition_hint'))
                self.click(L.edit.menu.play)
                self.click(L.edit.preview.help_not_show_tip_again)
                driver.driver.back()

                self.click(L.edit.menu.home)
                # Churn Recovery
                if self.is_exist(L.main.premium.pdr_premium, 1):
                    driver.driver.back()
                self.click(L.main.project.entry)
                self.long_press(L.main.project.project_name())
                self.click(find_string("Delete"))
                self.click(L.main.project.dialog_ok)
                logger("\n[Done] app_initial")
                return True

            except Exception as err:
                logger(f'[Error] {err}')
                driver.driver.close_app()
                driver.driver.launch_app()

        pytest.fail(f'App initial error')