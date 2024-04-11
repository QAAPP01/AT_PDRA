import pytest, inspect, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'

default_prompt = "English description only\n(Example: cute cat, hand-drawn, 2D, Flat background)"


class Test_SFT_Scenario_02_35:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report

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

        self.report.set_driver(driver)
        driver.driver.launch_app()
        yield
        driver.driver.close_app()

    def sce_2_35_1(self):
        uuid = '81350160-05b8-4fa1-ac6d-cde4bb662ef4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            if self.page_edit.sticker.ai_sticker.enter_ai_sticker():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Enter AI Sticker fail'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.sticker.ai_sticker.enter_ai_sticker()

            return "FAIL"

    def sce_2_35_2(self):
        uuid = '046bbb9d-cb11-4db6-b710-22dbe9f23dce'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            text = self.element(L.edit.main_tool.sticker.ai_sticker.prompt_entry).text

            if text == default_prompt:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Default text incorrect: {text}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.sticker.ai_sticker.enter_ai_sticker()

            return "FAIL"

    def sce_2_35_3(self):
        uuid = '135b5f8e-f5b9-4831-83fb-f7bd3b30b82d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            total = self.element(L.edit.main_tool.sticker.ai_sticker.count_total).text.split("/")[1]
            total = int(total)
            text = 'x' * (total + 1)
            self.element(L.edit.main_tool.sticker.ai_sticker.prompt_entry).send_keys(text)
            count = self.element(L.edit.main_tool.sticker.ai_sticker.count).text

            if int(count) == total + 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Count incorrect: {count}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.sticker.ai_sticker.enter_ai_sticker()
            self.element(L.edit.main_tool.sticker.ai_sticker.prompt_entry).send_keys('x'*801)

            return "FAIL"

    def sce_2_35_4(self):
        uuid = '612fea65-4627-4cbe-badf-dd325058d0e9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.element(L.edit.main_tool.sticker.ai_sticker.gen_btn).get_attribute('enabled') == 'false':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Generate btn is not disabled'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.sticker.ai_sticker.enter_ai_sticker()
            self.element(L.edit.main_tool.sticker.ai_sticker.prompt_entry).send_keys('x'*801)

            return "FAIL"

    def sce_2_35_5(self):
        uuid = '7387191c-7e85-4ef5-adff-6c81366c0ecf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.main_tool.sticker.ai_sticker.clear)
            text = self.element(L.edit.main_tool.sticker.ai_sticker.prompt_entry).text

            if text == default_prompt:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Text is not cleared: {text}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)
        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.sticker.ai_sticker.enter_ai_sticker()

            return "FAIL"

    def sce_2_35_6(self):
        uuid = 'efb60ced-e009-46de-bda0-a85455a48051'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.element(L.edit.main_tool.sticker.ai_sticker.clear).get_attribute('enabled') == 'false':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Clear btn is not disabled'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.sticker.ai_sticker.enter_ai_sticker()

            return "FAIL"

    def sce_2_35_7(self):
        uuid = '94160082-befc-48fb-b346-1e8a269becfa'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            selected_xpath = xpath('//*[contains(@id,"view_is_selected")]/../*[contains(@id,"tv_name")]')
            selected_style = self.element(selected_xpath).text

            if selected_style == "None":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] selected_style is not "None": {selected_style}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.sticker.ai_sticker.enter_ai_sticker()

            return "FAIL"

    def sce_2_35_9(self):
        uuid = 'b1842e2f-85e1-4733-b66a-e9e9a2709f43'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.sub_tool.ai_effect.reset):
                raise Exception('Click Reset fail')

            if self.element(L.edit.sub_tool.ai_effect.param_value(default_value[0])).text == default_value[1]:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Param value is not equal default value'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_10(self):
        uuid = 'aa3241e2-63f4-4e06-b722-d3c751c0aefe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.sub_tool.back):
                raise Exception('Click Back fail')

            if self.is_exist(L.edit.sub_tool.ai_effect.effect()):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No found effect'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_11(self):
        uuid = '9bd61e1e-f41a-4e72-8c8e-0060a3c86afe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(L.edit.sub_tool.back):
                raise Exception('Tap Back button fail')

            if self.is_exist(L.edit.sub_tool.tool(0)):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No found 2nd layer tool menu'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            return "FAIL"

    def sce_2_35_14(self):
        uuid = '7eb3f4d4-b6a0-464c-a046-3859f69557b5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_12(self):
        uuid = '6adefecd-8cbd-4164-aa84-9dd4bd06577e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No Effect is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_13(self):
        uuid = 'd49362dd-6d87-4c27-8d5f-785749caeef2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_15(self):
        uuid = '4411db3a-3fdc-461c-930f-793ab72b45a2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Custom is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_16(self):
        uuid = '80556c5f-b177-455d-bade-d46c0fa34195'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.scroll_playhead_to_beginning()
            if not self.click(find_string('No Effect')):
                raise Exception('Click No Effect fail')
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are different'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_17(self):
        uuid = 'adc2ccca-482d-4eb7-ac83-5bf5d4de19b7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Random')):
                raise Exception('Click Random fail')
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_19(self):
        uuid = '1b938b47-d9e3-43db-bc7f-93deba4de02f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.driver.swipe_element(L.edit.sub_tool.pan_zoom.custom.start_position, 'up', 100)
            self.click(L.edit.sub_tool.pan_zoom.custom.apply)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_18(self):
        uuid = '2fd0c8b8-59d5-4986-ad84-405637852a86'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:

            if not self.page_edit.trigger_default_pan_zoom_effect(enable=False):
                raise Exception('Disable Pan & Zoom Fail')
            self.page_edit.scroll_playhead_to_beginning()
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_20(self):
        uuid = '4a4ad790-5b78-4831-a156-315877f42bb8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] No Effect is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_21(self):
        uuid = '5a6815e0-1ac5-48b2-a582-567ebace8f71'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            random_icon = self.element(xpath(f'//*[contains(@text,"Random")]/preceding-sibling::android.widget.ImageView'))
            if not random_icon:
                raise Exception("Cannot locate Random's icon")

            if random_icon.get_attribute('enabled') == 'false':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not disabled'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_22(self):
        uuid = '415d116b-389c-44f0-bd08-d3ea14ea04de'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Custom is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_23(self):
        uuid = '60936593-4d5b-4117-9626-a262d693e59e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('No Effect')):
                raise Exception('Click No Effect fail')
            self.page_edit.scroll_playhead_to_beginning()
            pic_tgt = self.page_main.get_preview_pic()

            if HCompareImg(pic_tgt, pic_video_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are different'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_24(self):
        uuid = '88b811ec-fcb6-45f3-9480-27a7a68b9cdc'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            random_icon = self.element(xpath(f'//*[contains(@text,"Random")]/preceding-sibling::android.widget.ImageView'))
            if not random_icon:
                raise Exception("Cannot locate Random's icon")

            if random_icon.get_attribute('enabled') == 'false':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Random is not disabled'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_25(self):
        uuid = '822282fc-0374-4534-90d5-902de4e2de66'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Custom')):
                raise Exception('Click Custom fail')
            self.driver.swipe_element(L.edit.sub_tool.pan_zoom.custom.start_position, 'up', 100)
            self.click(L.edit.sub_tool.pan_zoom.custom.apply)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_photo_default).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = '[Fail] Image are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_26(self):
        uuid = '720154f9-f1e7-4e07-b01a-1b0fe8bcd216'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)
        log = 'Feature removed'
        self.report.new_result(uuid, None, 'N/A', log)
        return 'N/A'

    def sce_2_35_27(self):
        uuid = 'af2a4980-71b7-4181-a105-e978b380bb99'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)
        log = 'Feature removed'
        self.report.new_result(uuid, None, 'N/A', log)
        return 'N/A'

    def sce_2_35_28(self):
        uuid = '343072ee-7556-45fe-bc52-2a8889eed30c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)
        log = 'Feature removed'
        self.report.new_result(uuid, None, 'N/A', log)
        return 'N/A'

    def sce_2_35_31(self):
        uuid = '6cb4e483-d200-4a12-9ae1-14abc04f6d28'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_30(self):
        uuid = 'fe5e2f0d-ee84-43b7-9bba-1a27df66d71e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_32(self):
        uuid = '7cd0f6de-d928-4319-97f5-c2cb2e66ff7c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "5":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_29(self):
        uuid = '4260b495-a0f0-4ccb-81fc-d816bfd627c6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_33(self):
        uuid = 'b3da4cba-cbe8-49c6-8d1f-5df90e7bef60'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "40":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_34(self):
        uuid = 'ab490a99-98de-4070-9442-608fe225c520'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Strength')):
                raise Exception('Click Strength fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "120":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_35(self):
        uuid = '094cff54-681b-43f6-9bdd-300857c70370'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "110":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_36(self):
        uuid = '00a7f2e5-8f0c-467c-a7ae-c4c718ba985b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "150":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_39(self):
        uuid = '05fbc53e-aa2e-46ee-9942-3ac55343435d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_38(self):
        uuid = 'ef7c6f67-9c99-4092-93e3-cbc71daa8a32'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_40(self):
        uuid = '88eb60c0-199b-4009-aa12-b0a22b961669'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "0":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_37(self):
        uuid = 'ea4aa246-1530-4d35-a9fc-9c1e9a0104f1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_41(self):
        uuid = '524be4d9-98b2-4db8-903f-278778410326'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "200":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_42(self):
        uuid = 'f1061dea-2e58-4764-93dd-9c0b11a61066'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Light Number')):
                raise Exception('Click Light Number fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "2":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_43(self):
        uuid = '756a3f0f-2f9e-4923-805b-76a0c9ea1ae3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "1":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_44(self):
        uuid = '07fc3b8d-eac6-4f29-980f-683fd687ab85'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "3":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_45(self):
        uuid = '5d72248a-f7fd-4a3f-a1c6-0ad31155c63f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.click(find_string('Angle')):
                raise Exception('Click Angle fail')
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "50":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_46(self):
        uuid = '6ba7a9de-597a-4c79-abf8-699dcf9a0986'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "0":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_47(self):
        uuid = '2d933688-36c3-4b35-8ca8-d016b17dd005'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "200":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_50(self):
        uuid = '1e96519a-d4e2-46e4-b954-f15bee0992cf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_49(self):
        uuid = '338277ce-767a-4948-b34b-88d0e66186a3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_51(self):
        uuid = 'b64a4b32-804d-45bf-a049-7e79d36e35fb'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "0":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_48(self):
        uuid = 'ef54fa97-ccf7-4f9e-a0cc-78ef011ba1d2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_52(self):
        uuid = '57cd0f6de-d928-4319-97f5-c2cb2e66ff7c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text

            if value == "200":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_53(self):
        uuid = '0a65b372-42de-4762-a678-d2f2b6951660'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min()

            if self.element(L.edit.sub_tool.slider_value).text != value:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not changed'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_54(self):
        uuid = '561c6461-f8c4-49dd-89a2-7347d4a0d65b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            pic_src = self.page_main.get_preview_pic()
            self.driver.drag_slider_to_max()
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.timeline.master_track.master_clip(1))
            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_src).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_55(self):
        uuid = '77ed7370-d1b1-4c36-8159-02eaee850020'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_56(self):
        uuid = '071e7446-914c-4fce-ac7f-e6628bfc5408'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Sample Weight')):
                raise Exception('Click Sample Weight fail')
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_57(self):
        uuid = '1e3925fc-6203-458a-9932-b07ead0fa797'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_58(self):
        uuid = '114a8820-25cb-45a4-9208-735db7a3690e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Strength')):
                raise Exception('Click Strength fail')
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_59(self):
        uuid = '5bc0675a-4b90-431c-98b1-37f79bb27f2a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_60(self):
        uuid = '4df5c28e-3226-4f2b-8ac7-e1d3193bb76b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Degree')):
                raise Exception('Click Degree fail')
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_61(self):
        uuid = 'a0c6ea80-8f40-48ce-a82e-5e21813b6aa6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_62(self):
        uuid = '0a20ef94-bb4d-4ff9-8cf6-12f2b5b03a57'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.effect.edit)
            if not self.click(find_string('Detail')):
                raise Exception('Click Detail fail')
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_picture(L.edit.preview.pip_preview)

            self.click(L.edit.menu.delete)

            if not HCompareImg(pic_tgt, pic_pip_effect).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_63(self):
        uuid = '31974a6e-b202-4b5e-b343-673a1abb8066'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.check_setting_image_duration(5.0)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.page_edit.add_master_media("Photo", test_material_folder, photo_9_16)
            self.click(L.edit.timeline.master_track.transition.tx_out(1))

            if self.is_exist(L.edit.timeline.master_track.transition.tx_list):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] transition_list is not exist'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_64(self):
        uuid = '404da069-4c4b-4198-a492-745ebeb9dbc9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.select_transition_from_bottom_menu('Cross')
            self.click(L.edit.timeline.master_track.transition.tx_out(1))
            pic_src = self.page_main.get_preview_pic()
            self.click(L.edit.menu.play)
            time.sleep(1)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_src).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_65(self):
        uuid = '44a68076-a6b5-4e57-9fbe-27051750eae8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.timeline.master_track.transition.tx_out(2))
            none_border = (xpath('//*[contains(@text,"None")]/../../*[contains(@resource-id,"title_border")]'))

            if self.element(none_border).get_attribute("selected") == 'true':
                self.report.new_result(uuid, True)

                # sce_2_35_104
                self.report.start_uuid('d4a10596-a73a-4395-91b4-74a6e72dee7a')
                self.report.new_result('d4a10596-a73a-4395-91b4-74a6e72dee7a', True)

                return "PASS"
            else:
                fail_log = f'[Fail] 2nd transition None is not selected'
                self.report.new_result(uuid, False, fail_log=fail_log)

                # sce_2_35_104
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

    def sce_2_35_66(self):
        uuid = '5aec562c-3df2-43a7-8099-2f0944997568'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            transition_amount = self.page_edit.calculate_transition_amount()

            if transition_amount == 358:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] transition_amount is {transition_amount}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_103(self):
        uuid = '49437a84-cd81-4f47-8b2a-51e1b0ff0e73'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.timeline.master_track.transition.tx_out(1))
            self.page_edit.transition.set_duration(3.0, 1)
            self.click(L.edit.timeline.master_track.transition.tx_out(2))
            duration = self.element(L.edit.timeline.slider_value).text

            if duration == '3.0':
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Duration incorrect: {duration}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            return "FAIL"

    def sce_2_35_67(self):
        uuid = ''
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        global pic_before_filter
        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('Video', test_material_folder, video_9_16)
            self.click(L.edit.timeline.master_track.master_clip(1))
            if not self.page_edit.enter_sub_tool("Filter"):
                raise Exception('Enter Filter fail')

            pic_before_filter = self.page_main.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(3))
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_before_filter).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_69(self):
        uuid = '11b755de-eaa4-4232-afe5-d09b6cca72f6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.driver.drag_slider_to_min():
                raise Exception('Drag slider fail')
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.menu.delete)

            if HCompareImg(pic_tgt, pic_before_filter).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are diff'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_68(self):
        uuid = '01576a37-c1e2-4ff0-8663-74387b5036ed'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

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
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are the same'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_70(self):
        uuid = '185dee12-1fe5-4fe1-a0a9-941d643e1212'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.driver.drag_slider_to_min():
                raise Exception('Drag slider fail')
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.menu.delete)

            if HCompareImg(pic_tgt, pic_before_filter).full_compare_result():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Images are diff'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_73(self):
        uuid = '845d4a9d-6ec5-468d-8421-35cabc94d3f9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        global pic_default
        try:
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
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_72(self):
        uuid = '3a8cde6e-6b62-42c4-89c5-fe4ae98647b8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_74(self):
        uuid = '2ea6ab9e-71e4-48bd-ba43-b9cd2654efaf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "-100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_71(self):
        uuid = '7808a09b-9f46-43b2-8e53-fde4bd1d05ff'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_75(self):
        uuid = '8dc75ff8-4ef9-4fdd-9dbd-c113c112b494'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_78(self):
        uuid = 'b8aedb47-bb52-43b9-8712-4cf7ded8a7cf'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_option_tool('Contrast'):
                raise Exception('Enter Contrast fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_77(self):
        uuid = '3160506b-92e6-4796-b463-461306d7cf68'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_79(self):
        uuid = '35fa5496-30c2-4666-84d0-218fefa4e7ac'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "-100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_76(self):
        uuid = '89e31121-4472-4f2f-ac47-47691b592cc9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_80(self):
        uuid = '3bd8f601-e5c1-45c4-a7ce-5bce38299731'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_83(self):
        uuid = 'e378c5c1-7131-42b2-ad7d-2d26bbe72a92'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_option_tool('Saturation'):
                raise Exception('Enter Saturation fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "100":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_82(self):
        uuid = '0f159765-14b8-4a19-ae01-df132ecf41d9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_84(self):
        uuid = 'fbd555b1-57a7-43a5-a3b0-ca17d8ca41f4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_81(self):
        uuid = '7cc32cf8-d2e7-41a4-8d54-a79dde6b35a0'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_85(self):
        uuid = '822f8f26-eab7-446d-af29-d7c65701e43c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "200":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_88(self):
        uuid = '3be58560-ae77-40d9-b011-ff2d047f41dd'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_option_tool('Hue'):
                raise Exception('Enter Hue fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "100":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_87(self):
        uuid = 'ab7dc707-ef82-45fb-928c-f95721b0f36d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_89(self):
        uuid = '95c831a3-e9c6-4544-95fc-db8175aad502'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_86(self):
        uuid = 'c8ba369d-782a-40fc-ba3f-34f06f7299e7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_90(self):
        uuid = 'e06c1f1b-579e-40c0-9a30-11a115f220db'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "200":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_93(self):
        uuid = '10d8d88d-aeac-4214-a5a5-511ff25e6ae0'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_option_tool('Temp'):
                raise Exception('Enter Temp fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "50":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_92(self):
        uuid = 'ab862a41-58ad-44a2-8087-b264278abbec'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_94(self):
        uuid = 'bc052e63-4c9f-4694-b4f0-638c8a3c11e3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_91(self):
        uuid = 'd5b5d9f5-3eef-42e2-bc06-a2a1abe8dee7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_95(self):
        uuid = '62b5c254-4771-4b6a-9b48-8ef2027c460b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_98(self):
        uuid = '91d4fcee-d1fe-4bc6-93db-59a4d9236741'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_option_tool('Tint'):
                raise Exception('Enter Tint fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "50":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_97(self):
        uuid = '01f76d4e-1bb2-4308-9330-69b6444f4d58'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_min(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) < int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not decreased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_99(self):
        uuid = 'e1275432-69eb-4980-87e7-9b4a6448bd7c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_96(self):
        uuid = 'b3aba4f2-aa2e-4328-9fe9-8a96a1ab9cb2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value_before = self.element(L.edit.sub_tool.slider_value).text
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            value_after = self.element(L.edit.sub_tool.slider_value).text

            if int(value_after) > int(value_before):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Value is not increased'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_100(self):
        uuid = '0487a29e-b1db-4037-a4b9-49925706a128'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            self.click(L.edit.sub_tool.reset)

            if value == "100":
                if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview no change'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_101(self):
        uuid = 'f35c33a1-962c-475e-9f7f-0e18eed3e262'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.page_edit.enter_sub_option_tool('Sharpness'):
                raise Exception('Enter Sharpness fail')
            value = self.element(L.edit.sub_tool.slider_value).text
            pic_tgt = self.page_main.get_preview_pic()

            if value == "0":
                if HCompareImg(pic_tgt, pic_default).full_compare_result():
                    self.report.new_result(uuid, True)
                    return "PASS"
                else:
                    fail_log = f'[Fail] Preview is changed'
                    self.report.new_result(uuid, False, fail_log=fail_log)
                    raise Exception(fail_log)
            else:
                fail_log = f'[Fail] Value incorrect: {value}'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_102(self):
        uuid = '2f335a6a-e6b2-488b-9d0d-45de1be19d36'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.sub_tool.slider)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_default).full_compare() == 1:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Preview no change'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_2_35_105(self):
        uuid = '5bd41804-74f8-4e9b-bff4-246537c0af45'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.menu.full_screen)

            if self.is_exist(L.edit.preview.watermark):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] No watermark'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.menu.full_screen)

            return "FAIL"

    def sce_2_35_106(self):
        uuid = '3f81b17b-7ec0-463a-9423-acd1c8fad3ea'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.is_exist(L.edit.preview.fullscreen_timecode):
                self.click(L.edit.preview.movie_view)

            if self.is_exist(L.edit.preview.fullscreen_timecode):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] No fullscreen_timecode'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.click(L.edit.menu.full_screen)

            return "FAIL"

    def sce_2_35_109(self):
        uuid = '1a3be899-15fd-4058-bc84-7e3a26dd7cad'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if not self.is_exist(L.edit.preview.fullscreen_back):
                self.click(L.edit.preview.movie_view)
            self.click(L.edit.preview.fullscreen_back)

            if self.page_edit.back_to_launcher():
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] Back to launcher fail'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            return "FAIL"

    def sce_2_35_107(self):
        uuid = '6fbc941d-12c6-40ef-b1cd-000b035ee8b1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.menu.menu)
            self.page_edit.settings.swipe_to_option('FAQ & Send Feedback')
            self.click(find_string('FAQ & Send Feedback'))
            self.click(L.edit.settings.send_feedback.send_feedback_btn)

            if self.is_exist(L.edit.settings.send_feedback.feedback_text):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] No found feedback page'
                self.report.new_result(uuid, False, fail_log=fail_log)
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

    def sce_2_35_108(self):
        uuid = '225633cb-308a-4aaa-9ff6-fc1582084b5b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.element(L.edit.settings.send_feedback.feedback_text).send_keys('QA AT Testing')
            self.element(L.edit.settings.send_feedback.feedback_email).send_keys('qa@cyberlink.com')
            self.click(L.edit.settings.send_feedback.add_image)
            self.click(xpath('//android.widget.TextView[@content-desc="Search"]'))
            self.element(xpath('//*[contains(@resource-id, "search_src_text")]')).send_keys("jpg")
            self.driver.driver.press_keycode(66)    # keycode 66: Enter
            time.sleep(2)
            self.click(xpath('//*[contains(@text,".jpg")]'))
            self.click(L.edit.settings.send_feedback.top_right_btn)
            model_name = self.element(L.edit.settings.send_feedback.feedback_device_model_text).text

            if model_name == "SM-A5360":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                fail_log = f'[Fail] model_name incorrect: {model_name}'
                self.report.new_result(uuid, False, fail_log=fail_log)
                raise Exception(fail_log)

        except Exception as err:
            logger(f'\n{err}')

            return "FAIL"


    def test_case_1(self):
        result = {"sce_2_35_1": self.sce_2_35_1(),
                  "sce_2_35_2": self.sce_2_35_2(),
                  "sce_2_35_3": self.sce_2_35_3(),
                  "sce_2_35_4": self.sce_2_35_4(),
                  "sce_2_35_5": self.sce_2_35_5(),
                  "sce_2_35_6": self.sce_2_35_6(),
                  "sce_2_35_7": self.sce_2_35_7(),
                  # "sce_2_35_8": self.sce_2_35_8(),
                  # "sce_2_35_9": self.sce_2_35_9(),
                  # "sce_2_35_10": self.sce_2_35_10(),
                  # "sce_2_35_11": self.sce_2_35_11(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

