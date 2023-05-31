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


class Test_SFT_Scenario_05_15:
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

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        self.report.set_driver(driver)
        driver.driver.launch_app()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_05_15_1(self):
        result = {}

        # sce_05_15_1
        item_id = '05_15_1'
        uuid = '2b94f7e6-0550-4942-bdfa-ea7de20d3179'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline()
        self.page_edit.intro_video.enter_intro()
        self.page_edit.intro_video.edit_1st_template()
        self.page_edit.intro_video.customize()
        result[item_id] = self.page_edit.intro_video.add_to_video_in_intro()

        self.report.new_result(uuid, result[item_id])

        # sce_05_15_2
        item_id = '05_15_2'
        uuid = 'cb72109e-8791-43ca-a22e-36664f0e0e38'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_edit.intro_video.enter_intro()
        self.page_edit.intro_video.edit_1st_template()
        self.page_edit.intro_video.customize()
        result[item_id] = self.page_edit.intro_video.share_template()

        self.report.new_result(uuid, result[item_id])

        # print result
        pprint(result)
