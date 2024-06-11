import traceback
import inspect
import pytest
import allure

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from .conftest import TEST_MATERIAL_FOLDER as test_material_folder

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


@allure.feature("AI Art")
class Test_Scan_Sticker:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @allure.story("Maid")
    def test_ai_art_maid(self, driver):

        try:
            self.page_main.enter_launcher()
            self.page_main.subscribe()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)
            self.page_main.shortcut.click_style('Maid')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Swimsuit")
    def test_ai_art_swimsuit(self, driver):
        try:
            self.page_main.shortcut.click_style('Swimsuit')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Sailor")
    def test_ai_art_sailor(self, driver):
        try:
            self.page_main.shortcut.click_style('Sailor')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Kitty")
    def test_ai_art_kitty(self, driver):
        try:
            self.page_main.shortcut.click_style('Kitty')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Bunny")
    def test_ai_art_bunny(self, driver):
        try:
            self.page_main.shortcut.click_style('Bunny')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Bikini")
    def test_ai_art_bikini(self, driver):
        try:
            self.page_main.shortcut.click_style('Bikini')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Sakura")
    def test_ai_art_sakura(self, driver):
        try:
            self.page_main.shortcut.click_style('Sakura')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Horror")
    def test_ai_art_horror(self, driver):
        try:
            self.page_main.shortcut.click_style('Horror')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("New Year")
    def test_ai_art_new_year(self, driver):
        try:
            self.page_main.shortcut.click_style('New Year')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Student")
    def test_ai_art_student(self, driver):
        try:
            self.page_main.shortcut.click_style('Student')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Eastern")
    def test_ai_art_eastern(self, driver):
        try:
            self.page_main.shortcut.click_style('Eastern')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Princess")
    def test_ai_art_princess(self, driver):
        try:
            self.page_main.shortcut.click_style('Princess')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Celebration")
    def test_ai_art_celebration(self, driver):
        try:
            self.page_main.shortcut.click_style('Celebration')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("School")
    def test_ai_art_school(self, driver):
        try:
            self.page_main.shortcut.click_style('School')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Cool")
    def test_ai_art_cool(self, driver):
        try:
            self.page_main.shortcut.click_style('Cool')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Santa")
    def test_ai_art_santa(self, driver):
        try:
            self.page_main.shortcut.click_style('Santa')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Reindeer")
    def test_ai_art_reindeer(self, driver):
        try:
            self.page_main.shortcut.click_style('Reindeer')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Cyberpunk")
    def test_ai_art_cyberpunk(self, driver):
        try:
            self.page_main.shortcut.click_style('Cyberpunk')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Military")
    def test_ai_art_military(self, driver):
        try:
            self.page_main.shortcut.click_style('Military')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Sparkle")
    def test_ai_art_sparkle(self, driver):
        try:
            self.page_main.shortcut.click_style('Sparkle')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Snow")
    def test_ai_art_snow(self, driver):
        try:
            self.page_main.shortcut.click_style('Snow')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Zombie")
    def test_ai_art_zombie(self, driver):
        try:
            self.page_main.shortcut.click_style('Zombie')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Winter")
    def test_ai_art_winter(self, driver):
        try:
            self.page_main.shortcut.click_style('Winter')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Soccer")
    def test_ai_art_soccer(self, driver):
        try:
            self.page_main.shortcut.click_style('Soccer')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Festival")
    def test_ai_art_festival(self, driver):
        try:
            self.page_main.shortcut.click_style('Festival')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)

    @allure.story("Armor")
    def test_ai_art_armor(self, driver):
        try:
            self.page_main.shortcut.click_style('Armor')
            self.page_main.shortcut.waiting_generated()
            preview = self.page_edit.get_preview_pic()

            assert HCompareImg(preview).is_not_black()

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_ai_feature('AI Art')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            raise Exception(e)
