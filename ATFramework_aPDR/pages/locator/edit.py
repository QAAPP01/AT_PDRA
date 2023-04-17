from .locator_type import *


class Menu:
    class Produce_sub_page:
        save = id('text_setting_save_project')
        produce = id('text_setting_save_and_produce_project')

    produce_sub_page = Produce_sub_page()
    back = aid("[AID]TimeLine_Back")
    # back_session = aid("[AID]Session_Back")
    back_session = id('btn_session_back')
    back_library = aid("[AID]Library_Back")
    import_media = aid("[AID]TimeLine_VideoPhotoAudio")
    effect = aid("[AID]TimeLine_Layer")
    fx = aid("[AID]TimeLine_Fx")
    settings = id('btn_setting')
    produce = aid("[AID]TimeLine_Save")
    timeline_setting = aid("[AID]TimeLine_Setting")
    undo = id("btn_undo")
    play = aid("[AID]TimeLine_Play")
    # edit = id("btn_edit_img") # after select video
    edit = id("btn_session_edit")
    split = id("btn_split")
    delete = id("btn_delete")
    home = id('btn_home')
    btn_apply_all = id('btn_apply_all')


class ToolMenu:
    back = id('btn_session_back')


class SubToolMenu:
    back = id('btn_session_back')
    reset = id('btn_reset')


class SubMenu_Timeline_Setting():
    menu = Menu()
    audio_mixing = aid("[AID]Setting_AudioMixing")
    settings = aid("[AID]Setting_About")
    tips = aid("[AID]Setting_Helo")
    tutorials = aid("[AID]Setting_Help_Videos")


class Edit_sub():
    volume = aid("[AID]FloatingMenu_Volume")
    crop = aid("[AID]FloatingMenu_Crop")
    title = aid("[AID]FloatingMenu_Title Designer")
    duplicate = aid("[AID]FloatingMenu_Duplicate")
    skin_smoothener = aid("[AID]FloatingMenu_Skin Smoothener")
    speed = aid("[AID]FloatingMenu_Speed")
    rotate = aid("[AID]FloatingMenu_Rotate")
    color = aid("[AID]FloatingMenu_Color")
    reverse = aid("[AID]FloatingMenu_Reverse")
    pan_zoom = aid("[AID]FloatingMenu_Pan & Zoom")
    flip = aid("[AID]FloatingMenu_Flip")
    sharpness = aid("[AID]FloatingMenu_Sharpness")
    stabilizer = aid("[AID]FloatingMenu_Stabilizer")
    opacity = aid("[AID]FloatingMenu_Opacity")
    fade = aid("[AID]FloatingMenu_Fade")
    chroma_key = aid("[AID]FloatingMenu_Chroma Key")
    color_selector = aid("[AID]FloatingMenu_Color Selector")
    mask = aid("[AID]FloatingMenu_Mask")
    blending = aid("[AID]FloatingMenu_Blending")
    # bottom_edit_menu = id("entry_list")
    bottom_edit_menu = id("tools_menu")
    back_button = id("btn_session_back")
    adjustment_menu = id("color_adjustments_fragment")
    effect_menu = id("fxPage")
    crop_hint = id("pinch_image")
    in_animation_entry = id('in_animation_entry')
    out_animation_entry = id('out_animation_entry')


class Blending_Sub():
    Blending0 = aid("[AID]BlendingThumbnail_0")  # Normal
    Blending1 = aid("[AID]BlendingThumbnail_1")  # Overlay
    Blending2 = aid("[AID]BlendingThumbnail_2")  # Multiply
    Blending3 = aid("[AID]BlendingThumbnail_3")  # Screen
    Blending4 = aid("[AID]BlendingThumbnail_4")  # Hard Light
    Blending5 = aid("[AID]BlendingThumbnail_5")  # Soft Light
    Blending6 = aid("[AID]BlendingThumbnail_6")  # Lighten
    Blending7 = aid("[AID]BlendingThumbnail_7")  # Darken
    Blending8 = aid("[AID]BlendingThumbnail_8")  # Difference
    Blending9 = aid("[AID]BlendingThumbnail_9")  # Hue
    Blending10 = aid("[AID]BlendingThumbnail_10")  # Luminous
    OpacitySpeedBar = aid("[AID]PiPControl_OpacitySpeedBar")  # OpacitySpeedBar
    Reset = aid("[AID]Session_Reset")  # Reset
    Back = aid("[AID]Session_Back")  # Back


