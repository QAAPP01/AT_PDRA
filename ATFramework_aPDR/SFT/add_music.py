import sys
import time
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

class Test_Scenario:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

        driver.driver.launch_app()
        yield
        driver.driver.close_app()


    def test_case(self):
        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()

            def enter_mixtype():
                self.click(find_string("Audio"))
                self.click(find_string('Music'))
                self.click(id("tab_mix_tape_sound_clip"))

            all_category = set()
            all_music = set()
            adding_category = None

            enter_mixtype()
            while True:
                if adding_category:
                    enter_mixtype()
                    self.click(find_string(adding_category))
                else:
                    category = self.elements(id('library_unit_caption'))
                    last = category[-1].text

                    for i in category:
                        if i.text == 'Downloaded' or i.text == 'Favorite':
                            continue
                        elif i.text in all_category:
                            if i.text == last:
                                self.page_main.h_swipe_element(category[-1], category[0], 5)
                                category = self.elements(id('library_unit_caption'))
                                if category[-1].text == last:
                                    print(f'Category num: {len(all_category)}')
                                    print(f'Music num: {len(all_music)}')
                                    return True
                                else:
                                    last = category[-1].text
                                    break
                            else:
                                continue
                        else:
                            adding_category = i.text
                            all_category.add(i.text)
                            i.click()
                            break

                music = self.elements(id('library_unit_caption'))
                last_music = music[-1].text

                music_flag = 1
                while music_flag:
                    for j in range(len(music)):
                        if music[j].text in all_music:
                            if music[j].text == last_music:
                                self.page_main.h_swipe_element(music[-1], music[0], 5)
                                music = self.elements(id('library_unit_caption'))
                                if music[-1].text == last_music:
                                    adding_category = None
                                    music_flag = 0
                                    self.click(id('action_back'))
                                    break
                                else:
                                    last_music = music[-1].text
                                    break
                            else:
                                continue
                        else:
                            music_flag = 0
                            all_music.add(music[j].text)
                            music[j].click()
                            time.sleep(2)
                            self.click(id('library_unit_download'), 2)
                            self.click(xpath(f'(//*[contains(@resource-id,"library_unit_add")])[{j + 1}]'), 10)
                            self.click(L.edit.menu.play)
                            time.sleep(2)
                            self.click(L.edit.menu.delete)
                            break

        except Exception as err:
            logger(f'\n{err}')
            print(all_category)
            print(all_music)

