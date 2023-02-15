import sys
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
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_02_33:
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
        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)
        self.click = self.page_main.h_click
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

    def sce_02_33_01(self):
        item_id = '01_02_01'
        uuid = 'c2420360-95d7-4591-afbc-33ae908c62f0'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(skip_media=True)
        self.page_edit.click_tool("Photo")
        self.page_media.select_local_photo(self.test_material_folder, 'photo.jpg')



        self.page_main.h_click(L.main.project.new_project)
        import datetime
        dt = datetime.datetime.today()
        project_name_default = 'Project {:02d}-{:02d}(1)'.format(dt.month, dt.day)
        project_name = self.page_main.h_get_element(L.main.project.name).text

        if project_name == project_name_default:
            result = True
        else:
            result = False
            logger(f'[Info] Project Name: {project_name}')
            logger(f'[Info] Default Project Name: {project_name_default}')
            logger('\n[Fail] Project Name incorrect')
        self.report.new_result(uuid, result)
        return result

    def sce_01_02_02(self):
        item_id = '01_02_02'
        uuid = '8522a2ed-042c-4da4-bed6-8fb2512a6b2b'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.h_click(L.main.project.ratio_9_16)
        self.page_main.h_click(L.import_media.media_library.back)
        if self.page_edit.preview_ratio() == '9_16':
            result = True
        else:
            result = False
            logger(f'[Fail] Project ratio = {self.page_edit.preview_ratio()}')

        self.report.new_result(uuid, result)
        return result

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_01_02_01_to_33(self):
        try:
            result = {
                "sce_01_02_01": self.sce_01_02_01(),
                "sce_01_02_02": self.sce_01_02_02()
            }
            pprint(result)
        except Exception as err:
            logger(f'[Error] {err}')
