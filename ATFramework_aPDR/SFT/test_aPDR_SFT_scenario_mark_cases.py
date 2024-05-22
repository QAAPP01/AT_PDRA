import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest


from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER


pdr_package = PACKAGE_NAME
test_material_folder = TEST_MATERIAL_FOLDER


class Test_SFT_Scenario_Mark_Case:
    @pytest.fixture(autouse=True)
    def initial(self):
        # ---- local mode ---
        from .conftest import DRIVER_DESIRED_CAPS
        global report
        logger('\n============<Init driver session>============')
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
        self.test_material_folder = test_material_folder
                                                              
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
    
    def test_sce_mark_case(self):
        # for AT N/A cases =====================================
        # self.report.add_result('e94b15b5-a219-45a3-a2ed-10648c201b11', 'N/A', None)  # N/A case
        self.report.add_result('b7171c98-b2b0-4d60-8833-85e29c1a1b9b', None, 'N/A')  # sce_01_02
        self.report.add_result('7e39264d-815e-4537-8bb2-b35b69094a00', None, 'N/A')  # sce_01_02
        self.report.add_result('29ac056d-3693-43a4-bc98-1ac3c7b72236', None, 'N/A')  # sce_01_02
        self.report.add_result('59dd6e26-431e-4f73-9fb5-3be533af86ee', None, 'N/A')  # sce_01_02
        self.report.add_result('2d38ece5-b483-4dd0-86ae-1684e1dbd665', None, 'N/A', 'AT cannot verify')  # sce_01_03
        self.report.add_result('edc3a0c2-4c2e-41ae-87d7-3aa7844b21df', None, 'N/A', 'AT cannot verify')  # sce_01_03
        self.report.add_result('c5211b58-f4a7-401a-bf1e-4a689f7b5760', None, 'N/A')  # sce_01_04
        self.report.add_result('3fd5f57a-c005-423d-bad1-eb1a496fe105', None, 'N/A')  # sce_01_04
        self.report.add_result('9d6f1ed6-7bf6-4c98-9e3b-e1d2f1377e29', None, 'N/A')  # sce_01_04
        self.report.add_result('3c2b77dd-a778-4756-9ec3-4c7ee6fab4d0', None, 'N/A')  # sce_01_04
        self.report.add_result('5b7a04c7-9fdc-4b44-85f4-85193238a443', None, 'N/A', 'AT cannot verify')  # sce_02_03
        self.report.add_result('55c9924b-92f8-49be-a833-dab1c73faeaa', None, 'N/A', 'AT cannot verify')  # sce_03_02
        self.report.add_result('d68687b0-12aa-4b2b-88e2-99f08a7f7182', None, 'N/A', 'AT cannot verify')  # sce_03_02
        self.report.add_result('11417f73-b6a3-4c60-a6cb-29b5a0f4a414', None, 'N/A',
                               '[AT] virtual keyboard cannot be located')  # sce_03_03
        self.report.add_result('15009a4f-aef3-4e36-9ca9-2fd900e3ae20', None, 'N/A', 'AT cannot verify')  # sce_03_03
        self.report.add_result('97550987-5c6b-4c04-8f29-674f774d5a19', None, 'N/A', 'AT cannot verify')  # sce_03_03
        self.report.add_result('ef3c70fb-b597-4b08-bb8f-3b9893fc676f', None, 'N/A', 'AT cannot verify')  # sce_03_03
        self.report.add_result('1f8f940f-9e18-476e-86a1-55cc402cdbba', None, 'N/A', 'AT cannot verify')  # sce_03_04
        self.report.add_result('d776bfc3-8aa0-4b91-a929-5e003d89a877', None, 'N/A', 'AT cannot verify')  # sce_03_04
        self.report.add_result('284c30ba-4011-4640-9934-340857b777c5', None, 'N/A', 'AT cannot verify')  # sce_03_04
        self.report.add_result('fc742f14-bb01-4b2e-82dc-ce853aafa996', None, 'N/A', 'AT cannot verify')  # sce_03_04
        self.report.add_result('d85845dd-fbe6-4dab-b0c5-eb0a8401370d', None, 'N/A', 'AT cannot verify')  # sce_03_04
        self.report.add_result('e9220bd0-d467-4f32-b359-1d01be1cf2f2', None, 'N/A', 'AT cannot verify')  # sce_03_04
        self.report.add_result('72986842-2a8e-45e6-bfa8-66b7aec49487', None, 'N/A', 'AT cannot verify')  # sce_03_05
        self.report.add_result('05e8ef40-b638-4499-a281-7ab01d7cb2d8', None, 'N/A', 'AT cannot verify')  # sce_03_06
        self.report.add_result('22754649-7066-4161-89bb-4615d383ba22', None, 'N/A', 'AT cannot verify')  # sce_03_06
        self.report.add_result('2ad5ff77-ae01-487e-9c21-597cc1a9e0fb', None, 'N/A', 'AT cannot verify')  # sce_04_05

        # for removed cases =====================================
        # self.report.add_result('e94b15b5-a219-45a3-a2ed-10648c201b11', 'remove_item', None,
        #                        'AT: no entry')  # remove case
        self.report.add_result('4ed0836c-d665-4039-b3ab-f58959aa9ce5', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('eceb7942-fb14-49c7-93fd-c21b59a84b76', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('3fa98b4f-a4ca-4837-8481-c105038c2736', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('bfdbaaed-4814-45ad-adb4-dc4b8eb60e2b', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('bd0a63b7-5fdf-42b9-80a2-74db1ffe8a60', None, 'remove_item',
                               'AT: no entry')  # sce_03_01
        self.report.add_result('6d84b550-d50c-4883-88c4-1f5f42205db5', None, 'remove_item',
                               'AT: no entry')  # sce_03_03
        self.report.add_result('3734fa7f-8a78-4515-b90d-45dbc0596513', None, 'remove_item',
                               'AT: no entry')  # sce_03_03
        self.report.add_result('6e192395-ad05-4d07-a0f2-749bf0d382c3', None, 'remove_item',
                               'AT: no entry')  # sce_03_03
        self.report.add_result('e080b15a-4507-4776-a5f3-dfa509a35382', None, 'remove_item',
                               'AT: no entry')  # sce_03_03
        self.report.add_result('8a9fd489-92e6-4b67-911c-896e7d932256', None, 'remove_item',
                               'AT: no entry')  # sce_03_04
        self.report.add_result('c2f7f789-45b5-4725-833a-370a5ecaa599', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_03_06
        self.report.add_result('b3d70a9a-83ed-467f-a0e4-ffa115af99cd', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_03_06
        self.report.add_result('538aa9c9-6597-4ad3-942d-7baf8f4df682', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_03_06
        self.report.add_result('aee017dc-3deb-44ac-9ed2-2c8cb941db5f', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_03_06
        self.report.add_result('fe82d100-ebff-4e19-b7fd-5f2902f95cb3', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_03_06

        self.report.add_result('0f820f85-9c3a-4788-b25c-f4d0a3fafd2e', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('5795e732-326a-4e2f-9c28-419c542eff77', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('14e447f6-c072-4aed-b36d-1d6682a6ee02', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('11323034-483c-4cd5-8f73-f8461a9004ee', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('41b07933-a223-4f42-9929-68e6499e3564', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('a7144dbf-99b4-40e3-a7a8-b4df3912a04f', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('8a556904-5276-45ab-a38a-afd07d931c0e', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('8a9c48d8-5458-4626-9a28-51d0bd6c8049', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('fc198839-67d8-4c3e-9ac9-08623c52d5ab', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('567ce7ec-e3dd-41e3-a616-72ab3e87cd9b', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('2acf6466-c4a6-4263-a8e3-7efc4648dc87', None, 'N/A', 'Cannot verify on AT')  # sce_06_07
        self.report.add_result('eb07864a-2bf4-437f-b2bb-55f7dfc53a1b', None, 'N/A', 'Cannot verify on AT')  # sce_06_07