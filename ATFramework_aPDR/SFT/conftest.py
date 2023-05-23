import pytest
import sys
from os.path import dirname as dir
sys.path.insert(0,(dir(dir(dir(__file__)))))
from ATFramework_aPDR.ATFramework.utils import MyReport
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.page_factory import PageFactory
import main

DRIVER_DESIRED_CAPS = ''
REPORT_INSTANCE = MyReport(tr_number=main.tr_number, previous_tr_number=main.previous_tr_number)
DEFAULT_BROWSER = 'com.android.chrome'
platform_type = 'Android'
PACKAGE_NAME = main.package_name
TEST_MATERIAL_FOLDER = '00PDRa_Testing_Material'
TEST_MATERIAL_FOLDER_01 = '01PDRa_Testing_Material'

def pytest_addoption(parser):
    parser.addoption("--udid", action="store", default="auto", help="device unique udid")
    parser.addoption("--systemPort", action="store", default="8200", help="uiautomator2 port")


@pytest.fixture(scope='session')
def udid(request):
    return request.config.getoption("udid")

@pytest.fixture(scope='session')
def systemPort(request):
    return request.config.getoption("systemPort")

@pytest.fixture(scope='session', autouse=True)
def report_initial(udid):
    global REPORT_INSTANCE
    logger('report_init, udid='+ udid)
    REPORT_INSTANCE.set_udid(udid)
    logger("report = %s" % REPORT_INSTANCE)
    return True

@pytest.fixture(scope='class', autouse=True)
def driver_get_desiredcap(udid, systemPort):
    global DRIVER_DESIRED_CAPS
    if platform_type == 'Android':
        DRIVER_DESIRED_CAPS = {'udid': str(udid), 'systemPort': str(systemPort)}
    else:
        DRIVER_DESIRED_CAPS = {'udid': str(udid)}
    # print('driver_get_desiredcap, caps=', DRIVER_DESIRED_CAPS)
    return True


@pytest.fixture
def driver():
    import os
    from ATFramework_aPDR.ATFramework.utils.log import logger
    from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
    from ATFramework_aPDR.configs import app_config
    from ATFramework_aPDR.configs import driver_config
    from main import deviceName

    desired_caps = {}
    desired_caps.update(app_config.cap)
    desired_caps.update(DRIVER_DESIRED_CAPS)
    if desired_caps['udid'] not in desired_caps:
        desired_caps['udid'] = deviceName

    retry = 3
    while retry:
        try:
            driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                              desired_caps)
            if driver:
                logger("\n[Done] Driver created!")
                break
            else:
                raise Exception("\n[Fail] Create driver fail")
        except Exception as e:
            logger(e)
            logger("Remove Appium")
            os.system(f"adb -s {deviceName} shell pm uninstall io.appium.settings")
            os.system(f"adb -s {deviceName} shell pm uninstall io.appium.uiautomator2.server")
            retry -= 1

    yield driver
    driver.driver.quit()
