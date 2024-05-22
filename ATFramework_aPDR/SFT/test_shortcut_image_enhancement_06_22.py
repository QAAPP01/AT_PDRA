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


class Test_Tempo_Effect:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "5cf517d0-545d-4bbe-bc03-54234d6d1781",
            "08fe9bf6-7310-46de-ae60-945e2cf4c7dc",
            "3ab9ade5-b612-4bb0-823c-2b6545f144bb",
            "f4bbdd48-09c7-430c-b514-fbcc2add708a",
            "c8664568-f2b9-405e-8b80-fcf37f5faca4",
            "c85487d5-c510-408a-a5e1-4d86faca2561",
            "8f3712ed-1ef3-4014-bf53-3faef09a3280",
            "5debdf45-7ef4-41b2-b454-6d40cf2e13db",
            "cf052218-c9d7-47bd-94a4-2a0aa00c30a7",
            "05bdc10c-ad25-4588-a2b5-35b376051c84",
            "25423e9d-0450-4df7-9307-aa0e2daccf8a",
            "2b154983-1905-4ed2-b3e5-9ce7b0a1e7c4",
            "97a7213d-d80a-4b91-b5fe-333c27a2e2ba",
            "60cf47f6-8ccf-4b18-b608-0042118e1c4b"
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
        self.is_not_exist = self.page_main.h_is_not_exist

        
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def sce_6_22_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Image enhancement')

            if self.is_exist(find_string('Add Media')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter media picker failed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Image enhancement')

            return "FAIL"

    def sce_6_22_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.import_media.media_library.back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Return launcher failed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_22_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Image enhancement')
            self.page_media.select_local_photo(test_material_folder, photo_16_9)

            if self.is_exist(find_string('Export')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Enter editor failed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Image enhancement')
            self.page_media.select_local_photo(test_material_folder, photo_16_9)

            return "FAIL"

    def sce_6_22_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.pic_disable = self.page_main.get_preview_pic()
            self.click(find_string('Compare'))
            self.pic_enable = self.page_main.get_preview_pic()

            if not HCompareImg(self.pic_enable, pic_disable).ssim_compare():
                
                return "PASS"
            else:
                raise Exception('[Fail] Preview no change')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Image enhancement')
            self.page_media.select_local_photo(test_material_folder, photo_16_9)
            self.click(find_string('Compare'))
            self.pic_enable = self.page_main.get_preview_pic()

            return "FAIL"

    def sce_6_22_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            thumb = self.element(L.main.shortcut.photo_enhance.compare_thumb)
            rect = thumb.rect
            x = rect['x']
            y = rect['y']
            self.page_main.h_drag_element(thumb, x - 100, y)
            pic_after = self.page_main.get_preview_pic()

            if not HCompareImg(self.pic_enable, pic_after).ssim_compare():
                
                return "PASS"
            else:
                raise Exception('[Fail] Preview no change')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Image enhancement')
            self.page_media.select_local_photo(test_material_folder, photo_16_9)
            self.click(find_string('Compare'))

            return "FAIL"

    def sce_6_22_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(find_string('Compare'))
            pic_after = self.page_main.get_preview_pic()

            if HCompareImg(self.pic_disable, pic_after).ssim_compare():
                
                return "PASS"
            else:
                raise Exception('[Fail] Preview not resumed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Image enhancement')
            self.page_media.select_local_photo(test_material_folder, photo_16_9)

            return "FAIL"

    def sce_6_21_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.play)
            time.sleep(3)
            self.timecode_play = self.element(L.main.shortcut.timecode).text

            if self.timecode_play != "00:00":
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {self.timecode_play}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.play)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play != self.timecode_play:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play == '00:00':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tempo_effect.premium_item())

            if self.is_exist(L.edit.try_before_buy.premium_tag):
                
                return "PASS"
            else:
                raise Exception(f'[Fail] No premium tage')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_21_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.effect_name = self.element(L.main.shortcut.tempo_effect.effect_name(2)).text
            self.click(L.main.shortcut.tempo_effect.edit)

            if self.is_exist(find_string("Adjust")):
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Enter edit room fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.effect_name = self.element(L.main.shortcut.tempo_effect.effect_name(2)).text
            self.click(L.main.shortcut.tempo_effect.edit)

            return "FAIL"

    def sce_6_21_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tempo_effect.edit_back)

            if not self.is_exist(find_string("Adjust"), 1):
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Return effect room fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))

            return "FAIL"

    def sce_6_21_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tempo_effect.edit)
            self.click(L.main.shortcut.tempo_effect.spinner)

            if self.click(L.main.shortcut.tempo_effect.audio_source(2)):
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Select audio source fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.click(L.main.shortcut.tempo_effect.edit)

            return "FAIL"

    def sce_6_21_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(self.element(L.main.shortcut.tempo_effect.slider(2)))
            min_value = self.element(L.main.shortcut.tempo_effect.slider(2)).text
            self.driver.drag_slider_to_max(self.element(L.main.shortcut.tempo_effect.slider(2)))
            max_value = self.element(L.main.shortcut.tempo_effect.slider(2)).text

            if min_value != max_value:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Slider value no changed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.click(L.main.shortcut.tempo_effect.edit)

            return "FAIL"

    def sce_6_21_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(self.element(L.main.shortcut.tempo_effect.slider(3)))
            min_value = self.element(L.main.shortcut.tempo_effect.slider(3)).text
            self.driver.drag_slider_to_max(self.element(L.main.shortcut.tempo_effect.slider(3)))
            max_value = self.element(L.main.shortcut.tempo_effect.slider(3)).text

            if min_value != max_value:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Slider value no changed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.click(L.main.shortcut.tempo_effect.edit)

            return "FAIL"

    def sce_6_21_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            self.page_main.h_swipe_element(sliders[2], sliders[0], 3)
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            self.default_value = [self.element(sliders[-2]).text, self.element(sliders[-1]).text]
            self.driver.drag_slider_to_min(sliders[-2])
            min_value = self.element(sliders[-2]).text
            self.driver.drag_slider_to_max(sliders[-2])
            max_value = self.element(sliders[-2]).text

            if min_value != max_value:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Slider value no changed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.click(L.main.shortcut.tempo_effect.edit)
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            self.page_main.h_swipe_element(sliders[2], sliders[0], 3)
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            self.default_value = [self.element(sliders[-2]).text, self.element(sliders[-1]).text]
            self.driver.drag_slider_to_max(sliders[-2])

            return "FAIL"

    def sce_6_21_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            self.driver.drag_slider_to_min(sliders[-1])
            min_value = self.element(sliders[-1]).text
            self.driver.drag_slider_to_max(sliders[-1])
            max_value = self.element(sliders[-1]).text

            if min_value != max_value:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Slider value no changed')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.click(L.main.shortcut.tempo_effect.edit)
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            self.page_main.h_swipe_element(sliders[1], sliders[0], 5)
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            self.driver.drag_slider_to_max(sliders[-2])
            self.driver.drag_slider_to_max(sliders[-1])

            return "FAIL"

    def sce_6_21_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.tempo_effect.reset)
            sliders = self.elements(L.main.shortcut.tempo_effect.slider(0))
            value_1 = self.element(sliders[-2]).text
            value_2 = self.element(sliders[-1]).text

            if [value_1, value_2] == self.default_value:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] {value_1}, {value_2} != {self.default_value}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))
            self.click(L.main.shortcut.tempo_effect.edit)

            return "FAIL"

    def sce_6_21_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.full_editor)
            self.page_edit.click_sub_tool("AI Effect")
            item_name = self.element(xpath('//*[contains(@resource-id,"itemEdit")]/../../*[contains(@resource-id,"itemName")]')).text

            if item_name == self.effect_name:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] {item_name} != {self.effect_name}')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_6_21_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.menu.home)
            self.page_main.enter_shortcut('Tempo Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_9_16)
            self.page_media.waiting()
            self.click(L.main.shortcut.tempo_effect.effect(2))

            if self.page_main.shortcut_produce():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Produce fail')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()

            return "FAIL"

    
    def test_case(self):
        result = {
            "sce_6_21_1": self.sce_6_21_1(),
            "sce_6_21_2": self.sce_6_21_2(),
            "sce_6_21_3": self.sce_6_21_3(),
            "sce_6_21_4": self.sce_6_21_4(),
            "sce_6_21_5": self.sce_6_21_5(),
            "sce_6_21_6": self.sce_6_21_6(),
            "sce_6_21_7": self.sce_6_21_7(),
            "sce_6_21_8": self.sce_6_21_8(),
            "sce_6_21_9": self.sce_6_21_9(),
            "sce_6_21_10": self.sce_6_21_10(),
            "sce_6_21_11": self.sce_6_21_11(),
            "sce_6_21_12": self.sce_6_21_12(),
            "sce_6_21_13": self.sce_6_21_13(),
            "sce_6_21_14": self.sce_6_21_14(),
            "sce_6_21_15": self.sce_6_21_15(),
            "sce_6_21_16": self.sce_6_21_16(),
            "sce_6_21_17": self.sce_6_21_17(),
            "sce_6_21_18": self.sce_6_21_18(),
            "sce_6_21_19": self.sce_6_21_19(),
            "sce_6_21_20": self.sce_6_21_20(),
            "sce_6_21_21": self.sce_6_21_21(),
            "sce_6_21_22": self.sce_6_21_22(),
            "sce_6_21_23": self.sce_6_21_23(),
        }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
