import traceback

import pytest, os, inspect, base64, sys, time
from os import path
from appium.webdriver.common.touch_action import TouchAction

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory

from .conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

sys.path.insert(0, (path.dirname(path.dirname(__file__))))

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'


class Test_Shortcut_Body_Effect:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver
        self.uuid = [
            "4a7cb6cf-862c-44f6-a1a0-6c4afc3eb376",
            "4f5e9611-d4ce-4eef-85a2-30f0f82f7bbc",
            "155def96-b003-4b97-8d8f-eafe0a963920",
            "bfeb85d9-3e71-476f-80f5-7ce948e89d2e",
            "7081c779-aecb-47c6-ad16-42082691e61f",
            "7869f110-b898-42b9-b90e-435890d32621",
            "5dc7175f-1e5f-4099-a0b9-c0520dcad992",
            "a9413f69-1fc5-4fb8-a59b-8195457828aa",
            "1be4b42d-1bd6-4ecc-a96f-10ee18b379c1",
            "50717d25-e51e-4814-b3b7-4c32dfade009",
            "68347dfe-2643-430f-852b-f91b8e04cbf2",
            "3d6f1487-c898-4c79-ac7f-c8d14a650343",
            "dd0f6aa1-c65f-4920-b10a-e2c81efab8b1",
            "b933c6ca-1b77-47b6-aa3f-0c8a03492217",
            "0c6a13da-c10b-4743-86d9-b38d6f54b823",
            "ba0a505a-b312-4313-9052-a5037968cd57",
            "3417bf3f-cd1c-4cef-ad65-a1b09f8eed34",
            "645f399a-cfac-48c9-8b4b-448e41b9a82f",
            "50d3b7e7-4e07-44a9-93ea-8de7dbe5fa09",
            "36b13541-bf82-4452-82de-87ca385dd93c",
            "8bc0f3f6-0a2b-4ccb-95fb-2463d8d28493",
            "0fa87c12-fabf-4f48-b09f-16015c426a2d",
            "a5e69af1-608c-4637-99d7-ac48630c53d5",
            "e232531f-887c-4850-896d-8731f816b0b9",
            "079d77ea-27a1-4afa-bd1e-30db8bdfcd49",
            "3014559c-61a5-4ea8-bc38-4bd214179c7a",
            "961e422e-05ed-45d0-8e39-7ef868c6de2f",
            "2874330f-f344-4cc6-9b79-a8424d441d31",
            "3cb7af54-26d6-4e51-b3cd-af945ff01696",
            "056e80a8-5083-440b-a0d8-089860d98362",
            "6600f57d-5cfb-4bb0-b675-b72a2504277b",
            "7aa098f7-f6b9-467c-b413-ae84c24dd5f2",
            "66ce3366-5bc8-45db-9b58-892f115482c6"
                     ]

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

        
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='low', video_fps=30)
        driver.driver.launch_app()
        yield
        self.driver.driver.stop_recording_screen()
        driver.driver.close_app()

    def stop_recording(self, test_case_name):
        self.video_file_path = os.path.join(os.path.dirname(__file__), "recording", f"{test_case_name}.mp4")
        recording_data = self.driver.driver.stop_recording_screen()
        with open(self.video_file_path, 'wb') as video_file:
            video_file.write(base64.b64decode(recording_data))
        logger(f'Screen recording saved: {self.video_file_path}')
        self.driver.driver.start_recording_screen(video_type='mp4', video_quality='medium', video_fps=30)

    def sce_6_3_1(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Body Effect')

            if self.is_exist(find_string('Body Effect')):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Demo page')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Body Effect')

            return "FAIL"

    def sce_6_3_2(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.demo_back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_3_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)

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
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_3_4(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.import_media.media_library.back)

            if self.is_exist(L.main.shortcut.shortcut_name(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot return launcher')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_3_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_back)

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
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_3_6(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            if self.is_exist(L.main.shortcut.body_effect.effect(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Body Effect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)
            self.click(L.import_media.media_library.btn_preview())
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_3_7(self):
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
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_3_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            if self.is_exist(L.main.shortcut.body_effect.effect(0)):
                
                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Body Effect')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_3_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.play)
            time.sleep(3)
            self.timecode_play = self.element(L.main.shortcut.timecode).text

            if self.timecode_play != "00:00":
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {self.timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_3_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.play)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play != self.timecode_play:
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_3_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play == '00:00':
                
                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            self.stop_recording(func_name)
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('Body Effect')
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder,video_9_16)
            self.page_media.waiting()

            return "FAIL"



    def sce_6_4_1(self):
        uuid = '5974cd43-3dbe-419e-8406-07b89c4990f4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.main.ai_effect.back)

            if self.is_exist(L.main.ai_effect.try_now):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Cannot find try_now'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_2(self):
        uuid = '06054245-4a09-4b65-86d1-435dc32b0292'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_3(self):
        uuid = '1c1ca59a-306a-491b-9aa8-403dba30906c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_4(self):
        uuid = 'e2cadaca-6237-4a4f-acb6-d56142c12a35'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_5(self):
        uuid = '1cfe4a37-eb49-47a1-a872-927d77349328'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            for i in range(60):
                if self.is_exist(L.import_media.media_library.loading_circle, 1):
                    time.sleep(1)
                else:
                    break

            if self.is_exist(L.import_media.media_library.video.display_preview):
                self.driver.driver.back()
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_6(self):
        uuid = 'aea9aa01-7db5-4de8-a29f-150a80c47727'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_7(self):
        uuid = 'da4e5d16-6cdc-42d5-b4e0-8c6856b00dd0'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_8(self):
        uuid = '27f41d5f-29af-4ce2-a93d-b98a7a53171f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_9(self):
        uuid = '46a4a213-155f-4bf4-9f49-e7971e50c069'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_10(self):
        uuid = '0e5091f5-caf5-489b-9a76-2bdc5eac8483'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_11(self):
        uuid = 'e7bde95b-875f-465e-ab3c-fa97b21c2641'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_12(self):
        uuid = '1b367024-715d-465c-a03b-2a7231eff70b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_13(self):
        uuid = '678e883f-7d47-4550-814a-5fa5445525b3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_14(self):
        uuid = '705a77b8-de7e-48ae-bd56-7f1d7dee2108'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_15(self):
        uuid = '8fe1d6d1-1668-417f-be33-52e0376bf427'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_16(self):
        uuid = 'add59eeb-d4b9-4f4e-8a38-9e392418be25'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_17(self):
        uuid = 'fa875287-e015-43e6-9464-07aa4af79c9d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_18(self):
        uuid = 'f9a25aa8-79b9-4fdd-a1b8-75df98ca28ba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_19(self):
        uuid = 'a2c237ce-9be0-41ed-9f33-fb5928f64129'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_20(self):
        uuid = '4f4c6732-a1eb-4224-aab8-ab3b35be08c7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_21(self):
        uuid = '03ade2c2-26f5-4f35-b8cf-6f6902681b23'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_22(self):
        uuid = '36006f64-f596-4c1a-806b-5888b492cea5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_23(self):
        uuid = 'a631b422-8278-4405-be17-19a36bdf1169'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_24(self):
        uuid = '0645bdec-80e8-4cb5-bc71-f20f45506f49'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_25(self):
        uuid = '41f8a14e-13e8-4e62-a70d-fb00a6f89879'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.gettyimages_premium.buy_dialog.btn_buy)
            self.click(find_string("1-tap buy"), 10)
            self.click(find_string("Not now"))
            self.click(L.import_media.media_library.media(), 10)
            self.click(L.import_media.media_library.next)

            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()
            return "FAIL"

    def sce_6_4_26(self):
        uuid = '0a798223-d396-4e8a-83ac-b5b0274c6c18'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)

            if not self.page_media.select_video_library("giphy"):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Can find giphy'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            return "FAIL"

    def sce_6_4_27(self):
        uuid = 'a501cdc4-5a93-4600-9fb7-f53fdf072d88'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pexels")

            return "FAIL"

    def sce_6_4_28(self):
        uuid = '9eb5e76d-3a03-41b0-a1ea-75ada04053b6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pexels")

            return "FAIL"

    def sce_6_4_29(self):
        uuid = 'cac9790b-db7a-41bf-87fd-8b5712ed2f6f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            timeout = self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.videoDisplay) and timeout:
                result = True
                fail_log = None
            elif not timeout:
                result = False
                fail_log = '\n[Fail] Media loading timeout'
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pexels")

            return "FAIL"

    def sce_6_4_30(self):
        uuid = '9cb0f207-62b7-4895-a05c-3efd4534f346'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pexels")

            return "FAIL"

    def sce_6_4_31(self):
        uuid = '1c32f806-a485-4fc3-aeeb-0d9d48d4df28'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_32(self):
        uuid = '92c0bded-6eb1-4c63-99d3-1c165cded40c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pixabay")

            return "FAIL"

    def sce_6_4_33(self):
        uuid = 'c8de0ffb-9fd9-4a88-a8c5-d452bd2a2681'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pixabay")

            return "FAIL"

    def sce_6_4_34(self):
        uuid = 'eeee5f1d-b66b-4960-bb95-123f4704f20c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            timeout = self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.display_preview) and timeout:
                result = True
                fail_log = None
            elif not timeout:
                result = False
                fail_log = '\n[Fail] Media loading timeout'
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pixabay")

            return "FAIL"

    def sce_6_4_35(self):
        uuid = '7c96446d-1b2e-4bc5-b2d2-a45f628f9be8'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            waiting = self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.video.display_preview) and waiting:
                result = True
                fail_log = None
            elif not waiting:
                result = False
                fail_log = '\n[Fail] Media loading timeout'
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_video_library("pixabay")

            return "FAIL"

    def sce_6_4_36(self):
        uuid = 'c106a7ca-8477-4cd7-8e28-257f901908d3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_37(self):
        uuid = 'bb17a360-fce3-444f-976c-9e0022ce648b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()

            return "FAIL"

    def sce_6_4_38(self):
        uuid = 'e2848afa-8649-4064-8649-db1da9d1dec4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_39(self):
        uuid = 'e571055b-e737-4284-9b5c-cc698238afa1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_40(self):
        uuid = 'bdb051bd-5092-4e9e-9430-1dee5a391f4f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_41(self):
        uuid = 'a4302371-48b7-4cac-86c2-7a85889d793b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_42(self):
        uuid = '7f2aeaf7-62d2-4348-b7a5-b4c377cb3ea6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            if not self.is_exist(L.import_media.media_library.color_board):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Can find color_board'

            self.click(L.main.ai_effect.back)

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_43(self):
        uuid = '47039469-aa7c-4628-bd2a-03729c325a41'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_44(self):
        uuid = '70dd1f07-5aea-403a-9029-9419f42d4edc'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_45(self):
        uuid = '0591683c-e463-4e99-88ef-3a74cce46e17'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_46(self):
        uuid = '37c652fe-f97f-451f-a0e3-63d53e859ac3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_47(self):
        uuid = '41c0c860-9e5a-4545-ad54-57fea2dbf769'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.report.new_result(uuid, None, 'N/A', 'Stock is hidden')
            return 'N/A'
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_48(self):
        uuid = 'fa743ffe-22c0-485a-adfb-2975d16b5537'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.main.ai_effect.try_now)

            self.page_media.select_photo_library("getty")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_49(self):
        uuid = '041fcba0-af79-439f-9378-009fc9e08c9f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_50(self):
        uuid = 'f7e26440-d1b1-4704-b76e-88117bf520ba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_51(self):
        uuid = 'c2ad3af3-00a1-4e6e-8d0c-4cacb75e98b5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_52(self):
        uuid = 'a11cb1b4-cd8d-4f2f-8c28-7a4a7cae5aed'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_53(self):
        uuid = 'afa2ced7-bdb2-4054-982c-99c3a06fb899'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("getty_pro")
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_horizontal)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            global pic_src
            pic_src = self.page_main.h_full_screenshot()
            self.click(L.import_media.sort_menu.sort_button)
            self.click(L.import_media.sort_menu.by_vertical)
            self.driver.driver.back()
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_54(self):
        uuid = '7718ae03-38e7-4989-8861-9ecc98bd6b23'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_55(self):
        uuid = '4d1a50ad-1226-41fd-9695-9bfd0e531b1d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_56(self):
        uuid = 'ee83ed66-bb25-4843-aad0-545fe8c5d624'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_57(self):
        uuid = 'ebe7c158-bf56-4984-9646-d3e5e59dbb26'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_58(self):
        uuid = '0597ea98-5cae-4b2a-8714-8289bb624ca2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("pexels")
            self.click(L.import_media.media_library.pexels_link)

            if self.is_exist(find_string("pexels.com")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Not find "pexels.com"'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_59(self):
        uuid = 'c9683ebd-c159-4c88-9a96-3cdcf4a637e4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            pic_src = self.page_main.h_full_screenshot()
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_60(self):
        uuid = '9df4e187-e974-4c26-ba04-fa308832c0a9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_61(self):
        uuid = 'e964df3f-8d0a-4eac-b898-49be83ac472c'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    def sce_6_4_62(self):
        uuid = '5f904d0e-7fb8-48b2-9eed-18806a334f2b'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_63(self):
        uuid = '83c6529e-f81b-4f31-a726-82f5cb4b3df5'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.page_media.select_photo_library("pixabay")
            self.click(L.import_media.media_library.pixabay_link)

            if self.is_exist(find_string("pixabay.com")):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Not find "pixabay.com"'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_64(self):
        uuid = 'ffe5e33c-17cd-4856-b6f1-18898714f950'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            pic_src = self.page_main.h_full_screenshot()
            self.page_media.text_search("search", L.import_media.media_library.search)
            self.page_media.waiting_loading()
            time.sleep(2)
            pic_tgt = self.page_main.h_full_screenshot()

            if not HCompareImg(pic_tgt, pic_src).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Images are the same'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_65(self):
        uuid = '50ebb786-fa6b-4ac7-9f12-34feb0b6a0fe'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.btn_preview())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_66(self):
        uuid = '68727700-ba6e-4be4-a988-386898963aba'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.long_press(L.import_media.media_library.media())
            self.page_media.waiting_loading()

            if self.is_exist(L.import_media.media_library.photo.display_preview):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] id "display_preview" is not exist'

            self.driver.driver.back()

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker()
            self.page_media.select_photo_library("pixabay")

            return "FAIL"

    def sce_6_4_67(self):
        uuid = '57850b35-b48c-4a3f-affc-1e87a89763c7'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

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

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_68(self):
        uuid = 'f683a635-e229-4ce7-8fee-3f34ff839c7a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.click(L.import_media.media_library.video.video_capture)
            self.click(L.import_media.media_library.video.start_recording)
            time.sleep(5)
            self.click(L.import_media.media_library.video.stop_recording)
            self.click(L.import_media.media_library.video.camera_ok)
            self.page_media.sort_date_descend()
            self.click(L.import_media.media_library.media())
            self.click(L.import_media.media_library.next)
            import_timeout = self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce) and import_timeout:
                result = True
                fail_log = None
            elif not import_timeout:
                result = False
                fail_log = '\n[Fail] Media import timeout'
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_69(self):
        uuid = '6b4b4ae3-2d24-4914-aebe-688bb2424c75'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True)

            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.photo.photo_capture)
            self.click(L.import_media.media_library.photo.take_picture)
            self.click(L.import_media.media_library.photo.camera_ok)
            self.click(L.import_media.media_library.media())
            self.click(L.import_media.media_library.next)
            import_timeout = self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce) and import_timeout:
                result = True
                fail_log = None
            elif not import_timeout:
                result = False
                fail_log = '\n[Fail] Media import timeout'
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_70(self):
        uuid = '19a47ca2-91a4-40cb-a7ed-481baa667804'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)
            self.page_media.select_video_library("google_drive")
            self.click(('id', 'com.google.android.gms:id/account_name'))
            self.page_media.waiting_loading()
            self.click(L.import_media.media_library.google_folder())
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_71(self):
        uuid = '4bcad19b-ad8b-48c8-a2bb-1ba5c9ec4be6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library()
            self.page_ai_effect.enter_free_template_media_picker(skip_enter_template_library=True)
            self.page_media.select_photo_library("google_drive")
            self.click(('id', 'com.google.android.gms:id/account_name'), 3)
            self.page_media.waiting_loading()
            self.click(L.import_media.media_library.google_folder())
            self.click(L.import_media.media_library.media())
            self.page_media.waiting_download()
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.is_exist(L.main.ai_effect.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = '\n[Fail] Cannot find produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()

            return "FAIL"

    def sce_6_4_72(self):
        uuid = 'e424e887-0930-4d95-b868-aa69a8d9371f'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.play_btn)
            playing_time = self.element(L.ai_effect.editor.playing_time).text

            if playing_time != "00:00":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] playing time is not increase: {playing_time}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor()
            return "FAIL"

    def sce_6_4_73(self):
        uuid = '2be47a53-4aa2-4337-8415-d54d12f9e7a6'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.leave_editor_to_library(reenter=True, clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            selected_num = len(self.elements(L.import_media.media_library.media_order(0)))

            if selected_num == 2:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] media order number incorrect: {selected_num}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            return "FAIL"

    def sce_6_4_74(self):
        uuid = '07286423-8bf8-4644-a21a-d2e7d07b15f9'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            if self.element(L.import_media.media_library.next).get_attribute("enabled") == "true":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] "Next" button is not clickable'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            return "FAIL"

    def sce_6_5_1(self):
        uuid = '5f7ad02b-21bd-49bd-9981-4bdf351b12ff'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.next)

            if self.is_exist(L.import_media.media_library.downloading):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] downloading bar is not exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_free_template_media_picker(clip=2)
            self.click(L.import_media.media_library.photo_entry)
            self.click(L.import_media.media_library.media(1))
            self.click(L.import_media.media_library.media(2))
            self.click(L.import_media.media_library.next)
            return "FAIL"

    def sce_6_5_2(self):
        uuid = 'eaaadb38-b1d0-4554-9c21-2352d30cd212'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.cancel)

            if self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] "Next" button is not exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)

            return "FAIL"

    def sce_6_6_1(self):
        uuid = '6cbfa1ad-7017-4fba-83da-ce0d89d04513'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.next)
            self.page_media.waiting_download()

            if self.page_ai_effect.leave_editor_to_library:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] back to library fail'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_template_library()
            return "FAIL"

    def sce_6_6_2(self):
        uuid = '6c2a7cab-5d78-418b-abd4-b35f9d53aad3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_ai_effect.enter_editor(skip_enter_template_library=True, clip=2)
            time.sleep(2)

            if self.element(L.ai_effect.editor.playing_time).text != "00:00":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Playing time = "00:00"'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_3(self):
        uuid = '485634cf-42c7-4821-998c-7cd85c29d18e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.replace_all)

            if self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No "Next" button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_4(self):
        uuid = '2b98fc6b-6ce5-45d0-9362-89b7f3c2ce68'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.back)
            self.click(L.ai_effect.editor.volume_entry)
            volume = self.element(L.ai_effect.editor.slider_text).text

            if volume == "100":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Volume not 100: {volume}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_5(self):
        uuid = 'eb0b0f9b-30bb-446f-b2fa-9ee61e81475a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.volume.play)

            if not self.is_exist(L.ai_effect.editor.volume.play, 2):
                self.click(L.ai_effect.editor.preview)
                if self.is_exist(L.ai_effect.editor.volume.play):
                    result = True
                    fail_log = None
                else:
                    result = False
                    fail_log = f'\n[Fail] Preview is not stopped after tapped'
            else:
                result = False
                fail_log = f'\n[Fail] Play btn is not disappear tapped'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_6(self):
        uuid = '3994d2ce-a9a4-4ab4-a917-b655ef53e227'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.volume.cancel)

            if self.is_exist(L.ai_effect.editor.volume_entry):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No volume entry'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.volume_entry)
            return "FAIL"

    def sce_6_6_7(self):
        uuid = '12304abd-5541-48f7-9d50-1489c5460bd1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_main.drag_element(L.ai_effect.editor.volume.slider_text, L.ai_effect.editor.volume.slider)
            self.click(L.ai_effect.editor.volume.apply)

            if self.is_exist(L.ai_effect.editor.volume_entry):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No volume entry'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_8(self):
        uuid = '3a6192b7-3212-441e-8f7e-eb1b97563169'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            playing_time = self.click(L.ai_effect.editor.playing_time).text
            self.click(L.ai_effect.editor.play_btn)
            time.sleep(2)

            if self.click(L.ai_effect.editor.playing_time).text != playing_time:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Playing time no change'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_9(self):
        uuid = '59c63a35-fbec-4df1-8745-a42cb81c9f40'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.page_main.drag_slider_from_center_to_left(L.ai_effect.editor.playing_bar)
            preview_before = self.page_main.get_picture(L.ai_effect.editor.preview)
            self.page_main.drag_slider_from_center_to_right(L.ai_effect.editor.playing_bar)
            preview_after = self.page_main.get_picture(L.ai_effect.editor.preview)

            if not HCompareImg(preview_after, preview_before).full_compare_result():
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Images are the same after dragged slider'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_10(self):
        uuid = 'e9988c06-7a3c-49cd-955b-4ba45e5fa138'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Replace"))

            if not self.is_exist(L.import_media.media_library.next):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Exist "Next" button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_11(self):
        uuid = '77d3f699-a355-484a-a7f7-3a4f26362519'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.import_media.media_library.back)
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Crop & Range"))
            self.driver.zoom(L.ai_effect.editor.preview)
            self.driver.drag_slider_from_center_to_left(L.ai_effect.editor.crop_range.trim_bar)
            pic_src = self.page_main.get_picture(L.ai_effect.editor.preview)
            self.click(L.ai_effect.editor.crop_range.done)
            self.page_media.waiting_download()
            pic_tgt = self.page_main.get_picture(L.ai_effect.editor.preview)

            if HCompareImg(pic_tgt, pic_src).full_compare() >= 0.9:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Similarity < 0.9'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_12(self):
        uuid = '7747da3f-31f6-4c19-8eae-a9fc1bf052b3'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            if not self.is_exist(L.ai_effect.editor.edit):
                self.click(L.ai_effect.editor.clip())
            self.click(L.ai_effect.editor.edit)
            self.click(find_string("Volume"))
            volume = self.element(L.ai_effect.editor.slider_text).text

            if not self.is_exist(L.ai_effect.editor.volume.play, 2):
                self.click(L.ai_effect.editor.preview)
                if self.is_exist(L.ai_effect.editor.volume.play):
                    if volume == "0":
                        result = True
                        fail_log = None
                    else:
                        result = False
                        fail_log = f'\n[Fail] Volume not 100: {volume}'
                else:
                    result = False
                    fail_log = f'\n[Fail] Preview is not stopped after tapped'
            else:
                result = False
                fail_log = f'\n[Fail] Play btn is not disappear tapped'

            self.driver.drag_slider_from_left_to_right()
            self.click(L.ai_effect.editor.volume.apply)

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_6_13(self):
        uuid = '2776fd95-8f2d-4019-99c9-4217435a9171'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.export)

            if self.is_exist(L.ai_effect.editor.produce.produce):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No produce button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_1(self):
        uuid = '74673b45-4847-48f8-b55e-2395b40dd80d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.produce.back)

            if not self.is_exist(L.ai_effect.editor.produce.back):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_7_2(self):
        uuid = '6f5aca48-62ff-49be-a11e-0569569e8116'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.export)
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_1)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "0.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_3(self):
        uuid = '4fe8c038-5eac-41a3-8cfa-d6d4b973ebe1'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_2)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "1.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_4(self):
        uuid = '52b6104e-32de-4807-971c-9d37ad05737d'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_3)

            if self.element(L.ai_effect.editor.produce.resolution_bar).text == "2.0":
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] Back button is still exist'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_5(self):
        uuid = '1fb7010d-3f70-46a1-97d8-b7af71614290'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.drag_element(L.ai_effect.editor.produce.resolution_bar, L.ai_effect.editor.produce.resolution_4)

            if self.is_exist(L.produce.iap_back):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No IAP page'

            self.click(L.produce.iap_back)

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            return "FAIL"

    def sce_6_7_6(self):
        uuid = '855995da-c1ed-455f-b4bc-0932fee039d4'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.produce.produce)

            if self.is_exist(L.ai_effect.producing.progress_bar):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No progress bar'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            return "FAIL"

    def sce_6_7_7(self):
        uuid = '4167881a-77ab-42c0-b923-9922bf7f2656'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.producing.cancel)
            self.click(L.ai_effect.editor.producing.cancel_ok)

            if self.is_exist(L.ai_effect.editor.export):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No export button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break
            return "FAIL"

    def sce_6_8_1(self):
        uuid = '1f876e02-b413-4a06-9147-e8c9f3535988'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.produce.produced_back)

            if self.is_exist(L.ai_effect.editor.export):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No export button'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            return "FAIL"

    def sce_6_8_2(self):
        uuid = '60f0b428-a199-432a-a07a-4cf49e43aa38'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break

            self.click(L.ai_effect.producing.save_to_file)
            current_pack = self.driver.driver.current_package

            if current_pack != pdr_package:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] current_package is still pdr: {current_pack}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break
            return "FAIL"

    def sce_6_8_3(self):
        uuid = 'edde24ab-5aa4-49c9-b9ea-b68018b17148'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.driver.activate_app(pdr_package)
            self.click(L.ai_effect.producing.share_app_name())
            self.click(L.ai_effect.producing.share_ok, 2)
            current_pack = self.driver.driver.current_package

            if current_pack != pdr_package:
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] current_package is still pdr: {current_pack}'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            self.driver.driver.close_app()
            self.driver.driver.launch_app()
            self.page_ai_effect.enter_editor(clip=2)
            self.click(L.ai_effect.editor.export)
            self.click(L.ai_effect.editor.produce.produce)
            for i in range(60):
                if not self.is_exist(L.ai_effect.producing.done):
                    time.sleep(1)
                else:
                    break

            return "FAIL"

    def sce_6_8_4(self):
        uuid = '3d8d3218-05f2-4306-8187-82b87155a3bb'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        

        try:
            self.driver.driver.back()
            self.click(L.ai_effect.producing.done)

            if self.is_exist(L.ai_effect.template.template()):
                result = True
                fail_log = None
            else:
                result = False
                fail_log = f'\n[Fail] No template'

            
            if result:
                return "PASS"
            else:
                raise Exception(fail_log)
        except Exception as err:
            logger(err)

            return "FAIL"

    
    def test_case(self):
        result = {"sce_6_3_1": self.sce_6_3_1(),
                  "sce_6_3_2": self.sce_6_3_2(),
                  "sce_6_3_3": self.sce_6_3_3(),
                  "sce_6_3_4": self.sce_6_3_4(),
                  "sce_6_3_5": self.sce_6_3_5(),
                  "sce_6_3_6": self.sce_6_3_6(),
                  "sce_6_3_7": self.sce_6_3_7(),
                  "sce_6_3_8": self.sce_6_3_8(),
                  "sce_6_3_9": self.sce_6_3_9(),
                  "sce_6_3_10": self.sce_6_3_10(),
                  "sce_6_3_11": self.sce_6_3_11(),
                  }
        for key, value in result.items():
            if value != "PASS":
                print(f"[{value}] {key}")