class Mask_Sub():
    # mask_none = xpath("//android.widget.ImageView[@resource-id='com.cyberlink.powerdirector.DRA140225_01:id/btn_mask_none']")
    # mask_linear = xpath("//android.widget.ImageView[@resource-id='com.cyberlink.powerdirector.DRA140225_01:id/btn_mask_linear']")
    # mask_parallel = xpath("//android.widget.ImageView[@resource-id='com.cyberlink.powerdirector.DRA140225_01:id/btn_mask_parallel']")
    # mask_eclipse = xpath("//android.widget.ImageView[@resource-id='com.cyberlink.powerdirector.DRA140225_01:id/btn_mask_eclipse']")
    # mask_rectangle = xpath("//android.widget.ImageView[@resource-id='com.cyberlink.powerdirector.DRA140225_01:id/btn_mask_rectangle']")
    # seekbar_feather = xpath("/android.widget.SeekBar[@resource-id='com.cyberlink.powerdirector.DRA140225_01:id/seekbar_feather']")
    # switch_invert = xpath("//android.widget.Switch[@resource-id='com.cyberlink.powerdirector.DRA140225_01:id/switch_invert']")
    mask_none = id("btn_mask_none")
    mask_linear = id("btn_mask_linear")
    mask_parallel = id("btn_mask_parallel")
    mask_eclipse = id("btn_mask_eclipse")
    mask_rectangle = id("btn_mask_rectangle")
    seekbar_feather = id("adjustable_parameter_block")
    switch_invert = id("btn_mask_invert")
    rotate_right_point = id("rotate_right_point")
    rotate_left_point = id("rotate_left_point")
    move_point = id("move_point")


class Effect_Sub():
    # title = id("tab_title")
    title = id("library_menu_title")
    # video = id("tab_pip_video")
    video = id("library_menu_pip_video")
    # image = id("tab_pip_photo")
    image = id("library_menu_pip_photo")
    # sticker = id("tab_sticker")
    sticker = id("library_menu_sticker")
    overlay = id('library_menu_overlay')

    class Sticker_tabs():
        tab_top = id('tab_top')
        tab_new = id('tab_new')
        tab_free = id('tab_free')
        tab_downloaded = id('tab_dlc_sticker')

    sticker_tabs = Sticker_tabs()


class Pan_Zoom_Effect():
    no_effect = id("radiobutton_kenburns_no_motion")
    random_motion = id("radiobutton_kenburns_random_motion")
    custom_motion = id("radiobutton_kenburns_custom_motion")
    cancel = aid("[AID]Dialog_Cancel")
    ok = aid("[AID]Dialog_OK")
    # apply_to_all = aid("[AID]Dialog_Apply_All")
    apply_to_all = id('btn_apply_all')
    custom_motion_start = id('layout_frame_start_roi')
    custom_motion_end = id('layout_frame_end_roi')
    # back = aid('[AID]Session_Back')
    back = aid('[AID]TimeLine_Back')
    reset = aid('[AID]Session_Reset')


class Crop:
    btn_original = id('btn_crop_original')
    btn_free = id('btn_crop_free')
    btn_9_16 = id('btn_crop_9_16')
    btn_1_1 = id('btn_crop_1_1')
    btn_4_5 = id('btn_crop_4_5')
    btn_16_9 = id('btn_crop_16_9')
    btn_4_3 = id('btn_crop_4_3')
    btn_3_4 = id('btn_crop_3_4')
    btn_21_9 = id('btn_crop_21_9')
    right_top = aid('[AID]Resizable_RightTop')
    boundary = id('resizable_boundary')
    apply = id('apply_btn')
    cancel = id('cancel_btn')
    reset = id('resetBtn')
    play_pause = id('playPauseBtn')
    time_code = id('time_code_text')
    slider = id('movie_seekbar')


class Reverse:
    dialog_ok = aid("[AID]Dialog_OK")
    dialog_cancel = aid("[AID]Dialog_Cancel")
    ad = id("native_ad_container")
    ad_promotion = id("cross_promotion")
    remove_ok = aid("[AID]Dialog_OK")  # PDRa have to change the code
    remove_cancel = aid("[AID]Dialog_Cancel")  # PDRa have to change the code
    progress_bar = id('progress_bar')


class Produce_Video_Window():
    cancel = aid("[AID]ProjectProperties_Cancel")


class Stabilizer_Correction():
    mask_button = id("mask_bottom")


class Stabilizer():
    ad = id("native_ad_container")
    ad_promotion = id("cross_promotion")
    motion_level = id("ea_widget_parameter_seek_bar")
    # iap_back = aid("[AID]Upgrade_No")
    iap_back = aid("[AID]IAP_Back")


