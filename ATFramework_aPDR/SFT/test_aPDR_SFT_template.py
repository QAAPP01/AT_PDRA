import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest

report = ''
from .conftest import PACKAGE_NAME
pdr_package = PACKAGE_NAME


class Test_Template:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        
        global report
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        self.
        # ---- local mode > end ----
                                                              
        # retry 3 time if craete driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',desired_caps)
                if self.driver:
                    logger("driver created!")
                    break
                else:
                    raise Exception("create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
                
        self.report.set_driver(self.driver)
        self.driver.start_app(pdr_package)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.media_page = PageFactory().get_page_object("import_media", self.driver)
        self.effect_page = PageFactory().get_page_object("effect", self.driver)

        self.driver.implicit_wait(15)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    #@pytest.mark.skip
    def test_create_project(self):
        page = self.main_page
        page.project_click_empty()
        page.project_set_name("demo")
        self.report.add_result("c0947d88-07c6-441f-990c-b673391a5829", True, "sample")
        page.project_set_16_9()
        page.project_click_ok()