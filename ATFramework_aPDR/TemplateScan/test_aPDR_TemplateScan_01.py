import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from ATFramework.utils.compare_Mac import CompareImage
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest
import time
import os

from pages.locator import locator as L


from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER


pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER
package_path = os.path.dirname(os.path.dirname(__file__)) + r"\app\PowerDirector.apk"

class Test_TemplateScan_00:
    @classmethod
    def setup_class(cls):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver session>============')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        #desired_caps.update(app_config.prod_fullreset_cap)
        desired_caps.update(app_config.native_settings_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        logger(f"desired_caps={desired_caps}")
        logger("connect to report instance")
        cls.report = report
        logger("set udid")
        cls.device_udid = DRIVER_DESIRED_CAPS['udid']
        # ---- local mode > end ----
        logger("set testing material path")
        cls.test_material_folder = test_material_folder
        
                                                              
        # retry 10 time if craete driver fail
        retry = 10
        while retry:
            try:
                logger("creating driver.")
                cls.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',desired_caps)
                if cls.driver:
                    logger("driver created!")
                    break
                else:
                    raise Exception("create driver fail")
            except Exception as e:
                logger(e)
                retry -= 1
        else:
            logger("[ERROR] Unable to create driver, exit now")
            os._exit(1)
                
        #cls.report.set_driver(cls.driver)
        cls.driver.implicit_wait(15)

    def remove_pdr_projects(self):
        import subprocess
        logger('\n============<remove_pdr_projects>============')
        try:
            command = f'adb -s {self.device_udid} shell rm -r "storage/emulated/0/PowerDirector/projects"'
            subprocess.call(command)
        except Exception:
            pass
        return True

    @classmethod
    def teardown_class(cls):
        logger('\n============<Teardown>============')
        cls.driver.stop_driver()

    def setup_method(self, method):
        logger('\n============<Setup Method>============')
        self.remove_pdr_projects()
        #self.driver.start_app(pdr_package)

    def teardown_method(self, method):
        logger('\n============<TearDown Method>============')
        #self.driver.stop_app(pdr_package)

    #@pytest.mark.skip
    
    def test_sce_00_01_01a(self):
        logger('[V] Install and reset app')
        self.driver.remove_app(pdr_package)
        logger(f'package path={package_path}')
        self.driver.install_app(package_path, pdr_package)


class Test_TemplateScan_01:
    @classmethod
    def setup_class(cls):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        
        global report
        logger('\n============<Init driver session>============')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        #desired_caps.update(app_config.prod_install_cap)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        logger(f"desired_caps={desired_caps}")
        cls.
        # ---- local mode > end ----
        cls.test_material_folder = test_material_folder
        cls.driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local',
                                                              desired_caps)
        cls.report.set_driver(cls.driver)
        cls.driver.implicit_wait(15)
        cls.driver.reset_app(pdr_package)
        cls.device_udid = DRIVER_DESIRED_CAPS['udid']
        

    @classmethod
    def teardown_class(cls):
        logger('\n============<Teardown>============')
        cls.driver.stop_driver()

    def setup_method(self, method):
        logger('\n============<Setup Method>============')
        self.driver.start_app(pdr_package)

    def teardown_method(self, method):
        logger('\n============<TearDown Method>============')
        self.driver.stop_app(pdr_package)

    @pytest.fixture(name='set_permission')
    def set_permission(self):
        page_main = PageFactory().get_page_object("main_page", self.driver)
        logger('[V] Set Permission')
        logger('[Permission] Confirm GDPR')
        if page_main.exist_click(L.main.permission.gdpr_accept,5): # Android version  < 6 or locate in EU
            logger("[Permission] GDPR found and closed")
        page_main.is_exist(L.main.permission.file_ok, 120)
        page_main.el(L.main.permission.file_ok).click()
        page_main.el(L.main.permission.photo_allow).click()
        page_main.check_open_tutorial()
    
    # @pytest.mark.skip
    @pytest.mark.usefixtures('set_permission')
    
    def test_sce_00_01_01(self):
        
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        
        time.sleep(15)
        project_title = '16_9_small'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        time.sleep(5)
        
        page_main.check_open_tutorial()
        page_main.enter_settings_from_main()
        page_main.sign_in_cyberlink_account()
        
        page_main.click(L.timeline_settings.settings.back)
        page_main.swipe_main_page('down', 5)
        time.sleep(5)

        # Technology
        self.report.start_uuid('84a942f9-f674-42f5-b711-371918000411')  
        amount = 51
        pass_count = 0
        fail_count = 0
        index = 1
        page = 0
        result = True
        scroll_result = True
        category = 'Technology'
        
        page_main.project_click_new()
        # page_main.project_set_name(f"{category} {index}")
        page_main.project_set_16_9()
        page_main.project_set_to_portrait_mode()  
        # time.sleep(5)
        # page_edit.back()
        # time.sleep(5)
        page_edit.intro_video.enter_intro_video_library()  
        page_edit.intro_video.switch_tabs('discover') 
        page_edit.intro_video.select_category(category)
        current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
        page_edit.intro_video.select_template_by_index(index)
        page_edit.intro_video.enter_intro_video_designer()
        result = page_edit.intro_video.apply_to_project()
        pass_count = pass_count+1
        page_edit.intro_video.move_pic(current_template, category, result) 
        result = True
        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_16_9()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()  
                page_edit.intro_video.switch_tabs('discover') 
                # page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count+1
                if index >= 6:
                    page = page+1
                    if page > (amount/6):
                        index = index+1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True) 
            except Exception:
                fail_count = fail_count+1
                index = index+1
                if index > 6:
                    page = page+1
                    if page > (amount/6):
                        index = index+1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('84a942f9-f674-42f5-b711-371918000411', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')        
        
    
        # Travel
        self.report.start_uuid('7521dd2e-7d66-4501-b37f-f9f38db1fc88')  
        amount = 100
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Travel'
        
        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_16_9()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()  
                page_edit.intro_video.switch_tabs('discover') 
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('7521dd2e-7d66-4501-b37f-f9f38db1fc88', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')        
        
        
        # Family
        self.report.start_uuid('d4d2a902-1829-4f81-bc99-130711d6a246')  
        amount = 73
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Family'
        
        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_16_9()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()  
                page_edit.intro_video.switch_tabs('discover') 
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('d4d2a902-1829-4f81-bc99-130711d6a246', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')        


        # Season
        self.report.start_uuid('006ad599-c5c1-4596-8c6f-00dec9670a9f')  
        amount = 57
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Season'
        
        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_16_9()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()  
                page_edit.intro_video.switch_tabs('discover') 
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('006ad599-c5c1-4596-8c6f-00dec9670a9f', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')        


        # Handwritten
        self.report.start_uuid('861aa1bc-2abc-4ebe-a045-1aa240ad5cf4')  
        amount = 37
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Handwritten'
        
        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_16_9()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()  
                page_edit.intro_video.switch_tabs('discover') 
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('861aa1bc-2abc-4ebe-a045-1aa240ad5cf4', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')        

        
        # Minimalist
        self.report.start_uuid('44b43c24-07f9-4eb3-8bf8-edc5fe722b80')  
        amount = 104
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Minimalist'
        
        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_16_9()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()  
                page_edit.intro_video.switch_tabs('discover') 
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('44b43c24-07f9-4eb3-8bf8-edc5fe722b80', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')        


        # Fun & Playful
        self.report.start_uuid('d1fbc45b-27a6-4b9c-b681-097f6192a8f2')  
        amount = 147
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Fun & Playful'
        previous_template = None

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_16_9()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()  
                page_edit.intro_video.switch_tabs('discover') 
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 6:
                    page = page + 1
                    if page > (amount / 6):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('d1fbc45b-27a6-4b9c-b681-097f6192a8f2', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')        
        

    # @pytest.mark.skip
    # @pytest.mark.usefixtures('set_permission')
    
    def test_sce_00_01_02(self):

        global current_template
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)

        time.sleep(15)
        project_title = '9_16'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        time.sleep(5)

        # page_main.check_open_tutorial()
        # page_main.enter_settings_from_main()
        # page_main.sign_in_cyberlink_account()

        # page_main.click(L.timeline_settings.settings.back)
        # page_main.swipe_main_page('down', 5)
        # time.sleep(5)

        # Technology
        self.report.start_uuid('983268f3-c51d-4c40-88b3-3e83a5ed2d40')
        amount = 16
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Technology'

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_9_16()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()
                page_edit.intro_video.switch_tabs('discover')
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('983268f3-c51d-4c40-88b3-3e83a5ed2d40', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')


        # Travel
        self.report.start_uuid('e8c22232-6273-494c-98fb-79c30cea4c39')
        amount = 10
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Travel'

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_9_16()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()
                page_edit.intro_video.switch_tabs('discover')
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('e8c22232-6273-494c-98fb-79c30cea4c39', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')


        # Family
        self.report.start_uuid('3bebd3a6-de1e-491b-830b-184febd47b6b')
        amount = 10
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Family'

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_9_16()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()
                page_edit.intro_video.switch_tabs('discover')
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('3bebd3a6-de1e-491b-830b-184febd47b6b', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')


        # Season
        self.report.start_uuid('722c7296-d375-4ddc-ab39-a5c73f874356')
        amount = 4
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Season'

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_9_16()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()
                page_edit.intro_video.switch_tabs('discover')
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('722c7296-d375-4ddc-ab39-a5c73f874356', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')


        # Handwritten
        self.report.start_uuid('39897765-4575-47ae-8c6e-e12c11252a6a')
        amount = 4
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Handwritten'

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_9_16()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()
                page_edit.intro_video.switch_tabs('discover')
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('39897765-4575-47ae-8c6e-e12c11252a6a', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')


        # Minimalist
        self.report.start_uuid('184cb83b-b514-4f64-bcf9-896c6e1acd9a')
        amount = 6
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Minimalist'

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_9_16()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()
                page_edit.intro_video.switch_tabs('discover')
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('184cb83b-b514-4f64-bcf9-896c6e1acd9a', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')


        # Fun & Playful
        self.report.start_uuid('4f5c4189-fc98-4c28-ac39-e17d9d2f3052')
        amount = 20
        pass_count = 0
        fail_count = 0
        index = 0
        page = 0
        result = True
        scroll_result = True
        category = 'Fun & Playful'
        previous_template = None

        for retry in range(amount):
            try:
                page_main.project_reload("16_9")
                # time.sleep(5)
                page_main.start_app(pdr_package)
                time.sleep(5)
                page_main.project_click_new()
                # page_main.project_set_name(f"{category} {index}")
                page_main.project_set_9_16()
                # time.sleep(5)
                # page_edit.back()
                # time.sleep(5)
                page_edit.intro_video.enter_intro_video_library()
                page_edit.intro_video.switch_tabs('discover')
                page_edit.intro_video.select_category(category)
                if page > 0:
                    logger(f'Scroll to Page {page}')
                    scroll_result = page_edit.intro_video.scroll_template_list(page)
                index = index+1
                current_template = page_edit.intro_video.save_thumbnail_image_by_index(index)
                if not scroll_result:
                    if not current_template:
                        logger("End this category.")
                        break
                if not page_edit.intro_video.select_template_by_index(index):
                    break
                page_edit.intro_video.enter_intro_video_designer()
                page_edit.intro_video.apply_to_project()
                pass_count = pass_count + 1
                if index >= 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    elif scroll_result:
                        logger('Page scrolled, reset index')
                        index = 1
                page_edit.intro_video.move_pic(current_template, category, True)
            except Exception:
                fail_count = fail_count + 1
                index = index + 1
                if index > 2:
                    page = page + 1
                    if page > (amount / 2):
                        index = index + 1
                    else:
                        index = 1
                result = False
                logger(f'Exception occurs, fail count = {fail_count}')
                if not current_template:
                    page_edit.intro_video.move_pic(current_template, category, result)
        # amount = pass_count + fail_count
        self.report.new_result('4f5c4189-fc98-4c28-ac39-e17d9d2f3052', result, None, f'Tested:{amount}, PASS:{pass_count}, FAIL:{fail_count}')