class Sharpness():
    sharpness_level = id("ea_widget_parameter_seek_bar")
    value = id("ea_widget_parameter_edit")


class Opacity():
    # slider = aid("[AID]PiPControl_OpacitySpeedBar")
    slider = id("adjustable_parameter_seek_bar")


class Fade():
    fade_in = aid("[AID]Fade_ApplyFadeIn")
    fade_out = aid("[AID]Fade_ApplyFadeOut")
    ok = aid("[AID]Dialog_OK")


class Chroma_Key():
    btn_color_straw = id("color_straw_icon")
    reset = aid("[AID]Session_Reset")


class Color_Board():
    red = aid("[AID]ColorBoard_Red")
    pink = aid("[AID]ColorBoard_Pink")
    white = aid("[AID]ColorBoard_Write")


class Color_Selector():
    red_number = aid("[AID]ColorBoard_RedNumber")
    green_number = aid("[AID]ColorBoard_GreenNumber")
    blue_number = aid("[AID]ColorBoard_BlueNumber")
    red = aid("[AID]ColorBoard_Red")
    pink = aid("[AID]ColorBoard_Pink")


class Preview:
    movie_view = id("movie_view")
    preview = xpath('//*[contains(@resource-id,"movie_view")]/android.view.View')
    time_code = id('playingTime')
    set_font = aid("[AID]TitleDesign_RightTop")
    # rotate = aid("[AID]Resizable_RightBottom")
    rotate = id('rotate_point')
    # size_left_bottom = id("control_point_corner_left_bottom" )
    size_left_bottom = id("resize_point_left_top")
    pip_border = id('rectangle_mask_border')
    watermark = id("water_mark_image")
    water_mark = id("water_mark_image")
    water_mark_border = id("watermark_border")  # trigger subscription: water_mark_image > watermark_border
    # btn_title_designer_right_top = aid("[AID]TitleDesign_RightTop")
    # btn_title_designer_right_top = id("rz_control_corner_right_top")
    # btn_title_designer_right_top = id("rz_control_corner_style")
    btn_title_designer_right_top = id("title_designer_corner_right_top")
    # btn_title_designer_right_bottom = aid("[AID]TitleDesign_RightBottom")
    # btn_title_designer_right_bottom = id("rz_control_corner_right_bottom")
    btn_title_designer_right_bottom = id("control_point_corner_right_bottom")
    btn_fullscreen_landscape_preview = id("btn_fullscreen_landscape_preview")
    btn_fullscreen_portrait_preview = id("btn_fullscreen_portrait_preview")
    fullscreen_current_position = id("current_position")
    btn_fullscreen_play_pause = id("movie_play_pause")
    pan_and_zoom_preview = id("pan_zoom_video_roi_view")
    btn_close_fullscreen = id('leave_fullscreen')
    help_not_show_tip_again = id('help_not_show_tip_again')
    btn_close = id('btn_close')
    import_tips_icon = id('import_tips_icon')


