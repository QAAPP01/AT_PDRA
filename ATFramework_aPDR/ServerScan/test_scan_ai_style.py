import traceback
import inspect
import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger

from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *
from .conftest import TEST_MATERIAL_FOLDER as test_material_folder

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


@allure.epic("Scan AI Styles")
@allure.feature("AI Art")
@allure.story("Style")
class Test_Scan_AI_Art:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    def apply_style(self, style, retry=30):
        for i in range(retry):
            self.page_main.shortcut.click_style(style)
            self.click(aid('[AID]ConfirmDialog_No'), 1)
            self.page_main.shortcut.waiting_generated()
            if not self.click(id('ok_button'), 1):
                break
        else:
            raise Exception(f"Exceeded retry limit: {retry}")

        preview = self.page_edit.get_preview_pic()
        return HCompareImg(preview).is_not_black()

    def relaunch(self, driver):
        driver.driver.close_app()
        driver.driver.launch_app()

        self.page_main.enter_launcher()
        self.click(L.main.ai_creation.entry)
        self.page_shortcut.enter_ai_feature('AI Art')
        self.click(L.main.shortcut.try_it_now, 2)
        self.page_media.select_local_photo(test_material_folder, photo_9_16)

    @allure.title("Maid")
    def test_ai_art_maid(self, driver):
        try:
            self.page_main.enter_launcher()
            self.page_main.subscribe()
            self.click(L.main.ai_creation.entry)
            self.page_shortcut.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now, 2)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            assert self.apply_style('Maid')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Swimsuit")
    def test_ai_art_swimsuit(self, driver):
        try:
            assert self.apply_style('Swimsuit')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Sailor")
    def test_ai_art_sailor(self, driver):
        try:
            assert self.apply_style('Sailor')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Kitty")
    def test_ai_art_kitty(self, driver):
        try:
            assert self.apply_style('Kitty')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Bunny")
    def test_ai_art_bunny(self, driver):
        try:
            assert self.apply_style('Bunny')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Bikini")
    def test_ai_art_bikini(self, driver):
        try:
            assert self.apply_style('Bikini')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Sakura")
    def test_ai_art_sakura(self, driver):
        try:
            assert self.apply_style('Sakura')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Horror")
    def test_ai_art_horror(self, driver):
        try:
            assert self.apply_style('Horror')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("New Year")
    def test_ai_art_new_year(self, driver):
        try:
            assert self.apply_style('New Year')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Student")
    def test_ai_art_student(self, driver):
        try:
            assert self.apply_style('Student')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Eastern")
    def test_ai_art_eastern(self, driver):
        try:
            assert self.apply_style('Eastern')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Princess")
    def test_ai_art_princess(self, driver):
        try:
            assert self.apply_style('Princess')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Celebration")
    def test_ai_art_celebration(self, driver):
        try:
            assert self.apply_style('Celebration')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("School")
    def test_ai_art_school(self, driver):
        try:
            assert self.apply_style('School')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Cool")
    def test_ai_art_cool(self, driver):
        try:
            assert self.apply_style('Cool')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Santa")
    def test_ai_art_santa(self, driver):
        try:
            assert self.apply_style('Santa')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Reindeer")
    def test_ai_art_reindeer(self, driver):
        try:
            assert self.apply_style('Reindeer')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Cyberpunk")
    def test_ai_art_cyberpunk(self, driver):
        try:
            assert self.apply_style('Cyberpunk')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Military")
    def test_ai_art_military(self, driver):
        try:
            assert self.apply_style('Military')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Sparkle")
    def test_ai_art_sparkle(self, driver):
        try:
            assert self.apply_style('Sparkle')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Snow")
    def test_ai_art_snow(self, driver):
        try:
            assert self.apply_style('Snow')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Zombie")
    def test_ai_art_zombie(self, driver):
        try:
            assert self.apply_style('Zombie')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Winter")
    def test_ai_art_winter(self, driver):
        try:
            assert self.apply_style('Winter')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Soccer")
    def test_ai_art_soccer(self, driver):
        try:
            assert self.apply_style('Soccer')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Festival")
    def test_ai_art_festival(self, driver):
        try:
            assert self.apply_style('Festival')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Armor")
    def test_ai_art_armor(self, driver):
        try:
            assert self.apply_style('Armor')

        except Exception as e:
            traceback.print_exc()
            logger(e)

            raise


