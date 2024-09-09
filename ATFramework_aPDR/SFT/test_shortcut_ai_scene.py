import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'

@allure.epic("Shortcut - AI Scene")
class Test_Shortcut_AI_Scene:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @pytest.fixture(scope="module")
    def data(self):
        data = {'last_result': True}
        yield data

    def last_is_fail(self, data):
        if not data['last_result']:
            data['last_result'] = True
            self.page_main.relaunch()
            return True
        return False

    @allure.feature("Entry")
    @allure.story("Enter")
    @allure.title("From Shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            assert self.page_shortcut.enter_shortcut('AI Scene')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Entry")
    @allure.story("Back")
    @allure.title("To Shortcut")
    def test_back_to_shortcut(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Scene')

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.feature("Media Picker")
    @allure.story("Recommendation")
    @allure.title("Close")
    def test_close_recommendation(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.close_recommendation("AI Scene")

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    def sce_6_12_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_shortcut.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            for wait in range(60):
                if self.is_exist(find_string('Cancel')):
                    time.sleep(2)
                else:
                    break

            if self.is_exist(find_string('Export')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter AI Scene')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)
            self.page_media.select_local_photo(test_material_folder, photo_9_16)

            return "FAIL"

    def sce_6_12_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.editor_back)

            if self.is_exist(find_string('Add Media')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_shortcut.enter_shortcut('AI Scene')
            self.click(L.main.shortcut.btn_continue)

            return "FAIL"

    
    def test_case(self):
        result = {"sce_6_12_1": self.sce_6_12_1(),
                  "sce_6_12_2": self.sce_6_12_2(),
                  "sce_6_12_3": self.sce_6_12_3(),
                  "sce_6_12_4": self.sce_6_12_4(),
                  "sce_6_12_5": self.sce_6_12_5(),
                  "sce_6_12_6": self.sce_6_12_6(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")