class Timeline:
    slider = id("adjustable_parameter_seek_bar")
    main_track_import = id("icon_import_vp")
    main_track_import_float = id("icon_import_vp_pinned")
    tool = id('label')  # non unique
    sub_tool = id('tool_entry_label')  # non unique
    option_label = id("option_label")
    timeline_area = id('container_of_tracks')
    item_view_border = id("item_view_border")
    master_clip = id("item_view_border")
    effect_1st = (
    "xpath", "(//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout)[2]")

    clip_photo = ("xpath", '//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLinePhoto_")]')
    clip_title = id("item_view_title")
    tx_out = aid("[AID]Item_TxEffectOut")
    tx_in = aid("[AID]Item_TxEffectIn")
    playhead = id("timeline_playhead_indicator")
    trim_indicator = id("btn_trim_indicator")
    track = ("xpath", '//*[contains(@resource-id,"track_content")]')
    skin_smoothener = id("skin_smooth_effect")
    playhead_timecode = id('timeline_playhead_label')
    # playhead_timecode = id('timeline_ruler')
    track_content = id('track_content')
    item_view_title = id('item_view_title')
    timecode = id("timeline_playhead_label")
    fx_effect_thumbnail = id('fx_effect_thumbnail')
    item_view_thumbnail_host = id('item_view_thumbnail_host')
    exceed_max_video = aid('[AID]ConfirmDialog_OK')
    first_audio = ("xpath", '(//android.widget.LinearLayout[@content-desc="[AID]TimeLineAudio_mp3.mp3"])[1]')
    timeline_ruler = id('timeline_ruler')
    track_of_ruler = id('track_of_ruler')
    overlaytrack_container = id('tracks_container_of_not_main')
    btn_import = id('layout_import')
    btn_import2 = id('icon_import_vp')  # import btn id is different when timeline have content
    intro_video_entry = id('intro_video_entry')
    outro_video_entry = id('outro_video_entry')
    slider_value = id('adjustTextNow')
    reset = id('btn_reset')
    apply_all = id('btn_apply_all')

    @staticmethod
    def clip(index=1):
        if index == 0:
            return xpath(f'(//*[contains(@resource-id,"item_view_thumbnail_host")])[{index}]')
        else:
            return xpath(f'//*[contains(@resource-id,"item_view_thumbnail_host")]')

    @staticmethod
    def master_video(file_name=None):
        if file_name:
            return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineVideo_{file_name}")]')
        else:
            return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineVideo_")]')

    @staticmethod
    def master_video_thumbnail(file_name=None, clip_index=1, thumbnail_index=1):
        if file_name:
            return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineVideo_{file_name}")])[{clip_index}]/android.widget.ImageView')
        else:
            return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineVideo_")]/android.widget.ImageView)[1]')

    @staticmethod
    def master_photo(file_name=None, index=1):
        if file_name:
            if index:
                return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLinePhoto_{file_name}")])[{index}]')
            else:
                return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLinePhoto_{file_name}")]')
        else:
            if index:
                return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLinePhoto_")])[{index}]')
            else:
                return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLinePhoto_")]')

    @staticmethod
    def clip_audio(file_name=None, index=1):
        if file_name:
            if index:
                return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_{file_name}")])[{index}]')
            else:
                return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_{file_name}")]')
        else:
            if index:
                return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_")])[{index}]')
            else:
                return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_")]')