@allure.epic("Scan AI Styles")
@allure.feature("AI Cartoon")
@allure.story("Style")
class Test_Scan_AI_Cartoon:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    def apply_style(self, style, retry=30):
        for i in range(retry):
            self.page_main.shortcut.click_style(style)
            self.click(aid('[AID]ConfirmDialog_No'), 1)
            self.page_main.shortcut.waiting_generated()
            if not self.click(id('ok_button'), 1):
                break
        else:
            raise Exception(f"Exceeded retry limit: {retry}")

        preview = self.page_edit.get_preview_pic()
        return HCompareImg(preview).is_not_black()

    def relaunch(self, driver):
        driver.driver.close_app()
        driver.driver.launch_app()

        self.page_main.enter_launcher()
        self.click(L.main.ai_creation.entry)
        self.page_shortcut.enter_ai_feature('AI Cartoon')
        self.click(L.main.shortcut.try_it_now, 2)
        self.page_media.select_local_photo(test_material_folder, photo_9_16)

    @allure.title("Elf")
    def test_ai_cartoon_elf(self, driver):

        try:
            self.page_main.enter_launcher()
            self.page_main.subscribe()
            self.click(L.main.ai_creation.entry)
            self.page_shortcut.enter_ai_feature('AI Cartoon')
            self.click(L.main.shortcut.try_it_now, 2)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            assert self.apply_style('Elf')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Police")
    def test_ai_cartoon_police(self, driver):
        try:
            assert self.apply_style('Police')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Princess")
    def test_ai_cartoon_princess(self, driver):
        try:
            assert self.apply_style('Princess')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Prince")
    def test_ai_cartoon_prince(self, driver):
        try:
            assert self.apply_style('Prince')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Cowboy")
    def test_ai_cartoon_cowboy(self, driver):
        try:
            assert self.apply_style('Cowboy')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("School")
    def test_ai_cartoon_school(self, driver):
        try:
            assert self.apply_style('School')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Maid")
    def test_ai_cartoon_maid(self, driver):
        try:
            assert self.apply_style('Maid')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Athlete")
    def test_ai_cartoon_athlete(self, driver):
        try:
            assert self.apply_style('Athlete')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Warrior")
    def test_ai_cartoon_warrior(self, driver):
        try:
            assert self.apply_style('Warrior')

        except Exception as e:
            traceback.print_exc()
            logger(e)

            raise


@allure.epic("Scan AI Styles")
@allure.feature("AI Sketch")
@allure.story("Style")
class Test_Scan_AI_Sketch:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    def apply_style(self, style, retry=30):
        for i in range(retry):
            self.page_main.shortcut.click_style(style)
            self.click(aid('[AID]ConfirmDialog_No'), 1)
            self.page_main.shortcut.waiting_generated()
            if not self.click(id('ok_button'), 1):
                break
        else:
            raise Exception(f"Exceeded retry limit: {retry}")

        preview = self.page_edit.get_preview_pic()
        return HCompareImg(preview).is_not_black()

    def relaunch(self, driver):
        driver.driver.close_app()
        driver.driver.launch_app()

        self.page_main.enter_launcher()
        self.click(L.main.ai_creation.entry)
        self.page_shortcut.enter_ai_feature('AI Sketch')
        self.click(L.main.shortcut.try_it_now, 2)
        self.page_media.select_local_photo(test_material_folder, photo_9_16)

    @allure.title("Oil Painting")
    def test_ai_sketch_oil_painting(self, driver):

        try:
            self.page_main.enter_launcher()
            self.page_main.subscribe()
            self.click(L.main.ai_creation.entry)
            self.page_shortcut.enter_ai_feature('AI Sketch')
            self.click(L.main.shortcut.try_it_now, 2)
            if self.click(id("checkBox"), 0.5):
                self.click(id('tv_continue'))
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            assert self.apply_style('Oil Painting')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Intricate")
    def test_ai_sketch_intricate(self, driver):
        try:
            assert self.apply_style('Intricate')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Minimalist")
    def test_ai_sketch_minimalist(self, driver):
        try:
            assert self.apply_style('Minimalist')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Lovely")
    def test_ai_sketch_lovely(self, driver):
        try:
            assert self.apply_style('Lovely')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Marker")
    def test_ai_sketch_marker(self, driver):
        try:
            assert self.apply_style('Marker')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Colorful")
    def test_ai_sketch_colorful(self, driver):
        try:
            assert self.apply_style('Colorful')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Pop")
    def test_ai_sketch_pop(self, driver):
        try:
            assert self.apply_style('Pop')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Crayon")
    def test_ai_sketch_crayon(self, driver):
        try:
            assert self.apply_style('Crayon')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Romantic")
    def test_ai_sketch_romantic(self, driver):
        try:
            assert self.apply_style('Romantic')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Sweet")
    def test_ai_sketch_sweet(self, driver):
        try:
            assert self.apply_style('Sweet')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            self.relaunch(driver)

            raise

    @allure.title("Graffiti")
    def test_ai_sketch_graffiti(self, driver):
        try:
            assert self.apply_style('Graffiti')

        except Exception as e:
            traceback.print_exc()
            logger(e)

            raise
