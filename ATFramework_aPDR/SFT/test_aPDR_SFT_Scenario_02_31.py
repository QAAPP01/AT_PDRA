import inspect
import sys, os, glob
from os.path import dirname
from os import path
import subprocess
from pprint import pprint
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.locator.locator_type import *

from ATFramework_aPDR.pages.page_factory import PageFactory
from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.ATFramework.utils.log import logger
import pytest
import time

from main import deviceName
from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.ATFramework.utils.compare_Mac import CompareImage, HCompareImg

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

class Test_SFT_Scenario_02_31:
    @pytest.fixture(autouse=True)
    def initial(self):

        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger("[Start] Init driver session")
        desired_caps = {}
        desired_caps.update(app_config.cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        if desired_caps['udid'] == 'auto':
            desired_caps['udid'] = deviceName
        logger(f"[Info] caps={desired_caps}")
        self.report = report
        self.device_udid = desired_caps['udid']
        # ---- local mode > end ----
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01

        # retry 3 time if create driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                                       desired_caps)
                if self.driver:
                    logger("\n[Done] Driver created!")
                    break
                else:
                    raise Exception("\n[Fail] Create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
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

        self.report.set_driver(self.driver)
        self.driver.driver.start_recording_screen()
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(0.1)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger("\n[Stop] Teardown")
        self.driver.stop_driver()

    def sce_2_31_22(self):
        uuid = 'a441348c-7fc0-4b90-a0bf-b7672dc50e3b'
        logger(f"\n[Start] {inspect.stack()[0][3]}")
        self.report.start_uuid(uuid)

        for i in range(4):
            time.sleep(1)
            self.click(L.edit.pip.Text.font_category(3))
            self.click(L.edit.pip.Text.font(i + 1))
            self.click(L.edit.try_before_buy.try_it, 1)
            time.sleep(1)
            while self.element(L.edit.pip.Text.font(i + 1)).get_attribute("selected") != "true":
                time.sleep(1)
            self.click(L.edit.pip.Text.back)
            self.page_edit.click_sub_tool("Font")

        if self.element(L.edit.pip.Text.font_name(5)).text == "Default":
            result = True
            fail_log = None
        else:
            result = False
            fail_log = f'\n[Fail] 5th font name = {self.element(L.edit.pip.Text.font_name(5)).text}'
            logger(fail_log)

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_31_01_to_22(self):
        try:
            result = {}

            item_id = '02_31_01'
            uuid = 'd842fce8-5196-462a-8855-18f2f8b781ae'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.enter_launcher()
            self.page_main.enter_timeline()
            self.page_edit.click_tool("Text")
            self.page_main.h_click(L.edit.pip.Text.text_layout(1))
            self.page_main.h_click(L.edit.pip.Text.add)
            self.page_edit.click_sub_tool("Font")
            first_category = self.page_main.h_get_element(L.edit.pip.Text.font_category(1))
            result[item_id] = first_category.text == "Favorites"

            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_02'
            uuid = '4575e6fa-f2b6-4ed9-a1e6-4c72dcac40d8'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            first_category.click()
            favorite_message = self.page_main.h_get_element(L.edit.pip.Text.font_favorite_message).text

            result[item_id] = favorite_message == "No favorites yet.\nLong press a font to add."
            if not result[item_id]:
                logger(f'\n[Fail] favorite_message = {favorite_message}')

            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_03'
            uuid = '46f626d9-bc0d-4260-b9c5-78dd09f76901'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            second_category = self.page_main.h_get_element(L.edit.pip.Text.font_category(2))

            result[item_id] = second_category.text == "All"
            if not result[item_id]:
                logger(f'\n[Fail] second_category.text = {second_category.text}')
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_04'
            uuid = 'e193799e-09d7-4ad1-8845-895fbca2d298'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            def find_category(category):
                while 1:
                    find_category_result = self.page_main.h_is_exist(find_string(category))
                    if not find_category_result:
                        font_categories_ = self.page_main.h_get_elements(L.edit.pip.Text.font_category(0))
                        last_ = font_categories_[-1].text
                        self.page_main.h_swipe_element(font_categories_[-1], font_categories_[0], 5)
                        font_categories_ = self.page_main.h_get_elements(L.edit.pip.Text.font_category(0))
                        if font_categories_[-1].text == last_:
                            logger(f'[Info] The end of is {last_}')
                            logger(f'[Fail Cannot find "{category}"]')
                            break
                    else:
                        break
                return find_category_result

            result[item_id] = find_category("Handwriting")
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_05'
            uuid = '43012949-2010-439b-959d-f98515235ec2'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            result[item_id] = find_category("Calligraphy")
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_06'
            uuid = 'fa86261b-d4c2-4284-aa86-da8ac7a97b9a'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            result[item_id] = find_category("Monospace")
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_09'
            uuid = 'eb256f5c-a43c-4c49-8c81-da25b09442e7'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            font_categories = self.page_main.h_get_elements(L.edit.pip.Text.font_category(0))
            while 1:
                last = font_categories[-1].text
                self.page_main.h_swipe_element(font_categories[-1], font_categories[0], 5)
                font_categories = self.page_main.h_get_elements(L.edit.pip.Text.font_category(0))
                if font_categories[-1].text == last:
                    last = font_categories[-1].text
                    break

            result[item_id] = last == "From Files"
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_07'
            uuid = 'ab60335c-2f54-47a1-a229-873882325b7c'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            result[item_id] = font_categories[-2].text == "System Fonts"
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_08'
            uuid = '1a2d0245-9372-4464-bafe-83cc98c44fb5'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            font_categories[-2].click()
            system_font = "AndroidClock Regular"
            while 1:
                font_result = self.page_main.h_is_exist(find_string(system_font))
                if font_result:
                    break
                else:
                    fonts = self.page_main.h_get_elements(L.edit.pip.Text.font_name(0))
                    if len(fonts) % 2 == 0:
                        last = fonts[-2].text
                        self.page_main.h_swipe_element(fonts[-2], fonts[0], 7)
                        fonts = self.page_main.h_get_elements(L.edit.pip.Text.font_name(0))
                        if fonts[-2].text == last:
                            logger(f'[Info] Latest font is {last}')
                            logger(f'\n[Fail] Cannot find the system_font {system_font}')
                            break
                        else:
                            continue
                    else:
                        last = fonts[-1].text
                        self.page_main.h_swipe_element(fonts[-1], fonts[0], 7)
                        fonts = self.page_main.h_get_elements(L.edit.pip.Text.font_name(0))
                        if fonts[-1].text == last:
                            logger(f'[Info] Latest font is {last}')
                            logger(f'\n[Fail] Cannot find the system_font {system_font}')
                            break
                        else:
                            continue

            result[item_id] = font_result
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_10'
            uuid = '1bb358ad-0552-4836-8ebd-399d8475e7db'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.click(L.edit.pip.Text.font_import)
            import_font_name = "Raleway-Regular.ttf"
            self.click(xpath('//android.widget.TextView[@content-desc="Search"]'))
            self.element(xpath('//*[contains(@resource-id, "search_src_text")]')).send_keys(".ttf")
            self.driver.driver.press_keycode(66)    # keycode 66: Enter
            self.click(find_string(import_font_name))
            imported_font = import_font_name.split(".")[0]

            result[item_id] = self.page_main.h_is_exist(find_string(imported_font))
            if not result[item_id]:
                logger(f"\n[Fail] imported_font = {imported_font}")
            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_11'
            uuid = '0b280a2f-2268-4c71-9f7d-a4d96059429d'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            selected_categories = self.elements(xpath('//*[contains(@resource-id, "item_category_selected")]'))
            last_category_selected = selected_categories[-1].get_attribute("selected")

            result[item_id] = last_category_selected == "true"
            if not result[item_id]:
                logger(f"\n[Fail] last_category_selected = {last_category_selected}")
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_12'
            uuid = '1b6603e6-67dd-408f-a283-8d8a754f2c3e'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_long_press(find_string(imported_font))
            result[item_id] = self.page_main.h_is_exist(find_string("Added to Favorites."), 5)
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_13'
            uuid = 'e37adc83-eafc-43b4-b432-1460d167fa23'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            # Scroll back to Favorites
            while 1:
                font_categories = self.elements(L.edit.pip.Text.font_category(0))
                first = font_categories[0].text
                self.page_main.h_swipe_element(font_categories[0], font_categories[-1], 5)
                if self.page_main.h_is_exist(find_string("Favorites")):
                    self.click(find_string("Favorites"))
                    break
                else:
                    font_categories = self.elements(L.edit.pip.Text.font_category(0))
                    if font_categories[0].text == first:
                        logger(f'\n[Fail] Cannot find the category "Favorites"')
                        break
                    else:
                        continue
            time.sleep(1)
            favorite_first = self.element(L.edit.pip.Text.font_name(1))
            if not favorite_first:
                logger('[Error] Cannot find the font in "Favorites"')
                result_display_in_favorites = False
            else:
                result_display_in_favorites = favorite_first.text == imported_font

            result[item_id] = result_display_in_favorites
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_14'
            uuid = '77456912-5af1-498e-b7ff-35b9f437a148'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.page_main.h_long_press(L.edit.pip.Text.font_name(1))
            result[item_id] = self.page_main.h_is_exist(find_string("Removed from Favorites."))
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_15'
            uuid = '7ab428d3-948d-4399-a187-b0cc56d469d3'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            if favorite_first:
                if not self.page_main.h_is_exist(find_string(imported_font), 1):
                    result[item_id] = True
                else:
                    result[item_id] = False
                    logger(f'[Fail] Can find {imported_font}')
            else:
                result[item_id] = False
                logger('[Error] Cannot find the font in "Favorites"')

            self.report.new_result(uuid, result[item_id])


            item_id = '02_31_16'
            uuid = 'e06b4242-05c8-45f8-8e4b-643b5b3d17dd'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.click(xpath('(//*[contains(@resource-id, "category_name")])[2]'))
            self.click(L.edit.pip.Text.font_filter)
            self.click(L.edit.pip.Text.font_filter_2)
            self.click(L.edit.pip.Text.font_filter_back)
            pic_after = self.page_main.get_picture(L.edit.pip.Text.font_filter)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_31', '02_31_16.png')

            result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_17'
            uuid = 'b08c5b67-0188-4053-b7a2-6d8fa3bc6bdb'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.click(L.edit.pip.Text.font_filter)
            self.click(L.edit.pip.Text.font_filter_3)
            self.click(L.edit.pip.Text.font_filter_back)
            pic_after = self.page_main.get_picture(L.edit.pip.Text.font_filter)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_31', '02_31_17_1.png')

            result_cht = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

            self.click(L.edit.pip.Text.font_filter)
            self.click(L.edit.pip.Text.font_filter_4)
            self.click(L.edit.pip.Text.font_filter_back)
            pic_after = self.page_main.get_picture(L.edit.pip.Text.font_filter)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_31', '02_31_17_2.png')

            result_chs = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False

            result[item_id] = result_cht and result_chs
            if not result[item_id]:
                logger(f'[Fail] result_cht = {result_cht}, result_chs = {result_chs}')
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_18'
            uuid = 'b8dfe1e3-c31a-499b-a3d9-ae2d7099e9a4'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.click(L.edit.pip.Text.font_filter)
            self.click(L.edit.pip.Text.font_filter_5)
            self.click(L.edit.pip.Text.font_filter_back)
            pic_after = self.page_main.get_picture(L.edit.pip.Text.font_filter)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_31', '02_31_18.png')

            result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_19'
            uuid = 'e285b0b4-2583-4cdd-aad0-5288cea39dbd'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.click(L.edit.pip.Text.font_filter)
            self.page_main.h_swipe_element(L.edit.pip.Text.font_filter_4, L.edit.pip.Text.font_filter_1, 1)
            self.click(L.edit.pip.Text.font_filter_5)
            self.click(L.edit.pip.Text.font_filter_back)
            pic_after = self.page_main.get_picture(L.edit.pip.Text.font_filter)
            pic_base = path.join(path.dirname(__file__), 'test_material', '02_31', '02_31_19.png')

            result[item_id] = True if CompareImage(pic_base, pic_after).h_total_compare() > 0.9 else False
            self.report.new_result(uuid, result[item_id])

            item_id = '02_31_20'
            uuid = 'fdb62dd0-2663-4d54-bf40-77399dabf441'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            self.click(L.edit.pip.Text.back)
            self.page_edit.click_sub_tool("Font")

            result[item_id] = self.page_main.h_is_exist(find_string("Recently used"))
            self.report.new_result(uuid, result[item_id])

            # Case
            item_id = '02_31_21'
            uuid = '9296361c-87ef-415c-925c-f7550fab83da'
            logger(f"\n[Start] sce_{item_id}")
            self.report.start_uuid(uuid)

            # Check highlighted category is All
            highlight_frame = self.elements(xpath('//*[contains(@resource-id, "item_category_selected")]'))
            highlighted_category = False
            for i in range(len(highlight_frame)):
                if highlight_frame[i].get_attribute("selected") == "true":
                    highlighted_category = True
                    break

            if not highlighted_category:
                logger('\n[Fail] Cannot find the selected category')
                result_highlight = False
            else:
                highlighted_category = self.element(xpath(f'(//*[contains(@resource-id, "item_category_selected")])[{i+1}]//*[contains(@resource-id, "category_name")]')).text
                result_highlight = highlighted_category == "All"
                if not result_highlight:
                    logger(f'\n[Fail]highlighted_category = {highlighted_category}')

            # Check the other category has no "Recently used"
            self.click(L.edit.pip.Text.font_category(i+2))
            result_other_no_recently_used = not self.page_main.h_is_exist(find_string("Recently used"))

            result[item_id] = result_highlight and result_other_no_recently_used
            if not result[item_id]:
                logger(f'[Fail] result_highlight = {result_highlight}, result_other_no_recently_used = {result_other_no_recently_used}')
            self.report.new_result(uuid, result[item_id])

            result['2_31_22'] = self.sce_2_31_22()


            # # Case
            # item_id = '02_31_22'
            # uuid = 'a441348c-7fc0-4b90-a0bf-b7672dc50e3b'
            # logger(f"\n[Start] sce_{item_id}")
            # self.report.start_uuid(uuid)
            #
            # for i in range(4):
            #     self.click(L.edit.pip.Text.font_category(3))
            #     self.click(L.edit.pip.Text.font(i+1))
            #     self.click(L.edit.try_before_buy.try_it, 1)
            #     select_font = self.element(L.edit.pip.Text.font(i+1))
            #     while select_font.get_attribute("selected") != "true":
            #         time.sleep(1)
            #         select_font = self.element(L.edit.pip.Text.font(i + 1))
            #     self.click(L.edit.pip.Text.back)
            #     self.page_edit.click_sub_tool("Font")
            #
            # if self.element(L.edit.pip.Text.font_name(5)).text == "Default":
            #     result[item_id] = True
            # else:
            #     result[item_id] = False
            #     logger(f'[Fail] 5th font name = {self.element(L.edit.pip.Text.font_name(5)).text}')
            # self.report.new_result(uuid, result[item_id])

            # Ending
            pprint(result)

        except Exception as err:
            logger(f'[Error] {err}')
