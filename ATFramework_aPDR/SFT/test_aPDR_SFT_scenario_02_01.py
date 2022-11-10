import sys
from os.path import dirname as dir
from os import path
import subprocess
from pprint import pprint
from ATFramework_aPDR.pages.locator import locator as L

from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.ATFramework.utils.log import logger
import pytest
import time
from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import find_string, aid, id
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

sys.path.insert(0, (dir(dir(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_02_01:
    @pytest.fixture(autouse=True)
    def initial(self):

        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger("\n[Start] Init driver session")
        desired_caps = {}
        desired_caps.update(app_config.cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        if desired_caps['udid'] == 'auto':
            del desired_caps['udid']
        logger(f"\n[Info] caps={desired_caps}")
        self.report = report
        self.device_udid = DRIVER_DESIRED_CAPS['udid']
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

        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.report.set_driver(self.driver)
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(0.1)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Done] Teardown")
        self.driver.stop_driver()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_01_32(self):
        result = {}

        # sce_02_01_32
        item_id = '02_01_32'
        uuid = '4a9dcf18-a3a8-414f-839f-bc4b085f79c2'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(item_id, skip_media=False)
        self.page_media.select_local_video('0_Test_Material', 'video.mp4')
        self.page_main.h_click(aid('[AID]TimeLineVideo_video.mp4'))
        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_free)
        boundary_rect = self.page_main.h_get_element(L.edit.crop.boundary).rect
        end_x = boundary_rect['x'] + boundary_rect['width'] * 0.7
        end_y = boundary_rect['y'] + boundary_rect['height'] * 0.7
        self.page_edit.h_drag_element(L.edit.crop.right_top, end_x, end_y)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_32.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_02_01_33
        item_id = '02_01_33'
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
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_32.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_02_01_34
        item_id = '02_01_34'
        uuid = '789d8fa7-6027-47f5-a979-c165c4dc6028'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_9_16)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_34.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_02_01_35
        item_id = '02_01_35'
        uuid = '15c5cdc8-d471-4df4-9ae8-bfd5dcc32067'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_1_1)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_35.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])


        # sce_02_01_36
        item_id = '02_01_36'
        uuid = '8683f4f6-9110-4577-be14-3b7174f60f32'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_4_5)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_36.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])


        # sce_02_01_37
        item_id = '02_01_37'
        uuid = 'a962eb0d-a799-4dac-918f-b287ee3244c3'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_16_9)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_37.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])


        # sce_02_01_38
        item_id = '02_01_38'
        uuid = '4d9b5fae-140c-4f00-9260-088eec60dcb5'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.btn_4_3)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_38.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_02_01_39
        item_id = '02_01_39'
        uuid = 'd9106fce-f2b0-4b92-bd1f-ce3eb0e185dd'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_swipe_element(L.edit.crop.btn_1_1, L.edit.crop.btn_4_3, 1)
        self.page_main.h_click(L.edit.crop.btn_original)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_39.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_02_01_40
        item_id = '02_01_40'
        uuid = '7f642e5d-1ef0-44a8-8d01-5de9d10a933c'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_swipe_element(L.edit.crop.btn_4_5, L.edit.crop.btn_free, 1)
        self.page_main.h_click(L.edit.crop.btn_3_4)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_40.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])

        # sce_02_01_41
        item_id = '02_01_41'
        uuid = '00b2177a-05c4-411a-8c68-0b88cd3ce8bd'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        while not self.page_main.h_get_element(L.edit.crop.play_pause).get_attribute('clickable') == 'true':
            self.page_main.h_get_element(L.edit.crop.play_pause).get_attribute('clickable')
        self.page_main.h_click(L.edit.crop.play_pause)
        self.page_main.h_click(L.edit.crop.play_pause)
        time_code = self.page_main.h_get_element(L.edit.crop.time_code).text
        result[item_id] = True if time_code.split('/')[0] == '00:01' else False

        self.report.new_result(uuid, result[item_id])

        # sce_02_01_42
        item_id = '02_01_42'
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

        # sce_02_01_43
        item_id = '02_01_43'
        uuid = 'e38aad9a-a25a-4c41-8598-923c01c74b4a'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.click_sub_tool('Crop')
        self.page_main.h_click(L.edit.crop.reset)
        self.page_main.h_click(L.edit.crop.apply)
        pic_after = self.page_main.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_01', '02_01_43.png')
        result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

        self.report.new_result(uuid, result[item_id])
        # print result
        pprint(result)
