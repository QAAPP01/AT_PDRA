import pytest, os, inspect, base64, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME

from .conftest import TEST_MATERIAL_FOLDER
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))


pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'

# global
preview_default = None
preview_before = None


class Test_Ai_Effect:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
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

    def sce_7_1_1(self):
        uuid = '7713342c-d600-43b7-9fe8-1675a2124c7b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.page_edit.click_tool('AI Effect')

            if self.is_exist(L.edit.master.ai_effect.effect()):
                
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
            self.page_edit.click_tool('AI Effect')

            return "FAIL"

    def sce_7_1_2(self):
        uuid = '09586d72-f271-4863-9e7e-36416d682706'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            global preview_default
            preview_default = self.page_main.get_preview_pic()
            self.click(L.edit.master.ai_effect.effect(1))
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_media.waiting_download()

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
            self.page_edit.click_tool('AI Effect')
            self.click(L.edit.master.ai_effect.effect(1))
            self.click(L.edit.try_before_buy.try_it_first, 1)

            return "FAIL"

    def sce_7_1_3(self):
        uuid = 'b235c57c-2f0e-41af-94b7-559ef7848880'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.ai_effect.cancel)
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

            return "FAIL"

    def sce_7_1_4(self):
        uuid = '283f410f-a8aa-4ff7-aa9f-b60221586e8d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_sub_tool("AI Effect")

            if self.is_exist(L.edit.master.ai_effect.effect()):
                
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
            self.page_edit.click_sub_tool("AI Effect")

            return "FAIL"

    def sce_7_1_5(self):
        uuid = 'a887fe92-4174-45eb-b042-3e5967c6df35'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            effect_name = self.element(L.edit.master.ai_effect.effect_name(1)).text

            self.long_press(L.edit.master.ai_effect.effect(1))

            if not self.element(L.edit.master.ai_effect.favorite_icon(1)).get_attribute("selected") == "true":
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
            self.page_edit.click_sub_tool("AI Effect")
            self.long_press(L.edit.master.ai_effect.effect(1))
            self.click(find_string("Favorites"))

            return "FAIL"

    def sce_7_1_6(self):
        uuid = 'b6684755-ce40-4db2-b117-54004bf61e0e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.long_press(L.edit.master.ai_effect.effect(1))

            if not self.is_exist(L.edit.master.ai_effect.effect(0)):
                
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
            self.page_edit.click_sub_tool("AI Effect")

            return "FAIL"

    def sce_7_1_7(self):
        uuid = 'b38fa219-f9de-4492-9d97-cb8385bb2a4b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter "Body Effect"')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))

            return "FAIL"

    def sce_7_1_8(self):
        uuid = 'fcebcfb5-f2b5-41d7-91d8-70425154ba2c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))

        try:
            if self.is_exist(L.edit.master.ai_effect.edit):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find "Contour 2"')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))

            return "FAIL"

    def sce_7_1_9(self):
        uuid = '8f6911a6-f3ab-4d48-8626-08287afb95af'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.ai_effect.edit)
            global preview_before
            preview_before = self.page_main.get_preview_pic()

            color = self.elements(L.edit.master.ai_effect.color_preset(0))
            self.click(color[-1])
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_1_10(self):
        uuid = '6b006448-51b4-4c0e-aaa4-2ce61454af32'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.ai_effect.color_preset(1))
            if not self.click(L.edit.master.ai_effect.dropper):
                raise Exception("Cannot find the dropper")
            if not self.page_edit.drag_color_picker():
                raise Exception("Drag_color_picker fail")
            if not self.click(L.edit.master.ai_effect.apply):
                raise Exception("Click apply fail")
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_1_11(self):
        uuid = '03719502-c937-4167-8080-3ba26a580979'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            size_text = xpath('//*[contains(@text,"Size")]/../*[contains(@resource-id,"value")]')
            size_text = self.element(size_text).text

            if size_text == '6':
                
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_1_12(self):
        uuid = 'fde57950-3d73-4734-af2d-cf97feacb94b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.driver.drag_slider_to_max(L.edit.master.ai_effect.slider(1)):
                raise Exception("Drag slider to the max fail")
            size_text = xpath('//*[contains(@text,"Size")]/../*[contains(@resource-id,"value")]')
            size_text = self.element(size_text).text

            if size_text == '100':
                
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)
            self.driver.drag_slider_to_max(L.edit.master.ai_effect.slider(1))

            return "FAIL"

    def sce_7_1_13(self):
        uuid = '96e00830-27e6-4bd8-af67-799faed17367'
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_1_14(self):
        uuid = 'ec71b63d-857a-45e8-9aa6-ed255b7cf1a7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.master.ai_effect.slider(1))
            size_text = xpath('//*[contains(@text,"Size")]/../*[contains(@resource-id,"value")]')
            size_text = self.element(size_text).text

            if size_text == '1':
                
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)
            self.driver.drag_slider_to_min(L.edit.master.ai_effect.slider(1))

            return "FAIL"

    def sce_7_1_15(self):
        uuid = '64a6b861-c343-4afe-8758-8d522c2ee234'
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_1_16(self):
        uuid = 'b1842e2f-85e1-4733-b66a-e9e9a2709f43'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.ai_effect.reset)
            size_text = xpath('//*[contains(@text,"Size")]/../*[contains(@resource-id,"value")]')
            size_text = self.element(size_text).text

            if size_text == '6':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value is not the default(5): {size_text}')

        except Exception as err:
            self.stop_recording(func_name)
            logger(f'\n{err}')
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))
            self.click(L.edit.master.ai_effect.edit)

            return "FAIL"

    def sce_7_1_17(self):
        uuid = 'aa3241e2-63f4-4e06-b722-d3c751c0aefe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.ai_effect.back)

            if self.is_exist(L.edit.master.ai_effect.effect()):
                
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
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))

            return "FAIL"

    def sce_7_1_18(self):
        uuid = '9bd61e1e-f41a-4e72-8c8e-0060a3c86afe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.master.ai_effect.ok)
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
        result = {"sce_7_1_1": self.sce_7_1_1(),
                  "sce_7_1_2": self.sce_7_1_2(),
                  "sce_7_1_3": self.sce_7_1_3(),
                  "sce_7_1_4": self.sce_7_1_4(),
                  "sce_7_1_5": self.sce_7_1_5(),
                  "sce_7_1_6": self.sce_7_1_6(),
                  "sce_7_1_7": self.sce_7_1_7(),
                  "sce_7_1_8": self.sce_7_1_8(),
                  "sce_7_1_9": self.sce_7_1_9(),
                  "sce_7_1_10": self.sce_7_1_10(),
                  "sce_7_1_11": self.sce_7_1_11(),
                  "sce_7_1_12": self.sce_7_1_12(),
                  "sce_7_1_13": self.sce_7_1_13(),
                  "sce_7_1_14": self.sce_7_1_14(),
                  "sce_7_1_15": self.sce_7_1_15(),
                  "sce_7_1_16": self.sce_7_1_16(),
                  "sce_7_1_17": self.sce_7_1_17(),
                  "sce_7_1_18": self.sce_7_1_18(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
