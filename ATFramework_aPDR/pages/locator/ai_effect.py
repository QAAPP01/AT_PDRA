from .locator_type import *

class Launcher:
    ai_effect_entry = id("ai_template_entry")

class Template:
    library_title = id("top_toolbar_title")
    back = id("top_toolbar_back")
    try_now = id("btn_try_now")
    premium = xpath(f'//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[contains(@resource-id,"premium_icon")]')
    full_preview = id("ai_template_preview_card_view")
    media_library = id("pickerDeviceLibrary")
    toast = id("toast_text_hud")
    downloading = id("download_progress_bar")
    produce = id("iv_produce")
    leave = id("exit_btn")
    close = id("iv_close")

    @staticmethod
    def template(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"ai_template_image_view")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"ai_template_image_view")])[{index}]')

    @staticmethod
    def template_duration(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"template_duration_text")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"template_duration_text")])[{index}]')

    @staticmethod
    def template_clip_number(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"video_template_clip_count_text")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"video_template_clip_count_text")])[{index}]')

class Editor:
    play_btn = aid('[AID]TimeLine_Play')
    playing_time = id('playing_time')
    playing_bar = id('seekbar')
    replace_all = id('layout_replace_all')
    volume_entry = id('layout_volume')
    preview = id("movie_view")
    edit = id('iv_setting')
    export = id('iv_produce')
    close = id("iv_close")

    @staticmethod
    def clip(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"cv_background")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"cv_background")])[{index}]')

    class MediaPicker:
        @staticmethod
        def clip_duration(index=1):
            if index == 0:
                return xpath(f'//android.widget.TextView[2]/[contains(@resource-id,"duration")]')
            else:
                return xpath(f'(//android.widget.TextView[2]/[contains(@resource-id,"duration")])[{index}]')


    class Volume:
        slider = id('adjustable_parameter_seek_bar')
        slider_text = id("adjustTextNow")
        play_btn = id('btn_preview')
        cancel = id('cancel_button')
        apply = id('ok_button')

    class CropRange:
        done = id('ok_btn')
        trim_bar = id('trim_scroll_view')

    class Produce:
        back = id('iv_back')
        resolution_bar = id('resolution_seek_bar')
        resolution_1 = id('resolution_option1')
        resolution_2 = id('resolution_option2')
        resolution_3 = id('resolution_option3')
        resolution_4 = id('resolution_option4')
        produce = id('btn_produce')

    media_picker = MediaPicker
    volume = Volume
    crop_range = CropRange

class Producing:
    back = aid('[AID]Produce_Back')
    progress_bar = id('progress_bar')
    cancel = aid('[AID]ProjectProperties_Cancel')
    cancel_ok = aid('[AID]ConfirmDialog_OK')
    done = aid('[AID]ProjectProperties_Ok')
    save_to_file = id('btn_file_location')
    share_ok = id('btn_ok')

    def share_app_name(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"text_share")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"text_share")])[{index}]')

class Interface:
    launcher = Launcher
    template = Template
    editor = Editor
    producing = Producing