class Pip:
    @staticmethod
    def clip(index=1):
        if index == 0:
            return xpath(f'(//*[contains(@resource-id,"item_view_thumbnail_host")])[{index}]')
        else:
            return xpath(f'//*[contains(@resource-id,"item_view_thumbnail_host")]')

    @staticmethod
    def clip_audio(file_name=None, index=1):
        if file_name:
            if index:
                return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_{file_name}")])[{index}]')
            else:
                return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_{file_name}")]')
        else:
            if index:
                return xpath(f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_")])[{index}]')
            else:
                return xpath(f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_")]')

    @staticmethod
    def audio_thumbnail(file_name=None, index=1):
        if file_name:
            return xpath(
                f'(//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_{file_name}")])[{index}]/android.widget.ImageView')
        else:
            return xpath(
                f'//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineAudio_")]/android.widget.ImageView')

    tab_list = id('top_area_recycler')
    # btn_edit_face = id('text_button')
    btn_edit_face = find_string('Color')
    # btn_edit_bolder = id('border_button')
    btn_edit_bolder = find_string('Border')
    # btn_edit_shadow = id('shadow_button')
    btn_edit_shadow = find_string('Shadow')
    # switch_font_face = id('face_enable_switch')
    # btn_font = aid('[AID]Item_InputText')
    # btn_font = id('font_button')
    btn_font = find_string('Font')
    btn_format = find_string('Format')
    # font_list = aid('[AID]Item_InputText')
    font_recyclerview = id('font_recyclerview')
    font_list = id('material_text_item_text')
    font_item = id('font_item')
    # font_list_body = class_name('android.widget.ListView')
    font_list_body = id('font_style_page')
    # bold = aid('[AID]TextEdit_Bold')
    bold = id('text_bold')
    # italic = aid('[AID]TextEdit_Italic')
    italic = id('text_italic')
    # align_left = aid('[AID]TextEdit_AlignLeft')
    # align_mid = aid('[AID]TextEdit_AlignMid')
    # align_right = aid('[AID]TextEdit_AlignRight')
    align = id('text_alignment')
    align_left = id('text_alignment_left')
    align_center = id('text_alignment_center')
    align_right = id('text_alignment_right')

    tab_color = id('color_text')
    tab_gradient = id('gradient_text')

    tab_border1 = id('inner_border_text')
    tab_border2 = id('outer_border_text')

    # color_red = aid('[AID]TextColor_Red')
    # color_pink = aid('[AID]TextColor_Pink')
    color_list = id('color_recycler_view')
    color_item = id('color_image_view')
    color_palette_item = id('colors_container')

    # title_object = id('rz_content')
    pip_object = id('resizable_boundary')
    title_text_edit_area = aid('[AID]TextEdit_Text')
    title_text_edit_confirm = aid('[AID]TextEdit_Confirm')
    switch_border = id('border_enable_switch')
    border_size_text = id('border_size_Text_view')
    slider_border_size = id('border_size_seek_bar')
    switch_shadow = id('shadow_enable_switch')
    switch_fill_shadow = id('shadow_enable_switch')
    slider_shadow_distance = id('shadow_distance_seek_bar')
    font_download_btn = id('font_download_image')
    title_slider_area = id('title_slider_area')
    slider_seekbar = id('seekbar')
    slider_opacity = id('opacity_slider')
    slider_transition = id('transition_slider')
    slider_angle = id('angle_slider')
    slider_size = id('size_slider')
    slider_blur = id('blur_slider')
    slider_distance = id('distance_slider')
    slider_direction = id('direction_slider')

    class Text:
        @staticmethod
        def text_layout(index=1):
            if index == 0:
                return xpath(f'//*[contains(@resource-id,"btn_linearlayout")]')
            else:
                return xpath(f'(//*[contains(@resource-id,"btn_linearlayout")])[{index}]')

        @staticmethod
        def font_category(index=1):
            if index == 0:
                return xpath(f'//*[contains(@resource-id,"category_name")]')
            else:
                return xpath(f'(//*[contains(@resource-id,"category_name")])[{index}]')

        @staticmethod
        def font_name(index=1):
            if index == 0:
                return xpath(f'//*[contains(@resource-id,"material_text_item_text")]')
            else:
                return xpath(f'(//*[contains(@resource-id,"material_text_item_text")])[{index}]')

        @staticmethod
        def font(index=1):
            if index == 0:
                return xpath(f'//*[contains(@resource-id,"font_item")]')
            else:
                return xpath(f'(//*[contains(@resource-id,"font_item")])[{index}]')

        add = id("library_unit_add")
        back = id("back_button")
        font_favorite_message = id("favorite_message")
        font_import = id("import_button")
        font_filter = id("filter_button")
        font_filter_1 = xpath(f'(//*[contains(@resource-id,"selection_btn")])[1]')
        font_filter_2 = xpath(f'(//*[contains(@resource-id,"selection_btn")])[2]')
        font_filter_3 = xpath(f'(//*[contains(@resource-id,"selection_btn")])[3]')
        font_filter_4 = xpath(f'(//*[contains(@resource-id,"selection_btn")])[4]')
        font_filter_5 = xpath(f'(//*[contains(@resource-id,"selection_btn")])[5]')
        font_filter_back = id("filter_back_button")


    class ColorPicker():
        page = id('customize_color_area')
        slider_hue = id('text_edit_primary_color_pick_vertical')
        color_map = id('fill_color')
        first_color = id('first_select_color')
        second_color = id('second_select_color')
        btn_dropper = id('dropper_button')
        text_red = id('color_red_edit_text')
        text_green = id('color_green_edit_text')
        text_blue = id('color_blue_edit_text')

    colorpicker = ColorPicker()
    premium_font_icon = id('try_icon')


class AspectRatio:
    ratio_16_9 = id("layout_ratio_16_9")
    ratio_9_16 = id("layout_ratio_9_16")
    ratio_1_1 = id("layout_ratio_1_1")
    ratio_21_9 = id("layout_ratio_21_9")
    ratio_4_5 = id("layout_ratio_4_5")

class Transition():
    # duration_text = id('durationText')
    duration_text = id('adjustTextNow')
    timeline_transition = id('item_view_tx_effect_out')
    ok = aid('[AID]Dialog_OK')
    # btn_show_transition_duration = id('btn_show_transition_duration')
    btn_show_transition_duration = id('btn_transition_duration')
    apply_to_all = aid('[AID]Transition_ApplyAllCheck')


class Tips():
    chx_enable = id("help_enable_tip")


class Preset_sub():
    def __init__(self):
        for i in range(19):
            setattr(self, "color_profile_%s" % i, aid("[AID]ColorPresetThumbnail_%s" % i))

    frame = id("content_container")


class Adjust_sub():
    # frames = xpath('//android.widget.LinearLayout[contains(@resource-id,"ea_widget_container")]/android.widget.LinearLayout')
    frames = id("adjustable_parameter_block")
    # number = id("ea_widget_parameter_edit")
    number = id("adjustTextNow")
    # progress = id("ea_widget_parameter_seek_bar")
    progress = id("adjustable_parameter_seek_bar")
    reset = id('btn_reset')


class ChromaKey_sub():
    frames = xpath(
        '//android.widget.LinearLayout[contains(@resource-id,"ea_widget_container")]/android.widget.LinearLayout')
    number = id("ea_widget_parameter_edit")
    progress = id("ea_widget_parameter_seek_bar")


class Color_sub():
    frame = aid("[AID]ColorPresetList")
    perset = id("btn_effect_color_preset")
    adjust = id("btn_effect_color_adjust")
    adjust_sub = Adjust_sub()
    chromakey_sub = ChromaKey_sub()
    white_balance = id("btn_effect_white_balance")
    preset_sub = Preset_sub()
    # white_balance_sub = White_balance_sub()


class Speed():
    # slider = aid("[AID]SpeedControl_SpeedBar")
    slider = id("adjustable_parameter_seek_bar")
    # preview_toast_text = id("preview_toast_text_hud")
    preview_toast_text = id("adjustTextNow")
    # ease_in = id("easeInSwitch")
    # ease_out = id("easeOutSwitch")
    ease_in = ("xpath", '(//*[contains(@resource-id,"option_list")])/*[2]')
    ease_out = ("xpath", '(//*[contains(@resource-id,"option_list")])/*[3]')
    # mute_audio = id("muteSwitch")
    mute_audio = ("xpath", '(//*[contains(@resource-id,"option_list")])/*[1]')


class Subscription():
    btn_free_trial = id("subscribe_free_trial_btn_layout")


class Try_Before_Buy():
    remove = aid('[AID]Upgrade_No')
    free_trial = aid('[AID]Subscribe_Unlock_All')
    premium_features_used_bubble = id('premium_features_used_bubble')
    btn_tryit = id('btnTryIt')
    btn_subtounlock = id('unlock_content_view')
    icon_try = id('library_unit_lock')
    btn_delete_premium = id('delete_premium_btn')
    try_it = aid('[AID]Upgrade_No')
    btn_ads_sub = id('btnPurchase')


class Audio_Mixing():
    edit_text = id('audioMixing_editText')
    ok = aid('[AID]Dialog_OK')
    cancel = aid('[AID]Dialog_Cancel')
    volume_text = id('text_progress')
    slider_volume = id('slider_volume')
    maintrack_frame = id('volume_of_vp')
    othertracks_frame = id('volumes_container_of_not_main')


class Audio_Configuration():
    # volume_seekbar = aid('[AID]Volume_Seekbar')
    volume_seekbar = id('adjustable_parameter_seek_bar')
    btn_audio_mixing = id('audioMixingTextView')
    audio_mixing = Audio_Mixing()
    ok = aid('[AID]Dialog_OK')
    cancel = id('[AID]Dialog_Cancel')


class Audio_Denoise():
    denoise_value = id('denoise_param_value')
    slider = id('adjustable_parameter_seek_bar')


class Settings:
    menu = id('btn_setting')
    aspect_ratio = aid("[AID]Setting_Ratio")
    preference = aid('[AID]Setting_About')


    class DefaultImageDuration:
        default_image_duration = id("settings_default_image_duration")
        slider = aid("[AID]Transition_Seekbar")
        txt_duration = id('durationText')
        ok = aid("[AID]Dialog_OK")
        cancel = aid("[AID]Dialog_Cancel")

    class SendFeedback():
        send_feedback_btn = id('send_feedback_layout')
        feedback_text = aid('[AID]FeedBack_Text')
        feedback_email = aid('[AID]FeedBack_Email')
        top_right_btn = aid('[AID]TopBar_RightButton')
        feedback_device_model_text = id('bc_feedback_devicemodel')
        feedback_os_version_text = id('bc_feedback_osver')
        feedback_preview_view = id("scrollview_preview_feedback_outter")
        confirm_no_btn = id('no_text')

    about_btn = find_string('About PowerDirector')
    powerdirector_for_pc_btn = find_string('PowerDirector for PC')
    send_feedback_btn = id('faq_send_feedback')
    send_feedback = SendFeedback()
    scroll_view = class_name('android.widget.ScrollView')


class Keyframe():
    btn_keyframe = id('btn_keyframe')
    btn_keyframe_img = id('btn_keyframe_img')

    class Transform_Keyframe():
        text_x = id('text_x')
        text_y = id('text_y')
        text_scale = id('text_scale')
        text_rotation = id('text_rotation')

    transform_keyframe = Transform_Keyframe()
    remove_all = id('item_setting_keyframe_remove_all')
    duplicate_previous = id('item_setting_keyframe_duplicate_previous')
    duplicate_next = id('item_setting_keyframe_duplicate_next')


class Title_Animation():
    effect_list = id('animation_list')
    duration_slider = id('adjustable_parameter_seek_bar')
    duration_text = id('adjustTextNow')
    btn_in_animation = id('btn_in_animation')
    btn_out_animation = id('btn_out_animation')
    ok_btn = aid('[AID]ConfirmDialog_OK')
    cancel_btn = aid('[AID]ConfirmDialog_Cancel')


class Backdrop():
    btn_backdrop_enable = id('btn_backdrop_enable')
    btn_backdrop_type = id('btn_backdrop_type')
    btn_backdrop_color = id('btn_backdrop_color')
    btn_backdrop_opacity = id('btn_backdrop_opacity')
    btn_backdrop_y_offset = id('btn_backdrop_y_offset')
    btn_type_rectangle = id('btn_type_rectangle')
    btn_type_curved_edge = id('btn_type_curved_edge')
    btn_type_rounded = id('btn_type_rounded')
    btn_type_ellipse = id('btn_type_ellipse')
    btn_type_bar = id('btn_type_bar')
    hue_slider = aid('[AID]ColorBoard_ColorScroll')
    saturation_slider = aid('[AID]ColorBoard_ColorPick')
    preset_red = aid('[AID]ColorBoard_Red')
    preset_pink = aid('[AID]ColorBoard_Pink')


class Motion_Graphic_Title():
    dropdownmenu_text = id('material_title_item_text')
    font_list_body = ('id', 'android:id/select_dialog_listview')
    font_list = aid('[AID]Item_InputText')
    font_name = id('material_text_item_text')
    download_font = id('font_download_image')
    premium_font_icon = id('font_try_icon')


class Tutorial_Bubble():
    dialog = id('tooltip_viewpager')
    dialog_text = id('dialog_content')
    dialog_got_it = id('dialog_got_it')


class Fit_And_Fill():
    btn_fit = id('btn_fit')
    btn_fill = id('btn_fill')
    btn_background = id('btn_background')
    btn_none = id('btn_none')
    btn_blur = id('btn_blur')
    card_color = id('card_color')
    btn_background_color = id('btn_background_color')
    btn_background_pattern = id('btn_background_pattern')
    list_background_color = id('list_background_color')
    color_picker = id('applied_color')
    list_background_pattern = id('list_background_pattern')
    pattern_layout = id('pattern_layout')
    blur_slider = id('adjustable_parameter_seek_bar')
    blur_text = id('adjustTextNow')



class Background:
    btn_background = id('btn_background')
    btn_none = id('btn_none')
    btn_blur = id('btn_blur')
    btn_background_color = id('btn_background_color')
    btn_background_pattern = id('btn_background_pattern')
    list_background_color = id('list_background_color')
    color_picker = id('applied_color')
    list_background_pattern = id('list_background_pattern')
    blur_slider = id('adjustable_parameter_seek_bar')
    blur_text = id('adjustTextNow')
    try_icon = xpath('//*[contains(@resource-id,"try_icon")]')
    download_icon = id("download_icon")

    @staticmethod
    def card_color(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"card_color")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"card_color")])[{index}]')

    @staticmethod
    def pattern_layout(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"pattern_layout")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"pattern_layout")])[{index}]')

