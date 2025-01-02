import traceback
import inspect
import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L

from .conftest import TEST_MATERIAL_FOLDER as test_material_folder
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


@allure.epic("Server Scan")
@allure.feature("Filter")
class Test_Scan_Filter:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.story("Download")
    def test_filter_download(self, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            before = self.page_edit.get_preview_pic()
            self.page_edit.click_tool("Filter")
            self.click(L.edit.filter.filter())
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting_download()
            after = self.page_edit.get_preview_pic()

            assert not HCompareImg(before, after).ssim_compare()

        except Exception:
            traceback.print_exc()
            driver.driver.close_app()

            assert Exception