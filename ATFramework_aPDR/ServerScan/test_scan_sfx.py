import traceback
import inspect
import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


@allure.epic("Server Scan")
@allure.feature("SFX")
class Test_Scan_SFX:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.story("Meta")
    @allure.title("Download")
    def test_meta_sfx_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.enter_timeline()
            self.page_edit.enter_audio_library('SFX')
            self.page_media.click_sfx_tab('meta')

            music = self.elements(L.import_media.music_library.music(0))
            for i in music:
                i.click()
                if self.click(L.import_media.music_library.download, 2):
                    self.click(L.edit.try_before_buy.try_it_first, 1)
                    if self.is_exist(L.import_media.music_library.download_cancel, 1):
                        self.is_not_exist(L.import_media.music_library.download_cancel)
                    break

            assert self.is_exist(L.import_media.music_library.add)

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_audio_library('SFX')
            self.page_media.click_sfx_tab('meta')

            pytest.fail(f"{str(e)}")



    @allure.story("CL")
    @allure.title("Download")
    def test_cl_sfx_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_media.click_sfx_tab('cl')

            self.click(L.import_media.music_library.category(3))
            music = self.elements(L.import_media.music_library.music(0))
            for i in music:
                i.click()
                if self.click(L.import_media.music_library.download, 2):
                    self.click(L.edit.try_before_buy.try_it_first, 1)
                    if self.is_exist(L.import_media.music_library.download_cancel, 1):
                        self.is_not_exist(L.import_media.music_library.download_cancel)
                    break
            assert self.is_exist(L.import_media.music_library.add)

        except Exception:
            traceback.print_exc()

            pytest.fail(f"{str(e)}")

