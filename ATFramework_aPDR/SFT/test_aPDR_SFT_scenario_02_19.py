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


class Test_SFT_Scenario_02_19:
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
    def test_sce_02_19_01(self):
        logger('>>> test_sce_02_19_01: Text Designer Support Shadow Distance/Angle & Text color apply to all <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        
        # New project
        self.report.start_uuid('b0a6c937-00ca-44da-b21f-b03e0c3c47ab')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_19_01")
        page_main.project_set_16_9()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        time.sleep(5)
        page_media.select_title_by_order(1)
        time.sleep(5)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Designer')
        result = page_edit.is_exist(L.edit.menu.btn_apply_all)
        self.report.new_result('b0a6c937-00ca-44da-b21f-b03e0c3c47ab', result)

        self.report.start_uuid('4c02a70d-abec-4ab1-8ae6-aded20962f00')
        page_edit.title_designer.select_tab('Shadow')
        time.sleep(3)
        page_edit.title_designer.select_color_by_order(4)
        value = page_edit.title_designer.get_slider_value(L.edit.title_designer.slider_distance)
        result = True if value == '1.0' else False
        self.report.new_result('4c02a70d-abec-4ab1-8ae6-aded20962f00', result)

        self.report.start_uuid('b4308096-2c6f-4a5d-9e79-700e890181fd')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_distance, 0.9)
        self.report.new_result('b4308096-2c6f-4a5d-9e79-700e890181fd', result)

        self.report.start_uuid('d6333b10-e3a6-487f-bab3-9ee76ea6ecb6')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_distance, 0.1)
        self.report.new_result('d6333b10-e3a6-487f-bab3-9ee76ea6ecb6', result)

        self.report.start_uuid('96c5081c-56e3-4891-af23-cc78f6acbbd5')
        page_edit.title_designer.set_slider(L.edit.title_designer.slider_distance, 0.9)
        value = page_edit.title_designer.get_slider_value(L.edit.title_designer.slider_direction)
        result = True if value == '45' else False
        self.report.new_result('96c5081c-56e3-4891-af23-cc78f6acbbd5', result)

        self.report.start_uuid('7144cce1-23d3-49ef-85b5-e01339a94585')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_direction, 0.9)
        self.report.new_result('7144cce1-23d3-49ef-85b5-e01339a94585', result)

        self.report.start_uuid('9e9f3fa1-8304-404e-996c-6931880a9632')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_direction, 0.1)
        self.report.new_result('9e9f3fa1-8304-404e-996c-6931880a9632', result)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_19_02(self):
        logger('>>> test_sce_02_19_02: PiP Border & Shadow Support Shadow Distance/Angle <<<')
        media_list = ['01_static.mp4', 'jpg.jpg']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_effect = PageFactory().get_page_object("effect", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        # New project
        self.report.start_uuid('64db8810-53a9-488e-9ac6-b6b0ec45c685')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_19_02")
        page_main.project_set_16_9()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        time.sleep(3)
        page_media.switch_to_pip_video_library()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.select_media_by_text(media_list[0])
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Border & Shadow')
        time.sleep(3)
        page_edit.click(L.edit.border_and_shadow.tab_shadow)
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(3)
        value = page_edit.border_and_shadow.get_value('shadow_distance')
        result = True if value == '1.0' else False
        self.report.new_result('64db8810-53a9-488e-9ac6-b6b0ec45c685', result)

        self.report.start_uuid('c649c381-441d-48e2-b8d0-305b5f1282cb')
        result = page_edit.border_and_shadow.set_slider('shadow_distance', 0.1)
        self.report.new_result('c649c381-441d-48e2-b8d0-305b5f1282cb', result)

        self.report.start_uuid('0331907a-2916-475b-8c9a-94052afb3d7d')
        result = page_edit.border_and_shadow.set_slider('shadow_distance', 0.9)
        self.report.new_result('0331907a-2916-475b-8c9a-94052afb3d7d', result)

        self.report.start_uuid('6efed8be-7c3e-4ff3-9cb8-01231a6a6819')
        value = page_edit.border_and_shadow.get_value('shadow_angle')
        result = True if value == '45' else False
        self.report.new_result('6efed8be-7c3e-4ff3-9cb8-01231a6a6819', result)

        self.report.start_uuid('cfa6335c-0796-444e-b132-32a7034952f9')
        result = page_edit.border_and_shadow.set_slider('shadow_angle', 0.1)
        self.report.new_result('cfa6335c-0796-444e-b132-32a7034952f9', result)

        self.report.start_uuid('6c27928e-1ef1-476f-b7a1-f4eb8675ec3e')
        page_edit.border_and_shadow.set_slider('shadow_angle', 0.5)
        result = page_edit.border_and_shadow.set_slider('shadow_angle', 0.9)
        self.report.new_result('6c27928e-1ef1-476f-b7a1-f4eb8675ec3e', result)

        # Photo
        self.report.start_uuid('cb7b68a3-80a1-42d9-8475-8541f0ad4df1')
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        time.sleep(3)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[1])
        time.sleep(3)
        page_edit.click(L.import_media.library_gridview.add)
        time.sleep(3)
        page_edit.select_from_bottom_edit_menu('Border & Shadow')
        time.sleep(3)
        page_edit.click(L.edit.border_and_shadow.tab_shadow)
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(3)
        value = page_edit.border_and_shadow.get_value('shadow_distance')
        result = True if value == '1.0' else False
        self.report.new_result('cb7b68a3-80a1-42d9-8475-8541f0ad4df1', result)

        self.report.start_uuid('3a1a109e-fefc-4540-a96a-eb7c9d1b50cd')
        result = page_edit.border_and_shadow.set_slider('shadow_distance', 0.1)
        self.report.new_result('3a1a109e-fefc-4540-a96a-eb7c9d1b50cd', result)

        self.report.start_uuid('a5d1de96-4794-4c56-b279-ae65af1f6c9c')
        result = page_edit.border_and_shadow.set_slider('shadow_distance', 0.9)
        self.report.new_result('a5d1de96-4794-4c56-b279-ae65af1f6c9c', result)

        self.report.start_uuid('b151942f-bdbf-4318-8813-525ab8dadabb')
        value = page_edit.border_and_shadow.get_value('shadow_angle')
        result = True if value == '45' else False
        self.report.new_result('b151942f-bdbf-4318-8813-525ab8dadabb', result)

        self.report.start_uuid('06ad8235-a495-400a-8f00-5c5ac7f4f7cc')
        result = page_edit.border_and_shadow.set_slider('shadow_angle', 0.1)
        self.report.new_result('06ad8235-a495-400a-8f00-5c5ac7f4f7cc', result)

        self.report.start_uuid('15dbe79e-fb09-4f77-9443-b4c278070816')
        page_edit.border_and_shadow.set_slider('shadow_angle', 0.5)
        result = page_edit.border_and_shadow.set_slider('shadow_angle', 0.9)
        self.report.new_result('15dbe79e-fb09-4f77-9443-b4c278070816', result)