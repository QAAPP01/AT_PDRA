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

class Test_SFT_Scenario_Music_and_Sound_Clips:
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
    def test_sce_music(self):
        #self.report.start_uuid('')
        media_list = ['slow_motion.mp4', 'png.png']
        
        # Classical : 4 songs ~ 1 free
        classical_list = [  'With Honors', 'Acceptance', 'Andante Piano', 'Andante Stately', 
                            'Christmas Even Sn', 'Minuet Piano', 'Minuet Positive', 'Pompous March', 'Rondo']
        # Comedy : 25 songs ~ 3 free
        comedy_list = [ 'Crisp Afternoon', 'Funny Tune', 'New Day', 'Aloa Summer', 'Be Party',    
                        'Funny Rider', 'Holiday Connection', "It's Funny", 'Jollyboat', 
                        'Lazy Daisy', 'Living On River', 'Mystery Shopper', 'Petit Prince', 
                        'Prism', 'Rag Time Player Pine', 'Rag Time Player Rag', 'Sense Of Pleasure', 
                        'Shipbar', 'Shopping Sale', 'Strip Cartoon', 'The Bear Family', 'This And That', 
                        'Walk In The Park', 'Worth A Day', 'Young Minds']
        # Country : 17 songs ~ 2 free
        country_list = ['Country Rain', 'Parting Glance', 'Apple Cider', 'Boot Cut', 
                        'Cowboys Song', 'Different Opinions', 'Enikki', 'Friendly', 
                        'Kaze', 'Madobe No Table', 'Old Time Reunion', 'Outdoor Weekend', 
                        'Positive', 'Quiet Desire', 'Silent Night (Acoustic)', 
                        'Steel And Wood', 'Tsukiakari']
        # Electro : 17 songs ~ 0 free
        electro_list = ['A Chill In The Air', 'Beautiful Life', 'Breathe It In', 
                        'Daily Commerce', 'Delectable', 'Downbeat Thumpin', 'Easy Driving', 
                        'Gabriella', 'Gentle Current', 'Hairstylist', 'Livid Bass', 'Mezzomondo', 
                        'Samurai', 'Sign Your Name', 'Smooth Sailing', 'Stiletto', 'Techoid Loft']
        # Jazz : 21 songs ~ 0 free
        jazz_list = [ 'Auld Lang Syne Jazz', 'Bada Ba Baa', 'Carefree', 'Copacabana', 
                      'Deck Halls Jazzy A', 'Deck Halls Jazzy U', 'Jingle Bells Jazz A', 
                      'Leise rieselt der Schnee', 'Macht hoch die Tuer', 'More Of The Other', 
                      'Rocking Joy World', 'Seventies Show', 'Smoothly Jazzed', 'Table For Two', 
                      'The 12 Day Chris J', 'The Blue Plate Spe', 'Three Times Seven', 'Today', 
                      'We Wish You Merry JA', 'We Wish You Merry JU', 'Whisky Boogie' ]
        # Lounge : 13 songs ~ 1 free      
        lounge_list = [ 'Bill Dee Harlem', 'Been There, Done That', 'Flat Out', 'Flying Airs', 
                        'Horizon Swim', "I Didn't Mean It", 'Let The Record Sound', 'Luxury Jazz', 
                        'Music Hall', 'Music Loft', 'Piano Moods', 'Sunlight Reef', 'We Are Fashion' ]
                        
        # Musical Jingles : 5 songs ~ 4 free
        musicaljingles_list = [ 'Dream Breath', 'Fly Home (sting)', 'Friendly (sting)', 
                                'Heaven (sting)', 'One Step Closer']
        # Orchestral : 43 songs ~ 8 free
        orchestral_list = [ 'Action', 'Deck The Halls', 'Jingle Bells', 'O Come O Ye Faithful', 
                            'Picnic', 'Satougashi No Waltz', 'Transition,Logo,Woodwinds,Serene', 
                            'We Wish You A Merry Christmas', 'A Sweet Dream', 'Akiramenai Monotachi', 
                            'Atarashii Michi', 'Auld Lang Syne Trad', 'Condition Green', 'Dramatic Melody', 
                            'Empty Streets', 'Eternity', 'Fanfare,Regal,Loop', 'Froehliche Weihnacht ueberall', 
                            'Latin Lover', 'Lawless Direction', 'Leaving Home', 'Legal Balance', 
                            'Light And Sunshine', 'Lost Moments', 'Murasakiiro No Yume', 'Nightly Steps', 
                            'No Surrender', 'Opening', 'Prairie Bound', 'Shinshun', 'Silent Night', 
                            'Spectacle', 'Spy', 'Suesser die Glocken nie klingen', 'The First Noel', 
                            'The Gavel', 'Thrills And Spills', 'Transition,Logo,Brass,Regal,Soft', 
                            'Transition,Logo,Orchestra,Confident', 'Transition,Logo,Orchestra,Friendly', 
                            'Transition,Logo,Orchestra,Reveal', 'Vom Himmel hoch da komm ich her', 
                            "Zion's Daughter" ]
        # Piano : 30 songs ~ 1 free
        piano_list = [ 'Natsukashii Hibi', 'A Positive Med Piano 1', 'A Positive Med Piano 2', 'A Positive Slow Piano 2', 
				'Akogare', 'Ashita', 'Beautiful Morning', 'Candle Light', 'Felice', 'Gratitude', 'HNY Auld Lang Syne', 
				'Happiness', 'Hatsuyuki', 'Here Comes The Bride', 'Kakehiki', 'Mayonaka No Merry-Go-Round', 'Melancholy Piano War', 
				'Nichiyoubi', 'North Wind', 'Passages', 'Pearl', 'Playground', 'Prospect', 'Silent Movies Unde', 'Simple Life', 
				'Summer Dreaming', 'Tomorrow', 'Ushiro No Shoomen', 'Wonderful Piano', 'Youchien' ]
        # Pop : 27 songs ~ 4 free
        pop_list = [ 'Early Morning', 'Funk Sauce', 'Long Ago', 'TV Theme' ,'After All', 'Around The Block And Back', 
                     'Bright Sunshine', 'Campari And Orange', 'Do It Already', 'Editors Life', 
                     'Evening by the Fireplace', 'Fly Home', 'Good King Wencheslas', 'Heaven', 
                     'Kling Gloeckchen', 'Monday', "Morgen Kinder wird's was geben", 'My Little World', 
                     'Ninja', 'Shingakki', 'Spin Bottle', 'Strut Your Stuff', 'Swampland', 'Texas Sky', 
                     'Walk On', "Whistler's Dream", 'Wilder Aisles' ]
        # Rock : 25 songs ~ 8 free
        rock_list = [ '1983', 'Creepy', 'Darkness', 'Joy To The World', 'Jungle Monkey', 
                      'Mellow Day', 'Shady', 'Way Home', 'Access Time', 'Change Is Coming', 
                      'Fight For The Top', 'Filth Funk', 'Generation Hoverboard', 'Get It', 
                      'Gone Away', 'Make Me', 'Red Line Speeder', 'Rocking Christmas', 'Ryujin', 
                      'Saturday Suburbs', 'Second Leg', 'Shunkashuutoo', 'Slide Dog', 
                      'Strong', 'Tsuwamonotachi' ]
        # World : 13 songs ~ 0 free
        world_list = [ 'Bangkok Evening', 'Early Frost', 'Fuujin', 'Gift Of The Islands', 'Hyakka Ryoran',
                       'Kaikyo', 'Pineapple Republic', 'Shinonome', 'Shippuu', 'Stir The Sauce', 
                       'Tabidachi', 'Varanasi Sunset', 'Yuusui', 'Zendoji Temple Song' ]
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_music_library()
        page_media.select_media_by_text('Music')
        time.sleep(3)
        page_edit.el(L.import_media.music_library.pdr_tab).click()
        time.sleep(3)
        # Classical Folder
        udid = ['d1084492-ac6f-460f-bbbe-3d4cd6b445ec', '5d47b19e-d058-43c5-a0f2-9512367703d2', 
                'cdaf609d-a09e-47fa-97f8-008ad37f2549', 'a6846594-669a-4b2c-a0b9-9b8fcc5e20dd',
                '30ab29ed-4aaa-4dc9-937c-cd903b003981', 'c3498200-3c08-4be9-95d6-a7f14463f9c2',
                '4ca6ea08-e62f-41f5-8b55-f5114cec8c1b', '3763a7a3-5a74-45c4-a88f-5021f61f693e',
                '9d1675b1-f02c-4519-be3f-8f587bd9bd94']
        page_media.select_media_by_text('Classical')
        index = 0
        for name in classical_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Comedy Folder
        udid = ['511daa93-82cb-4356-81aa-7196a41bcf48', '10817069-66e8-40de-a54e-c12dd0b30808', 
                'a630a4b1-58f9-4116-9207-ad29182ac466', 'a7cf0557-b1b1-4598-9a5f-70a7bb33bbf2',
                '1829c0dc-7678-453f-b3a9-cffec1daced4', 'e0538e86-2ce4-4fca-b13e-6aa854d393b5',
                '7d5e7644-53a9-4141-b711-dac2185732be', 'ab43bc7e-adc5-4b98-b7e3-ecf21cc7c685',
                'dc4c9e76-8deb-473f-b1d6-db70693a8feb', 'f81ab04f-0f28-437d-a819-6419d2000b91',
                'f99aa9fa-e463-438e-821e-ebbe79621b84', 'ad2f7ecd-1c0a-4747-bd1b-ea1bc145417e', 
                '31791621-31c8-442e-97dd-703606c1944b', 'b0ee3ed1-81e1-4874-a107-b54f013023a6',
                '0dd14870-f132-4535-b2e3-8b1a98960045', '2ea6ab64-deef-44ad-ac4e-2275d63bec3c',
                'b73c4e75-c147-4e94-b8f2-836aea844420', '19e56268-b343-4a36-9cd0-332f2d43349c',
                '94e170f1-1204-41ea-9cbb-417a991525e2', '20951c64-ac99-4f4d-bdc4-53444bba4d3b', 
                '51da776b-480e-4516-9833-faad8a458c61', '772e425e-e0de-43c1-98df-f07d0c0df5cf', 
                '3f51bc39-323e-436d-856c-f01075845b8e', '484a850c-58d4-45ba-8119-1224523cae8e', 
                '94da79ec-c820-4d2b-8464-ae18b931e53e' ]
        page_media.select_media_by_text('Comedy')
        index = 0
        for name in comedy_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
        
        page_edit.el(L.edit.menu.back).click()
        
        # Country Folder
        udid = ['92604302-654c-4335-9ccd-8216071a63d4', '217843be-201c-410e-b166-10f0a5df920c',
                '70cb8e80-28ac-427e-ad61-150883d8e15f', 'ccab9dab-d596-43bf-a42a-ee7ca4afcc25',
                'ea9ee7dd-3db4-476c-b002-68ad73c900ef', 'f4366b07-3712-4e4b-9011-ca6099185840',
                'a0e13179-8933-4439-9791-34b5225c979a', '755daa94-13f5-4ae0-a669-57be2d8a1c80',
                '3aaac0fc-7ace-4bb8-9a2b-28e56c0f67bc', '1c49939e-8340-4d00-a69e-3606730be084',
                '74266e39-6cf0-446f-bc8c-7f340bde5b47', '67d889cd-c991-4e87-afa6-f371ad548a20',
                '56e379f5-cc1d-43cb-870a-a34c1c51cf80', 'd0955fd9-a194-4fac-a25e-9b965ccc0720',
                '40561774-4221-4b39-b4e6-a0c209b02321', '8fe66279-54d2-4d9d-a84d-4185d478bdda',
                '366a4452-a48c-4026-b673-e566d5bb6c32' ]
        page_media.select_media_by_text('Country')
        index = 0
        for name in country_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)

        page_edit.el(L.edit.menu.back).click()
        
        # Electro Folder
        udid = ['c0d64d4d-873f-4eae-9287-873098d774e2', 'c5f609ca-873b-48f1-8c03-96cae37333c8', 
                '5b2fdc9b-8162-4cf2-84fc-073826206cd3', '7107f912-f17f-46f6-b928-282916917ba3', 
                '1c6cb9d5-b2c1-4786-a6cc-bc95d02077a4', '76a87309-ee4e-4991-9a51-334ed63a8b8e', 
                'b6c5f747-0845-4d41-94eb-71fa2c245876', '031ae052-6ee4-4ae0-85fc-5a2035d2f357', 
                '910c7937-081b-4803-9ba1-2cdc3a0dcf22', 'c89f669b-9d35-461c-99ae-af5d3f1720e4', 
                'dc3dc6b2-476f-4f59-9e58-af713459abde', '13b944bd-07e0-4a09-ac9c-709be53d54e2', 
                '668304bb-3927-4693-8b69-fdef10a14128', 'dc676d8c-2d19-4d36-b2ea-3ba70707cbe7', 
                '6f15f819-8799-4950-b172-d002c981f8f5', '44fe7b62-ff64-4ffb-934c-7ea25649739f',
                '90fb8afb-38d1-48cd-a2f3-c86f4e3bb4b9' ]
        page_media.select_media_by_text('Electro')
        index = 0
        for name in electro_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
          
        page_edit.el(L.edit.menu.back).click()
        
        # Jazz Folder
        udid = ['c9f67dee-ad0b-456f-b5a6-eb7998e9cea2', 'e685bae2-baf1-44be-bf9c-23bcc3fbb9a0', 
                '7083ecf5-ab92-4703-878d-c06905f2b789', '78eb5195-6e7c-4706-86da-1c87b779aa43', 
                'bb71b492-7a47-4aa9-8129-960c8d4c7be0', '1f6ce23f-8cfd-4210-9eb0-2572c905231d', 
                '56bd61af-10b0-4e91-b7c2-53d7e5993e9c', 'a4e4acd5-102d-4880-8df9-64417441e5b5', 
                'ec915579-56c2-4ca3-a971-d0dd38f23e2a', '4a4a50a7-21fa-489e-944a-971bad9fc6eb', 
                'c087375f-8558-4d16-9d3e-e258edd6cfb0', '7100e060-878f-4467-bb42-10a1ba07a715', 
                'ea767acd-faf7-41bb-aff7-5d5d6c71c445', 'd4332654-2c90-40e8-abca-c2f19bb5153e', 
                '2e6f00f3-4b9f-490b-8347-324db0f34e29', '19da89b3-650d-47a9-a260-aaca8ecedaa8', 
                '3b849fe6-484f-4541-a0e8-cd2fc97f6c5f', '4ca118e0-5f81-45ca-a40f-3a2cfb242cb1', 
                '476804a8-c1c6-49b6-b180-747623d87cad', '6e141e7d-23c5-4860-a927-001d35929641', 
                '4d8a04b9-f7e6-4405-be42-5c92bff07106' ]
        page_media.select_media_by_text('Jazz')
        index = 0
        for name in jazz_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
          
        page_edit.el(L.edit.menu.back).click()
        
        # Lounge Folder
        udid = ['50a008e9-dc25-40c7-96e5-6e1a8f6a4fe7', '02af5f07-7bca-4414-9c34-53e688c7772a', 
                '61cfb7e9-a3a7-45d0-bfba-935a4a947467', '3dc2b100-c272-4c35-a734-ae9ed620032a', 
                '1ed5d8e6-5886-4715-94ec-376bcb727b33', '6b3d27c8-f4d1-4ca9-949a-0f7f9a49b606', 
                '02785000-a0a8-4d80-b18e-b52da4c7ec01', '90ef048e-5364-484a-a2e7-b6397c4dee7f', 
                '81b3a975-4ac2-4360-b668-d142bd05ad83', 'fa26e3f7-6607-4c98-80ad-5454e29628a7', 
                'aaf71bb0-9ee4-4e0b-82fe-c12b47be96d2', '52387e13-9801-40b6-95bd-a7a09401be10', 
                'd059e2bd-2a09-4e6c-ad1e-023b8eebdd42']
        page_media.select_media_by_text('Lounge')
        index = 0
        for name in lounge_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
         
        page_edit.el(L.edit.menu.back).click()
        
        # Musical Jingles Folder
        udid = ['76ce8779-8071-42d9-87ea-b0eaac0d804f', 'a5c56039-cf4d-48bf-b655-3dfa6b67699c',
                '56e79b4a-381a-4071-b5d6-38b3ce05b5e4', '186c4526-edf5-40f4-a2ff-b4da1330e67e',
                '42a4dbc9-0c66-4cc9-9b93-de76047d06c8']
        page_media.select_media_by_text('Musical Jingles')
        index = 0
        for name in musicaljingles_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)

        page_edit.el(L.edit.menu.back).click()
        
        # Orchestral Folder
        udid = ['444d2966-d78d-418d-8486-6fd062e44c95', '4327242b-75f0-41c3-96dd-7387c3e3cbe0', 
                'd10f960a-22b4-45d1-93b8-4a1b46fb1a8a', 'd9e76960-1619-4921-a5f1-9b17bb44d299', 
                'd8d46442-e7a8-427d-a144-e0bcbb8844e5', 'c5eaab0f-e930-447c-b355-fe60915fe045', 
                'ff4fe1f8-1206-4fad-a355-0b914329cd4f', '4d74deab-36af-4b01-81b9-e452c5b26e43', 
                '7a2df454-98e0-4eee-b117-5f1f23c21635', 'b454f4a4-bdd3-49b4-8514-4e01768034d2', 
                'a6c7c337-978b-4b64-af2c-0fc8c7f53e3d', '1c225335-9962-45d4-a0c0-4051932fe24a', 
                '49d8df67-0e59-426c-9453-5a10cfeafe2f', '46f0dd64-0d52-4d9f-8273-5772702447a0', 
                '62cdf523-7c81-4c16-ae88-e7a3e1cb6e3b', 'ad76f154-cb49-46f2-b71d-c5dba1e1a501', 
                '7723738e-73ed-4927-9769-91a212aff8d3', '6128b4c4-201b-4025-9576-4425fc549b99', 
                'd14e2e28-9697-4c7f-bf27-73b4fef9dd33', 'd127da37-cc30-4d8a-95d3-4c971f57d6c4', 
                '6d6a58fb-a879-4901-9702-db91980d20cd', '6c593c93-ec42-49f0-9e39-23e092d5b4d6', 
                '506566d1-4e44-46c0-af68-8dbfe24b872c', '795b35ad-0cb0-4155-92ee-900a47ac62d8', 
                'd53de6e8-6f98-4813-8911-ddf6d449fb90', 'c93e3c71-a2f7-446e-a9f5-f020d10482d6', 
                '51060e1a-5118-4f44-943b-5c1b9495a959', '14fc4910-8d74-4a31-82af-70e0b228270a', 
                'd5ee9257-bbd5-4a60-81a2-5fd7ded2d260', 'eeea7a13-21c0-48d0-acda-64cda825e358', 
                'a44cf353-b33a-41aa-a964-f8958317f153', 'ab89598b-1035-4061-a907-03643bf9b054', 
                'eb98ecc1-d95d-4711-8dae-a182ccc14465', '7f3b2282-d182-4f2b-9350-113b8d6c7b42', 
                '27cc399b-f115-4403-9474-7fb7bf26bcac', '3488d341-96d9-4a0d-ad87-c898cb7976c1', 
                'e9a55fdb-e4c5-4693-a515-7b6b24cebd4d', 'da0d0f93-6d41-4e60-bc29-5d9f5c983671', 
                '91985a79-322a-4e77-b663-5c4d1b505633', '24f92484-570f-4577-83f0-66d6aee3a09a', 
                'f6be8e1f-abe8-4e90-b6cd-7c0b3edfc241', '964fc8ad-8c6e-4d6c-9571-ef4e80b240e0', 
                'deca7c9d-d7eb-40d5-bf20-fbba73564841']
        page_media.select_media_by_text('Orchestral')
        index = 0
        for name in orchestral_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1  
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)

        page_edit.el(L.edit.menu.back).click()
        
        # Piano Folder
        udid = ['a5b59d4f-ad59-4248-8215-8b6e85806642', '6804737f-5de7-49e8-907d-1c8e0f1d3047', 
				'54334354-254f-4790-8e8b-da76e5508a16', 'd1469985-85b2-4834-b8f7-13c985ec5d8f', 
				'963867aa-f23d-4303-9cf7-67e83c4e5a7d', '63d2eb0f-95a6-401e-b6f9-43540187dfeb', 
				'7171e9dc-0b84-4e8f-8708-56085d5fd075', '61c0e3c0-1cf3-45f1-8081-46538b6a31cc', 
				'5abd6dba-c5e6-4979-b416-999d7f29e8b5', '637c7dc6-76c5-4eee-92ec-43047e3f909f', 
				'08a48025-ca01-453e-bb88-f2d4a96d6baf', '793b4b8e-93af-4cc2-99c9-cefe20fb85e1', 
				'4aa943a3-276a-4814-9a18-0f9f4580fd38', 'f1d3f4e0-259a-4d56-b984-e1cb718131f3', 
				'e5e5789a-af19-446a-b8c2-acfb675db799', '3e329abb-f572-489e-a68e-31c24a7f68df', 
				'3fd956ca-c44a-42bf-ae3e-719dca1ead4e', 'fe21f1d3-d5f2-4c6b-8a6e-2ee1523f9a69', 
				'72e394b4-841d-41b5-8463-5dcfb3f6c9d1', 'c85611a0-34d6-48da-b6be-c262b05b4525', 
				'c3b08232-3e15-4c14-bc1c-b53bcbec40f8', '176f65ab-8009-4267-be0f-c64d2e40c3cc', 
				'f2e9fe43-25b5-423a-b09b-0fcdfcba8af1', 'd5dd4275-459c-4e2d-8c30-263d35477b32', 
				'c5a6d0cf-e411-4d58-9d61-29d85b5bb3ab', '2b7c01a9-8078-482e-a41c-a592f02fa7e8', 
				'67be2809-642c-4812-b81a-1f75a2d47315', '6c42cd4d-a068-4223-b0a1-4095c2e91f0e', 
				'f0bb4937-5c67-480b-b055-dee3554aafa2', 'e275ebf5-b813-4810-a846-faf88c023a06']
        page_media.select_media_by_text('Piano')
        index = 0
        for name in piano_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)

        page_edit.el(L.edit.menu.back).click()
        
        # Pop Folder
        udid = ['f8a3fcb1-4824-4a2a-af44-dd3e217286da', '8343647f-95d1-4705-9d55-a8745f51c041', 
                'df606d81-52b4-4150-9a78-fe786962f68d', 'f50f1369-5f3a-4934-bc89-2f657ead2d84', 
                '2c063391-61ab-4c4c-8fca-e2224f3e9398', '754b43ea-eef6-444f-81f5-09be359b527f', 
                'e7a2e322-2f6c-4bd8-8644-641eed209954', 'e4f73fa6-21a3-4f68-a4da-0d8de68e1acb', 
                'f4616446-f36b-4443-80d6-c184212c7f35', '0ba78d4e-e14e-4a58-8ecf-17143e978b74', 
                '6cd350ce-5d3a-4b4e-8ce5-03926260d5f4', 'c267f724-ee24-41f4-a602-a3e400f88db8', 
                'fbed9372-f217-46a0-870a-bd8eccb25c5f', '14241183-b66a-4c11-a9f4-01c837d0ebce', 
                '290036c8-3a6b-45b3-aad5-7ca09761c518', '4223c172-236c-43f3-955a-8ad058a28c2b', 
                'ad9ddb18-f77e-4cd0-9c5a-07aabd6ce9d7', '31e8a515-a895-4b1f-9360-62d524cb5243', 
                '81f5f4d1-dae1-4d12-b1bc-0d3781afc5af', 'e58c27b9-f900-408a-be8e-d2455753d3de', 
                '5da76e49-3d9f-4d56-a7d9-fb65de03b924', '75d03850-c378-415b-948e-5637518bae5b', 
                '1c95521b-e18c-4169-8fda-d61648f9aaf0', '1366fa03-f14f-4c43-8b88-b93c3a85b951', 
                'c4311aab-ceca-4c64-9142-1f56b406ebe0', '1a7159b5-49ef-4e93-aaff-faf1f0e0a78c', 
                '89225330-9d25-4808-ac47-f2892077fd76']
        page_media.select_media_by_text('Pop')
        index = 0
        for name in pop_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)

        page_edit.el(L.edit.menu.back).click()
        
        # Rock Folder
        udid = ['7a913f29-f6d9-4ed2-b14c-0ab65a4ff71f', '957e7a21-4d32-4a8b-87d2-5295cc9c70cd', 
                '005be138-360b-4d40-9ece-11da474610e0', 'b56fbfa6-4090-4111-84f3-3c9bab0b1919', 
                '61237a62-b5e9-4782-b275-87672c0177b4', 'a15d4d13-cbbd-4f2a-9aac-ea844e5fafa8', 
                '6fb8bcdc-3874-4ea9-a77f-439e9974d1f9', '7e5e49cf-f894-4074-ab36-9ee7ac769770', 
                '8919fc31-11d5-4f1d-9509-647e36ff0b88', 'f2f2f5ca-3c69-4614-b28c-d86ef4bb3197', 
                'cf5b2617-6500-40c7-a142-364368252a30', 'c1994e62-9557-4f24-b5e6-72239d616727', 
                '08090f02-b34a-4e14-b2ce-f6d0cf572fd0', '450b89e8-511d-424b-8767-56db7446118c', 
                '215c58d8-83bb-4e9c-ac06-44559af59348', 'dc6f8ed0-c96c-45bc-a194-57e10ebd882a', 
                '9929c7c4-6ef1-4a90-a5a4-2b642df55a9b', '73f96d56-12f4-44fe-aa17-e6605689526d', 
                'd3d2bfe0-874c-4094-b47e-4614993c2678', '89262fcf-b001-4ee4-a368-cab732f4e792', 
                'aa2eb353-8215-46cc-8c46-311126655da7', '3f0deb83-58b7-460c-b9be-aad1b1a74196', 
                '226a343b-74c1-43f3-8dd8-c6556bd15bc0', 'a2e79d69-f533-4e51-8eb3-cfbc4aef108b', 
                '83e75b1b-0a05-4836-b32e-47801f7796d2']
        page_media.select_media_by_text('Rock')
        index = 0
        for name in rock_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)

        page_edit.el(L.edit.menu.back).click()
        
        # World Folder
        udid = ['6143b80b-675c-4904-93ec-7116b2162803', 'c3093168-99d2-4f8a-b5c7-402615bc948f', 
                '159e1048-25bc-435e-a7d8-300934052531', '92035301-1ba3-40e4-a7bd-580e6bdadf7f', 
                '1d33f20d-2144-4734-8bb2-2897f48a66ba', '7bd79946-f6f3-4739-8d79-f8b73d3f6cae', 
                '2292c132-2b67-4303-adfe-e9058b97e3d3', '1fc1b762-55c9-4ed3-b243-4cb3f40bccaf', 
                '8d76820b-f497-4bee-bcf5-1eb1bfe12680', '39f40c13-1ad6-4856-98d6-115fb22f461b', 
                'f9f9a36d-4a9a-4c92-99ab-90dd1533015c', 'ac3cd1bb-7069-445a-b7cc-b30d1d331f30', 
                'c4dd0a41-6684-4f16-9672-c4f01b9a0d6e', '16555a0d-6819-4e31-a185-5834c0dd52c5']
        page_media.select_media_by_text('World')
        index = 0
        for name in world_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
    #@pytest.mark.skip
    @report.exception_screenshot
    def test_sce_sound(self):
        
        media_list = ['png.png']
        page_main = PageFactory().get_page_object("main_page", self.driver)
        page_edit = PageFactory().get_page_object("edit", self.driver)
        page_media = PageFactory().get_page_object("import_media", self.driver)
        timeline_settings = PageFactory().get_page_object("timeline_settings", self.driver)
     
        # create existed 16_9 project
        project_title = '16_9'
        page_main.reset_project_list(self.device_udid, pdr_package, project_title)
        page_main.select_existed_project_by_title(project_title)
        page_main.el(L.main.project_info.btn_edit_project).click()
        page_edit.el(L.edit.menu.import_media).click()
        page_media.switch_to_music_library()
        page_media.select_media_by_text('Sound Clips')
        page_media.el(L.import_media.music_server_library.tab_sound_clip).click()
        
        # Animals Folder : 54 clips
        animals_list = ['Cat01', 'Cat02', 'Cat03', 'Cat04', 'Cat05', 'Cat06', 'Cat07', 
                        'Cicadas02', 'Cricket', 'Crows', 'Dog Bark02', 'Dog Bark03', 'Dog Bark04', 
                        'Dog Bark05', 'Dog Bark06', 'Dog Bark07', 'Dog Bark08', 'Dog Bark09', 
                        'Dog Bark10', 'Dog Bark11', 'Flies', 'Frog', 'Frogs', 'Animal drink', 
                        'Animal drink bubbling', 'Animal eat crunch', 'Bird wings flap', 'Cat eat', 
                        'Cattle', 'Cicadas01', 'Cock', 'Cow burp', 'Cow defecate', 'Cow eat breathe', 
                        'Cow moo', 'Cow scream', 'Dog Bark01', 'Dog border collie bark', 'Dog labrador bark', 
                        'Donkey bray cow moo', 'Elephant', 'Flying Birds02', 'Goat Eat  Carrot', 
                        'Goat Kid Scream', 'Horse', 'Horse Gallop Asphalt', 'Horse Nicker Neigh', 
                        'Lion', 'Owl', 'Pig Grunt', 'Pig Herd Grunt Scream', 'Pig Herd Scream', 'Sparrows', 'Wolf' ]
                        
        udid = ['0b59da80-bb5f-4fbc-938e-a9f83adc930b', '1850a9c5-9941-4e59-a57c-e78040ca3b2f', 
                '5acb726c-9f70-4dc9-b2b5-24e23b30cea9', '71d5a609-eded-4b81-aa36-535fdf81d7cd', 
                'b45e6313-ce83-48ac-a41d-cf5302077edb', '435dc368-1c23-46bb-89cb-d26c8f6b83d6', 
                '651d6dc8-69eb-43f3-9f1c-5a3ca0b075f4', 'ea7ceac9-8a5d-4c15-96b4-53b1e3f21d1c', 
                '6dc80b6d-d652-4db4-84a1-43f97f8f9c70', '36792363-d45c-46fe-8f1f-ea0a423c78c3', 
                '75221748-a0f8-4971-b24d-798e9cdfbdd6', 'fe700805-407f-4e2f-ad92-90e947f54b25', 
                '0d3630d8-a3a0-4778-89e6-3d115c865535', 'ed93b163-5392-4071-8bd0-f6f000af5441', 
                'fd7eea69-3d7d-4174-8f89-c5e182f66661', 'de04b027-9e38-49e9-95c5-4c8e1428f7b2', 
                '3d193bb6-f54b-4c06-821a-37e8e2b3ba3d', 'fce9e943-e42c-4e5d-98cf-98693f83bb74', 
                'c00a07ac-0f0c-444d-982e-21f4ac6672e9', '3471df84-d0b5-48d1-a21b-7b1a8020efa2', 
                'e8ca49b7-56c2-49da-b0ac-056520ce1a2a', '33c7f292-88b0-4e43-85c2-9ae70da43356', 
                '9d6ec610-de80-49f3-91f4-5dc93be21a08', 'c5fb9c04-f17b-4726-8f20-8c1001d0613e', 
                '9a8952fb-2e39-4d29-ae1b-f6423d42ee88', '6a404d3f-c417-4ed3-a158-b68002cde464', 
                '533c1dc0-02f1-49a4-a77c-3a5f4edb71e3', '8726ec4f-ffbe-4f71-8e51-0c47e68442c3', 
                '9fc0f986-c10b-4e47-ae6d-5a5bcb4ffa46', '2848c735-2b74-4bcb-960d-c06e93d6c582', 
                '8b4c6ec9-cd84-4ca7-915e-3bbb07f56858', '0e5437ca-82d5-41de-9369-f9961b814e09', 
                '5ebb1145-e305-4551-9763-afb815b4bbf8', '76699771-c822-4591-98f8-a226a808e3c9', 
                '77e6e5df-8e50-4af3-8ff8-a4d72ad3412c', '8d37e8fa-93bd-482d-9b5d-83837f93ff70', 
                'd9b3849e-3637-432d-a28f-c363dafceef4', '8eee74ef-4b4c-48b5-83b7-e19c746d34d8', 
                'ffe94096-71c1-40cd-afe1-91b2ee9ed5eb', '81c09730-0b14-402f-b653-7097ac4f0ef0', 
                'cf9188f2-9dde-42e4-b147-c9e1be47816e', 'a25ad670-ff8a-4431-9abc-1cccfaa7e9f1', 
                'e557d644-70e1-4187-86a4-53783737c195', '01f6c339-d402-4cb5-8910-7217cc057446', 
                '88aab865-426a-48ec-97ac-2e3dc7a801a8', '3a9c2007-41dc-4ce9-ae84-346fdd8f91d8', 
                '7abd54cd-ab30-4402-bc2d-851442db708e', '97c9a314-7efb-4c39-930c-55520e5ebe72', 
                'c54d7889-89a7-4817-89e3-bd266c0d15bd', '826c0502-40c0-4af9-9354-32e613f14a25', 
                '63c8fc5d-9608-42ea-8378-63927818f20d', '7b12fd39-31c3-4bad-9e75-902cf664f6c7', 
                'd92cb1cd-3064-4c68-a779-d287250e0728', 'f67baec5-229c-4146-9c1c-78a16c99d3ec']
        page_media.select_media_by_text('Animals')
        index = 0
        for name in animals_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Environment Folder : 46 clips
        environment_list = ['Cosmos', 'Crowd', 'Fireworks', 'Heavy Rain', 'Heavy Rain', 'In The Water', 
                            'Nightmare', 'Rain01', 'Raining Outside', 'Rainy Day', 'Running Water', 
                            'Sea Coast', 'Shower', 'Storm', 'Summer Night', 'Supermarket', 'Thunder01', 'Thunder02', 
                            'Water Droplets', 'CINEMATIC Animate Wind', 'CINEMATIC Flyby', 
                            'CINEMATIC Whoosh Air', 'Camera clicks', 'City mainz', 'Forest Crow', 
                            'Forest Rain01', 'Forest Woodpecker', 'Ghost', 'Roomtone Noise', 
                            'Water Dive Large', 'Water Dive Sink Medium', 'Water Dive Sink Small', 
                            'Water Impact Deep Large', 'Water Impact Deep Small', 'Water Impact Spray Large', 
                            'Water Impact Spray Small', 'Water Movement Rapids Small', 'Water Splash', 
                            'Water Whoosh Soft Large', 'Water Whoosh Soft Medium', 'Water Whoosh Soft Small', 
                            'Waterdrop', 'Wave Surf Small', 'Wave Tidal Medium', 'Wind', 
                            'forest birds01', 'forest birds02' ]
                        
        udid = ['cf7b9f07-f305-423c-9fe7-5e99908e2818', 'c1b09d39-b532-4d55-b646-ebe3986dc45e', 
                'b4aa6c39-75db-4c72-a625-e7d49489cc60', '175f6a4c-789c-439b-9cee-41571d4c8bc2', 
                '24d117a2-6b21-4917-8a65-861dbc2bdc72', '27df1960-9489-4262-9696-54912e67f42f', 
                '69a30ec9-e9a4-4532-b6e5-83ed3ec57705', 'd9eb54a9-0c86-49f6-b8e4-d19758bd724a', 
                'fe0e2d0c-13c9-4006-bcb8-c20e39974d53', '1a20e15c-e8f1-4ca9-905d-4a38405c4fbe', 
                'e38f54de-accd-4b48-a617-3492c87f9b28', '23c8e2e6-73bd-4d50-a37c-df5d03ff047e', 
                'c3a9d39c-a54d-4f99-bfce-d288b62acb3d', 'a2a057ca-f186-4e08-b884-8fb5bfde50d7', 
                'e31e5d81-23e4-45bc-aa33-b3a6ca3bdb4b', '19ce1ac5-e697-454b-b0a9-126d24636fc5',
                'f1f4e9ba-1a0f-4561-a32c-2ddab6250fa2', 
                'dc3aa280-abf4-477f-95ed-d1dd023da902', 'b3237875-4d0f-4fd1-b594-1c2f74717252', 
                'a07e3786-dd9c-4661-a3d8-cf0ccb7836b7', '35cf141e-111e-4562-b83a-0ba95a4aa6f8', 
                '4b9b60f2-1ddc-426a-9333-3ab36226c749', '439a0f84-1663-4881-aac5-58f9c3bbdb77', 
                '98adb04d-4ba7-44eb-8a4a-22b4c37f2230', '29e192df-523d-41eb-8842-6a4c8ddc34ad', 
                '235bc617-374c-410a-a653-9c8bc285eaba', '89857f76-edfe-493d-9818-7d55ed42d719', 
                'af676594-0b86-47ca-b994-36519217280a', 'aa55f219-36be-4cfe-a9e1-07d13b942401', 
                '289086a1-6076-4373-ac91-c1207cb8ba80', '986f0a38-bf65-40da-856a-28332f7118e1', 
                '169a12ac-2d94-4d49-8026-d1bdd6aca7e1', '9bec1259-f071-4ace-9a51-541596d0808f', 
                '848bda27-ffde-462b-b5bf-48891fc49498', 'db0641b6-589d-4754-b8c7-b0d25d6b078e', 
                '7a74811a-5d5d-4b65-82ee-8c6f48e041ae', '03d1a2f5-0eaf-42d3-a264-cb0b08d69088', 
                '7c82ea3e-2548-48c8-b1df-e5b8d0697fe2', '73ce4241-14ee-45ac-ba67-45fce551a430', 
                'd78346dc-9d13-4844-83af-88e2ba1c1cf1', '38b600b4-ac25-4feb-9185-63f223927cb3', 
                '2ce00ab7-c866-41a2-b9de-b6c31db83a92', '1f814ac9-1266-413a-962f-7de1525ff3ed', 
                'ea25cd80-66f7-4121-97d9-e51577b09dcf', '5eeb8166-7039-4b61-9687-7cabff3d7f2e', 
                'e0be34cc-4525-49c0-8f42-6dca7e6a2a66', '44b1319f-e442-4949-92ac-353be5f22a3d']
        page_media.select_media_by_text('Environment')
        index = 0
        for name in environment_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Instruments Folder : 28 clips
        instruments_list = ['Bass Drum', 'Bells', 'Chime', 'Christmas bell', 'Cowbell02', 'Cymbal', 
                            'Cymbal Crash', 'DJ Scratch02', 'DJ Scratch03', 'DJ Scratch04', 'Drum Stick', 
                            'Drum loop01', 'Drum loop02', 'Drum roll', 'Hihat', 'Hihat01', 'Snare Drum', 
                            'Synth Pad', 'Temple Block', 'Wichita Pipe01', 'Wichita Pipe02', 'Wichita Pipe03', 
                            'Clash Cymbals', 'Claves01', 'Cowbell01', 'DJ Scratch01', 'Drum Roll Timpani', 'Gong Short' ]
                        
        udid = ['f86b8143-eb10-40fc-8461-3b8c28ff5934', '11258b6b-c31b-4636-9651-226f9ed4513c', 
                'f6926ed7-8c84-4d2f-a738-5215482a7630', 'c706c9d9-37f2-4099-b7f3-85170d1ac7fc', 
                'd3777a48-1c39-427a-8332-6c4d2b44a0d3', '866e1fda-f3f4-4623-8f04-04f43db98cb9', 
                '3f230823-8765-4419-8241-ea87ee6b8978', '64f8e959-53ea-49d2-9406-5509c7857277', 
                '71e66216-f80e-4c59-ad66-0976207c05b6', 'cc4298d9-ac38-49b4-b39c-ede869b18172', 
                '74400844-0a91-4810-ba48-471300f9c8c7', 'dd66c1d1-c42f-475c-b6dc-376664f273ab', 
                '9f6764aa-290b-4cd2-9c39-dd0454d41fa7', '576ecd39-3fc1-4133-baa1-f68b4d471029', 
                '3412d3f8-8590-40a2-824b-64117c6fcacd', 'c7dcb2ee-0dcc-4bc7-9bc5-14804e26d860', 
                'b83ef54f-fbdb-439f-aa71-26d9099438ea', 'ca8a96e0-8bc0-4c25-8c41-3dd5ee6e26e1', 
                'd5144fdf-df28-4acd-bc98-baf77b25802c', '098417c3-1717-4a03-9887-fe205041b90b', 
                '55a0cbd6-397e-4517-8b8f-aefe40b58bed', '78bdd6f6-6779-46c1-8331-70d3308e49b0', 
                '49c3d383-0e78-4971-8b88-80e100ef8af3', '264625a4-06dd-4dee-b1f5-418e99423224', 
                'de8b0117-9faf-40ed-9b0f-4d2a294c1749', 'eb8a62d2-73e0-4c1a-a71b-499495ad932b', 
                'f4b615b6-c742-4ada-9528-f34cb3b3ad4b', '34c0b9ad-a2c2-4eef-a976-feb0ba7fe8c7']
        page_media.select_media_by_text('Instruments')
        index = 0
        for name in instruments_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Miscellaneous Folder : 122 clips
        miscellaneous_list = [  'Air', 'Bell01', 'Biyoyon01', 'Camera Shutter01', 'Camera Shutter02', 
                                'Countdown02', 'Discordant', 'Drop01', 'Explosion01', 'Flash01', 'Glass', 
                                'HIT Boom 01', 'Hit', 'Ice Ball Hit 01', 'PUNCH Oldschool 01', 
                                'Radio Wave Nuisance', 'Right', 'Synthesizer01', 'Synthesizer02', 
                                'Test Start', 'Topic Present', 'Whistle01', 'Whistle02', 'Wind Chimes', 
                                'Wrong', 'ABSTRACT NOISE Dark Rising Storm Scream', 
                                'ABSTRACT WHOOSH Distorted Rip Bass', 'ABSTRACT WHOOSH Storm Twitter', 
                                'Air horn', 'Balloon Air Release', 'Balloon Air Release Buzz', 
                                'Balloon Air Release Fart', 'Balloon Air Release Fart Airy', 
                                'Balloon Air Release Fart Rumble', 'Balloon Air Release Squeak Clean', 
                                'Balloon Air Release Squeak Glitchy', 'Bell02', 'Biyoyon02', 'Biyoyon03', 
                                'Bleep01', 'Bum', 'Buzzer', 'CINEMATIC Bell Hits Horror', 
                                'CINEMATIC Demon Voice Transition', 'CINEMATIC Ghost Choir Transition', 
                                'CINEMATIC Metal Horror Clang', 'CINEMATIC WHOOSH Impact Soft Wobble Bass', 
                                'CINEMATIC WHOOSH Impact Soft Wobble Bass High', 'CINEMATIC WHOOSH Sci Fi Sweep', 
                                'CINEMATIC WHOOSH Simple Low Grainy', 'CINEMATIC Whooshing Bass Drop Short', 
                                'Call 01', 'Celebrations01', 'Celebrations02', 'Church bell', 'Click plastic', 
                                'Cursor operaton01', 'Cursor operaton02', 'Cute landing', 'Cute walking', 
                                'Door stone close', 'Door stone open', 'Drop03', 'Electric spark', 
                                'Electrification01', 'Emergency', 'Energy up', 'Fireworks', 'Flash Kuiin', 
                                'Flashback', 'Get Shocked', 'Heavy Hit01', 'Hit Smash', 'Jump Down', 'Jump Up', 
                                'Landslide01', 'Landslide02', 'Magic01', 'Message Get01', 'Metal Hitting', 
                                'Metal Scatter', 'Multiple Drum', 'Pager01', 'Period Drama', 'Pneumatic', 'Pneumatic reverse'
                                'Police Whistle', 
                                'Punch Hard', 'Punch Soft', 'Quick Answer Race', 'Rulertwang01', 'Rulertwang02', 
                                'SCI FI Electricity', 'SCI FI Menu Close Light 01', 'SCI FI Menu Close Light 02', 
                                'SCI FI Menu Open Light 01', 'SCI FI Menu Open Light 02', 'School Bell01', 
                                'School Speaker', 'Sci-Fi01', 'Screech Sliding Stop', 'Selection02', 'Shine', 
                                'Shining', 'Show Up', 'Signal01', 'Simple Information01', 'Simple Information02', 
                                'Slip', 'System Confirmation01', 'Tada', 'Temple Bell', 'Test Over', 'Throw Away', 
                                'Transition01', 'Transition02', 'Transition03', 'Wall Destroy', 'Warning01', 
                                'Whistle Slide Tremolo 01', 'Whistle Stop', 'Whoopee Cushion Fart 01', 
                                'Wooden Vibration', 'beep03' ]
                        
        udid = ['be000924-3c22-41de-b502-241c3d816923', '2d0f4a50-0350-44bf-963b-40deb88fab80', 
				'298fbff0-1538-414e-9446-6c5a3f0c849a', 'bf4c33f1-6c76-4977-aca9-9c51561024fb', 
				'500d2b4a-095b-4e9f-aae4-fdc4d1ddc2f3', 'e8b7c707-5db4-481a-ab31-2aab993bad8a', 
				'34f6d4eb-4d57-4fe5-bec8-974f003e58b4', 'c38c9369-a8bc-40b0-bfc6-f14e65ac78af', 
				'cbf07cbd-4563-49ec-9129-6d402586d5d0', 'f146a633-9170-4caa-bbac-91f0aaf2cd19', 
				'e00df0bc-d284-46cb-94fe-531964f64404', 'ee35a6ef-d8cc-4915-864d-6f996a4a0851', 
				'ce05f797-2b45-471f-b117-b601a32f008d', '53c747c8-c391-43e2-8114-f2b62fde8354', 
				'231b411d-4901-4446-a6ca-7533908b6942', '3a69fa73-6577-4d6b-b9fc-510812edec76', 
				'64d81e02-cecd-4cf4-91d0-f4d1e9ce0d21', '47596447-cd0e-4d1d-b02c-6635e01ab160', 
				'be373c4f-3327-4c48-848a-9379c4f527f7', '3c1440dd-827d-477d-97c5-33b7b60a1bf8', 
				'ce560128-ab3c-4b73-bed0-674c15a0fec0', '326111a6-ac6a-4df4-a9cd-a77cd53b299a', 
				'fe14d0eb-c44a-4b94-ba31-3edb88a6e716', 'fa666d97-1c5a-4b5d-ad02-8dc36b3ae8bd', 
				'ba6c3a51-70d0-4285-a0fa-9124eb5bf451', 'dd1b4bb5-a755-4356-8a7d-276a577b3d48', 
				'63f2f878-e0c2-4235-b1f7-7e030e17aa28', '664d1ca8-ea9b-4a12-85e3-c9abf5a942bb', 
				'b100ad80-22ec-4051-ba7d-188a73098013', 'd8229fce-ba19-4bce-9734-6e44e69a8fcf', 
				'59b817a5-af9b-408e-90ef-3073fbee005b', '82c0f183-e4a3-4cd9-8051-7d8ea7660b5f', 
				'fb90907b-5d9f-40e0-a217-b4ffbde80f68', '61cfa20f-6e02-4513-b53d-74deeddfe810', 
				'a4087764-6bb1-4b1f-837c-d7371511441d', '3b657a6e-a12c-458c-8ae2-4608aeca1a9c', 
				'47edb13d-7c59-4d19-8998-5ab4eb419a34', '0670b576-74c1-44a8-998f-a0bc1fe8a28f', 
				'daba8dbd-8c0b-4b18-9e2c-cfc17c318d0c', 'c8147d27-74fc-4589-b41e-c75a263a5afa', 
				'b856f498-cd43-4d1f-8dab-fe5b2230d27d', 'fdadb378-3d4e-4f42-bb2e-373128895d81', 
				'100b9c14-9757-4e48-968b-4f533877e726', '50cf52db-5005-4fa9-94c3-14a1bf51eba5', 
				'd6791661-b842-4c37-a044-38a9bf956e2d', 'bfafcf3d-191f-4fbc-891d-5ddfb94b78c6', 
				'd1c5c1ec-e151-4302-82ab-7b054f7a3a7a', '8a52f111-0220-45d4-9d39-2fb3cfd8289f', 
				'971d3d3a-07e1-4d42-929b-a55305158ddb', 'e8dc18c9-56b5-437c-a94c-748b24f1a6ee', 
				'f3314ce5-9305-429e-ba34-c2fd5238721a', '583d0244-01ce-4071-bed3-641e159683b6', 
				'678322b8-d87b-4c4d-aa06-159db88eefa0', 'ff6f98e1-84b0-4ec2-bd38-5db4f381d98c', 
				'8f4942e3-2103-416e-b968-68cf20968fa8', 'bee90a14-4bb3-4ea4-8926-cc8de6b6a48a', 
				'51af8905-eed6-4822-9394-6d1a3aed49ba', '000f9646-fe78-4632-ac00-d58dc8b85f16', 
				'5a87dddb-0ff9-48e8-9d08-02285dbc291c', '3e523cc0-d605-4452-ad37-bae0eabe308b', 
				'30d4775a-3976-4a19-859e-e654703e9ff9', 'a9e71ba9-25aa-4d5f-86d6-994b8b2460da', 
				'dec2f09c-b9c9-4357-af43-80f11ba669b3', '5e7023b4-a79e-4898-a13b-84fcac79d853', 
				'056da3ef-91aa-4f5a-bfdc-7454198cb266', 'dcb65aee-8945-4e52-8f9f-67bc9113dc66', 
				'313647d8-d6cb-478a-86a7-6a7c4cb55730', '39da06e0-1a76-4f99-b466-0bda863c818e', 
				'864310fc-aeea-4ada-9095-59ab61edf4da', '0f0c282f-2712-454f-bea3-670ce8f4de02', 
				'1c92bca3-d868-4bf1-b568-d8ebe009bb73', '9a6694eb-5393-41e2-ae9d-8ca54123fb41', 
				'4c370a74-e216-4168-a7fd-fdb6dce0c651', '5e125363-5e02-497c-9744-fde693c05c19', 
				'6f3710c6-0251-4c37-87ad-1527f516e15b', '737636eb-9091-4b09-8df9-9abafe915b3e', 
				'01bf6898-61e6-46d1-967c-471b2a55d193', 'b2895328-cb04-41ac-a725-91e6254146dd', 
				'cfc0e72a-c7f0-465d-93b9-60ae6f792241', '9658166c-40a3-4005-b43d-0e9da7b710d4', 
				'2ad51bbe-6ffd-4f75-b36d-f5ca5cfed70d', '325dd53a-559e-44f2-a4a0-52cac305a0b9', 
				'8a191a63-4e13-4a5c-be2c-03871a8807ef', '15811c78-a646-4a39-ad69-22e5913b1e7d', 
                '5e43e4eb-49b0-4503-8ae9-2b5ce0a3ef0a', '9e88bcff-cae8-47f8-9cd7-004c422ac48a',
				'0ee6e22b-2501-45e3-9902-9cb968cb1fd2', '4599439b-b645-4c0d-a092-99d2188a7d44', 
				'de0f9796-da90-46cf-91da-35c4118e3edb', '4be2075f-7b9d-4975-ac73-eef9b0f392aa', 
				'1aa3c307-0c4a-4e54-860f-0a42dfc7d216', '492fe790-e41c-466d-9752-5d1ba35b08e1', 
				'79766feb-d6fd-4f6b-a326-dfbf7f05affc', '33225ea9-00c9-4792-a669-6ef64cb9a78a', 
				'19b02f2b-48ba-4b97-9bce-abcd8576d6ae', 'a98954bc-7097-4fea-910a-cc82020de4b5', 
				'15d4af36-d542-4f20-b397-d93f1822193e', 'c182d65d-a372-4ec4-8345-cf870218b0b7', 
				'861dc3cd-75ca-4cb2-a5b0-c0901fccfd93', '6c514fe9-fa13-47ad-9500-4eb27b2488f7', 
				'fcbb1a46-311f-4705-9752-e50e03c870ee', 'a426e3c0-939a-4f19-8d67-7e8bfef133cc', 
				'b9248f40-220f-48af-acb4-ac98d9e56c6f', '8117522c-4568-40db-b077-9454a00c8a67', 
				'571c224b-b501-4e3d-bbc2-42a51eea7b4c', 'fe726453-3cce-43e7-afdb-2609beb8b27d', 
				'02c4bcfa-a5c7-4705-ba57-63ade4b19e32', '443b2100-34b0-4b5b-9b8d-99c8a6355b9a', 
				'b6ea7cfd-7fc0-4a1a-adf0-ed51855a692a', '2875453e-1de3-4cd9-b299-822c600a043e', 
				'e7c47c76-a8a4-4c8f-a939-03fe550bf50e', '689b8438-7ca2-4fbe-9638-49ebc530bef6', 
				'5ca2bb55-6dba-411a-9f1a-8015dec135ee', '324ec9dd-57b5-442e-9cb8-785386aa6619', 
				'a5c5ef66-1a45-4b72-9e6b-8117f950e1bd', '9b25e24f-58cf-45ca-8e57-1ee691a31714', 
				'b198ad54-caba-4567-ad59-ad552981e646', 'dcff31a3-c346-4c01-bbb2-def418b79005', 
				'68aacdd5-003d-4d69-85f6-816e3f7bb76b', 'cf7f0f4c-2d29-4896-92ee-d60dbd3946fd', 
				'2f2d1230-9ded-4087-912a-010e6ca46f6c', '9836ed2d-0f8c-4ca4-a5d0-c3d32b3ca933', 
				'5e30c167-25ad-4af1-9096-5ec361183838', '427198da-a5c0-432a-b7b5-10a60035458e']
        page_media.select_media_by_text('Miscellaneous')
        index = 0
        for name in miscellaneous_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Musical Jingles Folder : 29 clips
        musicaljingles_list = [ 'Alto Sax', 'Bass', 'Bassline', 'Brass01', 'Brass02', 'Brass03', 
                                'Distorted Guitar', 'DrillBells', 'Drum & Bass', 'Drum Sequence', 
                                'Ice Wind', 'Innovation', 'Sensation01', 'Sensation02', 'Sensation03', 
                                'Slap Bass', 'Synth Bell01', 'Synth Bell02', 'Synth Bell03', 'Synth Bell04', 
                                'Synth Loop01', 'Synth Loop02', 'Synth Sequence01', 'Synth Sequence02', 
                                'Synth Sequence03', 'Synth Sequence04', 'Synthesizer03', 'Synthesizer04', 'Xylophone']
                        
        udid = ['262cd7a6-3581-4950-81f0-3710fdbd79e9', '537b69d1-6297-497c-9aad-960fe006ea09', 
				'95203e69-539e-4bd7-a6a1-1c64c3bd9855', '4e019431-1079-48f0-8dec-d5b2b33ecbf4', 
				'8b3e6e16-e148-4913-ab91-88e616959a92', 'eb2753fd-6fa6-4b9d-a8f7-9f532590d3b6', 
				'159bd937-e411-42cd-8fe3-f0792560ca8a', '9b372b23-65ec-47ac-89fd-29a3da5db4d8', 
				'cf642f6d-4f34-467a-b8ae-ed3e716c19f0', 'f4e097b4-57e6-46ff-b329-b334106d9fa4', 
				'b5c3840f-bb1c-4487-9d36-66bad518a589', '6ff78328-88c3-40e4-b3df-e236de9aee16', 
				'd9fd82e9-0fd0-459d-ab69-559e30ac4db1', 'de35d8a9-f7c8-4f82-95a2-81aa6441cb99', 
				'f4ac318e-a9be-424d-ab92-747823a6b4d6', 'a0bd4834-8ca9-46c4-8d5b-cfd928b8b27a', 
				'4075a556-fb22-4780-bd2d-6a226dff5830', '4be9c22e-45b0-4056-a9a7-a3c7edba504f', 
				'651c50e2-b229-470c-bb14-8d5636c28c77', 'a47c50a8-6419-49d4-804b-c3df2f458386', 
				'8ec6b88a-75e2-49c2-bb48-42c60044e96b', 'aad5cb6e-2377-49e1-a61e-edfae3142e5c', 
				'02c89a6c-0a24-4e92-9b98-6daf5dc1bef3', '3575e613-cf59-431c-b367-ebbfac3932de', 
				'1e6959a8-525f-4341-9914-646f1fd1a66c', 'aa41cbb0-ee1b-427a-9b0a-a86bd9969188', 
				'acb273b9-6e41-4d22-b397-091dbd8c7651', '08b2f7da-0b6b-45a3-9471-176200684d15', 
				'923fc870-2ab5-425c-82d7-c9d6c53a436f']
        page_media.select_media_by_text('Musical Jingles')
        index = 0
        for name in musicaljingles_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # People Folder : 75 clips
        people_list = [ 'Animation laughter', 'Applause01', 'Applause02', 'Applause03', 'Baby Crying01', 
                        'Baby Crying02', 'Baby Laughing01', 'Baby Laughing02', 'Baby Laughing03', 'Baby Snoring', 
                        'Baby Talk', 'Beer drinking', 'Cheers02', 'Clapping01', 'Finger Snap', 
                        'Footsteps Footsteps02', 'Happy Baby', 'Heart Sound', 'Man Walking', 'Scream', 
                        '"Bo" by mouth', 'Ambience crowd loop', 'AppleEating02', 'BREATH OUT Female01', 
                        'Beer', 'Cheering01', 'Child laugh', 'Child laugh fake', 'Clap01', 'Cleaning Teeth', 
                        'Crowd angry loop', 'Crowd cheer loop', 'Crowd festival', 'Crowd festival loop', 
                        'Crowd grumpy loop', 'Crowd panic loop', 'Did we Fake it', 'Disappointment', 
                        'Eat Like a pig', 'Eating Crisps', 'Eating Toast', 'Everyone laughs01', 'Excuse Me', 
                        'Female Die', 'Female Sing', 'Finger Punch', 'Finger Swipe', 'Gargle', 'Girls Laughter', 
                        'Hand Hit', 'Hanger', 'High Heel', 'Kiss01', 'Licking', 'Long Kiss', 'Male Die', 
                        'Male Fight', 'Male Gurgle Die', 'Male High Hum', 'Male Laugh', 'Male Laugh01', 
                        'Male Relief Sigh', 'Male Shout Aggressive', 'Male cheer01', 'Male cheer02', 
                        'Male hit01', 'Male whistle', 'Men Laughter', 'Out Of Breath', 'Screaming01', 
                        'Snap01', 'Tea Slurp01', 'Tea Slurp02', 'Washing Hands', 'Woo']
                        
        udid = ['248d96f5-a999-496b-8c87-6e9b148d0e06', 'b52be89e-2d9c-4090-960a-34ee4e3ad5ea', 
				'4c3a67e5-1a48-48af-ad8e-4fae8010b3be', 'd7e85dc4-fb4d-49d2-b4e2-11718ccafe30', 
				'6dd9b979-6aec-4493-a114-181c24b88588', 'b2e050fb-ce31-48d7-b1c7-43b54c20cd49', 
				'f6f5d7c7-2320-4076-a11d-3537e271b809', '33426a47-dfc0-41c1-aee6-abee953e5a79', 
				'6223e341-4285-4a7b-ac5f-53b0b8cb1a26', '074f7843-9697-4295-bf5a-f6e0c3f8c996', 
				'94e6a66b-bae4-4cb0-837d-a5e0163e8f8c', '9113c8f3-bfa6-4897-84ac-d0185582b6bd', 
				'19dcbb4e-e56a-4624-9193-5a328f01c2e9', '39704f65-9b4a-4ca3-a58b-18d9389431c2', 
				'a5d3c55d-4af9-4c24-8ba7-649fd73772d0', '73a265ba-d637-4ad6-9a03-d52a6082032d', 
				'13d0675a-0f8d-4cab-95fc-f03c1f219aa5', 'c415fd71-1900-46a2-9868-00f525558cd7', 
				'969456ee-c3cd-452c-8c16-9079545bb18b', 'c620287c-3501-4840-bf11-4339befcb09e', 
				'81ce99d9-8d15-4609-b4d1-ce32ef4d1cdd', '5127b6ac-cf3e-4cf8-b4f8-491fa56a13b2', 
				'46a384b7-a37b-49af-815a-dedb4b7a18fe', 'fd26b942-3f98-4a3b-bd13-17a642d202ae', 
				'926de39e-0f02-47a1-97ae-9b0c0b4f3d04', '6a2672c9-4e1b-4278-a755-d24612c16693', 
				'549cbe49-5def-49c0-beeb-789ad62b4326', '89cb4c88-2582-4dc2-96f9-80219a250ab4', 
				'757c2d87-b96a-4d1c-982b-9e14b4fc2e08', '9a4862e0-46a1-414b-94c8-7ac0336b5989', 
				'849d7adc-464b-4d1c-aff8-4a5872a5902d', 'c08b914a-95c1-4672-a34b-bb18a7ce4b6f', 
				'a65336fb-1533-42d8-afa1-67c02c22bfa6', 'a7193982-b385-4214-bdc9-d38f2a98d2a0', 
				'd29099ea-7a20-40c5-a527-497c3dd2d776', '8958255c-41e6-4cd7-8767-77c40cce88fe', 
				'84ab4716-77b5-4a75-bab0-b37243e9d9b1', 'a0c9827d-03f5-44cd-b4b2-5377b31629d8', 
				'f75e3074-e5b4-4797-a63f-6c407d3bcf32', '47a28e1d-60a2-4942-b2ee-8fbd3eded154', 
				'bf6de5eb-83dd-46da-bab2-dcc1b2cbb792', '24032cc8-9974-42da-af77-614214bbf310', 
				'a8d6c7b1-8e63-47b7-a9c9-90f315f6a678', '0e25d068-9735-484e-9f2f-9852212b26b9', 
				'ecafb5f8-763d-48b3-b30a-2ef589de36d2', 'f689eb45-e4f7-42a6-b930-96a58487cb28', 
				'e265779d-bf9e-4933-9eda-fca575a24463', 'df55b993-12de-4d4d-ba68-7f3a6e6c5ceb', 
				'618874ad-9d44-495d-a669-709eb8e38304', 'b42af50f-000b-402b-96a1-d63332fb0bf2', 
				'0622caea-e136-4e21-ac64-68851275c10e', '8a329c2d-7ab6-4c44-9354-fc6e23f98116', 
				'5e038235-bbf0-4952-9ed5-336908f3a319', '8a6f2b62-5001-4064-8ea8-3c622b983959', 
				'f9ca5555-7eaf-423d-a8f0-0b7ff3921d1f', '1cd2884c-c321-4075-b47d-9e20e147931c', 
				'370d1afd-87db-4347-91dc-76195991179b', '7b1886bd-0fc8-4f40-876a-baf9c246da6b', 
				'662ba418-09db-4ef2-95f0-97ab5939c251', '6f61bddc-84c7-4e09-a34a-620791768289', 
				'1261c7a4-51a1-4e51-bf50-1ce48f2faaa1', '45dd33a3-638a-4ef6-8c82-2536bc83b43f', 
				'c770c729-ef51-4ad0-a765-7cd2a47bcf79', 'a94a6521-3aa1-4c22-9b97-652f37f5d68f', 
				'4a58c7ca-b9ff-4131-99e4-854f892a5a01', 'f665dfa8-9c29-4401-a789-62ec6675bb8d', 
				'd6e9f630-e46d-4abb-9d63-22dd350aeef6', '48a2aac5-6776-4c25-9a24-e13aa262e0a9', 
				'39224a7b-5ae3-455c-9604-22aab4e0bc08', '45459327-bd05-4288-914d-754e31c0be0e', 
				'1f5db126-2fa9-46d6-94b0-7ccd54d1a25e', '37e9b193-8108-4e6e-b95f-a84d65dc1861', 
				'7a30e48b-ec17-4178-bd9c-f2f316e393b6', 'fe0d34ce-3a61-4761-ba99-4157fa26cbba', 
				'1ebb4055-3cd9-415f-86ac-77fcde08852f']
        page_media.select_media_by_text('People')
        index = 0
        for name in people_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Sports Folder : 17 clips
        sports_list = [ 'Badminton Atmosphere01', 'Badminton Atmosphere02', 'Badminton Hit01', 
                        'Badminton Hit02', 'Badminton Hit03', 'Badminton Hit04', 'Baseball Catch01', 
                        'Football Kick', 'Pingpong', 'Table Tennis01', 'Table Tennis02', 'Table Tennis03', 
                        'Tennis', 'Treadmill', 'Arrow Hit01', 'Basket Ball Perfect Shot01', 'Golf Hit01']
                        
        udid = ['7b71e749-e1c0-4cd7-bde0-a424fabe4855', 'db0e7613-6bea-46d9-b2fb-a56ae04680cd', 
				'9258de5c-2db8-4925-8aff-ececea41963e', 'da6c0a88-eba1-41c1-82e8-f465495ed824', 
				'575dff50-351e-4690-ace7-8e0709e7fe7c', 'd22ced13-e220-4345-b002-f4da7eeb652e', 
				'23e3cb34-6df4-427b-9d1b-81077c3c74f0', 'ff5cfb5d-768e-4188-a68a-dc113d9a4a63', 
				'609c58b2-29f5-45f4-96db-11ecf41b3d55', '82d950a4-5079-4aba-b926-514da34342d3', 
				'29995f7c-058c-4c5e-b6de-32b7191444b3', 'b1a74889-d7ad-4e5a-b15a-8921cc3dad88', 
				'05f1c73f-c3dc-4313-930c-08abe111355f', 'be4cb7b4-0204-485b-abe5-2f61fad70024', 
				'c7fe516c-6103-4a06-9587-77d5e2cbc0ac', '99c2409f-79da-407d-ba56-56fc660a3621', 
				'd3691863-aa19-4a51-aef5-a2436676d2c6']
        page_media.select_media_by_text('Sports')
        index = 0
        for name in sports_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Transportation Folder : 40 clips
        transportation_list = [ 'Car  Driving By01', 'Car  Driving By02', 'Car  Driving By03', 'Car  Engine Starting', 
                                'Car  Horn', 'Car  Horn01', 'Car Turn Signal', 'Car bumping', 'Helicopter01', 
                                'Motor Engine Starting', 'Motor  Engine', 'Racing Car', 'Ship Horn', 
                                'Spaceship Medium Fly 01', 'Train', 'Airplane', 'Canoe paddle series strong01', 
                                'Car horn', 'Carriage drive concrete01', 'Carriage prepare', 'F1 race car pass', 
                                'F1 race cars competition extreme', 'F1 race cars competition loop01', 
                                'Jet Interior Din Loop01', 'Jet Overflight Distant01', 'Jet Takeoff Runway01', 
                                'Jet Tarmac Loop', 'Minitractor Drive', 'Minitractor Start', 'Minitractor Stop', 
                                'Motorbike', 'Submarine Sonar', 'Train Freight Horn Blasts Crossing Bell', 
                                'Train Freight Horn Blasts Echo Loop', 'Train Freight Horn Blasts Town', 
                                'Train Hooter01', 'Train Pass By', 
                                'Train Passenger Car Interior Sec Rail Mod Fast Loop01', 
                                'Train Passenger Car Interior Sec Rail Slow Loop01', 
                                'Train pass commuter sectioned rail boll']
                        
        udid = ['53949b91-493b-4733-8723-89c416c917f1', 'c4fc2415-9c55-4e0c-a816-8333e2b43ddc', 
				'dafbfcdf-7d83-4e68-b8a6-25944316e252', 'ef7adeee-e8ef-45a8-86f8-0c4fb9dc66b8', 
				'b82b1adf-747f-4f10-9632-dee1dc5f1eba', '1ad7d9d4-dbdf-426c-b102-a87aecc062b1', 
				'dbf5ca2c-8742-426e-a148-973dbe23e510', 'c4e4c0f0-f0af-47a5-9ca0-853f3f7506aa', 
				'68969794-814d-46bf-9d64-ac13241e5c29', '46a7de61-a5f1-4e08-b08f-8b05f67f745f', 
				'5a970768-07e5-4fdb-9dfc-5c55461231ff', '2e4b2ff5-2f97-4bd4-9869-2028473d630d', 
				'dc9d62ef-fafc-40d8-bfba-9f2a5f47bca3', '36f1a85c-0357-4e59-b0b7-77fb1af083c2', 
				'5510bd6b-c993-4acd-95d0-aa06d81430d7', 'b6d37b90-b3df-46c2-85a8-fe2f86f3cfd1', 
				'18f8da33-ecd5-48b8-bf71-6aa529c512f3', 'e568b722-1123-40ee-9ade-c0ad2992cfe6', 
				'904ee5bf-68fb-44fb-bca2-1243486dd71e', '42c6d2ae-346c-40b4-a5fd-f31dc1483cfc', 
				'6a69c654-c715-4e41-8642-7341b040aca9', 'fc28a66e-36c8-432c-8acb-fe44625cf0e9', 
				'a5889565-7175-4380-80ce-08647a7c0619', '0f0f0c8c-0894-4868-9c8a-2863d33d5b32', 
				'63d4afc9-8c2e-4e64-b878-5f178982ab3c', '8d576b21-b3c6-4572-9319-ca2fef84d40e', 
				'b9f51062-1f98-4ea4-bf50-4951ec5bf3cb', 'e013d8af-545b-46f9-945d-935526d3135d', 
				'd395e401-db27-4018-a29b-50afc055430f', '1a979c4f-e03a-4e7c-b9c4-82cb15462572', 
				'00d706e8-b3c7-430a-976b-ad60d51bb32e', '2523b76c-0d2a-4a9c-99f6-70104c896569', 
				'f0ffddfa-7a45-43d6-8446-c221941559e0', '9eedf7de-da58-4a99-8335-ddf2cd0b91cf', 
				'1616f74d-3b6c-4480-be2d-89ba0d15c247', 'a9a9052e-f4cc-40de-82df-161a28382170', 
				'd0b7a945-cc70-44aa-b96f-75bcadd65cb2', '2455b649-2fd7-4c0d-a95f-eacaa4a63948', 
				'e5a74b45-1828-45b4-8903-608e76661784', '7908fc4b-400a-4fd1-b150-f53b1b0ac0d9']
        page_media.select_media_by_text('Transportation')
        index = 0
        for name in transportation_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()
        
        # Weapons Folder : 53 clips
        weapons_list = ['Air Compressor', 'Cart', 'EXPLOSION Big 01', 'EXPLOSION Fuel 01', 'Explosion03', 
                        'Gunfight', 'Gunshot', 'Hammer', 'Jackhammer01', 'Jackhammer02', 'Knife Drawing', 
                        'Machine Gun Fire', 'Moving Machine', 'Punch01', 'Radio White Noise', 'Scissors', 
                        'Siege Trebuchet Medium Shot 01', 'Synthesizer05', 'Wielding01', 'Axe hit metal', 
                        'Ballista hit', 'Bomb Drop', 'Bullet fall01', 'Bullet fall02', 'Bullet fall03', 
                        'Bullet loading', 'Bursts crispy', 'Close Auto', 'Distant Auto', 'Explosion01', 
                        'Explosion02', 'Gun01', 'Gun02', 'Heavy Auto', 'Knife Fight01', 'Knife Waving', 
                        'Missile', 'Punch02', 'Razor Gun01', 'Razor Gun03', 'Ricochet Western', 'Silent Gun', 
                        'Singleshots Huge', 'Sweep Dry01', 'Swing01', 'Swing02', 'Sword Hit Dry01', 
                        'Sword Hit Dry02', 'Sword Hit Wood01', 'Sword Hit Wood02', 'Tapping', 
                        'Wielding02', 'Wielding04']
                        
        udid = ['3c3015a2-24d2-4fda-9c66-584bf16010e0', '49484f47-facb-43fb-a6cc-5832cd5b3496', 
				'98d97698-c1ef-43de-a4a0-9dd9941bd71e', 'd02a15f2-3e43-47d4-8d04-b8c80f8d3da9', 
				'3d5d8f27-b7b4-494e-a74f-63458d8161a1', '03d11e74-e5a8-4fa0-8580-9175d93f7878', 
				'a26aecbe-bc65-4aa1-925b-86e2663b49b1', '4ad01cff-e05b-4a90-a134-0d3b93e743be', 
				'1d272142-7781-472a-9230-477051ec2f7b', '3bce3a4c-075e-4220-b651-ab46204d4373', 
				'34af3358-5969-4fff-a450-517d618a16a8', 'e791c7ee-2565-4a96-9ee3-826944542d46', 
				'05f10223-dbb7-4280-9a1b-6b7cbec3377c', 'f46a39e4-290c-44f4-9e1b-34ede1c03d6b', 
				'f1fd985b-d9c8-4bef-bb39-83eff1d3d222', 'd0424c69-9cd1-4420-b4cd-d4b1f7bffb06', 
				'52600d17-665a-4dbe-b5b7-018f9fe6c0f5', '756cb65c-3145-422e-858e-3bc64faa8e73', 
				'9def3bc7-2af8-4653-8a59-81be3a185705', '6a607161-aae9-473b-8da8-5d1251b2a627', 
				'92388e06-a4ec-488d-adc6-3ad55a5552ef', 'c4031e84-9aab-484f-8907-142f83f9efa1', 
				'7f83586d-1af4-4477-83e3-67360d9931d7', 'da3eff50-e236-49a3-b1c1-5a368eb04b49', 
				'bd24ad0b-b737-47a2-a7d1-1799527d4d2c', '4f334360-7c51-45cb-a563-13e20451e432', 
				'50ce2e50-6d71-4ed6-9b4b-f5ffc6c40a3f', 'cd44769a-febd-4d89-8070-2952596271dc', 
				'486e6b7b-b6ec-4361-b03f-091252663630', 'e98a1f91-4649-43a9-9f31-3a60ad72aae0', 
				'8cd171d1-01da-4d5f-a73e-6b01c473ca8c', '9d3ef62f-68e9-4dce-8da6-0daee14ed27e', 
				'e318d72d-8975-4586-a543-79b54436b739', 'd9bfdc26-8e82-485c-906a-0d942970bac8', 
				'b39447f2-73d1-47b2-a58b-c34115843f86', '9a1e069f-7b72-440b-a7a3-71581d53e25d', 
				'f60fdafa-fa4e-4033-8a62-b2f3da81ad37', '0c50125e-6a0f-4b0d-875c-5ed84a43728a', 
				'0217613a-c0a5-4021-a934-ecf9a6b02b04', '82d625e4-d07d-41db-93a9-c4d4782c8d18', 
				'0439302c-fb2f-462c-a5b2-5fd21d342ed9', 'a0b82c1d-263b-41e2-81ca-b67f760794f3', 
				'b70cba3a-f7b8-4e0a-9f62-ab50ab578e0f', 'bd3eab40-46ed-4c4d-87e4-145f014f0a4c', 
				'f704398d-a1ad-4a49-9631-cb192151f140', 'aad0db34-6126-4ead-ba45-5ac05e284b9f', 
				'079f4271-ab83-4fa9-84d9-eeb93813a5aa', 'c411cfb6-df1d-481d-9657-c6a495bbf9a9', 
				'fd54a865-51ed-4781-a626-292b2509c567', '95ce1594-fc3e-4c7e-a74d-84433bdd36a3', 
				'0a201253-48bf-4fe7-8fa8-4094b9cccf2b', '1f155dba-540e-4d4a-8260-7f155fd401eb', 
				'de5d04ed-7567-4eb9-b3f3-9429990f53b4']
        page_media.select_media_by_text('Weapons')
        index = 0
        for name in weapons_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()        
        
        # Work/Home/Daily Life Folder : 173 clips
        workhomedailylife_list = [  'Alarm clock', 'Axe Two-Handed Hit', 'Beer pouring', 'Big Drop and Smash 01', 'Bike horn', 'Burning', 
				'Clock04', 'Coin drop', 'Countdown01', 'Door', 'Doorbell01', 'Doorbell02', 'Keyboard01', 'Knock', 'Mechanical_Clock', 
				'Mechanics Medium 01', 'Phone Vibration', 'Phonecall01', 'Slidedoor', 'Stopwatch', 'Telephone Dialing', 'Toilet Flush', 
				'Typing', 'beep01', 'Airport announcement', 'AppleEating01', 'Beat01', 'Bike bell', 'Boing01', 'Boing02', 
				'BottleCork01', 'BottleCork02', 'Box of Matches', 'Box opening', 'Busy line', 'Camera01', 'Can Crush', 'Car engine', 
				'Cashier register', 'Cheers01', 'Click', 'Clock01', 'Clock02', 'Clock03', 'Clock05', 'Coin01', 'Coins Drop On Carpet', 
				'Coins Drop On Concrete', 'Coins Jingle', 'Cola Tin', 'Cork plug pulling', 'Cuckoo Wall Clock', 'Cup of Pens', 'Curtain drawing02', 
				'Cut01', 'Dishes rattle', 'Door closing', 'Door opening01', 'Door opening03', 'Doorbell04', 'Doors BackDoor', 'Doors Creaky door01', 
				'Doors Creaky door02', 'Doors Creaky door03', 'Doors Door01', 'Doors Door02', 'Doors Door03', 'Doors Door04', 'Doors Doorbell', 
				'Doors Sliding Door01', 'Drawer', 'Drawer opening', 'Electrical unlock', 'Elevator arrive01', 'Elevator attention', 
				'Food Mixer01', 'Footsteps Creaky Floorboard', 'Footsteps Creakyflrboard01', 'Footsteps Creakyflrboard02', 
				'Footsteps Down The Stairs01', 'Footsteps Down The Stairs02', 'Footsteps Footsteps01', 'Footsteps Footsteps03', 
				'Footsteps Footsteps04', 'Footsteps Footsteps05', 'Footsteps Footsteps06', 'Footsteps Footsteps07', 'Footsteps Footsteps08', 
				'Footsteps Footsteps09', 'Footsteps Footsteps10', 'Footsteps Footsteps11', 'Footsteps Footsteps12', 'Footsteps Footsteps13', 
				'Footsteps Footsteps14', 'Footsteps Footsteps15', 'Frying', 'Frying Pan', 'Gashob01', 'Gashob02', 'Glass Break', 
				'Glass01', 'Glass02', 'Grab Coins', 'Ignition01', 'Keyboard02', 'Keyboard03', 'Keyboard04', 'Keyboard05', 
				'Keyboard06', 'Keys', 'Keys Jingle', 'Kitchen Ice', 'Knocking On The Door01', 'Lemonade Bottle', 
				'Light Switch', 'Lit Match', 'Machine Beep01', 'Machine Functioning01', 'Matchburn', 'Matchstrike', 'Metal Dropping', 
				'Mobile Ring', 'Morse Code', 'Mouth Harp01', 'Pen Clicking', 'Pencil Writing', 'Piggy Bank', 'Police Siren', 
				'Pour A Drink', 'Projection', 'Radio Snowing', 'Ruler Vibrating', 'Rulertwang03', 'Rulertwang04', 'Rulertwang05', 
				'Saucepan', 'Scissors', 'Scissors Open Close', 'Seatbelt Sign In Airplane', 'Shower Taking', 'Side Sweet Jar', 
				'Slide Changing', 'Small Change 01', 'Small Change 02', 'Small Temple Bell', 'Snip01', 'Snip02', 'Snowing01', 
				'Spun Coin', 'Stapler', 'Steam', 'Sticky Tape 01', 'Sticky Tape 02', 'Taking-Up Wheel', 'Tap01', 'Tea', 'Tea Stir', 
				'Tear01', 'Telephone', 'Ticking', 'Timer01', 'Toaster01', 'Tv Snowing', 'Vintage Camera01', 'Watch Band Rattle', 
				'Wind Up', 'Wind Up - mouse', 'Wine Pouring', 'Writing', 'Zip', 'Zipper 01', 'Zipper 02', 'Zipper01']
                        
        udid = ['aaf7c1a5-58ad-44fe-bcc3-31da4694ba53', '4bf79388-b534-4f2b-9564-9808773481c0', 
				'59e08088-59b3-4afe-8193-2d5f3396ed17', '0b6fb6f5-b354-45d6-beb1-f9f38b0f9c21', 
				'61e99f2b-0bbd-47e1-8133-939a402a6023', '053e7ec6-5516-4fca-a8ec-47e24d336c52', 
				'92b4af65-702d-4fea-9c7b-1ac5a4752400', '7d41a7f7-eb1b-44d9-88db-271c1cec6ae0', 
				'eb65f94a-cec0-41c9-9f36-63bea1f6e023', 'de3a59c8-35fb-4945-bab7-8f4bf1ab9a75', 
				'385eb868-ada4-4d84-b4e6-d6dd51968ae7', '958b73df-5c39-470f-93ad-568d937aa302', 
				'b26c6815-88b5-433b-b1dc-d3b2228e66dc', '0953e07f-7274-4c72-b08f-fff70781ee18', 
				'f6ae0462-0749-40cf-957d-cedab41eb4d4', '338dd5a6-cfa3-4977-b52a-55b77b51636b', 
				'6bba18f9-8ee6-49ce-932a-28eed853ce9a', '8804de22-fd81-47d5-8a5e-a234ce2d9c38', 
				'befb0025-c604-4d8f-8d2e-3228927cbf53', '25dd2956-733c-4ccf-b79a-7f52cbce6ac9', 
				'1323130a-8eb8-4429-9cf6-af4b3d00fed5', 'cd509388-c954-4c99-8dd5-df1b914d71b5', 
				'c937a797-532e-43f5-9876-70ceff4fa946', '059192c2-ea80-462d-83cf-661154534fed', 
				'5f07827e-c207-432b-aebb-e13ab2d6bb43', '83d6d7c2-0a9a-48f2-a008-26b9928059e9', 
				'2146d508-4647-4caa-9154-d22a91d21b84', 'af3f7662-3933-4681-946e-64faf4bd9ef7', 
				'c8f91c1c-3c67-4e42-b95b-dee5fcfc7ece', 'cd8bb763-b660-4f55-9aab-ccc47d4dd05a', 
				'81e71d41-000e-463f-bde3-0b0bdd0c35ca', '38a89620-d3ce-479d-a41b-6d87a165478e', 
				'20368ab7-cb32-49b9-a8d0-17654344f270', 'ff5b3bec-ff94-448a-a200-f1d60e39ac8d', 
				'8c1b9f12-3070-45f0-9d6a-36ac283bc138', 'b4bfcf9e-2f39-4cd5-aee7-4780fad56ba9', 
				'976155c4-43dd-4c17-a584-acc8e93c63c0', '544c24fb-0cab-4f1a-8c95-c3811e9f0771', 
				'7a01c6f3-519c-44c8-acf2-191878aa74a8', '45c9cc86-2eba-49bd-8d39-323055735683', 
				'25ed606b-f83e-4ce6-94b4-44d547488c07', '93511316-c830-49e3-93e9-6ca6df824822', 
				'9c124b89-6f0c-4637-98f2-524b440998a4', 'b24ecd70-38bd-4ea3-8efa-8d7d27e2c75a', 
				'f096ce19-0b41-4e68-8f71-0b5dbba4e63b', 'f1c909fe-4930-4567-8e09-d6627fccc972', 
				'3fd91425-23b8-42df-940d-8d59d5603ae9', 'b7963fc7-1125-454b-9f73-de79fc146369', 
				'bfc84e5f-d24f-4914-9f7e-951a300f9d2b', 'f97f4c81-4ac2-4940-a55b-1309fa85703d', 
				'29a06729-012a-4ace-aa21-3d536af17e1c', '46e00e94-6945-406d-b59e-5c3cd9abe447', 
				'359b561d-e7a6-4bff-a560-1593b1c63961', 'afbdab29-f21a-4c33-bb3f-76cb0759e465', 
				'89a314f9-c018-43fc-bc93-0da7a7fb3d11', '48ed5d0f-2d63-4daf-9790-3385031e4013', 
				'da2ba315-5901-43ac-a014-b4d8d84ff665', 'cd936551-49f8-4ea5-a556-a493038e150b', 
				'fbf64d04-dc80-414c-a301-0c79a60ced36', '43e65977-58b3-4206-b3ce-7e48f0415ac8', 
				'd71b131a-9b02-47e1-a9ed-906d649c706a', '0bd5c30a-1373-496e-84ec-7305648e00c3', 
				'3a322a88-e20d-47f1-9a9c-02aa1622aa51', 'f474b03e-cbe5-4d84-8241-15b8974b665b', 
				'604ad8ff-36e3-4c41-b067-9b50cfb86cf0', 'cdcb6a78-51ba-4d87-8ba8-a456f8b94085', 
				'5e8b981b-f580-4a7b-b5fd-8c49f7439f2d', '7c8bddcf-61a5-46af-9303-da897828d879', 
				'24e07644-6b24-43f3-9236-64865dbe2f04', '6abf0f23-073e-4aa4-892d-5f2d6f279c26', 
				'142e5cbe-d848-4f06-a389-1af62006e7bd', 'd1bbaf92-4fba-4d5f-905d-bdd00fac28cc', 
				'dfc0e546-7661-4470-8cf9-33f6dad89f13', '0ac67be5-1639-42b3-80a0-fae4a06566be', 
				'0b40ee6a-d3f2-494e-9333-b5d34dff1370', '168d1cb5-f5c0-46a4-80d5-043c9cbc07dc', 
				'22df1878-8be8-4d11-8dc8-8a5a5ef36415', '41960c6a-6f8f-44f4-a106-55325261f70e', 
				'0ec05da3-4890-4a5b-a92a-b202a0d525b8', '705ea1e7-5cde-4bf1-a895-8dccca345fd5', 
				'ef20c984-a45c-4f80-8b35-d608df85f4d4', 'ce09d914-cbd5-414e-9cb7-bfa88696ab36', 
				'31420622-bad5-40ed-9266-06ec94661dae', '5a96b215-d1a1-45e8-be91-7c48824f9d82', 
				'b30650a1-8228-4caf-8512-2715ecdead0a', '06a6e25a-90e1-4fe6-92c0-3e187a031208', 
				'f09615a5-1604-443d-bc4c-acf9e10a00f0', 'e695e265-4e6d-4bcf-a08a-93239df516e0', 
				'0b0b44db-8bdc-48cc-a8ca-202e1447a739', 'd45ffeb2-89e8-47e4-8664-6ed8ed76577b', 
				'fab69615-4194-43ba-bca2-823b464072db', '5309d9bb-66c9-446d-80f5-7ddd9c9dd38e', 
				'ce6b159c-4481-4518-8100-115680310cdf', 'be40b9ab-e1a4-4460-9880-d609c8e7ed31', 
				'99562bb6-a5bd-44fd-9c88-c91be2d9444e', '7f740ac8-df55-43ca-a00b-0279b6963ff1', 
				'a44a74a5-b436-4103-a36c-2247f8393a58', '095960af-f93e-49a0-bf8b-6f4af75d0f87', 
				'a347d8fb-5149-4450-92da-bd8576bb4bb8', 'eb89da7b-ec71-491c-a43a-6cac7bd08c14', 
				'8373ba8e-d0b1-4c1b-ba94-4a35572436ad', '8f196ea8-0686-47de-88bd-12662be764bc', 
				'cb1e01e3-ede0-4da1-aa83-364139874413', '2bbf3c9a-eed3-446a-a14d-437039ea7cf1', 
				'26c2cacb-f3c0-4d59-b0fe-0c77b18715f3', 'f0b885cb-6168-4bfb-8e81-e362409811a7', 
				'a904fb82-8a35-4520-856b-6eeaa2f5c7a8', '2350dd85-147e-4e8b-9353-4dc17658fed7', 
				'b6d363b6-4548-4626-accb-4e5298576bc9', '58ca7d11-d9ae-4a54-bd4e-e506369b5c91', 
				'68e53138-6747-4fda-8462-040a671055c8', '10578765-0c4f-4067-aec9-9f99b8465121', 
				'1355a4ff-8e3b-42e7-9914-428667915978', '4946529b-d24f-4e7e-b5a9-99ceac01ceda', 
				'0feebbac-140f-469a-9a1c-5837ef512f26', '9b6ac9f3-cbbe-48a4-a1d7-4d3ca2be2ba7', 
				'88ced614-8b57-4931-b21d-3ec54d700ce2', 'ef8efe73-286e-402d-8991-3d986b7390eb', 
				'378e0da3-be04-4089-bc3f-6ba79cdd332e', 'e82313e8-f05b-4627-9373-c932ab608563', 
				'205b02b0-e64f-4f62-9aae-624a35a78b98', '2e09dcaf-b0e8-425f-946a-7291e1ecefbc', 
				'09c11c25-04e1-46cd-8161-3fdfc134fda3', '86e82327-76ba-41ae-9318-3f2ec0ec051d', 
				'ad9997b8-b665-4afa-aad3-21aa08f65407', '90e975a9-a943-4cd3-ac3b-146cc0f26328', 
				'fcd4352f-3c1e-40cc-bc33-2e9e921d5d7d', '80cca30b-65a0-4368-a19c-9744281c9f6a', 
				'00bd40fe-0c79-4e64-afaf-d92d963f3add', 'fc33f586-c91c-4f52-bcc4-ce67949067bc', 
				'7cee9066-da91-4370-bb72-fb209ac8a56d', 'f1f39841-1c3b-491d-a0b6-607ad58ec5e4', 
				'3edca283-f207-44d2-84e9-051d5d8f899a', 'c66459d0-d764-4107-a5df-17d000bd90b3', 
				'f4418c13-a9c1-479c-b32f-814f12bb8f8a', '41d31ec3-8419-4567-92b8-31ee92b9cccf', 
				'72ed1e22-e9b8-49e3-a968-108be0a9fe32', '71949d9a-7d37-4486-b874-5ff6958c7738', 
				'61cb8807-8d78-4719-be85-fd63fdf2ee2d', 'c25bf9fc-e187-4c29-ae69-93ca118f42c6', 
				'0854821b-7abe-4081-a6ab-02d2feea8c17', 'add7789b-fa8c-4089-8c3b-650e648126b9', 
				'88c647cf-13bd-47f3-8933-0ced973151e0', '54f4ffa9-f86a-4975-9d0c-3db789370c6f', 
				'63869518-9a81-4fce-83c8-cf7b9e361188', 'a736319a-c218-4496-96b3-18ed1a7879f6', 
				'a6694ef7-b816-4944-af9b-169f21c2cfa4', 'fcc60e79-d817-4717-a833-937896e60c25', 
				'e63001c1-f425-463f-9d1d-d3be22f48eee', 'f2d85111-ca30-47e2-b615-d65301a40a34', 
				'1f1ad3b8-6ace-4b31-a8f6-2528d8ba3c49', 'f2ea74c3-0e37-48e2-8b70-2719b0fe45e4', 
				'b735fe0a-58d6-4d86-b678-b19dc7e4507d', '2139f31f-c88b-4d19-b5c1-fdb1f838059e', 
				'59b41150-7481-4937-bff3-194577f29edd', 'd3e2ee77-887c-4fcf-8af6-3c6ec468cf0c', 
				'438ebd28-5f30-483d-b859-19fef7142840', '808332a5-0ccd-4d32-9629-724ecc96a4b7', 
				'90477ccf-bc19-4563-a140-05c3fb5abf71', '557d9cd4-6ee0-41f6-9e51-84817597624a', 
				'a5393e29-f2d4-43e5-b219-9d3bd66cbd1b', '06aab5bd-7dca-4695-8098-fda4a4359d06', 
				'b67fd9dc-6124-4003-ab32-da2a14716b5c', '5ff32445-6932-41c9-8e22-c6b67f61a556', 
				'721bf835-87c3-43ed-b544-b6ea88d6f619', 'a0a2e121-8e40-492d-ae9f-8bc8018503ca', 
				'6e3d7681-8b9f-4cdb-8f2d-2096c6815635', 'd54507b4-53a7-4823-a46f-04fa65bf2dff', 
				'f444b799-798d-473a-80cf-c46679df8b9c', '059c7c95-43c6-4e38-b7aa-d87c00157428', 
				'42584980-8398-4029-b062-51420e999c78', 'cf77854c-889f-4b51-abc8-8c3a0e82915b', 
				'b9ef9dbf-2d16-44f2-901e-34d2f25f88c2']
        page_media.select_media_by_text('Work/Home/Daily Life')
        index = 0
        for name in workhomedailylife_list:
            self.report.start_uuid(udid[index])
            result = page_media.check_song_exists_by_text(name)
            self.report.new_result(udid[index], result)
            index = index + 1
            if  index%3 == 0:
                page_edit.swipe_element(L.import_media.library_listview.frame, 'up', 315)
                time.sleep(3)
                
        page_edit.el(L.edit.menu.back).click()        
        