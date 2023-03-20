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
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_02_03:
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

    def sce_02_03_16(self):
        try:
            uuid = '2e869d26-d734-476c-a948-8fb7bcf3b64b'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            import datetime
            dt = datetime.datetime.today()
            default_project_name = 'Project {:02d}-{:02d}'.format(dt.month, dt.day)
            self.page_main.enter_launcher()
            self.page_main.enter_timeline(default_project_name)

            self.page_media.add_master_media('photo', self.test_material_folder, '9_16')
            self.page_media.add_pip_media('photo', self.test_material_folder, '16_9')
            self.page_edit.click_tool("Aspect Ratio")
            global image_original
            image_original = self.page_main.get_preview_pic()

            self.click(L.edit.aspect_ratio.ratio_9_16)

            if self.page_edit.preview_ratio() == "9_16":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_02_03_17(self):
        try:
            uuid = '6b9cf2f2-87ab-4738-8dc4-614223eb8df0'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_17.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_02_03_18(self):
        try:
            uuid = '42d6c14a-c2d9-4d54-a888-85c6337e33e4'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_1_1)

            if self.page_edit.preview_ratio() == "1_1":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_02_03_19(self):
        try:
            uuid = 'f35ceb9e-f37c-42f8-9bfe-b9f23da0d1a9'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_19.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_02_03_20(self):
        try:
            uuid = '9e04fdc7-beb5-442f-be6f-bedb66909e8f'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_21_9)

            if self.page_edit.preview_ratio() == "21_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            return "ERROR"

    def sce_02_03_21(self):
        try:
            uuid = '8bb03dce-1b63-4f9b-96cf-2e7882d02e76'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_21.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_22(self):
        try:
            uuid = 'c0edb49c-02f5-4fcb-a404-3488077f466c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_4_5)

            if self.page_edit.preview_ratio() == "4_5":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_23(self):
        try:
            uuid = '0ab23f49-c1ba-402a-97fe-714e84346b76'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_23.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_24(self):
        try:
            uuid = 'd5acb1cd-5810-44d8-ba0e-571c988a7ae4'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_16_9)

            if self.page_edit.preview_ratio() == "16_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_25(self):
        try:
            uuid = '6e4025cd-f203-4685-8e49-e6f4bb5b7bdf'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = image_original

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_26(self):
        try:
            uuid = 'b17ecaa4-c427-4337-95f9-cd506284b85a'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.timeline.master_clip)
            self.page_edit.click_sub_tool("Fit & Fill")
            self.click(L.edit.fit_and_fill.btn_fill)
            global image_original
            image_original = self.page_main.get_preview_pic()
            self.click(L.edit.settings.menu)
            self.click(L.edit.settings.aspect_ratio)

            self.click(L.edit.aspect_ratio.ratio_9_16)

            if self.page_edit.preview_ratio() == "9_16":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_27(self):
        try:
            uuid = 'faef9b26-5263-432d-9cf9-5b0765bf7ba2'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_27.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_28(self):
        try:
            uuid = 'c23658ab-d37c-471c-93a9-a67f4c7b205c'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_1_1)

            if self.page_edit.preview_ratio() == "1_1":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_29(self):
        try:
            uuid = 'fd2fc883-944e-40af-91f2-12258ad5bd69'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_29.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_30(self):
        try:
            uuid = 'd6ceb6f0-fffd-44c4-8fb1-b301315add5e'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_21_9)

            if self.page_edit.preview_ratio() == "21_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_31(self):
        try:
            uuid = '679139c0-c69d-43dd-b000-f9551adb6857'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_31.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_32(self):
        try:
            uuid = 'e4555e47-4e3a-42a9-b884-1d06d0cc2b5f'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_4_5)

            if self.page_edit.preview_ratio() == "4_5":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_33(self):
        try:
            uuid = '51dc22bb-e3c4-4ec3-a75d-287002a6e085'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_33.png')

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_34(self):
        try:
            uuid = '775129a4-9c40-46ba-95d3-da00f125b4b7'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            self.click(L.edit.aspect_ratio.ratio_16_9)

            if self.page_edit.preview_ratio() == "16_9":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Project ratio is incorrect'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def sce_02_03_35(self):
        try:
            uuid = 'c7eba5c2-11c8-4258-a405-945142cf77d8'
            logger(f"\n[Start] {inspect.stack()[0][3]}")
            self.report.start_uuid(uuid)

            pic_after = self.page_main.get_preview_pic()
            pic_base = image_original

            if HCompareImg(pic_base, pic_after).full_compare() > 0.97:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are different'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f'[Error] {err}')
            return "ERROR"

    def test_sce_02_03_16_to_35(self):
        result = {"sce_02_03_16": self.sce_02_03_16(),
                  "sce_02_03_17": self.sce_02_03_17(),
                  "sce_02_03_18": self.sce_02_03_18(),
                  "sce_02_03_19": self.sce_02_03_19(),
                  "sce_02_03_20": self.sce_02_03_20(),
                  "sce_02_03_21": self.sce_02_03_21(),
                  "sce_02_03_22": self.sce_02_03_22(),
                  "sce_02_03_23": self.sce_02_03_23(),
                  "sce_02_03_24": self.sce_02_03_24(),
                  "sce_02_03_25": self.sce_02_03_25(),
                  "sce_02_03_26": self.sce_02_03_26(),
                  "sce_02_03_27": self.sce_02_03_27(),
                  "sce_02_03_28": self.sce_02_03_28(),
                  "sce_02_03_29": self.sce_02_03_29(),
                  "sce_02_03_30": self.sce_02_03_30(),
                  "sce_02_03_31": self.sce_02_03_31(),
                  "sce_02_03_32": self.sce_02_03_32(),
                  "sce_02_03_33": self.sce_02_03_33(),
                  "sce_02_03_34": self.sce_02_03_34(),
                  "sce_02_03_35": self.sce_02_03_35()
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_310(self):
        result = {}

        # sce_02_03_310
        item_id = '02_03_310'
        uuid = '72f8d373-9b32-4dad-bf16-81bce0cb87a7'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_main.enter_launcher()
        self.page_main.enter_timeline()

        self.page_edit.click_tool('Photo')
        if not self.page_media.select_local_photo(self.test_material_folder, '9_16.jpg'):
            return False
        self.page_edit.click_tool('Effect')
        self.page_edit.h_click(find_string('Adjustment'))
        self.page_edit.h_click(L.effect.sub_menu.add)
        self.page_edit.h_click(L.edit.try_before_buy.try_it, 1)
        self.page_edit.click_sub_tool('Brightness')
        self.page_edit.h_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_310.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '100'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_311
        item_id = '02_03_311'
        uuid = '4f7e1155-33ab-4d1c-b080-e6ecf11af385'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Contrast')
        self.page_edit.h_set_slider(0)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_311.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '-100'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_312
        item_id = '02_03_312'
        uuid = 'f2482eb4-c4f4-42ae-9ae0-fa9b48305eaa'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Saturation')
        self.page_edit.h_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_312.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '200'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_313
        item_id = '02_03_313'
        uuid = 'd7723b46-9d61-442b-a905-0f3be2e45010'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Hue')
        self.page_edit.h_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_313.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '200'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_314
        item_id = '02_03_314'
        uuid = '21609f3c-7e8e-4498-9d81-8002f059998f'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Temp')
        self.page_edit.h_set_slider(0.7)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id + '.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '70'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_315
        item_id = '02_03_315'
        uuid = '0f261b4a-1644-41d6-8534-6f94570712ae'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Tint')
        self.page_edit.h_set_slider(0.5)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id + '.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '50'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        # sce_02_03_316
        item_id = '02_03_316'
        uuid = 'e39097dc-d519-4816-8980-bdff9e19f13c'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)
        self.page_edit.h_click(L.edit.adjust_sub.reset)
        self.page_edit.click_sub_tool('Sharpness')
        self.page_edit.h_set_slider(0.645)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id + '.png')
        result_photo = True if HCompareImg(pic_base, pic_after).full_compare() > 0.9 else False
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '129'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        pprint(result)
