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

# global
preview_default = None
preview_before = None


class Test_Overlay_Filter:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = ['9fa19a3c-2de2-4086-b428-dd86b6964d38',
                     '6f0a1dbd-0803-4c93-bcd4-7cf7d5c6beee',
                     'bdf4c115-df7c-468a-823d-00056f953ee9',
                     '62787882-6844-44bd-9463-54ad375ebae5',
                     '285c589d-4773-4c15-a028-66569ae2548a',
                     '95c5ee32-3163-422b-9040-17c94f169614',
                     'fd2b27cc-1d96-442a-ab24-49614705bb31',
                     '767efa1f-b544-4ab7-bd6b-d737f92720ff',
                     '2695c58a-69bb-41aa-972e-2c38615571d4',
                     '3115e48a-c912-4bb3-b090-e53640a650ea',
                     '0dcd9201-2b0f-42c4-b790-a8d8f1a3e4f1',
                     '5d93d985-e722-4aa4-b935-973b22da9fd2',
                     'bfbc60f8-bc92-4955-992d-19d70ceeb3bb',
                     'febccfeb-9763-461e-b6b1-fe0656e044a9',
                     '12b0f13a-1a90-4153-be74-e2667331ffb0',
                     '635cf33e-e59c-4dd5-bf6c-7755126ded33',
                     '95c20578-458d-471c-ba06-75d6048af8c3'
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
        driver.driver.close_app()

    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')

    def sce_9_1_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)

            if self.is_exist(L.edit.fx_layer.filter.item()):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the Filter')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)

            return "FAIL"

    def sce_9_1_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')

            if self.is_exist(L.edit.fx_layer.filter.item()):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the Filter')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')

            return "FAIL"

    def sce_9_1_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.preview_original = self.page_main.get_preview_pic()
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.preview_apply = self.page_main.get_preview_pic()
            self.click(L.edit.fx_layer.filter.edit)

            if self.is_exist(L.edit.fx_layer.filter.slider):
                
                return "PASS"
            else:
                raise Exception("[FAIL] No slider")

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.preview_original = self.page_main.get_preview_pic()
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.edit)

            return "FAIL"

    def sce_9_1_4(self):
        uuid = self.uuid[3]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.fx_layer.filter.slider).text

            if value == '100.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.edit)

            return "FAIL"

    def sce_9_1_5(self):
        uuid = self.uuid[4]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.fx_layer.filter.slider)
            value = self.element(L.edit.fx_layer.filter.slider).text

            if value == '0.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.edit)
            self.driver.drag_slider_to_min(L.edit.fx_layer.filter.slider)

            return "FAIL"

    def sce_9_1_6(self):
        uuid = self.uuid[5]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_apply).full_compare_result():
                

                self.preview_apply = preview

                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.edit)
            self.driver.drag_slider_to_min(L.edit.fx_layer.filter.slider)
            self.preview_apply = self.page_main.get_preview_pic()

            return "FAIL"

    def sce_9_1_7(self):
        uuid = self.uuid[6]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.fx_layer.filter.slider)
            value = self.element(L.edit.fx_layer.filter.slider).text
            if value == '100.0':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.edit)
            self.driver.drag_slider_to_max(L.edit.fx_layer.filter.slider)

            return "FAIL"

    def sce_9_1_8(self):
        uuid = self.uuid[7]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_apply).full_compare_result():
                

                self.preview_apply = preview

                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.edit)
            self.driver.drag_slider_to_max(L.edit.fx_layer.filter.slider)
            self.preview_apply = self.page_main.get_preview_pic()

    def sce_9_1_9(self):
        uuid = self.uuid[8]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        report.new_result(uuid, None, 'AT limitation')

        # try:
        #     action = TouchAction(self.driver.driver)
        #     action.long_press(self.element(L.edit.effect.filter.compare), duration=5000).perform()
        #     preview = self.page_main.get_preview_pic()
        #     action.release()
        #
        #     if HCompareImg(preview, self.preview_original).full_compare_result():
        #         
        #
        #         return "PASS"
        #     else:
        #         raise Exception(f'[Fail] Preview no change')
        #
        # except Exception as err:
        #     traceback.print_exc()
        #     self.stop_recording(func_name)
        #     
        #
        #     self.driver.driver.close_app()
        #     self.driver.driver.launch_app()
        #     self.page_main.enter_launcher()
        #     self.page_main.enter_timeline()
        #     self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
        #     self.page_edit.enter_main_tool('Effect')
        #     self.click(find_string('Filter'))
        #     self.click(L.edit.effect.add)
        #     self.click(L.edit.effect.filter.item())
        #     self.page_edit.try_it_first()
        #     self.click(L.edit.effect.filter.edit)
        #     self.driver.drag_slider_to_max(L.edit.effect.filter.slider)

    def sce_9_1_10(self):
        uuid = self.uuid[9]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.compare)
            preview = self.page_main.get_preview_pic()

            if HCompareImg(preview, self.preview_apply).full_compare_result():
                

                return "PASS"
            else:
                raise Exception(f'[Fail] Preview not resumed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()

    def sce_9_1_11(self):
        uuid = self.uuid[10]
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.cancel)
            preview = self.page_main.get_preview_pic()

            if HCompareImg(preview, self.preview_original).full_compare_result():
                

                return "PASS"
            else:
                raise Exception(f'[Fail] Preview not resumed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.cancel)

    def sce_9_1_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.tool_menu_filter)

            if self.is_exist(L.edit.fx_layer.filter.item()):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the Filter')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)

    def sce_9_1_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.apply)
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare_result():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.item())
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.apply)

    def sce_9_1_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.tool_menu_filter)
            self.click(L.edit.fx_layer.filter.none)
            self.click(L.edit.fx_layer.filter.apply)
            preview = self.page_main.get_preview_pic()

            if HCompareImg(preview, self.preview_original).full_compare_result():
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.none)
            self.click(L.edit.fx_layer.filter.apply)

    def sce_9_1_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.sub_tool.back)

            filter_layer = self.element(L.edit.fx_layer.filter.clip()).rect
            playhead = self.element(L.edit.timeline.playhead).rect
            x = filter_layer['x'] + filter_layer['width'] - playhead['x']
            y = playhead['y'] + playhead['height']/2
            self.driver.driver.swipe(playhead['x'], y, x, y, 5000)

            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)

            self.click(L.edit.fx_layer.filter.item(3))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.filter.apply_to_all)
            self.click(L.edit.fx_layer.filter.apply)

            self.click(L.edit.fx_layer.filter.clip(1))
            self.click(L.edit.fx_layer.filter.tool_menu_filter)

            if self.element(L.edit.fx_layer.filter.item_name(3)).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Highlight incorrect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.cancel)
            self.click(L.edit.sub_tool.back)
            filter_layer = self.element(L.edit.fx_layer.filter.clip()).rect
            playhead = self.element(L.edit.timeline.playhead).rect
            x = filter_layer['x'] + filter_layer['width'] - playhead['x']
            y = playhead['y'] + playhead['height'] / 2
            self.driver.driver.swipe(playhead['x'], y, x, y, 5000)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)

    def sce_9_1_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.cancel)

            clip = self.element(L.edit.fx_layer.filter.clip(2))
            clip.click()
            start_x = clip.rect['x'] + clip.rect['width']/2
            end_x = self.element(L.edit.timeline.playhead).rect['x']
            y = clip.rect['y']
            self.driver.driver.swipe(start_x, y, end_x, y, 2500)

            self.click(L.edit.fx_layer.filter.tool_menu_split)

            if len(self.elements(L.edit.fx_layer.filter.clip(0))) == 4:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Clip num incorrect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.sub_tool.back)
            filter_layer = self.element(L.edit.fx_layer.filter.clip()).rect
            playhead = self.element(L.edit.timeline.playhead).rect
            x = filter_layer['x'] + filter_layer['width'] - playhead['x']
            y = playhead['y'] + playhead['height'] / 2
            self.driver.driver.swipe(playhead['x'], y, x, y, 5000)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Filter'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Filter')
            self.click(L.edit.fx_layer.filter.cancel)
            clip = self.element(L.edit.fx_layer.filter.clip(2))
            clip.click()
            start_x = clip.rect['x'] + clip.rect['width'] / 2
            end_x = self.element(L.edit.timeline.playhead).rect['x']
            y = clip.rect['y']
            self.driver.driver.swipe(start_x, y, end_x, y, 2500)
            self.click(L.edit.fx_layer.filter.tool_menu_split)

    def sce_9_1_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.fx_layer.filter.tool_menu_duplicate)

            if len(self.elements(L.edit.fx_layer.filter.clip(0))) == 5:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Clip num incorrect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            



    def test_case(self):
        result = {"sce_9_1_1": self.sce_9_1_1(),
                  "sce_9_1_2": self.sce_9_1_2(),
                  "sce_9_1_3": self.sce_9_1_3(),
                  "sce_9_1_4": self.sce_9_1_4(),
                  "sce_9_1_5": self.sce_9_1_5(),
                  "sce_9_1_6": self.sce_9_1_6(),
                  "sce_9_1_7": self.sce_9_1_7(),
                  "sce_9_1_8": self.sce_9_1_8(),
                  # "sce_9_1_9": self.sce_9_1_9(),
                  "sce_9_1_10": self.sce_9_1_10(),
                  "sce_9_1_11": self.sce_9_1_11(),
                  "sce_9_1_12": self.sce_9_1_12(),
                  "sce_9_1_13": self.sce_9_1_13(),
                  "sce_9_1_14": self.sce_9_1_14(),
                  "sce_9_1_15": self.sce_9_1_15(),
                  "sce_9_1_16": self.sce_9_1_16(),
                  "sce_9_1_17": self.sce_9_1_17(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
