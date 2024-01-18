import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from selenium.webdriver import ActionChains

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


class Test_Class:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "d76b079d-4471-4094-8fac-e1e1708be8ee",
            "75e82855-966c-4fe2-b6c1-08a72fec64ec",
            "95ec2d1f-8287-44ce-931b-b7b63e71d44b",
            "c4d67802-cd55-40fc-a872-074b88dcb784",
            "08cbe216-8216-44c0-88f9-5bb5658cb0ef",
            "14262656-328d-48e1-9378-d39a2334bcd0",
            "6fb66eaa-8fc2-4121-af48-d4b71c9d1b4d",
            "5340d758-acdf-4df9-8408-428870f96e65",
            "fb00dd50-2ba9-4f6f-9348-b61249a1059c",
            "317a2c25-ce74-4e96-8d78-b401c9c408b6",
            "f3bb6850-a539-424f-a30a-4516c383861a",
            "c23308e4-103b-4379-a6d7-6c5c8aa7fe0f",
            "52666d61-b418-4594-a12e-f20df2f9f6cb",
            "ab3add8f-35a8-4ca7-a360-646c4ce9f601",
            "24bc6212-125b-4068-8b26-4aa9d2500a42",
            "9399c70c-a4b4-4479-a601-2a155ebb9f42",
            "ce7db935-b95f-42d5-b588-4494da4ac88f",
            "cb57c72d-2891-4694-b643-b6047083a890",
            "d8e19314-0b7a-4fd5-852a-46e29b4529e2",
            "77f01721-7557-4787-b6f0-2e3453c7d782",
            "7e9a4cb8-aa76-4181-ad36-326b58f5cdbc",
            "84a3be23-3941-4e93-834a-d292bd468001",
            "fde067b8-4c9d-413a-a7da-6b1909eb3ebf",
            "170e68cc-fb66-49ef-9fb5-2c2c161e8c00",
            "5af07b7f-659b-4a27-b288-a59d5cfc6bac",
            "67095f4f-ef1f-480d-aa90-c9adb60892f2",
            "0ee4f768-9e64-4e0e-b738-a25cf5c33b89",
            "0686ba98-f5c0-4b56-bd23-325a4e37b787"
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

    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='medium', video_fps=30)

    def sce_7_7_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)

            if self.page_edit.enter_sub_tool('Filter'):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Filter')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')

            return "FAIL"

    def sce_7_7_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)

            if self.is_exist(L.edit.sub_tool.filter.slider):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] No slider')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)

            return "FAIL"

    def sce_7_7_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.edit.sub_tool.filter.slider)

            if float(slider.text) == 100:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider.text}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)

            return "FAIL"

    def sce_7_7_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.after_filter = self.page_edit.get_preview_pic()

            if not HCompareImg(self.after_filter, self.before_filter).ssim_compare():
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
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.after_filter = self.page_edit.get_preview_pic()

            return "FAIL"

    def sce_7_7_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min()
            slider = self.element(L.edit.sub_tool.filter.slider)

            if float(slider.text) == 0:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider.text}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_min()

            return "FAIL"

    def sce_7_7_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.value_0 = self.page_edit.get_preview_pic()

            if not HCompareImg(self.value_0, self.after_filter).ssim_compare():
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
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_min()
            self.value_0 = self.page_edit.get_preview_pic()

            return "FAIL"

    def sce_7_7_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max()
            slider = self.element(L.edit.sub_tool.filter.slider)

            if float(slider.text) == 100:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider.text}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_max()

            return "FAIL"

    def sce_7_7_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.value_100 = self.page_edit.get_preview_pic()

            if not HCompareImg(self.value_100, self.value_0).ssim_compare():
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
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_max()

            return "FAIL"

    def sce_7_7_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            action_chains = ActionChains(self.driver.driver)
            action_chains.click_and_hold(self.element(L.edit.sub_tool.filter.compare)).perform()
            pic_compare = self.page_edit.get_preview_pic()
            action_chains = ActionChains(self.driver.driver)
            action_chains.click(self.element(L.edit.sub_tool.filter.compare)).perform()
            self.click(L.edit.sub_tool.filter.item(2))
            self.click(L.edit.sub_tool.filter.item(1))

            if HCompareImg(pic_compare, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is not original')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_max()
            self.click(L.edit.sub_tool.filter.compare)

            return "FAIL"

    def sce_7_7_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.filter.compare)
            pic_release = self.page_edit.get_preview_pic()

            if HCompareImg(pic_release, self.value_100).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is not resumed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)

            return "FAIL"

    def sce_7_7_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.filter.cancel)
            pic_cancel = self.page_edit.get_preview_pic()

            if HCompareImg(pic_cancel, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is changed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)

            return "FAIL"

    def sce_7_7_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.apply)
            pic_apply = self.page_edit.get_preview_pic()

            if not HCompareImg(pic_apply, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is not changed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.apply)

            return "FAIL"

    def sce_7_7_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.none)
            self.click(L.edit.sub_tool.filter.apply)
            pic_none = self.page_edit.get_preview_pic()

            if HCompareImg(pic_none, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is changed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)

            return "FAIL"

    def sce_7_7_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.add_master_media('video', test_material_folder, video_9_16)
            x = self.element(L.edit.master.clip()).rect['width']/2
            self.page_edit.scroll_playhead(-x)
            self.click(L.edit.master.clip(2))
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.apply_to_all)
            self.click(L.edit.sub_tool.filter.cancel)
            self.page_edit.scroll_playhead_to_beginning()
            self.click(L.edit.master.clip(1))
            self.page_edit.enter_sub_tool('Filter')

            if self.is_exist(L.edit.sub_tool.filter.edit):

                self.click(L.edit.sub_tool.filter.cancel)

                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Filter is not applied')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    def sce_7_7_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)

            if self.page_edit.enter_sub_tool('Filter'):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Filter')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')

            return "FAIL"

    def sce_7_7_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)

            if self.is_exist(L.edit.sub_tool.filter.slider):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] No slider')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)

            return "FAIL"

    def sce_7_7_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            slider = self.element(L.edit.sub_tool.filter.slider)

            if float(slider.text) == 100:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider.text}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)

            return "FAIL"

    def sce_7_7_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.after_filter = self.page_edit.get_preview_pic()

            if not HCompareImg(self.after_filter, self.before_filter).ssim_compare():
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
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.after_filter = self.page_edit.get_preview_pic()

            return "FAIL"

    def sce_7_7_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_min()
            slider = self.element(L.edit.sub_tool.filter.slider)

            if float(slider.text) == 0:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider.text}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_min()

            return "FAIL"

    def sce_7_7_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.value_0 = self.page_edit.get_preview_pic()

            if not HCompareImg(self.value_0, self.after_filter).ssim_compare():
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
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_min()
            self.value_0 = self.page_edit.get_preview_pic()

            return "FAIL"

    def sce_7_7_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.driver.drag_slider_to_max()
            slider = self.element(L.edit.sub_tool.filter.slider)

            if float(slider.text) == 100:
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider.text}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_max()

            return "FAIL"

    def sce_7_7_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.value_100 = self.page_edit.get_preview_pic()

            if not HCompareImg(self.value_100, self.value_0).ssim_compare():
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
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_max()

            return "FAIL"

    def sce_7_7_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            action_chains = ActionChains(self.driver.driver)
            action_chains.click_and_hold(self.element(L.edit.sub_tool.filter.compare)).perform()
            pic_compare = self.page_edit.get_preview_pic()
            action_chains = ActionChains(self.driver.driver)
            action_chains.click(self.element(L.edit.sub_tool.filter.compare)).perform()
            self.click(L.edit.sub_tool.filter.item(2))
            self.click(L.edit.sub_tool.filter.item(1))

            if HCompareImg(pic_compare, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is not original')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.edit)
            self.driver.drag_slider_to_max()
            self.click(L.edit.sub_tool.filter.compare)

            return "FAIL"

    def sce_7_7_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.filter.compare)
            pic_release = self.page_edit.get_preview_pic()

            if HCompareImg(pic_release, self.value_100).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is not resumed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.before_filter = self.page_edit.get_preview_pic()
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)

            return "FAIL"

    def sce_7_7_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.click(L.edit.sub_tool.filter.cancel)
            pic_cancel = self.page_edit.get_preview_pic()

            if HCompareImg(pic_cancel, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is changed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)

            return "FAIL"

    def sce_7_7_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.apply)
            pic_apply = self.page_edit.get_preview_pic()

            if not HCompareImg(pic_apply, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is not changed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.apply)

            return "FAIL"

    def sce_7_7_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.none)
            self.click(L.edit.sub_tool.filter.apply)
            pic_none = self.page_edit.get_preview_pic()

            if HCompareImg(pic_none, self.before_filter).ssim_compare():
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Preview is changed')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)

            return "FAIL"

    def sce_7_7_28(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        report.start_uuid(uuid)

        try:
            self.page_edit.add_master_media('photo', test_material_folder, photo_9_16)
            x = self.element(L.edit.master.clip()).rect['width']/2
            self.page_edit.scroll_playhead(-x)
            self.click(L.edit.master.clip(2))
            self.page_edit.enter_sub_tool('Filter')
            self.click(L.edit.sub_tool.filter.item(1))
            self.click(L.edit.try_before_buy.try_it_first, 2)
            self.click(L.edit.sub_tool.filter.apply_to_all)
            self.click(L.edit.sub_tool.filter.cancel)
            self.page_edit.scroll_playhead_to_beginning()
            self.click(L.edit.master.clip(1))
            self.page_edit.enter_sub_tool('Filter')

            if self.is_exist(L.edit.sub_tool.filter.edit):
                report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception(f'[Fail] Filter is not applied')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            return "FAIL"

    @report.exception_screenshot
    def test_case(self):
        result = {"sce_7_7_1": self.sce_7_7_1(),
                  "sce_7_7_2": self.sce_7_7_2(),
                  "sce_7_7_3": self.sce_7_7_3(),
                  "sce_7_7_4": self.sce_7_7_4(),
                  "sce_7_7_5": self.sce_7_7_5(),
                  "sce_7_7_6": self.sce_7_7_6(),
                  "sce_7_7_7": self.sce_7_7_7(),
                  "sce_7_7_8": self.sce_7_7_8(),
                  "sce_7_7_9": self.sce_7_7_9(),
                  "sce_7_7_10": self.sce_7_7_10(),
                  "sce_7_7_11": self.sce_7_7_11(),
                  "sce_7_7_12": self.sce_7_7_12(),
                  "sce_7_7_13": self.sce_7_7_13(),
                  "sce_7_7_14": self.sce_7_7_14(),
                  "sce_7_7_15": self.sce_7_7_15(),
                  "sce_7_7_16": self.sce_7_7_16(),
                  "sce_7_7_17": self.sce_7_7_17(),
                  "sce_7_7_18": self.sce_7_7_18(),
                  "sce_7_7_19": self.sce_7_7_19(),
                  "sce_7_7_20": self.sce_7_7_20(),
                  "sce_7_7_21": self.sce_7_7_21(),
                  "sce_7_7_22": self.sce_7_7_22(),
                  "sce_7_7_23": self.sce_7_7_23(),
                  "sce_7_7_24": self.sce_7_7_24(),
                  "sce_7_7_25": self.sce_7_7_25(),
                  "sce_7_7_26": self.sce_7_7_26(),
                  "sce_7_7_27": self.sce_7_7_27(),
                  "sce_7_7_28": self.sce_7_7_28(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
