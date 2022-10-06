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


class Test_SFT_Scenario_02_15:
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
    def test_sce_02_15_01(self):
        logger('>>> test_sce_02_15_01: Border & Shadow <<<')
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
        
        # New project
        self.report.start_uuid('600cc332-2edd-4ae0-bd31-bed76a9bc93a')
        page_main.project_click_new()
        page_main.project_set_name("sce_02_15_01")
        page_main.project_set_16_9()
        time.sleep(5)
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        page_media.switch_to_pip_video_library()
        time.sleep(5)
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_text('01_static.mp4')
        time.sleep(2)
        page_media.el(L.import_media.library_gridview.add).click()
        time.sleep(2)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Border & Shadow')
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(1)
        time.sleep(3)
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('600cc332-2edd-4ae0-bd31-bed76a9bc93a', result)

        self.report.start_uuid('ebf27a0f-6ee2-443c-b3ac-89ba2135950a')
        time.sleep(3)
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('ebf27a0f-6ee2-443c-b3ac-89ba2135950a', result)

        self.report.start_uuid('c37ed273-3c0b-4e0b-9ae2-d2393a32c312')
        result = page_edit.title_designer.select_color_dropper(0.1, 0.1)
        self.report.new_result('c37ed273-3c0b-4e0b-9ae2-d2393a32c312', result)

        self.report.start_uuid('89b40d1a-97cd-4e5d-8869-079295f7a1ad')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        page_edit.title_designer.set_RGB_number('green', 250)
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('89b40d1a-97cd-4e5d-8869-079295f7a1ad',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('47fcae5c-9c92-4e66-a1d9-fabc2c001941')
        page_edit.back()
        pic_base = page_edit.get_preview_pic()
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(0)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('47fcae5c-9c92-4e66-a1d9-fabc2c001941',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('dc7bad49-0742-45bd-a0d6-1807c8cbdc27')
        pic_base = pic_after
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('dc7bad49-0742-45bd-a0d6-1807c8cbdc27',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('790a2094-a0a3-442c-9e0f-c5308025bcbd')
        result = page_edit.border_and_shadow.get_value('border_size')
        self.report.new_result('790a2094-a0a3-442c-9e0f-c5308025bcbd', True if result == '3.0' else False)

        self.report.start_uuid('4eecfec3-49ff-4160-92dd-b2fe1e3054f1')
        page_edit.border_and_shadow.set_slider('border_size', 1)
        result = page_edit.border_and_shadow.get_value('border_size')
        self.report.new_result('4eecfec3-49ff-4160-92dd-b2fe1e3054f1', True if result == '10.0' else False)

        self.report.start_uuid('163aabc0-6d5f-492f-adbe-6d267daea881')
        page_edit.border_and_shadow.set_slider('border_size', 0)
        result = page_edit.border_and_shadow.get_value('border_size')
        self.report.new_result('163aabc0-6d5f-492f-adbe-6d267daea881', True if result == '0.0' else False)

        self.report.start_uuid('be9f989b-c47a-4cfa-b29c-12c074ca82b6')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('border_size', 0.7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('be9f989b-c47a-4cfa-b29c-12c074ca82b6',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('48c92c47-523b-4643-afc2-9ba6ec7eb836')
        result = page_edit.border_and_shadow.get_value('border_opacity')
        self.report.new_result('48c92c47-523b-4643-afc2-9ba6ec7eb836', True if result == '100' else False)

        self.report.start_uuid('e978af40-602b-4f82-885e-b3c433fd2edb')
        page_edit.border_and_shadow.set_slider('border_opacity', 0)
        result = page_edit.border_and_shadow.get_value('border_opacity')
        self.report.new_result('e978af40-602b-4f82-885e-b3c433fd2edb', True if result == '0' else False)

        self.report.start_uuid('5f359080-bd5a-438c-897b-2ccc92778f40')
        page_edit.border_and_shadow.set_slider('border_opacity', 1)
        result = page_edit.border_and_shadow.get_value('border_opacity')
        self.report.new_result('5f359080-bd5a-438c-897b-2ccc92778f40', True if result == '100' else False)

        self.report.start_uuid('fe1a5a22-686b-4963-89d6-e49372ebb76f')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('border_opacity', 0.5)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('fe1a5a22-686b-4963-89d6-e49372ebb76f',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('9c4ad3ce-7515-4a52-a97e-91c47138a876')
        self.report.start_uuid('7f41d420-4baf-4c44-9ea7-ed044c497b22')
        self.report.start_uuid('bbec0e66-c9b9-41de-9806-9f3a38ac81da')
        result_color, result_size, result_opacity = page_edit.border_and_shadow.tap_border_reset()
        self.report.new_result('9c4ad3ce-7515-4a52-a97e-91c47138a876', result_color)
        self.report.new_result('7f41d420-4baf-4c44-9ea7-ed044c497b22', result_size)
        self.report.new_result('bbec0e66-c9b9-41de-9806-9f3a38ac81da', result_opacity)

        # Shadow
        self.report.start_uuid('f6778b3a-7f12-4657-abbc-ed2fbd72bf90')
        page_edit.click(L.edit.border_and_shadow.tab_shadow)
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(1)
        time.sleep(3)
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('f6778b3a-7f12-4657-abbc-ed2fbd72bf90', result)

        self.report.start_uuid('c0abd003-2e29-43f6-ab81-58fa848c4013')
        time.sleep(3)
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('c0abd003-2e29-43f6-ab81-58fa848c4013', result)

        self.report.start_uuid('0bc4e8b4-08a2-4e36-8fb8-5954df41bc04')
        result = page_edit.title_designer.select_color_dropper(0.1, 0.1)
        self.report.new_result('0bc4e8b4-08a2-4e36-8fb8-5954df41bc04', result)

        self.report.start_uuid('767c9ec7-db10-4505-a2d8-9d02366d15d2')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        page_edit.title_designer.set_RGB_number('green', 250)
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('767c9ec7-db10-4505-a2d8-9d02366d15d2',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('916ced74-2f63-4fb1-a795-70019b0e5ea2')
        page_edit.back()
        pic_base = page_edit.get_preview_pic()
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(0)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('916ced74-2f63-4fb1-a795-70019b0e5ea2',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('368e2f96-d20c-4406-b67d-0c428cc2e762')
        pic_base = pic_after
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('368e2f96-d20c-4406-b67d-0c428cc2e762',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('7307d786-02cb-43fe-98eb-7a8211b6b426')
        result = page_edit.border_and_shadow.get_value('shadow_blur')
        self.report.new_result('7307d786-02cb-43fe-98eb-7a8211b6b426', True if result == '5.0' else False)

        self.report.start_uuid('e4833b28-c88a-430d-ac33-225abc066c7e')
        page_edit.border_and_shadow.set_slider('shadow_blur', 1)
        result = page_edit.border_and_shadow.get_value('shadow_blur')
        self.report.new_result('e4833b28-c88a-430d-ac33-225abc066c7e', True if result == '10.0' else False)

        self.report.start_uuid('fa0ba49c-4df3-479d-978c-b28121713afe')
        page_edit.border_and_shadow.set_slider('shadow_blur', 0)
        result = page_edit.border_and_shadow.get_value('shadow_blur')
        self.report.new_result('fa0ba49c-4df3-479d-978c-b28121713afe', True if result == '0.0' else False)

        self.report.start_uuid('a8be520e-d487-4c96-ba95-2010438eb5f4')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('shadow_blur', 0.7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('a8be520e-d487-4c96-ba95-2010438eb5f4',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('941fb2c8-409c-4d10-9600-ffa467bec959')
        result = page_edit.border_and_shadow.get_value('shadow_opacity')
        self.report.new_result('941fb2c8-409c-4d10-9600-ffa467bec959', True if result == '100' else False)

        self.report.start_uuid('8f873e3f-8e8d-41ca-9f24-9235ddcb21b1')
        page_edit.border_and_shadow.set_slider('shadow_opacity', 0)
        result = page_edit.border_and_shadow.get_value('shadow_opacity')
        self.report.new_result('8f873e3f-8e8d-41ca-9f24-9235ddcb21b1', True if result == '0' else False)

        self.report.start_uuid('7f499499-e3bf-4147-863a-f6539a929ecd')
        page_edit.border_and_shadow.set_slider('shadow_opacity', 1)
        result = page_edit.border_and_shadow.get_value('shadow_opacity')
        self.report.new_result('7f499499-e3bf-4147-863a-f6539a929ecd', True if result == '100' else False)

        self.report.start_uuid('7f51af88-2674-4260-93c6-3f2da0bde95b')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('shadow_opacity', 0.5)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('7f51af88-2674-4260-93c6-3f2da0bde95b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('8985b75e-25d7-4641-b5a8-9470522af42c')
        self.report.start_uuid('bd555337-31f9-4005-bbe1-b6231d5061c2')
        self.report.start_uuid('89ec740f-55f7-4acc-bb18-ba4eee986a39')
        result_color, result_blur, result_opacity = page_edit.border_and_shadow.tap_shadow_reset()
        self.report.new_result('8985b75e-25d7-4641-b5a8-9470522af42c', result_color)
        self.report.new_result('bd555337-31f9-4005-bbe1-b6231d5061c2', result_blur)
        self.report.new_result('89ec740f-55f7-4acc-bb18-ba4eee986a39', result_opacity)

        # Photo Border
        self.report.start_uuid('97373ee0-c6a9-4be0-af05-15e89662f935')
        page_edit.back()
        time.sleep(5)
        page_edit.click(L.edit.menu.delete)
        time.sleep(5)
        page_edit.click(L.edit.menu.effect)
        page_media.switch_to_pip_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.select_media_by_text('png.png')
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.timeline_select_item_by_index_on_track(2, 1)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Border & Shadow')
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(1)
        time.sleep(3)
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('97373ee0-c6a9-4be0-af05-15e89662f935', result)

        self.report.start_uuid('491453ee-9ea7-4178-bf76-117e33018409')
        time.sleep(3)
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('491453ee-9ea7-4178-bf76-117e33018409', result)

        self.report.start_uuid('abea30ec-cfa9-4af7-91cc-c11d03cf604e')
        result = page_edit.title_designer.select_color_dropper(0.1, 0.1)
        self.report.new_result('abea30ec-cfa9-4af7-91cc-c11d03cf604e', result)

        self.report.start_uuid('10ebc880-d8e8-445d-9542-910abd65ec3e')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        page_edit.title_designer.set_RGB_number('green', 250)
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('10ebc880-d8e8-445d-9542-910abd65ec3e',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('4d3db5b5-9ae0-4847-a733-e50236ce2dc6')
        page_edit.back()
        pic_base = page_edit.get_preview_pic()
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(0)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('4d3db5b5-9ae0-4847-a733-e50236ce2dc6',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('075b22d6-6719-4aa9-9008-043e1d5c63c2')
        pic_base = pic_after
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('075b22d6-6719-4aa9-9008-043e1d5c63c2',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('05468f8c-1129-4338-90dd-a644da659369')
        result = page_edit.border_and_shadow.get_value('border_size')
        self.report.new_result('05468f8c-1129-4338-90dd-a644da659369', True if result == '3.0' else False)

        self.report.start_uuid('bbb10772-dbd2-4345-b7f6-42a7888f27ea')
        page_edit.border_and_shadow.set_slider('border_size', 1)
        result = page_edit.border_and_shadow.get_value('border_size')
        self.report.new_result('bbb10772-dbd2-4345-b7f6-42a7888f27ea', True if result == '10.0' else False)

        self.report.start_uuid('52d965d8-5e70-4aff-a8c2-58c2735d30c8')
        page_edit.border_and_shadow.set_slider('border_size', 0)
        result = page_edit.border_and_shadow.get_value('border_size')
        self.report.new_result('52d965d8-5e70-4aff-a8c2-58c2735d30c8', True if result == '0.0' else False)

        self.report.start_uuid('93fc1bcd-8016-4a8d-8be7-792f4f73db41')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('border_size', 0.7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('93fc1bcd-8016-4a8d-8be7-792f4f73db41',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('de9f5b17-0d2e-40d9-84ed-e7aab983cbf4')
        result = page_edit.border_and_shadow.get_value('border_opacity')
        self.report.new_result('de9f5b17-0d2e-40d9-84ed-e7aab983cbf4', True if result == '100' else False)

        self.report.start_uuid('6e026639-f072-44f5-bb03-c066fa8246c3')
        page_edit.border_and_shadow.set_slider('border_opacity', 0)
        result = page_edit.border_and_shadow.get_value('border_opacity')
        self.report.new_result('6e026639-f072-44f5-bb03-c066fa8246c3', True if result == '0' else False)

        self.report.start_uuid('dc34b75f-0da1-4ec8-96c8-02b3a2681582')
        page_edit.border_and_shadow.set_slider('border_opacity', 1)
        result = page_edit.border_and_shadow.get_value('border_opacity')
        self.report.new_result('dc34b75f-0da1-4ec8-96c8-02b3a2681582', True if result == '100' else False)

        self.report.start_uuid('aad0a24b-b4d6-467c-b496-f8114a639af8')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('border_opacity', 0.5)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('aad0a24b-b4d6-467c-b496-f8114a639af8',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('2209b34e-e421-47fc-bf55-590869d7157b')
        self.report.start_uuid('0be339a8-1d4a-4391-b5c8-9003d6fc647e')
        self.report.start_uuid('62b2a5dc-cb53-41ad-b178-d292428a2127')
        result_color, result_size, result_opacity = page_edit.border_and_shadow.tap_border_reset()
        self.report.new_result('2209b34e-e421-47fc-bf55-590869d7157b', result_color)
        self.report.new_result('0be339a8-1d4a-4391-b5c8-9003d6fc647e', result_size)
        self.report.new_result('62b2a5dc-cb53-41ad-b178-d292428a2127', result_opacity)

        # Shadow
        self.report.start_uuid('05d66b72-5946-4e51-b733-368e72aded81')
        page_edit.click(L.edit.border_and_shadow.tab_shadow)
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(1)
        time.sleep(3)
        result = page_edit.title_designer.tap_color_map(0.3, 0.3)
        self.report.new_result('05d66b72-5946-4e51-b733-368e72aded81', result)

        self.report.start_uuid('9cc5e0d3-b196-4241-940f-e289c9d56eaa')
        time.sleep(3)
        result = page_edit.title_designer.set_hue_slider(0.3)
        self.report.new_result('9cc5e0d3-b196-4241-940f-e289c9d56eaa', result)

        self.report.start_uuid('ffa52d86-2911-45f3-bdf9-00d5da57c51a')
        result = page_edit.title_designer.select_color_dropper(0.1, 0.1)
        self.report.new_result('ffa52d86-2911-45f3-bdf9-00d5da57c51a', result)

        self.report.start_uuid('fd6925b2-60db-44df-b7d2-4aa47b37460e')
        pic_base = page_edit.get_preview_pic()
        page_edit.title_designer.set_RGB_number('red', 130)
        page_edit.title_designer.set_RGB_number('green', 250)
        page_edit.title_designer.set_RGB_number('blue', 150)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('fd6925b2-60db-44df-b7d2-4aa47b37460e',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('1ba6a272-7379-4f52-9a8e-7f460967fb03')
        page_edit.back()
        pic_base = page_edit.get_preview_pic()
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(0)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('1ba6a272-7379-4f52-9a8e-7f460967fb03',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('720bddd1-2f62-4332-991b-54b7d6de306b')
        pic_base = pic_after
        time.sleep(3)
        page_edit.border_and_shadow.select_color_by_order(7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('720bddd1-2f62-4332-991b-54b7d6de306b',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('92dd0823-7129-459b-929e-9b86938c31fc')
        result = page_edit.border_and_shadow.get_value('shadow_blur')
        self.report.new_result('92dd0823-7129-459b-929e-9b86938c31fc', True if result == '5.0' else False)

        self.report.start_uuid('40d13360-6b89-4e97-ab92-70632f6a3881')
        page_edit.border_and_shadow.set_slider('shadow_blur', 1)
        result = page_edit.border_and_shadow.get_value('shadow_blur')
        self.report.new_result('40d13360-6b89-4e97-ab92-70632f6a3881', True if result == '10.0' else False)

        self.report.start_uuid('223514a5-7a9d-42fe-86d1-4b9a86932d78')
        page_edit.border_and_shadow.set_slider('shadow_blur', 0)
        result = page_edit.border_and_shadow.get_value('shadow_blur')
        self.report.new_result('223514a5-7a9d-42fe-86d1-4b9a86932d78', True if result == '0.0' else False)

        self.report.start_uuid('5306f194-d25d-436b-b3b4-9aa3371a445c')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('shadow_blur', 0.7)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('5306f194-d25d-436b-b3b4-9aa3371a445c',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('e3f71d96-9b1d-411c-9d34-f02f72523073')
        result = page_edit.border_and_shadow.get_value('shadow_opacity')
        self.report.new_result('e3f71d96-9b1d-411c-9d34-f02f72523073', True if result == '100' else False)

        self.report.start_uuid('5abd577e-f4e9-47b8-b93a-9d325569f742')
        page_edit.border_and_shadow.set_slider('shadow_opacity', 0)
        result = page_edit.border_and_shadow.get_value('shadow_opacity')
        self.report.new_result('5abd577e-f4e9-47b8-b93a-9d325569f742', True if result == '0' else False)

        self.report.start_uuid('acaefe8b-0be9-4205-8656-fa53aed22437')
        page_edit.border_and_shadow.set_slider('shadow_opacity', 1)
        result = page_edit.border_and_shadow.get_value('shadow_opacity')
        self.report.new_result('acaefe8b-0be9-4205-8656-fa53aed22437', True if result == '100' else False)

        self.report.start_uuid('80c93439-ef0d-4724-97ca-a9aedff06898')
        pic_base = page_edit.get_preview_pic()
        page_edit.border_and_shadow.set_slider('shadow_opacity', 0.5)
        time.sleep(3)
        pic_after = page_edit.get_preview_pic()
        self.report.new_result('80c93439-ef0d-4724-97ca-a9aedff06898',
                               (lambda pic_src, pic_dest: True if not CompareImage(pic_src, pic_dest,
                                                                                   3).compare_image() else False)(
                                   pic_base, pic_after))

        self.report.start_uuid('1f192b49-6aa0-4207-9bea-cc32eac21698')
        self.report.start_uuid('eecb9e60-ca21-4354-9449-1b2f74178ede')
        self.report.start_uuid('80fa5fc9-3248-4a72-b8a8-365b880b1727')
        result_color, result_blur, result_opacity = page_edit.border_and_shadow.tap_shadow_reset()
        self.report.new_result('1f192b49-6aa0-4207-9bea-cc32eac21698', result_color)
        self.report.new_result('eecb9e60-ca21-4354-9449-1b2f74178ede', result_blur)
        self.report.new_result('80fa5fc9-3248-4a72-b8a8-365b880b1727', result_opacity)

        self.report.start_uuid('b098166a-7899-45eb-9226-c0a7e95a734c')
        self.report.start_uuid('4d176036-06b0-4355-90c8-e8e9af6d2f1e')
        self.report.start_uuid('48f06dec-a26f-4e4b-bc7a-5eb161ceff07')
        self.report.start_uuid('d961eb70-cb09-498c-8a65-2fbb0af94ab0')
        page_edit.border_and_shadow.select_color_by_order(7)
        page_edit.border_and_shadow.set_slider('shadow_blur', 0.7)
        page_edit.border_and_shadow.set_slider('shadow_opacity', 0.5)
        shadow_blur_base = page_edit.border_and_shadow.get_value('shadow_blur')
        shadow_opacity_base = page_edit.border_and_shadow.get_value('shadow_opacity')
        page_edit.click(L.edit.border_and_shadow.tab_border)
        time.sleep(5)
        page_edit.border_and_shadow.select_color_by_order(7)
        page_edit.border_and_shadow.set_slider('border_size', 0.7)
        page_edit.border_and_shadow.set_slider('border_opacity', 0.5)
        border_size_base = page_edit.border_and_shadow.get_value('border_size')
        border_opacity_base = page_edit.border_and_shadow.get_value('border_opacity')
        page_edit.back()
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Replace')
        page_media.switch_to_photo_library()
        page_media.select_media_by_text(self.test_material_folder)
        time.sleep(5)
        page_media.select_media_by_text('jpg.jpg')
        page_media.click(L.import_media.library_gridview.add)
        time.sleep(5)
        page_edit.select_from_bottom_edit_menu('Border & Shadow')
        border_size_after = page_edit.border_and_shadow.get_value('border_size')
        border_opacity_after = page_edit.border_and_shadow.get_value('border_opacity')
        page_edit.click(L.edit.border_and_shadow.tab_shadow)
        time.sleep(5)
        shadow_blur_after = page_edit.border_and_shadow.get_value('shadow_blur')
        shadow_opacity_after = page_edit.border_and_shadow.get_value('shadow_opacity')
        self.report.new_result('b098166a-7899-45eb-9226-c0a7e95a734c', True if border_size_base == border_size_after else False)
        self.report.new_result('4d176036-06b0-4355-90c8-e8e9af6d2f1e', True if border_opacity_base == border_opacity_after else False)
        self.report.new_result('48f06dec-a26f-4e4b-bc7a-5eb161ceff07', True if shadow_blur_base == shadow_blur_after else False)
        self.report.new_result('d961eb70-cb09-498c-8a65-2fbb0af94ab0', True if shadow_opacity_base == shadow_opacity_after else False)



