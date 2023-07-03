import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_SFT_Scenario_02_02:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.report = report

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        self.report.set_driver(driver)
        driver.driver.launch_app()
        yield
        driver.driver.close_app()


    def test_case(self):
        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            def enter_mixtype():
                self.click(id("Audio"))
                self.click(id('Music'))
                self.click(id("tab_mix_tape_sound_clip"))

            all_category = set()
            all_music = set()
            adding_category = None

            while True:
                enter_mixtype()
                if adding_category:
                    self.click(find_string(adding_category))
                else:
                    category = self.elements(id('library_unit_caption'))
                    last = category[-1].text

                    for i in category:
                        if i.text == 'Downloaded':
                            continue
                        elif i.text in all_category:
                            if i.text == last:
                                self.page_main.h_swipe_element(category[-1], category[0], 5)
                                category = self.elements(id('library_unit_caption'))
                                if category[-1].text == last:
                                    return True
                                else:
                                    last = category[-1].text
                            else:
                                continue
                        else:
                            adding_category = i.text
                            all_category.add(i.text)
                            i.click()

                            music = self.elements(id('library_unit_caption'))
                            last_music = music[-1].text

                            for j in range(len(music)):
                                if music[j].text in all_music:
                                    if music[j].text == last_music:
                                        self.page_main.h_swipe_element(music[-1], music[0], 5)
                                        music = self.elements(id('library_unit_caption'))
                                        if music[-1].text == last_music:
                                            adding_category = None
                                        else:
                                            last_music = music[-1].text
                                    else:
                                        continue
                                else:
                                    music[j].click()
                                    self.click(id('library_unit_download'))
                                    self.click(xpath(f'(//*[contains(@resource-id,"library_unit_add")])[{j+1}]'))
                                    self.click(L.edit.menu.play)
                                    self.click(L.edit.menu.delete)
                                    break
                            break


        except Exception as err:
            logger(f'\n{err}')

