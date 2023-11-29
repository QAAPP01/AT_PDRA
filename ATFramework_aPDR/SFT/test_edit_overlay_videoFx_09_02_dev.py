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

# global
preview_default = None
preview_before = None


class Test_Overlay_VideoFx:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = ["cb1c91c1-776f-42a0-a1a6-052cb1173dee",
                     "846938b4-00e3-414c-916b-b72c63499dee",
                     "fc233132-9a67-4570-ab6c-40284fa3f740",
                     "b34e7a84-3d66-4f3c-8bfb-10e4cf2f3023",
                     "32e0be3c-73fe-4c43-bf84-9b3fce0a46f3",
                     "00cd7722-e99c-45b0-8968-a6e085ea9b10",
                     "aa16b098-ea14-4014-a80e-5f059ee29830",
                     "66b7d54d-5931-4c3c-9185-adc8f46fe8c9",
                     "a670a893-c6c8-46de-aec3-62f5b64d31b8",
                     "b4eb177d-6903-44a1-a995-95c6559d4fab",
                     "48832739-592c-4621-8d9c-8485bc69a493",
                     "bb1c345e-2f79-468d-a803-f471b3df1deb",
                     "0a79095f-67f2-4106-8eb9-a173ddb47a72",
                     "c36c299e-0f00-486d-8bc9-bfff8b1cd249",
                     "d89fd8ad-706a-434f-9499-339af4f8648e",
                     "ce440a81-e3c8-4ec9-bff9-d6148e445f2a",
                     "234e280f-4652-4856-bdd6-64345ab45ee7",
                     "5cfcc8ed-ab54-4ef7-a9f5-f8008434a3bc",
                     "4b20ae55-6451-4d8c-8a8d-9a6352e2fc61",
                     "ec24f793-df7c-4c64-9a25-df4a77ad0f1d",
                     "fb143794-cde7-422b-aefb-2b6e5cd7a0b3",
                     "75384f9b-1c3a-474a-8b6b-4c77f59e0ce9",
                     "583d5ced-6c1d-4121-b724-0b80d6311917",
                     "ef70d371-d5fc-4b72-860e-2747a1a737f6",
                     "0103d9bd-7bcc-4097-b027-d737cf41b736",
                     "f3a12c04-66a6-4b80-b5e0-99dc08bcafbb",
                     "041f1252-87e3-46b5-be03-39a886faca72",
                     "7613a0b5-a34e-444e-8e16-154aca4b4fc2",
                     "abcfdeb1-ae2d-4995-8146-4503182c0d34",
                     "3cde6208-0c18-47e4-82b6-40c593f67fe8",
                     "89d0c81b-df0a-4154-b25d-56544b992c51",
                     "3724a9c7-f5bd-4080-8d4d-c1179ec06b76",
                     "74ceb53d-7fc3-4d82-a5d4-2040c470c1c5",
                     "7d0cb762-4a1e-473f-b5db-763b609a451b",
                     "b2fdfb6d-4d84-428a-bfb1-8cf28c9da064",
                     "62349d84-abe7-489f-bc6c-58d593b9ddb5",
                     "f889659c-2851-4125-8b8f-360bd84e7509",
                     "4d789278-c342-48e7-bfa5-20eca39dfdcd",
                     "1522c5bc-9b50-4e9b-9f4c-a1eac083b155",
                     "f52523bc-1ee8-412d-a728-6d687852422d",
                     "a81e4e57-b9fb-4771-a4a5-028e44ed9238",
                     "bbddcfce-73e0-46a8-b8fd-054180896def",
                     "653bca97-ebda-4885-af75-cbb1db5a4914",
                     "bf137995-cafd-4d85-9693-cb659559f38c",
                     "5628b1ad-e4c1-4fb9-bc22-d07ff740525e",
                     "5e55f715-2ccd-4a14-a17a-8d547ca30e88",
                     "eb7f7dff-43c8-4af4-852f-4469601bf3c9",
                     "ebc9e47e-cf49-461e-901c-5a9ec817c928",
                     "f5ae40cd-8685-41b6-b098-4e1f0caafc55",
                     "0265fcc0-0f4c-47c5-a300-80819b092bfd",
                     "bf4279be-0bc1-404c-9d18-7d8903264e79",
                     "45f9bc4c-1c98-4511-8e66-bdc00e0a657e",
                     "cc07e1cf-f3d4-4c95-8c74-c8891dde8f32",
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
        driver.driver.close_app()

    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')

    def sce_9_2_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)

            if self.is_exist(L.edit.fx_layer.videoFx.item()):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the Effect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)

            return "FAIL"

    def sce_9_2_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')

            if self.is_exist(L.edit.fx_layer.videoFx.item()):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the Effect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            return "FAIL"

    def sce_9_2_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.preview_original = self.page_main.get_preview_pic()
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            value = self.element(L.edit.fx_layer.videoFx.value(1)).text

            if value == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.preview_original = self.page_main.get_preview_pic()
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(1))
            value = self.element(L.edit.fx_layer.videoFx.value(1)).text

            if value == '0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(1))

            return "FAIL"

    def sce_9_2_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(1))
            value = self.element(L.edit.fx_layer.videoFx.value(1)).text

            if value == '100':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(1))

            return "FAIL"

    def sce_9_2_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            value = self.element(L.edit.fx_layer.videoFx.value(2)).text

            if value == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(2))
            value = self.element(L.edit.fx_layer.videoFx.value(2)).text

            if value == '0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(2))

            return "FAIL"

    def sce_9_2_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(2))
            value = self.element(L.edit.fx_layer.videoFx.value(2)).text

            if value == '100':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(2))

            return "FAIL"

    def sce_9_2_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.fx_layer.videoFx.reset)

            value_1 = self.element(L.edit.fx_layer.videoFx.value(1)).text
            value_2 = self.element(L.edit.fx_layer.videoFx.value(2)).text

            if value_1 == '50' and value_2 == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value_1}, {value_2}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.fx_layer.videoFx.back)

            if self.is_exist(L.edit.fx_layer.videoFx.item()):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] No found effect list')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.enter_main_tool('Video Effects')
            self.click(L.edit.fx_layer.videoFx.item_name('Bump'))
            self.page_edit.try_it_first()

            return "FAIL"

    def sce_9_2_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.click(L.edit.fx_layer.videoFx.edit)
            value = self.element(L.edit.fx_layer.videoFx.value(1)).text

            if value == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(1))
            value = self.element(L.edit.fx_layer.videoFx.value(1)).text

            if value == '0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(1))

            return "FAIL"

    def sce_9_2_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(1))
            value = self.element(L.edit.fx_layer.videoFx.value(1)).text

            if value == '100':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(1))

            return "FAIL"

    def sce_9_2_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            value = self.element(L.edit.fx_layer.videoFx.value(2)).text

            if value == '50':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(2))
            value = self.element(L.edit.fx_layer.videoFx.value(2)).text

            if value == '0':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_min(L.edit.fx_layer.videoFx.slider(2))

            return "FAIL"

    def sce_9_2_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def sce_9_2_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(2))
            value = self.element(L.edit.fx_layer.videoFx.value(2)).text

            if value == '100':
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {value}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)
            self.driver.drag_slider_to_max(L.edit.fx_layer.videoFx.slider(2))

            return "FAIL"

    def sce_9_2_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            preview = self.page_main.get_preview_pic()

            if not HCompareImg(preview, self.preview_original).full_compare() == 1:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview no change')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_main_tool('FX Layer')
            self.click(find_string('Video Effect'))
            self.click(L.edit.fx_layer.add)
            self.click(L.edit.fx_layer.filter.cancel)
            self.page_edit.click_category('Blur', L.edit.fx_layer.videoFx.category(0))
            self.page_edit.click_effect("Vague", L.edit.fx_layer.videoFx.item_name(0))
            self.page_edit.try_it_first()
            self.click(L.edit.fx_layer.videoFx.edit)

            return "FAIL"

    def test_case(self):
        result = {"sce_9_2_1": self.sce_9_2_1(),
                  "sce_9_2_2": self.sce_9_2_2(),
                  "sce_9_2_3": self.sce_9_2_3(),
                  "sce_9_2_4": self.sce_9_2_4(),
                  "sce_9_2_5": self.sce_9_2_5(),
                  "sce_9_2_6": self.sce_9_2_6(),
                  "sce_9_2_7": self.sce_9_2_7(),
                  "sce_9_2_8": self.sce_9_2_8(),
                  "sce_9_2_9": self.sce_9_2_9(),
                  "sce_9_2_10": self.sce_9_2_10(),
                  "sce_9_2_11": self.sce_9_2_11(),
                  "sce_9_2_12": self.sce_9_2_12(),
                  "sce_9_2_13": self.sce_9_2_13(),
                  "sce_9_2_14": self.sce_9_2_14(),
                  "sce_9_2_15": self.sce_9_2_15(),
                  "sce_9_2_16": self.sce_9_2_16(),
                  "sce_9_2_17": self.sce_9_2_17(),
                  "sce_9_2_18": self.sce_9_2_18(),
                  "sce_9_2_19": self.sce_9_2_19(),
                  "sce_9_2_20": self.sce_9_2_20(),
                  "sce_9_2_21": self.sce_9_2_21(),
                  "sce_9_2_22": self.sce_9_2_22(),
                  "sce_9_2_23": self.sce_9_2_23(),
                  "sce_9_2_24": self.sce_9_2_24(),

                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
