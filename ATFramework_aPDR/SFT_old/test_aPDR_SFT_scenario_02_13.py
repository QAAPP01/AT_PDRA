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


class Test_SFT_Scenario_02_13:
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

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_13_01(self):
        logger('>>> test_sce_02_13_01: Title Blending <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        
        # Add Title - Blending Normal
        self.report.start_uuid('8fb62a5f-68c5-4702-9b30-fb0e90b40453')
        page_edit.click(L.edit.menu.play)
        time.sleep(2)
        page_edit.click(L.edit.menu.play)
        time.sleep(2)
        page_edit.click(L.edit.menu.effect)
        time.sleep(10)
        page_media.search_template_by_image('title_note')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Blending')
        default_value = page_edit.get_opacity_value()
        self.report.new_result('8fb62a5f-68c5-4702-9b30-fb0e90b40453', True if default_value == '100' else False)
        
        self.report.start_uuid('735e35e5-bb01-407b-9433-de5f188c2240')
        pic_base = page_edit.get_preview_pic()
        page_edit.opacity_set_slider(0.5)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('735e35e5-bb01-407b-9433-de5f188c2240', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        # Overlay
        self.report.start_uuid('4ccb3bfe-7810-42fa-9719-c969569ab237')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Overlay')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4ccb3bfe-7810-42fa-9719-c969569ab237', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('41468bbf-4c32-4465-80f4-b77190730c7f')
        pic_base = pic_after
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('41468bbf-4c32-4465-80f4-b77190730c7f', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
                
        # Multiply
        self.report.start_uuid('e5e416a6-112a-451c-8e93-bf40366a1a33')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Multiply')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e5e416a6-112a-451c-8e93-bf40366a1a33', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('23e62502-9c77-46c7-9592-73a5f838f685')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.5)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('23e62502-9c77-46c7-9592-73a5f838f685', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
                
        # Screen
        self.report.start_uuid('7ffe3f4a-625f-43d6-9145-3feaf5da2f09')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Screen')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('7ffe3f4a-625f-43d6-9145-3feaf5da2f09', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('3c69295e-fb12-42d9-8c8b-53c90dd77d8b')
        pic_base = pic_after
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('3c69295e-fb12-42d9-8c8b-53c90dd77d8b', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
                
        # Hard Light
        self.report.start_uuid('bbf1c67c-c1a2-42f8-be1d-8c0973eb6059')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Hard Light')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('bbf1c67c-c1a2-42f8-be1d-8c0973eb6059', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('c0665226-a46f-42ee-911a-857bb13c137e')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.5)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c0665226-a46f-42ee-911a-857bb13c137e', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
    
        # Soft Light
        self.report.start_uuid('99ed340f-8a23-412b-b03f-88d83bf6bf64')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Soft Light')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('99ed340f-8a23-412b-b03f-88d83bf6bf64', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('34ea6c21-ce09-446e-82da-91899ee72a30')
        pic_base = pic_after
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('34ea6c21-ce09-446e-82da-91899ee72a30', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
       
        # Lighten
        self.report.start_uuid('7021e39f-fc8c-42ed-9ded-125929f37285')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Lighten')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('7021e39f-fc8c-42ed-9ded-125929f37285', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('e2eda363-4963-48a9-83f9-4fbb96159aed')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.5)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e2eda363-4963-48a9-83f9-4fbb96159aed', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
                
        # Darken
        self.report.start_uuid('acab1dc5-451a-4ff6-924f-dcdd79e0f8ce')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Darken')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('acab1dc5-451a-4ff6-924f-dcdd79e0f8ce', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('ac60088f-f4e9-4d26-b48b-609bb169617a')
        pic_base = pic_after
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('ac60088f-f4e9-4d26-b48b-609bb169617a', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
       
        # Difference
        self.report.start_uuid('c235225e-0bf4-4659-a6d9-b6f3f5bfd5c0')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Difference')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c235225e-0bf4-4659-a6d9-b6f3f5bfd5c0', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('846620ea-f8d5-4250-969f-55c1f2c3a3a7')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.5)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('846620ea-f8d5-4250-969f-55c1f2c3a3a7', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
                
        # Hue
        self.report.start_uuid('fdf12fe8-61ae-467e-b2c1-088ede80a982')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Hue')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('fdf12fe8-61ae-467e-b2c1-088ede80a982', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('dce1d17b-4759-401b-9a32-439a1871bd03')
        pic_base = pic_after
        page_edit.opacity_set_slider(1)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('dce1d17b-4759-401b-9a32-439a1871bd03', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
       
        # Luminous
        self.report.start_uuid('96360777-3c68-4915-a08b-10a4fdb25335')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Luminous')
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('96360777-3c68-4915-a08b-10a4fdb25335', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        self.report.start_uuid('dbea6901-c521-4562-851f-3f4eef332e1d')
        pic_base = pic_after
        page_edit.opacity_set_slider(0.5)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('dbea6901-c521-4562-851f-3f4eef332e1d', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_13_02(self):
        logger('>>> test_sce_02_13_02: Replace <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        
        # Video - Replace
        self.report.start_uuid('4859a0a8-4be8-4af1-b7f7-2451678a8d04')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        pic_base = page_edit.get_preview_pic()
        self.report.new_result('4859a0a8-4be8-4af1-b7f7-2451678a8d04', result)
        
        # Video -> Video
        self.report.start_uuid('414154e9-df3d-4735-9c7c-e9ca0e1d7236')
        self.report.start_uuid('80e46ab9-be68-4ca7-be35-c0bbd5157228')
        self.report.start_uuid('c2980436-2562-4a78-8632-ed3d163b03c4')
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.click(L.edit.replace.btn_replace_anyway)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after)
        self.report.new_result('414154e9-df3d-4735-9c7c-e9ca0e1d7236', result)
        self.report.new_result('c2980436-2562-4a78-8632-ed3d163b03c4', result)
        self.report.new_result('80e46ab9-be68-4ca7-be35-c0bbd5157228', result)
        
        # Video -> Photo
        self.report.start_uuid('dbcba6c7-1fd6-43de-8fc0-e7d12156154b')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('jpg.jpg')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('dbcba6c7-1fd6-43de-8fc0-e7d12156154b', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Photo Replace
        self.report.start_uuid('b7a59f41-5c6a-4fc7-bd3b-c3368aebe385')
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        self.report.new_result('b7a59f41-5c6a-4fc7-bd3b-c3368aebe385', result)        
        
        # Photo -> Video
        self.report.start_uuid('f0682fcf-ccba-4194-91e2-3531021ad5b4')
        pic_base = pic_after
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('f0682fcf-ccba-4194-91e2-3531021ad5b4', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        # Video -> Color Board
        self.report.start_uuid('9dd0c6b7-9f2d-4b82-8636-402fb1511537')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(1)
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9dd0c6b7-9f2d-4b82-8636-402fb1511537', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Color Board Replace
        self.report.start_uuid('10a39ca9-1ba6-4c27-8716-41a6df086765')
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        self.report.new_result('10a39ca9-1ba6-4c27-8716-41a6df086765', result)   
        
        # Color Board -> Photo
        self.report.start_uuid('f7bda347-2e76-4082-abd1-83a4d1b4254f')
        pic_base = pic_after
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('jpg.jpg')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('f7bda347-2e76-4082-abd1-83a4d1b4254f', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Photo -> Photo
        self.report.start_uuid('d2f2be06-8e32-46bc-bbdd-85e95b4f2e3c')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('bmp.bmp')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('d2f2be06-8e32-46bc-bbdd-85e95b4f2e3c', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Photo -> Color Board
        self.report.start_uuid('00138d3b-ff1d-4d9d-a210-522e4fc66bf9')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(1)
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('00138d3b-ff1d-4d9d-a210-522e4fc66bf9', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Color Board -> Color Board
        self.report.start_uuid('240665af-8a49-4af4-aee6-b15156f668d0')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(5)
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('240665af-8a49-4af4-aee6-b15156f668d0', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Color Board -> Video
        self.report.start_uuid('a4e05b72-cee4-4d4c-ba2f-4e5cacd872d4')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('a4e05b72-cee4-4d4c-ba2f-4e5cacd872d4', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # PiP Track
        # Video - Replace
        self.report.start_uuid('f85ccd0a-2049-4b62-8f88-ca30c2a1bc1a')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        time.sleep(10)
        page_media.switch_to_pip_video_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('mp4.mp4')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        pic_base = page_edit.get_preview_pic()
        self.report.new_result('f85ccd0a-2049-4b62-8f88-ca30c2a1bc1a', result)
        
        # Video -> Video
        self.report.start_uuid('83acf17d-fa08-4c19-a6e9-496db7266afe')
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.click(L.edit.replace.btn_replace_anyway)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('83acf17d-fa08-4c19-a6e9-496db7266afe', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        # Video -> Photo
        self.report.start_uuid('ed32c879-48e7-479d-8b27-f113d12716b5')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('jpg.jpg')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('ed32c879-48e7-479d-8b27-f113d12716b5', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Photo Replace
        self.report.start_uuid('d473c4b7-814a-4bff-88a3-6324333ece52')
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        self.report.new_result('d473c4b7-814a-4bff-88a3-6324333ece52', result)        
        
        # Photo -> Video
        self.report.start_uuid('db6c6d94-48a4-4383-99a7-4f82e21290f2')
        pic_base = pic_after
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('db6c6d94-48a4-4383-99a7-4f82e21290f2', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        
        # Video -> Color Board
        self.report.start_uuid('13bcdd3b-bb32-4014-a277-357901a241cc')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(1)
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('13bcdd3b-bb32-4014-a277-357901a241cc', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Color Board Replace
        self.report.start_uuid('6d8f718e-8890-405f-bf84-147df0c7099f')
        time.sleep(5)
        result = page_edit.select_from_bottom_edit_menu('Replace')
        self.report.new_result('6d8f718e-8890-405f-bf84-147df0c7099f', result)   
        
        # Color Board -> Photo
        self.report.start_uuid('3cef81b9-4efa-47dd-b61a-0b4e1dcc98e7')
        pic_base = pic_after
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('jpg.jpg')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('3cef81b9-4efa-47dd-b61a-0b4e1dcc98e7', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Photo -> Photo
        self.report.start_uuid('4fb92a0e-53eb-4c41-86bb-f23b62768f4f')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('bmp.bmp')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4fb92a0e-53eb-4c41-86bb-f23b62768f4f', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Photo -> Color Board
        self.report.start_uuid('282ad084-41f3-437f-82e6-537e70b29343')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(1)
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('282ad084-41f3-437f-82e6-537e70b29343', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Color Board -> Color Board
        self.report.start_uuid('b6c99b5e-9426-4890-b010-098c8b424bb4')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(5)
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('b6c99b5e-9426-4890-b010-098c8b424bb4', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # Color Board -> Video
        self.report.start_uuid('69d88115-0af7-417e-85d3-806bc14efa60')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('69d88115-0af7-417e-85d3-806bc14efa60', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))


        
        # Replace to longer Video
        self.report.start_uuid('73ba16e1-5ccf-45d1-af33-744e172c37d2')
        self.report.start_uuid('f750da8d-d886-448a-b9ec-1543b1d34068')
        self.report.start_uuid('7b8d57ec-eb5f-4a0e-9d8f-69a00b84ec79')
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('mp4.mp4')
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        result_trim_page, result_trim_text, result_duration = page_edit.replace.check_replace_trim_view()
        self.report.new_result('73ba16e1-5ccf-45d1-af33-744e172c37d2', result_trim_page)
        self.report.new_result('f750da8d-d886-448a-b9ec-1543b1d34068', result_trim_text)
        self.report.new_result('7b8d57ec-eb5f-4a0e-9d8f-69a00b84ec79', result_duration)

        self.report.start_uuid('2acc9da0-5ca2-4cc1-8f97-87546488635c')
        result = page_edit.replace.move_trim_area()
        self.report.new_result('2acc9da0-5ca2-4cc1-8f97-87546488635c', result)
        
        self.report.start_uuid('3567766c-bda7-43ba-bc39-a770f971761a')
        self.report.start_uuid('f0f47891-5d57-46ae-ad72-74e6075e4a18')
        self.report.start_uuid('453b9dd5-8e4a-4ff2-a397-eacd8f1a2ceb')
        result = page_edit.replace.seek_by_indicator()
        self.report.new_result('3567766c-bda7-43ba-bc39-a770f971761a', result)
        self.report.new_result('f0f47891-5d57-46ae-ad72-74e6075e4a18', result)
        self.report.new_result('453b9dd5-8e4a-4ff2-a397-eacd8f1a2ceb', result)
        
        self.report.start_uuid('e398e523-fa7f-474f-9d60-52d09bd62eb5')
        pic_base = pic_after
        page_edit.back()
        time.sleep(5)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e398e523-fa7f-474f-9d60-52d09bd62eb5', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))


    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_13_03(self):
        logger('>>> test_sce_02_13_03: Replace - V to V Keep edited check <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        page_main.subscribe()

        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        
        # Video - Replace
        self.report.start_uuid('5832d9c1-63cd-4596-acff-fcc399acee74')
        self.report.start_uuid('b86ce14b-4487-44b7-8775-232d1fa0258f')
        self.report.start_uuid('ea4aea97-e202-465c-a048-5e7ad8502c1f')
        self.report.start_uuid('49011d2d-e8f2-4820-892c-f9f589cf9211')
        self.report.start_uuid('fe356754-1a95-49cc-a78c-527e4211ea25')
        self.report.start_uuid('9683067a-87ec-4fb3-8532-4bf5933a8d68')
        self.report.start_uuid('f99db9bd-b220-4bbc-b1f2-9ecbcb6f673a')
        self.report.start_uuid('4f5d1d4e-a868-4e20-8af9-7a28ba64952a')
        self.report.start_uuid('c1db5ae6-6f1d-457e-8920-93b55f31e4e5')
        self.report.start_uuid('2f874c23-cedc-46f2-a409-eba777888222')
        self.report.start_uuid('82a89732-ad15-43f2-be9c-bf38c23a61ef')
        self.report.start_uuid('e2d7c9a1-6c50-449f-bd1e-6eda169b0ad5')
        self.report.start_uuid('eeb1adc8-1b94-4113-9a92-f671710fdd22')
        self.report.start_uuid('f0eca23d-7778-4bae-b54d-fc53dbcc248b')
        self.report.start_uuid('d53b7e18-1a8f-4dde-a43d-011d2e7fbd42')
        self.report.start_uuid('b0998cad-b26e-4862-9384-adb31d326cf9')
        self.report.start_uuid('4ac2a8c4-66e6-4e0c-a272-4207f7abb437')
        self.report.start_uuid('5a284f52-506d-4bac-8fa2-56117f1de2e2')
        self.report.start_uuid('64f7eace-9588-4f35-a415-be2b12491eb6')
        self.report.start_uuid('b5e822e8-116a-4338-8785-787b8d45f653')
        self.report.start_uuid('8d869f2a-7c74-4583-84c2-59a225bfef48')
        self.report.start_uuid('c437b592-ad7b-48a5-9b8a-c5595eed4dc3')
        self.report.start_uuid('26fcc95b-5380-4697-85c2-0b794bf8b90d')
        self.report.start_uuid('80013a55-11e0-4e3c-ba7b-4f0327ad565e')
        self.report.start_uuid('33b67cf6-2e06-4517-ae20-f848fc05b665')
        self.report.start_uuid('860e3bf3-dc38-44dd-8320-8c9437bdf813')
        
        self.report.start_uuid('987469bb-7a2a-4e07-b4eb-443bb728ca90')
        self.report.start_uuid('d4949374-a507-4afc-9a53-ebb43e266d7f')
        self.report.start_uuid('903fbadc-9af1-45f0-bdb3-c18132e28d77')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Volume')
        page_edit.select_from_bottom_edit_menu('Fade in')
        page_edit.select_from_bottom_edit_menu('Fade out')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Audio Tool')
        page_edit.select_from_bottom_edit_menu('Voice Changer')
        page_edit.select_from_bottom_edit_menu('Man')
        page_edit.back()
        page_edit.select_from_bottom_edit_menu('Denoise')
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.select_from_bottom_edit_menu('Food')
        page_edit.select_from_bottom_edit_menu('Cake')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_from_bottom_edit_menu('Brightness')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Contrast')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Saturation')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Hue')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Temp')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Tint')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Sharpness')
        page_edit.opacity_set_slider(1)
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Speed')
        page_edit.opacity_set_slider(0.5)
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.select_from_bottom_edit_menu('Beating')
        page_edit.back()
        time.sleep(3)
        page_edit.click_stabilizer_wait()
        page_edit.back()
        page_edit.select_from_bottom_edit_menu('Skin Smoothener')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Fit & Fill')
        page_edit.select_from_bottom_edit_menu('Background')
        page_edit.select_from_bottom_edit_menu('Blur')
        page_edit.back()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Pan & Zoom')
        page_edit.click(L.edit.pan_zoom_effect.custom_motion)
        time.sleep(5)
        page_edit.pan_zoom.set_custom_motion()
        time.sleep(5)
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Rotate')
        page_edit.select_from_bottom_edit_menu('Flip')
        time.sleep(3)
        page_edit.click_reverse_noremove()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        
        result_volume = page_edit.check_bottom_edit_menu_item_apply_status('Volume')
        result_audiotool = page_edit.check_bottom_edit_menu_item_apply_status('Audio Tool')
        result_filter = page_edit.check_bottom_edit_menu_item_apply_status('Filter')
        result_adjustment = page_edit.check_bottom_edit_menu_item_apply_status('Adjustment')
        result_speed = page_edit.check_bottom_edit_menu_item_apply_status('Speed')
        result_effect = page_edit.check_bottom_edit_menu_item_apply_status('Effect')
        result_stabilizer = page_edit.check_bottom_edit_menu_item_apply_status('Stabilizer')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        result_skin = page_edit.check_bottom_edit_menu_item_apply_status('Skin Smoothener')
        result_fit = page_edit.check_bottom_edit_menu_item_apply_status('Fit & Fill')
        result_pan = page_edit.check_bottom_edit_menu_item_apply_status('Pan & Zoom')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        result_rotate = page_edit.check_bottom_edit_menu_item_apply_status('Rotate')
        result_flip = page_edit.check_bottom_edit_menu_item_apply_status('Flip')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        result_reverse = page_edit.check_bottom_edit_menu_item_apply_status('Reverse')
        
        self.report.new_result('5832d9c1-63cd-4596-acff-fcc399acee74', result_volume)
        self.report.new_result('b86ce14b-4487-44b7-8775-232d1fa0258f', result_volume)
        self.report.new_result('ea4aea97-e202-465c-a048-5e7ad8502c1f', result_volume)
        self.report.new_result('49011d2d-e8f2-4820-892c-f9f589cf9211', result_audiotool)
        self.report.new_result('fe356754-1a95-49cc-a78c-527e4211ea25', result_audiotool)
        self.report.new_result('9683067a-87ec-4fb3-8532-4bf5933a8d68', result_filter)
        self.report.new_result('f99db9bd-b220-4bbc-b1f2-9ecbcb6f673a', result_filter)
        self.report.new_result('4f5d1d4e-a868-4e20-8af9-7a28ba64952a', result_adjustment)
        self.report.new_result('c1db5ae6-6f1d-457e-8920-93b55f31e4e5', result_adjustment)
        self.report.new_result('2f874c23-cedc-46f2-a409-eba777888222', result_adjustment)
        self.report.new_result('82a89732-ad15-43f2-be9c-bf38c23a61ef', result_adjustment)
        self.report.new_result('e2d7c9a1-6c50-449f-bd1e-6eda169b0ad5', result_adjustment)
        self.report.new_result('eeb1adc8-1b94-4113-9a92-f671710fdd22', result_adjustment)
        self.report.new_result('f0eca23d-7778-4bae-b54d-fc53dbcc248b', result_adjustment)
        self.report.new_result('d53b7e18-1a8f-4dde-a43d-011d2e7fbd42', not result_speed)
        self.report.new_result('b0998cad-b26e-4862-9384-adb31d326cf9', not result_speed)
        self.report.new_result('4ac2a8c4-66e6-4e0c-a272-4207f7abb437', not result_speed)
        self.report.new_result('5a284f52-506d-4bac-8fa2-56117f1de2e2', result_effect)
        self.report.new_result('64f7eace-9588-4f35-a415-be2b12491eb6', not result_stabilizer)
        self.report.new_result('b5e822e8-116a-4338-8785-787b8d45f653', result_skin)
        self.report.new_result('8d869f2a-7c74-4583-84c2-59a225bfef48', result_skin)
        self.report.new_result('c437b592-ad7b-48a5-9b8a-c5595eed4dc3', result_fit)
        self.report.new_result('26fcc95b-5380-4697-85c2-0b794bf8b90d', result_fit)
        self.report.new_result('80013a55-11e0-4e3c-ba7b-4f0327ad565e', result_fit)
        self.report.new_result('33b67cf6-2e06-4517-ae20-f848fc05b665', result_fit)
        self.report.new_result('860e3bf3-dc38-44dd-8320-8c9437bdf813', result_pan)
        self.report.new_result('987469bb-7a2a-4e07-b4eb-443bb728ca90', result_rotate)
        self.report.new_result('d4949374-a507-4afc-9a53-ebb43e266d7f', result_flip)
        self.report.new_result('903fbadc-9af1-45f0-bdb3-c18132e28d77', not result_reverse)
        
        self.report.start_uuid('f2c0db1e-9494-4419-ae51-af12f7ada5f8')
        page_edit.click_crop()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text('02_static.mp4')
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        result_crop = page_edit.check_bottom_edit_menu_item_apply_status('Crop')
        self.report.new_result('f2c0db1e-9494-4419-ae51-af12f7ada5f8', result_crop)
        
    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_13_04(self):
        logger('>>> test_sce_02_13_04: Replace - P to P Keep edited check <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        page_main.subscribe()

        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        
        # Video - Replace
        self.report.start_uuid('c151942b-94b3-406b-abc8-b93d25ff76bd')
        self.report.start_uuid('5db54a22-6a66-456c-a2d8-e7cbf922695e')
        self.report.start_uuid('974ab578-7285-4957-9de8-a58dbaa5bb21')
        self.report.start_uuid('6b706f25-0a22-4b3c-bd5c-081014a3829e')
        self.report.start_uuid('7e9e03da-75ea-4518-aae3-2cefce78ba80')
        self.report.start_uuid('a279ccb2-2f6e-45ed-b180-add80c4c3e1c')
        self.report.start_uuid('6409e53e-8c12-4343-b9bf-65fcdce4e2ac')
        self.report.start_uuid('d21f0fd3-005e-4252-b3a6-dd27ae5e07fc')
        self.report.start_uuid('83903378-d760-486e-82f6-91abf07244ef')
        self.report.start_uuid('f1eaeed6-3c7f-427d-b083-59e93dde7e3e')
        self.report.start_uuid('c5625458-56c9-443a-af11-779ca8445151')
        self.report.start_uuid('96b544c7-acbd-460f-8f35-441406905e8f')
        self.report.start_uuid('50a5a1fe-e3da-409c-b569-b44b4e735116')
        self.report.start_uuid('eeb0cef1-2771-44ac-a33d-da50efc0a357')
        self.report.start_uuid('4933c016-9346-4c56-9fed-c77107d4b0b0')
        self.report.start_uuid('e5a661ee-6c38-4196-9b55-22ff37193267')
        self.report.start_uuid('c4a01156-1f5c-4b7d-8762-306c990cc0dd')
        self.report.start_uuid('ae4d5391-7c4d-4101-85d5-3385570fda9b')
        self.report.start_uuid('e0880e5c-d98d-4c66-b3e4-a49d187d0a47')
        self.report.start_uuid('7d9a0a88-e5d6-4248-9800-0a8cdf4478c1')
        self.report.start_uuid('9b182412-bd0c-44f4-a5a0-cd1a6dfff820')
        self.report.start_uuid('dacb589b-a870-4562-9cec-8a0e2122c0a3')
        self.report.start_uuid('5289ba0c-3153-4ed5-b2de-4d4c8291c788')
        self.report.start_uuid('ad62a740-8479-4dcf-bb79-4257a8443889')
        self.report.start_uuid('f3a0eeef-928b-4b0b-ac18-6340e65dba30')
        self.report.start_uuid('f526e354-8410-4c70-8e6c-e05ca0934bb7')
        self.report.start_uuid('c7ec0548-3df7-47df-9573-56dcdb3ce77c')
        self.report.start_uuid('10086c52-4d0e-493c-a201-69b9de3fe2d7')
        self.report.start_uuid('647be048-390d-4031-9237-a0284a0dd1aa')
        self.report.start_uuid('ac907ce8-f966-4ce2-a7ee-5d4e8b38ec20')
        self.report.start_uuid('c61c323e-a276-4b99-9907-ac2ba6be5e9c')

        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('jpg.jpg')
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.select_from_bottom_edit_menu('Food')
        page_edit.select_from_bottom_edit_menu('Cake')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_from_bottom_edit_menu('Brightness')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Contrast')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Saturation')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Hue')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Temp')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Tint')
        page_edit.opacity_set_slider(1)
        page_edit.select_from_bottom_edit_menu('Sharpness')
        page_edit.opacity_set_slider(1)
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Opacity')
        page_edit.opacity_set_slider(0.8)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Fade')
        page_edit.select_from_bottom_edit_menu('Fade in')
        page_edit.select_from_bottom_edit_menu('Fade out')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Blending')
        page_edit.select_from_bottom_edit_menu('Overlay')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Mask')
        page_edit.select_from_bottom_edit_menu('Line')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Transform Keyframe')
        page_edit.keyframe.add_remove_keyframe()
        page_edit.back()
        time.sleep(3)    
        page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.select_from_bottom_edit_menu('Beating')
        page_edit.back()
        time.sleep(3) 
        page_edit.select_from_bottom_edit_menu('Chroma Key')
        time.sleep(3) 
        page_edit.click(L.edit.chroma_key.btn_color_straw)
        time.sleep(3)
        page_edit.click_on_preview_area()
        time.sleep(3)
        page_edit.back()
        time.sleep(3)
        
        page_edit.select_from_bottom_edit_menu('Skin Smoothener')
        page_edit.back()
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Flip')
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('png.png')
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        result_filter = page_edit.check_bottom_edit_menu_item_apply_status('Filter')
        result_adjustment = page_edit.check_bottom_edit_menu_item_apply_status('Adjustment')
        result_opacity = page_edit.check_bottom_edit_menu_item_apply_status('Adjustment')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        result_fade = page_edit.check_bottom_edit_menu_item_apply_status('Fade')
        result_blending = page_edit.check_bottom_edit_menu_item_apply_status('Blending')
        result_mask = page_edit.check_bottom_edit_menu_item_apply_status('Mask')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        result_keyframe = page_edit.check_bottom_edit_menu_item_apply_status('Transform Keyframe')
        result_effect = page_edit.check_bottom_edit_menu_item_apply_status('Effect')
        result_chroma = page_edit.check_bottom_edit_menu_item_apply_status('Chroma Key')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        page_edit.swipe_bottom_edit_menu('left')
        result_skin = page_edit.check_bottom_edit_menu_item_apply_status('Skin Smoothener')
        result_flip = page_edit.check_bottom_edit_menu_item_apply_status('Flip')
        
        self.report.new_result('c151942b-94b3-406b-abc8-b93d25ff76bd', result_filter)
        self.report.new_result('5db54a22-6a66-456c-a2d8-e7cbf922695e', result_filter)
        self.report.new_result('974ab578-7285-4957-9de8-a58dbaa5bb21', result_adjustment)
        self.report.new_result('6b706f25-0a22-4b3c-bd5c-081014a3829e', result_adjustment)
        self.report.new_result('7e9e03da-75ea-4518-aae3-2cefce78ba80', result_adjustment)
        self.report.new_result('a279ccb2-2f6e-45ed-b180-add80c4c3e1c', result_adjustment)
        self.report.new_result('6409e53e-8c12-4343-b9bf-65fcdce4e2ac', result_adjustment)
        self.report.new_result('d21f0fd3-005e-4252-b3a6-dd27ae5e07fc', result_adjustment)
        self.report.new_result('83903378-d760-486e-82f6-91abf07244ef', result_adjustment)
        self.report.new_result('f1eaeed6-3c7f-427d-b083-59e93dde7e3e', result_effect)
        self.report.new_result('c5625458-56c9-443a-af11-779ca8445151', result_skin)
        self.report.new_result('96b544c7-acbd-460f-8f35-441406905e8f', result_skin)
        self.report.new_result('50a5a1fe-e3da-409c-b569-b44b4e735116', None, 'Function not available for pip')
        self.report.new_result('eeb0cef1-2771-44ac-a33d-da50efc0a357', None, 'Function not available for pip')
        self.report.new_result('4933c016-9346-4c56-9fed-c77107d4b0b0', None, 'Function not available for pip')
        self.report.new_result('e5a661ee-6c38-4196-9b55-22ff37193267', None, 'Function not available for pip')
        self.report.new_result('c4a01156-1f5c-4b7d-8762-306c990cc0dd', None, 'Function not available for pip')
        self.report.new_result('ae4d5391-7c4d-4101-85d5-3385570fda9b', None, 'Function not available for pip')
        self.report.new_result('e0880e5c-d98d-4c66-b3e4-a49d187d0a47', None, 'Function not available for pip')
        self.report.new_result('7d9a0a88-e5d6-4248-9800-0a8cdf4478c1', result_flip)
        self.report.new_result('9b182412-bd0c-44f4-a5a0-cd1a6dfff820', None, 'Function not available for pip')
        self.report.new_result('dacb589b-a870-4562-9cec-8a0e2122c0a3', result_opacity)
        self.report.new_result('5289ba0c-3153-4ed5-b2de-4d4c8291c788', result_fade)
        self.report.new_result('ad62a740-8479-4dcf-bb79-4257a8443889', result_blending)
        self.report.new_result('f3a0eeef-928b-4b0b-ac18-6340e65dba30', result_mask)
        self.report.new_result('f526e354-8410-4c70-8e6c-e05ca0934bb7', result_mask)
        self.report.new_result('c7ec0548-3df7-47df-9573-56dcdb3ce77c', result_mask)
        self.report.new_result('10086c52-4d0e-493c-a201-69b9de3fe2d7', result_keyframe)
        self.report.new_result('647be048-390d-4031-9237-a0284a0dd1aa', result_chroma)
        self.report.new_result('ac907ce8-f966-4ce2-a7ee-5d4e8b38ec20', result_chroma)
        self.report.new_result('c61c323e-a276-4b99-9907-ac2ba6be5e9c', result_chroma)
        

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_13_05(self):
        logger('>>> test_sce_02_13_05: Replace - C to P / P to C Keep edited check <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)


        self.report.start_uuid('ffdb54eb-9f31-4733-b22d-bab0f78cdbd3')
        self.report.start_uuid('05d92a33-96ef-4c88-81fd-1e9a487c5ade')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.import_media)
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(5)
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.select_from_bottom_edit_menu('Beating')
        page_edit.back()
        time.sleep(5) 
        page_edit.select_from_bottom_edit_menu('Duration')
        time.sleep(3) 
        page_edit.duration.set_duration_slider(1)
        page_edit.click(L.edit.duration.btn_ok)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('png.png')
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        result_effect = page_edit.check_bottom_edit_menu_item_apply_status('Effect')
        page_edit.select_from_bottom_edit_menu('Duration')
        time.sleep(3) 
        value = page_edit.duration.get_duration_text()
        page_edit.click(L.edit.duration.btn_ok)
        time.sleep(5)
        self.report.new_result('ffdb54eb-9f31-4733-b22d-bab0f78cdbd3', result_effect)
        self.report.new_result('05d92a33-96ef-4c88-81fd-1e9a487c5ade', True if value == '10.0 s' else False)

        self.report.start_uuid('c68f4dbf-f3c4-4b66-bdfb-64099d240dcc')
        self.report.start_uuid('250e5e2f-b50b-4a86-a70d-86195b2ea773')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text('jpg.jpg')
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Effect')
        page_edit.select_from_bottom_edit_menu('Beating')
        page_edit.back()
        time.sleep(5) 
        page_edit.select_from_bottom_edit_menu('Duration')
        time.sleep(3) 
        page_edit.duration.set_duration_slider(1)
        page_edit.click(L.edit.duration.btn_ok)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Replace')
        time.sleep(5)
        page_media.switch_to_photo_library()
        time.sleep(5)
        page_media.select_media_by_text('Color Board')
        page_media.select_media_by_order(5)
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(5)
        result_effect = page_edit.check_bottom_edit_menu_item_apply_status('Effect')
        page_edit.select_from_bottom_edit_menu('Duration')
        time.sleep(3) 
        value = page_edit.duration.get_duration_text()
        self.report.new_result('c68f4dbf-f3c4-4b66-bdfb-64099d240dcc', result_effect)
        self.report.new_result('250e5e2f-b50b-4a86-a70d-86195b2ea773', True if value == '10.0 s' else False)