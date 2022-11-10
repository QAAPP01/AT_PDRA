import sys
from os.path import dirname as dir
from os import path
import subprocess
from pprint import pprint

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

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
from ATFramework_aPDR.pages.locator.locator_type import find_string, id
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage

sys.path.insert(0, (dir(dir(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_05_16:
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
        self.driver.implicit_wait(0.2)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Done] Teardown")
        self.driver.stop_driver()

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_05_16_16(self):
        result = {}

        # sce_05_16_16
        item_id = '05_16_16'
        uuid = 'd6cd4a33-715a-4eae-ad88-271e44b91482'
        logger(f"\n[Start] sce_{item_id}")
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()
        self.page_main.enter_timeline(item_id)
        self.page_edit.intro_video.enter_intro()
        self.page_edit.intro_video.edit_1st_template()
        self.page_edit.intro_video.customize()
        self.page_edit.intro_video.share_template()
        terms = self.page_edit.get_element(id('terms_of_use'))
        x = terms.location["x"] + terms.size["width"] * 0.9
        y = terms.location["y"] + terms.size["height"] / 2
        actions = ActionChains(self.driver.driver)
        actions.w3c_actions = ActionBuilder(self.driver.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down().release()
        actions.perform()
        result[item_id] = self.page_edit.h_is_exist(id('contentMessage'))

        self.report.new_result(uuid, result[item_id])

        # print result
        pprint(result)
