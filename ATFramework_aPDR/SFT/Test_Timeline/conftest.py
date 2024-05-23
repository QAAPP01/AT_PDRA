import pytest

from ATFramework_aPDR.ATFramework.drivers.appium_driver import AppiumU2Driver
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.main_page import MainPage
from ATFramework_aPDR.pages.edit import EditPage
from ATFramework_aPDR.pages.import_media import MediaPage


# === Logging fixture ===
@pytest.fixture(scope='class', autouse=True)
def log_class_start(request):
    logger(f"[Start Test(Class)] Class: {request.node.cls.__name__}", log_level='info')
    yield
    logger(f"[End Test(Class)] Class: {request.node.cls.__name__}", log_level='info')


@pytest.fixture(autouse=True)
def log_function_test(request):
    logger(f"[Start Test] Function: {request.node.name}", log_level='info')
