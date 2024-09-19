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
        self.page_main, self.page_edit, self.page_media, self.page_preference, self.page_shortcut = shortcut

        self.click = self.page_main.h_click
        self.long_press = self.page_main.h_long_press
        self.element = self.page_main.h_get_element
        self.elements = self.page_main.h_get_elements
        self.is_exist = self.page_main.h_is_exist
        self.is_not_exist = self.page_main.h_is_not_exist

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

    @allure.story("Entry")
    @allure.title("From shortcut")
    def test_entry_from_shortcut(self, data):
        try:
            self.page_shortcut.enter_shortcut('AI Audio Tools')

            assert self.element(L.main.shortcut.demo_title).text == 'AI Audio Tools'

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Entry")
    @allure.title("Mute demo")
    def test_mute_demo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Audio Tools')

            assert self.page_shortcut.mute_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Entry")
    @allure.title("Back from demo")
    def test_back_from_demo(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_shortcut('AI Audio Tools')

            assert self.page_shortcut.back_from_demo()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Enter media picker")
    def test_speech_enhance_entry_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_media_picker('AI Audio Tools', audio_tool='Speech Enhance')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Back from media picker")
    def test_speech_enhance_back_from_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Audio Tools', audio_tool='Speech Enhance')

            assert self.page_shortcut.back_from_media_picker()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Enter trim before edit")
    def test_speech_enhance_entry_trim_before_edit(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_trim_before_edit('AI Audio Tools', audio_tool='Speech Enhance')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Back from trim before edit")
    def test_speech_enhance_back_from_trim_before_edit(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_trim_before_edit('AI Audio Tools', audio_tool='Speech Enhance')

            assert self.page_shortcut.back_from_trim()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Trim and edit")
    def test_speech_enhance_trim_and_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_trim_before_edit('AI Audio Tools', audio_tool='Speech Enhance')

            assert self.page_shortcut.trim_and_import()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Back from editor")
    def test_speech_enhance_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='Speech Enhance')

            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise


    @allure.story("Speech Enhance")
    @allure.title("Enter Editor")
    def test_speech_enhance_entry_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Audio Tools', audio_tool='Speech Enhance')

            assert self.page_shortcut.enter_editor(file=video_speech)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Play preview")
    def test_speech_enhance_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='Speech Enhance', file=video_speech)

            assert self.page_shortcut.preview_play()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Play start position")
    def test_speech_enhance_play_start_position(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='Speech Enhance', file=video_speech)

            assert self.page_shortcut.preview_beginning()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Play end position")
    def test_speech_enhance_play_end_position(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='Speech Enhance', file=video_speech)

            assert self.page_shortcut.preview_ending()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("Speech Enhance")
    @allure.title("Export")
    def test_speech_enhance_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='Speech Enhance', file=video_speech)

            assert self.page_shortcut.export()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Enter media picker")
    def test_ai_denoise_entry_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_media_picker('AI Audio Tools', audio_tool='AI Denoise')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Back from media picker")
    def test_ai_denoise_back_from_media_picker(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Audio Tools', audio_tool='AI Denoise')

            assert self.page_shortcut.back_from_media_picker()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Enter trim before edit")
    def test_ai_denoise_entry_trim_before_edit(self, data):
        try:
            if self.last_is_fail(data):
                pass

            assert self.page_shortcut.enter_trim_before_edit('AI Audio Tools', audio_tool='AI Denoise')

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Back from trim before edit")
    def test_ai_denoise_back_from_trim_before_edit(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_trim_before_edit('AI Audio Tools', audio_tool='AI Denoise')

            assert self.page_shortcut.back_from_trim()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Trim and edit")
    def test_ai_denoise_trim_and_import(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_trim_before_edit('AI Audio Tools', audio_tool='AI Denoise')

            assert self.page_shortcut.trim_and_import()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Back from editor")
    def test_ai_denoise_back_from_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='AI Denoise')

            assert self.page_shortcut.back_from_editor()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False

    @allure.story("AI Denoise")
    @allure.title("Enter Editor")
    def test_ai_denoise_entry_editor(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_media_picker('AI Audio Tools', audio_tool='AI Denoise')

            assert self.page_shortcut.enter_editor(file=video_speech)

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Play preview")
    def test_ai_denoise_play_preview(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='AI Denoise', file=video_speech)

            assert self.page_shortcut.preview_play()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Play start position")
    def test_ai_denoise_play_start_position(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='AI Denoise', file=video_speech)

            assert self.page_shortcut.preview_beginning()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Play end position")
    def test_ai_denoise_play_end_position(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='AI Denoise', file=video_speech)

            assert self.page_shortcut.preview_ending()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    @allure.story("AI Denoise")
    @allure.title("Export")
    def test_ai_denoise_export(self, data):
        try:
            if self.last_is_fail(data):
                self.page_shortcut.enter_editor('AI Audio Tools', audio_tool='AI Denoise', file=video_speech)

            assert self.page_shortcut.export()

        except Exception as e:
            traceback.print_exc()
            logger(e)
            data['last_result'] = False
            raise

    def sce_6_19_7(self):
        func_name = inspect.stack()[0][3]
        uuid = self.uuid[int(func_name.split('_')[3]) - 1]
        logger(f"\n[Start] {func_name}")


        try:
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
            self.click(L.main.shortcut.audio_tool.demo_speech_enhance)
            self.click(L.main.shortcut.try_it_now)

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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
            self.page_shortcut.enter_shortcut('AI Audio Tools')
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
