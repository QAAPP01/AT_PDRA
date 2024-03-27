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


class Test_SFT_Scenario_02_10:
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
    def test_sce_02_10_01(self):
        logger('>>> test_sce_02_10_01: Neon effect titles <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'

        page_main.enter_settings_from_main()
        page_main.sign_in_cyberlink_account()

        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        # page_main.subscribe()


        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(5)
        
        # Edit Text
        self.report.start_uuid('0e54b09e-ecd0-488d-8150-4c57d13cf82b')
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.select_title_category('Special Effect')
        page_media.search_template_by_image('neon')
        page_media.click(L.import_media.library_gridview.add)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Edit Text')
        page_edit.el(L.edit.title_designer.title_text_edit_area).set_text('CyberLink\ntest')
        self.report.new_result('0e54b09e-ecd0-488d-8150-4c57d13cf82b', True if page_edit.el(L.edit.title_designer.title_text_edit_area).text == 'CyberLink\ntest' else False)
        page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
        time.sleep(5)
        
        # Font
        self.report.start_uuid('808c5d80-2adf-4662-82f4-197c427f4434')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Font')
        page_edit.title_designer.set_font_by_index(3, 'menu')
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('808c5d80-2adf-4662-82f4-197c427f4434', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
        
        # Line Thickness
        self.report.start_uuid('24331371-4003-4bcf-b72e-ef71ead5d6f6')
        page_edit.select_from_bottom_edit_menu('Line Thickness')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('24331371-4003-4bcf-b72e-ef71ead5d6f6', True if value == '50' else False)        
          
        self.report.start_uuid('1a847748-385c-4fff-83da-8e065b4f5d78')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a847748-385c-4fff-83da-8e065b4f5d78', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
                
        self.report.start_uuid('2fdbbf9f-ea24-4441-9ef9-d0ac5f2f45ae')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('2fdbbf9f-ea24-4441-9ef9-d0ac5f2f45ae', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
        
        # Brightness
        self.report.start_uuid('c1730393-45f0-4488-a35e-4883df14a373')
        page_edit.select_from_bottom_edit_menu('Brightness')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('c1730393-45f0-4488-a35e-4883df14a373', True if value == '50' else False)        
          
        self.report.start_uuid('4df48f83-5eb3-49a0-88dc-067b17f4795e')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4df48f83-5eb3-49a0-88dc-067b17f4795e', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
                
        self.report.start_uuid('bc60e79a-c547-40e1-b47d-a95576b6e2e8')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('bc60e79a-c547-40e1-b47d-a95576b6e2e8', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        

        # Light Color (Neon)
        self.report.start_uuid('5bb77090-ee79-4e2d-afa5-1785f7eca42c')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Light Color')
        time.sleep(5)
        page_edit.title_designer.select_color_by_order(0)
        time.sleep(5)
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 255)
        # page_edit.color_selector.set_red_number(100)
        # page_edit.color_selector.set_green_number(0)
        # page_edit.color_selector.set_blue_number(100)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('5bb77090-ee79-4e2d-afa5-1785f7eca42c', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        

        self.report.start_uuid('78bf5a19-61da-4ca0-b320-0fcb95c812dc')
        page_edit.select_from_bottom_edit_menu('Light Color')
        time.sleep(5)
        # page_edit.color_selector.set_hue_slider(30)
        result = page_edit.title_designer.set_hue_slider(0.3)
        time.sleep(2)
        self.report.new_result('78bf5a19-61da-4ca0-b320-0fcb95c812dc', result)

        self.report.start_uuid('4c2b99a0-f82a-4719-b903-2d37f3e32657')
        # self.report.start_uuid('4c2b99a0-f82a-4719-b903-2d37f3e32657')
        # pic_base = pic_after
        # page_edit.select_from_bottom_edit_menu('Light Color')
        # time.sleep(5)
        # page_edit.color_selector.set_saturation_slider(70)
        # time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        # pic_after = page_edit.get_preview_pic()
        # self.report.new_result('4c2b99a0-f82a-4719-b903-2d37f3e32657', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.new_result('4c2b99a0-f82a-4719-b903-2d37f3e32657', None, 'N/A', 'Removed in New Color Picker page')

        self.report.start_uuid('2d3cd92f-acdb-4b6e-9366-c8a092782f2e')
        pic_base = page_edit.get_preview_pic()
        page_edit.back()
        page_edit.title_designer.select_color_by_order(4)
        time.sleep(5)
        # page_edit.click(L.edit.color_selector.red)
        # time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('2d3cd92f-acdb-4b6e-9366-c8a092782f2e', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        

        # Speed (Spark)
        self.report.start_uuid('23b3ea93-06de-459c-affe-fe63b390535a')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.search_template_by_image('spark')
        page_media.click(L.import_media.library_gridview.add)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Speed')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('23b3ea93-06de-459c-affe-fe63b390535a', True if value == '50' else False)        
          
        self.report.start_uuid('b859890d-14b7-4a39-8f22-8f761db9e519')
        pic_base = page_edit.get_preview_pic()
        value = page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('b859890d-14b7-4a39-8f22-8f761db9e519', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
                
        self.report.start_uuid('5e6f68a5-9e89-4b39-9fc0-a3b6cd4004d4')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('5e6f68a5-9e89-4b39-9fc0-a3b6cd4004d4', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        

        # Density (Spark)
        self.report.start_uuid('08eae7c0-dcef-40ab-929f-c21e54789e53')
        page_edit.select_from_bottom_edit_menu('Density')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('08eae7c0-dcef-40ab-929f-c21e54789e53', True if value == '50' else False)        
          
        self.report.start_uuid('9ad3b25e-22b2-400c-a888-b6279e600bae')
        pic_base = page_edit.get_preview_pic()
        value = page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9ad3b25e-22b2-400c-a888-b6279e600bae', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
                
        self.report.start_uuid('fc589ade-ab54-4114-9c13-be430fd14530')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('fc589ade-ab54-4114-9c13-be430fd14530', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        

        # Color 1/2 (Hand Drawn)
        self.report.start_uuid('cd84490c-dfcf-4cd9-b73c-be5f367853c1')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.search_template_by_image('handdrawn')
        page_media.click(L.import_media.library_gridview.add)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        pic_base = page_edit.get_preview_pic()
        page_edit.select_from_bottom_edit_menu('Color 1')
        time.sleep(5)
        page_edit.title_designer.select_color_by_order(0)
        time.sleep(5)
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 255)
        # page_edit.color_selector.set_red_number(100)
        # page_edit.color_selector.set_green_number(0)
        # page_edit.color_selector.set_blue_number(100)
        time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('cd84490c-dfcf-4cd9-b73c-be5f367853c1', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        

        self.report.start_uuid('8cd56196-1fa2-476c-877d-86b7229b15ea')
        # pic_base = pic_after
        # page_edit.select_from_bottom_edit_menu('Color 1')
        # time.sleep(5)
        # page_edit.title_designer.select_color_by_order(0)
        # time.sleep(5)
        # page_edit.color_selector.set_hue_slider(30)
        result = page_edit.title_designer.set_hue_slider(0.3)
        # time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        # pic_after = page_edit.get_preview_pic()
        self.report.new_result('8cd56196-1fa2-476c-877d-86b7229b15ea', result)

        self.report.start_uuid('4fddf300-5caa-4b4d-8b82-7dc7f6b62121')
        # self.report.start_uuid('4fddf300-5caa-4b4d-8b82-7dc7f6b62121')
        # pic_base = pic_after
        # page_edit.select_from_bottom_edit_menu('Color 1')
        # time.sleep(5)
        # page_edit.color_selector.set_saturation_slider(70)
        # time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        # pic_after = page_edit.get_preview_pic()
        # self.report.new_result('4fddf300-5caa-4b4d-8b82-7dc7f6b62121', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.new_result('4fddf300-5caa-4b4d-8b82-7dc7f6b62121', None, 'N/A', 'Removed in New Color Picker page')

        self.report.start_uuid('2f3dde79-a326-422a-a6ad-4528da2c9736')
        pic_base = page_edit.get_preview_pic()
        page_edit.back()
        page_edit.title_designer.select_color_by_order(4)
        # page_edit.select_from_bottom_edit_menu('Color 1')
        # time.sleep(5)
        # page_edit.click(L.edit.color_selector.red)
        time.sleep(2)
        page_edit.back()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('2f3dde79-a326-422a-a6ad-4528da2c9736', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
        
        self.report.start_uuid('c60a78d0-0720-42cf-8b4b-554c924b8bdf')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Color 2')
        time.sleep(5)
        page_edit.title_designer.select_color_by_order(0)
        time.sleep(5)
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 255)
        # page_edit.color_selector.set_red_number(100)
        # page_edit.color_selector.set_green_number(0)
        # page_edit.color_selector.set_blue_number(100)
        time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c60a78d0-0720-42cf-8b4b-554c924b8bdf', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        

        self.report.start_uuid('f5ec202d-05ef-4875-977a-99b38405ae89')
        # pic_base = pic_after
        # page_edit.select_from_bottom_edit_menu('Color 2')
        # time.sleep(5)
        # page_edit.color_selector.set_hue_slider(30)
        result = page_edit.title_designer.set_hue_slider(0.3)
        # time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        # pic_after = page_edit.get_preview_pic()
        self.report.new_result('f5ec202d-05ef-4875-977a-99b38405ae89', result)

        self.report.start_uuid('a7504ae0-8776-4181-aaab-8a90ea86d8b4')
        # self.report.start_uuid('a7504ae0-8776-4181-aaab-8a90ea86d8b4')
        # pic_base = pic_after
        # page_edit.select_from_bottom_edit_menu('Color 2')
        # time.sleep(5)
        # page_edit.color_selector.set_saturation_slider(70)
        # time.sleep(2)
        # page_edit.back()
        # time.sleep(2)
        # pic_after = page_edit.get_preview_pic()
        # self.report.new_result('a7504ae0-8776-4181-aaab-8a90ea86d8b4', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))
        self.report.new_result('a7504ae0-8776-4181-aaab-8a90ea86d8b4', None, 'N/A', 'Removed in New Color Picker page')

        self.report.start_uuid('87d76bf4-9aa7-464b-adfd-d79c50469692')
        pic_base = page_edit.get_preview_pic()
        page_edit.back()
        page_edit.title_designer.select_color_by_order(4)
        # page_edit.select_from_bottom_edit_menu('Color 2')
        # time.sleep(5)
        # page_edit.click(L.edit.color_selector.red)
        # time.sleep(2)
        page_edit.back()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('87d76bf4-9aa7-464b-adfd-d79c50469692', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
        
        # Size (Blink)
        self.report.start_uuid('760ee6e6-9047-4530-81c1-d9a8da5c930e')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.search_template_by_image('blink')
        page_media.click(L.import_media.library_gridview.add)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Size')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('760ee6e6-9047-4530-81c1-d9a8da5c930e', True if value == '90' else False)

        self.report.start_uuid('53f79d3c-35a0-4619-b847-3706f0302934')
        pic_base = page_edit.get_preview_pic()
        value = page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('53f79d3c-35a0-4619-b847-3706f0302934', (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after))

        self.report.start_uuid('51f54db9-66d7-4ca7-8ccc-c0dd61fcfcaf')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('51f54db9-66d7-4ca7-8ccc-c0dd61fcfcaf', (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after))

        # Speed (Blink)
        self.report.start_uuid('06e95cb7-e558-4eb1-996c-aa324efe3270')
        page_edit.select_from_bottom_edit_menu('Speed')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('06e95cb7-e558-4eb1-996c-aa324efe3270', True if value == '50' else False)

        self.report.start_uuid('8a54afe5-0cf9-456f-ba34-8a4b5d0259da')
        page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        value = page_edit.get_opacity_value()
        self.report.new_result('8a54afe5-0cf9-456f-ba34-8a4b5d0259da', True if value == '0' else False)

        self.report.start_uuid('ad975c1b-4b09-461c-bb52-4487686de8a3')
        page_edit.opacity_set_slider(1)
        time.sleep(2)
        value = page_edit.get_opacity_value()
        self.report.new_result('ad975c1b-4b09-461c-bb52-4487686de8a3', True if value == '100' else False)

        # Opacity (Blink)
        self.report.start_uuid('fceff25e-3fee-47fe-b31b-dbdbd0a915f9')
        page_edit.select_from_bottom_edit_menu('Opacity')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('fceff25e-3fee-47fe-b31b-dbdbd0a915f9', True if value == '30' else False)

        self.report.start_uuid('e7ca1171-f327-4e15-8572-76a28ce3813f')
        pic_base = page_edit.get_preview_pic()
        value = page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e7ca1171-f327-4e15-8572-76a28ce3813f', (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after))

        self.report.start_uuid('efdf9fa1-937c-4e24-b23f-9b6a22fbcac0')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('efdf9fa1-937c-4e24-b23f-9b6a22fbcac0', (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after))

        # Direction (Fire)
        self.report.start_uuid('4b926499-5557-4d58-b366-587f19e9a8dd')
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.fx_layer)
        time.sleep(5)
        page_media.search_template_by_image('fire')
        page_media.click(L.import_media.library_gridview.add)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Direction')
        value = page_edit.get_opacity_value()
        time.sleep(2)
        self.report.new_result('4b926499-5557-4d58-b366-587f19e9a8dd', True if value == '100' else False)

        self.report.start_uuid('ca009b16-085f-4ee7-af6b-3ea7261038e5')
        pic_base = page_edit.get_preview_pic()
        value = page_edit.opacity_set_slider(0.05)  # Set to minimal
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('ca009b16-085f-4ee7-af6b-3ea7261038e5', (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after))

        self.report.start_uuid('c079014d-3033-46a6-9d67-654718dcdc4f')
        pic_base = pic_after
        value = page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c079014d-3033-46a6-9d67-654718dcdc4f', (
            lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(
            pic_base, pic_after))

        self.report.start_uuid('67a3b16b-6aa3-4731-b243-8f6c001601a5')
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('Fire color')
        time.sleep(5)
        page_edit.title_designer.select_color_by_order(0)
        time.sleep(5)
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 255)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('67a3b16b-6aa3-4731-b243-8f6c001601a5', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        self.report.start_uuid('980fdcd7-15e0-4eca-9d2a-d696855aa972')
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('980fdcd7-15e0-4eca-9d2a-d696855aa972', result)

        self.report.start_uuid('dd053350-c623-40e0-9209-8706221c4013')
        self.report.new_result('dd053350-c623-40e0-9209-8706221c4013', None, 'N/A', 'Removed in New Color Picker page')

        self.report.start_uuid('0ad9132e-d418-4e77-a93f-3c12dc16c4b8')
        pic_base = page_edit.get_preview_pic()
        page_edit.back()
        page_edit.title_designer.select_color_by_order(6)
        page_edit.back()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0ad9132e-d418-4e77-a93f-3c12dc16c4b8', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))

        # in/out
        self.report.start_uuid('57af18bb-5686-4b1b-8874-665f074655c7')
        pic_base = pic_after
        page_edit.click(L.edit.edit_sub.back_button)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('57af18bb-5686-4b1b-8874-665f074655c7', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
     
        self.report.start_uuid('ff68e5b2-61c3-4534-a813-9779461801b0')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        pic_base = pic_after
        page_edit.select_from_bottom_edit_menu('In/Out')
        time.sleep(5)
        page_edit.click(L.edit.edit_sub.back_button)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('ff68e5b2-61c3-4534-a813-9779461801b0', (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 7).compare_image() else False)(pic_base, pic_after))        
