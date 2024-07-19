import time
import pytest
import allure
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *
from ATFramework_aPDR.ATFramework.utils.log import logger


@allure.epic("App initial")
class TestInit:
    @pytest.fixture(scope='module', autouse=True)
    def driver_init(self, driver):
        logger("==== Start driver session ====")
        driver.driver.reset()
        time.sleep(1)
        driver.driver.launch_app()
        yield
        driver.driver.close_app()

    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.feature("Expand pip track")
    def expand_pip_track(self):
        self.page_main.h_click(L.edit.menu.settings)
        self.page_main.h_click(find_string('Expand Track Height'), 2)

    @allure.feature("Close overlay tip")
    def close_overlay_tip(self):
        self.page_edit.add_pip_media('photo')
        self.click(id('iv_hint'))

    def test_app_init(self, driver):
        for retry in range(3):
            try:
                page_main = PageFactory().get_page_object("main_page", driver)
                page_edit = PageFactory().get_page_object("edit", driver)
                click = page_main.h_click
                page_main.enter_launcher()
                page_main.h_click(L.main.project.new_project, 2)
                page_main.h_click(L.main.permission.file_ok)
                page_main.h_click(L.main.permission.photo_allow)
                page_main.click(('id', 'top_toolbar_back'))
                page_main.click(('id', 'set_default'))
                page_main.click(('id', 'tv_continue'))
                page_main.h_click(("id", "tv_hint"), 2)

                self.expand_pip_track()
                self.close_overlay_tip()

                if not page_main.h_click(L.edit.preview.import_tips_icon, timeout=1):
                    if not page_main.h_click(L.edit.timeline.main_track_import, timeout=1):
                        if not page_main.h_click(L.edit.timeline.main_track_import_float, timeout=1):
                            logger('[Warning] No import button')
                page_main.click(find_string('Photo'))
                page_main.h_click(("xpath", '(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[1]'))
                page_main.h_click(("xpath", '(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[2]'))
                page_main.h_click(L.import_media.media_library.apply)

                self.page_edit.preference.trigger_fileName(enable=True)

                page_main.h_click(('id', 'transition_hint'))
                page_main.h_click(L.edit.menu.play)
                page_main.h_click(L.edit.preview.help_not_show_tip_again)
                driver.driver.back()

                page_main.h_click(L.edit.menu.home)
                # Churn Recovery
                if page_main.h_is_exist(L.main.premium.pdr_premium, 1):
                    driver.driver.back()
                page_main.h_click(L.main.project.entry)
                page_main.h_long_press(L.main.project.project_name())
                page_main.h_click(find_string("Delete"))
                page_main.h_click(L.main.project.dialog_ok)
                logger("\n[Done] app_initial")
                return True

            except Exception as err:
                logger(f'[Error] {err}')
                driver.driver.close_app()
                driver.driver.launch_app()

        pytest.fail(f'App initial error')