class Replace():
    btn_replace_anyway = id('replace_text_view')
    btn_cancel_replace = id('cancel_text_view')
    bottom_area = id('bottom_area')
    drag_text = id('drag_text')
    duration_text = id('duration_text')
    seek_bar = id('seek_bar')
    trim_area = id('trim_area')
    trim_view = id('trim_view')
    ok_btn = id('ok_btn')
    warning_title = id('warning_title')


class Duration:
    slider = aid('[AID]Transition_Seekbar')
    text_duration = id('durationText')
    btn_cancel = id("btnClose")
    btn_ok = aid('[AID]Dialog_OK')
    switch_apply_to_all_photo = aid('[AID]Transition_ApplyAllPhotosCheck')
    switch_apply_to_all_pip = aid('[AID]Transition_ApplyAllPIPsCheck')
    switch_apply_as_default = aid('[AID]Transition_ApplyAsDefaultCheck')


class Music:
    local = id("tab_music_local")
    sort = id("action_sort")
    by_name = id("by_name")
    by_ascending = id("order_asc")


class Border_and_Shadow():
    tab_border = id('border_tab')
    tab_shadow = id('shadow_tab')
    color_list = id('color_recycler_view')
    color_item = id('color_image_view')
    slider_area = id('slider_layout')
    border_size = id('size_slider')
    border_opacity = id('opacity_slider')
    shadow_blur = id('blur_slider')
    shadow_opacity = id('opacity_slider')
    shadow_angle = id('direction_slider')
    shadow_distance = id('distance_slider')
    slider = id('seekbar')
    btn_reset = id('btn_reset')


