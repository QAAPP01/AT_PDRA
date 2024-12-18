import pytest, os, inspect, base64, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory

from .conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'

# global
preview_default = None
preview_before = None


class Test_Effect:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        driver.driver.close_app()
        
    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')

    def sce_7_2_1(self):
        uuid = '5934f484-9410-45e9-b636-5b23e9c99ff6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')

            if self.is_exist(L.edit.master.effect.effect()):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the effect')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')

            return "FAIL"

    def sce_7_2_2(self):
        uuid = '0606d5b9-b7a0-4f29-b0a8-a4590f535afd'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            global preview_default
            preview_default = self.page_main.get_preview_pic()
            self.click(L.edit.master.effect.effect(1))
            self.click(L.edit.try_before_buy.try_it_first, 1)

            if self.element(id('itemMask')).get_attribute("selected") == "true":
                
                return "PASS"
            else:
                raise Exception("[FAIL] Effect is not selected")

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.click(L.edit.master.ai_effect.effect(1))
            self.click(L.edit.try_before_buy.try_it_first, 1)

            return "FAIL"

    def sce_7_2_3(self):
        uuid = 'b5509a27-f666-46aa-86f3-80308c15e20a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.effect.cancel)
            after_preview = self.page_main.get_preview_pic()

            if HCompareImg(after_preview, preview_default).full_compare() > 0.96:
                
                return "PASS"
            else:
                raise Exception("[FAIL] Images diff")

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')

            return "FAIL"

    def sce_7_2_4(self):
        uuid = '628bbb74-58fe-4124-b436-1ac2c85c0c5c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            effect_name = self.element(L.edit.master.effect.effect_name(1)).text

            self.long_press(L.edit.master.effect.effect(1))

            if not self.element(L.edit.master.effect.favorite_icon(1)).get_attribute("selected") == "true":
                raise Exception('[Fail] Favorite icon is not lighted up')

            self.click(find_string("Favorites"))

            if not self.is_exist(find_string(effect_name)):
                raise Exception('[Fail] Cannot find the effect in the favorite category')

            
            return "PASS"

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.long_press(L.edit.master.effect.effect(1))
            self.click(find_string("Favorites"))

            return "FAIL"

    def sce_7_2_5(self):
        uuid = 'cb938d4f-259e-4640-9062-49bb8425faec'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.long_press(L.edit.master.effect.effect(1))

            if not self.is_exist(L.edit.master.effect.effect(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Favorite category is not empty')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')

            return "FAIL"

    def sce_7_2_6(self):
        uuid = '8d2a5c71-5274-4786-ad45-89d3825a62d3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.click_category("Texture", L.edit.master.effect.category(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter "Texture"')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))

            return "FAIL"

    def sce_7_2_7(self):
        uuid = 'e67df955-4cbd-4bd5-900d-e9cd2164374c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))

        try:
            if self.is_exist(L.edit.master.effect.edit):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find "Solarize"')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))

            return "FAIL"

    def sce_7_2_8(self):
        uuid = 'f298392c-b7cf-4972-9e22-f481e186d1be'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.effect.edit)
            global preview_before
            preview_before = self.page_main.get_preview_pic()

            size_text = self.element(L.edit.master.effect.value()).text

            if size_text == '120':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Default value incorrect: {size_text}')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_2_9(self):
        uuid = '8e18a9e8-a447-4aea-8f1e-123595cb55bd'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.master.effect.slider())
            size_text = self.element(L.edit.master.effect.value()).text

            if size_text == '255':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Max value incorrect: {size_text}')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_2_10(self):
        uuid = '10e58ba1-fb87-4d7b-84e9-d1aa3921a521'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            preview_after = self.page_main.get_preview_pic()

            if HCompareImg(preview_after, preview_before).full_compare() < 1:
                
                return "PASS"
            else:
                raise Exception('[Fail] Preview has no changed')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_2_11(self):
        uuid = 'fa2f384c-53e7-420d-9d49-6d6272aa4238'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.master.effect.slider())
            size_text = self.element(L.edit.master.effect.value()).text

            if size_text == '0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] min value incorrect: {size_text}')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_2_12(self):
        uuid = '6ba32eb7-728c-4868-8831-c22cf170352b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            preview_after = self.page_main.get_preview_pic()

            if HCompareImg(preview_after, preview_before).full_compare() < 1:
                
                return "PASS"
            else:
                raise Exception('[Fail] Preview has no changed')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_2_13(self):
        uuid = 'cfee92ca-96aa-4b3a-b6b3-acf267d197bb'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.effect.reset)
            size_text = self.element(L.edit.master.effect.value()).text

            if size_text == '120':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value is not the default(120): {size_text}')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_2_14(self):
        uuid = '28afbbfa-bf9e-49cc-9036-b878869456c8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.effect.back)

            if self.is_exist(L.edit.master.effect.effect()):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the effect')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_category("Texture", L.edit.master.effect.category(0))
            self.page_edit.click_effect("Solarize", L.edit.master.effect.effect_name(0))

            return "FAIL"

    def sce_7_2_15(self):
        uuid = '57de526e-0748-46d3-aa15-1e6d9f2af112'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.effect.ok)
            preview_after = self.page_main.get_preview_pic()

            if HCompareImg(preview_after, preview_default).full_compare() < 1:
                
                return "PASS"
            else:
                raise Exception('[Fail] Preview has no changed')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            return "FAIL"

    def test_case(self):
        result = {"sce_7_2_1": self.sce_7_2_1(),
                  "sce_7_2_2": self.sce_7_2_2(),
                  "sce_7_2_3": self.sce_7_2_3(),
                  "sce_7_2_4": self.sce_7_2_4(),
                  "sce_7_2_5": self.sce_7_2_5(),
                  "sce_7_2_6": self.sce_7_2_6(),
                  "sce_7_2_7": self.sce_7_2_7(),
                  "sce_7_2_8": self.sce_7_2_8(),
                  "sce_7_2_9": self.sce_7_2_9(),
                  "sce_7_2_10": self.sce_7_2_10(),
                  "sce_7_2_11": self.sce_7_2_11(),
                  "sce_7_2_12": self.sce_7_2_12(),
                  "sce_7_2_13": self.sce_7_2_13(),
                  "sce_7_2_14": self.sce_7_2_14(),
                  "sce_7_2_15": self.sce_7_2_15(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")



