import inspect
import sys
import time
from os import path
from os.path import dirname

import cv2
import numpy as np
import pytest

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.pages.page_factory import PageFactory
from .conftest import PACKAGE_NAME
from .conftest import REPORT_INSTANCE
from .conftest import TEST_MATERIAL_FOLDER
from .conftest import TEST_MATERIAL_FOLDER_01
from ATFramework_aPDR.pages.locator.locator_type import *


sys.path.insert(0, (dirname(dirname(__file__))))

report = REPORT_INSTANCE
pdr_package = PACKAGE_NAME

test_material_folder = TEST_MATERIAL_FOLDER
video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'

class Test_class:
    @pytest.fixture(autouse=True)
    def initial(self, driver):
        logger("[Start] Init driver session")

        self.driver = driver

        # shortcut
        self.page_main = PageFactory().get_page_object("main_page", self.driver)
        self.page_edit = PageFactory().get_page_object("edit", self.driver)
        self.page_media = PageFactory().get_page_object("import_media", self.driver)
        self.page_preference = PageFactory().get_page_object("timeline_settings", self.driver)

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist

    def test_case(self):
        before = self.page_edit.get_preview_pic()
        self.click(find_string('Flip'))
        after = self.page_edit.get_preview_pic()
        original_image = cv2.imread(before)
        flipped_image = cv2.imread(after)
        result = np.allclose(original_image, flipped_image)

        if result:
            print("影像相等")
        else:
            # 計算相對誤差
            relative_error = np.abs(original_image - flipped_image) / np.maximum(np.abs(original_image),
                                                                                 np.abs(flipped_image))

            # 打印相對誤差值
            print("影像不相等，相對誤差值：")
            print(relative_error)