class Intro_Video:
    intro_video_entry = id('intro_video_entry')
    outro_video_entry = id('outro_video_entry')
    library_caption = id('top_toolbar_title')
    search_button = id('search_button')
    search_text = id('searchText')
    top_toolbar_tutorial = id('top_toolbar_tutorial')
    youtube_title = ('id', 'com.google.android.youtube:id/collapsed_title')
    top_toolbar_account = id('top_toolbar_account')
    profile_page = find_string('Posts')
    intro_category = id('library_category_tab_text')  # not unique
    intro_first_highlight = xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView')
    tab_cyberlink = id('cyberlink_switch')
    tab_discover = id('discover_switch')
    tab_search = id('search_switch')

    loading_icon = id('loading_progress')
    loading_designer = id('loading')
    top_toolbar_back = id('top_toolbar_back')
    list_category = id('category_recycler_view')
    list_template = id('template_recycler_view')
    top_toolbar_search = id('top_toolbar_search')
    template_thumbnail = id('video_template_thumbnail')  # not unique
    video_template_favorite_icon = id('video_template_favorite_icon')
    duration_text = id('duration_text')
    list_libraryEntry = id('libraryEntryList')
    btn_save_menu = id('btn_save_menu')

    # Save dialog
    btn_share = id('share_btn')
    btn_apply_to_timeline = id('apply_to_project_btn')
    btn_cancel = id('cancel_btn')

    # Share Page
    share_page_share = id('shareable_share')

    # Close confirm
    btn_leave = id('exit_btn')
    btn_no = id('no_btn')

    # Template info page
    btn_back = xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image')
    btn_fav = ('id', "\u5716\u5C64_1")
    preview = xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View')
    loading = xpath('//android.widget.ProgressBar')
    web_page_loading = id('web_view_loading')
    edit_in_intro = find_string('Customize')
    add_to_timeline = find_string('Add to Your Video')
    downloading = id('download_progress_bar')

    # Designer
    home = id('btn_home')
    libraryEntryList = id('libraryEntryList')

    # Trim page
    trim_play = id('playPauseBtn')

    # Added to timeline
    intro_master_clip = id("item_view_thumbnail_host")


