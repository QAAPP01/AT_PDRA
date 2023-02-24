import os
import sys
from main import deviceName
from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config, driver_config
from ATFramework_aPDR.pages.locator.locator_type import find_string
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.ATFramework.utils.log import logger


def test_app_init():
    try:
        desired_caps = {}
        desired_caps.update(app_config.init_cap)
        from .conftest import DRIVER_DESIRED_CAPS
        desired_caps.update(DRIVER_DESIRED_CAPS)
        if desired_caps['udid'] == 'auto':
            desired_caps['udid'] = deviceName
        # retry 3 time if create driver fail
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
                os.system(f"adb -s {deviceName} shell pm uninstall io.appium.settings")
                os.system(f"adb -s {deviceName} shell pm uninstall io.appium.uiautomator2.server")
                retry -= 1
        page_main = PageFactory().get_page_object("main_page", driver)
        page_main.enter_launcher()
        page_main.h_click(L.main.project.new_project, 2)
        page_main.h_click(L.main.permission.file_ok)
        page_main.h_click(L.main.permission.photo_allow)
        page_main.h_click(("id", "btn_play_container"))
        page_main.h_click(L.import_media.media_library.apply)
        page_main.h_click(find_string("Use Original"), 4)
        page_main.h_click(L.edit.settings.menu)
        page_main.h_click(L.edit.settings.preference)
        while not page_main.h_is_exist(L.main.menu.display_file_name_switch, 1):
            elements = page_main.h_get_elements(('xpath', '//android.widget.LinearLayout'))
            page_main.h_swipe_element(elements[len(elements) - 1], elements[0])
        if page_main.h_get_element(L.main.menu.display_file_name_switch).get_attribute('checked') == 'false':
            page_main.h_click(L.main.menu.display_file_name_switch)
        driver.driver.back()
        page_main.h_click(L.edit.menu.play)
        page_main.h_click(L.edit.preview.help_not_show_tip_again)
        driver.driver.back()
        page_main.h_click(L.edit.menu.home)
        # Churn Recovery
        if page_main.h_is_exist(L.main.premium.pdr_premium):
            driver.driver.back()
        page_main.h_long_press(L.main.project.project_name())
        page_main.h_click(find_string("Delete"))
        page_main.h_click(L.main.project.dialog_ok)
        driver.stop_driver()
        logger("\n[Done] app_initial")
    except Exception as e:
        sys.exit(f'[Error] {e}')