import inspect
import sys
import time
from os import path
from os.path import dirname

import pytest

from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.configs import app_config
from ATFramework_aPDR.configs import driver_config
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from main import deviceName
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

file_video = 'video.mp4'
file_photo = 'photo.jpg'


class Test_SFT_Scenario_06_01:
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

    def sce_6_1_1(self):
        uuid = 'c706815e-c49f-45c4-a1d4-e8e3db931827'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_main.enter_launcher()
            self.click(L.main.ai_effect.ai_effect_entry)

            if self.element(L.main.ai_effect.library_title).text == "AI Effect":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find the title "AI Effect": {self.element(L.main.ai_effect.library_title).text}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_2_1(self):
        uuid = '3e59087b-3f6b-4d75-a71d-0cccc3c9747e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.back)

            if self.click(L.main.ai_effect.ai_effect_entry):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find ai_effect_entry'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_2_2(self):
        uuid = 'ccdef567-1991-4961-a961-c514123529ee'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            templates = self.elements(id("ai_template_card_view"))

            if len(templates) > 3:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Template number < 4'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_2_3(self):
        uuid = 'b747078b-bde0-4244-82c9-dec13eb6eef7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            if self.is_exist(L.main.ai_effect.template()):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find template'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_2_6(self):
        uuid = '9f39bb41-13ab-438d-ae69-cb1468f913f8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.template())
            duration_locator = '//androidx.cardview.widget.CardView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[contains(@resource-id,"template_duration_text")]'
            duration = self.element(xpath(duration_locator)).text

            clip_locator = '//androidx.cardview.widget.CardView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[contains(@resource-id,"video_template_clip_count_text")]'
            clip_number = self.element(xpath(clip_locator)).text

            if self.is_exist(L.main.ai_effect.try_now):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find try_now'

            self.report.new_result(uuid, result, fail_log=fail_log)

            self.click(L.main.ai_effect.back)

            def sce_6_2_4():
                _uuid = '794fb7cf-3061-4c79-b09a-5ca88f54b2d4'
                _func_name = inspect.stack()[0][3]
                logger(f"\n[Start] {_func_name}")
                _case_id = _func_name.split("sce_")[1]
                self.report.start_uuid(_uuid)

                try:
                    library_duration = self.element(L.main.ai_effect.template_duration()).text

                    if duration == library_duration:
                        _result = True
                        _fail_log = None
                    else:
                        _result = False
                        _fail_log = f'\n[Fail] Duration incorrect: {library_duration}'

                    global result_sce_6_2_4
                    result_sce_6_2_4 = _result

                    self.report.new_result(_uuid, _result, fail_log=_fail_log)
                    return "PASS" if _result else "FAIL"
                except Exception as _err:
                    logger(f"[Error] {_err}")
                    self.report.new_result(_uuid, False, fail_log="ERROR")
                    return "ERROR"

            def sce_6_2_5():
                _uuid = '25c707c4-e001-4477-81b5-32c47aae7016'
                _func_name = inspect.stack()[0][3]
                logger(f"\n[Start] {_func_name}")
                _case_id = _func_name.split("sce_")[1]
                self.report.start_uuid(_uuid)

                try:
                    library_clip_number = self.element(L.main.ai_effect.template_clip_number()).text

                    if clip_number == library_clip_number:
                        _result = True
                        _fail_log = None
                    else:
                        _result = False
                        _fail_log = f'\n[Fail] template_clip_number incorrect {library_clip_number}'

                    global result_sce_6_2_5
                    result_sce_6_2_5 = _result

                    self.report.new_result(_uuid, _result, fail_log=_fail_log)
                    return "PASS" if _result else "FAIL"
                except Exception as _err:
                    logger(f"[Error] {_err}")
                    self.report.new_result(_uuid, False, fail_log="ERROR")
                    return "ERROR"

            sce_6_2_4()
            sce_6_2_5()

            self.click(L.main.ai_effect.template())

            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_3_1(self):
        uuid = '2313a0da-9631-49c7-a276-80a658e3966a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.back)

            templates = self.elements(id("ai_template_card_view"))

            if len(templates) > 3:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Template number < 4'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_3_2(self):
        uuid = '1b83d97e-8046-4fa3-8c69-be36ec49ee3c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.template())

            while not self.is_exist(L.main.ai_effect.premium, 1):
                page_before = self.element(L.main.ai_effect.full_preview)
                self.driver.swipe_up()
                if page_before == self.element(L.main.ai_effect.full_preview):
                    break

            if self.is_exist(L.main.ai_effect.premium):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find premium_icon'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_3_3(self):
        uuid = 'd7f0515a-7ce4-4a92-9e35-51e2331065d9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            if self.is_exist(L.main.ai_effect.full_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find full screen preview'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_3_4(self):
        uuid = 'bee11837-3711-4071-bf77-48f09135787c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.back)
            self.click(L.main.ai_effect.template())
            page_before = self.element(L.main.ai_effect.full_preview)

            # swipe up to free template for export test
            while self.is_exist(L.main.ai_effect.premium, 1):
                page_before = self.element(L.main.ai_effect.full_preview)
                self.driver.swipe_up()
                if page_before == self.element(L.main.ai_effect.full_preview):
                    break

            if not page_before == self.element(L.main.ai_effect.full_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Preview is no change'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_3_5(self):
        uuid = 'aee4de37-54cb-4a7b-a547-aaae2f6f6b61'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            if result_sce_6_2_4 and result_sce_6_2_5:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Duration: {result_sce_6_2_4}, Clip: {result_sce_6_2_5}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_3_6(self):
        uuid = '52a8372a-401d-426e-be15-b7bc1ddbf3f7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.try_now)

            if self.is_exist(L.main.ai_effect.media_library):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find media_library'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_1(self):
        uuid = '5974cd43-3dbe-419e-8406-07b89c4990f4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.back)

            if self.is_exist(L.main.ai_effect.try_now):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find try_now'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_2(self):
        uuid = '06054245-4a09-4b65-86d1-435dc32b0292'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.try_now)
            toast_default = "Recommend choosing images/videos with clear view of face."
            toast = self.element(L.main.ai_effect.toast).text

            if toast == toast_default:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Toast incorrect: {toast}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_3(self):
        uuid = '1c1ca59a-306a-491b-9aa8-403dba30906c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.descending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name, reverse=True)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_4(self):
        uuid = 'e2cadaca-6237-4a4f-acb6-d56142c12a35'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.ascending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_5(self):
        uuid = '1cfe4a37-eb49-47a1-a872-927d77349328'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            for i in range(60):
                if self.is_exist(L.import_media.media_library.loading_circle, 1):
                    time.sleep(1)
                else:
                    break

            if self.is_exist(L.import_media.media_library.Video.display_preview):
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_6(self):
        uuid = 'aea9aa01-7db5-4de8-a29f-150a80c47727'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            while self.is_exist(L.import_media.media_library.loading_circle, 1):
                time.sleep(1)

            if self.is_exist(L.import_media.media_library.Video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_7(self):
        uuid = 'da4e5d16-6cdc-42d5-b4e0-8c6856b00dd0'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            file_name = "mp4.mp4"
            self.page_media.select_local_video(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def reenter_template(self):
        self.click(L.main.ai_effect.close)
        self.click(L.main.ai_effect.leave)
        self.click(L.main.ai_effect.template())
        # swipe up to free template for export test
        while self.is_exist(L.main.ai_effect.premium, 0.5):
            page_before = self.element(L.main.ai_effect.full_preview)
            self.driver.swipe_up()
            if page_before == self.element(L.main.ai_effect.full_preview):
                break
        self.click(L.main.ai_effect.try_now)

    def sce_6_4_8(self):
        uuid = '27f41d5f-29af-4ce2-a93d-b98a7a53171f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            file_name = "mkv.mkv"
            self.page_media.select_local_video(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)

            while self.is_exist(L.main.ai_effect.downloading):
                continue

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_9(self):
        uuid = '46a4a213-155f-4bf4-9f49-e7971e50c069'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            file_name = "slow_motion.mp4"
            self.page_media.select_local_video(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)

            while self.is_exist(L.main.ai_effect.downloading):
                continue

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_10(self):
        uuid = '0e5091f5-caf5-489b-9a76-2bdc5eac8483'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            file_name = "4k.mp4"
            self.page_media.select_local_video(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)

            while self.is_exist(L.main.ai_effect.downloading):
                continue

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_11(self):
        uuid = 'e7bde95b-875f-465e-ab3c-fa97b21c2641'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_12(self):
        uuid = '1b367024-715d-465c-a03b-2a7231eff70b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_13(self):
        uuid = '678e883f-7d47-4550-814a-5fa5445525b3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_14(self):
        uuid = '705a77b8-de7e-48ae-bd56-7f1d7dee2108'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_15(self):
        uuid = '8fe1d6d1-1668-417f-be33-52e0376bf427'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_16(self):
        uuid = 'add59eeb-d4b9-4f4e-8a38-9e392418be25'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            self.page_media.select_video_library("getty")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.newest)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.best_match)
            self.driver.driver.back()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_17(self):
        uuid = 'fa875287-e015-43e6-9464-07aa4af79c9d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_main.text_search(L.import_media.media_library.search, "search")
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_18(self):
        uuid = 'f9a25aa8-79b9-4fdd-a1b8-75df98ca28ba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.Video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_19(self):
        uuid = 'a2c237ce-9be0-41ed-9f33-fb5928f64129'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.Video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_20(self):
        uuid = '4f4c6732-a1eb-4224-aab8-ab3b35be08c7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_21(self):
        uuid = '03ade2c2-26f5-4f35-b8cf-6f6902681b23'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            self.page_media.select_video_library("getty_pro")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.newest)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.random)
            self.driver.driver.back()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_22(self):
        uuid = '36006f64-f596-4c1a-806b-5888b492cea5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_main.text_search(L.import_media.media_library.search, "search")
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_23(self):
        uuid = 'a631b422-8278-4405-be17-19a36bdf1169'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.Video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_24(self):
        uuid = '0645bdec-80e8-4cb5-bc71-f20f45506f49'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_25(self):
        uuid = '41f8a14e-13e8-4e62-a70d-fb00a6f89879'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.gettyimages_premium.buy_dialog.btn_buy)
            self.click(find_string("1-tap buy"), 10)
            self.click(L.import_media.media_library.media(), 10)
            self.click(L.import_media.media_library.next)

            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_26(self):
        uuid = '0a798223-d396-4e8a-83ac-b5b0274c6c18'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            if not self.page_media.select_video_library("giphy"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Can find giphy'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_27(self):
        uuid = 'a501cdc4-5a93-4600-9fb7-f53fdf072d88'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.main.ai_effect.back)
            self.click(L.main.ai_effect.try_now)

            self.page_media.select_video_library("pexels")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            global pic_src
            time.sleep(2)
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_all_orientation)
            self.driver.driver.back()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_28(self):
        uuid = '9eb5e76d-3a03-41b0-a1ea-75ada04053b6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_main.text_search(L.import_media.media_library.search, "search")
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_29(self):
        uuid = 'cac9790b-db7a-41bf-87fd-8b5712ed2f6f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.videoDisplay):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_30(self):
        uuid = '9cb0f207-62b7-4895-a05c-3efd4534f346'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.videoDisplay):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_31(self):
        uuid = '1c32f806-a485-4fc3-aeeb-0d9d48d4df28'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_32(self):
        uuid = '92c0bded-6eb1-4c63-99d3-1c165cded40c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            self.page_media.select_video_library("pixabay")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.newest)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            global pic_src
            time.sleep(2)
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.best_match)
            self.driver.driver.back()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_33(self):
        uuid = 'c8de0ffb-9fd9-4a88-a8c5-d452bd2a2681'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.page_main.text_search(L.import_media.media_library.search, "search")
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_34(self):
        uuid = 'eeee5f1d-b66b-4960-bb95-123f4704f20c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.Video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_35(self):
        uuid = '7c96446d-1b2e-4bc5-b2d2-a45f628f9be8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_36(self):
        uuid = 'c106a7ca-8477-4cd7-8e28-257f901908d3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.media_library.media())
            self.click(L.edit.try_before_buy.try_it)
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_37(self):
        uuid = 'bb17a360-fce3-444f-976c-9e0022ce648b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            self.page_media.switch_to_photo_library()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.descending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name, reverse=True)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_38(self):
        uuid = 'e2848afa-8649-4064-8649-db1da9d1dec4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_name)
            self.click(L.import_media.sort_menu.ascending)
            self.driver.driver.back()

            files_name = []
            files = self.elements(L.import_media.media_library.file_name(0))
            for i in files:
                files_name.append(i.text)
            file_name_order = sorted(files_name)

            if file_name_order == files_name:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] files_name order incorrect: {files_name}'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_39(self):
        uuid = 'e571055b-e737-4284-9b5c-cc698238afa1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            file_name = "jpg.jpg"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_40(self):
        uuid = 'bdb051bd-5092-4e9e-9430-1dee5a391f4f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            file_name = "gif.gif"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_41(self):
        uuid = 'a4302371-48b7-4cac-86c2-7a85889d793b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            file_name = "png.png"
            self.page_media.select_local_photo(self.test_material_folder, file_name)
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"

    def sce_6_4_42(self):
        uuid = '7f2aeaf7-62d2-4348-b7a5-b4c377cb3ea6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        try:
            self.reenter_template()

            if not self.is_exist(L.import_media.media_library.color_board):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Can find color_board'

            self.report.new_result(uuid, result, fail_log=fail_log)
            return "PASS" if result else "FAIL"
        except Exception as err:
            logger(f"[Error] {err}")
            self.report.new_result(uuid, False, fail_log="ERROR")
            return "ERROR"



    @report.exception_screenshot
    def test_sce_6_1_1_to_135(self):
        result = {"sce_6_1_1": self.sce_6_1_1(),
                  "sce_6_2_1": self.sce_6_2_1(),
                  "sce_6_2_2": self.sce_6_2_2(),
                  "sce_6_2_3": self.sce_6_2_3(),
                  # "sce_6_2_4" is in sce_6_2_6,
                  # "sce_6_2_5" is in sce_6_2_6,
                  "sce_6_2_6": self.sce_6_2_6(),
                  "sce_6_3_1": self.sce_6_3_1(),
                  "sce_6_3_2": self.sce_6_3_2(),
                  "sce_6_3_3": self.sce_6_3_3(),
                  "sce_6_3_4": self.sce_6_3_4(),
                  "sce_6_3_5": self.sce_6_3_5(),
                  "sce_6_3_6": self.sce_6_3_6(),
                  "sce_6_4_1": self.sce_6_4_1(),
                  "sce_6_4_2": self.sce_6_4_2(),
                  "sce_6_4_3": self.sce_6_4_3(),
                  "sce_6_4_4": self.sce_6_4_4(),
                  "sce_6_4_5": self.sce_6_4_5(),
                  "sce_6_4_6": self.sce_6_4_6(),
                  "sce_6_4_7": self.sce_6_4_7(),
                  "sce_6_4_8": self.sce_6_4_8(),
                  "sce_6_4_9": self.sce_6_4_9(),
                  "sce_6_4_10": self.sce_6_4_10(),
                  "sce_6_4_11": self.sce_6_4_11(),
                  "sce_6_4_12": self.sce_6_4_12(),
                  "sce_6_4_13": self.sce_6_4_13(),
                  "sce_6_4_14": self.sce_6_4_14(),
                  "sce_6_4_15": self.sce_6_4_15(),
                  "sce_6_4_16": self.sce_6_4_16(),
                  "sce_6_4_17": self.sce_6_4_17(),
                  "sce_6_4_18": self.sce_6_4_18(),
                  "sce_6_4_19": self.sce_6_4_19(),
                  "sce_6_4_20": self.sce_6_4_20(),
                  "sce_6_4_21": self.sce_6_4_21(),
                  "sce_6_4_22": self.sce_6_4_22(),
                  "sce_6_4_23": self.sce_6_4_23(),
                  "sce_6_4_24": self.sce_6_4_24(),
                  "sce_6_4_25": self.sce_6_4_25(),
                  "sce_6_4_26": self.sce_6_4_26(),
                  "sce_6_4_27": self.sce_6_4_27(),
                  "sce_6_4_28": self.sce_6_4_28(),
                  "sce_6_4_29": self.sce_6_4_29(),
                  "sce_6_4_30": self.sce_6_4_30(),
                  "sce_6_4_31": self.sce_6_4_31(),
                  "sce_6_4_32": self.sce_6_4_32(),
                  "sce_6_4_33": self.sce_6_4_33(),
                  "sce_6_4_34": self.sce_6_4_34(),
                  "sce_6_4_35": self.sce_6_4_35(),
                  "sce_6_4_36": self.sce_6_4_36(),
                  "sce_6_4_37": self.sce_6_4_37(),
                  "sce_6_4_38": self.sce_6_4_38(),
                  "sce_6_4_39": self.sce_6_4_39(),
                  "sce_6_4_40": self.sce_6_4_40(),
                  "sce_6_4_41": self.sce_6_4_41(),
                  "sce_6_4_42": self.sce_6_4_42(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")