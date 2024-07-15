import time
import traceback
import pytest
import allure
from ATFramework_aPDR.ATFramework.utils.compare_Mac import HCompareImg
from ATFramework_aPDR.ATFramework.utils.log import logger
from ATFramework_aPDR.pages.locator import locator as L
from ATFramework_aPDR.SFT.conftest import TEST_MATERIAL_FOLDER as test_material_folder
from ATFramework_aPDR.pages.locator.locator_type import *

video_9_16 = 'video_9_16.mp4'
video_16_9 = 'video_16_9.mp4'
photo_9_16 = 'photo_9_16.jpg'
photo_16_9 = 'photo_16_9.jpg'
video_speech = 'speech_noise_1.mp4'


@allure.epic("Shortcut")
@allure.feature("AI Audio Tools")
class Test_Shortcut_AI_Audio_Tools:
    @pytest.fixture(autouse=True)
    def init_shortcut(self, shortcut):
        self.page_main, self.page_edit, self.page_media, self.page_preference = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

    @pytest.fixture(scope="module")
    def shared_data(self):
        data = {}
        yield data

    @allure.story("Entry")
    @allure.title("Enter demo page")
    def test_entry_demo_page(self, driver):
        try:
            self.page_main.enter_launcher()

            self.page_main.enter_shortcut('AI Audio Tools')

            assert self.element(L.main.shortcut.demo_title).text == 'AI Audio Tools'

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')

            pytest.fail(f"{str(e)}")

    @allure.story("Entry")
    @allure.title("Back to launcher")
    def test_back_to_launcher(self, driver):
        try:
            self.click(L.main.shortcut.demo_back)

            assert self.is_exist(L.main.shortcut.shortcut_name(0))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            pytest.fail(f"{str(e)}")

    def sce_6_19_3(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            before = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)
            self.click(L.main.shortcut.demo_mute)
            after = self.page_main.get_picture(L.main.shortcut.voice_changer.mute)

            if not HCompareImg(before, after).ssim_compare():
                
                return "PASS"
            else:
                raise Exception('[Fail] Mute button no change')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')

            return "FAIL"

    @allure.feature("Speech Enhance")
    @allure.story("Media Picker")
    @allure.title("Enter media picker")
    def test_speech_enhance_entry_media_picker(self, driver):
        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)

            assert self.is_exist(find_string('Add Media'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)

            pytest.fail(f"{str(e)}")

    @allure.feature("Speech Enhance")
    @allure.story("Media Picker")
    @allure.title("Back from media picker")
    def test_speech_enhance_back_from_media_picker(self, driver):
        try:
            self.click(L.import_media.media_library.back)

            assert self.is_exist(L.main.shortcut.shortcut_name(0))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()

            pytest.fail(f"{str(e)}")

    @allure.feature("Speech Enhance")
    @allure.story("Media Picker")
    @allure.title("Enter Editor")
    def test_speech_enhance_entry_editor(self, driver):
        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_edit.waiting()

            assert self.is_exist(L.main.shortcut.export)

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_edit.waiting()

            pytest.fail(f"{str(e)}")

    @allure.feature("Speech Enhance")
    @allure.story("Export")
    @allure.title("Produce video")
    def test_speech_enhance_produce_video(self, driver):
        try:
            self.click(L.main.shortcut.export)
            self.click(L.main.shortcut.produce)
            self.page_edit.waiting_produce()

            assert self.is_exist(L.main.shortcut.save_to_camera_roll)

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()

            pytest.fail(f"{str(e)}")

    @allure.feature("AI Denoise")
    @allure.story("Media Picker")
    @allure.title("Enter media picker")
    def test_ai_denoise_entry_media_picker(self, driver):
        try:
            self.click(L.main.shortcut.produce_home)
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_ai_denoise)
            self.click(L.main.shortcut.try_it_now)

            assert self.is_exist(find_string('Add Media'))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_ai_denoise)
            self.click(L.main.shortcut.try_it_now)

            pytest.fail(f"{str(e)}")

    @allure.feature("AI Denoise")
    @allure.story("Media Picker")
    @allure.title("Back from media picker")
    def test_ai_denoise_back_from_media_picker(self, driver):
        try:
            self.click(L.import_media.media_library.back)

            assert self.is_exist(L.main.shortcut.shortcut_name(0))

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()

            pytest.fail(f"{str(e)}")

    @allure.feature("AI Denoise")
    @allure.story("Media Picker")
    @allure.title("Enter Editor")
    def test_ai_denoise_entry_editor(self, driver):
        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_ai_denoise)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_edit.waiting()

            assert self.is_exist(L.main.shortcut.export)

        except Exception as e:
            traceback.print_exc()
            driver.driver.close_app()
            driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.click(L.main.ai_creation.entry)
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_ai_denoise)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_edit.waiting()

            pytest.fail(f"{str(e)}")

    @allure.feature("AI Denoise")
    @allure.story("Export")
    @allure.title("Produce video")
    def test_ai_denoise_produce_video(self, driver):
        try:
            self.click(L.main.shortcut.export)
            self.click(L.main.shortcut.produce)
            self.page_edit.waiting_produce()

            assert self.is_exist(L.main.shortcut.save_to_camera_roll)

        except Exception as e:
            traceback.print_exc()

            pytest.fail(f"{str(e)}")

    def sce_6_19_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_16_9)

            if self.is_exist(find_string('No sound detected')):


                self.click(id('btn_ok'))

                return "PASS"
            else:
                raise Exception('[Fail] No found "No sound detected" dialog')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_8(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.click(L.import_media.media_library.trim_back)

            if self.is_exist(find_string('Add Media')):

                return "PASS"
            else:
                raise Exception(f'[Fail] Tap preview "{video_speech}" fail')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_9(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.driver.swipe_element(L.import_media.trim_before_edit.left, 'right', 50)
            self.driver.swipe_element(L.import_media.trim_before_edit.right, 'left', 50)
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            if self.is_exist(L.main.shortcut.export):

                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter Voice Changer')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.click(xpath(f'//*[@text="{video_speech}"]/../*[contains(@resource-id,"btn_preview")]'))
            self.click(L.import_media.media_library.trim_next)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_10(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(L.main.shortcut.editor_back)

            if self.is_exist(find_string('Add Media')):

                return "PASS"
            else:
                raise Exception('[Fail] Enter media picker fail')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_11(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()
            self.click(L.main.shortcut.play)

            if self.is_exist(L.main.shortcut.export):

                return "PASS"
            else:
                raise Exception('[Fail] Cannot find the export button')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_12(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(L.main.shortcut.play)
            time.sleep(3)
            self.timecode_play = self.element(L.main.shortcut.timecode).text

            if self.timecode_play != "00:00":

                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {self.timecode_play}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_13(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(L.main.shortcut.play)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play != self.timecode_play:

                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_14(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_min(L.main.shortcut.playback_slider)
            timecode_play = self.element(L.main.shortcut.timecode).text

            if timecode_play == '00:00':

                return "PASS"
            else:
                raise Exception(f'[Fail] Timecode no change: {timecode_play}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_15(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(L.main.shortcut.audio_tool.info)

            if self.click(find_string('Try It Now')):

                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try It Now" fail')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_16(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '80.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_17(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '0.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_18(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '100.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_19(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '20.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_20(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '0.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_21(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '100.0':


                self.click(L.main.shortcut.editor_back)
                self.click(L.import_media.media_library.back)

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()

            return "FAIL"

    def sce_6_19_5(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)

            if self.is_exist(find_string('Add Media')):

                return "PASS"
            else:
                raise Exception('[Fail] Cannot enter media picker')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)

            return "FAIL"

    def sce_6_19_22(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()
            self.click(L.main.shortcut.audio_tool.info)

            if self.click(find_string('Try It Now')):

                return "PASS"
            else:
                raise Exception(f'[Fail] Click "Try It Now" fail')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_23(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '80.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_24(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '0.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_25(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.strength_slider)
            slider = self.element(L.main.shortcut.audio_tool.strength_slider).text
            if slider == '100.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_26(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '20.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_27(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_min(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '0.0':

                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_28(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.driver.drag_slider_to_max(L.main.shortcut.audio_tool.compensation_slider)
            slider = self.element(L.main.shortcut.audio_tool.compensation_slider).text
            if slider == '100.0':


                return "PASS"
            else:
                raise Exception(f'[Fail] Value incorrect: {slider}')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_29(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(L.edit.try_before_buy.premium_tag)

            if self.click(L.main.subscribe.back_btn):


                return "PASS"
            else:
                raise Exception(f'[Fail] Click IAP Back button fail')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_30(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.click(L.main.shortcut.export)

            if self.click(L.main.subscribe.back_btn):


                return "PASS"
            else:
                raise Exception(f'[Fail] Click IAP Back button fail')

        except Exception as err:
            traceback.print_exc()

            self.driver.driver.close_app()
            self.driver.driver.launch_app()

            self.page_main.enter_launcher()
            self.page_main.enter_shortcut('AI Audio Tools')
            self.click(find_string('AI Denoise'))
            self.click(L.main.shortcut.try_it_now)
            self.page_media.select_local_video(test_material_folder, video_speech)
            self.page_media.waiting()

            return "FAIL"

    def sce_6_19_31(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")
        

        try:
            self.click(L.main.shortcut.full_editor)

            if self.is_exist(L.edit.menu.produce):
                

                return "PASS"
            else:
                raise Exception(f'[Fail] No timeline produce button')

        except Exception as err:
            traceback.print_exc()
            
            self.driver.driver.close_app()

            return "FAIL"
