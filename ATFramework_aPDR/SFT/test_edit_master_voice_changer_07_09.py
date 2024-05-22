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


class Test_Edit_Master_Voice_Changer:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "fcc9b63f-bdf3-4bf0-9f0f-4471dcee8fe0",
            "dbc83692-2d27-4f6b-a421-1302cde1455e",
            "293d80b4-bb8c-438b-84b6-d8f8cbb51cb7",
            "8fd47126-20be-422e-ab53-d7c102226a1e",
            "c7ba5882-dcfd-498b-aed6-02aba1cc7222",
            "0caff366-435c-455f-b8cc-001d8101da96",
            "4bf9333e-bb70-4731-bf6f-2781706256c8",
            "d66b8df2-8627-4274-b0f9-a45507ce0db4",
            "7d4aa421-efda-4cde-ab49-346e4612567b",
            "999c2308-9404-4e9a-8613-f81487c39c19",
            "42d07e0b-5592-4d7b-9f78-f076629b5408",
            "d9948d01-c808-4ee6-9502-1e0dd1352465",
            "3c20c1e5-9483-4d3f-98e3-e2f705b8fa96",
            "fafc1e10-71dc-4992-8b6f-09b090197208",
            "1fc3dfdd-8548-481e-8bba-97d04dd0715d"
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

    def sce_7_9_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_16_9)
            self.click(L.edit.master.clip())

            locator = id('tool_entry_label')[1]
            entry = self.element(xpath(f'//*[@resource-id="{locator}" and @text="AI Audio \nTool"]/../..'))
            if entry.get_attribute('enabled') == 'false':
                
                return "PASS"
            else:
                raise Exception('[Fail] Entry is not disabled')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_16_9)
            self.click(L.edit.master.clip())

            return "FAIL"

    def sce_7_9_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.menu.delete)
            self.page_edit.add_master_media('video', test_material_folder, video_20min)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)

            if self.element(L.edit.ai_audio_tool.title).text == 'AI Voice Changer':
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter the page')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_20min)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)

            return "FAIL"

    def sce_7_9_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.cancel)

            if self.is_exist(xpath('//android.widget.TextView[@text="AI Voice\nChanger"]')):
                
                return "PASS"
            else:
                raise Exception('[Fail] No found "AI Voice Changer" tool')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_20min)
            self.page_edit.enter_main_tool('AI Audio \nTool')

            return "FAIL"

    def sce_7_9_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.tool_back)

            if self.is_exist(id('tool_entry_icon')):
                
                return "PASS"
            else:
                raise Exception('[Fail] No found clip tools')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_20min)
            self.click(L.edit.master.clip())

            return "FAIL"

    def sce_7_9_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)

            if self.element(L.edit.ai_audio_tool.title).text == 'AI Voice Changer':
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter the page')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_20min)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)

            return "FAIL"

    def sce_7_9_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.unlock)

            if self.click(L.main.subscribe.back_btn):
                
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP back fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_20min)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('AI Audio \nTool')

            return "FAIL"

    def sce_7_9_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.menu.delete)
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.effect)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first)
            self.click(L.edit.ai_audio_tool.ok)

            if self.is_exist(L.edit.ai_audio_tool.voice_changer_is_applied):
                
                return "PASS"
            else:
                raise Exception('[Fail] Voice Changer is not applied')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')

    def sce_7_9_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

            if self.is_exist(L.edit.ai_audio_tool.voice_changer_is_applied):
                
                return "PASS"
            else:
                raise Exception('[Fail] Voice Changer is not applied')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_9_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.filter)
            self.click(L.edit.ai_audio_tool.filter_close)

            if not self.is_exist(L.edit.ai_audio_tool.filter_save):
                
                return "PASS"
            else:
                raise Exception('[Fail] Filter is still exist')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)

    def sce_7_9_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.filter)
            options = self.elements(xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup'))
            for i in options:
                i.click()
            self.click(L.edit.ai_audio_tool.filter_save)

            if self.is_exist(L.edit.ai_audio_tool.voice()) or self.is_exist(find_string('No results found for your selected filters.')) :
                
                return "PASS"
            else:
                raise Exception('[Fail] Apply filter fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.filter)
            options = self.elements(xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup'))
            for i in options:
                i.click()
            self.click(L.edit.ai_audio_tool.filter_save)

    def sce_7_9_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.filter)
            self.click(L.edit.ai_audio_tool.filter_reset)
            option = self.element(L.edit.ai_audio_tool.voice_changer.filter_option(0))
            self.click(L.edit.ai_audio_tool.filter_save)

            if option.get_attribute('selected') == 'false':
                
                return "PASS"
            else:
                raise Exception('[Fail] Reset filter fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_9_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                raise Exception('[Fail] Voice changer preview is OFF')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_9_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.ai_audio_tool.voice_changer_on_off)

            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'false':
                
                return "PASS"
            else:
                raise Exception('[Fail] Turn off voice changer preview fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.professional)
            self.click(L.edit.ai_audio_tool.voice())
            self.click(L.edit.ai_audio_tool.apply)
            self.click(L.edit.try_before_buy.try_it_first, 1)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

    def sce_7_9_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.click(L.edit.ai_audio_tool.voice_changer.remove)
            self.click(L.edit.ai_audio_tool.ok)

            if not self.is_exist(L.edit.ai_audio_tool.voice_changer_is_applied, 2):
                
                return "PASS"
            else:
                raise Exception('[Fail] Remove voice changer fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')

    def sce_7_9_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.ai_voice_changer)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)
            self.click(L.edit.menu.produce)

            if self.click(L.main.subscribe.back_btn):
                
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP Back fail')

        except Exception as err:
            traceback.print_exc()
            

    
    def test_case(self):
        result = {"sce_7_9_4": self.sce_7_9_4(),
                  "sce_7_9_1": self.sce_7_9_1(),
                  "sce_7_9_6": self.sce_7_9_6(),
                  "sce_7_9_2": self.sce_7_9_2(),
                  "sce_7_9_3": self.sce_7_9_3(),
                  "sce_7_9_5": self.sce_7_9_5(),
                  "sce_7_9_7": self.sce_7_9_7(),
                  "sce_7_9_8": self.sce_7_9_8(),
                  "sce_7_9_9": self.sce_7_9_9(),
                  "sce_7_9_10": self.sce_7_9_10(),
                  "sce_7_9_11": self.sce_7_9_11(),
                  "sce_7_9_12": self.sce_7_9_12(),
                  "sce_7_9_13": self.sce_7_9_13(),
                  "sce_7_9_14": self.sce_7_9_14(),
                  "sce_7_9_15": self.sce_7_9_15(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
