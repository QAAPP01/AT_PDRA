import traceback
import inspect
import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


@allure.epic("Server Scan")
@allure.feature("Sticker")
class Test_Scan_Sticker:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.story("Download")
    def test_sticker_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_sticker_library('sticker')
            self.click(L.edit.sticker.sticker())
            self.page_edit.waiting_download()

            assert self.is_exist(L.edit.preview.pip_preview)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()

            raise Exception
