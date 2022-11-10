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
from ATFramework_aPDR.pages.locator.locator_type import find_string
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

sys.path.insert(0, (dir(dir(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

file_name = 'material.jpg'
file_path = r'C:\Users\hausen_lin\PycharmProjects\PDRA\PDRa_portrait_3118\ATFramework_aPDR\SFT\test_material\material.jpg'

class Test_SFT_Scenario_02_03:
    @pytest.fixture(autouse=True)
    def initial(self):
        # Copy material
        material_path = 'storage/emulated/0/Pictures/0_Test_Material'
        no_dir = subprocess.call(['adb', 'shell', 'ls', material_path], stdout=subprocess.DEVNULL,
                                 stderr=subprocess.STDOUT)
        if no_dir:
            logger(f"[Info] Create {material_path}")
            subprocess.call(['adb', 'shell', 'mkdir', material_path])

        no_photo = subprocess.call(['adb', 'shell', 'ls', material_path + '/' + file_name], stdout=subprocess.DEVNULL,
                                   stderr=subprocess.STDOUT)
        if no_photo:
            logger("[Info] Start copying file ...")
            copy = subprocess.call(
                ['adb', 'push', file_path, material_path])
            if not copy:
                logger(f"[Info] Copy file to {material_path} completed！\n")
            else:
                logger(f"[Info] Copy file to {material_path} failed！\n")

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
        self.driver.implicit_wait(0.2)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Done] Teardown")
        self.driver.stop_driver()

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
        if self.page_edit.h_click(L.main.project.shopping_cart, 1):
            self.page_edit.h_click(L.main.subscribe.iap_monthly)
            self.page_edit.h_click(L.main.subscribe.continue_btn)
            self.page_edit.h_click(find_string('Subscribe'))
            self.page_edit.h_click(find_string('Not now'), 1)
        self.page_main.enter_timeline('sce_02_03_310')
        self.page_edit.settings.enable_fileName()
        self.driver.driver.back()
        self.driver.driver.back()
        self.page_edit.click_tool('Photo')
        if not self.page_media.select_local_photo('0_Test_Material', file_name):
            return False
        self.page_edit.click_tool('Effect')
        self.page_edit.h_click(find_string('Adjustment'))
        self.page_edit.h_click(L.effect.sub_menu.add)
        self.page_edit.h_click(L.edit.try_before_buy.try_it, 1)
        self.page_edit.click_sub_tool('Brightness')
        self.page_edit.opacity_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_310.png')
        result_photo = CompareImage(pic_base, pic_after, 7).compare_image()
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
        self.page_edit.opacity_set_slider(0)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_311.png')
        result_photo = CompareImage(pic_base, pic_after, 7).compare_image()
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
        self.page_edit.opacity_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_312.png')
        result_photo = CompareImage(pic_base, pic_after, 7).compare_image()
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
        self.page_edit.opacity_set_slider(1)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', '02_03_313.png')
        result_photo = CompareImage(pic_base, pic_after, 7).compare_image()
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
        self.page_edit.opacity_set_slider(0.7)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id+'.png')
        result_photo = CompareImage(pic_base, pic_after, 7).compare_image()
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
        self.page_edit.opacity_set_slider(0.5)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id + '.png')
        result_photo = CompareImage(pic_base, pic_after, 7).compare_image()
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
        self.page_edit.opacity_set_slider(0.645)
        pic_after = self.page_edit.get_preview_pic()
        pic_base = path.join(path.dirname(__file__), 'test_material', '02_03', item_id + '.png')
        result_photo = CompareImage(pic_base, pic_after, 7).compare_image()
        result_value = self.page_edit.h_get_element(L.edit.adjust_sub.number).text == '129'
        logger(f"[Info] result_photo = {result_photo}, result_value = {result_value}")
        result[item_id] = result_photo and result_value
        self.report.new_result(uuid, result[item_id])

        pprint(result)
