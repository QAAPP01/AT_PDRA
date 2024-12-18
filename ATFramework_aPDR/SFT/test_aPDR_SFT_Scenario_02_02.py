import pytest, inspect, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME

from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))


pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_SFT_Scenario_02_02:
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

        
        driver.driver.launch_app()
        yield
        driver.driver.close_app()

    def sce_2_2_1(self):
        uuid = '4979f807-43ed-48ae-b85f-9a28b2ab989a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()

            if self.page_main.enter_timeline():
                
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find timeline canvas'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_2(self):
        uuid = '7713342c-d600-43b7-9fe8-1675a2124c7b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16):
                raise Exception('Add media fail')

            if not self.page_edit.enter_main_tool('AI Effect'):
                raise Exception('Enter AI Effect fail')

            if self.is_exist(find_string('None')):
                
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find "None"'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_3(self):
        uuid = 'e8286094-ffe5-4cca-8dd5-4a29e66f1b15'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.is_exist(L.edit.timeline.master_track.trim_indicator):
                
                return "PASS"
            else:
                fail_log = '[Fail] No master clip is selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_4(self):
        uuid = '283f410f-a8aa-4ff7-aa9f-b60221586e8d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.tap_blank_space():
                raise Exception('Tap blank space fail')
            self.click(L.edit.timeline.master_track.master_clip())
            if not self.page_edit.enter_sub_tool('AI Effect'):
                raise Exception('Enter AI Effect fail')

            if self.is_exist(L.edit.sub_tool.ai_effect.effect(0)):
                
                return "PASS"
            else:
                fail_log = '[Fail] No master clip is selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_5(self):
        uuid = 'b235c57c-2f0e-41af-94b7-559ef7848880'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if self.element(L.edit.sub_tool.ai_effect.none_highlight).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] None is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')

            return "FAIL"

    def sce_2_2_6(self):
        uuid = '09586d72-f271-4863-9e7e-36416d682706'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            index = 1
            if not self.click(L.edit.sub_tool.ai_effect.effect(index)):
                raise Exception('Click effect fail')
            self.click(L.edit.try_before_buy.try_it, 2)
            self.page_media.waiting_download()

            if self.element(L.edit.sub_tool.ai_effect.effect_name(index)).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] Effect is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.sub_tool.ai_effect.effect(1))

            return "FAIL"

    def sce_2_2_7(self):
        uuid = 'fcebcfb5-f2b5-41d7-91d8-70425154ba2c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(L.edit.sub_tool.ai_effect.edit):
                raise Exception('Click editing icon fail')

            if self.is_exist(L.edit.sub_tool.ai_effect.param_area):
                
                return "PASS"
            else:
                fail_log = '[Fail] Cannot find param_area'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.sub_tool.ai_effect.effect(1))
            self.click(L.edit.sub_tool.ai_effect.edit)

            return "FAIL"

    def sce_2_2_8(self):
        uuid = '8f6911a6-f3ab-4d48-8626-08287afb95af'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        global default_value
        try:
            param_flag = 0

            param_elements = self.elements(L.edit.sub_tool.ai_effect.param_value(0))
            for i, param_element in enumerate(param_elements, start=1):
                if param_element.text != "":
                    param_flag = 1
                    default_value = (i, param_element.text)
                    self.click(param_element)
                    self.driver.drag_slider_from_left_to_right()
                    break

            if not param_flag:
                self.click(L.edit.sub_tool_menu.back)
                effect = self.elements(L.edit.sub_tool.ai_effect.effect(0))
                other_effect_num = len(effect)
                effect_index = 1
                for j in range(other_effect_num):
                    self.click(effect[effect_index])
                    self.click(L.edit.sub_tool.ai_effect.edit)

                    param_elements = self.elements(L.edit.sub_tool.ai_effect.param_value(0))
                    for i, param_element in enumerate(param_elements, start=1):
                        if param_element.text != "":
                            param_flag = 1
                            default_value = (i, param_element.text)
                            self.click(param_element)
                            self.driver.drag_slider_from_left_to_right()
                            break

                    if param_flag:
                        break
                    else:
                        self.click(L.edit.sub_tool_menu.back)
                        effect = self.elements(L.edit.sub_tool.ai_effect.effect(0))
                        effect_index += 1

            if not param_flag:
                raise Exception('No parameter can edit in this effect')

            if self.element(L.edit.sub_tool.slider_value).text != default_value[1]:
                
                return "PASS"
            else:
                fail_log = '[Fail] Param value no change'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.sub_tool.ai_effect.effect(1))
            self.click(L.edit.sub_tool.ai_effect.edit)

            return "FAIL"

    def sce_2_2_9(self):
        uuid = 'b1842e2f-85e1-4733-b66a-e9e9a2709f43'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(L.edit.sub_tool.ai_effect.reset):
                raise Exception('Click Reset fail')

            if self.element(L.edit.sub_tool.ai_effect.param_value(default_value[0])).text == default_value[1]:
                
                return "PASS"
            else:
                fail_log = '[Fail] Param value is not equal default value'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.sub_tool.ai_effect.effect(1))
            self.click(L.edit.sub_tool.ai_effect.edit)

            return "FAIL"

    def sce_2_2_10(self):
        uuid = 'aa3241e2-63f4-4e06-b722-d3c751c0aefe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(L.edit.sub_tool.back):
                raise Exception('Click Back fail')

            if self.is_exist(L.edit.sub_tool.ai_effect.effect()):
                
                return "PASS"
            else:
                fail_log = '[Fail] No found effect'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('AI Effect')
            self.click(L.edit.sub_tool.ai_effect.effect(1))


            return "FAIL"

    def sce_2_2_11(self):
        uuid = '9bd61e1e-f41a-4e72-8c8e-0060a3c86afe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(L.edit.sub_tool.back):
                raise Exception('Tap Back button fail')

            if self.is_exist(L.edit.sub_tool.tool(0)):
                
                return "PASS"
            else:
                fail_log = '[Fail] No found 2nd layer tool menu'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            return "FAIL"

    def sce_2_2_14(self):
        uuid = '7eb3f4d4-b6a0-464c-a046-3859f69557b5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            global pic_photo_default
            pic_photo_default = self.page_main.get_preview_pic()
            if not self.page_edit.trigger_default_pan_zoom_effect(enable=True):
                raise Exception('Click default_pan_zoom_effect fail')
            self.page_edit.scroll_playhead_to_beginning()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)


            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Random')).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] Random is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_12(self):
        uuid = '6adefecd-8cbd-4164-aa84-9dd4bd06577e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.swipe_element(L.edit.timeline.timeline_ruler, 'left', 300)
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            self.click(find_string('No Effect'))
            if not self.click(L.edit.sub_tool.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('No Effect')).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] No Effect is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_13(self):
        uuid = 'd49362dd-6d87-4c27-8d5f-785749caeef2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            self.click(find_string('Random'))
            if not self.click(L.edit.sub_tool.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Random')).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] Random is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_15(self):
        uuid = '4411db3a-3fdc-461c-930f-793ab72b45a2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.click(L.edit.sub_tool.pan_zoom.custom.apply)
            if not self.click(L.edit.sub_tool.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Custom')).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] Custom is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_16(self):
        uuid = '80556c5f-b177-455d-bade-d46c0fa34195'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.scroll_playhead_to_beginning()
            if not self.click(find_string('No Effect')):
                raise Exception('Click No Effect fail')
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                
                return "PASS"
            else:
                fail_log = '[Fail] Image are different'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_17(self):
        uuid = 'adc2ccca-482d-4eb7-ac83-5bf5d4de19b7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(find_string('Random')):
                raise Exception('Click Random fail')
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_19(self):
        uuid = '1b938b47-d9e3-43db-bc7f-93deba4de02f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.driver.swipe_element(L.edit.sub_tool.pan_zoom.custom.start_position, 'up', 100)
            self.click(L.edit.sub_tool.pan_zoom.custom.apply)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)

            return "FAIL"

    def sce_2_2_18(self):
        uuid = '2fd0c8b8-59d5-4986-ad84-405637852a86'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:

            if not self.page_edit.trigger_default_pan_zoom_effect(enable=False):
                raise Exception('Disable Pan & Zoom Fail')
            self.page_edit.scroll_playhead_to_beginning()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_20(self):
        uuid = '4a4ad790-5b78-4831-a156-315877f42bb8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.scroll_playhead_to_beginning()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            global pic_video_default
            pic_video_default = self.page_main.get_preview_pic()

            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.click(L.edit.sub_tool.pan_zoom.custom.apply)

            self.driver.swipe_element(L.edit.timeline.timeline_ruler, 'left', 300)
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            self.click(find_string('No Effect'))
            if not self.click(L.edit.sub_tool.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('No Effect')).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] No Effect is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_21(self):
        uuid = '5a6815e0-1ac5-48b2-a582-567ebace8f71'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            random_icon = self.element(xpath(f'//*[contains(@text,"Random")]/preceding-sibling::android.widget.ImageView'))
            if not random_icon:
                raise Exception("Cannot locate Random's icon")

            if random_icon.get_attribute('enabled') == 'false':
                
                return "PASS"
            else:
                fail_log = '[Fail] Random is not disabled'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)

            return "FAIL"

    def sce_2_2_22(self):
        uuid = '415d116b-389c-44f0-bd08-d3ea14ea04de'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(2)):
                raise Exception('Click 2nd clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.click(L.edit.sub_tool.pan_zoom.custom.apply)
            if not self.click(L.edit.sub_tool.apply_to_all):
                raise Exception('Click apply_to_all fail')

            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Click 1st clip fail')
            self.page_edit.enter_sub_tool('Pan & Zoom')

            if self.element(find_string('Custom')).get_attribute('selected') == 'true':
                
                return "PASS"
            else:
                fail_log = '[Fail] Custom is not selected'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_23(self):
        uuid = '60936593-4d5b-4117-9626-a262d693e59e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(find_string('No Effect')):
                raise Exception('Click No Effect fail')
            self.page_edit.scroll_playhead_to_beginning()
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_video_default).full_compare_result():
                
                return "PASS"
            else:
                fail_log = '[Fail] Image are different'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_24(self):
        uuid = '88b811ec-fcb6-45f3-9480-27a7a68b9cdc'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            random_icon = self.element(xpath(f'//*[contains(@text,"Random")]/preceding-sibling::android.widget.ImageView'))
            if not random_icon:
                raise Exception("Cannot locate Random's icon")

            if random_icon.get_attribute('enabled') == 'false':
                
                return "PASS"
            else:
                fail_log = '[Fail] Random is not disabled'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Pan & Zoom')

            return "FAIL"

    def sce_2_2_25(self):
        uuid = '822282fc-0374-4534-90d5-902de4e2de66'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.driver.swipe_element(L.edit.sub_tool.pan_zoom.custom.start_position, 'up', 100)
            self.click(L.edit.sub_tool.pan_zoom.custom.apply)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)

            return "FAIL"

    def sce_2_2_26(self):
        uuid = '720154f9-f1e7-4e07-b01a-1b0fe8bcd216'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        
        log = 'Feature removed'
        
        return 'N/A'

    def sce_2_2_27(self):
        uuid = 'af2a4980-71b7-4181-a105-e978b380bb99'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        
        log = 'Feature removed'
        
        return 'N/A'

    def sce_2_2_28(self):
        uuid = '343072ee-7556-45fe-bc52-2a8889eed30c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        
        log = 'Feature removed'
        
        return 'N/A'

    def sce_2_2_31(self):
        uuid = '6cb4e483-d200-4a12-9ae1-14abc04f6d28'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Select clip fail')
            if not self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect'):
                raise Exception('Enter Effect fail')
            if not self.page_edit.click_tool_by_itemName('Beating'):
                raise Exception('Click Beating fail')
            if not self.click(L.edit.sub_tool.effect.edit):
                raise Exception('Click Edit button fail')
            if not self.click(find_string('Frequency')):
                raise Exception('Click Frequency fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "20":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_30(self):
        uuid = 'fe5e2f0d-ee84-43b7-9bba-1a27df66d71e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_32(self):
        uuid = '7cd0f6de-d928-4319-97f5-c2cb2e66ff7c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "5":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_29(self):
        uuid = '4260b495-a0f0-4ccb-81fc-d816bfd627c6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Frequency'))

            return "FAIL"

    def sce_2_2_33(self):
        uuid = 'b3da4cba-cbe8-49c6-8d1f-5df90e7bef60'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "40":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"

    def sce_2_2_34(self):
        uuid = 'ab490a99-98de-4070-9442-608fe225c520'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(find_string('Strength')):
                raise Exception('Click Strength fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "120":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"

    def sce_2_2_35(self):
        uuid = '094cff54-681b-43f6-9bdd-300857c70370'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "110":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"

    def sce_2_2_36(self):
        uuid = '00a7f2e5-8f0c-467c-a7ae-c4c718ba985b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "150":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Strength'))

            return "FAIL"

    def sce_2_2_39(self):
        uuid = '05fbc53e-aa2e-46ee-9942-3ac55343435d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Select clip fail')
            if not self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect'):
                raise Exception('Enter Effect fail')
            if not self.page_edit.click_tool_by_itemName('Bloom'):
                raise Exception('Click Bloom fail')
            if not self.click(L.edit.sub_tool.effect.edit):
                raise Exception('Click Edit button fail')
            if not self.click(find_string('Sample Weight')):
                raise Exception('Click Sample Weight fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "100":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Sample Weight'))

            return "FAIL"

    def sce_2_2_38(self):
        uuid = 'ef7c6f67-9c99-4092-93e3-cbc71daa8a32'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Sample Weight'))

            return "FAIL"

    def sce_2_2_40(self):
        uuid = '88eb60c0-199b-4009-aa12-b0a22b961669'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "0":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Sample Weight'))

            return "FAIL"

    def sce_2_2_37(self):
        uuid = 'ea4aa246-1530-4d35-a9fc-9c1e9a0104f1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Sample Weight'))

            return "FAIL"

    def sce_2_2_41(self):
        uuid = '524be4d9-98b2-4db8-903f-278778410326'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "200":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Sample Weight'))

            return "FAIL"

    def sce_2_2_42(self):
        uuid = 'f1061dea-2e58-4764-93dd-9c0b11a61066'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(find_string('Light Number')):
                raise Exception('Click Light Number fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "2":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Light Number'))

            return "FAIL"

    def sce_2_2_43(self):
        uuid = '756a3f0f-2f9e-4923-805b-76a0c9ea1ae3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "1":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Light Number'))

            return "FAIL"

    def sce_2_2_44(self):
        uuid = '07fc3b8d-eac6-4f29-980f-683fd687ab85'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "3":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Light Number'))

            return "FAIL"

    def sce_2_2_45(self):
        uuid = '5d72248a-f7fd-4a3f-a1c6-0ad31155c63f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.click(find_string('Angle')):
                raise Exception('Click Angle fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "50":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Angle'))

            return "FAIL"

    def sce_2_2_46(self):
        uuid = '6ba7a9de-597a-4c79-abf8-699dcf9a0986'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "0":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Angle'))

            return "FAIL"

    def sce_2_2_47(self):
        uuid = '2d933688-36c3-4b35-8ca8-d016b17dd005'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "200":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Angle'))

            return "FAIL"

    def sce_2_2_50(self):
        uuid = '1e96519a-d4e2-46e4-b954-f15bee0992cf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.tap_blank_space()
            if not self.click(L.edit.timeline.master_track.master_clip(1)):
                raise Exception('Select clip fail')
            if not self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect'):
                raise Exception('Enter Effect fail')
            if not self.page_edit.click_tool_by_itemName('Black & White'):
                raise Exception('Click Black & White fail')
            if not self.click(L.edit.sub_tool.effect.edit):
                raise Exception('Click Edit button fail')
            if not self.click(find_string('Degree')):
                raise Exception('Click Degree fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "200":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Black & White')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Degree'))

            return "FAIL"

    def sce_2_2_49(self):
        uuid = '338277ce-767a-4948-b34b-88d0e66186a3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Black & White')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Degree'))

            return "FAIL"

    def sce_2_2_51(self):
        uuid = 'b64a4b32-804d-45bf-a049-7e79d36e35fb'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "0":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Black & White')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Degree'))

            return "FAIL"

    def sce_2_2_48(self):
        uuid = 'ef54fa97-ccf7-4f9e-a0cc-78ef011ba1d2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Black & White')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Degree'))

            return "FAIL"

    def sce_2_2_52(self):
        uuid = '57cd0f6de-d928-4319-97f5-c2cb2e66ff7c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "200":
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Black & White')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Degree'))

            return "FAIL"

    def sce_2_2_53(self):
        uuid = '0a65b372-42de-4762-a678-d2f2b6951660'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min()

            if self.element(L.edit.sub_tool.slider_value).text != value:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not changed'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Black & White')
            self.click(L.edit.sub_tool.effect.edit)
            self.click(find_string('Degree'))

            return "FAIL"

    def sce_2_2_54(self):
        uuid = '561c6461-f8c4-49dd-89a2-7347d4a0d65b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            pic_src = self.page_main.get_preview_pic()
            self.driver.drag_slider_to_max()
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.timeline.master_track.master_clip(1))
            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_src).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_55(self):
        uuid = '77ed7370-d1b1-4c36-8159-02eaee850020'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        global pic_pip_effect
        try:
            self.page_edit.add_pip_media('Video', test_material_folder, video_9_16)
            self.click(L.edit.timeline.pip.pip_clip(1))

            pic_src = self.page_main.get_picture(L.edit.preview.pip_preview)
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            if not self.page_edit.click_tool_by_itemName('Bloom'):
                raise Exception('Click Bloom fail')


            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            if not HCompareImg(pic_pip_effect, pic_src).full_compare_result():
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media("Video", test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Bloom')
            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            return "FAIL"

    def sce_2_2_56(self):
        uuid = '071e7446-914c-4fce-ac7f-e6628bfc5408'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Sample Weight')):
                raise Exception('Click Sample Weight fail')
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_57(self):
        uuid = '1e3925fc-6203-458a-9932-b07ead0fa797'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        global pic_pip_effect
        try:
            self.page_edit.add_pip_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.pip.pip_clip(1))

            pic_src = self.page_main.get_picture(L.edit.preview.pip_preview)
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            if not self.page_edit.click_tool_by_itemName('Beating'):
                raise Exception('Click Beating fail')
            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            if not HCompareImg(pic_src, pic_pip_effect).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.pip.pip_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Beating')
            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            return "FAIL"

    def sce_2_2_58(self):
        uuid = '114a8820-25cb-45a4-9208-735db7a3690e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Strength')):
                raise Exception('Click Strength fail')
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_59(self):
        uuid = '5bc0675a-4b90-431c-98b1-37f79bb27f2a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        global pic_pip_effect
        try:
            self.page_edit.add_pip_colorboard(6)
            self.click(L.edit.timeline.pip.pip_clip())

            pic_src = self.page_main.get_picture(L.edit.preview.pip_preview)
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            if not self.page_edit.click_tool_by_itemName('Black & White'):
                raise Exception('Click Black & White fail')
            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            if not HCompareImg(pic_src, pic_pip_effect).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_pip_colorboard(6)
            self.click(L.edit.timeline.pip.pip_clip())
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Black & White')
            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            return "FAIL"

    def sce_2_2_60(self):
        uuid = '4df5c28e-3226-4f2b-8ac7-e1d3193bb76b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Degree')):
                raise Exception('Click Degree fail')
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_61(self):
        uuid = 'a0c6ea80-8f40-48ce-a82e-5e21813b6aa6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        global pic_pip_effect
        try:
            self.page_edit.enter_main_tool('Sticker')
            if not self.click(find_string("Add Sticker")):
                raise Exception('Enter Sticker fail')
            self.click(find_string("New"))
            if not self.click(L.edit.main_tool.sticker.item()):
                raise Exception('Click Sticker fail')

            timeout_flag = 1
            for i in range(60):
                if self.is_exist(L.edit.main_tool.sticker.library, 1):
                    continue
                else:
                    timeout_flag = 0
                    break
            if timeout_flag:
                raise Exception('Download sticker timeout')

            self.click(L.edit.timeline.pip.pip_clip(1))
            pic_src = self.page_main.get_picture(L.edit.preview.pip_preview)
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            if not self.page_edit.click_tool_by_itemName('Chinese Painting'):
                raise Exception('Click Chinese Painting fail')
            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            if not HCompareImg(pic_src, pic_pip_effect).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.enter_main_tool('Sticker')
            self.click(find_string("Add Sticker"))
            self.click(find_string("New"))
            self.click(L.edit.main_tool.sticker.item())
            for i in range(60):
                if self.is_exist(L.edit.main_tool.sticker.library, 1):
                    continue
                else:
                    timeout_flag = 0
                    break
            self.click(L.edit.timeline.pip.pip_clip(1))
            self.page_edit.enter_sub_tool('Effect', exclusive='AI Effect')
            self.page_edit.click_tool_by_itemName('Chinese Painting')
            pic_pip_effect = self.page_main.get_picture(L.edit.preview.pip_preview)

            return "FAIL"

    def sce_2_2_62(self):
        uuid = '0a20ef94-bb4d-4ff9-8cf6-12f2b5b03a57'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Detail')):
                raise Exception('Click Detail fail')
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_63(self):
        uuid = '31974a6e-b202-4b5e-b343-673a1abb8066'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.check_setting_image_duration(5.0)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.transition.tx_out(1))

            if self.is_exist(L.edit.timeline.master_track.transition.tx_list):
                
                return "PASS"
            else:
                fail_log = f'[Fail] transition_list is not exist'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.transition.tx_out(1))

            return "FAIL"

    def sce_2_2_64(self):
        uuid = '404da069-4c4b-4198-a492-745ebeb9dbc9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_edit.select_transition_from_bottom_menu('Cross')
            self.click(L.edit.timeline.master_track.transition.tx_out(1))
            self.click(L.edit.try_before_buy.try_it_first, 1)
            pic_src = self.page_main.get_preview_pic()
            self.click(L.edit.menu.play)
            time.sleep(1)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_src).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.transition.tx_out(1))
            self.page_edit.select_transition_from_bottom_menu('Cross')

            return "FAIL"

    def sce_2_2_65(self):
        uuid = '44a68076-a6b5-4e57-9fbe-27051750eae8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.timeline.master_track.transition.tx_out(2))
            none_border = (xpath('//*[contains(@text,"None")]/../../*[contains(@resource-id,"title_border")]'))

            if self.element(none_border).get_attribute("selected") == 'true':
                

                # sce_2_2_104
                self.report.start_uuid('d4a10596-a73a-4395-91b4-74a6e72dee7a')
                self.report.new_result('d4a10596-a73a-4395-91b4-74a6e72dee7a', True)

                return "PASS"
            else:
                fail_log = f'[Fail] 2nd transition None is not selected'
                

                # sce_2_2_104
                self.report.start_uuid('d4a10596-a73a-4395-91b4-74a6e72dee7a')
                self.report.new_result('d4a10596-a73a-4395-91b4-74a6e72dee7a', False)

                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.transition.tx_out(2))

            return "FAIL"

    def sce_2_2_66(self):
        uuid = '5aec562c-3df2-43a7-8099-2f0944997568'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            transition_amount = self.page_edit.calculate_transition_amount()

            if transition_amount >= 363:
                
                return "PASS"
            else:
                fail_log = f'[Fail] transition_amount is {transition_amount}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.transition.tx_out(1))
            self.page_edit.select_transition_from_bottom_menu('Cross')

            return "FAIL"

    def sce_2_2_103(self):
        uuid = '49437a84-cd81-4f47-8b2a-51e1b0ff0e73'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.timeline.master_track.transition.tx_out(1))
            self.page_edit.transition.set_duration(3.0, 1)
            self.click(L.edit.timeline.master_track.transition.tx_out(2))
            duration = self.element(L.edit.timeline.slider_value).text

            if duration == '3.0':
                
                return "PASS"
            else:
                fail_log = f'[Fail] Duration incorrect: {duration}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            return "FAIL"

    def sce_2_2_67(self):
        uuid = '255f3e69-7e80-4d64-ad07-b99646558dae'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Video', test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            if not self.page_edit.enter_sub_tool("Filter"):
                raise Exception('Enter Filter fail')

            self.pic_before_filter = self.page_main.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(3))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, self.pic_before_filter).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Video', test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool("Filter")
            pic_before_filter = self.page_main.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(3))

            return "FAIL"

    def sce_2_2_69(self):
        uuid = '11b755de-eaa4-4232-afe5-d09b6cca72f6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.driver.drag_slider_to_min():
                raise Exception('Drag slider fail')
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.menu.delete)

            if HCompareImg(pic_tgt, pic_before_filter).full_compare_result():
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are diff'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_68(self):
        uuid = '01576a37-c1e2-4ff0-8663-74387b5036ed'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        global pic_before_filter
        try:
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            if not self.page_edit.enter_sub_tool("Filter"):
                raise Exception('Enter Filter fail')

            pic_before_filter = self.page_main.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(3))
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_before_filter).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool("Filter")
            pic_before_filter = self.page_main.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(3))

            return "FAIL"

    def sce_2_2_70(self):
        uuid = '185dee12-1fe5-4fe1-a0a9-941d643e1212'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.driver.drag_slider_to_min():
                raise Exception('Drag slider fail')
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.menu.delete)

            if HCompareImg(pic_tgt, pic_before_filter).full_compare_result():
                
                return "PASS"
            else:
                fail_log = f'[Fail] Images are diff'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_73(self):
        uuid = '845d4a9d-6ec5-468d-8421-35cabc94d3f9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        global pic_default
        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            pic_default = self.page_main.get_preview_pic()
            if not self.page_edit.enter_sub_tool('Adjustment'):
                raise Exception('Enter Adjustment fail')
            if not self.page_edit.enter_sub_option_tool('Brightness'):
                raise Exception('Enter Brightness fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            pic_default = self.page_main.get_preview_pic()
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Brightness')

            return "FAIL"

    def sce_2_2_72(self):
        uuid = '3a8cde6e-6b62-42c4-89c5-fe4ae98647b8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Brightness')

            return "FAIL"

    def sce_2_2_74(self):
        uuid = '2ea6ab9e-71e4-48bd-ba43-b9cd2654efaf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "-100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Brightness')

            return "FAIL"

    def sce_2_2_71(self):
        uuid = '7808a09b-9f46-43b2-8e53-fde4bd1d05ff'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Brightness')

            return "FAIL"

    def sce_2_2_75(self):
        uuid = '8dc75ff8-4ef9-4fdd-9dbd-c113c112b494'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')

            return "FAIL"

    def sce_2_2_78(self):
        uuid = 'b8aedb47-bb52-43b9-8712-4cf7ded8a7cf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.enter_sub_option_tool('Contrast'):
                raise Exception('Enter Contrast fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Contrast')

            return "FAIL"

    def sce_2_2_77(self):
        uuid = '3160506b-92e6-4796-b463-461306d7cf68'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Contrast')

            return "FAIL"

    def sce_2_2_79(self):
        uuid = '35fa5496-30c2-4666-84d0-218fefa4e7ac'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "-100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Contrast')

            return "FAIL"

    def sce_2_2_76(self):
        uuid = '89e31121-4472-4f2f-ac47-47691b592cc9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Contrast')

            return "FAIL"

    def sce_2_2_80(self):
        uuid = '3bd8f601-e5c1-45c4-a7ce-5bce38299731'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')

            return "FAIL"

    def sce_2_2_83(self):
        uuid = 'e378c5c1-7131-42b2-ad7d-2d26bbe72a92'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.enter_sub_option_tool('Saturation'):
                raise Exception('Enter Saturation fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "100":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Saturation')

            return "FAIL"

    def sce_2_2_82(self):
        uuid = '0f159765-14b8-4a19-ae01-df132ecf41d9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Saturation')

            return "FAIL"

    def sce_2_2_84(self):
        uuid = 'fbd555b1-57a7-43a5-a3b0-ca17d8ca41f4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Saturation')

            return "FAIL"

    def sce_2_2_81(self):
        uuid = '7cc32cf8-d2e7-41a4-8d54-a79dde6b35a0'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Saturation')

            return "FAIL"

    def sce_2_2_85(self):
        uuid = '822f8f26-eab7-446d-af29-d7c65701e43c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "200":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')

            return "FAIL"

    def sce_2_2_88(self):
        uuid = '3be58560-ae77-40d9-b011-ff2d047f41dd'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.enter_sub_option_tool('Hue'):
                raise Exception('Enter Hue fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "100":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Hue')

            return "FAIL"

    def sce_2_2_87(self):
        uuid = 'ab7dc707-ef82-45fb-928c-f95721b0f36d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Hue')

            return "FAIL"

    def sce_2_2_89(self):
        uuid = '95c831a3-e9c6-4544-95fc-db8175aad502'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Hue')

            return "FAIL"

    def sce_2_2_86(self):
        uuid = 'c8ba369d-782a-40fc-ba3f-34f06f7299e7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Hue')

            return "FAIL"

    def sce_2_2_90(self):
        uuid = 'e06c1f1b-579e-40c0-9a30-11a115f220db'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "200":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')

            return "FAIL"

    def sce_2_2_93(self):
        uuid = '10d8d88d-aeac-4214-a5a5-511ff25e6ae0'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.enter_sub_option_tool('Temp'):
                raise Exception('Enter Temp fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "50":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Temp')

            return "FAIL"

    def sce_2_2_92(self):
        uuid = 'ab862a41-58ad-44a2-8087-b264278abbec'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Temp')

            return "FAIL"

    def sce_2_2_94(self):
        uuid = 'bc052e63-4c9f-4694-b4f0-638c8a3c11e3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Temp')

            return "FAIL"

    def sce_2_2_91(self):
        uuid = 'd5b5d9f5-3eef-42e2-bc06-a2a1abe8dee7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Temp')

            return "FAIL"

    def sce_2_2_95(self):
        uuid = '62b5c254-4771-4b6a-9b48-8ef2027c460b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')

            return "FAIL"

    def sce_2_2_98(self):
        uuid = '91d4fcee-d1fe-4bc6-93db-59a4d9236741'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.enter_sub_option_tool('Tint'):
                raise Exception('Enter Tint fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "50":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Tint')

            return "FAIL"

    def sce_2_2_97(self):
        uuid = '01f76d4e-1bb2-4308-9330-69b6444f4d58'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Tint')

            return "FAIL"

    def sce_2_2_99(self):
        uuid = 'e1275432-69eb-4980-87e7-9b4a6448bd7c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Tint')

            return "FAIL"

    def sce_2_2_96(self):
        uuid = 'b3aba4f2-aa2e-4328-9fe9-8a96a1ab9cb2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Tint')

            return "FAIL"

    def sce_2_2_100(self):
        uuid = '0487a29e-b1db-4037-a4b9-49925706a128'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')

            return "FAIL"

    def sce_2_2_101(self):
        uuid = 'f35c33a1-962c-475e-9f7f-0e18eed3e262'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.page_edit.enter_sub_option_tool('Sharpness'):
                raise Exception('Enter Sharpness fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Photo', test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            self.page_edit.enter_sub_tool('Adjustment')
            self.page_edit.enter_sub_option_tool('Sharpness')

            return "FAIL"

    def sce_2_2_102(self):
        uuid = '2f335a6a-e6b2-488b-9d0d-45de1be19d36'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                
                return "PASS"
            else:
                fail_log = f'[Fail] Preview no change'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_2_105(self):
        uuid = '5bd41804-74f8-4e9b-bff4-246537c0af45'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.edit.menu.full_screen)

            if self.is_exist(L.edit.preview.watermark):
                
                return "PASS"
            else:
                fail_log = f'[Fail] No watermark'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.menu.full_screen)

            return "FAIL"

    def sce_2_2_106(self):
        uuid = '3f81b17b-7ec0-463a-9423-acd1c8fad3ea'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.is_exist(L.edit.preview.fullscreen_timecode):
                self.click(L.edit.preview.movie_view)

            if self.is_exist(L.edit.preview.fullscreen_timecode):
                
                return "PASS"
            else:
                fail_log = f'[Fail] No fullscreen_timecode'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.menu.full_screen)

            return "FAIL"

    def sce_2_2_109(self):
        uuid = '1a3be899-15fd-4058-bc84-7e3a26dd7cad'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            if not self.is_exist(L.edit.preview.fullscreen_back):
                self.click(L.edit.preview.movie_view)
            self.click(L.edit.preview.fullscreen_back)

            if self.page_edit.back_to_launcher():
                
                return "PASS"
            else:
                fail_log = f'[Fail] Back to launcher fail'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"

    def sce_2_2_107(self):
        uuid = '6fbc941d-12c6-40ef-b1cd-000b035ee8b1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.menu.menu)
            self.page_edit.settings.swipe_to_option('FAQ & Send Feedback')
            self.click(find_string('FAQ & Send Feedback'))
            self.click(L.edit.settings.send_feedback.send_feedback_btn)

            if self.is_exist(L.edit.settings.send_feedback.feedback_text):
                
                return "PASS"
            else:
                fail_log = f'[Fail] No found feedback page'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.click(L.main.menu.menu)
            self.page_edit.settings.swipe_to_option('FAQ & Send Feedback')
            self.click(L.edit.settings.send_feedback.send_feedback_btn)

            return "FAIL"

    def sce_2_2_108(self):
        uuid = '225633cb-308a-4aaa-9ff6-fc1582084b5b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.element(L.edit.settings.send_feedback.feedback_text).send_keys('QA AT Testing')
            self.element(L.edit.settings.send_feedback.feedback_email).send_keys('qa@cyberlink.com')
            self.click(L.edit.settings.send_feedback.add_image)
            #
            self.click(xpath('//android.widget.TextView[@content-desc="Search"]'))
            self.element(xpath('//*[contains(@resource-id, "search_src_text")]')).send_keys("jpg")
            self.driver.driver.press_keycode(66)    # keycode 66: Enter
            time.sleep(2)
            self.click(xpath('//*[contains(@text,".jpg")]'))
            self.click(L.edit.settings.send_feedback.top_right_btn)
            model_name = self.element(L.edit.settings.send_feedback.feedback_device_model_text).text

            if model_name == "SM-A5360":
                
                return "PASS"
            else:
                fail_log = f'[Fail] model_name incorrect: {model_name}'
                
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            return "FAIL"


    def test_case_1(self):
        result = {"sce_2_2_1": self.sce_2_2_1(),
                  "sce_2_2_14": self.sce_2_2_14(),
                  "sce_2_2_12": self.sce_2_2_12(),
                  "sce_2_2_13": self.sce_2_2_13(),
                  "sce_2_2_15": self.sce_2_2_15(),
                  "sce_2_2_16": self.sce_2_2_16(),
                  "sce_2_2_17": self.sce_2_2_17(),
                  "sce_2_2_19": self.sce_2_2_19(),
                  "sce_2_2_18": self.sce_2_2_18(),
                  "sce_2_2_20": self.sce_2_2_20(),
                  "sce_2_2_21": self.sce_2_2_21(),
                  "sce_2_2_22": self.sce_2_2_22(),
                  "sce_2_2_23": self.sce_2_2_23(),
                  "sce_2_2_24": self.sce_2_2_24(),
                  "sce_2_2_25": self.sce_2_2_25(),
                  "sce_2_2_26": self.sce_2_2_26(),
                  "sce_2_2_27": self.sce_2_2_27(),
                  "sce_2_2_28": self.sce_2_2_28(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

    def test_case_3(self):
        result = {"sce_2_2_73": self.sce_2_2_73(),
                  "sce_2_2_72": self.sce_2_2_72(),
                  "sce_2_2_74": self.sce_2_2_74(),
                  "sce_2_2_71": self.sce_2_2_71(),
                  "sce_2_2_75": self.sce_2_2_75(),
                  "sce_2_2_78": self.sce_2_2_78(),
                  "sce_2_2_77": self.sce_2_2_77(),
                  "sce_2_2_79": self.sce_2_2_79(),
                  "sce_2_2_76": self.sce_2_2_76(),
                  "sce_2_2_80": self.sce_2_2_80(),
                  "sce_2_2_83": self.sce_2_2_83(),
                  "sce_2_2_82": self.sce_2_2_82(),
                  "sce_2_2_84": self.sce_2_2_84(),
                  "sce_2_2_81": self.sce_2_2_81(),
                  "sce_2_2_85": self.sce_2_2_85(),
                  "sce_2_2_88": self.sce_2_2_88(),
                  "sce_2_2_87": self.sce_2_2_87(),
                  "sce_2_2_89": self.sce_2_2_89(),
                  "sce_2_2_86": self.sce_2_2_86(),
                  "sce_2_2_90": self.sce_2_2_90(),
                  "sce_2_2_93": self.sce_2_2_93(),
                  "sce_2_2_92": self.sce_2_2_92(),
                  "sce_2_2_94": self.sce_2_2_94(),
                  "sce_2_2_91": self.sce_2_2_91(),
                  "sce_2_2_95": self.sce_2_2_95(),
                  "sce_2_2_98": self.sce_2_2_98(),
                  "sce_2_2_97": self.sce_2_2_97(),
                  "sce_2_2_99": self.sce_2_2_99(),
                  "sce_2_2_96": self.sce_2_2_96(),
                  "sce_2_2_100": self.sce_2_2_100(),
                  "sce_2_2_101": self.sce_2_2_101(),
                  "sce_2_2_102": self.sce_2_2_102(),
                  "sce_2_2_105": self.sce_2_2_105(),
                  "sce_2_2_106": self.sce_2_2_106(),
                  "sce_2_2_109": self.sce_2_2_109(),
                  # "sce_2_2_107": self.sce_2_2_107(),
                  # "sce_2_2_108": self.sce_2_2_108(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")


