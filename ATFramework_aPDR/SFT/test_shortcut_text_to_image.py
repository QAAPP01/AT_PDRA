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


@allure.epic("Shortcut")
@allure.feature("Text to Image")
class Test_Shortcut_Text_to_Image:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @pytest.fixture(scope="module")
    def shared_data(self):
        data = {}
        yield data

    @allure.story("Entry")
    @allure.title("Enter feature page")
    def test_entry_feature_page(self, driver):
        try:
            self.page_main.enter_launcher()

            self.page_main.enter_shortcut('Text to Image')
            time.sleep(1)

            assert self.element(L.main.shortcut.tti.title).text == 'Text to Image'

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')

            pytest.fail(f"{str(e)}")

    def sce_6_13_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.close)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_13_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            input_box = self.element(L.main.shortcut.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.main.shortcut.tti.done)

            if self.element(L.main.shortcut.tti.prompt).text == "x"*401:
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter prompt fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            input_box = self.element(L.main.shortcut.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.main.shortcut.tti.done)

            return "FAIL"

    def sce_6_13_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.is_exist(L.main.shortcut.tti.exceed_hint):
                
                return "PASS"
            else:
                raise Exception('[Fail] No found warning message')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            input_box = self.element(L.main.shortcut.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.main.shortcut.tti.done)

            return "FAIL"

    def sce_6_13_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.element(L.main.shortcut.tti.generate).get_attribute("enabled") == "false":
                
                return "PASS"
            else:
                raise Exception('[Fail] Generate button is not disabled')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            input_box = self.element(L.main.shortcut.tti.input_box)
            input_box.send_keys("x"*401)
            self.click(L.main.shortcut.tti.done)

            return "FAIL"

    def sce_6_13_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.element(L.main.shortcut.tti.prompt).click()
            input_box = self.element(L.main.shortcut.tti.input_box)
            input_box.send_keys('sexy')
            self.click(L.main.shortcut.tti.done)

            if not self.is_exist(L.main.shortcut.tti.sensitive):
                self.click(L.main.shortcut.tti.generate)
                time.sleep(1)

            if self.is_exist(L.main.shortcut.tti.sensitive):
                
                return "PASS"
            else:
                raise Exception('[Fail] No found warning message')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            input_box = self.element(L.main.shortcut.tti.input_box)
            input_box.send_keys('sexy')
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
    
    def sce_6_13_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.element(L.main.shortcut.tti.generate).get_attribute("enabled") == "false":
                
                return "PASS"
            else:
                raise Exception('[Fail] Generate button is not disabled')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            input_box = self.element(L.main.shortcut.tti.input_box)
            input_box.send_keys('sexy')
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
        
    def sce_6_13_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tti.prompt)
            self.click(L.main.shortcut.tti.clear)
            self.click(L.main.shortcut.tti.done)

            if self.element(L.main.shortcut.tti.prompt).text == "Type more than 10 words, describing the object, colors, composition, lighting, painting styles, etc.":
                
                return "PASS"
            else:
                raise Exception('[Fail] Prompt is not cleared')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()

            return "FAIL"
        
    def sce_6_13_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.input = self.element(L.main.shortcut.tti.input_box).text
            self.click(L.main.shortcut.tti.done)

            if self.element(L.main.shortcut.tti.prompt).text == self.input:
                
                return "PASS"
            else:
                raise Exception('[Fail] Prompt is incorrect')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.input = self.element(L.main.shortcut.tti.input_box).text
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
        
    def sce_6_13_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            select = self.element(xpath('//*[contains(@resource-id,"view_is_selected")]/../*[contains(@resource-id,"tv_name")]')).text

            if select == "None":
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Default incorrect: {select}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
        
    def sce_6_13_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(xpath('//*[contains(@resource-id,"card_view")]//*[contains(@resource-id,"iv_premium")]'))

            if self.click(L.main.subscribe.back_btn):
                
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP Back fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
        
    def sce_6_13_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(xpath('(//*[contains(@resource-id,"card_view") and not(.//*[contains(@resource-id,"iv_premium")])])[2]'))
            time.sleep(0.5)
            select = self.element(xpath('//*[contains(@resource-id,"view_is_selected")]/../*[contains(@resource-id,"tv_name")]')).text

            if select != "None":
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Select stlye fail: {select}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
        
    def sce_6_13_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(xpath('//*[contains(@resource-id,"cv_sticker")]/*[contains(@resource-id,"iv_premium")]'))

            if self.click(L.main.subscribe.back_btn):
                
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP Back fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
        
    def sce_6_13_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.main.shortcut.tti.overwrite_cancel)

            if self.element(L.main.shortcut.tti.prompt).text == self.input:
                
                return "PASS"
            else:
                raise Exception('[Fail] Prompt is incorrect')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
        
    def sce_6_13_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.main.shortcut.tti.overwrite_ok)
            prompt = self.element(L.main.shortcut.tti.prompt).text

            if prompt != self.input:
                

                self.input = prompt

                return "PASS"
            else:
                raise Exception('[Fail] Prompt is incorrect')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)
            self.click(xpath('//*[contains(@resource-id,"cv_sticker") and not(.//*[contains(@resource-id,"iv_premium")])]'))
            self.click(L.main.shortcut.tti.overwrite_ok)
            self.input = self.element(L.main.shortcut.tti.prompt).text

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
            self.page_main.enter_shortcut('Text to Image')
            self.click(L.main.shortcut.tti.entry)
            self.element(L.main.shortcut.tti.prompt).click()
            self.click(L.main.shortcut.tti.prompt)
            tags = self.elements(L.main.shortcut.tti.recommend)
            for tag in tags:
                tag.click()
            self.click(L.main.shortcut.tti.done)

            return "FAIL"
