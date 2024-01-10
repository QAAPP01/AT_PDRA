import traceback

import pytest, sys, subprocess, os
from appium.webdriver.appium_service import AppiumService

from os.path import dirname as dir

from selenium.common import InvalidSessionIdException

sys.path.insert(0,(dir(dir(dir(__file__)))))
from ATFramework_aPDR.ATFramework.utils import MyReport
from ATFramework_aPDR.ATFramework.utils.log import logger
from main import package_name

try:
    with open('tr_info', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            if key == 'tr_number':
                tr_number = value
            elif key == 'previous_tr_number':
                previous_tr_number = value
except Exception:
    traceback.print_exc()
    tr_number = ''
    previous_tr_number = ''

DRIVER_DESIRED_CAPS = ''
REPORT_INSTANCE = MyReport(tr_number=tr_number, previous_tr_number=previous_tr_number)
DEFAULT_BROWSER = 'com.android.chrome'
platform_type = 'Android'
PACKAGE_NAME = package_name
TEST_MATERIAL_FOLDER = '00PDRa_Testing_Material'
TEST_MATERIAL_FOLDER_01 = '01PDRa_Testing_Material'

# Recording path
folder_path = os.path.join(os.path.dirname(__file__), "recording")
os.makedirs(folder_path, exist_ok=True)

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


@pytest.fixture(scope="session")
def driver():
    import os
    from ATFramework_aPDR.ATFramework.utils.log import logger
    from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
    from ATFramework_aPDR.configs import app_config
    from ATFramework_aPDR.configs import driver_config
    from main import deviceName

    driver = None
    desired_caps = {}
    desired_caps.update(app_config.cap)
    desired_caps.update(DRIVER_DESIRED_CAPS)

    if 'udid' not in desired_caps:

        def get_connected_devices():
            adb_devices_command = "adb devices"
            result = subprocess.run(adb_devices_command, shell=True, capture_output=True, text=True)
            devices_output = result.stdout.strip().split("\n")[1:]
            devices = [line.split("\t")[0] for line in devices_output if line.endswith("\tdevice")]
            return devices

        devices = get_connected_devices()

        # debug_device = "RFCW2198L7B"
        # if debug_device in devices:
        #     desired_caps['udid'] = debug_device
        if deviceName in devices:
            desired_caps['udid'] = deviceName
        else:
            desired_caps['udid'] = devices[0] if devices else None

        mode = 'debug'
        args = [
            "--address", "127.0.0.1",
            "--port", "4725",
            "--base-path", '/wd/hub'
        ]

        cap = {
            # "udid": "",
            # "language": "ja",
            # "locale": "JP",
            # 'autoGrantPermissions': True,
            # "noReset": True,
            # "autoLaunch": False,
        }
        desired_caps.update(cap)
    else:
        mode = 'local'
        args = [
            "--address", "127.0.0.1",
            "--port", "4723",
            "--base-path", '/wd/hub'
        ]

    appium = AppiumService()
    appium.start(args=args)

    retry = 3
    while retry:
        try:
            driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, mode,
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
    try:
        driver.driver.quit()
    except InvalidSessionIdException:
        pass
    appium.stop()
