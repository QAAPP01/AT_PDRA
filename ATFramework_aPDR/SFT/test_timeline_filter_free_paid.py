import traceback
import inspect

import pytest
import allure
from random import randint

from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg, CompareImage
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L


from .conftest import TEST_MATERIAL_FOLDER, driver

test_material_folder = TEST_MATERIAL_FOLDER
ori_preview = None



@allure.epic('Timeline_Master_Photo')
@allure.feature('Filter')
@allure.story('Free_Paid')
class Test_Master_Photo_Filter_Free_Paid:
    @pytest.fixture(autouse=True)
    def initial(self, shortcut):
        # shortcut
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist
        self.set_slider = self.page_edit.h_set_slider

    @pytest.fixture(scope="module")
    def data(self):
        data = {'last_result': True}
        yield data

    def last_is_fail(self, data):
        if not data['last_result']:
            data['last_result'] = True
            self.page_main.relaunch()
            return True
        return False


    @allure.title('Enter Filter')
    def test_filter_enter_filter(self, data, driver):
        func_name = inspect.stack()[0][3]
        logger(f"\n[Start] {func_name}")


        try:
            def is_element_present(element, locator):
                try:
                    element.find_element(locator[0], locator[1])
                    return True
                except Exception:
                    return False

        
            pro_tag_list = [True, True, True, False, False, True, False, False, True, False, True, False]
            self.page_edit.filter.start_with_filter('master photo')
            filter = self.elements(L.edit.filter.fliters)
            
            for i, filter in enumerate(filter):
                is_present = is_element_present(filter, L.edit.filter.pro_tag)
                if is_present == pro_tag_list[i]:
                    logger("PASS")
                else:
                    logger(f"Not match at index {i+1}")


        except Exception:
            traceback.print_exc()
            data['last_result'] = False
            raise Exception

    