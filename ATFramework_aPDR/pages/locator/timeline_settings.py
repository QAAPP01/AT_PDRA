from .locator_type import *

class Preference:
    default_image_duration = id("settings_default_image_duration")
    default_image_duration_value = id('settings_default_image_duration_value')
    default_pan_zoom_effect = aid("[AID]PremiumContent_Switch")
    back = id("iv_back")
    reset_all_tips = id("reseting_all_tips")
    default_transition_duration = id('settings_default_transition_duration')
    default_transition_duration_value = id('settings_default_transition_duration_value')
    default_title_duration = id('settings_default_title_duration')
    default_title_duration_value = id('settings_default_title_duration_value')
    shopping_cart = id("btn_shopping_cart")
    open_tool_menu_switch = aid("[AID]Open_Tool_Menu_When_Select_An_Object_In_Timeline")
    display_file_name_switch = id('displayNameInMedia_switch')
    text_video_quality = id('settings_default_video_quality_text')
    remove_watermark = aid('[AID]remove_watermark')
    advanced_setting = id('advanced_setting')
    settings_edit_mode = id('settings_edit_mode')
    current_UI_mode_text = id('settings_current_edit_mode_text')
    radio_btn_portrait = id('radio_btn_portrait')
    radio_btn_landscape = id('radio_btn_landscape')
    radio_btn_auto = id('radio_btn_auto')

    @staticmethod
    def UI_mode(mode):
        if mode == "auto-rotate":
            return id('radio_btn_auto')
        else:
            return id(f'radio_btn_{mode}')

class DefaultImageDuration():
    slider = aid("[AID]Transition_Seekbar")
    txt_duration = id('durationText')
    ok = aid("[AID]Dialog_OK")
    cancel = aid("[AID]Dialog_Cancel")

class DefaultTransitionDuration():
    slider = aid("[AID]Transition_Seekbar")
    txt_duration = id('durationText')
    ok = aid("[AID]Dialog_OK")
    cancel = aid("[AID]Dialog_Cancel")

class DefaultTitleDuration():
    slider = aid("[AID]Transition_Seekbar")
    txt_duration = id('durationText')
    ok = aid("[AID]Dialog_OK")
    cancel = aid("[AID]Dialog_Cancel")

class DefaultVideoQuality():
    btn_back = id('video_quality_back_button')
    radio_btn_uhd = id('radio_btn_uhd')
    radio_btn_fhd = id('radio_btn_fhd')
    radio_btn_hd = id('radio_btn_hd')
    radio_btn_sd = id('radio_btn_sd')

class Interface():
    settings = Preference()
    preference = Preference()
    default_image_duration = DefaultImageDuration()
    default_transition_duration = DefaultTransitionDuration()
    default_title_duration = DefaultTitleDuration()
    default_video_quality = DefaultVideoQuality()