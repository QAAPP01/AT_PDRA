import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest
import time

from pages.locator import locator as L
from pages.locator.locator_type import *


from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER



test_material_folder = TEST_MATERIAL_FOLDER


class Test_sce_06_00_00:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        print('Init. driver session')
        print('DRIVER_CAPS=', DRIVER_DESIRED_CAPS)
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        desired_caps = {}
        desired_caps.update(driver_config.android_device)
        desired_caps.update(app_config.prod_cap)
        desired_caps.update(DRIVER_DESIRED_CAPS)
        print('desired_caps=', desired_caps)
        
        # ---- local mode > end ----
                                                              
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
        self.driver.start_app(PACKAGE_NAME)
        self.main_page = PageFactory().get_page_object("main_page", self.driver)
        self.import_media = PageFactory().get_page_object("import_media", self.driver)
        self.produce = PageFactory().get_page_object("produce", self.driver)
        self.edit = PageFactory().get_page_object("edit", self.driver)
        self.settings = PageFactory().get_page_object("timeline_settings", self.driver)

        self.main_page.clean_projects()
        self.driver.implicit_wait(5)

        yield self.driver  # keep driver for the function which uses 'initial'

        # teardown
        logger('\n============<Teardown>============')
        self.driver.stop_driver()

    # @pytest.mark.skip
    
    def test_sce_gt_01(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        # video preview color preset
        _start('ec404b31-1e27-47c4-9092-355fc4a2401a')
        main.project_create_new(ratio="16:9")
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        edit.click(aid('[AID]ColorPresetThumbnail_3'))
        edit.click(aid('[AID]ColorPresetThumbnail_8'))
        result_gt = edit.ground_truth_photo(L.edit.preview.movie_view,"video_color_preset_16_9.png")
        _end('ec404b31-1e27-47c4-9092-355fc4a2401a', result_gt)
        edit.driver.driver.back()
        time.sleep(1)
        edit.driver.driver.back()
        time.sleep(1)
        edit.driver.driver.back()
        time.sleep(1)

        
        # photo preview color preset
        _start('4dc86868-4e85-4809-8d36-f3d35bff2496')
        #main.relaunch_app(PACKAGE_NAME)
        main.project_create_new(ratio="16:9",type="photo")
        edit.click(L.edit.timeline.clip_photo)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        edit.click(aid('[AID]ColorPresetThumbnail_3'))
        edit.click(aid('[AID]ColorPresetThumbnail_8'))
        result_gt = edit.ground_truth_photo(L.edit.preview.movie_view,"photo_color_preset_16_9.png")
        _end('4dc86868-4e85-4809-8d36-f3d35bff2496',result_gt)
        
        # 16:9 
        _start('32448a26-3bea-41ef-b1c4-352715ee44d6') # color preset on produced video
        _start('503b32f0-3341-43a8-af27-86a019c89758') # profile
        _start('c9592e94-e602-41d2-8a1f-2bee4007dc4e') # watermark
        _start('d4174583-e3fa-4d23-b980-a0c3fcf8ab39') # quality
        _start('5747445c-6119-48bd-aa91-a1dae6b59964') # aspect ratio
        _start('e00e06e6-2593-48e8-8bd2-112354b49a36') # free account watermark
        edit.back()
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.pan_zoom)
        edit.select_from_bottom_edit_menu('Pan & Zoom')
        edit.click(L.edit.pan_zoom_effect.no_effect)
        edit.click(L.edit.pan_zoom_effect.ok)
        edit.click(L.edit.menu.export)
        edit.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.facebook)
        produce.click(L.produce.facebook.sd)
        time.sleep(2)
        produce.click(L.produce.facebook.next)
        produce.ad.close_full_page_ad()
        produce.exist_click(L.produce.facebook.tooltip.ok)
        result = produce.ground_truth_video('photo_color_preset_16_9.mp4')
        _end('32448a26-3bea-41ef-b1c4-352715ee44d6',result)
        _end('503b32f0-3341-43a8-af27-86a019c89758',result)
        _end('c9592e94-e602-41d2-8a1f-2bee4007dc4e',result)
        _end('d4174583-e3fa-4d23-b980-a0c3fcf8ab39',result)
        _end('5747445c-6119-48bd-aa91-a1dae6b59964',result)
        _end('e00e06e6-2593-48e8-8bd2-112354b49a36',result)

    # @pytest.mark.skip
    
    def test_sce_gt_02(self):
        main = self.main_page
        import_media = self.import_media
        produce = self.produce
        edit = self.edit
        driver = self.driver.driver
        settings = self.settings
        _start = self.report.start_uuid 
        _end = self.report.new_result
        
        
        _start('7d15a1ea-525b-47c0-9210-576d7445f770')
        main.project_create_new(ratio="9:16")
        edit.click(L.edit.timeline.clip)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        edit.click(aid('[AID]ColorPresetThumbnail_3'))
        edit.click(aid('[AID]ColorPresetThumbnail_8'))
        result_gt = edit.ground_truth_photo(L.edit.preview.movie_view,"video_color_preset_9_16.png")
        _end('7d15a1ea-525b-47c0-9210-576d7445f770', result_gt)
        edit.driver.driver.back()
        time.sleep(1)
        edit.driver.driver.back()
        time.sleep(1)
        edit.driver.driver.back()
        time.sleep(1)
       
        
        _start('98b0bb24-6796-422d-b293-4b6347ff8ec7')
        #main.relaunch_app(PACKAGE_NAME)
        main.project_create_new(ratio="9:16",type="photo")
        edit.click(L.edit.timeline.clip_photo)
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.color)
        edit.select_from_bottom_edit_menu('Filter')
        edit.click(aid('[AID]ColorPresetThumbnail_3'))
        edit.click(aid('[AID]ColorPresetThumbnail_8'))
        result_gt = edit.ground_truth_photo(L.edit.preview.movie_view,"photo_color_preset_9_16.png")
        _end('98b0bb24-6796-422d-b293-4b6347ff8ec7',result_gt)
        
        # color preset
        _start('6eb45eff-2eda-499f-b1f7-3b596194ec46')
        _start('dd9c050e-7ae7-48cd-b348-60089085bd7c')
        _start('33ed0d72-0563-43ed-8b99-2735d9f15400')
        _start('5c196ec7-fc06-4dd0-bec5-9a256f176479')
        _start('5d47331a-bd40-43e0-9778-e22be42344b5')
        _start('70fb1749-c8f6-47b2-b3ce-f76c74996be9')
        edit.back()
        #edit.click(L.edit.menu.edit)
        #edit.click(L.edit.edit_sub.pan_zoom)
        edit.select_from_bottom_edit_menu('Pan & Zoom')
        edit.click(L.edit.pan_zoom_effect.no_effect)
        edit.click(L.edit.pan_zoom_effect.ok)
        edit.click(L.edit.menu.export)
        edit.click(L.edit.menu.produce_sub_page.produce)
        produce.click(L.produce.tab.facebook)
        produce.click(L.produce.facebook.sd)
        time.sleep(1)
        produce.click(L.produce.facebook.next)
        produce.ad.close_full_page_ad()
        produce.exist_click(L.produce.facebook.tooltip.ok)
        result = produce.ground_truth_video('photo_color_preset_9_16.mp4')
        _end('6eb45eff-2eda-499f-b1f7-3b596194ec46',result)
        _end('dd9c050e-7ae7-48cd-b348-60089085bd7c',result)
        _end('33ed0d72-0563-43ed-8b99-2735d9f15400',result)
        _end('5c196ec7-fc06-4dd0-bec5-9a256f176479',result)
        _end('5d47331a-bd40-43e0-9778-e22be42344b5',result)
        _end('70fb1749-c8f6-47b2-b3ce-f76c74996be9',result)


'''
        _start('')
        
        _end('',result)
'''