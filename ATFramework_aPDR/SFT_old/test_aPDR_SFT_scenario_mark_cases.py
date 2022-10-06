import sys
from os.path import dirname as dir
sys.path.insert(0, (dir(dir(__file__))))
from pages.page_factory import PageFactory
from ATFramework.drivers.driver_factory import DriverFactory
from configs import app_config
from configs import driver_config
from ATFramework.utils.log import logger
import pytest

from .conftest import REPORT_INSTANCE
from .conftest import PACKAGE_NAME
from .conftest import TEST_MATERIAL_FOLDER
report = REPORT_INSTANCE

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
        self.report = report
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
    @report.exception_screenshot
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
        self.report.add_result('d206bce2-b32b-408f-a622-306add228ead', None, 'N/A')  # sce_02_02
        self.report.add_result('e7d8db6b-62b5-4553-b69d-4cff16e5844c', None, 'N/A', 'AT cannot verify')  # sce_02_02
        self.report.add_result('97a814da-ba03-4a8e-8359-1f8a99ab5f99', None, 'N/A', 'AT cannot verify')  # sce_02_02
        self.report.add_result('454f7f0b-1d60-4537-b43b-9c46e9417ea9', None, 'N/A',
                               '[AT] virtual keyboard cannot be located')  # sce_02_03
        self.report.add_result('e243c29f-42d3-4b92-8d26-ee619448f5c8', None, 'N/A', 'AT cannot verify')  # sce_02_03
        self.report.add_result('0782758a-b8bf-49d8-9f22-8ec8f949feb6', None, 'N/A', 'AT cannot verify')  # sce_02_03
        self.report.add_result('5b7a04c7-9fdc-4b44-85f4-85193238a443', None, 'N/A', 'AT cannot verify')  # sce_02_03
        self.report.add_result('36201cf1-37f8-4748-b423-cc661ebc437b', None, 'N/A', 'AT cannot verify')  # sce_02_04
        self.report.add_result('486d6387-3efb-4772-b921-bf58b8570da1', None, 'N/A', 'AT cannot verify')  # sce_02_04
        self.report.add_result('64792290-a8f8-499d-86be-34f6ee81d950', None, 'N/A', 'AT cannot verify')  # sce_02_04
        self.report.add_result('6f7e84e8-ef28-4bf7-a4d3-50af2456a462', None, 'N/A', 'AT cannot verify')  # sce_02_04
        self.report.add_result('b290da2b-fe2f-40ab-afe4-1057b30884f4', None, 'N/A', 'AT cannot verify')  # sce_02_04
        self.report.add_result('5f6d521f-6f91-4395-a1d1-069d57042e5f', None, 'N/A', 'AT cannot verify')  # sce_02_04
        self.report.add_result('79dbbac4-4661-45af-bb87-3edfdaad8804', None, 'N/A', 'AT cannot verify')  # sce_02_05
        self.report.add_result('44b758fc-d08f-4ea0-9733-e3b745e471c3', None, 'N/A', 'AT cannot verify')  # sce_02_06
        self.report.add_result('a56e7a9d-3d5f-4f0d-9697-165a0d01b25b', None, 'N/A', 'AT cannot verify')  # sce_02_06
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
        self.report.add_result('85e1312a-7802-4236-a21f-022626aeb00e', None, 'remove_item',
                               'AT: no entry')  # sce_01_01
        self.report.add_result('df3e9c61-ae64-475d-9b7d-505701ed2ec3', None, 'remove_item',
                               'AT: no entry')  # sce_01_02
        self.report.add_result('7276823d-afde-48f8-9056-ae819b9cd22a', None, 'remove_item',
                               'AT: no entry')  # sce_01_03
        self.report.add_result('191bb420-4257-4b81-8311-b3239445e589', None, 'remove_item',
                               'AT: no entry')  # sce_01_04
        self.report.add_result('657fd6b7-8ce8-4e84-8fc0-85d15df53014', None, 'remove_item',
                               'no toast message')  # sce_02_01
        self.report.add_result('4ed0836c-d665-4039-b3ab-f58959aa9ce5', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('eceb7942-fb14-49c7-93fd-c21b59a84b76', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('3fa98b4f-a4ca-4837-8481-c105038c2736', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('bfdbaaed-4814-45ad-adb4-dc4b8eb60e2b', None, 'remove_item',
                               'AT: no entry')  # sce_02_03
        self.report.add_result('6bb8826e-765e-4172-9ec8-2b1748c15a84', None, 'remove_item',
                               'AT: no entry')  # sce_02_04
        self.report.add_result('d612a2e9-7bd7-408b-b09e-e45267a2fdb0', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_02_06
        self.report.add_result('37f1bfac-be5a-413a-a5a6-cce801053f93', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_02_06
        self.report.add_result('d1f4af97-6926-49c9-a854-ddae5c5ebe8d', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_02_06
        self.report.add_result('accf336a-9ab9-4a23-85e4-f7272ba2ee95', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_02_06
        self.report.add_result('35d11f12-e465-4c0b-9eda-2c9b4d3f6cbe', None, 'remove_item',
                               'remove this item because no this behavior (it\'s from ACD android)')  # sce_02_06
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
        self.report.add_result('3e2fca27-37be-4204-834f-35285d9cd514', None, 'remove_item',
                               'AT: no entry')  # sce_06_01
        self.report.add_result('9330d7a9-8198-4653-844f-aadd5e993d12', None, 'remove_item',
                               'AT: no entry')  # sce_06_01
        self.report.add_result('ccd5481a-240f-4fb3-a656-7e4c1d3efaea', None, 'remove_item',
                               'AT: no entry')  # sce_06_01
        self.report.add_result('9384ad85-2b50-4651-9ca5-c8a1a6eb42dc', None, 'remove_item',
                               'AT: no entry')  # sce_06_01
        self.report.add_result('c07ff2ea-33e1-45ff-8c2c-dcfdaafbebf2', None, 'remove_item',
                               'AT: no entry')  # sce_06_01
        self.report.add_result('fb399ce8-8082-464b-935e-7829bb2399eb', None, 'remove_item',
                               'AT: no entry')  # sce_06_02
        self.report.add_result('4893c2dd-2ebd-4f26-9e10-cf99f5e7c019', None, 'remove_item',
                               'AT: no entry')  # sce_06_02
        self.report.add_result('526ed894-f818-45a5-abde-6783ffa0c6e7', None, 'remove_item',
                               'AT: no entry')  # sce_06_02
        self.report.add_result('73abfe8d-4e1a-44a6-b6f0-46dc2f652c88', None, 'remove_item',
                               'AT: no entry')  # sce_06_03
        self.report.add_result('8fd7d04b-207f-46f6-a869-4aec8cb04e89', None, 'remove_item',
                               'AT: no entry')  # sce_06_03
        self.report.add_result('60f01814-4d04-4f4c-a5d8-68d0263e21dc', None, 'remove_item',
                               'AT: no entry')  # sce_06_03

        
        self.report.add_result('1a34fe3f-ea2e-4203-a61f-8af323da0f2b', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('07777aa5-cb37-4d96-9d6b-078075e69030', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('e1ebc171-af2e-4bbd-9194-e5e9a990350d', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('8ea668d1-73a2-4975-b555-3f407fea379d', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('41e09f89-6707-4d68-8e8a-00ef6a7329cb', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('92d363d0-c8df-4cbc-85af-f9ab145aad5e', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('601058bb-f257-45a1-ac98-4f6bd2b1ad04', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('35361159-cce4-4915-9009-2b221f7a2eef', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('8160f133-eeab-42fb-81f3-83512ea7b21e', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('2ee82f19-0681-4217-ad15-75550ad5dfae', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('54912f40-2114-48f5-b1f2-41f7bd7c7ac5', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('53234dd1-0d9b-417e-91fe-06263e720224', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('b4f7944c-b080-457f-853e-2a1775c49ead', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('b6dd22b5-c057-4ebf-a3c9-5472b58f70df', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('38b3d6bf-8005-47f7-be41-b5d48f119517', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
        self.report.add_result('47daa03a-255c-4aae-a8e0-c22ba06c8e30', None, 'remove_item',
                               'AT: no entry')  # sce_05_01        
      
       
        self.report.add_result('7fc864c0-854c-41cc-8312-4632a8ce0675', None, 'remove_item',
                               'AT: no entry')  # sce_00_02       
        self.report.add_result('6bb8826e-765e-4172-9ec8-2b1748c15a84', None, 'remove_item',
                               'AT: no entry')  # sce_00_02       
        self.report.add_result('9e067d50-df7e-43e8-b76f-6cb36fc8d03d', None, 'remove_item',
                               'AT: no entry')  # sce_00_02        
        self.report.add_result('2e469c7d-aea7-417a-99bf-e0d440487249', None, 'remove_item',
                               'AT: no entry')  # sce_00_02       
        self.report.add_result('81ac64fb-ec6e-4762-a0b1-1ff786f9af0f', None, 'remove_item',
                               'AT: no entry')  # sce_00_02
        self.report.add_result('cdab4753-ecb9-430f-b3eb-ed0fd36b4761', None, 'remove_item',
                               'AT: no entry')  # sce_00_02
        self.report.add_result('848b90c4-da3b-48f6-b246-cd6daf4f497c', None, 'remove_item',
                               'AT: no entry')  # sce_00_02
        self.report.add_result('b0ccacbd-be6f-4d6f-9735-e0134f50ded7', None, 'remove_item',
                               'AT: no entry')  # sce_00_02
        self.report.add_result('20bcee25-7f62-45b1-98e9-501496df7c1b', None, 'remove_item',
                               'AT: no entry')  # sce_00_02
                               
                               
        self.report.add_result('35bdb1ab-dbba-45aa-ab6f-22ec495c0344', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('18600fa6-2720-4d35-8677-ac985eee1616', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('ea91473b-c83d-4d3c-ad4a-43da25128d18', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('e4bba393-2d8f-4001-8580-68a35eea7ecd', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('6a9cd909-4916-40a6-bbc6-2d905b693ec3', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('79abb5f6-bcc8-4c2e-a1c8-7d878c9e6cf8', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('5a237f73-d5ac-4dfa-b16a-585a39f384bd', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('1dc34369-00a6-4c3d-ad2d-951c5d94e3dd', None, 'remove_item',
                               'AT: no entry')  # sce_00_01
        self.report.add_result('f914eb95-c545-434b-8877-dd50e2a6e736', None, 'remove_item',
                               'AT: no entry')  # sce_00_01

        self.report.add_result('f790a46e-0ada-44db-a2ba-b37c8d25e67f', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('6ab82885-8dca-4d55-85d2-73d68015e693', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('c180a0d3-192a-4d8c-a6b8-b638f1ade340', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('3fba401e-927e-4816-91c5-e98bcf89cf3d', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('fafbe475-ef7d-49f2-8766-249f837f9411', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('41436d3e-7a5a-47a1-a43a-77cbcb6c767c', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('5490e801-e387-4300-9b3a-9ad560dc3dd6', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('2a09345a-34b3-4242-aada-637f51f96460', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('e8c853ff-5b53-467e-82bb-6427ef0d2c62', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('628eedeb-2b5b-473d-be47-89e8b70b4fd6', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('c159218d-cc36-4c29-8b62-bd7f9aae97e2', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('1e7653f6-9b46-4f49-9c48-ef080128e4a6', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('12226749-184d-4ab6-a50d-3966c97dffb4', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('eb684fa2-952f-44ce-a8ff-49de71e927fd', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('33395f3b-c382-4b85-8385-1c50e2ca8360', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('4285e51c-9c7c-427b-888b-438f7011a6ea', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('c7344e0c-64d6-4145-811c-25f6212de136', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('4fa3bb72-4d4e-419a-9f36-ae4801603b87', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('0d2f0536-dbbe-4698-99c8-61cc60295b40', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('1fcea73b-f469-49a8-920d-afeead1ae3fb', None, 'N/A', 'Old cases')  # sce_06_07
        self.report.add_result('160bea25-7706-438c-8658-36e4313640cb', None, 'N/A', 'Old cases')  # sce_06_07
        
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