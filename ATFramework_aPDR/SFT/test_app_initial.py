import sys
import time

import pytest

from ATFramework_aPDR.pages.locator.locator_type import find_string
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.ATFramework.utils.log import logger


def test_app_init(driver):
    try:
        driver.driver.reset()
        time.sleep(1)
        driver.driver.launch_app()

        page_main = PageFactory().get_page_object("main_page", driver)
        page_edit = PageFactory().get_page_object("edit", driver)
        page_main.enter_launcher()
        page_main.h_click(L.main.project.new_project, 2)
        page_main.h_click(L.main.permission.file_ok)
        page_main.h_click(L.main.permission.photo_allow)
        page_main.click(('id', 'top_toolbar_back'))
        page_main.h_click(("id", "tv_hint"), 2)

        if not page_main.h_click(L.edit.preview.import_tips_icon, timeout=1):
            if not page_main.h_click(L.edit.timeline.main_track_import, timeout=1):
                if not page_main.h_click(L.edit.timeline.main_track_import_float, timeout=1):
                    logger('[Warning] No import button')
        page_main.click(find_string('Photo'))
        page_main.h_click(("xpath", '(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[1]'))
        page_main.h_click(("xpath", '(//*[@resource-id="com.cyberlink.powerdirector.DRA140225_01:id/source_image_view"])[2]'))
        page_main.h_click(L.import_media.media_library.apply)

        if not page_edit.preference.trigger_fileName(enable=True):
            raise Exception('trigger_fileName fail')
        page_main.h_click(('id', 'transition_hint'))
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
        logger("\n[Done] app_initial")
    except Exception as err:
        pytest.fail(f'[Error] {err}')