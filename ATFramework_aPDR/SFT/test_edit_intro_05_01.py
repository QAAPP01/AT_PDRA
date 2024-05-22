import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from appium.webdriver.common.touch_action import TouchAction

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
video_speech = 'speech_noise_1.mp4'
video_20min = '20min.mp4'


class Test_Edit_Intro:
    @pytest.fixture(autouse=True)
    def initial(self, driver): 
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "d0bafbda-e361-4cbf-af80-9da541351a27",
            "a110aba2-999a-4d58-85bb-cdb217d5d2e7",
            "ecd0fd71-aee2-40a0-a69b-52f55ebd7ed9",
            "8a5cbcca-3072-45fe-ad31-5640d95b18a3",
            "1ae322d8-d8ec-481f-84a3-08a5fdd76adb",
            "71adbc41-8fea-4aca-a384-9afb48612000",
            "57ee9b4b-7809-42e0-9dab-f0f2c9f913f1",
            "9b2f2a26-aac6-4f88-bb91-25957758fa2b",
            "6f81c401-70fb-4e16-9f23-99de8e9deef0",
            "22104cdc-9087-464f-8797-5dabae9e750c",
            "882daf2e-a106-4ee9-9c21-69cc8c4bebe3",
            "988899b1-6436-4a64-b099-412d4766faaf",
            "2e7e5627-366e-40c1-81eb-9999b7661489",
            "26f607a5-31d8-4571-ad1d-fc936eb1749e",
            "3123ca89-836a-4541-8fb6-0db417be9a90",
            "fe999c5b-bbc1-4556-b5e6-33e858999b12",
            "d7560472-7d45-4a5c-8516-518d8c252591",
            "0ba3da30-a81b-4be4-b03b-d09707cfe999",
            "96c700ac-30b1-4e6a-94a7-4cf2eb853ff6",
            "c9a510ed-4a78-4a59-8e21-c1ca04cc5654",
            "0c368338-5336-48d8-ace0-e079a443975d",
            "a7d61b7b-7451-47f7-9c67-a06dc808cf31",
            "c03b70df-baa5-410a-b6fc-9541ace65513",
            "800eed03-6214-43fd-97ea-74eec6bb35ac",
            "b0249545-24d4-422d-b355-0ae89a367ea6",
            "2f6b8baa-cf9d-4a8c-8854-769b03d08874",
            "81e1f96b-1bec-46e5-8ca8-abebef06a217"
        ]

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
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def sce_5_1_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            if self.page_edit.intro_video.enter_intro():
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.intro_video.check_intro_caption():
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.intro_video.intro_back():
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.intro_video.check_intro_search():
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.intro_video.top_toolbar_tutorial)

            if self.is_exist(xpath('//*[@content-desc="PowerDirector Video Editor - CyberLink"]')):
                

                time.sleep(1)
                self.driver.driver.back()
                time.sleep(1)
                self.driver.driver.back()

                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.intro_video.enter_intro_profile():
                

                self.page_main.h_click(xpath('(//android.widget.Image)[1]'))

                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.intro_video.check_my_favorite():
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.category = self.page_edit.intro_video.check_category()

            if 'CyberLink' not in self.category:
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            defined = ['Beauty', 'Black & White', 'Business', 'Design', 'Education', 'Event', 'Family', 'Fashion', 'Food', 'Fun & Playful', 'Gaming', 'Handwritten', 'Health', 'Holiday', 'Life', 'Love', 'Minimalist', 'Modern', 'Music', 'Nature', 'Pets', 'Repair', 'Retro', 'Season', 'Social Media', 'Sport', 'Technology', 'Travel']
            miss = False
            for element in defined:
                if element not in self.category:
                    miss = element
                    break

            if not miss:
                

                self.result_5_1_9 = True

                return "PASS"
            else:
                raise Exception(f'[Fail] No found {miss}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.result_5_1_9:
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_5_1_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.page_edit.intro_video.tap_category():
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter Intro fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.intro_video.enter_intro()

            return "FAIL"

    def sce_7_8_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.ok)

            if self.is_exist(L.edit.ai_audio_tool.speech_enhance_is_applied):
                
                return "PASS"
            else:
                raise Exception('[Fail] Speech Enhance is not applied')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_8_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                raise Exception('[Fail] Audio tool preview is OFF')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_8_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.voice_changer_on_off)

            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'false':
                
                return "PASS"
            else:
                raise Exception('[Fail] Turn off Audio tool fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_8_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.click(L.edit.ai_audio_tool.remove)
            self.click(L.edit.ai_audio_tool.ok)

            if not self.is_exist(L.edit.ai_audio_tool.speech_enhance_is_applied, 2):
                
                return "PASS"
            else:
                raise Exception('[Fail] Speech Enhance is still applied')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')

    def sce_7_8_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.info)

            if self.click(find_string('Try it now')):
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try it now" fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '50.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

    def sce_7_8_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.ai_audio_tool.strength_slider)
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '0.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

    def sce_7_8_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.ai_audio_tool.strength_slider)
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '100.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

    def sce_7_8_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '50.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

    def sce_7_8_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.ai_audio_tool.compensation_slider)
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '0.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

    def sce_7_8_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.ai_audio_tool.compensation_slider)
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '100.0':
                

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

    def sce_7_8_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.ok)

            if self.is_exist(L.edit.ai_audio_tool.audio_denoise_is_applied):
                
                return "PASS"
            else:
                raise Exception('[Fail] Audio Denoise is not applied')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_8_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                raise Exception('[Fail] Audio tool preview is OFF')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_8_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.voice_changer_on_off)

            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'false':
                
                return "PASS"
            else:
                raise Exception('[Fail] Turn off Audio tool fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_8_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.click(L.edit.ai_audio_tool.remove)
            self.click(L.edit.ai_audio_tool.ok)

            if not self.is_exist(L.edit.ai_audio_tool.audio_denoise_is_applied, 2):
                
                return "PASS"
            else:
                raise Exception('[Fail] Audio Denoise is still applied')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')

    def sce_7_8_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)
            self.click(L.edit.menu.produce)

            if self.click(L.main.subscribe.back_btn):
                
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP Back fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()

    
    def test_case(self):
        result = {"sce_5_1_1": self.sce_5_1_1(),
                  "sce_5_1_2": self.sce_5_1_2(),
                  "sce_5_1_4": self.sce_5_1_4(),
                  "sce_5_1_5": self.sce_5_1_5(),
                  "sce_5_1_6": self.sce_5_1_6(),
                  "sce_5_1_7": self.sce_5_1_7(),
                  "sce_5_1_11": self.sce_5_1_11(),
                  "sce_5_1_8": self.sce_5_1_8(),
                  "sce_5_1_9": self.sce_5_1_9(),
                  "sce_5_1_3": self.sce_5_1_3(),
                  "sce_5_1_10": self.sce_5_1_10(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
