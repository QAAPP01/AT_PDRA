import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
from ATFramework.utils.compare_Mac import CompareImage
import pytest
import time

from pages.locator import locator as L

from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME



class Test_SFT_Scenario_03_02:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver sessioin>============')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        logger(f"desired_caps={desired_caps}")
        self.report = report
        self.device_udid = DRIVER_DESIRED_CAPS['udid']
        # ---- local mode > end ----
        self.test_material_folder = TEST_MATERIAL_FOLDER
        self.test_material_folder_01 = TEST_MATERIAL_FOLDER_01
                                                              
        # retry 3 time if craete driver fail
        retry = 3
        while retry:
            try:
                self.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',desired_caps)
                if self.driver:
                    logger("driver created!")
                    break
                else:
                    raise Exception("create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
                
        self.report.set_driver(self.driver)
        self.driver.start_app(pdr_package)
        self.driver.implicit_wait(15)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_02_01(self):
        media_list = ['slow_motion.mp4', 'png.png']
        self.report.start_uuid('08eb3bf4-68b3-48db-80ba-c88726155ad9')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result('08eb3bf4-68b3-48db-80ba-c88726155ad9', page_edit.check_preview_aspect_ratio(project_title))

        #add media video & photo
        self.report.start_uuid('33cffa6e-fa85-4bb6-a223-e6282f680373')
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_video_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        #color preset - video
        page_edit.timeline_select_media(media_list[0], 'Video')
        #page_edit.timeline_select_item_by_index_on_track(1, 2)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_3).click()
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_8).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        result_compare = CompareImage(pic_base, pic_after, 9).compare_image()
        self.report.new_result('33cffa6e-fa85-4bb6-a223-e6282f680373', True if (not result_compare) or (result_compare == 100) else False)
        self.report.start_uuid('bd7c0300-90ba-4534-be32-98f2cb7e38b0')
        pic_base = pic_after
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        page_edit.el(L.edit.menu.play).click()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('bd7c0300-90ba-4534-be32-98f2cb7e38b0',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   9).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('be2abc3e-ee61-4c19-b608-0c561c740f01')
        page_edit.el(L.edit.menu.delete).click()
        #color preset - photo
        pic_base = pic_after
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_media(media_list[1], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_3).click()
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_8).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = CompareImage(pic_base, pic_after, 9).compare_image()
        self.report.new_result('be2abc3e-ee61-4c19-b608-0c561c740f01',
                               True if not compare_result or compare_result == 100 else False)
        self.report.start_uuid('47e78f7b-1ead-4ef5-828c-95567d353a76')
        pic_base = pic_after
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = CompareImage(pic_base, pic_after, 9).compare_image()
        self.report.new_result('47e78f7b-1ead-4ef5-828c-95567d353a76',
                               True if not compare_result else False)
        # Brightness
        self.report.start_uuid('f74bb261-bd46-466a-97e7-448466d99102')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        #page_edit.el(L.edit.color_sub.adjust).click()
        page_edit.timeline_select_media(media_list[1], 'Photo')
        page_edit.driver.driver.back()
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('f74bb261-bd46-466a-97e7-448466d99102', True if number == 0 else False)
        self.report.start_uuid('b7e40b93-1eb0-4253-a55a-47420d49d8cc')
        page_edit.color.adjust.brightness.set_progress(0.7)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('b7e40b93-1eb0-4253-a55a-47420d49d8cc', True if number > 0 else False)
        self.report.start_uuid('4f467952-39c1-448a-ac58-0c597d01dfe5')
        page_edit.color.adjust.brightness.set_progress(0.3)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('4f467952-39c1-448a-ac58-0c597d01dfe5', True if number < 0 else False)
        self.report.start_uuid('f9cb6977-f25a-482a-9114-b6f29684d5f0')
        page_edit.color.adjust.brightness.set_progress(0)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('f9cb6977-f25a-482a-9114-b6f29684d5f0', True if number == -100 else False)
        self.report.start_uuid('c5dc5592-dcab-4084-8990-17b6b4c9b95a')
        page_edit.color.adjust.brightness.set_progress(1)
        number = int(page_edit.color.adjust.brightness.get_number())
        self.report.new_result('c5dc5592-dcab-4084-8990-17b6b4c9b95a', True if number == 100 else False)
        self.report.start_uuid('7e9e6661-a160-4e53-b0fd-d2b036a2da3d')
        #Contract
        page_edit.select_adjustment_from_bottom_edit_menu('Contrast')
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('7e9e6661-a160-4e53-b0fd-d2b036a2da3d', True if number == 0 else False)
        self.report.start_uuid('c5ea6d27-71b3-4c27-8085-843f26a6758b')
        page_edit.color.adjust.contrast.set_progress(0.7)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('c5ea6d27-71b3-4c27-8085-843f26a6758b', True if number > 0 else False)
        self.report.start_uuid('db5bd87a-403f-44dc-8e82-d55285133561')
        page_edit.color.adjust.contrast.set_progress(0.3)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('db5bd87a-403f-44dc-8e82-d55285133561', True if number < 0 else False)
        self.report.start_uuid('cbe33481-b363-4a21-844b-f2fa360377e1')
        page_edit.color.adjust.contrast.set_progress(0)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('cbe33481-b363-4a21-844b-f2fa360377e1', True if number == -100 else False)
        self.report.start_uuid('91ddc513-cde0-47b9-ac65-e347b5805c02')
        page_edit.color.adjust.contrast.set_progress(1)
        number = int(page_edit.color.adjust.contrast.get_number())
        self.report.new_result('91ddc513-cde0-47b9-ac65-e347b5805c02', True if number == 100 else False)
        self.report.start_uuid('75b3d9f6-de08-42c2-8221-b28882f3a870')
        #Saturation
        page_edit.select_adjustment_from_bottom_edit_menu('Saturation')
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('75b3d9f6-de08-42c2-8221-b28882f3a870', True if number == 100 else False)
        self.report.start_uuid('875aba14-a700-4db4-8728-9cceb1aec34a')
        page_edit.color.adjust.saturation.set_progress(0.7)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('875aba14-a700-4db4-8728-9cceb1aec34a', True if number > 100 else False)
        self.report.start_uuid('f34f7d9c-6e38-4dd3-9048-03e361c767e3')
        page_edit.color.adjust.saturation.set_progress(0.3)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('f34f7d9c-6e38-4dd3-9048-03e361c767e3', True if number < 100 else False)
        self.report.start_uuid('3a554e35-e483-4887-908c-c219a45ccb0e')
        page_edit.color.adjust.saturation.set_progress(0)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('3a554e35-e483-4887-908c-c219a45ccb0e', True if number == 0 else False)
        self.report.start_uuid('a76bc3e3-028d-4b6c-ab38-feecdd4dafd9')
        page_edit.color.adjust.saturation.set_progress(1)
        number = int(page_edit.color.adjust.saturation.get_number())
        self.report.new_result('a76bc3e3-028d-4b6c-ab38-feecdd4dafd9', True if number == 200 else False)
        self.report.start_uuid('adf451bc-4238-47fe-94bc-4b8b33d2dbac')
        #Hue
        page_edit.select_adjustment_from_bottom_edit_menu('Hue')
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('adf451bc-4238-47fe-94bc-4b8b33d2dbac', True if number == 100 else False)
        self.report.start_uuid('6c8cf81c-8f04-4a96-aad7-9cfb8e467d9c')
        page_edit.color.adjust.hue.set_progress(0.7)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('6c8cf81c-8f04-4a96-aad7-9cfb8e467d9c', True if number > 100 else False)
        self.report.start_uuid('be378585-6760-4163-a9db-9b083412b798')
        page_edit.color.adjust.hue.set_progress(0.3)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('be378585-6760-4163-a9db-9b083412b798', True if number < 100 else False)
        self.report.start_uuid('540ba700-6be7-4298-8ed2-7b13a15d5f43')
        page_edit.color.adjust.hue.set_progress(0)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('540ba700-6be7-4298-8ed2-7b13a15d5f43', True if number == 0 else False)
        self.report.start_uuid('c8e0fc9d-c8d8-426b-803a-99bba1266a2c')
        page_edit.color.adjust.hue.set_progress(1)
        number = int(page_edit.color.adjust.hue.get_number())
        self.report.new_result('c8e0fc9d-c8d8-426b-803a-99bba1266a2c', True if number == 200 else False)
        self.report.start_uuid('7e3aef0f-b546-4948-b230-93df1009fa32')
        #white balance
        #page_edit.el(L.edit.color_sub.white_balance).click()
        #Color Temperature
        page_edit.select_adjustment_from_bottom_edit_menu('Temp')
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('7e3aef0f-b546-4948-b230-93df1009fa32', True if number == 50 else False)
        self.report.start_uuid('933887d9-19c4-4deb-be5f-9d69052ba810')
        page_edit.color.white_balance.color_temperature.set_progress(0.7)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('933887d9-19c4-4deb-be5f-9d69052ba810', True if number > 50 else False)
        self.report.start_uuid('f1312ee4-fb2b-4d71-b5e3-5154c5d8080a')
        page_edit.color.white_balance.color_temperature.set_progress(0.3)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('f1312ee4-fb2b-4d71-b5e3-5154c5d8080a', True if number < 50 else False)
        self.report.start_uuid('86e98aa9-59d9-478a-9550-b61eca1f4d34')
        page_edit.color.white_balance.color_temperature.set_progress(0)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('86e98aa9-59d9-478a-9550-b61eca1f4d34', True if number == 0 else False)
        self.report.start_uuid('11003d74-b6f4-4846-80b5-d0bb44c76892')
        page_edit.color.white_balance.color_temperature.set_progress(1)
        number = int(page_edit.color.white_balance.color_temperature.get_number())
        self.report.new_result('11003d74-b6f4-4846-80b5-d0bb44c76892', True if number == 100 else False)
        self.report.start_uuid('f04dd285-88be-4921-9be6-b6e91d289181')
        #Tint
        page_edit.select_adjustment_from_bottom_edit_menu('Tint')
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('f04dd285-88be-4921-9be6-b6e91d289181', True if number == 50 else False)
        self.report.start_uuid('dd694332-57ac-4444-a2ab-4a994010295c')
        page_edit.color.white_balance.tint.set_progress(0.7)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('dd694332-57ac-4444-a2ab-4a994010295c', True if number > 50 else False)
        self.report.start_uuid('319511a3-3093-4b99-88d1-51fd9a2c58e0')
        page_edit.color.white_balance.tint.set_progress(0.3)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('319511a3-3093-4b99-88d1-51fd9a2c58e0', True if number < 50 else False)
        self.report.start_uuid('2b67bb49-ba18-41aa-a331-98951066b604')
        page_edit.color.white_balance.tint.set_progress(0)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('2b67bb49-ba18-41aa-a331-98951066b604', True if number == 0 else False)
        self.report.start_uuid('ec05d5f5-db42-4738-85d7-bf47fe61707a')
        page_edit.color.white_balance.tint.set_progress(1)
        number = int(page_edit.color.white_balance.tint.get_number())
        self.report.new_result('ec05d5f5-db42-4738-85d7-bf47fe61707a', True if number == 100 else False)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_02_02(self):
        media_list = ['png.png']
        self.report.start_uuid('95a95e27-b582-4bdb-b969-ddab5b13ea0f')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
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
        #page_media.click(L.import_media.photo_library.sort)
        #page_media.click(L.import_media.photo_library.sort_menu.by_date)
        #page_media.click(L.import_media.photo_library.sort_menu.descending)
        #page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.driver.driver.back()
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.menu.fx).click()
        page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.select_from_bottom_edit_menu('Effect')
        # Beating
        page_edit.select_effect_from_bottom_edit_menu('Beating')
        #page_media.select_media_by_text('Beating')
        #page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        # >> frequency
        page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Frequency')
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)       
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('95a95e27-b582-4bdb-b969-ddab5b13ea0f',
                               True if (number == 20) and (not compare_result) else False)
        self.report.start_uuid('2ee26105-a766-4aeb-a605-0c0f24bb8ec6')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Frequency')
        page_edit.different_fx.beating_frequency.set_progress(0.7)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        self.report.new_result('2ee26105-a766-4aeb-a605-0c0f24bb8ec6', True if number > 20 else False)
        self.report.start_uuid('ebc36acc-bc60-46b1-ada2-d959ddee6714')
        page_edit.different_fx.beating_frequency.set_progress(0.3)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        self.report.new_result('ebc36acc-bc60-46b1-ada2-d959ddee6714', True if number < 20 else False)
        self.report.start_uuid('3eedd2e2-8817-49d1-8606-abccdaaf0db1')
        self.report.start_uuid('fc9e77af-dac5-4e7d-b18c-8cbfd64d593a')
        self.report.start_uuid('d20cd754-fd9e-4e64-a759-cca6f8fecbb6')
        page_edit.different_fx.beating_frequency.set_progress(0)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)        
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1.3)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('3eedd2e2-8817-49d1-8606-abccdaaf0db1',
                               True if (number == 5) and (not compare_result) else False)
        self.report.new_result('fc9e77af-dac5-4e7d-b18c-8cbfd64d593a', True if number == 5 else False)
        self.report.new_result('d20cd754-fd9e-4e64-a759-cca6f8fecbb6', True if not compare_result else False)
        self.report.start_uuid('554bd150-5286-4ca8-a794-6a8c0548a44c')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Frequency')
        page_edit.different_fx.beating_frequency.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_frequency.get_number())
        #page_edit.driver.driver.back()
        time.sleep(2)          
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1.3)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('554bd150-5286-4ca8-a794-6a8c0548a44c',
                               True if (number == 40) and (not compare_result) else False)
        self.report.start_uuid('495175fa-eeae-4e2c-86c7-0f88bad9a3d2')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        # >> strength
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Strength')
        number = int(page_edit.different_fx.beating_strength.get_number())
        #page_edit.driver.driver.back()               
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('495175fa-eeae-4e2c-86c7-0f88bad9a3d2',
                               True if (number == 120) and (not compare_result) else False)
        self.report.start_uuid('8b283bab-ff81-48e6-a2e5-1fecd7bec9a4')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Strength')
        page_edit.different_fx.beating_strength.set_progress(0)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_strength.get_number())
        #page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('8b283bab-ff81-48e6-a2e5-1fecd7bec9a4',
                               True if (number == 110) and (not compare_result) else False)
        self.report.start_uuid('b8a2b336-8b89-4611-8537-4a232bd7a6d2')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Beating')
        page_edit.select_effect_from_bottom_edit_menu('Strength')
        page_edit.different_fx.beating_strength.set_progress(1)
        time.sleep(5)
        number = int(page_edit.different_fx.beating_strength.get_number())
        #page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('b8a2b336-8b89-4611-8537-4a232bd7a6d2',
                               True if (number == 150) and (not compare_result) else False)
        self.report.start_uuid('15ae16ff-b32a-43aa-a091-8f74ff53dfbb')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.menu.fx).click()
        # Bloom
        #page_media.select_media_by_text('Bloom')
        #page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        page_edit.driver.driver.back()
        #page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.select_effect_from_bottom_edit_menu('Bloom')
        # >> Sample Weight
        time.sleep(2)
        page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Sample Weight')
        time.sleep(2)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        #page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1.3)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('15ae16ff-b32a-43aa-a091-8f74ff53dfbb',
                               True if (number == 100) and compare_result else False)
        self.report.start_uuid('166a757a-a6a9-4e58-aeb6-95d4ce193159')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Sample Weight')
        page_edit.different_fx.bloom_sample_weight.set_progress(0.7)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        self.report.new_result('166a757a-a6a9-4e58-aeb6-95d4ce193159', True if number > 100 else False)
        self.report.start_uuid('00cec4f8-7b7a-4de1-8f41-4a3154164052')
        page_edit.different_fx.bloom_sample_weight.set_progress(0.3)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        self.report.new_result('00cec4f8-7b7a-4de1-8f41-4a3154164052', True if number < 100 else False)
        self.report.start_uuid('b5c8d013-e4e6-46c5-8156-62a11375acb5')
        page_edit.different_fx.bloom_sample_weight.set_progress(0)
        number = int(page_edit.different_fx.bloom_sample_weight.get_number())
        #page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(10)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(1.3)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('b5c8d013-e4e6-46c5-8156-62a11375acb5',
                               True if (number == 0) and compare_result else False)
        self.report.start_uuid('42deb578-569b-43b1-8977-e951a023c0bb')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Sample Weight')
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
        self.report.new_result('42deb578-569b-43b1-8977-e951a023c0bb',
                               True if (number == 200) and compare_result else False)
        self.report.start_uuid('694e9c68-5da3-44fb-8fcd-433de94a5764')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        # >> Light Number
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
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
        self.report.new_result('694e9c68-5da3-44fb-8fcd-433de94a5764',
                               True if (number == 2) and compare_result else False)
        self.report.start_uuid('a3dd43d2-df85-4cb5-8de9-8efe81718990')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Light Number')
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
        self.report.new_result('a3dd43d2-df85-4cb5-8de9-8efe81718990',
                               True if (number == 1) and compare_result else False)
        self.report.start_uuid('ebc8b8dc-1fae-4b4e-b9be-a9b9fa1beb43')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Light Number')
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
        self.report.new_result('ebc8b8dc-1fae-4b4e-b9be-a9b9fa1beb43',
                               True if (number == 3) and compare_result else False)
        self.report.start_uuid('9a22a74b-4a8b-4c49-9f00-ae568d90813f')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        # >> Angle
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
        self.report.new_result('9a22a74b-4a8b-4c49-9f00-ae568d90813f',
                               True if (number == 50) and compare_result else False)
        self.report.start_uuid('e9167afa-d219-4dbe-b122-cdab2996521c')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Angle')
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
        self.report.new_result('e9167afa-d219-4dbe-b122-cdab2996521c',
                               True if (number == 0) and compare_result else False)
        self.report.start_uuid('387f6b41-e525-4cb3-9ee9-b4d5a52088ca')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Bloom')
        page_edit.select_effect_from_bottom_edit_menu('Angle')
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
        self.report.new_result('387f6b41-e525-4cb3-9ee9-b4d5a52088ca',
                               True if (number == 200) and compare_result else False)
        self.report.start_uuid('0209ae97-6446-4ca2-9aa7-a6acb271bd7e')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.menu.fx).click()
        # Black and White
        #page_media.select_media_by_text('Black & White')
        #page_media.el(L.import_media.library_gridview.add).click()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        page_edit.driver.driver.back()
        #page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        time.sleep(2)
        # >> Degree
        page_edit.select_effect_from_bottom_edit_menu('Black & White')
        page_edit.select_effect_from_bottom_edit_menu('Degree')
        time.sleep(2)
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        #page_edit.driver.driver.back()
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 7).compare_image())(
            pic_base, pic_after)
        self.report.new_result('0209ae97-6446-4ca2-9aa7-a6acb271bd7e',
                               True if (number == 200) and compare_result else False)
        self.report.start_uuid('2eb4540b-9ae0-4d1c-8343-13c1d78aadd7')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Black & White')
        page_edit.select_effect_from_bottom_edit_menu('Degree')
        page_edit.different_fx.black_and_white_degree.set_progress(0.7)
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        self.report.new_result('2eb4540b-9ae0-4d1c-8343-13c1d78aadd7', True if number > 100 else False)
        self.report.start_uuid('fb245de1-117c-4971-9063-6235619a47cd')
        page_edit.different_fx.black_and_white_degree.set_progress(0.3)
        number = int(page_edit.different_fx.black_and_white_degree.get_number())
        self.report.new_result('fb245de1-117c-4971-9063-6235619a47cd', True if number < 100 else False)
        self.report.start_uuid('c3c84687-a3dd-4a6b-89f5-4603401d4882')
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
        self.report.new_result('c3c84687-a3dd-4a6b-89f5-4603401d4882',
                               True if (number == 0) and compare_result else False)
        self.report.start_uuid('a8b7da78-47ab-4fec-9e5b-65aab5b1c42f')
        #page_edit.driver.driver.back()
        #page_edit.el(L.edit.timeline.fx_effect_thumbnail).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.select_from_bottom_edit_menu('Effect')
        #page_edit.select_effect_from_bottom_edit_menu('Black & White')
        page_edit.select_effect_from_bottom_edit_menu('Degree')
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
        self.report.new_result('a8b7da78-47ab-4fec-9e5b-65aab5b1c42f',
                               True if (number == 200) and compare_result else False)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_02_03(self):
        media_list = ['3gp.3GP']
        self.report.start_uuid('4846b337-fbc4-45e8-b7d4-8ea609dce99f')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.swipe_element(L.edit.timeline.playhead, "left", 600)
        pic_base = page_edit.get_preview_pic()
        page_edit.click(L.edit.timeline.clip)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.sharpness).click()
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
        # Sharpness
        number = int(page_edit.sharpness_effect.sharpness.get_number())
        self.report.new_result('4846b337-fbc4-45e8-b7d4-8ea609dce99f', True if number == 0 else False)
        self.report.start_uuid('3caeffa7-5fee-401a-b15d-8431b57670cb')
        page_edit.sharpness_effect.sharpness.set_progress(1)
        page_edit.driver.driver.back()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        compare_result = (lambda pic_src, pic_dest: CompareImage(pic_src, pic_dest, 9).compare_image())(
            pic_base, pic_after)
        self.report.new_result('3caeffa7-5fee-401a-b15d-8431b57670cb', True if not compare_result else False)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_02_04(self):
        media_list = ['png.png', 'jpg.jpg']
        self.report.start_uuid('762a27ca-5b29-4fcf-856b-eba4096dede8')
        self.report.start_uuid('ddaf394d-68ce-4327-81e9-ada90a6fba60')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
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
        #page_media.click(L.import_media.photo_library.sort)
        #page_media.click(L.import_media.photo_library.sort_menu.by_date)
        #page_media.click(L.import_media.photo_library.sort_menu.descending)
        #page_media.driver.driver.back()
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        #page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.timeline_select_item_by_index_on_track(1, 2)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        # [Photo_Apply to All] Pan_Zoom - Random Motion
        is_default_random_motion = True if page_edit.el(L.edit.pan_zoom_effect.random_motion).get_attribute(
            'checked') == 'true' else False
        self.report.new_result('762a27ca-5b29-4fcf-856b-eba4096dede8', is_default_random_motion)
        self.report.new_result('ddaf394d-68ce-4327-81e9-ada90a6fba60', is_default_random_motion)
        self.report.start_uuid('92de50a4-8180-4c74-bc02-384ffbbc990e')
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
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
        self.report.new_result('92de50a4-8180-4c74-bc02-384ffbbc990e',
                               True if compare_result_1 and compare_result_2 else False)
        # [Photo_Apply to All] Pan_Zoom - No Effect
        self.report.start_uuid('fd3c413f-c7a2-4175-b1db-e478f3b43781')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.timeline_select_media(media_list[0], 'Photo')
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        #page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        time.sleep(3)
        
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('fd3c413f-c7a2-4175-b1db-e478f3b43781',
                               True if compare_result_1 and compare_result_2 else False, 'DRA197258-0001')
        # [Photo_Apply to All] Pan_Zoom - Custom Motion
        self.report.start_uuid('8e6f606b-3e57-4993-b458-6703dc643e71')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
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
        time.sleep(2)
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
        self.report.new_result('8e6f606b-3e57-4993-b458-6703dc643e71',
                               True if compare_result_1 and compare_result_2 else False)
        # [Photo_Apply OK] Random Motion
        self.report.start_uuid('8fb60945-6baf-43ec-ba7f-6f18b219e5a1')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.random_motion).click()
        page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
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
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('8fb60945-6baf-43ec-ba7f-6f18b219e5a1',
                               True if compare_result_1 and compare_result_2 else False)
        # [Photo_Apply OK] No Effect
        self.report.start_uuid('b5b0c5a3-d02a-479d-9a20-8f8c4d112f2c')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(1)        
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 3).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[1], 'Photo')
        time.sleep(3)
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 3).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('b5b0c5a3-d02a-479d-9a20-8f8c4d112f2c',
                               True if compare_result_1 and compare_result_2 else False)
        #                       True if compare_result_1 and compare_result_2 else False, 'DRA197258-0001')
        # [Photo_Apply OK] Custom Motion
        self.report.start_uuid('77ccbc3c-8fc7-4ccb-ae25-3c40f94f5b8b')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[0], 'Photo')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        time.sleep(2)
        page_edit.el(L.edit.pan_zoom_effect.reset).click()
        time.sleep(1)
        page_edit.pan_zoom.set_custom_motion()
        page_edit.el(L.edit.pan_zoom_effect.back).click()
        page_edit.el(L.edit.pan_zoom_effect.ok).click()
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
        self.report.new_result('77ccbc3c-8fc7-4ccb-ae25-3c40f94f5b8b',
                               True if compare_result_1 and compare_result_2 else False)

    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_02_05(self):
        media_list = ['3gp.3GP', '01_static.mp4', '02_static.mp4']
        self.report.start_uuid('2e92dab6-ebcc-454f-a34c-b9ca2fed5f72')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_setting = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        # preview full screen
        time.sleep(5)
        page_edit.enter_fullscreen_preview()
        time.sleep(1)
        if page_edit.is_not_exist(L.edit.preview.fullscreen_current_position):
            page_edit.el(L.edit.preview.movie_view).click()
        self.report.new_result('2e92dab6-ebcc-454f-a34c-b9ca2fed5f72',
                               page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        time.sleep(8)
        self.report.start_uuid('e4a3c5ea-366e-4e37-89a3-ed97d9771504')
        self.report.new_result('e4a3c5ea-366e-4e37-89a3-ed97d9771504',
                               page_edit.is_exist(L.edit.preview.water_mark))
        self.report.start_uuid('5a8f50a8-cfe0-4ab7-b2dc-594f46b001a8')
        self.report.start_uuid('a5c46a51-fdee-45bb-a043-a504fcc9f6d0')
        page_edit.driver.driver.back()
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
        page_edit.timeline_select_media(media_list[1], 'Video')
        time.sleep(2)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu('left')
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        is_disabled_random_motion = True if page_edit.el(L.edit.pan_zoom_effect.random_motion).get_attribute(
            'enabled') == 'false' else False
        self.report.new_result('5a8f50a8-cfe0-4ab7-b2dc-594f46b001a8', is_disabled_random_motion)
        self.report.new_result('a5c46a51-fdee-45bb-a043-a504fcc9f6d0', is_disabled_random_motion)
        # [Video_Apply to All] No Effect
        self.report.start_uuid('622fc45c-1e9f-43cb-98ca-86fee60af878')
        page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(3)       
        page_edit.el(L.edit.menu.play).click()
        pic_base = page_edit.get_preview_pic()
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
        self.report.new_result('622fc45c-1e9f-43cb-98ca-86fee60af878',
                               True if compare_result_1 and compare_result_2 else False)
        # [Video_Apply to All] Custom Motion
        self.report.start_uuid('76d46c5f-99e5-44ca-9c75-a7020e2c670f')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[1], 'Video')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu('left')
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        time.sleep(2)
        page_edit.el(L.edit.pan_zoom_effect.reset).click()
        time.sleep(1)
        page_edit.pan_zoom.set_custom_motion()
        page_edit.el(L.edit.pan_zoom_effect.back).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[2], 'Video')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('76d46c5f-99e5-44ca-9c75-a7020e2c670f',
                               True if compare_result_1 and compare_result_2 else False)
        # [Video_Apply OK] No Effect
        self.report.start_uuid('f0f6ffdc-69ef-44c2-b3e0-5dcd2beed7c5')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[1], 'Video')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu('left')
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[2], 'Video')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('f0f6ffdc-69ef-44c2-b3e0-5dcd2beed7c5',
                               True if compare_result_1 and compare_result_2 else False)
        # [Video_Apply OK] Custom Motion - reset to no effect first
        self.report.start_uuid('2a7b46ab-09af-49c1-8e78-a21014e4fe49')
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        page_edit.timeline_select_media(media_list[1], 'Video')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu('left')
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.no_effect).click()
        page_edit.el(L.edit.pan_zoom_effect.apply_to_all).click()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.pan_zoom).click()
        page_edit.swipe_bottom_edit_menu('left')
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.el(L.edit.pan_zoom_effect.custom_motion).click()
        time.sleep(2)
        page_edit.el(L.edit.pan_zoom_effect.reset).click()
        time.sleep(1)
        page_edit.pan_zoom.set_custom_motion()
        page_edit.el(L.edit.pan_zoom_effect.back).click()
        page_edit.el(L.edit.pan_zoom_effect.ok).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result_1 = (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after)
        page_edit.timeline_select_media(media_list[2], 'Video')
        time.sleep(3)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        compare_result_2 = (
            lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest, 2).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('2a7b46ab-09af-49c1-8e78-a21014e4fe49',
                               True if compare_result_1 and compare_result_2 else False)

        # set default duration of transition
        self.report.start_uuid('a81073f8-865f-4d59-be44-978a4aa8c6a5')
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        default_value = page_edit.el(L.timeline_settings.settings.default_transition_duration_value).text
        self.report.new_result('a81073f8-865f-4d59-be44-978a4aa8c6a5',
                               True if default_value == '2.0  Second(s)' else False)
        self.report.start_uuid('d90a3cc5-214d-4701-ac74-48477c6f1967')
        timeline_setting.set_default_transition_duration(0.1)
        time.sleep(2)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        page_edit.select_transition_from_bottom_menu('Blur')
        #page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_media.el(L.edit.transition.btn_show_transition_duration).click()
        default_value = page_edit.el(L.edit.transition.duration_text).text
        self.report.new_result('d90a3cc5-214d-4701-ac74-48477c6f1967',
                               True if default_value == '0.1 s' else False)
        self.report.start_uuid('99a6d36e-cccf-4897-97c4-4da719293663')
        page_media.el(L.edit.transition.ok).click()
        time.sleep(1)
        page_edit.driver.driver.back()
        # set default duration as 4.0
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        timeline_setting.set_default_transition_duration(4.0)
        time.sleep(2)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.el(L.edit.menu.import_media).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[1])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        #page_media.click(L.import_media.video_library.sort)
        #page_media.click(L.import_media.video_library.sort_menu.by_date)
        #page_media.click(L.import_media.video_library.sort_menu.descending)
        #page_media.driver.driver.back()
        page_edit.timeline_select_transition_effect(2)
        page_edit.select_transition_from_bottom_menu('Fade')
        #page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(2)
        time.sleep(2)
        page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_second = True if page_edit.el(L.edit.transition.duration_text).text == '4.0 s' else False
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_first = True if page_edit.el(L.edit.transition.duration_text).text == '0.1 s' else False
        self.report.new_result('99a6d36e-cccf-4897-97c4-4da719293663',
                               True if result_first and result_second else False)
        # adjust transition duration - apply all [OFF]
        self.report.start_uuid('d719457a-8a7b-40da-ba86-34e3649724c7')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.transition.set_duration(3.0)
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_second = True if page_edit.el(L.edit.transition.duration_text).text == '3.0 s' else False
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(2)
        time.sleep(2)
        page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_first = True if page_edit.el(L.edit.transition.duration_text).text == '4.0 s' else False
        self.report.new_result('d719457a-8a7b-40da-ba86-34e3649724c7',
                               True if result_first and result_second else False)
        # adjust transition duration - apply all [ON]
        self.report.start_uuid('416aa8d0-e3c5-4d7d-8c71-55e790ac6e93')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        page_edit.transition.set_duration(3.0, 1)
        time.sleep(2)
        page_edit.timeline_select_transition_effect(2)
        time.sleep(2)
        page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_second = True if page_edit.el(L.edit.transition.duration_text).text == '3.0 s' else False
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        time.sleep(2)
        page_media.el(L.edit.transition.btn_show_transition_duration).click()
        result_first = True if page_edit.el(L.edit.transition.duration_text).text == '3.0 s' else False
        self.report.new_result('416aa8d0-e3c5-4d7d-8c71-55e790ac6e93',
                               True if result_first and result_second else False)  
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        timeline_setting.set_default_transition_duration(2.0)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_02_06(self):
        media_list = ['3gp.3GP', '01_static.mp4', '02_static.mp4']
        self.report.start_uuid('e551835d-58b1-41a3-9f84-30709c21fbd8')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_setting = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        # remove exists 3gp
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
        self.report.new_result('e551835d-58b1-41a3-9f84-30709c21fbd8',
                               page_edit.check_transition_exists_in_list('Blur'))
        self.report.start_uuid('326153e0-58ea-4354-973b-c4ae8a7fa430')
        #amount = page_edit.calculate_library_content_amount()
        
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
        
        self.report.new_result('326153e0-58ea-4354-973b-c4ae8a7fa430', True if amount >= 143 else False, f'amount={amount}')
        '''
        self.report.start_uuid('cdc276b6-39a8-44a6-b613-a4658c398bae')
        time.sleep(1)
        page_edit.select_transition_from_bottom_menu('X-Ray')
        time.sleep(1)
        page_media.el(L.import_media.library_gridview.play).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('cdc276b6-39a8-44a6-b613-a4658c398bae',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        '''
        
        self.report.start_uuid('d07e84a9-a127-4b85-9704-1e406870e553')
        #time.sleep(1)
        #page_edit.driver.driver.back()
        #time.sleep(2)
        #page_edit.timeline_select_transition_effect(1)
        elm = page_edit.timeline_get_transition_effect(1)
        pic_base = page_edit.driver.save_pic(elm)
        page_edit.select_transition_from_bottom_menu('X-Ray')
        time.sleep(1)
        #page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        pic_after = page_edit.driver.save_pic(elm)
        self.report.new_result('d07e84a9-a127-4b85-9704-1e406870e553',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # leave and save project
        self.report.start_uuid('c01ed916-e87b-434f-a3fe-b469270d9078')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        elm = page_edit.timeline_get_transition_effect(1)
        pic_base = page_edit.driver.save_pic(elm)
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        #page_main.select_existed_project_by_title(project_title)
        #time.sleep(1)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        page_edit.timeline_select_transition_effect(1)
        elm = page_edit.timeline_get_transition_effect(1)
        time.sleep(2)
        pic_after = page_edit.driver.save_pic(elm)
        self.report.new_result('c01ed916-e87b-434f-a3fe-b469270d9078',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               1).compare_image() else False)(
                                   pic_base, pic_after))

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_02_07(self):
        media_list = ['01_static.mp4']
        self.report.start_uuid('c85b15c4-1a6a-4e52-8a34-f80c84b6442c')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(1)
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(1)
        page_edit.settings.swipe_to_option('FAQ & Send Feedback')
        self.report.new_result('c85b15c4-1a6a-4e52-8a34-f80c84b6442c', True)
        self.report.start_uuid('e7c87b7e-5ce8-4a64-8747-5e6a3f5c5ceb')
        page_edit.el(L.edit.settings.send_feedback_btn).click()
        page_edit.el(L.edit.settings.send_feedback.send_feedback_btn).click()
        time.sleep(3)
        page_edit.back()
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
        self.report.new_result('e7c87b7e-5ce8-4a64-8747-5e6a3f5c5ceb',
                               True if result_device_model and result_os_version else False)
