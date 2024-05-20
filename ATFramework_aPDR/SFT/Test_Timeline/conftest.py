import pytest

from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.main_page import MainPage
from ATFramework_aPDR.pages.edit import EditPage
from ATFramework_aPDR.pages.import_media import MediaPage


# === Class scope page fixture ===
@pytest.fixture(scope="class")
def page_main(driver):
    yield MainPage(driver)


@pytest.fixture(scope="class")
def page_media(driver):
    yield MediaPage(driver)


@pytest.fixture(scope="class")
def page_edit(driver):
    yield EditPage(driver)


@pytest.fixture(scope="class", autouse=True)
def class_setup_teardown(driver: AppiumU2Driver,
                         page_main: MainPage):

    # driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
    driver.activate_app('com.cyberlink.powerdirector.DRA140225_01')
    page_main.enter_launcher()
    page_main.subscribe()
    page_main.enter_timeline()
    # Will open to main menu
    yield
    # driver.driver.stop_recording_screen()
    driver.stop_app('com.cyberlink.powerdirector.DRA140225_01')


# === Logging fixture ===
@pytest.fixture(scope='class', autouse=True)
def log_class_start(request):
    logger(f"[Start Test(Class)] Class: {request.node.cls.__name__}", log_level='info')
    yield
    logger(f"[End Test(Class)] Class: {request.node.cls.__name__}", log_level='info')


@pytest.fixture(autouse=True)
def log_function_test(request):
    logger(f"[Start Test] Function: {request.node.name}", log_level='info')
