import json
import time
import datetime
import traceback
import os
import pytest
import sys
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.page_factory import PageFactory
from main_server_sacn import package_name
from appium.webdriver.appium_service import AppiumService
from selenium.common import InvalidSessionIdException



DRIVER_DESIRED_CAPS = {}
DEFAULT_BROWSER = 'com.android.chrome'
platform_type = 'Android'
PACKAGE_NAME = package_name
TEST_MATERIAL_FOLDER = '00PDRa_Testing_Material'
TEST_MATERIAL_FOLDER_01 = '01PDRa_Testing_Material'

debug_mode = 0
tr_number = ''
previous_tr_number = ''
try:
    with open('tr_info', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            if key == 'tr_number':
                tr_number = value
            elif key == 'previous_tr_number':
                previous_tr_number = value

except FileNotFoundError:
    debug_mode = 1

except Exception:
    traceback.print_exc()



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
def driver_get_desiredcap(udid, systemPort):
    global DRIVER_DESIRED_CAPS
    if platform_type == 'Android':
        DRIVER_DESIRED_CAPS = {'udid': str(udid), 'systemPort': str(systemPort)}
    else:
        DRIVER_DESIRED_CAPS = {'udid': str(udid)}
    return True


@pytest.fixture(scope="session")
def driver():
    import os
    from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
    from ATFramework_aPDR.configs import app_config
    from ATFramework_aPDR.configs import driver_config

    driver = None
    desired_caps = {}
    desired_caps.update(app_config.cap)
    desired_caps.update(DRIVER_DESIRED_CAPS)

    if debug_mode:
        logger('**** Debug Mode ****')
        desired_caps['udid'] = 'R5CT32Q3WQN'
        if desired_caps['udid'] not in os.popen('adb devices').read():
            desired_caps['udid'] = 'R5CW31G76ST'
            # desired_caps['udid'] = '9596423546005V8'

        mode = 'debug'
        args = [
            "--address", "127.0.0.1",
            "--port", "4725",
            "--base-path", '/wd/hub'
        ]

        cap = {
            # "udid": "",
            # "language": "en",
            # "locale": "US",
            # 'autoGrantPermissions': True,
            # "noReset": True,
            # "autoLaunch": False,
        }
        desired_caps.update(cap)
    else:
        logger('**** Testing Mode ****')
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
            os.system(f"adb -s {desired_caps['udid']} shell pm uninstall io.appium.settings")
            os.system(f"adb -s {desired_caps['udid']} shell pm uninstall io.appium.uiautomator2.server")
            retry -= 1

    yield driver
    if not debug_mode:
        try:
            driver.driver.quit()
        except InvalidSessionIdException:
            pass
    appium.stop()


@pytest.fixture(scope='class', autouse=True)
def driver_init(driver):
    logger("==== Start driver session ====")
    driver.driver.launch_app()
    yield
    driver.driver.close_app()


@pytest.fixture(scope="session")
def shortcut(driver):
    page_main = PageFactory().get_page_object("main_page", driver)
    page_edit = PageFactory().get_page_object("edit", driver)
    page_media = PageFactory().get_page_object("import_media", driver)
    page_preference = PageFactory().get_page_object("timeline_settings", driver)
    page_shortcut = PageFactory().get_page_object("shortcut", driver)
    return page_main, page_edit, page_media, page_preference, page_shortcut


def pytest_terminal_summary(terminalreporter):
    logger("pytest_terminal_summary")

    def format_duration(seconds):
        td = datetime.timedelta(seconds=int(seconds))
        return str(td)

    results = terminalreporter.stats
    num_collected = terminalreporter._numcollected
    passed = len(results.get('passed', []))
    failed = len(results.get('failed', []))
    errors = len(results.get('error', []))
    skipped = len(results.get('skipped', []))

    duration_seconds = time.time() - terminalreporter._sessionstarttime
    formatted_duration = format_duration(duration_seconds)

    summary = {
        "num_collected": num_collected,
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "skipped": skipped,
        "duration": formatted_duration
    }

    with open('summary.json', 'w') as f:
        json.dump(summary, f)

# === Logging fixture ===

@pytest.fixture(scope='class', autouse=True)
def log_class_start(request):
    if request.node.cls is not None:
        logger(f"\n[Start] Class: {request.node.cls.__name__}", log_level='info')


@pytest.fixture(autouse=True)
def log_function_test(request):
    logger(f"\n[Start] Function: {request.node.name}", log_level='info')
