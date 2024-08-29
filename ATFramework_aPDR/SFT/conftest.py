import json
import subprocess
import time
import datetime
import traceback
import allure
import os
import pytest
import sys
from PIL import Image
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.page_factory import PageFactory
from selenium.common import InvalidSessionIdException
from main import package_name as PACKAGE_NAME



DRIVER_DESIRED_CAPS = {}
DEFAULT_BROWSER = 'com.android.chrome'
platform_type = 'Android'
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
    from appium.webdriver.appium_service import AppiumService

    driver = None
    desired_caps = {**app_config.cap, **DRIVER_DESIRED_CAPS, 'udid': 'R5CT32Q3WQN'}

    if debug_mode:
        logger('**** Debug Mode ****')
        mode = 'debug'
        args = ["--address", "127.0.0.1", "--port", "4725", "--base-path", '/wd/hub']

        connected_devices = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
        connected_devices_output = connected_devices.stdout.decode().splitlines()

        device_ids = [line.split()[0] for line in connected_devices_output if line and '\tdevice' in line]

        if desired_caps['udid'] not in device_ids:
            if device_ids:
                desired_caps['udid'] = device_ids[0]
            else:
                raise RuntimeError("No devices connected.")

    else:
        logger('**** Testing Mode ****')
        mode = 'local'
        args = ["--address", "127.0.0.1", "--port", "4723", "--base-path", '/wd/hub']

    appium = AppiumService()
    appium.start(args=args)

    cap = {
        "language": "en",
        "locale": "US",
        'autoGrantPermissions': True,
        "noReset": False,
        "autoLaunch": True,
    }
    desired_caps.update(cap)

    def create_driver(retry=3):
        for i in range(retry):
            try:
                _driver = DriverFactory().get_mobile_driver_object(
                    "appium u2", driver_config, app_config, mode, desired_caps
                )
                if _driver:
                    logger("\n[Done] Driver created!")
                    return _driver
                else:
                    raise Exception("\n[Fail] Create driver fail")
            except Exception as e:
                logger(e)
                logger("Remove Appium")
                os.system(f"adb -s {desired_caps['udid']} shell pm uninstall io.appium.settings")
                os.system(f"adb -s {desired_caps['udid']} shell pm uninstall io.appium.uiautomator2.server")
        else:
            raise Exception("All retries to create driver failed")

    driver = create_driver()

    driver.driver.close_app()

    cap['noReset'] = True
    cap['autoLaunch'] = False
    desired_caps.update(cap)

    driver = create_driver()

    yield driver

    if not debug_mode:
        try:
            driver.driver.quit()
            appium.stop()
        except InvalidSessionIdException:
            pass

@pytest.fixture(scope='class', autouse=True)
def driver_init(driver):
    page_main = PageFactory().get_page_object("main_page", driver)
    logger("==== Start driver session ====")
    driver.driver.launch_app()
    page_main.enter_launcher()
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


# === Exception Screenshot Fixture ===

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def exception_screenshot(request, driver):
    yield
    if request.node.rep_call.failed:
        class_name = request.node.cls.__name__ if request.node.cls else ""
        test_name = request.node.name
        screenshot_name = f"{class_name}_{test_name}.jpg"

        failure_dir = os.path.join(os.path.dirname(__file__), "exception_screenshot")
        os.makedirs(failure_dir, exist_ok=True)
        screenshot_path = os.path.join(failure_dir, screenshot_name)

        driver.driver.get_screenshot_as_file(screenshot_path)

        image = Image.open(screenshot_path)
        width, height = image.size
        new_width = 240
        new_height = int(height * (new_width / width))
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        if resized_image.mode == 'RGBA':
            resized_image = resized_image.convert('RGB')

        resized_image.save(screenshot_path, 'JPEG', quality=70)

        allure.attach.file(screenshot_path, name='screenshot', attachment_type=allure.attachment_type.JPG)
        logger(f"Exception screenshot: {screenshot_path}", log_level='error')