class Interface:
    adjust_sub = Adjust_sub()
    audio_configuration = Audio_Configuration()
    audio_denoise = Audio_Denoise()
    aspect_ratio = AspectRatio
    backdrop = Backdrop()
    Blending_Sub = Blending_Sub()
    border_and_shadow = Border_and_Shadow()
    chroma_key = Chroma_Key()
    color_board = Color_Board()
    color_selector = Color_Selector()
    color_sub = Color_sub()
    crop = Crop()
    duration = Duration()
    edit_sub = Edit_sub()
    effect_sub = Effect_Sub()
    fade = Fade()
    fit_and_fill = Fit_And_Fill()
    background = Background
    hide_timeline_pannel = id('btnHideTimeLine')
    intro_video = Intro_Video()
    keyframe = Keyframe()
    Mask_Sub = Mask_Sub()
    menu = Menu()
    motion_graphic_title = Motion_Graphic_Title()
    music = Music()
    opacity = Opacity()
    pan_zoom_effect = Pan_Zoom_Effect()
    pip = Pip()
    pip_library = Pip()
    preview = Preview()
    replace = Replace()
    reverse = Reverse()
    reverse_video_window = Produce_Video_Window()
    settings = Settings()
    sharpness = Sharpness()
    show_timeline_pannel = id('btnShowTimeLine')
    speed = Speed()
    stabilizer = Stabilizer()
    stabilizer_correction = Stabilizer_Correction()
    stabilizing_video_window = Produce_Video_Window()
    sub_menu = SubMenu_Timeline_Setting()
    timeline = Timeline()
    tips = Tips()
    title_animation = Title_Animation()
    tool_menu = ToolMenu()
    sub_tool_menu = SubToolMenu
    transition = Transition()
    try_before_buy = Try_Before_Buy()
    tutorial_bubble = Tutorial_Bubble()
