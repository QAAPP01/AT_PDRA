import inspect
import sys, os, glob
from os.path import dirname
from os import path
import subprocess
from pprint import pprint
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *

from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.ATFramework.utils.log import logger
import pytest
import time

from main import deviceName
from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage, HCompareImg

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

class Test_SFT_Scenario_02_01:
    @pytest.fixture(autouse=True)
    def initial(self):

        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger("[Start] Init driver session")
        desired_caps = {}
        desired_caps.update(app_config.cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        if desired_caps['udid'] == 'auto':
            desired_caps['udid'] = deviceName
        logger(f"[Info] caps={desired_caps}")
        self.report = report
        self.device_udid = desired_caps['udid']
        # ---- local mode > end ----
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

        # retry 3 time if create driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                                       desired_caps)
                if self.driver:
                    logger("\n[Done] Driver created!")
                    break
                else:
                    raise Exception("\n[Fail] Create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
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

        self.report.set_driver(self.driver)
        self.driver.driver.start_recording_screen()
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(0.1)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Stop] Teardown")
        self.driver.stop_driver()

    def sce_2_1_1(self):
        uuid = '923cc0c9-f6d8-4f65-8076-f1b585d5b1a3'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        import datetime
        dt = datetime.datetime.today()
        default_project_name = 'Project {:02d}-{:02d}'.format(dt.month, dt.day)
        self.page_main.enter_launcher()

        if self.page_main.enter_timeline(default_project_name):
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Cannot find timeline canvas'
            logger(fail_log)

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_2_1_2(self):
        uuid = 'a6faa123-8177-429b-9202-14c21e8905c0'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        global video_file
        video_file = 'mp4.mp4'
        self.page_media.add_master_media('Video', self.test_material_folder, video_file)
        self.click(L.edit.timeline.master_clip)

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

            clip = self.element(L.edit.timeline.master_video(video_file)).rect
            x = clip["x"] + clip["width"]//2
            self.page_main.h_swipe_playhead(x)
            self.page_edit.click_sub_tool("Split")
            playhead = self.element(L.edit.timeline.playhead).rect
            playhead_center = playhead["x"] + playhead["width"]//2
            x_after = self.elements(L.edit.timeline.master_video(video_file))[1].rect["x"]

            if x_after == playhead_center:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Split fail: playhead_center = {playhead_center}, x_after = {x_after}'
                logger(fail_log)

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

            clip = self.elements(L.edit.timeline.master_video_thumbnail(video_file, 2))[0]
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
        try:
            uuid = '6805d7b3-1775-4b5f-930f-159965846428'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            time.sleep(2)
            pic_after = self.page_main.h_screenshot()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_12.png')

            global result_12
            if HCompareImg(pic_base, pic_after).full_compare() > 0.98:
                result_12 = True
                fail_log = None
            else:
                result_12 = False
                fail_log = f'\n[Fail] Images are different'

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




    def sce_2_1_5(self):
        try:
            uuid = 'a29fa42b-7da3-47ae-8f5b-8d3d9a8b4dfb'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.page_main.h_swipe_playhead(10, 1)
            self.page_media.add_master_media('Photo', self.test_material_folder, 'photo.jpg')
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

            clip = self.element(L.edit.timeline.master_photo('photo.jpg')).rect
            x = clip["x"] + clip["width"]//2
            self.page_main.h_swipe_playhead(x)
            self.page_edit.click_sub_tool("Split")
            playhead = self.element(L.edit.timeline.playhead).rect
            playhead_center = playhead["x"] + playhead["width"]//2
            x_after = self.elements(L.edit.timeline.master_photo('photo.jpg'))[1].rect["x"]

            if x_after == playhead_center:
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

            clip = self.elements(L.edit.timeline.master_photo('photo.jpg'))[1]
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

            pic_after = self.page_main.h_screenshot()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_15.png')

            global result_14
            if HCompareImg(pic_base, pic_after).full_compare() > 0.98:
                result_14 = True
                fail_log = None
            else:
                result_14 = False
                fail_log = f'\n[Fail] Images are different'

            self.report.new_result(uuid, result_14, fail_log=fail_log)
            return "PASS" if result_14 else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_2_1_16(self):
        try:
            uuid = '9a0bb1c8-ad1a-435c-9857-de26254509d0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            if result_14:
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

            self.page_edit.click_tool("Audio")
            self.click(find_string("Music"))
            self.click(L.import_media.music_library.local)
            self.click(find_string(self.test_material_folder))
            global file_name
            file_name = self.element(L.import_media.music_library.file_name).text
            self.click(L.import_media.music_library.add)
            self.click(L.edit.pip.clip_audio(file_name))

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

            clip = self.element(L.edit.pip.clip_audio(file_name)).rect
            x = clip["x"] + clip["width"]//2
            self.page_main.h_swipe_playhead(x)
            self.page_edit.click_sub_tool("Split")
            playhead = self.element(L.edit.timeline.playhead).rect
            playhead_center = playhead["x"] + playhead["width"]//2
            x_after = self.element(L.edit.pip.clip_audio(file_name, 2)).rect["x"]

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

            if self.is_exist(L.edit.pip.audio_thumbnail(file_name, 2)):
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



    @report.exception_screenshot
    def test_sce_2_1_1_to_135(self):
        try:
            result = {
                "sce_2_1_1": self.sce_2_1_1(),
                "sce_2_1_2": self.sce_2_1_2(),
                "sce_2_1_3": self.sce_2_1_3(),
                "sce_2_1_4": self.sce_2_1_4(),
                "sce_2_1_11": self.sce_2_1_11(),
                "sce_2_1_12": self.sce_2_1_12(),
                "sce_2_1_13": self.sce_2_1_13(),
                "sce_2_1_5": self.sce_2_1_5(),
                "sce_2_1_6": self.sce_2_1_6(),
                "sce_2_1_7": self.sce_2_1_7(),
                "sce_2_1_14": self.sce_2_1_14(),
                "sce_2_1_15": self.sce_2_1_15(),
                "sce_2_1_16": self.sce_2_1_16(),
                "sce_2_1_8": self.sce_2_1_8(),
                "sce_2_1_9": self.sce_2_1_9(),
                "sce_2_1_10": self.sce_2_1_10()
            }
            pprint(result)
        except Exception as err:
            logger(f'[Error] {err}')

    @report.exception_screenshot
    def test_sce_2_1_32(self):
        result = {}

        # sce_2_1_32
        item_id = '2_1_32'
        uuid = '4a9dcf18-a3a8-414f-839f-bc4b085f79c2'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(skip_media=False)
        self.page_media.select_local_video(self.test_material_folder, 'video.mp4')
        self.page_main.h_click(aid('[AID]TimeLineVideo_video.mp4'))
        original_pic = self.page_main.get_preview_pic()
        self.page_edit.click_sub_tool('Crop', timeout=0.1)
        self.page_main.h_click(L.edit.crop.btn_free)
        boundary_rect = self.page_main.h_get_element(L.edit.crop.boundary).rect
        end_x = boundary_rect['x'] + boundary_rect['width'] * 0.7
        end_y = boundary_rect['y'] + boundary_rect['height'] * 0.7
        self.page_edit.h_drag_element(L.edit.crop.right_top, end_x, end_y)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_32.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_2_1_33
        item_id = '2_1_33'
        uuid = 'af6b9dc7-3318-47bd-93e9-cdf5e452b326'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_free)
        boundary_rect = self.page_main.h_get_element(L.edit.crop.boundary).rect
        end_x = boundary_rect['x'] + boundary_rect['width'] * 0.7
        end_y = boundary_rect['y'] + boundary_rect['height'] * 0.7
        self.page_edit.h_drag_element(L.edit.crop.right_top, end_x, end_y)
        self.page_main.h_click(L.edit.crop.cancel)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_32.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_2_1_34
        item_id = '2_1_34'
        uuid = '789d8fa7-6027-47f5-a979-c165c4dc6028'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_9_16)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_34.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_2_1_35
        item_id = '2_1_35'
        uuid = '15c5cdc8-d471-4df4-9ae8-bfd5dcc32067'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')

        # # Bug workaround
        # self.page_main.h_swipe_element(L.edit.crop.btn_1_1, L.edit.crop.btn_4_5, 1)
        # self.page_main.h_click(L.edit.crop.btn_free)
        # self.page_main.h_click(L.edit.crop.btn_9_16)


        self.page_main.h_click(L.edit.crop.btn_1_1)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_35.png')

        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])


        # sce_2_1_36
        item_id = '2_1_36'
        uuid = '8683f4f6-9110-4577-be14-3b7174f60f32'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_4_5)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_36.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])


        # sce_2_1_37
        item_id = '2_1_37'
        uuid = 'a962eb0d-a799-4dac-918f-b287ee3244c3'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_16_9)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_37.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])


        # sce_2_1_38
        item_id = '2_1_38'
        uuid = '4d9b5fae-140c-4f00-9260-088eec60dcb5'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_4_3)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_38.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_2_1_39
        item_id = '2_1_39'
        uuid = 'd9106fce-f2b0-4b92-bd1f-ce3eb0e185dd'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_swipe_element(L.edit.crop.btn_1_1, L.edit.crop.btn_4_3, 1)
        self.page_main.h_click(L.edit.crop.btn_original)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_39.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_2_1_40
        item_id = '2_1_40'
        uuid = '7f642e5d-1ef0-44a8-8d01-5de9d10a933c'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_swipe_element(L.edit.crop.btn_4_5, L.edit.crop.btn_free, 1)
        self.page_main.h_click(L.edit.crop.btn_3_4)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '2_1_40.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_2_1_41
        item_id = '2_1_41'
        uuid = '00b2177a-05c4-411a-8c68-0b88cd3ce8bd'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        result[item_id] = not self.page_main.h_is_exist(L.edit.crop.play_pause)

        self.report.new_result(uuid, result[item_id])

        # sce_2_1_42
        try:
            item_id = '2_1_42'
            uuid = '8e379056-3eba-4d4f-8601-9b321f014a46'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            slider_rect = self.page_main.h_get_element(L.edit.crop.slider).rect
            x = slider_rect['x'] + slider_rect['width'] / 2
            y = slider_rect['y'] + slider_rect['height'] / 2
            self.page_main.h_tap(x, y)
            time_code = self.page_main.h_get_element(L.edit.crop.time_code).text
            result[item_id] = True if time_code.split('/')[0] == '00:03' else False
            self.page_main.h_click(L.edit.crop.apply)

            self.report.new_result(uuid, result[item_id])
        except Exception as err:
            logger(f'[Error] {err}')

        # sce_2_1_43
        item_id = '2_1_43'
        uuid = 'e38aad9a-a25a-4c41-8598-923c01c74b4a'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.reset)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = original_pic
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])
        # print result
        pprint(result)