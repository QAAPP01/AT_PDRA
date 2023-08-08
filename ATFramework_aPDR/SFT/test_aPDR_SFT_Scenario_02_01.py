import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from main import deviceName
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

file_video = 'video.mp4'


class Test_SFT_Scenario_02_01:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

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

    def sce_2_1_1(self):
        uuid = '923cc0c9-f6d8-4f65-8076-f1b585d5b1a3'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        import datetime
        dt = datetime.datetime.today()
        global default_project_name
        default_project_name = 'Project {:02d}-{:02d}'.format(dt.month, dt.day)
        self.page_main.enter_launcher()

        if self.page_main.enter_timeline(default_project_name):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Cannot find timeline canvas'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_2_1_2(self):
        uuid = 'a6faa123-8177-429b-9202-14c21e8905c0'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.page_edit.add_master_media('Video', self.test_material_folder, file_video)
        self.click(L.edit.timeline.master_clip)
        global pic_default_video
        pic_default_video = self.page_main.get_preview_pic()

        if self.page_edit.is_sub_tool_exist("Split"):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Cannot find "Split"'
            logger(fail_log)

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_2_1_3(self):
        try:
            uuid = '8973afb2-a0de-4e47-bd0c-d670f83f3c88'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clip = self.element(L.edit.timeline.master_video(file_video)).rect
            x = clip["x"] + clip["width"] // 2
            self.page_main.h_swipe_playhead(x)
            self.page_edit.click_sub_tool("Split")
            playhead = self.element(L.edit.timeline.playhead).rect
            playhead_center = playhead["x"] + playhead["width"] // 2
            x_after = self.elements(L.edit.timeline.master_video(file_video))[1].rect["x"]

            if abs(x_after - playhead_center) < 2:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Split fail: playhead_center = {playhead_center}, x_after = {x_after}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "Error"

    def sce_2_1_4(self):
        try:
            uuid = '09cadca9-f7cd-4d6e-a0d1-e26cce285fcf'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clip = self.elements(L.edit.timeline.master_video_thumbnail(file_video, 2))[0]
            pic_after = self.page_main.h_screenshot(clip)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_4.png')

            if HCompareImg(pic_base, pic_after).keypoint_compare() > 0.9:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_11(self):
        try:
            uuid = 'b3121bdd-b1f5-4532-9f6c-13237193ee4f'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.page_edit.click_sub_tool('Rotate'):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Click "Rotate" fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_12(self):
        uuid = '6805d7b3-1775-4b5f-930f-159965846428'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            time.sleep(5)
            pic_after = self.page_main.h_screenshot()

            global result_12
            if not HCompareImg(pic_default_video, pic_after).full_compare() == 1:
                result_12 = True
                fail_log = None
            else:
                result_12 = False
                fail_log = f'\n[Fail] Preview has no changed'

            self.report.new_result(uuid, result_12, fail_log=fail_log)
            return "PASS" if result_12 else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_13(self):
        try:
            uuid = 'd5b79a1e-03ee-443a-8a49-d98349bba1b3'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if result_12:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Image incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_17(self):
        try:
            uuid = '394f27cb-9e6f-411b-add7-638473575131'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.page_edit.trim_clip(frame="right") and self.page_edit.trim_clip(frame="left"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Trim fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_18(self):
        try:
            uuid = '73720235-b876-49a2-82d9-75b7e3a4d620'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            # by pass bug
            self.page_main.swipe_element(L.edit.timeline.timeline_ruler, 'left', 1)
            self.page_main.swipe_element(L.edit.timeline.timeline_ruler, 'right', 100)
            #

            clip = self.elements(L.edit.timeline.master_video_thumbnail(file_video, 1))[0]
            pic_after = self.page_main.h_screenshot(clip)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_18.png')

            if HCompareImg(pic_base, pic_after).keypoint_compare() > 0.9:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_19(self):
        try:
            uuid = 'ae24be03-9cad-455e-b23e-924d12984199'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clips = self.elements(L.edit.timeline.master_video(file_video))
            clip1 = clips[0].rect
            clip2 = clips[1].rect

            if clip1["x"] + clip1["width"] == clip2["x"]:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] end of clip1 = {clip1["x"] + clip1["width"]}, start of clip2 = {clip2["x"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_26(self):
        try:
            uuid = 'bef218e9-b099-4126-ac5b-1d5a80ed0554'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            # by pass bug
            self.click(L.edit.timeline.clip())
            #

            if self.page_edit.click_sub_tool('Flip'):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Click "Flip" fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_27(self):
        try:
            uuid = '6be89ea0-524f-4d3f-bc99-e27c2acbe909'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            time.sleep(5)
            pic_after = self.page_main.h_screenshot()

            global result_27
            if not HCompareImg(pic_default_video, pic_after).full_compare == 1:
                result_27 = True
                fail_log = None
            else:
                result_27 = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result_27, fail_log=fail_log)
            return "PASS" if result_27 else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_28(self):
        try:
            uuid = 'cac9a824-5140-47d6-ae60-d126e04becde'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if result_27:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Image incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_32(self):
        try:
            uuid = '4a9dcf18-a3a8-414f-839f-bc4b085f79c2'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            global pic_original
            pic_original = self.page_main.h_screenshot()
            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_free)
            boundary_rect = self.element(L.edit.crop.boundary).rect
            end_x = boundary_rect['x'] + boundary_rect['width'] * 0.7
            end_y = boundary_rect['y'] + boundary_rect['height'] * 0.7
            self.page_edit.h_drag_element(L.edit.crop.right_top, end_x, end_y)
            self.click(L.edit.crop.apply)
            global pic32
            pic32 = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_32.png')

            # self.page_main.copy_file(pic32, pic_base)

            if HCompareImg(pic_base, pic32).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_33(self):
        try:
            uuid = 'af6b9dc7-3318-47bd-93e9-cdf5e452b326'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_free)
            boundary_rect = self.element(L.edit.crop.boundary).rect
            end_x = boundary_rect['x'] + boundary_rect['width'] * 0.7
            end_y = boundary_rect['y'] + boundary_rect['height'] * 0.7
            self.page_edit.h_drag_element(L.edit.crop.right_top, end_x, end_y)
            self.click(L.edit.crop.cancel)
            pic_after = self.page_main.get_preview_pic()

            if HCompareImg(pic32, pic_after).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_34(self):
        try:
            uuid = '789d8fa7-6027-47f5-a979-c165c4dc6028'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_9_16)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_34.png')

            # self.page_main.copy_file(pic_after, pic_base)

            if HCompareImg(pic_base, pic_after).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_35(self):
        try:
            uuid = '15c5cdc8-d471-4df4-9ae8-bfd5dcc32067'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_1_1)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_35.png')

            # self.page_main.copy_file(pic_after, pic_base)

            if HCompareImg(pic_base, pic_after).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_36(self):
        try:
            uuid = '8683f4f6-9110-4577-be14-3b7174f60f32'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_4_5)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_36.png')

            # self.page_main.copy_file(pic_after, pic_base)

            if HCompareImg(pic_base, pic_after).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_37(self):
        try:
            uuid = 'a962eb0d-a799-4dac-918f-b287ee3244c3'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_16_9)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()

            if not HCompareImg(pic_default_video, pic_after).full_compare() == 1:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Preview has no changed'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_38(self):
        try:
            uuid = '4d9b5fae-140c-4f00-9260-088eec60dcb5'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_4_3)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_38.png')

            # self.page_main.copy_file(pic_after, pic_base)

            if HCompareImg(pic_base, pic_after).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_39(self):
        try:
            uuid = 'd9106fce-f2b0-4b92-bd1f-ce3eb0e185dd'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.page_main.h_swipe_element(L.edit.crop.btn_1_1, L.edit.crop.btn_4_3, 1)
            self.click(L.edit.crop.btn_original)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()

            if not HCompareImg(pic_default_video, pic_after).full_compare() == 1:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Preview has no changed'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_40(self):
        try:
            uuid = '7f642e5d-1ef0-44a8-8d01-5de9d10a933c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.page_main.h_swipe_element(L.edit.crop.btn_4_5, L.edit.crop.btn_free, 1)
            self.click(L.edit.crop.btn_3_4)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_40.png')

            # self.page_main.copy_file(pic_after, pic_base)

            if HCompareImg(pic_base, pic_after).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_41(self):
        try:
            uuid = '2eec3b22-9b2a-41b6-8c8b-ae50e1ab1f10'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.btn_21_9)
            self.click(L.edit.crop.apply)
            pic_after = self.page_main.get_preview_pic()

            if not HCompareImg(pic_default_video, pic_after).full_compare() == 1:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Preview has no changed'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_42(self):
        try:
            uuid = '00b2177a-05c4-411a-8c68-0b88cd3ce8bd'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')

            if not self.is_exist(L.edit.crop.play_pause):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Found Play/Pause button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_43(self):
        try:
            uuid = '8e379056-3eba-4d4f-8601-9b321f014a46'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            slider_rect = self.element(L.edit.crop.slider).rect
            x = slider_rect['x'] + slider_rect['width'] // 2
            y = slider_rect['y'] + slider_rect['height'] // 2
            self.page_main.h_tap(x, y)
            time_code = self.element(L.edit.crop.time_code).text
            self.click(L.edit.crop.apply)

            if time_code.split('/')[0] == "00:01" or time_code.split('/')[0] == "00:02":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] time code is incorrect:{time_code.split("/")[0]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_44(self):
        try:
            uuid = 'e38aad9a-a25a-4c41-8598-923c01c74b4a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_tool('Crop')
            self.click(L.edit.crop.reset)
            self.click(L.edit.crop.apply)
            time.sleep(1)
            pic_after = self.page_main.get_preview_pic()

            if HCompareImg(pic_original, pic_after).full_compare() > 0.96:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_45(self):
        try:
            uuid = '227a3419-90e9-465a-b230-6efe8bc640d0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.add_master_media('video', self.test_material_folder, file_video)
            if self.page_edit.click_sub_tool('Reverse'):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Click "Reverse" fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"

        except Exception as err:
            logger(f'\n{err}')

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', self.test_material_folder, file_video)

            return "FAIL"

    def sce_2_1_46(self):
        try:
            uuid = '73b8a01c-23d2-498c-8d99-0d1e6fb681c3'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.reverse.dialog_ok)
            progress_bar = self.is_exist(L.edit.reverse.progress_bar)
            ad = self.is_exist(L.edit.reverse.ad, 10)

            if progress_bar and ad:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] progress_bar:{progress_bar}, ad:{ad}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_47(self):
        try:
            uuid = '63ef8f5b-b929-400d-b32c-69e647e9f4b6'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            logger('[Info] Reversing')
            while self.is_exist(L.edit.reverse.progress_bar):
                time.sleep(1)

            pic_base = self.page_main.h_screenshot(
                self.element(L.edit.timeline.master_video_thumbnail(thumbnail_index=1)))
            self.page_edit.click_sub_tool('Reverse')
            self.click(L.edit.reverse.dialog_ok)
            time.sleep(2)
            pic_after = self.page_main.h_screenshot(
                self.element(L.edit.timeline.master_video_thumbnail(thumbnail_index=1)))

            if not HCompareImg(pic_base, pic_after).full_compare() > 0.98:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Thumbnails are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_48(self):
        uuid = 'dce25f23-067f-4a5f-8dda-692ee46fada3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        self.report.new_result(uuid, None, 'N/A')

        # try:
        #     global stab_before
        #     stab_before = self.page_main.h_screenshot()
        #     self.click(L.edit.sub_tool.back, timeout=0.1)
        #
        #     if self.page_edit.click_sub_tool("Stabilizer"):
        #         result = True
        #         fail_log = None
        #     else:
        #         result = False
        #         fail_log = f'\n[Fail] Cannot find "Stabilizer"'
        #
        #     self.report.new_result(uuid, result, fail_log=fail_log)
        #     return "PASS" if result else "FAIL"
        # except Exception as err:
        #     logger(f"[Error] {err}")
        #     return "ERROR"

    def sce_2_1_50(self):
        uuid = '36454a6f-1031-4372-a1fb-f2f3f79a8ce3'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.report.new_result(uuid, None, 'N/A')

        # try:
        #     self.click(L.main.subscribe.iap_monthly)
        #     self.click(L.main.subscribe.continue_btn)
        #     self.click(find_string("Subscribe"))
        #     self.click(find_string("Not now"))
        #
        #     if self.is_exist(find_string("Stabilizing video"), 10):
        #         result = True
        #         fail_log = None
        #     else:
        #         result = False
        #         fail_log = f'\n[Fail] Cannot find "Stabilizing video"'
        #
        #     self.report.new_result(uuid, result, fail_log=fail_log)
        #     return "PASS" if result else "FAIL"
        # except Exception as err:
        #     logger(f"[Error] {err}")
        #     return "ERROR"

    def sce_2_1_49(self):
        uuid = '8ce1701e-fa22-4544-a586-98eef705981d'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.report.new_result(uuid, None, 'N/A')

        # try:
        #     logger("[Info] Stabilizing")
        #     while self.is_exist(find_string("Stabilizing video")):
        #         time.sleep(1)
        #
        #     global stab_after
        #     stab_after = self.page_main.h_screenshot()
        #
        #     result_pic = True if not HCompareImg(stab_after, stab_before).full_compare() > 0.98 else False
        #     result_value = True if self.element(L.edit.timeline.slider_value).text == "50" else False
        #
        #     if result_pic and result_value:
        #         result = True
        #         fail_log = None
        #     else:
        #         result = False
        #         fail_log = f'\n[Fail] result_pic = {result_pic}, result_value = {result_value}'
        #
        #     self.report.new_result(uuid, result, fail_log=fail_log)
        #     return "PASS" if result else "FAIL"
        # except Exception as err:
        #     logger(f"[Error] {err}")
        #     return "ERROR"

    def sce_2_1_51(self):
        uuid = 'f770a0a8-68b9-4811-86c6-7131c3a732f3'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.report.new_result(uuid, None, 'N/A')

        # try:
        #
        #     rect = self.element(L.edit.timeline.slider).rect
        #     min_value = rect["x"]
        #     self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, min_value)
        #     time.sleep(2)
        #
        #     global stab_min
        #     stab_min = self.page_main.h_screenshot()
        #
        #     result_pic = True if not HCompareImg(stab_min, stab_after).full_compare() > 0.98 and HCompareImg(stab_min,
        #                                                                                                      stab_before).full_compare() > 0.98 else False
        #     result_value = True if self.element(L.edit.timeline.slider_value).text == "0" else False
        #
        #     if result_pic and result_value:
        #         result = True
        #         fail_log = None
        #     else:
        #         result = False
        #         fail_log = f'\n[Fail] result_pic = {result_pic}, result_value = {result_value}'
        #
        #     self.report.new_result(uuid, result, fail_log=fail_log)
        #     return "PASS" if result else "FAIL"
        # except Exception as err:
        #     logger(f"[Error] {err}")
        #     return "ERROR"

    def sce_2_1_52(self):
        uuid = 'aae26929-d157-441c-9959-cc4f3004cd7c'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        self.report.new_result(uuid, None, 'N/A')
        #
        # try:
        #
        #     rect = self.element(L.edit.timeline.slider).rect
        #     max_value = rect["x"] + rect["width"]
        #     self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, max_value)
        #     time.sleep(2)
        #
        #     stab_max = self.page_main.h_screenshot()
        #     result_pic = True if not HCompareImg(stab_max, stab_after).full_compare() > 0.98 and not HCompareImg(
        #         stab_max, stab_before).full_compare() > 0.98 else False
        #     result_value = True if self.element(L.edit.timeline.slider_value).text == "100" else False
        #
        #     if result_pic and result_value:
        #         result = True
        #         fail_log = None
        #     else:
        #         result = False
        #         fail_log = f'\n[Fail] result_pic = {result_pic}, result_value = {result_value}'
        #
        #     self.report.new_result(uuid, result, fail_log=fail_log)
        #     return "PASS" if result else "FAIL"
        # except Exception as err:
        #     logger(f"[Error] {err}")
        #     return "ERROR"

    def sce_2_1_skip(self):
        # Skip
        logger(f"\n[Start] {inspect.stack()[0][3]}")

        self.report.add_result('bca3a613-0136-4e50-bed8-d3bcaa2916dc', None, 'N/A', 'merge to sce_2.2')     # 2.1.53, merge to sce_2.2
        self.report.add_result('4c4e9e25-e039-4899-a165-1e18c39db2bd', None, 'N/A', 'merge to sce_2.2')     # 2.1.54, merge to sce_2.2
        self.report.add_result('300efe76-5d15-4f53-821f-9d0ce6f859d2', None, 'N/A', 'merge to sce_2.33')    # 2.1.57, merge to sce_2.33
        self.report.add_result('72409732-13c5-4490-a1a9-3bd1d6ba34db', None, 'N/A', 'merge to sce_2.33')    # 2.1.58, merge to sce_2.33
        self.report.add_result('ec404b31-1e27-47c4-9092-355fc4a2401a', None, 'N/A', 'merge to sce_2.33')    # 2.1.59, merge to sce_2.33
        self.report.add_result('4dc86868-4e85-4809-8d36-f3d35bff2496', None, 'N/A', 'merge to sce_2.33')    # 2.1.60, merge to sce_2.33
        self.report.add_result('32448a26-3bea-41ef-b1c4-352715ee44d6', None, 'N/A', 'merge to sce_2.33')    # 2.1.61, merge to sce_2.33
        return "N/A"

    def sce_2_1_64(self):
        try:
            uuid = '4017ecaf-4099-45c4-bdff-2fb9633d42c4'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.add_master_media('video', self.test_material_folder, 'video.mp4')
            self.click(L.edit.timeline.master_video('video.mp4'))
            self.page_edit.click_sub_tool("Adjustment")
            self.page_edit.click_sub_option_tool("Brightness")
            value = self.element(L.edit.timeline.slider_value).text

            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_64.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_62(self):
        try:
            uuid = '94c02d7d-3fc6-479a-969e-c9aee5cc4ca1'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 0:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_66(self):
        try:
            uuid = '5be6d9f5-cf81-4408-80a7-2aca089389cb'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_66.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_63(self):
        try:
            uuid = '206d5ec5-53fc-439e-8277-6fc407bdd26e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 0:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_65(self):
        try:
            uuid = '56bfcf3c-ebc3-4c44-b278-2f99a5ac017e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "-100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_65.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_69(self):
        try:
            uuid = '176f1faa-cf8d-47e7-aa9d-15f975a5abae'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_option_tool("Contrast")
            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_69.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_67(self):
        try:
            uuid = '120dc857-7115-4dff-aa89-9a4c87cac13c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 0:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_71(self):
        try:
            uuid = '8ceae3f4-e25a-4420-8e9e-036efe2c32ad'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_71.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_68(self):
        try:
            uuid = 'a4434695-07e6-4013-92d3-a776e99ce42a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 0:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_70(self):
        try:
            uuid = '6e38e549-1176-4c7c-b247-dfb73b34c98e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "-100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_70.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_74(self):
        try:
            uuid = '563a3999-87e2-4b02-8256-ea1c0c42e6a8'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_option_tool("Saturation")
            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_74.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_72(self):
        try:
            uuid = 'd8fe2c0e-f903-4c34-9f3b-dc4b1165c19e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 100:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_76(self):
        try:
            uuid = '7156957f-4dca-496f-a4c6-65e674753603'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "200"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_76.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_73(self):
        try:
            uuid = '0523771e-346a-4477-80ef-b7c2d2c4f46d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 100:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_75(self):
        try:
            uuid = '4641b18f-3f95-431a-85a3-8d68bd6afc22'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_75.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_79(self):
        try:
            uuid = '8d509724-ad94-41ba-8add-ca7a0c018aae'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_option_tool("Hue")
            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_79.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_77(self):
        try:
            uuid = 'eb384538-b939-4445-b12c-4c2038c9a51d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 100:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_81(self):
        try:
            uuid = 'e1e887e6-8cba-4c26-9de3-ee1ad93c0599'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "200"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_81.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_78(self):
        try:
            uuid = 'c7701799-6d27-4126-8ab9-f158d6ca49ac'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 100:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_80(self):
        try:
            uuid = '55d52fc1-4867-408c-aa91-0240796084f0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_80.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_84(self):
        try:
            uuid = 'ae478e12-9e67-42d0-9052-1cf63f3394ca'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_option_tool("Temp")
            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "50"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_84.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_82(self):
        try:
            uuid = 'cb5ef2e5-c9c4-422e-8a53-a1e0a67c717e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 50:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_86(self):
        try:
            uuid = '0a4208a2-2d52-4964-9df4-23c29aba3f2a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_86.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_83(self):
        try:
            uuid = 'c01e1811-16c2-447c-980d-cbe12e197e1c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 50:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_85(self):
        try:
            uuid = 'ed5d6e4a-eeb7-47af-936f-ae7c2ff8ef95'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_85.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_89(self):
        try:
            uuid = '7ef47ca5-1eaf-4202-bb35-b576ea881f21'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.click_sub_option_tool("Tint")
            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "50"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_89.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_87(self):
        try:
            uuid = '8a325e3f-f985-4bae-91da-c58266a6d4dc'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 50:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_91(self):
        try:
            uuid = '1637dd88-bb2a-40c0-ab03-c854f9681e58'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_91.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_88(self):
        try:
            uuid = '2049e934-49b4-4f49-b4b2-5c5b2bbfa708'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 50:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_90(self):
        try:
            uuid = 'cb672a5c-543a-4d03-b81c-0a1a9f56070a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_90.png')

            result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_55(self):
        try:
            uuid = '66247e49-e3aa-4b77-929e-33b67fff2f63'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.timeline.reset)
            self.page_edit.click_sub_option_tool("Sharpness")
            value = self.element(L.edit.timeline.slider_value).text

            global pic_no_sharpness
            pic_no_sharpness = self.page_main.get_preview_pic()

            if value == "0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_56(self):
        try:
            uuid = '8ac1816f-4cf6-4c48-95b7-6f770176cf73'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "200"

            pic_tgt = self.page_main.get_preview_pic()
            pic_src = pic_no_sharpness

            result_preview = True if not HCompareImg(pic_tgt, pic_src).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_92(self):
        try:
            uuid = 'ef0b9513-1de9-45a3-a6e4-2059298ee095'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.sub_tool_menu.back)
            self.page_edit.add_master_media('video', self.test_material_folder, 'video.mp4')
            self.click(L.edit.timeline.master_video('video.mp4'))
            global pic_no_skin
            pic_no_skin = self.page_main.get_preview_pic()
            self.page_edit.click_sub_tool("Skin Smoothener")

            if self.page_edit.click_sub_option_tool("Brightness"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find "Skin Smoothener"'

            self.click(L.edit.timeline.reset)

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_95(self):
        try:
            uuid = '5205c71f-b7ee-4d85-91ff-85db47e21d33'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "80"
            pic_tgt = self.page_main.get_preview_pic()

            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_93(self):
        try:
            uuid = '523fa5b4-4430-4696-a383-d2225a96f4ae'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_97(self):
        try:
            uuid = '30928b0e-7adf-49bb-9985-6f942fde8659'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_94(self):
        try:
            uuid = 'd0dc8798-0ade-4c09-a472-d2a2b7b00c56'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_96(self):
        try:
            uuid = 'e5838f68-1e4c-4364-a45c-dbc8ceeaa47d'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "40"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_98(self):
        try:
            uuid = 'e843e5e9-7186-48e9-abb1-9c4f2b9030c8'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.page_edit.click_sub_option_tool("Smoothness"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find "Skin Smoothener"'

            self.click(L.edit.timeline.reset)

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_101(self):
        try:
            uuid = '393cfcfd-43b0-475f-b13d-fe0252d6c02a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "80"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_99(self):
        try:
            uuid = '86e0beb3-2ccf-4458-bb7f-11d91d70306c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_103(self):
        try:
            uuid = '4d4f4af3-6c98-4a4c-9774-bac2339ed28a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_100(self):
        try:
            uuid = 'cd508710-449f-46a2-9885-02f359ea68bb'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_102(self):
        try:
            uuid = 'f96b2755-2cab-4f5c-bcfa-49da0a234a26'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.page_edit.click_sub_option_tool("Remove")

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_104(self):
        try:
            uuid = '9876425c-07fa-4251-aac2-043efba6099e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.add_master_media("photo", self.test_material_folder, "photo.jpg")
            self.click(L.edit.timeline.master_photo("photo.jpg"))
            global pic_no_skin
            pic_no_skin = self.page_main.get_preview_pic()
            self.page_edit.click_sub_tool("Skin Smoothener")

            if self.page_edit.click_sub_option_tool("Brightness"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find "Skin Smoothener"'

            self.click(L.edit.timeline.reset)

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_107(self):
        try:
            uuid = 'e6c5ef78-3357-4d24-bd2c-35b84312ab6e'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "80"
            pic_tgt = self.page_main.get_preview_pic()

            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_105(self):
        try:
            uuid = '7702acb8-01ab-485b-a1b9-1ae0d40b3db0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_109(self):
        try:
            uuid = 'd137ff35-e784-48a6-932c-8c6043842bd0'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_106(self):
        try:
            uuid = 'a4eca9b7-5e95-4705-85c3-215ced32e652'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_108(self):
        try:
            uuid = 'd0a7463a-9844-446a-bd11-d569093a238e'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "40"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_110(self):
        try:
            uuid = 'efbf6762-c2be-423a-866a-5f02850339b0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.page_edit.click_sub_option_tool("Smoothness"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find "Skin Smoothener"'

            self.click(L.edit.timeline.reset)

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_113(self):
        try:
            uuid = 'b8555a72-e79c-48e8-be81-b8cd86c7e385'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "80"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_111(self):
        try:
            uuid = '98e4a27e-3f30-4416-99c5-09a5120d3d0d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) > 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_115(self):
        try:
            uuid = 'a410a826-d866-4cf9-a1c7-a7a77af7432b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "100"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_112(self):
        try:
            uuid = 'a7a640c4-9eb1-457b-9983-96fabfd51c26'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if int(value) < 80:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_114(self):
        try:
            uuid = 'cb153b5e-c536-4ed6-8d9f-71f235711d5d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text
            result_value = value == "0"

            pic_tgt = self.page_main.get_preview_pic()
            result_preview = True if not HCompareImg(pic_tgt, pic_no_skin).full_compare() == 1 else False

            if result_value and result_preview:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_134(self):
        try:
            uuid = '1cccd2a9-0e20-4988-95a9-cda0dabef154'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            self.click(L.edit.menu.undo)
            value = self.element(L.edit.timeline.slider_value).text

            if value == "100":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Undo fail'

            self.page_edit.click_sub_option_tool("Remove")

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_117(self):
        try:
            uuid = 'a7a218b8-8869-4823-b94f-09e43738c99d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_edit.add_master_media("photo", self.test_material_folder, "9_16.jpg")
            self.click(L.edit.timeline.master_photo("9_16.jpg"))
            self.page_edit.click_sub_tool("Fit & Fill")
            global pic_orignal
            pic_orignal = self.page_main.get_preview_pic()
            self.click(L.edit.fit_and_fill.btn_fill)
            pic_fill = self.page_main.get_preview_pic()

            if not HCompareImg(pic_fill, pic_orignal).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_116(self):
        try:
            uuid = '1dd00bf7-eb3d-4c16-a59e-df719e686705'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.fit_and_fill.btn_fit)
            pic_fit = self.page_main.get_preview_pic()

            if HCompareImg(pic_fit, pic_orignal).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_118(self):
        try:
            uuid = 'df25ea97-3885-4565-8674-8e1dab542c1f'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.driver.zoom(L.edit.preview.preview)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_orignal).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_119(self):
        try:
            uuid = '9ce3c256-c06f-4d46-ae32-690a8f55dc0e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.sub_tool_menu.back)
            self.page_edit.click_sub_tool("Background")

            if self.element(L.edit.background.btn_none).get_attribute("selected") == "true":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] None is not selected'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_120(self):
        try:
            uuid = 'da46e132-84b5-4309-85e6-25912abfe68c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.background.btn_blur)
            value = self.element(L.edit.timeline.slider_value).text

            if value == "5.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_121(self):
        try:
            uuid = '5421f1c3-fa82-4e1c-9bd2-3ec000e6bc79'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if value == "10.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_122(self):
        try:
            uuid = '392c83be-1b18-4144-8139-e37f4bc78912'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if value == "0.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_123(self):
        try:
            uuid = '12078d3f-6e1e-4c7c-9646-cdd0b4f1bf78'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.background.btn_background_color)
            self.click(L.edit.background.card_color(2))

            if self.is_exist(L.edit.timeline.slider):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Slider is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_124(self):
        try:
            uuid = '788d9d49-a399-4836-9a5a-73e6adbcec6b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            value = self.element(L.edit.timeline.slider_value).text

            if value == "0.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_125(self):
        try:
            uuid = '839b984f-7bbc-4c90-9f7c-937517e968c7'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"] + rect["width"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if value == "1.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_126(self):
        try:
            uuid = 'b4f3d847-7ca1-49d8-9675-2548942ff9c4'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            rect = self.element(L.edit.timeline.slider).rect
            end_x = rect["x"]
            self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
            value = self.element(L.edit.timeline.slider_value).text

            if value == "-1.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Value incorrect: {value}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_128(self):
        try:
            uuid = '2700a3cb-50c3-4b20-b2a6-c53551176f01'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            locator = L.edit.background.card_color(1)
            self.click(locator)
            pic_src = self.page_main.get_picture(locator)
            rect = self.element(L.edit.preview.preview).rect
            y = rect["y"] + rect["height"]/2
            x = rect["x"] + rect["width"]/2
            x_end = rect["x"] + rect["width"]/4
            self.page_main.h_swipe_location(x, y, x_end, y)
            pic_tgt = self.page_main.get_picture(locator)

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Image is the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_127(self):
        try:
            uuid = '9576806e-542b-454e-bcb9-f68b2129b64d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            cards = self.elements(L.edit.background.card_color(0))
            self.click(cards[-1])
            retry = 20
            while self.is_exist(L.edit.timeline.slider) and retry:
                cards = self.elements(L.edit.background.card_color(0))
                self.page_main.h_swipe_element(cards[-1], cards[0], 2)
                cards = self.elements(L.edit.background.card_color(0))
                self.click(cards[-1])
                retry -= 1

            if retry > 0:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Slider is exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_129_130(self):
        try:
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            pic_src = self.page_main.get_preview_pic()

            def sce_2_1_129(index):
                try:
                    uuid = 'a7c251ce-afdb-48d7-9ee3-5ecf91451c7c'
                    logger(f"\n[Start] {inspect.stack()[0][3]}")
                    self.report.start_uuid(uuid)

                    cards = self.elements(L.edit.background.pattern_layout(0))
                    self.click(cards[index])
                    cards = self.elements(L.edit.background.pattern_layout(0))
                    retry = 20
                    while self.page_main.h_is_child_id_exist(cards[index], L.edit.background.download_icon) and retry:
                        cards = self.elements(L.edit.background.pattern_layout(0))
                        time.sleep(1)
                        retry -= 1
                    if retry == 0:
                        logger("\n[Error] Download fail")

                    pic_tgt = self.page_main.get_preview_pic()

                    if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                        result = True
                        fail_log = None
                    else:
                        result = False
                        fail_log = f'\n[Fail] Images are different'

                    self.report.new_result(uuid, result, fail_log=fail_log)
                    return "PASS" if result else "FAIL"

                except Exception as err:
                    logger(f"[Error] {err}")
                    return "ERROR"

            def sce_2_1_130(index):
                try:
                    uuid = '5df5c584-5393-4b89-bee8-cf139e820fb0'
                    logger(f"\n[Start] {inspect.stack()[0][3]}")
                    self.report.start_uuid(uuid)

                    cards = self.elements(L.edit.background.pattern_layout(0))
                    self.click(cards[index])
                    cards = self.elements(L.edit.background.pattern_layout(0))
                    retry = 20
                    while self.page_main.h_is_child_id_exist(cards[index], L.edit.background.download_icon) and retry:
                        cards = self.elements(L.edit.background.pattern_layout(0))
                        time.sleep(1)
                        retry -= 1
                    if retry == 0:
                        logger("\n[Error] Download fail")

                    pic_tgt = self.page_main.get_preview_pic()
                    result_img = not HCompareImg(pic_tgt, pic_src).full_compare_result()
                    result_premium = self.is_exist(L.edit.try_before_buy.premium_features_used_bubble)

                    if result_img and result_premium:
                        result = True
                        fail_log = None
                    else:
                        result = False
                        fail_log = f'\n[Fail] result_img = {result_img}, result_premium = {result_premium}'

                    self.report.new_result(uuid, result, fail_log=fail_log)
                    return "PASS" if result else "FAIL"
                except Exception as err:
                    logger(f"[Error] {err}")
                    return "ERROR"

            self.click(L.edit.sub_tool.back)
            self.click(L.edit.background.btn_background_pattern)
            cards = self.elements(L.edit.background.pattern_layout(0))
            free_flag = 0
            paid_flag = 0
            result_129 = 0
            result_130 = 0

            while not free_flag or not paid_flag:
                for i in range(len(cards)):
                    if free_flag and paid_flag:
                        break
                    if self.page_main.h_is_child_id_exist(cards[i], L.edit.background.try_icon):
                        if not paid_flag:
                            result_130 = sce_2_1_130(i)
                            paid_flag = 1
                            cards = self.elements(L.edit.background.pattern_layout(0))
                    elif not free_flag:
                        result_129 = sce_2_1_129(i)
                        free_flag = 1
                        cards = self.elements(L.edit.background.pattern_layout(0))
                if free_flag and paid_flag:
                    break
                else:
                    cards = self.elements(L.edit.background.pattern_layout(0))
                    last = self.page_main.get_picture(cards[-1])
                    self.page_main.h_swipe_element(cards[-1], cards[0])
                    cards = self.elements(L.edit.background.pattern_layout(0))
                    if HCompareImg(self.page_main.get_picture(cards[-1]), last).full_compare_result():
                        logger("[Fail] End of pattern")
                        return "ERROR"

            self.click(L.edit.sub_tool_menu.back)
            self.click(L.edit.try_before_buy.try_it)

            return "PASS" if result_129 and result_130 else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    # def sce_2_1_53(self):
    #     # executed in test_aPDR_SFT_scenario_02_02
    #     pass
    #     try:
    #         uuid = 'bca3a613-0136-4e50-bed8-d3bcaa2916dc'
    #         logger(f"\n[Start] {inspect.stack()[0][3]}")
    #         self.report.start_uuid(uuid)
    #
    #         self.page_edit.add_master_media('photo', self.test_material_folder, 'photo.jpg')
    #         self.click(L.edit.timeline.master_clip)
    #         self.page_edit.click_sub_tool("Adjustment")
    #         self.page_edit.click_sub_option_tool("Sharpness")
    #         value = self.element(L.edit.timeline.slider_value).text
    #         result_value = value == "0"
    #
    #         pic_tgt = self.page_main.get_preview_pic()
    #         pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_53.png')
    #
    #         result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False
    #
    #         if result_value and result_preview:
    #             result = True
    #             fail_log = None
    #         else:
    #             result = False
    #             fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'
    #
    #         self.report.new_result(uuid, result, fail_log=fail_log)
    #         return "PASS" if result else "FAIL"
    #     except Exception as err:
    #         logger(f"[Error] {err}")
    #         return "ERROR"
    #
    # def sce_2_1_54(self):
    #     try:
    #         uuid = '4c4e9e25-e039-4899-a165-1e18c39db2bd'
    #         logger(f"\n[Start] {inspect.stack()[0][3]}")
    #         self.report.start_uuid(uuid)
    #
    #         rect = self.element(L.edit.timeline.slider).rect
    #         end_x = rect["x"] + rect["width"]
    #         self.page_main.h_swipe_element_to_location(L.edit.timeline.slider_value, end_x)
    #         value = self.element(L.edit.timeline.slider_value).text
    #         result_value = value == "200"
    #
    #         pic_tgt = self.page_main.get_preview_pic()
    #         pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_54.png')
    #
    #         result_preview = True if HCompareImg(pic_tgt, pic_src).full_compare() > 0.96 else False
    #
    #         if result_value and result_preview:
    #             result = True
    #             fail_log = None
    #         else:
    #             result = False
    #             fail_log = f'\n[Fail] result_value:{result_value}, result_preview: {result_preview}'
    #
    #         self.report.new_result(uuid, result, fail_log=fail_log)
    #         return "PASS" if result else "FAIL"
    #     except Exception as err:
    #         logger(f"[Error] {err}")
    #         return "ERROR"

    def sce_2_1_5(self):
        try:
            uuid = 'a29fa42b-7da3-47ae-8f5b-8d3d9a8b4dfb'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            for i in range(4):
                if self.click(L.edit.sub_tool.back, timeout=0.1):
                    continue
                else:
                    break
            self.page_main.h_swipe_playhead(10, 1)
            global file_photo
            file_photo = 'photo.jpg'
            self.page_edit.add_master_media('Photo', self.test_material_folder, file_photo)
            self.click(L.edit.timeline.master_clip)

            if self.page_edit.is_sub_tool_exist("Split"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find "Split"'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_6(self):
        try:
            uuid = 'a8b1a23a-6604-4ea4-b703-388bf7afaca0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clip = self.element(L.edit.timeline.master_photo(file_photo)).rect
            x = clip["x"] + clip["width"] // 2
            self.page_main.h_swipe_playhead(x)
            self.page_edit.click_sub_tool("Split")
            playhead = self.element(L.edit.timeline.playhead).rect
            playhead_center = playhead["x"] + playhead["width"] // 2
            x_after = self.element(L.edit.timeline.master_photo(file_photo, 2)).rect["x"]

            if abs(x_after - playhead_center) < 10:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Split fail: playhead_center = {playhead_center}, x_after = {x_after}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_7(self):
        try:
            uuid = 'f210260a-0827-41aa-a792-85d5cbf3c1e3'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clip = self.element(L.edit.timeline.master_photo(file_photo, 2))
            pic_after = self.page_main.h_screenshot(clip)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_7.png')

            if HCompareImg(pic_base, pic_after).keypoint_compare() > 0.9:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_14(self):
        try:
            uuid = '0ed05cdd-8647-4dcf-9747-9894dad0e3e3'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.page_edit.click_sub_tool('Rotate'):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Click "Rotate" fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_15(self):
        try:
            uuid = '1a05c9a6-66b7-4703-9f22-6172a920c201'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            time.sleep(5)
            pic_after = self.page_main.h_screenshot()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_15.png')

            global result_15
            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result_15 = True
                fail_log = None
            else:
                result_15 = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result_15, fail_log=fail_log)
            return "PASS" if result_15 else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_16(self):
        try:
            uuid = '9a0bb1c8-ad1a-435c-9857-de26254509d0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if result_15:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Image incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_20(self):
        try:
            uuid = '2ace49cd-c714-4e6c-a8fc-ae494f61b24b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.page_edit.trim_clip(frame="right") and self.page_edit.trim_clip(frame="left"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Trim fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_21(self):
        uuid = '89c4c006-39de-49b3-8152-3d32058ee865'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            # by pass bug
            self.page_main.swipe_element(L.edit.timeline.timeline_ruler, 'left', 1)
            self.page_main.swipe_element(L.edit.timeline.timeline_ruler, 'right', 100)
            #

            clip = self.element(L.edit.timeline.master_photo(file_photo))
            pic_tgt = self.page_main.h_screenshot(clip)
            pic_src = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_21.png')

            if HCompareImg(pic_tgt, pic_src).keypoint_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_22(self):
        try:
            uuid = '48a4971d-ce32-4169-9aea-bb8a55f9cd47'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clips = self.elements(L.edit.timeline.master_photo(file_photo, 0))
            clip1 = clips[0].rect
            clip2 = clips[1].rect

            if clip1["x"] + clip1["width"] == clip2["x"]:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] end of clip1 = {clip1["x"] + clip1["width"]}, start of clip2 = {clip2["x"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_29(self):
        try:
            uuid = '4ac3df8a-866a-4b1a-9b2f-131828bec003'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            # by pass bug
            self.click(L.edit.timeline.clip())
            #

            if self.page_edit.click_sub_tool('Flip'):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Click "Flip" fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_30(self):
        try:
            uuid = 'f25a6a25-0e02-47e7-a946-ced87e59c5b7'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            time.sleep(5)
            pic_after = self.page_main.h_screenshot()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_30.png')

            global result_30
            if HCompareImg(pic_base, pic_after).full_compare() > 0.98:
                result_30 = True
                fail_log = None
            else:
                result_30 = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result_30, fail_log=fail_log)
            return "PASS" if result_30 else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_31(self):
        try:
            uuid = '9fdbe069-5de1-4c45-bb21-d3ea110a0342'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if result_30:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Image incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_8(self):
        try:
            uuid = 'a1963b21-6657-428a-8d7c-e364759ff8f7'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            global file_music
            file_music = "wav.wav"
            self.click(L.edit.timeline.clip_audio(file_music))

            if self.page_edit.is_sub_tool_exist("Split"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find "Split"'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_9(self):
        try:
            uuid = 'edf7a556-0c94-4873-8964-f3607bb7bea6'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clip = self.element(L.edit.pip.clip_audio(file_music)).rect
            x = clip["x"] + clip["width"] // 2
            self.page_main.h_swipe_playhead(x)
            self.page_edit.click_sub_tool("Split")
            playhead = self.element(L.edit.timeline.playhead).rect
            playhead_center = playhead["x"] + playhead["width"] // 2
            x_after = self.element(L.edit.pip.clip_audio(file_music, 2)).rect["x"]

            if x_after - playhead_center < 10:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Split fail: playhead_center = {playhead_center}, x_after = {x_after}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_10(self):
        try:
            uuid = '4c5605cb-b555-49e2-98af-42f218648b7d'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.is_exist(L.edit.pip.audio_thumbnail(file_music, 2)):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find the thumbnail of music clip'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_23(self):
        try:
            uuid = 'cf534cbd-b813-4ff4-b4e5-8f6d78d8d038'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)
            clip = L.edit.pip.clip_audio(file_music)

            if self.page_edit.trim_clip(clip, frame="right") and self.page_edit.trim_clip(clip, frame="left"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Trim fail'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_24(self):
        try:
            uuid = 'd08f9e0a-2f6c-4671-9337-360023460dd2'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if self.is_exist(L.edit.pip.audio_thumbnail(file_music, 2)):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find the thumbnail of music clip'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_25(self):
        try:
            uuid = '4afec38c-bc92-4b82-9f80-0f34c02668b1'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            clips = self.elements(L.edit.pip.clip_audio(file_music, 0))
            clip1 = clips[0].rect
            clip2 = clips[1].rect

            if clip2["x"] > clip1["x"] + clip1["width"]:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] end of clip1 = {clip1["x"] + clip1["width"]}, start of clip2 = {clip2["x"]}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_131(self):
        try:
            uuid = '1f282e0d-52ca-4dd5-8f58-901afba122e7'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            for i in range(4):
                if self.click(L.edit.sub_tool.back, timeout=0.1):
                    continue
                else:
                    break

            if self.is_exist(L.edit.preview.watermark):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] cannot find the watermark'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_132(self):
        try:
            uuid = '666bb375-a688-4f90-9dc1-535a374ad165'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            pic_src = self.page_main.get_preview_pic()
            self.click(L.edit.menu.play)
            time.sleep(10)
            pic_tgt = self.page_main.get_preview_pic()

            if not HCompareImg(pic_tgt, pic_src).full_compare() == 1:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_133(self):
        try:
            uuid = 'd21dac5a-a1a4-46e6-a587-1c14512a663c'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            if self.is_exist(L.edit.timeline.playhead_timecode):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find the timecode'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_135(self):
        try:
            uuid = '2653a289-4c3f-44f0-98fd-7496f6a52d0a'
            func_name = inspect.stack()[0][3]
            logger(f"\n[Start] {func_name}")
            case_id = func_name.split("sce_")[1]
            self.report.start_uuid(uuid)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()

            if self.page_main.enter_timeline(default_project_name):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find timeline canvas'

            self.page_edit.click_sub_option_tool("Remove")

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    @report.exception_screenshot
    def test_sce_2_1_1_to_135(self):
        result = {"sce_2_1_1": self.sce_2_1_1(),

                  # Video
                  "sce_2_1_2": self.sce_2_1_2(),
                  "sce_2_1_3": self.sce_2_1_3(),
                  "sce_2_1_4": self.sce_2_1_4(),
                  "sce_2_1_11": self.sce_2_1_11(),
                  "sce_2_1_12": self.sce_2_1_12(),
                  "sce_2_1_13": self.sce_2_1_13(),
                  "sce_2_1_17": self.sce_2_1_17(),
                  "sce_2_1_18": self.sce_2_1_18(),
                  "sce_2_1_19": self.sce_2_1_19(),
                  "sce_2_1_26": self.sce_2_1_26(),
                  "sce_2_1_27": self.sce_2_1_27(),
                  "sce_2_1_28": self.sce_2_1_28(),
                  "sce_2_1_32": self.sce_2_1_32(),
                  "sce_2_1_33": self.sce_2_1_33(),
                  "sce_2_1_34": self.sce_2_1_34(),
                  "sce_2_1_35": self.sce_2_1_35(),
                  "sce_2_1_36": self.sce_2_1_36(),
                  "sce_2_1_37": self.sce_2_1_37(),
                  "sce_2_1_38": self.sce_2_1_38(),
                  "sce_2_1_39": self.sce_2_1_39(),
                  "sce_2_1_40": self.sce_2_1_40(),
                  "sce_2_1_41": self.sce_2_1_41(),
                  "sce_2_1_42": self.sce_2_1_42(),
                  "sce_2_1_43": self.sce_2_1_43(),
                  "sce_2_1_44": self.sce_2_1_44(),
                  "sce_2_1_45": self.sce_2_1_45(),
                  "sce_2_1_46": self.sce_2_1_46(),
                  "sce_2_1_47": self.sce_2_1_47(),

                  # Stabilizer
                  "sce_2_1_48": self.sce_2_1_48(),
                  "sce_2_1_50": self.sce_2_1_50(),
                  "sce_2_1_49": self.sce_2_1_49(),
                  "sce_2_1_51": self.sce_2_1_51(),
                  "sce_2_1_52": self.sce_2_1_52(),

                  "sce_2_1_skip": self.sce_2_1_skip(),

                  "sce_2_1_64": self.sce_2_1_64(),
                  "sce_2_1_62": self.sce_2_1_62(),
                  "sce_2_1_66": self.sce_2_1_66(),
                  "sce_2_1_63": self.sce_2_1_63(),
                  "sce_2_1_65": self.sce_2_1_65(),

                  "sce_2_1_69": self.sce_2_1_69(),
                  "sce_2_1_67": self.sce_2_1_67(),
                  "sce_2_1_71": self.sce_2_1_71(),
                  "sce_2_1_68": self.sce_2_1_68(),
                  "sce_2_1_70": self.sce_2_1_70(),

                  "sce_2_1_79": self.sce_2_1_79(),
                  "sce_2_1_77": self.sce_2_1_77(),
                  "sce_2_1_81": self.sce_2_1_81(),
                  "sce_2_1_78": self.sce_2_1_78(),
                  "sce_2_1_80": self.sce_2_1_80(),

                  "sce_2_1_74": self.sce_2_1_74(),
                  "sce_2_1_72": self.sce_2_1_72(),
                  "sce_2_1_76": self.sce_2_1_76(),
                  "sce_2_1_73": self.sce_2_1_73(),
                  "sce_2_1_75": self.sce_2_1_75(),

                  "sce_2_1_84": self.sce_2_1_84(),
                  "sce_2_1_82": self.sce_2_1_82(),
                  "sce_2_1_86": self.sce_2_1_86(),
                  "sce_2_1_83": self.sce_2_1_83(),
                  "sce_2_1_85": self.sce_2_1_85(),

                  "sce_2_1_89": self.sce_2_1_89(),
                  "sce_2_1_87": self.sce_2_1_87(),
                  "sce_2_1_91": self.sce_2_1_91(),
                  "sce_2_1_88": self.sce_2_1_88(),
                  "sce_2_1_90": self.sce_2_1_90(),

                  "sce_2_1_55": self.sce_2_1_55(),
                  "sce_2_1_56": self.sce_2_1_56(),

                  "sce_2_1_92": self.sce_2_1_92(),
                  "sce_2_1_95": self.sce_2_1_95(),
                  "sce_2_1_93": self.sce_2_1_93(),
                  "sce_2_1_97": self.sce_2_1_97(),
                  "sce_2_1_94": self.sce_2_1_94(),
                  "sce_2_1_96": self.sce_2_1_96(),

                  "sce_2_1_98": self.sce_2_1_98(),
                  "sce_2_1_101": self.sce_2_1_101(),
                  "sce_2_1_99": self.sce_2_1_99(),
                  "sce_2_1_103": self.sce_2_1_103(),
                  "sce_2_1_100": self.sce_2_1_100(),
                  "sce_2_1_102": self.sce_2_1_102(),

                  # Photo
                  "sce_2_1_104": self.sce_2_1_104(),
                  "sce_2_1_107": self.sce_2_1_107(),
                  "sce_2_1_105": self.sce_2_1_105(),
                  "sce_2_1_109": self.sce_2_1_109(),
                  "sce_2_1_106": self.sce_2_1_106(),
                  "sce_2_1_108": self.sce_2_1_108(),

                  "sce_2_1_110": self.sce_2_1_110(),
                  "sce_2_1_113": self.sce_2_1_113(),
                  "sce_2_1_111": self.sce_2_1_111(),
                  "sce_2_1_115": self.sce_2_1_115(),
                  "sce_2_1_112": self.sce_2_1_112(),
                  "sce_2_1_114": self.sce_2_1_114(),
                  "sce_2_1_134": self.sce_2_1_134(),

                  "sce_2_1_117": self.sce_2_1_117(),
                  "sce_2_1_116": self.sce_2_1_116(),
                  "sce_2_1_118": self.sce_2_1_118(),
                  "sce_2_1_119": self.sce_2_1_119(),
                  "sce_2_1_120": self.sce_2_1_120(),
                  "sce_2_1_121": self.sce_2_1_121(),
                  "sce_2_1_122": self.sce_2_1_122(),
                  "sce_2_1_123": self.sce_2_1_123(),
                  "sce_2_1_124": self.sce_2_1_124(),
                  "sce_2_1_125": self.sce_2_1_125(),
                  "sce_2_1_126": self.sce_2_1_126(),
                  "sce_2_1_128": self.sce_2_1_128(),
                  "sce_2_1_127": self.sce_2_1_127(),
                  "sce_2_1_129_130": self.sce_2_1_129_130(),

                  "sce_2_1_5": self.sce_2_1_5(),
                  "sce_2_1_6": self.sce_2_1_6(),
                  "sce_2_1_7": self.sce_2_1_7(),
                  "sce_2_1_14": self.sce_2_1_14(),
                  "sce_2_1_15": self.sce_2_1_15(),
                  "sce_2_1_16": self.sce_2_1_16(),
                  "sce_2_1_20": self.sce_2_1_20(),
                  "sce_2_1_21": self.sce_2_1_21(),
                  "sce_2_1_22": self.sce_2_1_22(),
                  "sce_2_1_29": self.sce_2_1_29(),
                  "sce_2_1_30": self.sce_2_1_30(),
                  "sce_2_1_31": self.sce_2_1_31(),

                  # Music
                  "sce_2_1_8": self.sce_2_1_8(),
                  "sce_2_1_9": self.sce_2_1_9(),
                  "sce_2_1_10": self.sce_2_1_10(),
                  "sce_2_1_23": self.sce_2_1_23(),
                  "sce_2_1_24": self.sce_2_1_24(),
                  "sce_2_1_25": self.sce_2_1_25(),

                  "sce_2_1_131": self.sce_2_1_131(),
                  "sce_2_1_132": self.sce_2_1_132(),
                  "sce_2_1_133": self.sce_2_1_133(),
                  "sce_2_1_135": self.sce_2_1_135(),

                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
