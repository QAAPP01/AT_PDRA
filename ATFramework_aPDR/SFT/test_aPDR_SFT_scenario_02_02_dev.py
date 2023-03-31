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


class Test_SFT_Scenario_02_02:
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

    def sce_2_2_1(self):
        uuid = '4979f807-43ed-48ae-b85f-9a28b2ab989a'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        self.page_main.enter_launcher()

        if self.page_main.enter_timeline():
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Cannot find timeline canvas'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_2_2_2(self):
        uuid = '6adefecd-8cbd-4164-aa84-9dd4bd06577e'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        self.page_media.add_master_media('photo', TEST_MATERIAL_FOLDER, file_photo)
        self.click(L.edit.timeline.master_photo(file_photo))
        self.page_edit.click_sub_tool("Pan & Zoom")
        self.click()
        pic_src = self.page_main.get_preview_pic()
        self.click(L.edit.menu.play)
        time.sleep(10)
        pic_tgt = self.page_main.get_preview_pic()

        if HCompareImg(pic_tgt, pic_src).full_compare_result():
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Images are different'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    def sce_2_2_3(self):
        uuid = 'd49362dd-6d87-4c27-8d5f-785749caeef2'
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")
        case_id = func_name.split("sce_")[1]
        self.report.start_uuid(uuid)

        self.page_media.add_master_media('photo', TEST_MATERIAL_FOLDER, file_photo)
        self.click(L.edit.timeline.master_photo(file_photo))
        self.page_edit.click_sub_tool("Pan & Zoom")
        self.click()
        pic_src = self.page_main.get_preview_pic()
        self.click(L.edit.menu.play)
        time.sleep(10)
        pic_tgt = self.page_main.get_preview_pic()

        if HCompareImg(pic_tgt, pic_src).full_compare_result():
            result = True
            fail_log = None
        else:
            result = False
            fail_log = '\n[Fail] Cannot find timeline canvas'

        self.report.new_result(uuid, result, fail_log=fail_log)
        return "PASS" if result else "FAIL"

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_01(self):
        self.report.start_uuid('4979f807-43ed-48ae-b85f-9a28b2ab989a')
        media_list = ['slow_motion.mp4', 'png.png']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result('4979f807-43ed-48ae-b85f-9a28b2ab989a',
                               page_edit.check_preview_aspect_ratio(project_title))
        self.report.start_uuid('255f3e69-7e80-4d64-ad07-b99646558dae')
        #add media video & photo
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_video_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_date)
        #page_media.click(L.import_media.video_library.sort_menu.descending)
        #page_media.driver.driver.back()
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        #color preset - video
        time.sleep(5)
        page_edit.timeline_select_media(media_list[0], 'Video')
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_3).click()
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_8).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = CompareImage(pic_base, pic_after, 9).compare_image()
        self.report.new_result('255f3e69-7e80-4d64-ad07-b99646558dae',
                               True if not compare_result or compare_result == 100 else False)
        self.report.start_uuid('11b755de-eaa4-4232-afe5-d09b6cca72f6')
        pic_base = pic_after
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        page_edit.el(L.edit.menu.play).click()
        pic_after = page_edit.get_preview_pic()
        compare_result = CompareImage(pic_base, pic_after, 9).compare_image()
        self.report.new_result('11b755de-eaa4-4232-afe5-d09b6cca72f6',
                               True if not compare_result or compare_result == 100 else False)
        self.report.start_uuid('01576a37-c1e2-4ff0-8663-74387b5036ed')
        page_edit.el(L.edit.menu.delete).click()
        #color preset - photo
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_date)
        #page_media.click(L.import_media.video_library.sort_menu.descending)
        #page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_media(media_list[1], 'Photo')
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_3).click()
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_8).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = CompareImage(pic_base, pic_after, 9).compare_image()
        self.report.new_result('01576a37-c1e2-4ff0-8663-74387b5036ed',
                               True if not compare_result or compare_result == 100 else False)
        self.report.start_uuid('185dee12-1fe5-4fe1-a0a9-941d643e1212')
        pic_base = pic_after
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result = CompareImage(pic_base, pic_after, 7).compare_image()
        self.report.new_result('185dee12-1fe5-4fe1-a0a9-941d643e1212',
                               True if not compare_result or compare_result == 100 else False) 
        #                       True if not compare_result or compare_result == 100 else False) 
        self.report.start_uuid('845d4a9d-6ec5-468d-8421-35cabc94d3f9')
        # Brightness
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        #page_edit.el(L.edit.color_sub.adjust).click()
        page_edit.el(L.edit.menu.back_session).click()
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('845d4a9d-6ec5-468d-8421-35cabc94d3f9', True if number == 0 else False)
        self.report.start_uuid('7808a09b-9f46-43b2-8e53-fde4bd1d05ff')
        page_edit.color.adjust.brightness.set_progress(0.7)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('7808a09b-9f46-43b2-8e53-fde4bd1d05ff', True if number > 0 else False)
        self.report.start_uuid('3a8cde6e-6b62-42c4-89c5-fe4ae98647b8')
        page_edit.color.adjust.brightness.set_progress(0.3)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('3a8cde6e-6b62-42c4-89c5-fe4ae98647b8', True if number < 0 else False)
        self.report.start_uuid('2ea6ab9e-71e4-48bd-ba43-b9cd2654efaf')
        page_edit.color.adjust.brightness.set_progress(0)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('2ea6ab9e-71e4-48bd-ba43-b9cd2654efaf', True if number == -100 else False)
        self.report.start_uuid('8dc75ff8-4ef9-4fdd-9dbd-c113c112b494')
        page_edit.color.adjust.brightness.set_progress(1)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('8dc75ff8-4ef9-4fdd-9dbd-c113c112b494', True if number == 100 else False)
        self.report.start_uuid('b8aedb47-bb52-43b9-8712-4cf7ded8a7cf')
        #Contrast
        page_edit.select_adjustment_from_bottom_edit_menu('Contrast')
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('b8aedb47-bb52-43b9-8712-4cf7ded8a7cf', True if number == 0 else False)
        self.report.start_uuid('89e31121-4472-4f2f-ac47-47691b592cc9')
        page_edit.color.adjust.contrast.set_progress(0.7)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('89e31121-4472-4f2f-ac47-47691b592cc9', True if number > 0 else False)
        self.report.start_uuid('3160506b-92e6-4796-b463-461306d7cf68')
        page_edit.color.adjust.contrast.set_progress(0.3)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('3160506b-92e6-4796-b463-461306d7cf68', True if number < 0 else False)
        self.report.start_uuid('35fa5496-30c2-4666-84d0-218fefa4e7ac')
        page_edit.color.adjust.contrast.set_progress(0)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('35fa5496-30c2-4666-84d0-218fefa4e7ac', True if number == -100 else False)
        self.report.start_uuid('3bd8f601-e5c1-45c4-a7ce-5bce38299731')
        page_edit.color.adjust.contrast.set_progress(1)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('3bd8f601-e5c1-45c4-a7ce-5bce38299731', True if number == 100 else False)
        self.report.start_uuid('e378c5c1-7131-42b2-ad7d-2d26bbe72a92')
        #Saturation
        page_edit.select_adjustment_from_bottom_edit_menu('Saturation')
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('e378c5c1-7131-42b2-ad7d-2d26bbe72a92', True if number == 100 else False)
        self.report.start_uuid('7cc32cf8-d2e7-41a4-8d54-a79dde6b35a0')
        page_edit.color.adjust.saturation.set_progress(0.7)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('7cc32cf8-d2e7-41a4-8d54-a79dde6b35a0', True if number > 100 else False)
        self.report.start_uuid('0f159765-14b8-4a19-ae01-df132ecf41d9')
        page_edit.color.adjust.saturation.set_progress(0.3)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('0f159765-14b8-4a19-ae01-df132ecf41d9', True if number < 100 else False)
        self.report.start_uuid('fbd555b1-57a7-43a5-a3b0-ca17d8ca41f4')
        page_edit.color.adjust.saturation.set_progress(0)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('fbd555b1-57a7-43a5-a3b0-ca17d8ca41f4', True if number == 0 else False)
        self.report.start_uuid('822f8f26-eab7-446d-af29-d7c65701e43c')
        page_edit.color.adjust.saturation.set_progress(1)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('822f8f26-eab7-446d-af29-d7c65701e43c', True if number == 200 else False)
        self.report.start_uuid('3be58560-ae77-40d9-b011-ff2d047f41dd')
        #Hue
        page_edit.select_adjustment_from_bottom_edit_menu('Hue')
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('3be58560-ae77-40d9-b011-ff2d047f41dd', True if number == 100 else False)
        self.report.start_uuid('c8ba369d-782a-40fc-ba3f-34f06f7299e7')
        page_edit.color.adjust.hue.set_progress(0.7)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('c8ba369d-782a-40fc-ba3f-34f06f7299e7', True if number > 100 else False)
        self.report.start_uuid('ab7dc707-ef82-45fb-928c-f95721b0f36d')
        page_edit.color.adjust.hue.set_progress(0.3)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('ab7dc707-ef82-45fb-928c-f95721b0f36d', True if number < 100 else False)
        self.report.start_uuid('95c831a3-e9c6-4544-95fc-db8175aad502')
        page_edit.color.adjust.hue.set_progress(0)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('95c831a3-e9c6-4544-95fc-db8175aad502', True if number == 0 else False)
        self.report.start_uuid('e06c1f1b-579e-40c0-9a30-11a115f220db')
        page_edit.color.adjust.hue.set_progress(1)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('e06c1f1b-579e-40c0-9a30-11a115f220db', True if number == 200 else False)
        self.report.start_uuid('10d8d88d-aeac-4214-a5a5-511ff25e6ae0')
        #white balance
        #page_edit.el(L.edit.color_sub.white_balance).click()
        #Color Temperature
        page_edit.select_adjustment_from_bottom_edit_menu('Temp')
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('10d8d88d-aeac-4214-a5a5-511ff25e6ae0', True if number == 50 else False)
        self.report.start_uuid('d5b5d9f5-3eef-42e2-bc06-a2a1abe8dee7')
        page_edit.color.white_balance.color_temperature.set_progress(0.7)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('d5b5d9f5-3eef-42e2-bc06-a2a1abe8dee7', True if number > 50 else False)
        self.report.start_uuid('ab862a41-58ad-44a2-8087-b264278abbec')
        page_edit.color.white_balance.color_temperature.set_progress(0.3)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('ab862a41-58ad-44a2-8087-b264278abbec', True if number < 50 else False)
        self.report.start_uuid('bc052e63-4c9f-4694-b4f0-638c8a3c11e3')
        page_edit.color.white_balance.color_temperature.set_progress(0)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('bc052e63-4c9f-4694-b4f0-638c8a3c11e3', True if number == 0 else False)
        self.report.start_uuid('62b5c254-4771-4b6a-9b48-8ef2027c460b')
        page_edit.color.white_balance.color_temperature.set_progress(1)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('62b5c254-4771-4b6a-9b48-8ef2027c460b', True if number == 100 else False)
        self.report.start_uuid('91d4fcee-d1fe-4bc6-93db-59a4d9236741')
        #Tint
        page_edit.select_adjustment_from_bottom_edit_menu('Tint')
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('91d4fcee-d1fe-4bc6-93db-59a4d9236741', True if number == 50 else False)
        self.report.start_uuid('b3aba4f2-aa2e-4328-9fe9-8a96a1ab9cb2')
        page_edit.color.white_balance.tint.set_progress(0.7)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('b3aba4f2-aa2e-4328-9fe9-8a96a1ab9cb2', True if number > 50 else False)
        self.report.start_uuid('01f76d4e-1bb2-4308-9330-69b6444f4d58')
        page_edit.color.white_balance.tint.set_progress(0.3)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('01f76d4e-1bb2-4308-9330-69b6444f4d58', True if number < 50 else False)
        self.report.start_uuid('e1275432-69eb-4980-87e7-9b4a6448bd7c')
        page_edit.color.white_balance.tint.set_progress(0)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('e1275432-69eb-4980-87e7-9b4a6448bd7c', True if number == 0 else False)
        self.report.start_uuid('0487a29e-b1db-4037-a4b9-49925706a128')
        page_edit.color.white_balance.tint.set_progress(1)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('0487a29e-b1db-4037-a4b9-49925706a128', True if number == 100 else False)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_02(self):
        self.report.start_uuid('6cb4e483-d200-4a12-9ae1-14abc04f6d28')
        media_list = ['png.png']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        # set default pan zoom [OFF]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        timeline_settings.SetPanZoom('OFF')
        time.sleep(1)
        page_edit.driver.driver.back()
        # =========================
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_date)
        #page_media.click(L.import_media.video_library.sort_menu.descending)
        #page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.driver.driver.back()
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.menu.fx).click()
        page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.select_from_bottom_edit_menu('Effect')
        #Beating
        page_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #>> frequency
        page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Frequency')
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
                                   pic_base, pic_after)
        self.report.new_result('6cb4e483-d200-4a12-9ae1-14abc04f6d28', True if (number == 20) and (not compare_result) else False)
        self.report.start_uuid('4260b495-a0f0-4ccb-81fc-d816bfd627c6')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_edit.select_effect_from_bottom_edit_menu('Frequency')
        page_edit.different_fx.beating_frequency.set_progress(0.7)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1.3)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('4260b495-a0f0-4ccb-81fc-d816bfd627c6', True if (number > 20) and (not compare_result) else False)
        self.report.start_uuid('fe5e2f0d-ee84-43b7-9bba-1a27df66d71e')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_edit.select_effect_from_bottom_edit_menu('Frequency')
        page_edit.different_fx.beating_frequency.set_progress(0.3)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()        
        time.sleep(1.3)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('fe5e2f0d-ee84-43b7-9bba-1a27df66d71e', True if (number < 20) and (not compare_result) else False)
        self.report.start_uuid('7cd0f6de-d928-4319-97f5-c2cb2e66ff7c')
        self.report.start_uuid('0a65b372-42de-4762-a678-d2f2b6951660')
        self.report.start_uuid('561c6461-f8c4-49dd-89a2-7347d4a0d65b')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_edit.select_effect_from_bottom_edit_menu('Frequency')
        page_edit.different_fx.beating_frequency.set_progress(0)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()       
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('7cd0f6de-d928-4319-97f5-c2cb2e66ff7c', True if (number == 5) and (not compare_result) else False)
        self.report.new_result('0a65b372-42de-4762-a678-d2f2b6951660', True if number == 5 else False)
        self.report.new_result('561c6461-f8c4-49dd-89a2-7347d4a0d65b', True if not compare_result else False)
        self.report.start_uuid('b3da4cba-cbe8-49c6-8d1f-5df90e7bef60')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_edit.select_effect_from_bottom_edit_menu('Frequency')
        page_edit.different_fx.beating_frequency.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()        
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('b3da4cba-cbe8-49c6-8d1f-5df90e7bef60', True if (number == 40) and (not compare_result) else False)
        self.report.start_uuid('ab490a99-98de-4070-9442-608fe225c520')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        # >> strength
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Strength')
        number = int(page_edit.different_fx.beating_strength.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()        
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('ab490a99-98de-4070-9442-608fe225c520', True if (number == 120) and (not compare_result) else False)
        self.report.start_uuid('094cff54-681b-43f6-9bdd-300857c70370')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #age_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_edit.select_effect_from_bottom_edit_menu('Strength')
        page_edit.different_fx.beating_strength.set_progress(0)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_strength.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()        
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('094cff54-681b-43f6-9bdd-300857c70370', True if (number == 110) and (not compare_result) else False)
        self.report.start_uuid('00a7f2e5-8f0c-467c-a7ae-c4c718ba985b')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_edit.select_effect_from_bottom_edit_menu('Strength')
        page_edit.different_fx.beating_strength.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_strength.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()        
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('00a7f2e5-8f0c-467c-a7ae-c4c718ba985b', True if (number == 150) and (not compare_result) else False)
        self.report.start_uuid('05fbc53e-aa2e-46ee-9942-3ac55343435d')
        #page_edit.driver.driver.back()
        #Bloom
        #page_media.select_media_by_text('Bloom')
        #page_media.el(L.import_media.library_gridview.add).click()
        page_edit.el(L.edit.menu.back_session).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.select_effect_from_bottom_edit_menu('Bloom')
        time.sleep(2)
        page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Sample Weight')
        time.sleep(2)
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #>> Sample Weight
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('05fbc53e-aa2e-46ee-9942-3ac55343435d', True if (number == 100) and compare_result else False)
        self.report.start_uuid('ea4aa246-1530-4d35-a9fc-9c1e9a0104f1')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        #page_edit.select_effect_from_bottom_edit_menu('Sample Weight')
        page_edit.different_fx.bloom_sample_weight.set_progress(0.7)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        self.report.new_result('ea4aa246-1530-4d35-a9fc-9c1e9a0104f1', True if number > 100 else False)
        self.report.start_uuid('ef7c6f67-9c99-4092-93e3-cbc71daa8a32')
        page_edit.different_fx.bloom_sample_weight.set_progress(0.3)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        self.report.new_result('ef7c6f67-9c99-4092-93e3-cbc71daa8a32', True if number < 100 else False)
        self.report.start_uuid('88eb60c0-199b-4009-aa12-b0a22b961669')
        page_edit.different_fx.bloom_sample_weight.set_progress(0)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('88eb60c0-199b-4009-aa12-b0a22b961669', True if (number == 0) and compare_result else False)
        self.report.start_uuid('524be4d9-98b2-4db8-903f-278778410326')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        #page_edit.select_effect_from_bottom_edit_menu('Sample Weight')
        page_edit.different_fx.bloom_sample_weight.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('524be4d9-98b2-4db8-903f-278778410326', True if (number == 200) and compare_result else False)
        self.report.start_uuid('f1061dea-2e58-4764-93dd-9c0b11a61066')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #>> Light Number
        #page_edit.select_from_bottom_edit_menu('Effect')
       # page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Light Number')
        number = int(page_edit.different_fx.bloom_light_number.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('f1061dea-2e58-4764-93dd-9c0b11a61066', True if (number == 2) and compare_result else False)
        self.report.start_uuid('756a3f0f-2f9e-4923-805b-76a0c9ea1ae3')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        #page_edit.select_effect_from_bottom_edit_menu('Light Number')
        page_edit.different_fx.bloom_light_number.set_progress(0)
        time.sleep(5)
        number = int(page_edit.different_fx.bloom_light_number.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('756a3f0f-2f9e-4923-805b-76a0c9ea1ae3', True if (number == 1) and compare_result else False)
        self.report.start_uuid('07fc3b8d-eac6-4f29-980f-683fd687ab85')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        #page_edit.select_effect_from_bottom_edit_menu('Light Number')
        page_edit.different_fx.bloom_light_number.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.bloom_light_number.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('07fc3b8d-eac6-4f29-980f-683fd687ab85', True if (number == 3) and compare_result else False)
        self.report.start_uuid('5d72248a-f7fd-4a3f-a1c6-0ad31155c63f')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #>> Angle
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Angle')
        number = int(page_edit.different_fx.bloom_angle.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('5d72248a-f7fd-4a3f-a1c6-0ad31155c63f', True if (number == 50) and compare_result else False)
        self.report.start_uuid('6ba7a9de-597a-4c79-abf8-699dcf9a0986')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        #page_edit.select_effect_from_bottom_edit_menu('Angle')
        page_edit.different_fx.bloom_angle.set_progress(0)
        time.sleep(5)
        number = int(page_edit.different_fx.bloom_angle.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('6ba7a9de-597a-4c79-abf8-699dcf9a0986', True if (number == 0) and compare_result else False)
        self.report.start_uuid('2d933688-36c3-4b35-8ca8-d016b17dd005')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        #page_edit.select_effect_from_bottom_edit_menu('Angle')
        page_edit.different_fx.bloom_angle.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.bloom_angle.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('2d933688-36c3-4b35-8ca8-d016b17dd005', True if (number == 200) and compare_result else False)
        self.report.start_uuid('1e96519a-d4e2-46e4-b954-f15bee0992cf')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.menu.fx).click()
        #Black and White
        #page_media.select_media_by_text('Black & White')
        #page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.el(L.edit.menu.back_session).click()
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        time.sleep(2)
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        page_edit.select_effect_from_bottom_edit_menu('Degree')
        time.sleep(2)
        #page_edit.el(L.edit.menu.edit).click()
        #>> Degree
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        #page_edit.driver.driver.back()
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('1e96519a-d4e2-46e4-b954-f15bee0992cf',
                               True if (number == 200) and compare_result else False)
        self.report.start_uuid('ef54fa97-ccf7-4f9e-a0cc-78ef011ba1d2')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Black & White')
        #page_edit.select_effect_from_bottom_edit_menu('Degree')
        page_edit.different_fx.black_and_white_degree.set_progress(0.7)
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        self.report.new_result('ef54fa97-ccf7-4f9e-a0cc-78ef011ba1d2', True if number > 100 else False)
        self.report.start_uuid('338277ce-767a-4948-b34b-88d0e66186a3')
        page_edit.different_fx.black_and_white_degree.set_progress(0.3)
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        self.report.new_result('338277ce-767a-4948-b34b-88d0e66186a3', True if number < 100 else False)
        self.report.start_uuid('b64a4b32-804d-45bf-a049-7e79d36e35fb')
        page_edit.different_fx.black_and_white_degree.set_progress(0)
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('b64a4b32-804d-45bf-a049-7e79d36e35fb',
                               True if (number == 0) and compare_result else False)
        self.report.start_uuid('5061f1b1-8161-4756-bc4a-30e77e678281')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Black & White')
        #page_edit.select_effect_from_bottom_edit_menu('Degree')
        page_edit.different_fx.black_and_white_degree.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('5061f1b1-8161-4756-bc4a-30e77e678281',
                               True if (number == 200) and compare_result else False)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_03(self):
        self.report.start_uuid('f35c33a1-962c-475e-9f7f-0e18eed3e262')
        media_list = ['mp4.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.swipe_element(L.edit.timeline.playhead, "left", 600)
        page_edit.click(L.edit.timeline.clip)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.sharpness).click()
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
        # Sharpness
        number = int(page_edit.sharpness_effect.sharpness.get_number())
        self.report.new_result('f35c33a1-962c-475e-9f7f-0e18eed3e262', True if number == 0 else False)
        self.report.start_uuid('2f335a6a-e6b2-488b-9d0d-45de1be19d36')
        pic_base = page_edit.get_preview_pic()
        page_edit.sharpness_effect.sharpness.set_progress(0.9)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('2f335a6a-e6b2-488b-9d0d-45de1be19d36', True if not compare_result else False)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_04(self):
        self.report.start_uuid('7eb3f4d4-b6a0-464c-a046-3859f69557b5')
        self.report.start_uuid('2fd0c8b8-59d5-4986-ad84-405637852a86')
        media_list = ['png.png', 'jpg.jpg']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        # set default pan zoom [ON]
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        timeline_settings.SetPanZoom('ON')
        time.sleep(1)
        page_edit.driver.driver.back()
        # =========================
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_date)
        #page_media.click(L.import_media.video_library.sort_menu.descending)
        #page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        # [Photo_Apply to All] Pan_Zoom - Random Motion
        is_default_random_motion = page_edit.check_bottom_edit_menu_select_status('Random')
        # is_default_random_motion = True if page_edit.el(L.edit.pan_zoom_effect.random_motion).get_attribute(
        #                            'checked') == 'true' else False
        self.report.new_result('7eb3f4d4-b6a0-464c-a046-3859f69557b5', is_default_random_motion)
        self.report.new_result('2fd0c8b8-59d5-4986-ad84-405637852a86', is_default_random_motion)
        self.report.start_uuid('d49362dd-6d87-4c27-8d5f-785749caeef2')
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead,"right",700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('d49362dd-6d87-4c27-8d5f-785749caeef2',
                               True if compare_result_1 and compare_result_2 else False)
        # [Photo_Apply to All] Pan_Zoom - No Effect
        self.report.start_uuid('6adefecd-8cbd-4164-aa84-9dd4bd06577e')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('No Effect')
        # page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        #page_edit.swipe_element(L.edit.timeline.playhead, "right", 500)
        time.sleep(1)
        #page_edit.swipe_element(L.edit.timeline.playhead, "right", 500)
        time.sleep(1)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('6adefecd-8cbd-4164-aa84-9dd4bd06577e',
                               True if compare_result_1 and compare_result_2 else False, 'DRA197258-0001')
        # [Photo_Apply to All] Pan_Zoom - Custom Motion
        self.report.start_uuid('4411db3a-3fdc-461c-930f-793ab72b45a2')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('Custom')
        # page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        time.sleep(2)
        page_edit.el(L.edit.pan_zoom_effect.reset).click()
        time.sleep(1)
        page_edit.pan_zoom.set_custom_motion()
        page_edit.el(L.edit.pan_zoom_effect.back).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        #page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('4411db3a-3fdc-461c-930f-793ab72b45a2',
                               True if compare_result_1 and compare_result_2 else False)
        #[Photo_Apply OK] Random Motion
        self.report.start_uuid('adc2ccca-482d-4eb7-ac83-5bf5d4de19b7')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('No Effect')
        # page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        # page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('Random')
        # page_edit.el(L.edit.pan_zoom_effect.random_motion).click()
        # page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('adc2ccca-482d-4eb7-ac83-5bf5d4de19b7',
                               True if compare_result_1 and compare_result_2 else False)
        # [Photo_Apply OK] No Effect
        self.report.start_uuid('80556c5f-b177-455d-bade-d46c0fa34195')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('No Effect')
        # page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        # page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('80556c5f-b177-455d-bade-d46c0fa34195',
                               True if compare_result_1 and compare_result_2 else False, 'DRA197258-0001')
        # [Photo_Apply OK] Custom Motion
        self.report.start_uuid('1b938b47-d9e3-43db-bc7f-93deba4de02f')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('Custom')
        # page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        time.sleep(2)
        page_edit.el(L.edit.pan_zoom_effect.reset).click()
        time.sleep(1)
        page_edit.pan_zoom.set_custom_motion()
        page_edit.el(L.edit.pan_zoom_effect.back).click()
        # page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('1b938b47-d9e3-43db-bc7f-93deba4de02f',
                               True if compare_result_1 and compare_result_2 else False)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_05(self):
        media_list = ['mp4.mp4', '01_static.mp4', '02_static.mp4']
        self.report.start_uuid('3f81b17b-7ec0-463a-9423-acd1c8fad3ea')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_setting = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        # preview full screen
        time.sleep(2)
        page_edit.enter_fullscreen_preview()
        time.sleep(1)
        if page_edit.is_not_exist(L.edit.preview.fullscreen_current_position):
            page_edit.el(L.edit.preview.movie_view).click()
        self.report.new_result('3f81b17b-7ec0-463a-9423-acd1c8fad3ea',
                               page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        time.sleep(2)
        self.report.start_uuid('5bd41804-74f8-4e9b-bff4-246537c0af45')
        self.report.new_result('5bd41804-74f8-4e9b-bff4-246537c0af45',
                               page_edit.is_exist(L.edit.preview.water_mark))
        self.report.start_uuid('5a6815e0-1ac5-48b2-a582-567ebace8f71')
        self.report.start_uuid('88b811ec-fcb6-45f3-9480-27a7a68b9cdc')
        page_edit.driver.driver.back()
        time.sleep(2)
        #remove exists mp4
        page_edit.timeline_select_media(media_list[0], 'Video')
        page_edit.el(L.edit.menu.delete).click()
        #add 2 static video to timeline
        page_edit.el(L.edit.menu.import_media).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_name)
        #page_media.click(L.import_media.video_library.sort_menu.ascending)
        #page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[1])        
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_media.select_media_by_text(media_list[2])
        #page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_media(media_list[1], 'Video')
        time.sleep(2)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu('left')
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        is_disabled_random_motion = page_edit.check_bottom_edit_menu_select_status('No Effect')
        # is_disabled_random_motion = True if page_edit.el(L.edit.pan_zoom_effect.random_motion).get_attribute(
        #     'enabled') == 'false' else False
        self.report.new_result('5a6815e0-1ac5-48b2-a582-567ebace8f71', is_disabled_random_motion)
        self.report.new_result('88b811ec-fcb6-45f3-9480-27a7a68b9cdc', is_disabled_random_motion)
        #[Video_Apply to All] No Effect
        self.report.start_uuid('4a4ad790-5b78-4831-a156-315877f42bb8')
        # page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.select_from_bottom_edit_menu('No Effect')
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[2], 'Video')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('4a4ad790-5b78-4831-a156-315877f42bb8',
                               True if compare_result_1 and compare_result_2 else False)
        # [Video_Apply to All] Custom Motion
        self.report.start_uuid('415d116b-389c-44f0-bd08-d3ea14ea04de')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[1], 'Video')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('Custom')
        # page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        time.sleep(2)
        page_edit.el(L.edit.pan_zoom_effect.reset).click()
        time.sleep(1)
        page_edit.pan_zoom.set_custom_motion()
        page_edit.el(L.edit.pan_zoom_effect.back).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[2], 'Video')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('415d116b-389c-44f0-bd08-d3ea14ea04de',
                               True if compare_result_1 and compare_result_2 else False)
        # [Video_Apply OK] No Effect
        self.report.start_uuid('60936593-4d5b-4117-9626-a262d693e59e')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[1], 'Video')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('No Effect')
        # page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        # page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[2], 'Video')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('60936593-4d5b-4117-9626-a262d693e59e',
                               True if compare_result_1 and compare_result_2 else False)
        # [Video_Apply OK] Custom Motion - reset to no effect first
        self.report.start_uuid('822282fc-0374-4534-90d5-902de4e2de66')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[1], 'Video')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('No Effect')
        # page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        # page_edit.swipe_bottom_edit_menu()
        # page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.select_from_bottom_edit_menu('Custom')
        # page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        time.sleep(2)
        page_edit.el(L.edit.pan_zoom_effect.reset).click()
        time.sleep(1)
        page_edit.pan_zoom.set_custom_motion()
        page_edit.el(L.edit.pan_zoom_effect.back).click()
        # page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[2], 'Video')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('822282fc-0374-4534-90d5-902de4e2de66',
                               True if compare_result_1 and compare_result_2 else False)

        #set default duration of transition
        self.report.start_uuid('720154f9-f1e7-4e07-b01a-1b0fe8bcd216')
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_edit.settings.swipe_to_option('Information')
        timeline_setting.enter_advanced_page()
        default_value = page_edit.el(L.timeline_settings.settings.default_transition_duration_value).text
        default_transition_duration = default_value.replace('  Second(s)', '').strip()
        self.report.new_result('720154f9-f1e7-4e07-b01a-1b0fe8bcd216',
                               True if default_value == '2.0  Second(s)' else False)
        self.report.start_uuid('af2a4980-71b7-4181-a105-e978b380bb99')
        page_edit.driver.driver.back()
        time.sleep(2)
        timeline_setting.set_default_transition_duration(0.1)
        time.sleep(2)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        #page_media.select_media_by_text('Binary 1')
        page_edit.select_transition_from_bottom_menu('Blur')
        #page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        # page_media.el(L.edit.transition.btn_show_transition_duration).click()
        default_value = page_edit.el(L.edit.transition.duration_text).text
        self.report.new_result('af2a4980-71b7-4181-a105-e978b380bb99',
                               True if default_value == '0.1' else False)
        self.report.start_uuid('343072ee-7556-45fe-bc52-2a8889eed30c')
        # page_media.el(L.edit.transition.ok).click()
        time.sleep(1)
        page_edit.driver.driver.back()
        #set default duration as 4.0
        time.sleep(2)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_edit.settings.swipe_to_option('Information')
        time.sleep(2)
        timeline_setting.set_default_transition_duration(4.0)
        time.sleep(2)
        for retry in range(5):
            page_edit.back()
            if page_edit.is_exist(L.edit.menu.import_media):
                logger('Found import button, stop tapping back.')
                break
        page_edit.el(L.edit.menu.import_media).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(2)
        page_edit.select_transition_from_bottom_menu('Fade')
        time.sleep(2)
        result_second = True if page_edit.el(L.edit.transition.duration_text).text == '4.0' else False
        page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        page_edit.select_transition_from_bottom_menu('Blur')
        time.sleep(2)
        result_first = True if page_edit.el(L.edit.transition.duration_text).text == '0.1' else False
        self.report.new_result('343072ee-7556-45fe-bc52-2a8889eed30c',
                               True if result_first and result_second else False)
        #adjust transition duration - apply all [OFF]
        self.report.start_uuid('d4a10596-a73a-4395-91b4-74a6e72dee7a')
        time.sleep(1)
        # page_edit.transition.set_duration(3.0)
        page_edit.opacity_set_slider(0.5)
        # time.sleep(2)
        # page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        # page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_second = True if page_edit.el(L.edit.transition.duration_text).text == '2.0' else False
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(2)
        time.sleep(2)
        # page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_first = True if page_edit.el(L.edit.transition.duration_text).text == '4.0' else False
        self.report.new_result('d4a10596-a73a-4395-91b4-74a6e72dee7a',
                               True if result_first and result_second else False)
        # adjust transition duration - apply all [ON]
        self.report.start_uuid('49437a84-cd81-4f47-8b2a-51e1b0ff0e73')
        time.sleep(1)
        page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        # page_edit.el(L.edit.transition.btn_show_transition_duration).click()
        # time.sleep(2)
        # page_edit.transition.set_duration(3.0, 1)
        page_edit.opacity_set_slider(0.5)
        page_edit.click(L.edit.menu.btn_apply_all)
        time.sleep(2)
        page_edit.timeline_select_transition_effect(2)
        time.sleep(2)
        # page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_second = True if page_edit.el(L.edit.transition.duration_text).text == '2.0' else False
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        time.sleep(1)
        # page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_first = True if page_edit.el(L.edit.transition.duration_text).text == '2.0' else False
        self.report.new_result('49437a84-cd81-4f47-8b2a-51e1b0ff0e73',
                               True if result_first and result_second else False)
        #reset duration
        #self.report.start_uuid('1a3be899-15fd-4058-bc84-7e3a26dd7cad')
        time.sleep(1)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        timeline_setting.set_default_transition_duration(default_transition_duration)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_06(self):
        media_list = ['mp4.mp4', '01_static.mp4', '02_static.mp4']
        self.report.start_uuid('31974a6e-b202-4b5e-b343-673a1abb8066')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_setting = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        # remove exists mp4
        page_edit.timeline_select_media(media_list[0], 'Video')
        page_edit.el(L.edit.menu.delete).click()
        # add 2 static video to timeline
        page_edit.el(L.edit.menu.import_media).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_name)
        #page_media.click(L.import_media.video_library.sort_menu.ascending)
        #page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_media.select_media_by_text(media_list[2])
        #page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_date)
        #page_media.click(L.import_media.video_library.sort_menu.descending)
        #page_media.driver.driver.back()
        page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        self.report.new_result('31974a6e-b202-4b5e-b343-673a1abb8066',
                               page_edit.check_transition_exists_in_list('Blur'))
        self.report.start_uuid('5aec562c-3df2-43a7-8099-2f0944997568')
        
        amount = page_edit.calculate_transition_amount() #6
        '''
        page_edit.select_transition_category('Rotation')
        amount += page_edit.calculate_transition_amount() #12
        page_edit.select_transition_category('3D')
        amount += page_edit.calculate_transition_amount() #12
        page_edit.select_transition_category('Slideshow')
        amount += page_edit.calculate_transition_amount() #15        
        page_edit.select_transition_category('Geometric')
        amount += page_edit.calculate_transition_amount() #36
        page_edit.select_transition_category('Plain Shape')
        amount += page_edit.calculate_transition_amount() #6
        page_edit.select_transition_category('Linear')
        amount += page_edit.calculate_transition_amount() #10        
        page_edit.select_transition_category('Distortion')
        amount += page_edit.calculate_transition_amount() #10
        page_edit.select_transition_category('Dissolve')
        amount += page_edit.calculate_transition_amount() #7     
        page_edit.select_transition_category('Ripple')
        amount += page_edit.calculate_transition_amount() #6
        page_edit.select_transition_category('Glitch')
        amount += page_edit.calculate_transition_amount() #8
        page_edit.select_transition_category('LifeStyle')
        amount += page_edit.calculate_transition_amount() #15
        '''

        self.report.new_result('5aec562c-3df2-43a7-8099-2f0944997568', True if amount >= 143 else False, f'amount={amount}')
        self.report.start_uuid('404da069-4c4b-4198-a492-745ebeb9dbc9')
        time.sleep(1)
        page_edit.select_transition_from_bottom_menu('X-Ray')
        time.sleep(3)
        page_edit.timeline_select_transition_effect(1)
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_media.el(L.edit.menu.play).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('404da069-4c4b-4198-a492-745ebeb9dbc9',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Transtition will auto apply on new UI (7.3.0+)

        #self.report.start_uuid('44a68076-a6b5-4e57-9fbe-27051750eae8')
        #time.sleep(1)
        #page_edit.driver.driver.back()
        #time.sleep(2)
        #page_edit.timeline_select_transition_effect(1)
        #elm = page_edit.timeline_get_transition_effect(1)
        #time.sleep(1)
        #pic_base = page_edit.driver.save_pic(elm)
        #page_media.select_media_by_text('X-Ray')
        #time.sleep(3)
        #page_media.el(L.import_media.library_gridview.add).click()
        #time.sleep(1)
        #pic_after = page_edit.driver.save_pic(elm)
        #self.report.new_result('44a68076-a6b5-4e57-9fbe-27051750eae8',
        #                       (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
        #                                                                           5).compare_image() else False)(
        #                           pic_base, pic_after))

        # leave and save project
        self.report.start_uuid('1a3be899-15fd-4058-bc84-7e3a26dd7cad')
        # time.sleep(1)
        # page_edit.driver.driver.back()
        # time.sleep(1)
        # elm = page_edit.timeline_get_transition_effect(1)
        # pic_base = page_edit.driver.save_pic(elm)
        # time.sleep(1)
        # page_edit.driver.driver.back()
        # time.sleep(1)
        # page_edit.driver.driver.back()
        # time.sleep(1)
        # page_main.select_existed_project_by_title(project_title)
        # #time.sleep(1)
        # # page_main.el(L.main.project_info.btn_edit_project).click()
        # time.sleep(10)
        # elm = page_edit.timeline_get_transition_effect(1)
        # time.sleep(1)
        # page_edit.swipe_element(L.edit.timeline.playhead, "right", 500)
        # time.sleep(1)
        # page_edit.timeline_select_transition_effect(1)
        # time.sleep(1)
        # pic_after = page_edit.driver.save_pic(elm)
        page_main.relaunch_app(pdr_package)
        result = page_main.select_existed_project_by_title(project_title)
        self.report.new_result('1a3be899-15fd-4058-bc84-7e3a26dd7cad', result)
                               # (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                               #                                                 3).compare_image() else False)(
                               #     pic_base, pic_after))

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_07(self):
        media_list = ['01_static.mp4']
        self.report.start_uuid('6fbc941d-12c6-40ef-b1cd-000b035ee8b1')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(1)
        page_edit.settings.swipe_to_option('FAQ & Send Feedback')
        self.report.new_result('6fbc941d-12c6-40ef-b1cd-000b035ee8b1', True)
        self.report.start_uuid('225633cb-308a-4aaa-9ff6-fc1582084b5b')
        page_edit.el(L.edit.settings.send_feedback_btn).click()
        time.sleep(5)
        page_edit.el(L.edit.settings.send_feedback.send_feedback_btn).click()
        time.sleep(3)
        # page_edit.back()
        time.sleep(3)
        page_edit.el(L.edit.settings.send_feedback.feedback_text).set_text('for testing')
        time.sleep(3)
        page_edit.driver.driver.back()
        if page_edit.is_exist(L.edit.settings.send_feedback.confirm_no_btn, 3):
            page_edit.el(L.edit.settings.send_feedback.confirm_no_btn).click()
            time.sleep(1)
        page_edit.el(L.edit.settings.send_feedback.feedback_email).set_text('abc@gmail.com')
        time.sleep(3)
        page_edit.driver.driver.back()
        if page_edit.is_exist(L.edit.settings.send_feedback.confirm_no_btn, 3):
            page_edit.el(L.edit.settings.send_feedback.confirm_no_btn).click()
            time.sleep(1)
        page_edit.el(L.edit.settings.send_feedback.top_right_btn).click()
        # verify device model & os version
        page_edit.swipe_element(L.edit.settings.send_feedback.feedback_preview_view, "up", 300)
        device_model = page_edit.el(L.edit.settings.send_feedback.feedback_device_model_text).text
        os_version = page_edit.el(L.edit.settings.send_feedback.feedback_os_version_text).text
        result_device_model = True if device_model in page_edit.settings.get_device_model() else False
        result_os_version = True if os_version in page_edit.settings.get_os_version() else False
        self.report.new_result('225633cb-308a-4aaa-9ff6-fc1582084b5b',
                               True if result_device_model and result_os_version else False)


    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_02_08(self):
        media_list = ['01_static.mp4', 'jpg.jpg']
        self.report.start_uuid('77ed7370-d1b1-4c36-8159-02eaee850020')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        time.sleep(2)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(2)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        # pip video effect
        page_edit.select_from_bottom_edit_menu('Effect')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_effect_from_bottom_edit_menu('Bloom')
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('77ed7370-d1b1-4c36-8159-02eaee850020',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('071e7446-914c-4fce-ac7f-e6628bfc5408')                           
        page_edit.select_effect_from_bottom_edit_menu('Bloom')                           
        page_edit.select_effect_from_bottom_edit_menu('Sample Weight')
        pic_base = pic_after
        time.sleep(2)
        page_edit.different_fx.bloom_sample_weight.set_progress(1)
        pic_after = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.delete).click()
        self.report.new_result('071e7446-914c-4fce-ac7f-e6628bfc5408',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        
        
        # pip photo effect
        self.report.start_uuid('1e3925fc-6203-458a-9932-b07ead0fa797') 
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        time.sleep(2)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[1])
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Effect')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1e3925fc-6203-458a-9932-b07ead0fa797',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('114a8820-25cb-45a4-9208-735db7a3690e')                           
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        page_edit.select_effect_from_bottom_edit_menu('Degree')
        pic_base = pic_after
        time.sleep(1)
        #page_edit.different_fx.beating_frequency.set_progress(1)
        page_edit.different_fx.black_and_white_degree.set_progress(0.5)
        pic_after = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.delete).click()
        self.report.new_result('114a8820-25cb-45a4-9208-735db7a3690e',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))        
        
        # pip colot board effect
        self.report.start_uuid('5bc0675a-4b90-431c-98b1-37f79bb27f2a') 
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        time.sleep(2)
        page_media.select_media_by_text('Color Board')
        time.sleep(2)
        page_media.select_media_by_order(5)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Effect')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('5bc0675a-4b90-431c-98b1-37f79bb27f2a',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('4df5c28e-3226-4f2b-8ac7-e1d3193bb76b')                           
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        page_edit.select_effect_from_bottom_edit_menu('Degree')
        pic_base = pic_after
        time.sleep(2)
        page_edit.different_fx.black_and_white_degree.set_progress(0.3)
        pic_after = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.delete).click()
        self.report.new_result('4df5c28e-3226-4f2b-8ac7-e1d3193bb76b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))        
        
        
        # pip stcker effect
        self.report.start_uuid('a0c6ea80-8f40-48ce-a82e-5e21813b6aa6') 
        page_edit.el(L.edit.menu.effect).click()
        # page_edit.el(L.edit.effect_sub.sticker).click()
        # time.sleep(2)
        # page_edit.el(L.edit.effect_sub.sticker_tabs.tab_downloaded).click()
        page_media.switch_to_sticker_library()
        time.sleep(5)
        page_media.select_template_category('Social Media')
        time.sleep(10)
        page_media.select_sticker_by_order(1)
        # page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(10)
        # page_media.el(L.import_media.library_gridview.add_sticker).click()
        time.sleep(2)
        # page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Effect')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_effect_from_bottom_edit_menu('Chinese Painting')
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('a0c6ea80-8f40-48ce-a82e-5e21813b6aa6',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('0a20ef94-bb4d-4ff9-8cf6-12f2b5b03a57')                           
        page_edit.select_effect_from_bottom_edit_menu('Chinese Painting')
        page_edit.select_effect_from_bottom_edit_menu('Detail')
        pic_base = pic_after
        time.sleep(2)
        page_edit.different_fx.black_and_white_degree.set_progress(1)
        pic_after = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.delete).click()
        self.report.new_result('0a20ef94-bb4d-4ff9-8cf6-12f2b5b03a57',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        
        
        
        
        
        
        
