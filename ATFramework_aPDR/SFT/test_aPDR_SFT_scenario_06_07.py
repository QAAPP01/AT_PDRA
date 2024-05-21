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


from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01


pdr_package = PACKAGE_NAME


class Test_SFT_Scenario_06_07:
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
    # 
    # def test_sce_06_07_01(self):
        # logger('>>> test_sce_06_07_01 : Gamification <<<')
        # media_list = ['01_static.mp4']
        # page_main = PageFactory().get_page_object("main_page", self.driver)
        # page_edit = PageFactory().get_page_object("edit", self.driver)
        # page_media = PageFactory().get_page_object("import_media", self.driver)
        # page_produce = PageFactory().get_page_object("produce", self.driver)
        # page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        # page_produce.ad.close_opening_ads()
        # create existed 16_9 project
        # project_title = '16_9'
        # page_main.reset_project_list(self.device_udid, pdr_package, project_title)

        # self.report.start_uuid('f790a46e-0ada-44db-a2ba-b37c8d25e67f')
        # result = page_main.enter_gamification()
        # self.report.new_result('f790a46e-0ada-44db-a2ba-b37c8d25e67f', result)

        # 4K Reward
        # self.report.start_uuid('6ab82885-8dca-4d55-85d2-73d68015e693')
        # result = page_main.check_gamification_titles('30 min. of 4K Video Output')
        # self.report.new_result('6ab82885-8dca-4d55-85d2-73d68015e693', result)

        # self.report.start_uuid('c180a0d3-192a-4d8c-a6b8-b638f1ade340')
        # result = page_main.select_gamification_claim_by_order(0)
        # self.report.new_result('c180a0d3-192a-4d8c-a6b8-b638f1ade340', result)

        # self.report.start_uuid('3fba401e-927e-4816-91c5-e98bcf89cf3d')
        # result = True if page_main.is_exist(L.main.gamification.claim_dialog.description) else False
        # self.report.new_result('3fba401e-927e-4816-91c5-e98bcf89cf3d', result)

        # self.report.start_uuid('41436d3e-7a5a-47a1-a43a-77cbcb6c767c')
        # result = True if page_main.is_exist(L.main.gamification.claim_dialog.btn_use) else False
        # self.report.new_result('41436d3e-7a5a-47a1-a43a-77cbcb6c767c', result)

        # self.report.start_uuid('5490e801-e387-4300-9b3a-9ad560dc3dd6')
        # result = True if page_main.is_exist(L.main.gamification.claim_dialog.clock_img) else False
        # self.report.new_result('5490e801-e387-4300-9b3a-9ad560dc3dd6', result)

        # self.report.start_uuid('fafbe475-ef7d-49f2-8766-249f837f9411')
        # result = page_main.close_gamification_claim_dialog()
        # self.report.new_result('fafbe475-ef7d-49f2-8766-249f837f9411', result)

        # Producing Video Reward
        # self.report.start_uuid('eb684fa2-952f-44ce-a8ff-49de71e927fd')
        # result = page_main.check_gamification_titles('Producing Videos - Level 1')
        # self.report.new_result('eb684fa2-952f-44ce-a8ff-49de71e927fd', result)

        # self.report.start_uuid('33395f3b-c382-4b85-8385-1c50e2ca8360')
        # result = page_main.select_gamification_claim_by_order(1)
        # self.report.new_result('33395f3b-c382-4b85-8385-1c50e2ca8360', result)

        # self.report.start_uuid('4285e51c-9c7c-427b-888b-438f7011a6ea')
        # result = True if page_main.is_exist(L.main.gamification.claim_dialog.title_not_complete) else False
        # self.report.new_result('4285e51c-9c7c-427b-888b-438f7011a6ea', result)

        # self.report.start_uuid('4fa3bb72-4d4e-419a-9f36-ae4801603b87')
        # result = True if page_main.is_exist(L.main.gamification.claim_dialog.btn_ok) else False
        # self.report.new_result('4fa3bb72-4d4e-419a-9f36-ae4801603b87', result)

        # self.report.start_uuid('c7344e0c-64d6-4145-811c-25f6212de136')
        # result = page_main.close_gamification_claim_dialog()
        # self.report.new_result('c7344e0c-64d6-4145-811c-25f6212de136', result)

        # self.report.start_uuid('0d2f0536-dbbe-4698-99c8-61cc60295b40')
        # result = True if page_main.is_exist(L.main.gamification.produced_videos_progress) else False
        # self.report.new_result('0d2f0536-dbbe-4698-99c8-61cc60295b40', result)

        # Login Reward
        # self.report.start_uuid('2a09345a-34b3-4242-aada-637f51f96460')
        # self.report.start_uuid('160bea25-7706-438c-8658-36e4313640cb')
        # page_main.click(L.main.gamification.tab_complete)
        # time.sleep(5)
        # result = page_main.check_gamification_titles('Log in to CyberLink Account')
        # self.report.new_result('2a09345a-34b3-4242-aada-637f51f96460', result)
        # self.report.new_result('160bea25-7706-438c-8658-36e4313640cb', result)

    # @pytest.mark.skip
    
    def test_sce_06_07_01(self):
        logger('>>> test_sce_06_07_01 : Gamification <<<')
        media_list = ['01_static.mp4']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        page_produce = PageFactory().get_page_object("produce", self.driver)
        page_timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
        
        # page_main.check_open_tutorial()
        page_main.project_click_new()
        page_main.project_set_name("sce_06_07_01")
        page_main.project_set_9_16() 
        time.sleep(10)
        page_media.select_media_by_text(self.test_material_folder_01)
        time.sleep(5)
        page_media.select_media_by_order(1)
        page_media.el(L.import_media.library_gridview.add).click()
        page_media.el(L.import_media.video_entry.back).click()
        page_media.el(L.import_media.video_entry.back).click()
        page_produce.click(L.edit.menu.produce)
        page_produce.select_produce_type('gallery')
        page_produce.start_produce()

        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        time.sleep(15)

        self.report.start_uuid('65ebd201-8428-4b82-bfd6-474ffadf9107')
        result = page_main.enter_gamification()
        self.report.new_result('65ebd201-8428-4b82-bfd6-474ffadf9107', result)

        self.report.start_uuid('fcdb81bb-18fc-4705-971c-ee517189b041')
        result = True if page_main.is_exist(L.launcher.gamification.produced_videos_progress) else False
        self.report.new_result('fcdb81bb-18fc-4705-971c-ee517189b041', result)

        # Login
        self.report.start_uuid('05157b8f-1b9f-4448-99c5-c76cf1059441')
        page_main.click(L.launcher.gamification.tab_complete)
        time.sleep(5)
        result = page_main.check_gamification_titles('Sign up and log in')
        self.report.new_result('05157b8f-1b9f-4448-99c5-c76cf1059441', result)

        self.report.start_uuid('a62eb402-aa70-4fe1-b6a5-b867d5e07d17')
        # page_main.click(L.main.gamification.tab_complete)
        # time.sleep(5)
        # result = True if page_main.is_exist(L.main.gamification.no_cmoplete_text) else False
        self.report.new_result('a62eb402-aa70-4fe1-b6a5-b867d5e07d17', result)

        # 3 day check in
        self.report.start_uuid('6ffb8ac9-5fb4-4296-9397-979fbbbca288')
        page_main.click(L.launcher.gamification.tab_active)
        time.sleep(5)
        # result = page_main.check_gamification_titles('Check in for 3 days')
        description_list = page_main.check_gamification_mission_description()
        result = True if "You've completed the check in for 3 days challenge." in description_list else False
        self.report.new_result('6ffb8ac9-5fb4-4296-9397-979fbbbca288', result)

        # ADD x-promote
        self.report.start_uuid('f3543c6d-c2b2-4272-8c39-4d0fa5e1b973')
        result = True if "You've completed the AdDirector challenge!" in description_list else False
        self.report.new_result('f3543c6d-c2b2-4272-8c39-4d0fa5e1b973', result)

        self.report.start_uuid('a9b71b0b-6b5b-4bfe-bb07-1500c4211fc7')
        self.report.start_uuid('d38a4c35-4be2-46ad-ae6b-838e49f1a9ea')
        result = True if page_main.is_exist(L.launcher.gamification.btn_claim) else False
        self.report.new_result('a9b71b0b-6b5b-4bfe-bb07-1500c4211fc7', result)
        self.report.new_result('d38a4c35-4be2-46ad-ae6b-838e49f1a9ea', result)


        # Producing Video Reward
        self.report.start_uuid('3f896e46-6fdb-4fe0-a8c5-751a1cec2936')
        # result = page_main.check_gamification_titles('Produce Video - Level 1')
        # result = page_main.check_gamification_titles('2 days of premium for free')
        result = True if "You've completed the producing 1 video challenge." in description_list else False
        self.report.new_result('3f896e46-6fdb-4fe0-a8c5-751a1cec2936', result)
        
        self.report.start_uuid('34fdc0a8-09bd-4242-8a59-3cf4e69adfd8')
        page_main.back()
        time.sleep(5)
        page_main.enter_gamification()
        time.sleep(5)
        result = page_main.select_gamification_claim_by_order(0)
        self.report.new_result('34fdc0a8-09bd-4242-8a59-3cf4e69adfd8', result)
        
        self.report.start_uuid('f5535381-8531-4baa-9877-989747e182e7')
        self.report.start_uuid('166f7433-2171-4b54-8304-6708a741f02b')
        result = page_main.check_gamification_reward_content('2 days of premium for free')
        self.report.new_result('f5535381-8531-4baa-9877-989747e182e7', result)
        self.report.new_result('166f7433-2171-4b54-8304-6708a741f02b', result)

        self.report.start_uuid('a0986f30-c3de-431e-bb37-3ca38c2af404')
        self.report.start_uuid('d9777f94-1737-4989-8f2d-18bd94c5f1e7')
        self.report.start_uuid('51903285-4e2a-4bcd-b2a8-211afff942c9')
        self.report.start_uuid('95a0cc73-8fc1-4b8b-b524-c020935dc925')
        # page_main.click(L.main.gamification.claim_dialog.btn_use)
        # time.sleep(5)
        # result = page_main.check_gamification_claim_countdown()
        result = True if page_main.is_exist(L.launcher.gamification.claim_dialog.btn_use) else False
        self.report.new_result('a0986f30-c3de-431e-bb37-3ca38c2af404', result)
        self.report.new_result('d9777f94-1737-4989-8f2d-18bd94c5f1e7', result)
        self.report.new_result('51903285-4e2a-4bcd-b2a8-211afff942c9', result)
        self.report.new_result('95a0cc73-8fc1-4b8b-b524-c020935dc925', result)

        
        # self.report.start_uuid('12e52dce-ca56-411b-905d-76d2c18bd622')
        # page_main.project_click_new()
        # page_main.project_set_name("sce_06_07_01")
        # page_main.project_set_16_9()
        # time.sleep(5)
        # page_main.back()
        # result = False if page_main.is_exist(L.edit.preview.watermark) else True
        # self.report.new_result('12e52dce-ca56-411b-905d-76d2c18bd622', result)
        #
        # self.report.start_uuid('05ca45f9-69ca-4b4c-91de-e976792509f0')
        # page_edit.click(L.edit.menu.timeline_setting)
        # page_edit.click(L.edit.sub_menu.settings)
        # time.sleep(3)
        # page_main.sign_in_cyberlink_account()
        # time.sleep(5)
        # page_main.sign_out_cyberlink_account()
        # page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        # time.sleep(15)
        # page_main.enter_gamification()
        # page_main.click(L.main.gamification.tab_complete)
        # time.sleep(5)
        # result = page_main.check_gamification_titles('Sign up and log in')
        # self.report.new_result('05ca45f9-69ca-4b4c-91de-e976792509f0', result)
        
        

