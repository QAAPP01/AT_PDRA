import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from appium.webdriver.common.touch_action import TouchAction

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import REPORT_INSTANCE as report
from .conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'
video_speech = 'speech_noise_1.mp4'
video_20min = '20min.mp4'


class Test_Edit_Master_Audio_Tool:
    @pytest.fixture(autouse=True)
    def initial(self, driver): 
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "8b925085-4b38-4a37-8014-cfad110723f7",
            "f65c9fc9-4dd5-4524-b44b-19996ac0ce39",
            "964d05bd-66f8-4a82-9b37-a8bb6c59f3a3",
            "1b8a2560-13e7-45b8-86d7-8827bd77a95d",
            "b57ce391-1ff5-4de7-b2d3-2a6ac32291a5",
            "abdf46c8-f3ef-48fb-bdd7-d086f40d5c11",
            "31268592-c7d0-453a-8a75-36f7e7205bc8",
            "051dc239-bd7f-41b1-b1a3-ae1ba97a5b60",
            "2f1bac70-dae4-48d8-95f2-37c0071984e8",
            "ec8dfbcf-fb9a-4c53-abca-0abd182f2482",
            "cd05e561-e069-40b3-81d1-a9cc4a2def95",
            "811a6299-0eb8-4c03-8036-394a0527cefc",
            "b244215c-fd35-40b3-951e-55b935261e9a",
            "0d02707d-224a-48cd-918b-6bcbff51c8a3",
            "e95e9712-3980-444e-baad-8ee43b4c780a",
            "e022aa69-b15c-4b0d-adae-7a5a1891019d",
            "3076c274-bf5a-4120-8811-58344116680c",
            "53ffe99a-9cb2-49ec-895c-3002b78e6c4a",
            "c096ebc3-e466-40aa-91b5-5cef388a3fcc",
            "dac4fd4a-53b2-421b-bb82-ff5031687a19",
            "42b58fb4-e9b0-4cc0-ba3b-95dedc1f4cf8",
            "9def28a4-588b-4d8e-ac86-e3e665b5e570",
            "c6c35988-70ef-4ee7-8e22-5c5ed1d4a951",
            "9084c8a0-146b-43e6-9256-fe3fe5378b40",
            "721d9f68-9c8e-40d8-9f76-6f42abb5f93a",
            "a1eaecbb-6ac8-4c25-870a-883034fe1cdd",
            "a1d1db89-963d-43b7-95cb-bd09a7e045c0"
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

        report.set_driver(driver)
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def sce_7_8_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_16_9)
            self.click(L.edit.master.clip())

            locator = id('tool_entry_label')[1]
            entry = self.element(xpath(f'//*[@resource-id="{locator}" and @text="AI Audio \nTool"]/../..'))
            if entry.get_attribute('enabled') == 'false':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Entry is not disabled')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_16_9)
            self.click(L.edit.master.clip())

            return "FAIL"

    def sce_7_8_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.menu.delete)
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            if self.element(L.edit.ai_audio_tool.title).text == 'Speech Enhance':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter the page')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.ai_audio_tool.cancel)
            self.click(L.edit.ai_audio_tool.tool_back)

            if self.is_exist(id('tool_entry_icon')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] No found clip tools')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.click(L.edit.master.clip())

            return "FAIL"

    def sce_7_8_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            if self.element(L.edit.ai_audio_tool.title).text == 'Speech Enhance':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter the page')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.ai_audio_tool.info)
            
            if self.click(find_string('Try it now')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try it now" fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.click(L.edit.master.clip())
            self.page_edit.click_sub_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '50.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.ai_audio_tool.strength_slider)
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.ai_audio_tool.strength_slider)
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '50.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.ai_audio_tool.compensation_slider)
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.ai_audio_tool.compensation_slider)
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.ai_audio_tool.ok)

            if self.is_exist(L.edit.ai_audio_tool.speech_enhance_is_applied):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Speech Enhance is not applied')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

            return "FAIL"

    def sce_7_8_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'true':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Audio tool preview is OFF')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

            return "FAIL"

    def sce_7_8_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.ai_audio_tool.voice_changer_on_off)

            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'false':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Turn off Audio tool fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

            return "FAIL"

    def sce_7_8_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.speech_enhance)
            self.click(L.edit.ai_audio_tool.remove)
            self.click(L.edit.ai_audio_tool.ok)

            if not self.is_exist(L.edit.ai_audio_tool.speech_enhance_is_applied, 2):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Speech Enhance is still applied')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')

            return "FAIL"

    def sce_7_8_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.info)

            if self.click(find_string('Try it now')):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try it now" fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
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
        report.start_uuid(uuid)

        try:
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '50.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.ai_audio_tool.strength_slider)
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.ai_audio_tool.strength_slider)
            slider = self.element(L.edit.ai_audio_tool.strength_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '50.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.ai_audio_tool.compensation_slider)
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '0.0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.ai_audio_tool.compensation_slider)
            slider = self.element(L.edit.ai_audio_tool.compensation_slider).text
            if slider == '100.0':
                report.new_result(uuid, True)

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()

            return "FAIL"

    def sce_7_8_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.ai_audio_tool.ok)

            if self.is_exist(L.edit.ai_audio_tool.audio_denoise_is_applied):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Audio Denoise is not applied')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

            return "FAIL"

    def sce_7_8_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'true':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Audio tool preview is OFF')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

            return "FAIL"

    def sce_7_8_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.ai_audio_tool.voice_changer_on_off)

            if self.element(L.edit.ai_audio_tool.voice_changer_on_off).get_attribute('selected') == 'false':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Turn off Audio tool fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)

            return "FAIL"

    def sce_7_8_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.click(L.edit.ai_audio_tool.remove)
            self.click(L.edit.ai_audio_tool.ok)

            if not self.is_exist(L.edit.ai_audio_tool.audio_denoise_is_applied, 2):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Audio Denoise is still applied')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_speech)
            self.page_edit.enter_main_tool('AI Audio \nTool')

            return "FAIL"

    def sce_7_8_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.click_audio_tool(L.edit.ai_audio_tool.audio_denoise)
            self.page_edit.waiting()
            self.click(L.edit.ai_audio_tool.ok)
            self.click(L.edit.menu.produce)

            if self.click(L.main.subscribe.back_btn):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Click IAP Back fail')

        except Exception as err:
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)
            self.driver.driver.close_app()

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_7_8_3": self.sce_7_8_3(),
                  "sce_7_8_1": self.sce_7_8_1(),
                  "sce_7_8_2": self.sce_7_8_2(),
                  "sce_7_8_4": self.sce_7_8_4(),
                  "sce_7_8_5": self.sce_7_8_5(),
                  "sce_7_8_6": self.sce_7_8_6(),
                  "sce_7_8_7": self.sce_7_8_7(),
                  "sce_7_8_8": self.sce_7_8_8(),
                  "sce_7_8_9": self.sce_7_8_9(),
                  "sce_7_8_10": self.sce_7_8_10(),
                  "sce_7_8_11": self.sce_7_8_11(),
                  "sce_7_8_12": self.sce_7_8_12(),
                  "sce_7_8_13": self.sce_7_8_13(),
                  "sce_7_8_14": self.sce_7_8_14(),
                  "sce_7_8_15": self.sce_7_8_15(),
                  "sce_7_8_16": self.sce_7_8_16(),
                  "sce_7_8_17": self.sce_7_8_17(),
                  "sce_7_8_18": self.sce_7_8_18(),
                  "sce_7_8_19": self.sce_7_8_19(),
                  "sce_7_8_20": self.sce_7_8_20(),
                  "sce_7_8_21": self.sce_7_8_21(),
                  "sce_7_8_22": self.sce_7_8_22(),
                  "sce_7_8_23": self.sce_7_8_23(),
                  "sce_7_8_24": self.sce_7_8_24(),
                  "sce_7_8_25": self.sce_7_8_25(),
                  "sce_7_8_26": self.sce_7_8_26(),
                  "sce_7_8_27": self.sce_7_8_27(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
