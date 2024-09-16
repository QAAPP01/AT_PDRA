import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


@allure.epic("Shortcut - Text to Image")
class Test_Shortcut_Text_to_Image:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut, driver):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

        self.driver = driver

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

    @allure.feature("Entry")
    @allure.story("Enter")
    @allure.title("Enter from Shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            assert self.page_shortcut.enter_shortcut('Text to Image')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Back")
    @allure.title("Back to Shortcut")
    def test_back_to_shortcut(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Text to Image')

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Prompt")
    @allure.title("Done")
    def test_prompt_done(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.tti_enter_prompt()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Prompt")
    @allure.title("Over limit")
    def test_prompt_over_limit(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.tti_enter_prompt()

            assert self.is_exist(L.main.shortcut.tti.exceed_hint)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Prompt")
    @allure.title("Block generate over limit")
    def test_block_generate_over_limit(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.tti_enter_prompt()

            assert self.element(L.main.shortcut.tti.generate).get_attribute("enabled") == "false"

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Prompt")
    @allure.title("Sensitive prompt")
    def test_sensitive_prompt(self, data):
        try:
            if self.last_is_fail(data):
                pass

            self.page_shortcut.tti_enter_prompt('sexy')

            if not self.is_exist(L.main.shortcut.tti.sensitive):
                self.click(L.main.shortcut.tti.generate)

            assert self.is_exist(L.main.shortcut.tti.sensitive)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Prompt")
    @allure.title("Block generate sensitive prompt")
    def test_block_generate_sensitive_prompt(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.tti_enter_prompt('sexy')

            assert self.element(L.main.shortcut.tti.generate).get_attribute("enabled") == "false"

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Prompt")
    @allure.title("Clear")
    def test_clear_prompt(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.tti_enter_prompt()

            assert self.page_shortcut.tti_clear_prompt()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Prompt")
    @allure.title("Recommend prompt")
    def test_recommend_prompt(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.tti_enter_prompt()
                
            data['prompt'] = self.page_shortcut.tti_recommend_prompt()

            assert data['prompt']

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Style")
    @allure.title("Default")
    def test_default_style(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Text to Image')

            select = self.element(L.main.shortcut.tti.selected_style).text

            assert select == "None"

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Style")
    @allure.title("Change style")
    def test_change_style(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Text to Image')

            self.click(L.main.shortcut.tti.style(2))
            time.sleep(0.5)
            select = self.element(L.main.shortcut.tti.selected_style).text

            assert select != "None"

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Style")
    @allure.title("Change category")
    def test_change_category(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('Text to Image')

            select = self.element(L.main.shortcut.tti.selected_style)
            self.click(L.main.shortcut.tti.style_scenery)
            time.sleep(0.5)

            assert self.element(L.main.shortcut.tti.selected_style) != select

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Describe")
    @allure.story("Editor Choice")
    @allure.title("Overwrite cancel")
    def test_overwrite_cancel(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.tti_enter_prompt()

            self.driver.click_element_top_center(L.main.shortcut.tti.preset())
            self.click(L.main.shortcut.tti.overwrite_cancel)

            assert self.element(L.main.shortcut.tti.prompt).text == data['prompt']

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise
        
    def sce_6_13_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.main.shortcut.tti.overwrite_ok)
            prompt = self.element(L.main.shortcut.tti.prompt).text

            if prompt != data['prompt']:
                

                data['prompt'] = prompt

                return "PASS"
            else:
                raise Exception('[Fail] Prompt is incorrect')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.main.shortcut.tti.overwrite_ok)
            data['prompt'] = self.element(L.main.shortcut.tti.prompt).text

            return "FAIL"

    def sce_6_13_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tti.generate)

            if self.is_exist(L.main.shortcut.tti.remove_watermark):
                
                return "PASS"
            else:
                raise Exception('[Fail] No found remove watermark')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
