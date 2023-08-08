import pytest, inspect, sys, time
from os import path

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'

# global
preview_default = None


class Test_AiSticker:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        global report
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

    def sce_7_1_1(self):
        uuid = '7713342c-d600-43b7-9fe8-1675a2124c7b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.page_edit.click_tool('AI Effect')

            if self.is_exist(L.edit.master.ai_effect.effect()):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the effect')

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.page_edit.click_tool('AI Effect')

            return "FAIL"

    def sce_7_1_2(self):
        uuid = '09586d72-f271-4863-9e7e-36416d682706'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            global preview_default
            default_preview = self.page_main.get_preview_pic()
            self.click(L.edit.master.ai_effect.effect(1))
            self.click(L.edit.try_before_buy.try_it_first, 1)

            if self.element(id('itemMask')).get_attribute("selected") == "true":
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception("[FAIL] Effect is not selected")

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.page_edit.click_tool('AI Effect')
            self.click(L.edit.master.ai_effect.effect(1))
            self.click(L.edit.try_before_buy.try_it_first, 1)

            return "FAIL"

    def sce_7_1_3(self):
        uuid = 'b235c57c-2f0e-41af-94b7-559ef7848880'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.click(L.edit.master.ai_effect.cancel)
            after_preview = self.page_main.get_preview_pic()

            if HCompareImg(after_preview, preview_default).full_compare() > 0.96:
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception("[FAIL] Images diff")

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('photo', file_name=photo_9_16)
            self.click(L.edit.master.master_clip())

            return "FAIL"

    def sce_7_1_4(self):
        uuid = '283f410f-a8aa-4ff7-aa9f-b60221586e8d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.page_edit.click_sub_tool("AI Effect")

            if self.is_exist(L.edit.master.ai_effect.effect()):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the effect')

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', file_name=video_9_16)
            self.click(L.edit.master.master_clip())
            self.page_edit.click_sub_tool("AI Effect")

            return "FAIL"

    def sce_7_1_5(self):
        uuid = 'a887fe92-4174-45eb-b042-3e5967c6df35'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            effect_name = self.element(L.edit.master.ai_effect.effect_name(1)).text

            self.long_press(L.edit.master.ai_effect.effect(1))

            if not self.element(L.edit.master.ai_effect.favorite_icon(1)).get_attribute("selected") == "true":
                raise Exception('[Fail] Favorite icon is not lighted up')

            self.click(find_string("Favorites"))

            if not self.is_exist(find_string(effect_name)):
                raise Exception('[Fail] Cannot find the effect in the favorite category')

            self.report.new_result(uuid, True)
            return "PASS"

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', file_name=video_9_16)
            self.click(L.edit.master.master_clip())
            self.page_edit.click_sub_tool("AI Effect")
            self.long_press(L.edit.master.ai_effect.effect(1))
            self.click(find_string("Favorites"))

            return "FAIL"

    def sce_7_1_6(self):
        uuid = 'b6684755-ce40-4db2-b117-54004bf61e0e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.edit.master.ai_effect.effect(1))

            if not self.is_exist(L.edit.master.ai_effect.effect(0)):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Favorite category is not empty')

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', file_name=video_9_16)
            self.click(L.edit.master.master_clip())
            self.page_edit.click_sub_tool("AI Effect")

            return "FAIL"

    def sce_7_1_7(self):
        uuid = 'b38fa219-f9de-4492-9d97-cb8385bb2a4b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0)):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter "Body Effect"')

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', file_name=video_9_16)
            self.click(L.edit.master.master_clip())
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))

            return "FAIL"

    def sce_7_1_8(self):
        uuid = 'fcebcfb5-f2b5-41d7-91d8-70425154ba2c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        self.report.start_uuid(uuid)

        try:
            if self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0)):
                self.report.new_result(uuid, True)
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter "Contour 2"')

        except Exception as err:
            logger(f'\n{err}')
            self.report.new_result(uuid, False, fail_log=err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.add_master_media('video', file_name=video_9_16)
            self.click(L.edit.master.master_clip())
            self.page_edit.click_sub_tool("AI Effect")
            self.page_edit.click_category("Body Effect", L.edit.master.ai_effect.category(0))
            self.page_edit.click_effect("Contour 2", L.edit.master.ai_effect.effect_name(0))

            return "FAIL"

    def test_case(self):
        result = {"sce_7_1_1": self.sce_7_1_1(),
                  "sce_7_1_2": self.sce_7_1_2(),
                  "sce_7_1_3": self.sce_7_1_3(),
                  "sce_7_1_4": self.sce_7_1_4(),
                  "sce_7_1_5": self.sce_7_1_5(),
                  "sce_7_1_6": self.sce_7_1_6(),
                  "sce_7_1_7": self.sce_7_1_7(),
                  "sce_7_1_8": self.sce_7_1_8(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")



