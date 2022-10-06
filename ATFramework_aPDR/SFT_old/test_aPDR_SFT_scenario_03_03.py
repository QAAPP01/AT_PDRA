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


class Test_SFT_Scenario_03_03:
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
    def test_sce_03_03_01(self):
        video_list = ['mp4.mp4']
        self.report.start_uuid('e94b15b5-a219-45a3-a2ed-10648c201b11')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        self.report.new_result('e94b15b5-a219-45a3-a2ed-10648c201b11',
                               page_edit.check_preview_aspect_ratio(project_title))
        self.report.start_uuid('48acb92a-0f70-4e6b-9d4c-87d72b570d3b')
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        # select Title to add timeline
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        # verify if add to effect track#1
        result_add_clip = True if page_edit.el(L.edit.timeline.playhead).rect['x'] < \
                                  page_edit.timeline_get_item_by_index_on_track(2, 1).rect['x'] else False
        self.report.new_result('48acb92a-0f70-4e6b-9d4c-87d72b570d3b', result_add_clip)
        self.report.start_uuid('85ef3b31-feaf-48fc-9fb1-a9928c7bf0bc')
        self.report.start_uuid('c9f50094-70ea-4c37-b4d4-4b41e0b32a60')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.force_uncheck_help_enable_tip_to_Leave()
        time.sleep(2)
        result_check_edit_btn = (True if page_edit.is_exist(L.edit.preview.btn_title_designer_right_top) else False)
        self.report.new_result('85ef3b31-feaf-48fc-9fb1-a9928c7bf0bc', result_check_edit_btn)
        # font face: OFF (default is ON) ================================
        self.report.new_result('c9f50094-70ea-4c37-b4d4-4b41e0b32a60', result_check_edit_btn) #check edit btn
        self.report.start_uuid('68b4ac19-c0e2-4636-b10a-0aa90fbf5374')
        page_edit.el(L.edit.preview.btn_title_designer_right_top).click()
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('68b4ac19-c0e2-4636-b10a-0aa90fbf5374',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest, 3).compare_image() else False)(pic_base, pic_after))
        # font face switch is removed in new Title Designer (9.3.0)
        self.report.start_uuid('9ba561a8-4cad-4a39-ab37-9fd44c52784e')
        self.report.start_uuid('5f6bc51a-cb9b-4aa5-9591-f450f29900e0')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9ba561a8-4cad-4a39-ab37-9fd44c52784e',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # set font
        self.report.new_result('5f6bc51a-cb9b-4aa5-9591-f450f29900e0', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('0fcde1db-e2bb-4ea1-853b-7b988eaf7deb')
        self.report.start_uuid('1ac386c7-8daf-4624-821f-e31d9af631f6')
        pic_base = pic_after
        page_edit.title_designer.set_font_by_index(2)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0fcde1db-e2bb-4ea1-853b-7b988eaf7deb',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # red color
        self.report.new_result('1ac386c7-8daf-4624-821f-e31d9af631f6', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('58a0ca76-5e3f-453b-ae99-c8fa6368500b')
        self.report.start_uuid('af9086ea-0063-464c-b622-ce7ee24fe57f')
        pic_base = pic_after
        page_edit.click(L.edit.title_designer.btn_edit_face)
        time.sleep(3)
        page_edit.title_designer.select_color_by_order(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('58a0ca76-5e3f-453b-ae99-c8fa6368500b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.new_result('af9086ea-0063-464c-b622-ce7ee24fe57f', result_check_edit_btn)  # check edit btn

        # Set opacity
        self.report.start_uuid('37a1df3f-ce52-40aa-9bc8-286349d43c48')
        self.report.start_uuid('295b242f-b4bb-4691-bc3d-65d3c3cce480')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
        page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 1)
        self.report.new_result('37a1df3f-ce52-40aa-9bc8-286349d43c48', result)
        self.report.new_result('295b242f-b4bb-4691-bc3d-65d3c3cce480', result)

        # Color Selector
        self.report.start_uuid('748c5deb-ab36-4cf5-9225-85d832639f48')
        page_edit.title_designer.select_color_by_order(1)
        time.sleep(3)
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('748c5deb-ab36-4cf5-9225-85d832639f48', result)

        self.report.start_uuid('5ea703aa-ea14-40fe-91b6-7bfb0868cc3c')
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('5ea703aa-ea14-40fe-91b6-7bfb0868cc3c', result)

        self.report.start_uuid('de243c5f-5cb3-4316-a03d-391c2787130f')
        result = page_edit.title_designer.select_color_dropper(0.1, 0.1)
        self.report.new_result('de243c5f-5cb3-4316-a03d-391c2787130f', result)

        self.report.start_uuid('75d69255-b397-445a-a158-aaab3b95aad4')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('75d69255-b397-445a-a158-aaab3b95aad4',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('e843e0a3-5cec-443a-9d73-28dbe9559b40')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('green', 250)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e843e0a3-5cec-443a-9d73-28dbe9559b40',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('167357eb-53da-4907-b91c-e7b648eb8bd4')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        page_edit.driver.driver.back()
        self.report.new_result('167357eb-53da-4907-b91c-e7b648eb8bd4',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        # Set Gradient color
        self.report.start_uuid('727b0cfa-6560-46b4-9cc6-0891da9b1a22')
        page_edit.click(L.edit.title_designer.tab_gradient)
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(4)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('727b0cfa-6560-46b4-9cc6-0891da9b1a22',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('bb17ea63-f9f0-4bb2-b0cd-aff9702b57ee')
        self.report.start_uuid('f0638f65-f1fa-4cc5-b75d-24061925be52')
        page_edit.title_designer.select_color_by_order(1)
        page_edit.click(L.edit.title_designer.colorpicker.second_color)
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('bb17ea63-f9f0-4bb2-b0cd-aff9702b57ee', result)
        self.report.new_result('f0638f65-f1fa-4cc5-b75d-24061925be52', result)

        self.report.start_uuid('0d54b381-a85e-4f93-bb7d-9a87f93bf9d6')
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('0d54b381-a85e-4f93-bb7d-9a87f93bf9d6', result)

        self.report.start_uuid('46701956-e496-49f9-a103-f9126d63f1a6')
        self.report.start_uuid('e628285f-f875-4589-8591-cfe72eb08a1c')
        page_edit.click(L.edit.title_designer.colorpicker.first_color)
        result = page_edit.title_designer.select_color_dropper(0.1, 0.1)
        self.report.new_result('46701956-e496-49f9-a103-f9126d63f1a6', result)
        self.report.new_result('e628285f-f875-4589-8591-cfe72eb08a1c', result)

        self.report.start_uuid('0754d52a-a096-4cf1-b366-d63421cb9a4d')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0754d52a-a096-4cf1-b366-d63421cb9a4d',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('0646c4e8-61f3-4178-a16a-2835fb441df4')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('green', 250)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0646c4e8-61f3-4178-a16a-2835fb441df4',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('ff187efe-ab0d-4537-82a0-05965e1a438c')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        page_edit.driver.driver.back()
        self.report.new_result('ff187efe-ab0d-4537-82a0-05965e1a438c',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('2224bbbb-16a7-4c9a-a6f0-9b2577755011')
        self.report.start_uuid('5c741ac4-aca5-453d-bb31-a6be8b9f75e0')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_angle, 1)
        self.report.new_result('2224bbbb-16a7-4c9a-a6f0-9b2577755011', result)
        self.report.new_result('5c741ac4-aca5-453d-bb31-a6be8b9f75e0', result)

        self.report.start_uuid('3f4f23f2-26ac-484e-afc2-3cae8ff529c7')
        self.report.start_uuid('269ab00b-ab1d-4b2d-b263-3996fe879c07')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_transition, 0.3)
        self.report.new_result('3f4f23f2-26ac-484e-afc2-3cae8ff529c7', result)
        self.report.new_result('269ab00b-ab1d-4b2d-b263-3996fe879c07', result)

        self.report.start_uuid('f18ef1e4-6589-4d9a-ada4-757271225041')
        self.report.start_uuid('54a92b1b-7547-41dd-8953-7ba085f6257a')
        page_edit.title_designer.swipe_slider_area('up')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
        self.report.new_result('f18ef1e4-6589-4d9a-ada4-757271225041', result)
        self.report.new_result('54a92b1b-7547-41dd-8953-7ba085f6257a', result)

        # Character type : Bold (default: Normal) ================================

        self.report.start_uuid('c74a467a-4ec9-49f4-ab5e-fe359a68d847')
        self.report.start_uuid('4f22e6a3-2b27-4a95-bde9-6fe83031d4d9')
        pic_base = pic_after
        page_edit.title_designer.set_font_bold('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c74a467a-4ec9-49f4-ab5e-fe359a68d847',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   10).compare_image() else False)(
                                   pic_base, pic_after))
        # Character type : Italic
        self.report.new_result('4f22e6a3-2b27-4a95-bde9-6fe83031d4d9', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('6235253d-bc66-43c9-a657-822ccc31c46c')
        self.report.start_uuid('4efa6a0d-70fa-47e4-99e0-afcb809cb402')
        pic_base = pic_after
        page_edit.title_designer.set_font_bold('OFF')
        page_edit.title_designer.set_font_italic('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('6235253d-bc66-43c9-a657-822ccc31c46c',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Character type : Bold+Italic
        self.report.new_result('4efa6a0d-70fa-47e4-99e0-afcb809cb402', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('f4e1a741-df08-4b9d-b74c-858df43d6722')
        self.report.start_uuid('ebc3a76d-5a29-4b9b-88da-466d983ee197')
        pic_base = pic_after
        page_edit.title_designer.set_font_bold('ON')
        page_edit.title_designer.set_font_italic('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('f4e1a741-df08-4b9d-b74c-858df43d6722',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Character type : Normal
        self.report.new_result('ebc3a76d-5a29-4b9b-88da-466d983ee197', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('6426f330-7235-451e-9341-b381bff175b5')
        pic_base = pic_after
        page_edit.title_designer.set_font_bold('OFF')
        page_edit.title_designer.set_font_italic('OFF')
        page_edit.driver.driver.back()
        page_edit.exist_click(L.edit.try_before_buy.remove)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('6426f330-7235-451e-9341-b381bff175b5',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        #modify title text
        self.report.start_uuid('050aa73b-617a-4f03-b5b6-cd1b1db0b054')
        self.report.start_uuid('48227e6a-8653-4c74-9d7e-f1eaea09f479')
        self.report.start_uuid('37ce2ccd-4509-4645-a69c-54643fc71618')
        page_edit.el(L.edit.title_designer.title_object).click()
        self.report.new_result('48227e6a-8653-4c74-9d7e-f1eaea09f479',
                               page_edit.is_exist(L.edit.title_designer.title_text_edit_area))
        page_edit.el(L.edit.title_designer.title_text_edit_area).set_text('CyberLink\ntest')
        self.report.new_result('37ce2ccd-4509-4645-a69c-54643fc71618', True if page_edit.el(
            L.edit.title_designer.title_text_edit_area).text == 'CyberLink\ntest' else False)
        page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
        # Align to Mid
        self.report.new_result('050aa73b-617a-4f03-b5b6-cd1b1db0b054', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('408459ed-eb4e-4cf8-80f8-990d272f0b25')
        self.report.start_uuid('8f1fd821-8b09-4119-9887-22edba7dac3b')
        pic_base = pic_after
        # page_edit.el(L.edit.preview.btn_title_designer_right_top).click()
        page_edit.el(L.edit.title_designer.align).click()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('408459ed-eb4e-4cf8-80f8-990d272f0b25',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Align to Left
        self.report.new_result('8f1fd821-8b09-4119-9887-22edba7dac3b', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('33d2f4e3-bb0c-43e5-8358-a8f101a37b3b')
        self.report.start_uuid('b34aceea-2fce-40c4-a6c0-ceff80be5805')
        pic_base = pic_after
        page_edit.el(L.edit.title_designer.align).click()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('33d2f4e3-bb0c-43e5-8358-a8f101a37b3b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Align to Right
        self.report.new_result('b34aceea-2fce-40c4-a6c0-ceff80be5805', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('00aee89f-b1f5-42ee-b523-d290a057ab28')
        pic_base = pic_after
        page_edit.el(L.edit.title_designer.align).click()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('00aee89f-b1f5-42ee-b523-d290a057ab28',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        #Title Designer - Border ================================
        self.report.start_uuid('ebcae207-809b-453e-a96c-f3e9c63f87be')
        page_edit.el(L.edit.title_designer.btn_edit_bolder).click()
        # default_border_setting = True if (page_edit.el(L.edit.title_designer.switch_border).get_attribute('checked') == 'true') and (page_edit.el(L.edit.title_designer.border_size_text).text == '0.0') else False
        default_border_setting = None
        # Border - 4.0, White
        self.report.new_result('ebcae207-809b-453e-a96c-f3e9c63f87be', default_border_setting)
        self.report.start_uuid('3e20d243-b802-4b21-a96a-072da9bc7706')
        self.report.start_uuid('f108703f-f45c-4022-a6f7-076fb1d39a63')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_size, 0.8)
        self.report.new_result('3e20d243-b802-4b21-a96a-072da9bc7706', result)
        # Border - OFF (default: ON)
        self.report.new_result('f108703f-f45c-4022-a6f7-076fb1d39a63', default_border_setting)
        self.report.start_uuid('79c33330-58b1-4327-ace8-5c677884e19e')
        self.report.start_uuid('ae6898ed-75de-47c8-98fb-3cfbb8474ac9')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('79c33330-58b1-4327-ace8-5c677884e19e',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Border - ON
        self.report.new_result('ae6898ed-75de-47c8-98fb-3cfbb8474ac9', default_border_setting)
        self.report.start_uuid('0f794ece-6f15-4c6a-b973-9a43f31792e2')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0f794ece-6f15-4c6a-b973-9a43f31792e2',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        # Title Designer - Border 2================================
        self.report.start_uuid('4c267666-03a2-4dad-9501-4bcdf3d44693')
        page_edit.el(L.edit.title_designer.tab_border2).click()
        # default_border_setting = True if (page_edit.el(L.edit.title_designer.switch_border).get_attribute('checked') == 'true') and (page_edit.el(L.edit.title_designer.border_size_text).text == '0.0') else False
        default_border_setting = None
        # Border - 4.0, White
        self.report.new_result('4c267666-03a2-4dad-9501-4bcdf3d44693', default_border_setting)
        self.report.start_uuid('0aeb408a-9fbd-43bb-8e9a-ef62ebae22c7')
        self.report.start_uuid('2d13fbfc-c167-43b1-965b-dc5830ca0ffd')
        page_edit.title_designer.select_color_by_order(3)
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_size, 0.8)
        self.report.new_result('0aeb408a-9fbd-43bb-8e9a-ef62ebae22c7', result)
        # Border - OFF
        self.report.new_result('2d13fbfc-c167-43b1-965b-dc5830ca0ffd', default_border_setting)
        self.report.start_uuid('e36cbe6b-3df5-4214-96df-7ab7def49625')
        self.report.start_uuid('967fea74-96bc-4c2d-951f-1ca0a3b907b8')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e36cbe6b-3df5-4214-96df-7ab7def49625',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Border - ON
        self.report.new_result('967fea74-96bc-4c2d-951f-1ca0a3b907b8', default_border_setting)
        self.report.start_uuid('8085e580-7287-4efa-b5d7-a32340ca6196')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('8085e580-7287-4efa-b5d7-a32340ca6196',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        # Title Designer - Shadow ================================
        self.report.start_uuid('99ff30ba-e348-4c0e-b3c8-aa92a6403d31')
        page_edit.el(L.edit.title_designer.btn_edit_shadow).click()
        self.report.new_result('99ff30ba-e348-4c0e-b3c8-aa92a6403d31', True if (page_edit.el(L.edit.title_designer.switch_fill_shadow).get_attribute('enabled') == 'false')
                                else False)
        #Shadow - ON (default: OFF) w/ black color (default)
        self.report.start_uuid('7970a12f-035b-44fd-b03d-53ae49ce3c03')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(6)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('7970a12f-035b-44fd-b03d-53ae49ce3c03',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Shadow - OFF
        self.report.start_uuid('693f2361-43f7-4645-8a39-db10108f2e1c')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('693f2361-43f7-4645-8a39-db10108f2e1c',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Shadow - 3.0, Red
        self.report.start_uuid('319ddc0e-fb3e-41fd-9ee9-d63a5670d6d3')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(1)
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 0)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('319ddc0e-fb3e-41fd-9ee9-d63a5670d6d3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Fill Shadow - ON
        self.report.start_uuid('4464974f-ab3c-432f-a52b-67995807afa8')
        pic_base = pic_after
        page_edit.title_designer.set_fill_shadow('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4464974f-ab3c-432f-a52b-67995807afa8',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))
        # Fill Shadow - OFF
        self.report.start_uuid('2003f3c8-95fb-431f-ab6a-14ce3e51fd54')
        pic_base = pic_after
        page_edit.title_designer.set_fill_shadow('OFF')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('2003f3c8-95fb-431f-ab6a-14ce3e51fd54',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   8).compare_image() else False)(
                                   pic_base, pic_after))

        # Shadow sliders
        self.report.start_uuid('00dc948a-5b84-4d80-b3b6-3ba49d7d7b37')
        self.report.start_uuid('5d27b2a4-dd55-4267-b902-d763bec33fd5')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_blur, 0)
        self.report.new_result('00dc948a-5b84-4d80-b3b6-3ba49d7d7b37', result)
        self.report.new_result('5d27b2a4-dd55-4267-b902-d763bec33fd5', result)
        self.report.start_uuid('12c19ce1-bac2-47f2-a43e-422db9f0673e')
        self.report.start_uuid('ea79e5c8-6125-4f04-ab3f-c89d60b55863')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_distance, 0.9)
        self.report.new_result('12c19ce1-bac2-47f2-a43e-422db9f0673e', result)
        self.report.new_result('ea79e5c8-6125-4f04-ab3f-c89d60b55863', result)
        self.report.start_uuid('5a4d5b79-cabe-48f5-8543-99fc0e8a314c')
        self.report.start_uuid('e432078f-9875-42c0-9fd1-961b2a4cc48f')
        page_edit.title_designer.swipe_slider_area('up')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
        self.report.new_result('5a4d5b79-cabe-48f5-8543-99fc0e8a314c', result)
        self.report.new_result('e432078f-9875-42c0-9fd1-961b2a4cc48f', result)

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_03_02(self):
        self.report.start_uuid('9fcd27f4-fc5f-4f42-8c91-a248210e4d35')
        self.report.start_uuid('acbca933-64f9-4445-a4f7-f4c3c4affcd9')
        media_list = ['png.png', 'Like', '01_static.mp4', '3gp.3GP', '(255, 153, 204)']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        # set title duration to 5 sec
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        timeline_settings.set_default_title_duration('5.0')
        time.sleep(2)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        # select Assembly Line to add timeline
        #page_media.select_media_by_text('Assembly Line')
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.driver.swipe_left()
        time.sleep(2)
        page_edit.driver.swipe_left()
        time.sleep(2)
        amount = page_edit.calculate_library_content_amount()
        self.report.new_result('9fcd27f4-fc5f-4f42-8c91-a248210e4d35', True if amount == 17 else False)
        # >> check preview frame
        self.report.start_uuid('be19a8eb-3d59-4a9e-bbc3-7cac4a5550ef')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        # [Pip - Title] snap to boundary
        time.sleep(2)
        page_effect.snap_title_to_boundary()
        time.sleep(2)
        result_snap = page_effect.check_title_snap_to_boundary()
        self.report.new_result('acbca933-64f9-4445-a4f7-f4c3c4affcd9', result_snap)
        self.report.new_result('be19a8eb-3d59-4a9e-bbc3-7cac4a5550ef', result_snap)
        self.report.start_uuid('43470412-14e8-47c7-9948-f18cedc6f2cc')
        self.report.start_uuid('d7f358a6-7f6c-4a9c-95f6-dafa93163e77')
        page_effect.move_title_to_center()
        time.sleep(2)
        # [Pip - Title] re-size
        pic_base = page_edit.get_preview_pic()
        page_effect.modify_title_size()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        result_resize = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                            5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('43470412-14e8-47c7-9948-f18cedc6f2cc',result_resize)
        self.report.new_result('d7f358a6-7f6c-4a9c-95f6-dafa93163e77', True if result_snap and result_resize else False)
        self.report.start_uuid('31e052e2-474b-4122-891b-52aab3d4afac')
        # [Pip - Title] set rotate
        pic_base = pic_after
        page_effect.modify_title_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('31e052e2-474b-4122-891b-52aab3d4afac',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('ca1b73a6-4b08-4a26-9f4c-b6c2065e6499')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(2)
        # [Pip - Photo] ================================
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        # [Pip - Photo] snap to boundary
        time.sleep(2)
        page_effect.snap_effect_to_boundary()
        time.sleep(2)
        self.report.new_result('ca1b73a6-4b08-4a26-9f4c-b6c2065e6499', page_effect.check_effect_snap_to_boundary())
        self.report.start_uuid('04d2f577-6e08-45da-b397-064b6b39b723')
        page_effect.move_effect_to_center()
        time.sleep(2)
        # [Pip - Photo] re-size
        pic_base = page_edit.get_preview_pic()
        page_effect.modify_effect_size()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('04d2f577-6e08-45da-b397-064b6b39b723',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('d776375e-e3f4-4bc7-84d9-2eada5b044a4')
        # [Pip - Photo] set rotate
        pic_base = pic_after
        page_effect.modify_effect_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('d776375e-e3f4-4bc7-84d9-2eada5b044a4',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('c2669355-bcf2-4259-9ec8-213af8e749f4')
        self.report.start_uuid('be6327c9-bbbc-4c6e-991b-592eb9ac59ec')
        time.sleep(1)
        # ========================
        # [Pip - Photo > Sharpness]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.sharpness).click()
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
        time.sleep(2)
        default_value = int(page_edit.sharpness_effect.sharpness.get_number())
        self.report.new_result('c2669355-bcf2-4259-9ec8-213af8e749f4', True if default_value == 0 else False)
        self.report.new_result('be6327c9-bbbc-4c6e-991b-592eb9ac59ec', True if default_value == 0 else False)
        self.report.start_uuid('dbdd27a5-ebab-4db4-aaef-f61ba7cc54ce')
        self.report.start_uuid('d42692f4-0815-4822-8c26-25351199a04a')
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.sharpness.sharpness_level).set_text('100')
        page_edit.sharpness_effect.sharpness.set_progress(1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('dbdd27a5-ebab-4db4-aaef-f61ba7cc54ce', result)
        self.report.new_result('d42692f4-0815-4822-8c26-25351199a04a', result)
        self.report.start_uuid('14bd7895-fef3-43a8-a543-9aaadfdcf0b4')
        page_edit.driver.driver.back()
        time.sleep(2)
        # ========================
        # [Pip - Photo > Skin Smoothener]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.skin_smoothener).click()
        page_edit.select_from_bottom_edit_menu('Skin Smoothener')
        time.sleep(2)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        result_brightness = page_edit.skin_smoothener.skin_brightness.is_number(80)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        result_smoothness = page_edit.skin_smoothener.skin_smoothness.is_number(80)
        self.report.new_result('14bd7895-fef3-43a8-a543-9aaadfdcf0b4',
                               True if result_brightness and result_smoothness else False)
        self.report.start_uuid('8b1c9348-bbe8-491a-b1e9-dc337fa51bd6')
        self.report.start_uuid('d3443440-1647-40c2-8cb9-caf768a9f7cb')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        #page_edit.skin_smoothener.skin_brightness.set_number(50)
        page_edit.skin_smoothener.skin_brightness.set_progress(0.5)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        #page_edit.skin_smoothener.skin_smoothness.set_number(50)
        page_edit.skin_smoothener.skin_smoothness.set_progress(0.5)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('8b1c9348-bbe8-491a-b1e9-dc337fa51bd6', result)
        self.report.new_result('d3443440-1647-40c2-8cb9-caf768a9f7cb', result)
        self.report.start_uuid('25c18f46-078c-456d-bf01-6e87c6b41281')
        pic_base = pic_after
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        #page_edit.skin_smoothener.skin_brightness.set_number(40)
        page_edit.skin_smoothener.skin_brightness.set_progress(0)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        #page_edit.skin_smoothener.skin_smoothness.set_number(0)
        page_edit.skin_smoothener.skin_smoothness.set_progress(0)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('25c18f46-078c-456d-bf01-6e87c6b41281',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('53e23c0f-ba76-439c-b489-9783b99f96f5')
        self.report.start_uuid('2538cc64-2e6c-4ac2-bf11-d44831a569ea')
        time.sleep(1)
        page_edit.driver.driver.back()
        # ========================
        # [Pip - Photo > Color Filter]
        page_edit.swipe_element(L.edit.timeline.playhead, 'left', 100)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_3).click()
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_8).click()
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('53e23c0f-ba76-439c-b489-9783b99f96f5', result)
        self.report.new_result('2538cc64-2e6c-4ac2-bf11-d44831a569ea', result)
        self.report.start_uuid('62cacb1a-89d7-4176-8d27-7b24b43c5f28')
        # ========================
        # [Pip - Photo > Chroma key]
        pic_base_timeline = page_edit.get_preview_pic()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.chroma_key).click()
        page_edit.select_from_bottom_edit_menu('Chroma Key')
        result_color_range = page_edit.chroma_key.color_range.is_enabled()
        result_denoise = page_edit.chroma_key.denoise.is_enabled()
        self.report.new_result('62cacb1a-89d7-4176-8d27-7b24b43c5f28',
                               True if (not result_color_range) and (not result_denoise) else False)
        self.report.start_uuid('4471397a-22a9-406a-9ba1-f144db554cd9')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.chroma_key.btn_color_straw).click()
        time.sleep(1)
        page_edit.click_on_preview_area()
        time.sleep(1)
        page_edit.el(L.edit.chroma_key.btn_color_straw).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('4471397a-22a9-406a-9ba1-f144db554cd9', result)
        self.report.start_uuid('e70dd29f-1bb7-4ea0-ad46-d36ff5b45224')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        pic_after_timeline = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base_timeline, pic_after_timeline)
        self.report.new_result('e70dd29f-1bb7-4ea0-ad46-d36ff5b45224', result)
        self.report.start_uuid('2e931534-a9b2-4d20-8060-451325b5f3bd')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.chroma_key).click()
        page_edit.select_from_bottom_edit_menu('Chroma Key')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        # click reset
        page_edit.el(L.edit.chroma_key.reset).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('2e931534-a9b2-4d20-8060-451325b5f3bd', result)
        self.report.start_uuid('d31d993f-68ec-494d-bb4c-b1d7cd03c930')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # ========================
        # >> [Pip - Edit Photo] Opacity
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.opacity).click()
        page_edit.select_from_bottom_edit_menu('Opacity')
        time.sleep(2)
        pic_base = pic_after
        #page_edit.el(L.edit.opacity.slider).set_text('30')
        page_edit.opacity_set_slider(0.3)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('d31d993f-68ec-494d-bb4c-b1d7cd03c930',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('9df23065-fd6d-4f49-907e-c51acc9eba9c')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Photo] Flip
        pic_base = pic_after
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.flip).click()
        page_edit.select_from_bottom_edit_menu('Flip')
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9df23065-fd6d-4f49-907e-c51acc9eba9c',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('b4ead7ab-3c69-4a22-98e2-303dd5b52293')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Photo] Fade
        page_edit.swipe_element(L.edit.timeline.playhead, "right", 700)
        time.sleep(1)
        #page_edit.timeline_select_item_on_track(media_list[3])
        page_edit.timeline_select_item_by_index_on_track(1, 1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.fade).click()
        page_edit.select_from_bottom_edit_menu('Fade')
        #time.sleep(1)
        #page_edit.fade.set_fade_out('OFF')
        #time.sleep(1)
        #page_edit.el(L.edit.fade.ok).click()
        time.sleep(1)
        page_edit.select_adjustment_from_bottom_edit_menu('Fade out')
        page_edit.driver.driver.back()  # for un-select title item on timeline
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('b4ead7ab-3c69-4a22-98e2-303dd5b52293',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('20f46d31-ea40-409f-ab90-ca2ec6e3cb90')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(2)
        # [Pip - Sticker] ================================
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.sticker).click()
        page_edit.el(L.edit.effect_sub.sticker_tabs.tab_downloaded).click()
        #page_media.select_media_by_text(media_list[1])
        page_media.select_media_by_order(5)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        # [Pip - Sticker] snap to boundary
        page_effect.snap_effect_to_boundary()
        time.sleep(1)
        self.report.new_result('20f46d31-ea40-409f-ab90-ca2ec6e3cb90', page_effect.check_effect_snap_to_boundary())
        self.report.start_uuid('6f515787-e306-47fe-a08e-605032d2f0af')
        page_effect.move_effect_to_center()
        time.sleep(2)
        # [Pip - Sticker] re-size
        pic_base = page_edit.get_preview_pic()
        page_effect.modify_effect_size()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('6f515787-e306-47fe-a08e-605032d2f0af',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('a889c4d4-9a49-469a-ad6e-d9051aa1c093')
        # [Pip - Sticker] set rotate
        pic_base = pic_after
        page_effect.modify_effect_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('a889c4d4-9a49-469a-ad6e-d9051aa1c093',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('1de7c402-45d8-4ff8-8c52-7c55dfbbfed3')
        time.sleep(1)
        # ==================
        # >> [Pip - Edit Sticker] Opacity
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.opacity).click()
        page_edit.select_from_bottom_edit_menu('Opacity')
        time.sleep(2)
        pic_base = pic_after
        #page_edit.el(L.edit.opacity.slider).set_text('30')
        page_edit.opacity_set_slider(0.3)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1de7c402-45d8-4ff8-8c52-7c55dfbbfed3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('6ae2f2f1-6586-4c62-9dcb-585daed7c925')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Sticker] Flip
        pic_base = pic_after
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.flip).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Flip')
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('6ae2f2f1-6586-4c62-9dcb-585daed7c925',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('87eabab0-3222-43dd-bc92-28fc60a04e50')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Sticker] Fade
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.fade).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Fade')
        #time.sleep(1)
        #page_edit.fade.set_fade_out('OFF')
        #time.sleep(1)
        #page_edit.el(L.edit.fade.ok).click()
        time.sleep(1)
        page_edit.select_adjustment_from_bottom_edit_menu('Fade out')
        page_edit.driver.driver.back()  # for un-select title item on timeline
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('87eabab0-3222-43dd-bc92-28fc60a04e50',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('3d373113-a650-4b44-9d68-214f0c31dbd4')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        # ==================
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # [Pip - Video] ================================
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder_01) 
        page_media.select_media_by_text(media_list[2])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        # [Pip - Video] snap to boundary
        time.sleep(2)
        page_effect.snap_effect_to_boundary()
        time.sleep(2)
        self.report.new_result('3d373113-a650-4b44-9d68-214f0c31dbd4', page_effect.check_effect_snap_to_boundary())
        self.report.start_uuid('a875c023-eb37-4587-a982-87212c4527ee')
        page_effect.move_effect_to_center()
        time.sleep(2)
        # [Pip - Video] re-size
        pic_base = page_edit.get_preview_pic()
        page_effect.modify_effect_size()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('a875c023-eb37-4587-a982-87212c4527ee',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # [Pip - Video] set rotate
        self.report.start_uuid('83d4f35b-7418-4a31-a099-c696137e7d6f')
        pic_base = pic_after
        page_effect.modify_effect_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('83d4f35b-7418-4a31-a099-c696137e7d6f',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('53cda1f4-483a-4940-910e-2cb6acef70d3')
        time.sleep(1)
        # ========================
        # [Pip - Video > Sharpness]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.sharpness).click()
        time.sleep(2)
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
        default_value = int(page_edit.sharpness_effect.sharpness.get_number())
        #default_value = page_edit.el(L.edit.sharpness.value).text
        self.report.new_result('53cda1f4-483a-4940-910e-2cb6acef70d3', True if default_value == 0 else False)
        self.report.start_uuid('d4e58999-3ccb-4ca0-ac5d-0c7d23788304')
        self.report.new_result('d4e58999-3ccb-4ca0-ac5d-0c7d23788304', True if default_value == 0 else False)
        self.report.start_uuid('c88bb452-fc7b-476a-8726-88bcdae8aba7')
        self.report.start_uuid('ac24d927-6e5f-4bcb-9638-90774f6f2650')
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.sharpness.sharpness_level).set_text('100')
        page_edit.sharpness_effect.sharpness.set_progress(1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('c88bb452-fc7b-476a-8726-88bcdae8aba7', result, 'DRA197426-0020')
        self.report.new_result('ac24d927-6e5f-4bcb-9638-90774f6f2650', result, 'DRA197426-0020')
        self.report.start_uuid('a0751ae4-140a-4eb5-8217-dfb1bc1983bb')
        page_edit.driver.driver.back()
        time.sleep(2)
        # ========================
        # [Pip - Video > Skin Smoothener]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.skin_smoothener).click()
        page_edit.select_from_bottom_edit_menu('Skin Smoothener')
        time.sleep(2)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        result_brightness = page_edit.skin_smoothener.skin_brightness.is_number(80)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        result_smoothness = page_edit.skin_smoothener.skin_smoothness.is_number(80)
        self.report.new_result('a0751ae4-140a-4eb5-8217-dfb1bc1983bb',
                               True if result_brightness and result_smoothness else False)
        self.report.start_uuid('0ec1a886-97b7-4652-a649-fb494caa4796')
        self.report.start_uuid('454be55d-10d3-43d7-80ce-019a75b97efd')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        #page_edit.skin_smoothener.skin_brightness.set_number(50)
        page_edit.skin_smoothener.skin_brightness.set_progress(0.5)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        #page_edit.skin_smoothener.skin_smoothness.set_number(50)
        page_edit.skin_smoothener.skin_smoothness.set_progress(0.5)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('0ec1a886-97b7-4652-a649-fb494caa4796', result, 'DRA197426-0019')
        self.report.new_result('454be55d-10d3-43d7-80ce-019a75b97efd', result, 'DRA197426-0019')
        self.report.start_uuid('62edb2a4-f106-4559-9385-9288f2169c7e')
        pic_base = pic_after
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        #page_edit.skin_smoothener.skin_brightness.set_number(40)
        page_edit.skin_smoothener.skin_brightness.set_progress(0)
        page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        #page_edit.skin_smoothener.skin_smoothness.set_number(0)
        page_edit.skin_smoothener.skin_smoothness.set_progress(0)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('62edb2a4-f106-4559-9385-9288f2169c7e',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after), 'DRA197426-0019')
        self.report.start_uuid('3200ff5d-83c5-4328-9216-5793b059a3ae')
        self.report.start_uuid('a7f72371-2c7b-428f-9ce7-b6df978c10fc')
        time.sleep(1)
        page_edit.driver.driver.back()
        # ========================
        # [Pip - Video > Color Filter]
        page_edit.swipe_element(L.edit.timeline.playhead, 'left', 100)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color).click()
        page_edit.select_from_bottom_edit_menu('Filter')
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_3).click()
        page_edit.el(L.edit.color_sub.preset_sub.color_profile_8).click()
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('3200ff5d-83c5-4328-9216-5793b059a3ae', result)
        self.report.new_result('a7f72371-2c7b-428f-9ce7-b6df978c10fc', result)
        self.report.start_uuid('6006a950-6c0d-45b0-acc7-f315e6637663')
        # [Pip - Video > Chroma key]
        pic_base_timeline = page_edit.get_preview_pic()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.chroma_key).click()
        page_edit.select_from_bottom_edit_menu('Chroma Key')
        result_color_range = page_edit.chroma_key.color_range.is_enabled()
        result_denoise = page_edit.chroma_key.denoise.is_enabled()
        self.report.new_result('6006a950-6c0d-45b0-acc7-f315e6637663',
                               True if (not result_color_range) and (not result_denoise) else False)
        self.report.start_uuid('53886c8f-fb65-40eb-a3b3-88437dc983f6')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.chroma_key.btn_color_straw).click()
        time.sleep(1)
        page_edit.click_on_preview_area()
        time.sleep(1)
        page_edit.el(L.edit.chroma_key.btn_color_straw).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('53886c8f-fb65-40eb-a3b3-88437dc983f6', result)
        self.report.start_uuid('0053f5d0-31e3-4cea-8b16-ef02d1f0b83b')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        pic_after_timeline = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base_timeline, pic_after_timeline)
        self.report.new_result('0053f5d0-31e3-4cea-8b16-ef02d1f0b83b', result)
        self.report.start_uuid('abeba771-71fa-40b6-9c93-14362ede6f11')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.chroma_key).click()
        page_edit.select_from_bottom_edit_menu('Chroma Key')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        # click reset
        page_edit.el(L.edit.chroma_key.reset).click()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('abeba771-71fa-40b6-9c93-14362ede6f11', result)
        self.report.start_uuid('81f221c7-7d21-4702-8214-2138f3815f91')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # ========================
        # >> [Pip - Edit Video] Opacity
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.opacity).click()
        page_edit.select_from_bottom_edit_menu('Opacity')
        time.sleep(2)
        pic_base = pic_after
        #page_edit.el(L.edit.opacity.slider).set_text('30')
        page_edit.opacity_set_slider(0.3)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('81f221c7-7d21-4702-8214-2138f3815f91',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('4a04410a-a5eb-4100-a4ea-c066e2b7208b')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Video] Flip
        pic_base = pic_after
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.flip).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Flip')
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4a04410a-a5eb-4100-a4ea-c066e2b7208b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('e662aee3-fffa-4e8a-898d-68be5d423bae')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Video] Fade
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.fade).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Fade')
        time.sleep(1)
        #page_edit.fade.set_fade_out('OFF')
        #time.sleep(1)
        #page_edit.el(L.edit.fade.ok).click()
        #time.sleep(1)
        page_edit.select_adjustment_from_bottom_edit_menu('Fade out')
        page_edit.driver.driver.back()  # for un-select title item on timeline
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead, 'right', 200)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('e662aee3-fffa-4e8a-898d-68be5d423bae',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('15c48360-06c3-4096-baa8-66ea5b33cbdc')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        # ========================
        # >> [Pip - Video] Duplicate
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('15c48360-06c3-4096-baa8-66ea5b33cbdc',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('7e9eb203-d8cf-4013-8275-6839f0e0de3d')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # ========================
        # >> [Pip - Title] Duplicate
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        #page_media.select_media_by_text('Assembly Line')
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_effect.move_title_to_center()
        page_effect.snap_title_to_boundary()
        time.sleep(1)
        # >> >> preview in full screen
        self.report.start_uuid('288bbafa-2f93-4072-bbef-019955f703ad')
        time.sleep(2)
        page_edit.enter_fullscreen_preview()
        time.sleep(1)
        page_edit.tap_screen_center()
        self.report.new_result('288bbafa-2f93-4072-bbef-019955f703ad',
                               page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        time.sleep(8)
        self.report.start_uuid('6dd178a9-e33c-41b3-b543-96f0860ae2d3')
        self.report.new_result('6dd178a9-e33c-41b3-b543-96f0860ae2d3',
                               page_edit.is_exist(L.edit.preview.water_mark))
        # check title position
        self.report.start_uuid('696cf556-f1ce-4804-8214-36bc2dbae672')
        page_edit.el(L.edit.preview.movie_view).click()
        page_edit.el(L.edit.preview.btn_fullscreen_play_pause).click()
        time.sleep(5)
        pic_base = page_edit.get_preview_pic()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('696cf556-f1ce-4804-8214-36bc2dbae672',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        time.sleep(5)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        # =============================
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('7e9eb203-d8cf-4013-8275-6839f0e0de3d',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('29aea1ae-de34-4686-8028-83a292168daf')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # ========================
        # >> [Pip - Photo] Duplicate
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('29aea1ae-de34-4686-8028-83a292168daf',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('efbe30cd-c944-4650-bb86-4cc7f2eb84f5')
        page_edit.el(L.edit.menu.delete).click()
        # >> [Pip - Sticker] Duplicate
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.sticker).click()
        page_edit.el(L.edit.effect_sub.sticker_tabs.tab_downloaded).click()
        #page_media.select_media_by_text(media_list[1])
        page_media.select_media_by_order(5)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('efbe30cd-c944-4650-bb86-4cc7f2eb84f5',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('08c84239-5e50-40a1-89cf-34bc41622e27')
        page_edit.el(L.edit.menu.delete).click()
        # >> [Pip - Color Board] Duplicate
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.select_media_by_text('Color Board')
        #page_media.select_media_by_text(media_list[4])
        page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.duplicate).click()
        page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('08c84239-5e50-40a1-89cf-34bc41622e27',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('8631570f-ac1c-451c-818a-c9ae8d475a19')
        page_edit.el(L.edit.menu.delete).click()
        # ========================
        # >> [Pip - Color Board] Opacity
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.select_media_by_text('Color Board')
        #page_media.select_media_by_text(media_list[4])
        page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #result = page_edit.is_exist(L.edit.menu.edit)
        result = page_edit.is_exist(L.edit.edit_sub.bottom_edit_menu)
        self.report.new_result('8631570f-ac1c-451c-818a-c9ae8d475a19', result)
        self.report.start_uuid('121e7406-3945-4136-ac68-22b6e0c22c83')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.opacity).click()
        page_edit.select_from_bottom_edit_menu('Opacity')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('50')
        page_edit.opacity_set_slider(0.5)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('121e7406-3945-4136-ac68-22b6e0c22c83',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('d208f8c9-4458-4c71-ad40-44c9c5ed6fa2')
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Color Board] Color Selector
        #result = page_edit.is_exist(L.edit.menu.edit)
        result = page_edit.is_exist(L.edit.edit_sub.bottom_edit_menu)
        self.report.new_result('d208f8c9-4458-4c71-ad40-44c9c5ed6fa2', result)
        self.report.start_uuid('71506c5d-1b03-45cb-8c56-f39ee7c295f6')
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color_selector).click()
        page_edit.select_from_bottom_edit_menu('Color Selector')
        page_edit.el(L.edit.color_board.pink).click()
        page_edit.driver.driver.back()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('71506c5d-1b03-45cb-8c56-f39ee7c295f6',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('b580f3bf-dcef-4c0b-ac9d-019f9c3f1883')
        time.sleep(1)
        # =========================
        # Leave and Save project
        pic_base = page_edit.get_preview_pic()
        #page_edit.driver.driver.back()
        #time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        #page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('b580f3bf-dcef-4c0b-ac9d-019f9c3f1883',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               2).compare_image() else False)(
                                   pic_base, pic_after))

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_03_03(self):
        media_list = ['mp4.mp4', '(255, 153, 204)']
        self.report.start_uuid('feb4b80b-0104-4363-b641-df267ef96cec')
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
        # PiP Track - Color Board ===============
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.select_media_by_text('Color Board')
        #page_media.select_media_by_text(media_list[1])
        page_media.select_media_by_order(3)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        x_axis_timeline_indicator = int(page_edit.el(L.edit.timeline.playhead).rect['x'])
        self.report.new_result('feb4b80b-0104-4363-b641-df267ef96cec', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(2, 1).rect['x']) else False)
        self.report.start_uuid('276fc7ca-9f71-410e-b53d-c72143c998c8')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        # PiP Track - Title/ Photo/ Still Sticker/ Animated Sticker ===============
        # default title duration
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_edit.el(L.timeline_settings.settings.default_title_duration).click()
        time.sleep(1)
        if page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text != "5.0 s":
            page_edit.el(L.timeline_settings.default_title_duration.slider).set_text('45')  # set default as 5.0s
        time.sleep(2)
        # >> drag slider to left
        page_edit.drag_slider_from_center_to_left(L.timeline_settings.default_title_duration.slider)
        time.sleep(2)
        txt_duration = page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text
        self.report.new_result('276fc7ca-9f71-410e-b53d-c72143c998c8',
                               True if float(txt_duration.replace(' s', '')) < 5.0 else False)
        self.report.start_uuid('4fa515fd-48b9-4d88-846a-f7521ba8ee7c')
        if page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text != "5.0 s":
            page_edit.el(L.timeline_settings.default_title_duration.slider).set_text('45')  # set default as 5.0s
        time.sleep(2)
        # >> drag slider to right
        page_edit.drag_slider_from_center_to_right(L.timeline_settings.default_title_duration.slider)
        time.sleep(2)
        txt_duration = page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text
        self.report.new_result('4fa515fd-48b9-4d88-846a-f7521ba8ee7c',
                               True if float(txt_duration.replace(' s', '')) > 5.0 else False)
        # >> set default as 5.0 s
        self.report.start_uuid('358d9d00-64f4-42d8-9f6f-4eb16d17f86a')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        timeline_setting.set_default_title_duration('5.0')
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        time.sleep(2)
        #page_media.select_media_by_text('Assembly Line')
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        # >> check preview frame
        # self.report.start_uuid('358d9d00-64f4-42d8-9f6f-4eb16d17f86a')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        time.sleep(6)
        self.report.new_result('358d9d00-64f4-42d8-9f6f-4eb16d17f86a',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('2f198c98-1106-4bef-a80b-69115a327d0c')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> set default as 0.5 s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(1)
        timeline_setting.set_default_title_duration('0.5')
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        time.sleep(2)
        #page_media.select_media_by_text('Assembly Line')
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        # >> check preview frame
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('2f198c98-1106-4bef-a80b-69115a327d0c',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('4295c2f3-2d4f-4303-a3c8-9e1654e6d7a4')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> set default as 10.0 s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(1)
        timeline_setting.set_default_title_duration('10.0')
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        time.sleep(2)
        #page_media.select_media_by_text('Assembly Line')
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        # >> check preview frame
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(4)
        pic_after = page_edit.get_preview_pic()
        time.sleep(10)
        self.report.new_result('4295c2f3-2d4f-4303-a3c8-9e1654e6d7a4',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('e247d8f6-8227-470a-97a7-289116f018b0')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead, "left", 200)
        time.sleep(1)
        # PiP - Photo by Camera
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.get_picture_from_camera()
        time.sleep(1)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(1)
        x_axis_timeline_indicator = int(page_edit.el(L.edit.timeline.playhead).rect['x'])
        self.report.new_result('e247d8f6-8227-470a-97a7-289116f018b0', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(2, 2).rect['x']) else False)
        page_edit.timeline_select_item_by_index_on_track(2, 2)
        time.sleep(1)
        # PiP - Sticker (still/ animated)
        self.report.start_uuid('bafbcbd4-c851-4d69-9c7d-1be04c7883d7')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead, "left", 400)
        time.sleep(1)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.sticker).click()
        page_edit.el(L.edit.effect_sub.sticker_tabs.tab_downloaded).click()
        #page_media.select_media_by_text('Photoframe 05')
        page_media.select_media_by_order(2)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        x_axis_timeline_indicator = int(page_edit.el(L.edit.timeline.playhead).rect['x'])
        self.report.new_result('bafbcbd4-c851-4d69-9c7d-1be04c7883d7', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(2, 3).rect['x']) else False)
        self.report.start_uuid('57787893-f40c-45dd-b7f8-630a9ae07e25')
        time.sleep(1)
        #page_media.select_media_by_text('Like')
        page_media.select_media_by_order(5)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        x_axis_timeline_indicator = int(page_edit.el(L.edit.timeline.playhead).rect['x'])
        self.report.new_result('57787893-f40c-45dd-b7f8-630a9ae07e25', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(3, 1).rect['x']) else False)

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_03_04(self):
        custom_font_list = ['AiDeep.otf', 'HuaKangTiFan-CuTi-1.ttf']
        self.report.start_uuid('8256d362-f080-4a96-b5a2-b730175ddb9a')
        self.report.start_uuid('5e6f436e-0aee-4405-8bf9-d35c0ae78df9')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        result_import_custom_font = page_main.import_custom_font_list(pdr_package, custom_font_list)
        self.report.new_result('8256d362-f080-4a96-b5a2-b730175ddb9a', result_import_custom_font)
        self.report.new_result('5e6f436e-0aee-4405-8bf9-d35c0ae78df9', result_import_custom_font)
        # create existed 9_16 project
        self.report.start_uuid('84d14d23-702e-4845-b5a8-1206aae196d7')
        self.report.start_uuid('51980f3e-3ac7-467f-9a60-a358950ed67e')
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        # select Assembly Line to add timeline
        #page_media.select_media_by_text('Assembly Line')
        page_media.select_media_by_text('Default')
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        # page_edit.force_uncheck_help_enable_tip_to_Leave()
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.title).click()
        page_edit.select_from_bottom_edit_menu('Title Designer')
        time.sleep(2)
        page_edit.title_designer.set_custom_font_by_name('HuaKangTiFan-CuTi-1')
        time.sleep(1)
        result_font_name_huakang = True if page_edit.el(
            L.edit.title_designer.btn_font).text == 'HuaKangTiFan-CuTi-1' else False
        page_edit.driver.driver.back()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result_preview_huakang = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.title).click()
        page_edit.select_from_bottom_edit_menu('Title Designer')
        pic_base = pic_after
        page_edit.title_designer.set_custom_font_by_name('AiDeep Bold', 'No')
        time.sleep(1)
        result_font_name_aideep = True if page_edit.el(
            L.edit.title_designer.btn_font).text == 'AiDeep Bold' else False
        page_edit.driver.driver.back()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        time.sleep(2)
        result_preview_aideep = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                    5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('84d14d23-702e-4845-b5a8-1206aae196d7',
                               True if result_font_name_huakang and result_font_name_aideep else False)
        self.report.new_result('51980f3e-3ac7-467f-9a60-a358950ed67e',
                               True if result_preview_huakang and result_preview_aideep else False)

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_03_03_05(self):
        media_list = ['mp4.mp4']
        self.report.start_uuid('edb1e2f8-9ec1-4e3e-8523-5f21a75caa47')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 9_16 project
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_media.driver.driver.back()
        time.sleep(2)
        #elm = page_edit.timeline_get_item_by_index_on_track(1, 1, 'title')
        #self.report.new_result('edb1e2f8-9ec1-4e3e-8523-5f21a75caa47', True if elm.text == media_list[0] else False)
        self.report.new_result('edb1e2f8-9ec1-4e3e-8523-5f21a75caa47', page_media.select_media_by_text('Video Capture'))
        #self.report.start_uuid('30676737-13ec-403e-bb66-3903be9a20b9')
        page_media.get_video_from_camera()
        time.sleep(1)
        page_media.click(L.import_media.library_gridview.add)
        #self.report.new_result('30676737-13ec-403e-bb66-3903be9a20b9', page_edit.is_exist(L.ad.dialog_title))
