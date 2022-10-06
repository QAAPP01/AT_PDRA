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


class Test_SFT_Scenario_02_03:
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

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_01(self):
        video_list = ['mp4.mp4']
        self.report.start_uuid('4f38b72e-6424-40dc-adec-fe50681b6bdc')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        self.report.new_result('4f38b72e-6424-40dc-adec-fe50681b6bdc',
                               page_edit.check_preview_aspect_ratio(project_title))
        self.report.start_uuid('30281dfe-de3b-4809-9dcd-469ce0741ecf')
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        # select Title to add timeline
        # page_media.select_media_by_text('Default')
        time.sleep(5)
        page_media.select_title_by_order(1)
        time.sleep(3)
        page_media.el(L.import_media.library_gridview.add).click()
        # verify if add to effect track#1
        result_add_clip = True if page_edit.el(L.edit.timeline.playhead).rect['x'] < page_edit.timeline_get_item_by_index_on_track(2, 1).rect['x'] else False
        self.report.new_result('30281dfe-de3b-4809-9dcd-469ce0741ecf', result_add_clip)
        self.report.start_uuid('a0c00987-cc01-4dde-a89f-02c6db3b070a')
        self.report.start_uuid('43086874-7083-4095-abb5-63ba0e25ed2e')
        # page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        result_check_edit_btn = (True if page_edit.is_exist(L.edit.preview.btn_title_designer_right_top) else False)
        self.report.new_result('a0c00987-cc01-4dde-a89f-02c6db3b070a', result_check_edit_btn)
        # font face ================================
        self.report.new_result('43086874-7083-4095-abb5-63ba0e25ed2e', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('dcdb1941-2d1b-4529-9a81-36a29e288409')
        # page_edit.el(L.edit.preview.btn_title_designer_right_top).click()
        page_edit.select_from_bottom_edit_menu("Designer")
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('dcdb1941-2d1b-4529-9a81-36a29e288409',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        # font face switch is removed in new Title Designer (9.3.0)
        self.report.start_uuid('98edd595-0f13-4568-a945-3e602d81f9be')
        self.report.start_uuid('51b7c152-bad9-45a3-9135-f82e29178f3f')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('98edd595-0f13-4568-a945-3e602d81f9be',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.new_result('51b7c152-bad9-45a3-9135-f82e29178f3f', result_check_edit_btn)  # check edit btn
        # set font
        self.report.start_uuid('7cac1827-6e96-4e11-9d11-6a9ffdfb8b90')
        self.report.start_uuid('9d686df8-6249-40d6-8c71-0fff28af0586')
        pic_base = pic_after
        page_edit.title_designer.set_font_by_index(2)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('7cac1827-6e96-4e11-9d11-6a9ffdfb8b90',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.new_result('9d686df8-6249-40d6-8c71-0fff28af0586', result_check_edit_btn)  # check edit btn

        # red color
        self.report.start_uuid('4568faa0-4a02-4b2a-89fc-0fd151d86769')
        self.report.start_uuid('e5350c05-8659-4ad1-8050-ee466d01aec3')
        pic_base = pic_after
        page_edit.click(L.edit.title_designer.btn_edit_face)
        time.sleep(3)
        page_edit.title_designer.select_color_by_order(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4568faa0-4a02-4b2a-89fc-0fd151d86769',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.new_result('e5350c05-8659-4ad1-8050-ee466d01aec3', result_check_edit_btn)  # check edit btn
        # Set opacity
        self.report.start_uuid('5ffee8b6-4f65-41df-b9a9-26794dc17ffb')
        self.report.start_uuid('bdcb120c-22eb-44fe-bb6a-c0e1a01dffc2')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
        page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 1)
        self.report.new_result('5ffee8b6-4f65-41df-b9a9-26794dc17ffb', result)
        self.report.new_result('bdcb120c-22eb-44fe-bb6a-c0e1a01dffc2', result)

        # Color Selector
        self.report.start_uuid('e4cacd8c-9bd7-4ae2-9179-eb5f9284da34')
        page_edit.title_designer.select_color_by_order(1)
        time.sleep(3)
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('e4cacd8c-9bd7-4ae2-9179-eb5f9284da34', result)

        self.report.start_uuid('60bb63d7-561e-4900-b695-474ceffbdc55')
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('60bb63d7-561e-4900-b695-474ceffbdc55', result)

        self.report.start_uuid('8633c2b9-338f-46c2-a2b3-14d8dc0dbeff')
        result = page_edit.title_designer.select_color_dropper(0.5, 0.1)
        self.report.new_result('8633c2b9-338f-46c2-a2b3-14d8dc0dbeff', result)

        self.report.start_uuid('1d21a49d-7baa-4a7c-ad6f-5c4f1888de04')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1d21a49d-7baa-4a7c-ad6f-5c4f1888de04',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('16b24cbe-ce7d-4921-8382-0aa5d73de1be')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('green', 250)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('16b24cbe-ce7d-4921-8382-0aa5d73de1be',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('468007a4-2af1-4e9c-ad86-5befb398790b')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        time.sleep(5)
        page_edit.driver.driver.back()
        self.report.new_result('468007a4-2af1-4e9c-ad86-5befb398790b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        # Set Gradient color
        self.report.start_uuid('84cbf64f-23bd-44b6-bef6-9f211b12dceb')
        page_edit.click(L.edit.title_designer.tab_gradient)
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(4)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('84cbf64f-23bd-44b6-bef6-9f211b12dceb',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('6f499a07-f505-4e26-a63b-466be691ed42')
        self.report.start_uuid('30f297bc-8c58-4e11-b4d8-e7bdaa5d7e71')
        page_edit.title_designer.select_color_by_order(1)
        time.sleep(3)
        page_edit.click(L.edit.title_designer.colorpicker.second_color)
        time.sleep(3)
        result = page_edit.title_designer.set_hue_slider(0.5)
        self.report.new_result('6f499a07-f505-4e26-a63b-466be691ed42', result)
        self.report.new_result('30f297bc-8c58-4e11-b4d8-e7bdaa5d7e71', result)

        self.report.start_uuid('a9f229b8-8774-45d6-8087-5f8230fecf8e')
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('a9f229b8-8774-45d6-8087-5f8230fecf8e', result)

        self.report.start_uuid('a44a2d86-e943-4b8f-be43-677722ac0c04')
        self.report.start_uuid('b5410134-8379-465c-b963-d1f50a8ddf8d')
        page_edit.click(L.edit.title_designer.colorpicker.first_color)
        result = page_edit.title_designer.select_color_dropper(0.1, 0.1)
        self.report.new_result('a44a2d86-e943-4b8f-be43-677722ac0c04', result)
        self.report.new_result('b5410134-8379-465c-b963-d1f50a8ddf8d', result)

        self.report.start_uuid('60fe0313-c235-44e4-a405-6b3fedffa1c5')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('60fe0313-c235-44e4-a405-6b3fedffa1c5',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('75d76f2f-c3a6-403e-bd80-e9f3f6863a91')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('green', 250)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('75d76f2f-c3a6-403e-bd80-e9f3f6863a91',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('5e652f46-4c4f-4863-8dd8-7fe08c3c349b')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        page_edit.driver.driver.back()
        self.report.new_result('5e652f46-4c4f-4863-8dd8-7fe08c3c349b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('4ef1e75e-f181-4039-9132-36cfc90bf49d')
        self.report.start_uuid('e7418914-e39f-4d6e-ad5b-73dfae38ffef')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_angle, 1)
        self.report.new_result('4ef1e75e-f181-4039-9132-36cfc90bf49d', result)
        self.report.new_result('e7418914-e39f-4d6e-ad5b-73dfae38ffef', result)

        self.report.start_uuid('40c98844-cfd7-4700-b9ab-7e00db1960eb')
        self.report.start_uuid('8fee8a51-4b40-4176-92c3-552009ef965c')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_transition, 0.3)
        self.report.new_result('40c98844-cfd7-4700-b9ab-7e00db1960eb', result)
        self.report.new_result('8fee8a51-4b40-4176-92c3-552009ef965c', result)

        self.report.start_uuid('c9b3365b-67d7-48ef-bca5-f3c297ee2884')
        self.report.start_uuid('c956d7bb-29d6-4412-9f48-57e184d6ad6b')
        page_edit.title_designer.swipe_slider_area('up')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
        self.report.new_result('c9b3365b-67d7-48ef-bca5-f3c297ee2884', result)
        self.report.new_result('c956d7bb-29d6-4412-9f48-57e184d6ad6b', result)


        # Character type : Bold (default: Normal) ================================
        self.report.start_uuid('b5536be6-2187-41ec-b17f-57634ff03f64')
        self.report.start_uuid('d598cb02-ecb4-4d41-afd7-10e77b965b29')
        pic_base = pic_after
        page_edit.click(L.edit.title_designer.btn_format)
        time.sleep(5)
        page_edit.title_designer.set_font_bold('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('b5536be6-2187-41ec-b17f-57634ff03f64',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        # Character type : Italic
        self.report.new_result('d598cb02-ecb4-4d41-afd7-10e77b965b29', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('ce7556d2-2909-4fc2-ab47-a30fca6a8708')
        self.report.start_uuid('1d8c0c80-de39-4ef6-a23e-c9065a9efa22')
        pic_base = pic_after
        page_edit.title_designer.set_font_bold('OFF')
        page_edit.title_designer.set_font_italic('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('ce7556d2-2909-4fc2-ab47-a30fca6a8708',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        # Character type : Bold+Italic
        self.report.new_result('1d8c0c80-de39-4ef6-a23e-c9065a9efa22', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('ae44a2b6-e559-415e-a401-c33f064e7e63')
        self.report.start_uuid('a6f8fedc-40e5-4834-9bb1-c6fec71e6603')
        pic_base = pic_after
        page_edit.title_designer.set_font_bold('ON')
        page_edit.title_designer.set_font_italic('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('ae44a2b6-e559-415e-a401-c33f064e7e63',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        # Character type : Normal
        self.report.new_result('a6f8fedc-40e5-4834-9bb1-c6fec71e6603', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('78de6b49-a0b8-4e5f-9fcf-662ccf558fa6')
        pic_base = pic_after
        page_edit.title_designer.set_font_bold('OFF')
        page_edit.title_designer.set_font_italic('OFF')
        page_edit.driver.driver.back()
        # page_edit.exist_click(L.edit.try_before_buy.remove)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('78de6b49-a0b8-4e5f-9fcf-662ccf558fa6',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        # modify title text
        self.report.start_uuid('e9bac74a-e5f1-4124-ae7c-816772dd9887')
        self.report.start_uuid('23ce0171-c8d6-4504-8fd8-f3953a52e56e')
        self.report.start_uuid('1057da8e-71d7-4fe6-a595-c57b2315f0d5')
        page_edit.el(L.edit.title_designer.title_object).click()
        self.report.new_result('23ce0171-c8d6-4504-8fd8-f3953a52e56e', page_edit.is_exist(L.edit.title_designer.title_text_edit_area))
        page_edit.el(L.edit.title_designer.title_text_edit_area).set_text('CyberLink\ntest')
        self.report.new_result('1057da8e-71d7-4fe6-a595-c57b2315f0d5', True if page_edit.el(L.edit.title_designer.title_text_edit_area).text == 'CyberLink\ntest' else False)
        page_edit.el(L.edit.title_designer.title_text_edit_confirm).click()
        # Align to Mid
        self.report.new_result('e9bac74a-e5f1-4124-ae7c-816772dd9887', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('1e3ee0d0-b048-46a1-8236-996bf2c1cbfa')
        self.report.start_uuid('c9f0c09e-85d1-4097-bf33-c9eb1a4cd91e')
        page_edit.select_from_bottom_edit_menu("Designer")
        time.sleep(5)
        page_edit.click(L.edit.title_designer.btn_format)
        time.sleep(5)
        pic_base = pic_after
        # page_edit.el(L.edit.preview.btn_title_designer_right_top).click()
        page_edit.el(L.edit.title_designer.align_center).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1e3ee0d0-b048-46a1-8236-996bf2c1cbfa',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Align to Left
        self.report.new_result('c9f0c09e-85d1-4097-bf33-c9eb1a4cd91e', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('dd724b40-2646-43fd-9002-c5476fac90db')
        self.report.start_uuid('d437dc97-9ddd-4f9f-891b-64c5e953197f')
        pic_base = pic_after
        page_edit.el(L.edit.title_designer.align_left).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('dd724b40-2646-43fd-9002-c5476fac90db',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Align to Right
        self.report.new_result('d437dc97-9ddd-4f9f-891b-64c5e953197f', result_check_edit_btn)  # check edit btn
        self.report.start_uuid('aca42450-7d2e-4441-a970-a2fa754fca12')
        pic_base = pic_after
        page_edit.el(L.edit.title_designer.align_right).click()
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('aca42450-7d2e-4441-a970-a2fa754fca12',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))

        # Title Designer - Border ================================
        self.report.start_uuid('eef88152-bf69-4382-9e00-e08a7f8222a3')
        page_edit.el(L.edit.title_designer.btn_edit_bolder).click()
        # default_border_setting = True if (page_edit.el(L.edit.title_designer.switch_border).get_attribute('checked') == 'true') and (page_edit.el(L.edit.title_designer.border_size_text).text == '0.0') else False
        default_border_setting = None
        # Border - 4.0, White
        self.report.new_result('eef88152-bf69-4382-9e00-e08a7f8222a3', default_border_setting)
        self.report.start_uuid('96ee8805-cadc-4fdb-b94f-c140b2418ee4')
        self.report.start_uuid('ecb22131-6c36-42f2-9132-5feec2b6afec')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_size, 0.8)
        self.report.new_result('96ee8805-cadc-4fdb-b94f-c140b2418ee4', result)
        # Border - OFF (default: ON)
        self.report.new_result('ecb22131-6c36-42f2-9132-5feec2b6afec', default_border_setting)
        self.report.start_uuid('66dcfce4-562d-4c78-829d-0c97ed6afa7f')
        self.report.start_uuid('bce60bf0-0713-4ca5-87eb-4a58850f9623')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('66dcfce4-562d-4c78-829d-0c97ed6afa7f',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Border - ON
        self.report.new_result('bce60bf0-0713-4ca5-87eb-4a58850f9623', default_border_setting)
        self.report.start_uuid('5365cb35-1918-4e94-b94b-31ae3d973aa4')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('5365cb35-1918-4e94-b94b-31ae3d973aa4',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))


        # Title Designer - Border 2================================
        self.report.start_uuid('34f1f653-a245-46c6-a18e-14ec31352365')
        page_edit.el(L.edit.title_designer.tab_border2).click()
        # default_border_setting = True if (page_edit.el(L.edit.title_designer.switch_border).get_attribute('checked') == 'true') and (page_edit.el(L.edit.title_designer.border_size_text).text == '0.0') else False
        default_border_setting = None
        # Border - 4.0, White
        self.report.new_result('34f1f653-a245-46c6-a18e-14ec31352365', default_border_setting)
        self.report.start_uuid('2e214a20-6d78-4734-81db-8b8f501b5459')
        self.report.start_uuid('5e1fa326-da1d-42e2-a351-922299bbca44')
        page_edit.title_designer.select_color_by_order(3)
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_size, 0.8)
        self.report.new_result('2e214a20-6d78-4734-81db-8b8f501b5459', result)
        # Border - OFF
        self.report.new_result('5e1fa326-da1d-42e2-a351-922299bbca44', default_border_setting)
        self.report.start_uuid('cf26f32e-fce8-42e7-bab6-6e4a0518b76a')
        self.report.start_uuid('245a95a0-8d59-4f96-87c2-79eeeb7acd6d')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('cf26f32e-fce8-42e7-bab6-6e4a0518b76a',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Border - ON
        self.report.new_result('245a95a0-8d59-4f96-87c2-79eeeb7acd6d', default_border_setting)
        self.report.start_uuid('03e73596-e74c-4bbc-867d-d37915a85b99')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('03e73596-e74c-4bbc-867d-d37915a85b99',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))



        # Title Designer - Shadow ================================
        self.report.start_uuid('baf9362d-289c-4ed0-a422-a3c466bdf078')
        page_edit.el(L.edit.title_designer.btn_edit_shadow).click()
        self.report.new_result('baf9362d-289c-4ed0-a422-a3c466bdf078', True if (page_edit.el(L.edit.title_designer.switch_fill_shadow).get_attribute('enabled') == 'false')
                                else False)
        #Shadow - ON (default: OFF) w/ black color (default)
        self.report.start_uuid('9a732f1a-b296-48cb-b7a4-1832968fd943')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.select_color_by_order(4)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9a732f1a-b296-48cb-b7a4-1832968fd943',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Shadow - OFF
        self.report.start_uuid('841b0885-cadd-49e2-beb7-c48b651d527d')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(0)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('841b0885-cadd-49e2-beb7-c48b651d527d',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        #Shadow - 3.0, Red
        self.report.start_uuid('f07978fd-733d-431b-96df-ebc249f473af')
        pic_base = pic_after
        page_edit.title_designer.select_color_by_order(1)
        page_edit.title_designer.set_RGB_number('red', 255)
        page_edit.title_designer.set_RGB_number('green', 0)
        page_edit.title_designer.set_RGB_number('blue', 0)
        page_edit.driver.driver.back()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('f07978fd-733d-431b-96df-ebc249f473af',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Fill Shadow - ON
        self.report.start_uuid('0ae156ae-8236-463b-8999-80bd0228abd9')
        pic_base = pic_after
        page_edit.title_designer.set_fill_shadow('ON')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0ae156ae-8236-463b-8999-80bd0228abd9',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # Fill Shadow - OFF
        self.report.start_uuid('1b4e2634-007f-4a87-9e86-bd5a2ab57097')
        pic_base = pic_after
        page_edit.title_designer.set_fill_shadow('OFF')
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1b4e2634-007f-4a87-9e86-bd5a2ab57097',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))

        # Shadow sliders
        self.report.start_uuid('76472c6d-b081-49f9-9d78-72fb4a23208d')
        self.report.start_uuid('d20cbe81-c267-4e86-b33a-664217a4bc83')
        page_edit.title_designer.swipe_slider_area('up')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_blur, 0)
        self.report.new_result('76472c6d-b081-49f9-9d78-72fb4a23208d', result)
        self.report.new_result('d20cbe81-c267-4e86-b33a-664217a4bc83', result)
        self.report.start_uuid('fcbb3be6-dff3-4706-9d79-b1e9a8a0d570')
        self.report.start_uuid('b2b2880b-ec6b-4d20-8da6-7d7bfe554561')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_distance, 0.9)
        self.report.new_result('fcbb3be6-dff3-4706-9d79-b1e9a8a0d570', result)
        self.report.new_result('b2b2880b-ec6b-4d20-8da6-7d7bfe554561', result)
        self.report.start_uuid('335adaf3-da0d-452b-8da3-3d324f3a2cee')
        self.report.start_uuid('c6da7cbd-d484-4f23-b743-7e49aa92bd5f')
        page_edit.title_designer.swipe_slider_area('up')
        result = page_edit.title_designer.set_slider(L.edit.title_designer.slider_opacity, 0.5)
        self.report.new_result('335adaf3-da0d-452b-8da3-3d324f3a2cee', result)
        self.report.new_result('c6da7cbd-d484-4f23-b743-7e49aa92bd5f', result)

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_02(self):
        self.report.start_uuid('544837ac-690e-4897-a749-afa8c672b448')
        media_list = ['png.png', 'Like', '01_static.mp4', 'mp4.mp4', '(255, 153, 204)']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_effect = PageFactory().get_page_object("effect", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # page_produce = PageFactory().get_page_object("produce", self.driver)
        #page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        #set title duration to 5 sec
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_edit.settings.swipe_to_option('Information')
        timeline_settings.set_default_title_duration('5.0')
        time.sleep(2)
        page_edit.driver.driver.back()
        time.sleep(2)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        # select Assembly Line to add timeline
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_media.select_media_by_text('Assembly Line')
        # page_media.select_media_by_text('Default')
        page_media.select_title_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        # [Pip - Title] snap to boundary
        time.sleep(2)
        page_effect.snap_title_to_boundary()
        time.sleep(2)
        result_snap = page_effect.check_title_snap_to_boundary()
        self.report.new_result('544837ac-690e-4897-a749-afa8c672b448', result_snap)
        self.report.start_uuid('4570b556-1b73-4cb6-8879-321954de28c1')
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
        self.report.new_result('4570b556-1b73-4cb6-8879-321954de28c1', result_resize)
        self.report.new_result('d7f358a6-7f6c-4a9c-95f6-dafa93163e77', True if result_snap and result_resize else False)
        self.report.start_uuid('5ced416a-b596-4320-b1c2-e74b2451f947')
        # [Pip - Title] set rotate
        pic_base = pic_after
        page_effect.modify_title_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('5ced416a-b596-4320-b1c2-e74b2451f947',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('d597e7da-ec2d-499b-8782-de57a02ab207')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(2)
        # [Pip - Photo] ================================
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        time.sleep(5)
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        # [Pip - Photo] snap to boundary
        time.sleep(2)
        page_effect.snap_effect_to_boundary()
        time.sleep(2)
        self.report.new_result('d597e7da-ec2d-499b-8782-de57a02ab207', page_effect.check_effect_snap_to_boundary())
        self.report.start_uuid('147665ed-4e97-4318-9d58-0d7dd0a04857')
        page_effect.move_effect_to_center()
        time.sleep(2)
        # [Pip - Photo] re-size
        pic_base = page_edit.get_preview_pic()
        page_effect.modify_effect_size()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('147665ed-4e97-4318-9d58-0d7dd0a04857',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('0bc1b127-0ae2-455e-9986-5cf207274d98')
        # [Pip - Photo] set rotate
        pic_base = pic_after
        page_effect.modify_effect_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0bc1b127-0ae2-455e-9986-5cf207274d98',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('3343fcf5-de42-44aa-a16a-51b032c9a7a0')
        time.sleep(1)
        # ========================
        # [Pip - Photo > Sharpness]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.sharpness).click()
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
        default_value = int(page_edit.sharpness_effect.sharpness.get_number())
        logger(f"default_value get_number = {default_value}")
        self.report.new_result('3343fcf5-de42-44aa-a16a-51b032c9a7a0', True if default_value == 0 else False)
        self.report.start_uuid('06268258-b261-4f27-b53b-2cc0d8579e08')
        pic_base = page_edit.get_preview_pic()
        page_edit.sharpness_effect.sharpness.set_progress(1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('06268258-b261-4f27-b53b-2cc0d8579e08', result)
        self.report.start_uuid('bcc8591f-3caa-44aa-9647-30c23080cd46')
        self.report.start_uuid('935861a1-c839-4db0-9c80-e6dbf337244e')
        self.report.start_uuid('1d6bf350-11c2-4ffa-8f63-845d274e11a1')
        page_edit.driver.driver.back()
        time.sleep(2)
        # ========================
        # [Pip - Photo > Skin Smoothener]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.skin_smoothener).click()
        page_edit.select_from_bottom_edit_menu('Skin Smoothener')
        time.sleep(2)
        pic_base = page_edit.get_preview_pic()
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
        result_brightness = page_edit.skin_smoothener.skin_brightness.is_number(80)
        page_edit.skin_smoothener.skin_brightness.set_progress(0.5)
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        page_edit.select_adjustment_from_bottom_edit_menu('Smoothness')
        result_smoothness = page_edit.skin_smoothener.skin_smoothness.is_number(80)
        page_edit.skin_smoothener.skin_smoothness.set_progress(0.5)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('bcc8591f-3caa-44aa-9647-30c23080cd46',
                               True if result_brightness and result_smoothness else False)
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base, pic_after)
        self.report.new_result('935861a1-c839-4db0-9c80-e6dbf337244e', result)
        self.report.new_result('1d6bf350-11c2-4ffa-8f63-845d274e11a1', result)
        self.report.start_uuid('0ef7bf8b-0c98-4ed9-92d0-ee08cf3618f7')
        pic_base = pic_after
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
        #page_edit.skin_smoothener.skin_brightness.set_number(40)
        page_edit.skin_smoothener.skin_brightness.set_progress(0)
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        page_edit.select_adjustment_from_bottom_edit_menu('Smoothness')
        #page_edit.skin_smoothener.skin_smoothness.set_number(0)
        page_edit.skin_smoothener.skin_smoothness.set_progress(0)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('0ef7bf8b-0c98-4ed9-92d0-ee08cf3618f7',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('99e389f3-4a71-423f-93ae-55a6316edf95')
        self.report.start_uuid('51294588-5fae-49ce-aeb1-fe6c33d9d3c0')
        time.sleep(1)
        page_edit.driver.driver.back()
        # ========================
        # [Pip - Photo > Color Filter]
        page_edit.swipe_element(L.edit.timeline.playhead, 'left', 100)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(3)
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
        self.report.new_result('99e389f3-4a71-423f-93ae-55a6316edf95', result)
        self.report.new_result('51294588-5fae-49ce-aeb1-fe6c33d9d3c0', result)
        self.report.start_uuid('ae333b51-5048-4cea-9e9f-2baf20fcb65a')
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
        self.report.new_result('ae333b51-5048-4cea-9e9f-2baf20fcb65a',
                               True if (not result_color_range) and (not result_denoise) else False)
        self.report.start_uuid('03aaaef8-846a-42db-8ec3-8bea9bde24da')
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
        self.report.new_result('03aaaef8-846a-42db-8ec3-8bea9bde24da', result)
        self.report.start_uuid('54d3ee25-ba6a-4d63-98b2-33dbcc6c614a')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        pic_after_timeline = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base_timeline, pic_after_timeline)
        self.report.new_result('54d3ee25-ba6a-4d63-98b2-33dbcc6c614a', result)
        self.report.start_uuid('ea8579a7-30ae-420d-8c36-f8682ef48dfa')
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
        self.report.new_result('ea8579a7-30ae-420d-8c36-f8682ef48dfa', result)
        self.report.start_uuid('09170834-5455-48a8-bb69-6123a97cf141')
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
        self.report.new_result('09170834-5455-48a8-bb69-6123a97cf141',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('46ff7639-641f-4058-bb90-d4bc3fb6c25e')
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
        self.report.new_result('46ff7639-641f-4058-bb90-d4bc3fb6c25e',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('d1120197-78ed-450f-b34f-bf4d840b031b')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Photo] Fade
        page_edit.swipe_element(L.edit.timeline.clip, "right", 500)
        time.sleep(1)
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
        page_edit.select_adjustment_from_bottom_edit_menu('Fade out')
        time.sleep(1)
        page_edit.driver.driver.back() # for un-select title item on timeline
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('d1120197-78ed-450f-b34f-bf4d840b031b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('3007a8f5-d240-4a12-bba0-99fac33461b2')
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
        time.sleep(2)
        page_effect.snap_effect_to_boundary()
        time.sleep(2)
        self.report.new_result('3007a8f5-d240-4a12-bba0-99fac33461b2', page_effect.check_effect_snap_to_boundary())
        self.report.start_uuid('14dbe4ce-d7ab-4038-b78a-e348aa386a67')
        page_effect.move_effect_to_center()
        time.sleep(2)
        # [Pip - Sticker] re-size
        pic_base = page_edit.get_preview_pic()
        page_effect.modify_effect_size()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('14dbe4ce-d7ab-4038-b78a-e348aa386a67',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('dab0c276-9f53-414d-81da-12c05b624101')
        # [Pip - Sticker] set rotate
        pic_base = pic_after
        page_effect.modify_effect_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('dab0c276-9f53-414d-81da-12c05b624101',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('2265fb50-d713-43c3-aa60-4d802bfae0c2')
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
        self.report.new_result('2265fb50-d713-43c3-aa60-4d802bfae0c2',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('f4b7d8dc-0b60-416c-a8d8-7077d895de86')
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
        self.report.new_result('f4b7d8dc-0b60-416c-a8d8-7077d895de86',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('842b6e24-a642-4268-b0de-3da2ead02892')
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
        page_edit.select_adjustment_from_bottom_edit_menu('Fade out')
        time.sleep(1)
        page_edit.driver.driver.back()  # for un-select title item on timeline
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('842b6e24-a642-4268-b0de-3da2ead02892',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('8dff9f76-bdb1-4e0f-abab-a670a1ebfe32')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        # ==================
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # [Pip - Video] ================================
        # page_edit.timeline_select_item_by_index_on_track(1, 1)
        # time.sleep(1)
        # page_edit.el(L.edit.menu.delete).click()
        # time.sleep(1)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder_01)
        page_media.click(L.import_media.video_library.sort)
        page_media.click(L.import_media.video_library.sort_menu.by_name)
        page_media.click(L.import_media.video_library.sort_menu.ascending)
        page_media.driver.driver.back()
        #page_media.select_media_by_text(media_list[2])
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(2)
        # [Pip - Video] snap to boundary
        time.sleep(2)
        page_effect.snap_effect_to_boundary()
        time.sleep(2)
        self.report.new_result('8dff9f76-bdb1-4e0f-abab-a670a1ebfe32', page_effect.check_effect_snap_to_boundary())
        self.report.start_uuid('8bdf3416-957b-4849-8abf-7cca225deaca')
        page_effect.move_effect_to_center()
        time.sleep(2)
        # [Pip - Video] re-size
        pic_base = page_edit.get_preview_pic()
        page_effect.modify_effect_size()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('8bdf3416-957b-4849-8abf-7cca225deaca',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        # [Pip - Video] set rotate
        self.report.start_uuid('4d8f9c9c-80dc-4bf8-8436-a276299636e3')
        pic_base = pic_after
        page_effect.modify_effect_rotate()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4d8f9c9c-80dc-4bf8-8436-a276299636e3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('0b427be1-decb-45cd-8db5-08466127f08c')
        time.sleep(1)
        # ========================
        # [Pip - Video > Sharpness]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.sharpness).click()
        page_edit.select_from_bottom_edit_menu('Adjustment')
        page_edit.select_adjustment_from_bottom_edit_menu('Sharpness')
        default_value = int(page_edit.sharpness_effect.sharpness.get_number())
        logger(f"default_value get_number = {default_value}")
        self.report.new_result('0b427be1-decb-45cd-8db5-08466127f08c', True if default_value == 0 else False)

        self.report.start_uuid('652101c7-9180-4c3b-a06f-0cff7e24733e')
        pic_base = page_edit.get_preview_pic()
        page_edit.sharpness_effect.sharpness.set_progress(1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)
        self.report.new_result('652101c7-9180-4c3b-a06f-0cff7e24733e', result, 'DRA197426-0020')

        self.report.start_uuid('b866b7dd-3fca-4998-a074-761d57d4c8ed')
        page_edit.driver.driver.back()
        time.sleep(2)
        # ========================
        # [Pip - Video > Skin Smoothener]
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.skin_smoothener).click()
        page_edit.select_from_bottom_edit_menu('Skin Smoothener')
        time.sleep(2)
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
        result_brightness = page_edit.skin_smoothener.skin_brightness.is_number(80)
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        page_edit.select_adjustment_from_bottom_edit_menu('Smoothness')
        result_smoothness = page_edit.skin_smoothener.skin_smoothness.is_number(80)
        self.report.new_result('b866b7dd-3fca-4998-a074-761d57d4c8ed', True if result_brightness and result_smoothness else False)
        self.report.start_uuid('99a8b19c-7c96-4e6a-aaa5-501f5d2009d6')
        self.report.start_uuid('e817011f-3816-453b-9e5f-f3a3ee4adb59')
        pic_base = page_edit.get_preview_pic()
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        page_edit.skin_smoothener.skin_brightness.set_progress(0.5)
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        page_edit.select_adjustment_from_bottom_edit_menu('Smoothness')
        page_edit.skin_smoothener.skin_smoothness.set_progress(0.5)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after)
        self.report.new_result('99a8b19c-7c96-4e6a-aaa5-501f5d2009d6', result, 'DRA197426-0019')
        self.report.new_result('e817011f-3816-453b-9e5f-f3a3ee4adb59', result, 'DRA197426-0019')
        self.report.start_uuid('20bee89c-a43b-4af4-9b66-473bd28519de')
        pic_base = pic_after
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Brightness')
        page_edit.select_adjustment_from_bottom_edit_menu('Brightness')
        page_edit.skin_smoothener.skin_brightness.set_progress(0)
        # page_edit.select_adjustment_from_bottom_edit_menu('Skin Smoothness')
        page_edit.select_adjustment_from_bottom_edit_menu('Smoothness')
        page_edit.skin_smoothener.skin_smoothness.set_progress(0)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('20bee89c-a43b-4af4-9b66-473bd28519de',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after), 'DRA197426-0019')
        self.report.start_uuid('c481738f-d83d-4042-8a86-5be0cf843cee')
        self.report.start_uuid('8132e226-d166-432d-9a73-39f316404fd3')
        time.sleep(1)
        page_edit.driver.driver.back()
        # ========================
        # [Pip - Video > Color Filter]
        #page_edit.swipe_element(L.edit.timeline.playhead, 'left', 100)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(3)
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
        self.report.new_result('c481738f-d83d-4042-8a86-5be0cf843cee', result)
        self.report.new_result('8132e226-d166-432d-9a73-39f316404fd3', result)
        self.report.start_uuid('cc3d4e1c-6612-476e-9eeb-bf2dfffef082')
        # [Pip - Video > Chroma key]
        pic_base_timeline = page_edit.get_preview_pic()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.chroma_key).click()
        page_edit.select_from_bottom_edit_menu('Chroma Key')
        result_color_range = page_edit.chroma_key.color_range.is_enabled()
        result_denoise = page_edit.chroma_key.denoise.is_enabled()
        self.report.new_result('cc3d4e1c-6612-476e-9eeb-bf2dfffef082', True if (not result_color_range) and (not result_denoise) else False)
        self.report.start_uuid('2a0ae0c9-6774-42bf-92d1-2942333ae079')
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
        self.report.new_result('2a0ae0c9-6774-42bf-92d1-2942333ae079', result)
        self.report.start_uuid('0e33e169-5fb7-4c54-9b6c-ff8cf378abe1')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(2)
        pic_after_timeline = page_edit.get_preview_pic()
        result = (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                     5).compare_image() else False)(
            pic_base_timeline, pic_after_timeline)
        self.report.new_result('0e33e169-5fb7-4c54-9b6c-ff8cf378abe1', result)
        self.report.start_uuid('aed5d2c9-4bc9-4861-9c52-c89c0f1d4491')
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
        self.report.new_result('aed5d2c9-4bc9-4861-9c52-c89c0f1d4491', result)
        self.report.start_uuid('6a43958b-ea20-4c3d-aca3-af0784b1ba34')
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
        self.report.new_result('6a43958b-ea20-4c3d-aca3-af0784b1ba34',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('8763d02d-cc3e-4bd8-a0c7-0867370bf9f1')
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
        self.report.new_result('8763d02d-cc3e-4bd8-a0c7-0867370bf9f1',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('654099a3-33c8-4d57-af65-02b615c3ef7a')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Video] Fade
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.fade).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        page_edit.select_from_bottom_edit_menu('Fade')
        #time.sleep(1)
        #page_edit.fade.set_fade_out('OFF')
        #time.sleep(1)
        #page_edit.el(L.edit.fade.ok).click()
        page_edit.select_adjustment_from_bottom_edit_menu('Fade out')
        time.sleep(1)
        page_edit.driver.driver.back()  # for un-select title item on timeline
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead, 'right', 200)
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(8)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('654099a3-33c8-4d57-af65-02b615c3ef7a',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('bf4293c1-ee2c-4c57-816a-064d45aa46b6')
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
        self.report.new_result('bf4293c1-ee2c-4c57-816a-064d45aa46b6',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('c6e54077-6f7f-42dc-9d91-e19ff4b04969')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # ========================
        # >> [Pip - Title] Duplicate
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_media.select_media_by_text('Assembly Line')
        # page_media.select_media_by_text('Default')
        page_media.select_title_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        # >> >> preview in full screen
        # self.report.start_uuid('3b59910b-aaeb-47b5-998a-bc54376ec670')
        # time.sleep(2)
        # page_edit.enter_fullscreen_preview()
        # time.sleep(1)
        # page_edit.tap_screen_center()
        # self.report.new_result('3b59910b-aaeb-47b5-998a-bc54376ec670',
        #                        page_edit.is_exist(L.edit.preview.fullscreen_current_position))
        # time.sleep(8)
        # self.report.start_uuid('6baa16a2-df70-47aa-851f-53ac856ce3f3')
        # self.report.new_result('6baa16a2-df70-47aa-851f-53ac856ce3f3',
        #                        page_edit.is_exist(L.edit.preview.water_mark))
        # check title position
        # self.report.start_uuid('646c1f68-84a0-4ee5-b09a-2ac39479eb98')
        # page_edit.el(L.edit.preview.movie_view).click()
        # page_edit.el(L.edit.preview.btn_fullscreen_play_pause).click()
        # time.sleep(5)
        # pic_base = page_edit.get_preview_pic()
        # time.sleep(1)
        # pic_after = page_edit.get_preview_pic()
        # self.report.new_result('646c1f68-84a0-4ee5-b09a-2ac39479eb98',
        #                        (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
        #                                                                        5).compare_image() else False)(
        #                            pic_base, pic_after))
        # time.sleep(5)
        # page_edit.driver.driver.back()
        # time.sleep(2)
        # page_edit.timeline_select_item_by_index_on_track(2, 1)
        # time.sleep(1)
        # =============================
        pic_base = page_edit.get_preview_pic()
        # page_edit.el(L.edit.menu.edit).click()
        # page_edit.el(L.edit.edit_sub.duplicate).click()
        page_edit.select_from_bottom_edit_menu('Duplicate')
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c6e54077-6f7f-42dc-9d91-e19ff4b04969',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('3afcbb54-90b9-4b6b-9c32-a5b0d60dcb5a')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # ========================
        # >> [Pip - Photo] Duplicate
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(1)
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
        self.report.new_result('3afcbb54-90b9-4b6b-9c32-a5b0d60dcb5a',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('9d82c667-10e0-4ef7-952d-e40138883343')
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
        self.report.new_result('9d82c667-10e0-4ef7-952d-e40138883343',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('ed5ae6e9-c98f-4f24-a3ba-977b0a157ebe')
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
        self.report.new_result('ed5ae6e9-c98f-4f24-a3ba-977b0a157ebe',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                               5).compare_image() else False)(
                                   pic_base, pic_after))
        '''
        self.report.start_uuid('03f62bce-3f01-4149-adef-efb2f770a1c7')
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
        result = page_edit.is_exist(L.edit.edit_sub.bottom_edit_menu)
        self.report.new_result('03f62bce-3f01-4149-adef-efb2f770a1c7', result)
        self.report.start_uuid('f8a6a9ea-a85f-4f65-8f39-61d0f9cfde50')
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.opacity).click()
        page_edit.select_from_bottom_edit_menu('Opacity')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('50')
        page_edit.opacity_set_slider(0.5)
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('f8a6a9ea-a85f-4f65-8f39-61d0f9cfde50',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('98d2543e-b01d-4cb7-8729-70471e4b2c27')
        page_edit.driver.driver.back()
        time.sleep(1)
        # >> [Pip - Edit Color Board] Color Selector
        result = page_edit.is_exist(L.edit.edit_sub.bottom_edit_menu)
        self.report.new_result('98d2543e-b01d-4cb7-8729-70471e4b2c27', result)
        self.report.start_uuid('9c77b1bf-f657-43eb-9e6b-4a001ac006af')
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.color_selector).click()
        page_edit.select_from_bottom_edit_menu('Color Selector')
        page_edit.el(L.edit.color_board.pink).click()
        page_edit.driver.driver.back()
        time.sleep(1)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('9c77b1bf-f657-43eb-9e6b-4a001ac006af',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
       '''
        self.report.start_uuid('bf21a71d-8360-4300-8ca2-844360e5b449')
        time.sleep(1)
        # =========================
        # Leave and Save project
        pic_base = page_edit.get_preview_pic()
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        #page_main.ad.close_full_page_ad()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(1)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(10)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('bf21a71d-8360-4300-8ca2-844360e5b449',
                               (lambda pic_src, pic_dest: True if CompareImage(pic_src, pic_dest,
                                                                                   2).compare_image() else False)(
                                   pic_base, pic_after))

    # @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_03(self):
        media_list = ['mp4.mp4', '(255, 153, 204)']
        self.report.start_uuid('36063d64-1682-497d-9833-23b8b2fc5be5')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_setting = PageFactory().get_page_object("timeline_settings", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        #page_produce.ad.close_opening_ads()
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
        self.report.new_result('36063d64-1682-497d-9833-23b8b2fc5be5', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(2, 1).rect['x']) else False)
        self.report.start_uuid('a1785993-89ab-4fff-9392-558f1dba1f8b')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        page_edit.el(L.edit.menu.delete).click()
        # PiP Track - Title/ Photo/ Still Sticker/ Animated Sticker ===============
        # default title duration
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        page_edit.settings.swipe_to_option('Information')
        timeline_setting.enter_advanced_page()
        page_edit.settings.swipe_to_option('Continue Playback After Seeking')
        page_edit.el(L.timeline_settings.settings.default_title_duration).click()
        time.sleep(1)
        if page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text != "5.0 s":
            page_edit.el(L.timeline_settings.default_title_duration.slider).set_text('45')  # set default as 5.0s
        time.sleep(2)
        # >> drag slider to left
        page_edit.drag_slider_from_center_to_left(L.timeline_settings.default_title_duration.slider)
        time.sleep(2)
        txt_duration = page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text
        self.report.new_result('a1785993-89ab-4fff-9392-558f1dba1f8b',
                               True if float(txt_duration.replace(' s', '')) < 5.0 else False)
        self.report.start_uuid('819376c8-8d0b-4a4f-8272-9b1d1dd63e76')
        if page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text != "5.0 s":
            page_edit.el(L.timeline_settings.default_title_duration.slider).set_text('45')  # set default as 5.0s
        time.sleep(2)
        # >> drag slider to right
        page_edit.drag_slider_from_center_to_right(L.timeline_settings.default_title_duration.slider)
        time.sleep(2)
        txt_duration = page_edit.el(L.timeline_settings.default_title_duration.txt_duration).text
        self.report.new_result('819376c8-8d0b-4a4f-8272-9b1d1dd63e76',
                               True if float(txt_duration.replace(' s', '')) > 5.0 else False)
        # >> set default as 5.0 s
        self.report.start_uuid('22625080-9f16-4ba3-9bc7-6d6cbd5ee1c1')
        time.sleep(1)
        page_edit.driver.driver.back()
        time.sleep(1)
        timeline_setting.set_default_title_duration('5.0')
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        time.sleep(2)
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_media.select_media_by_text('Assembly Line')
        # page_media.select_media_by_text('Default')
        page_media.select_title_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(3)
        page_media.select_title_category('Classic')
        time.sleep(3)
        amount = page_edit.calculate_library_content_amount()
        self.report.new_result('22625080-9f16-4ba3-9bc7-6d6cbd5ee1c1', True if amount == 17 else False)
        # >> check preview frame
        self.report.start_uuid('4aa79f8e-ec89-4298-9ff7-a332c8af9110')
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        time.sleep(6)
        self.report.new_result('4aa79f8e-ec89-4298-9ff7-a332c8af9110',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('c1920d5d-e501-468f-8a66-8eb3723c0584')
        page_edit.el(L.edit.menu.delete).click()
        time.sleep(1)
        # >> set default as 0.5 s
        page_edit.el(L.edit.menu.timeline_setting).click()
        page_edit.el(L.edit.sub_menu.settings).click()
        time.sleep(1)
        page_edit.settings.swipe_to_option('Information')
        timeline_setting.set_default_title_duration('0.5')
        time.sleep(1)
        page_edit.driver.driver.back()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        time.sleep(2)
        #page_edit.driver.swipe_left()
        page_media.select_title_category('Classic')
        page_media.select_media_by_text('Movie - Opening 3')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        # >> check preview frame
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('c1920d5d-e501-468f-8a66-8eb3723c0584',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('345b40e7-fe5c-4ce4-b937-620046a29299')
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
        #page_edit.driver.swipe_left()
        page_media.select_title_category('Classic')
        page_media.select_media_by_text('Movie - Opening 3')
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        # >> check preview frame
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        pic_base = page_edit.get_preview_pic()
        page_edit.el(L.edit.menu.play).click()
        time.sleep(4)
        pic_after = page_edit.get_preview_pic()
        time.sleep(10)
        self.report.new_result('345b40e7-fe5c-4ce4-b937-620046a29299',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('a52b08eb-ff8c-4e3f-b4ce-9c9b788495fd')
        page_edit.driver.driver.back()
        time.sleep(1)
        page_edit.swipe_element(L.edit.timeline.playhead, "left", 200)
        time.sleep(1)
        # PiP - Photo by Camera
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.image).click()
        page_media.get_picture_from_camera()
        time.sleep(1)
        page_media.select_media_by_order(1)
        time.sleep(1)
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(1)
        x_axis_timeline_indicator = int(page_edit.el(L.edit.timeline.playhead).rect['x'])
        self.report.new_result('a52b08eb-ff8c-4e3f-b4ce-9c9b788495fd', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(2, 2).rect['x']) else False)
        page_edit.timeline_select_item_by_index_on_track(2, 2)
        time.sleep(1)
        # PiP - Sticker (still/ animated)
        self.report.start_uuid('777ea83b-8d5c-4223-aa8f-0f147655b1e3')
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
        self.report.new_result('777ea83b-8d5c-4223-aa8f-0f147655b1e3', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(2, 3).rect['x']) else False)
        self.report.start_uuid('c693f85d-82ac-4333-9e9a-aac11a028141')
        time.sleep(1)
        #page_media.select_media_by_text('Like')
        page_media.select_media_by_order(5)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        x_axis_timeline_indicator = int(page_edit.el(L.edit.timeline.playhead).rect['x'])
        self.report.new_result('c693f85d-82ac-4333-9e9a-aac11a028141', True if x_axis_timeline_indicator < int(
            page_edit.timeline_get_item_by_index_on_track(3, 1).rect['x']) else False)

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_04(self):
        custom_font_list = ['AiDeep.otf', 'HuaKangTiFan-CuTi-1.ttf']
        self.report.start_uuid('7c918b36-7420-4b3f-8d71-519212f5747d')
        self.report.start_uuid('c46fa43b-e4ec-4dd8-abd3-114f2ab43738')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        result_import_custom_font = page_main.import_custom_font_list(pdr_package, custom_font_list)
        self.report.new_result('7c918b36-7420-4b3f-8d71-519212f5747d', result_import_custom_font)
        self.report.new_result('c46fa43b-e4ec-4dd8-abd3-114f2ab43738', result_import_custom_font)
        # create existed 16_9 project
        self.report.start_uuid('9df6cc40-83ce-445a-9afa-996d8e4c8683')
        self.report.start_uuid('99c95f71-a855-47f6-b8ad-f994d792b882')
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        #page_produce.ad.close_opening_ads()
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.title).click()
        # select Assembly Line to add timeline
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_edit.driver.swipe_left()
        #page_media.select_media_by_text('Assembly Line')
        # page_media.select_media_by_text('Default')
        page_media.select_title_by_order(1)
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
        self.report.new_result('9df6cc40-83ce-445a-9afa-996d8e4c8683',
                               True if result_font_name_huakang and result_font_name_aideep else False)
        self.report.new_result('99c95f71-a855-47f6-b8ad-f994d792b882',
                               True if result_preview_huakang and result_preview_aideep else False)

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_05(self):
        media_list = ['mp4.mp4']
        self.report.start_uuid('46ba374f-003f-40f4-ac10-f533da35ff86')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        #page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder)
        #page_media.select_media_by_text(media_list[0])
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_media.driver.driver.back()
        time.sleep(2)
        #elm = page_edit.timeline_get_item_by_index_on_track(1, 1, 'title')        
        #self.report.new_result('46ba374f-003f-40f4-ac10-f533da35ff86', True if elm.text == media_list[0] else False)
        self.report.new_result('46ba374f-003f-40f4-ac10-f533da35ff86', page_media.select_media_by_text('Camera'))
        '''
        self.report.start_uuid('f4a72be9-6184-40dd-92bc-89e109b2220d')
        page_media.get_video_from_camera()
        time.sleep(1)
        page_media.click(L.import_media.library_gridview.add)
        self.report.new_result('f4a72be9-6184-40dd-92bc-89e109b2220d', page_edit.is_exist(L.ad.dialog_title))
        '''

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_05a(self):
        media_list = ['mkv.mkv']
        self.report.start_uuid('18ebb862-1dd2-11b2-8002-080027b246c3')
        #page_main = PageFactory().get_page_object("main_page", self.driver)
        #page_edit = PageFactory().get_page_object("edit", self.driver)
        #page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        #project_title = '16_9'
        #page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        #page_main.select_existed_project_by_title(project_title)
        #page_main.el(L.main.project_info.btn_edit_project).click()
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        #page_produce.ad.close_opening_ads()
        page_main.project_click_new()
        page_main.project_set_name("02_03_05a")
        page_main.project_set_16_9()
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(1)
        page_media.driver.driver.back()
        time.sleep(1)
        page_media.driver.driver.back()
        time.sleep(1)
        page_edit.check_help_enable_tip_visible()
        page_edit.force_uncheck_help_enable_tip_to_Leave(0, 0, L.edit.menu.timeline_setting, 2)
        time.sleep(1)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.blending).click()
        page_edit.select_from_bottom_edit_menu('Blending')
        result = page_edit.select_Blanding1()
        self.report.new_result('18ebb862-1dd2-11b2-8002-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8001-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('50')
        page_edit.opacity_set_slider(0.5)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8001-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-8000-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding0()
        self.report.new_result('18ebb862-1dd2-11b2-8000-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8000-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('100')
        page_edit.opacity_set_slider(1)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8000-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-8004-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding2()
        self.report.new_result('18ebb862-1dd2-11b2-8004-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8002-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('70')
        page_edit.opacity_set_slider(0.7)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8002-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-8006-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding3()
        self.report.new_result('18ebb862-1dd2-11b2-8006-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8003-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('80')
        page_edit.opacity_set_slider(0.8)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8003-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-8008-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding4()
        self.report.new_result('18ebb862-1dd2-11b2-8008-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8004-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('90')
        page_edit.opacity_set_slider(0.9)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8004-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-800a-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding5()
        self.report.new_result('18ebb862-1dd2-11b2-800a-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8005-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('50')
        page_edit.opacity_set_slider(0.5)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8005-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-800c-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding6()
        self.report.new_result('18ebb862-1dd2-11b2-800c-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8006-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('90')
        page_edit.opacity_set_slider(0.9)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8006-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-800e-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding7()
        self.report.new_result('18ebb862-1dd2-11b2-800e-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8007-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('70')
        page_edit.opacity_set_slider(0.7)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8007-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-8001-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding8()
        self.report.new_result('18ebb862-1dd2-11b2-8001-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8008-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('50')
        page_edit.opacity_set_slider(0.5)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8008-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-8003-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding9()
        self.report.new_result('18ebb862-1dd2-11b2-8003-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-8009-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('90')
        page_edit.opacity_set_slider(0.9)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-8009-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.report.start_uuid('18ebb862-1dd2-11b2-8005-080027b246c3')
        time.sleep(1)
        result = page_edit.select_Blanding10()
        self.report.new_result('18ebb862-1dd2-11b2-8005-080027b246c3', result)
        self.report.start_uuid('1a2f1587-1dd2-11b2-800a-080027b246c3')
        time.sleep(1)
        pic_base = page_edit.get_preview_pic()
        #page_edit.el(L.edit.opacity.slider).set_text('70')
        page_edit.opacity_set_slider(0.7)
        time.sleep(2)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1a2f1587-1dd2-11b2-800a-080027b246c3',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   5).compare_image() else False)(
                                   pic_base, pic_after))
        self.driver.driver.back()

    @pytest.mark.skip
    @report.exception_screenshot
    def test_sce_02_03_05b(self):
        media_list = ['24:30']
        self.report.start_uuid('18ebb862-1dd2-11b2-8007-080027b246c3')
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        #page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        # page_main.el(L.main.project_info.btn_edit_project).click()
        time.sleep(2)
        page_edit.el(L.edit.menu.effect).click()
        page_edit.el(L.edit.effect_sub.video).click()
        page_media.select_media_by_text(self.test_material_folder)
        page_media.select_media_by_text(media_list[0])
        #page_media.select_media_by_order(4)
        page_media.el(L.import_media.library_gridview.add).click()
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(1)
        #page_edit.el(L.edit.menu.edit).click()
        #page_edit.el(L.edit.edit_sub.mask).click()
        page_edit.select_from_bottom_edit_menu('Mask')
        result = page_edit.select_mask_linear()
        self.report.new_result('18ebb862-1dd2-11b2-8007-080027b246c3', result)
        self.report.start_uuid('3285d205-1dd2-11b2-8000-080027b246c3')
        time.sleep(1)
        result = page_edit.select_mask_none()
        self.report.new_result('3285d205-1dd2-11b2-8000-080027b246c3', result)
        self.report.start_uuid('18ebb862-1dd2-11b2-8009-080027b246c3')
        time.sleep(1)
        result = page_edit.select_mask_parallel()
        self.report.new_result('18ebb862-1dd2-11b2-8009-080027b246c3', result)
        self.report.start_uuid('18ebb862-1dd2-11b2-800d-080027b246c3')
        time.sleep(1)
        result = page_edit.select_mask_eclipse()
        self.report.new_result('18ebb862-1dd2-11b2-800d-080027b246c3', result)
        self.report.start_uuid('18ebb862-1dd2-11b2-800b-080027b246c3')
        time.sleep(1)
        result = page_edit.select_mask_rectangle()
        self.report.new_result('18ebb862-1dd2-11b2-800b-080027b246c3', result)
        self.driver.driver.back()
