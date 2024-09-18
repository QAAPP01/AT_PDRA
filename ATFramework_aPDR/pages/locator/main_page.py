from .locator_type import *
new_project = id('layout_new_project')


class Launcher:
    new_project = id('layout_new_project')
    subscribe = id('layout_premium')
    ai_creation = id('layout_ai_creation')
    home = id('layout_home')

class AI_Creation:
    title = id('tv_project_title')
    entry = id('layout_ai_creation')

    @staticmethod
    def feature_name(index: int = 1):
        if index:
            return xpath(f'(//*[contains(@resource-id,"tv_title")])[{index}]')
        else:
            return xpath(f'//*[contains(@resource-id,"tv_title")]')


class Shortcut:
    demo_title = id('tv_title')
    demo_back = id('iv_back')
    demo_mute = id('btn_mute')
    try_it_now = id('tv_try_it_now')
    btn_continue = id('tv_continue')
    close = id('iv_close')
    editor_back = id('iv_close')
    play = id('btn_play')
    timecode = id('playing_time')
    total_time = id('total_time')
    playback_slider = id('seekbar')
    export = xpath(f'//*[contains(@resource-id,"tv_ok") and @text="Export"]')
    produce = id('btn_produce')
    full_editor = id('tv_full_editor')
    produce_progress_bar = id('progress_bar')
    produce_full_editor = id('btn_full_editor')
    save_to_camera_roll = id('btn_save_to_camera_roll')
    produce_back = aid('[AID]Produce_Back')
    produce_percentage = id('progress_percentage')
    save = id('btn_save')
    upgrade = id('btn_upgrade')
    produce_home = id('home_button')
    export_close = id("back_btn")
    save_image = id("save_image_btn")
    dont_show_again = id("dont_show_again_checkbox")
    crop = id('crop_button')
    crop_close = id('cancel_btn')
    crop_title = id("tv_title")

    @staticmethod
    def shortcut_name(param=1):
        if type(param) == str:
            return xpath(f'//*[contains(@resource-id,"tv_name") and @text="{param}"]')
        elif param:
            return xpath(f'(//*[contains(@resource-id,"tv_name")])[{param}]')
        else:
            return xpath(f'//*[contains(@resource-id,"tv_name")]')

    @staticmethod
    def item(index: int = 1):
        if index:
            return xpath(f'(//*[contains(@resource-id,"top_area")])[{index}]')
        else:
            return xpath(f'//*[contains(@resource-id,"top_area")]')

    class hsl:
        red = id('view_red')
        hue_slider = id('seek_bar_hue')
        hue_value = id('tv_hue')
        saturation_slider = id('seek_bar_saturation')
        saturation_value = id('tv_saturation')
        luminance_slider = id('seek_bar_luminance')
        luminance_value = id('tv_luminance')

    class body_effect:
        edit = id('itemEdit')
        cancel = id('btn_cancel')
        ok = id('btn_ok')
        dropper = id('dropper_button')
        color_picker = id('color_dropper_straw_view')
        apply = id('btn_apply_icon')
        reset = id('btn_reset')
        back = id('btn_back')

        @staticmethod
        def category(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"library_category_tab_text")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"library_category_tab_text")]')

        @staticmethod
        def effect(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"top_area")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"top_area")]')

        @staticmethod
        def effect_name(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemName")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemName")]')

        @staticmethod
        def favorite_icon(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemFavorite")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemFavorite")]')

        @staticmethod
        def color_preset(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"color_image_view")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"color_image_view")]')

        @staticmethod
        def slider(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"seekbar")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"seekbar")]')

        @staticmethod
        def value(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"value")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"value")]')

    class video_effect:
        edit = id('itemEdit')
        cancel = id('btn_cancel')
        ok = id('btn_ok')
        dropper = id('dropper_button')
        color_picker = id('color_dropper_straw_view')
        apply = id('btn_apply_icon')
        reset = id('btn_reset')
        back = id('btn_back')

        @staticmethod
        def category(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"library_category_tab_text")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"library_category_tab_text")]')

        @staticmethod
        def effect(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"top_area")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"top_area")]')

        @staticmethod
        def effect_name(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemName")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemName")]')

        @staticmethod
        def favorite_icon(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemFavorite")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemFavorite")]')

        @staticmethod
        def color_preset(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"color_image_view")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"color_image_view")]')

        @staticmethod
        def slider(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"seekbar")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"seekbar")]')

        @staticmethod
        def value(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"value")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"value")]')

    class cutout:
        @staticmethod
        def color(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"color")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"color")]')

    class anime_art:
        title = id('tv_title')
        back = id("top_toolbar_back")
        @staticmethod
        def template(index=1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"ai_template_card_view")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"ai_template_card_view")]')

    class voice_changer:
        mute = id('btn_mute')

    class audio_tool:
        info = id('info_icon')
        demo_speech_enhance = xpath('//*[@text="Speech Enhance"]')
        demo_ai_denoise = xpath('//*[@text="AI Denoise"]')

        strength_slider = id("strength_seekbar")
        compensation_slider = id("compensation_seekbar")
        @staticmethod
        def slider(index=1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"strength_seekbar")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"strength_seekbar")]')

    class tempo_effect:
        edit = id('itemEdit')
        edit_back = id('btn_back')
        spinner = id('spinner')
        reset = id('btn_reset')

        @staticmethod
        def effect(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"top_area")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"top_area")]')

        @staticmethod
        def effect_name(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemName")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemName")]')

        @staticmethod
        def premium_item(index=1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemPremium")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemPremium")]')

        @staticmethod
        def audio_source(index=1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"material_title_item_bg")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"material_title_item_bg")]')

        @staticmethod
        def slider(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"seekbar")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"seekbar")]')


    class tti:
        entry = id('tti_switch')
        title = id('tv_title')
        close = id('iv_close')
        prompt = id("tv_prompt")
        done = id("tv_done")
        clear = id('tv_clear')
        recommend = id('tv_tag')
        input_box = id('et_prompt')
        exceed_hint = id("tv_blocked_hint_exceeds_limit")
        sensitive = id('tv_blocked_hint_violation')
        generate = id('btn_generate')
        remove_watermark = id('remove_watermark')
        overwrite_cancel = id('cancel_button')
        overwrite_ok = id("ok_button")
        generate_ok = id('confirm_button')
        generate_cancel = id('cancel_button')
        editor_choice = id('cl_container')
        selected_style = xpath('//*[contains(@resource-id,"view_is_selected")]/../*[contains(@resource-id,"tv_name")]')
        style_scenery = id('tv_style_scenery')
        select = id('tv_select')
        generating = id('iv_progress')
        credit = id('tv_credit')
        generating_leave = id('btn_leave')
        generating_cancel = id('btn_cancel')

        @staticmethod
        def style(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"tv_name")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"tv_name")]')

        @staticmethod
        def preset(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"cv_sticker")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"cv_sticker")]')

        @staticmethod
        def generated_image(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"layout_normal")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"layout_normal")]')

    class photo_enhance:
        compare_thumb = id('iv_thumb')
        compare = id('btn_compare')

    class ai_art:
        generating = id('animated_image')
        prompt = id('editText')
        clear = id('btnDelete')
        apply = id('btnConfirm')
        custom_history = id('history_button')
        page_title = id('tv_title')
        close = id('iv_close')
        regenerate = id('itemRefresh')
        compare = id('tv_compare')
        compare_thumb = id('iv_thumb')
        history = id('history_button')
        close_history = id('back_btn')

        @staticmethod
        def history_image(index: int = 1):
            if index:
                return xpath(f'//android.widget.FrameLayout[3]/*/*/*/*/android.view.ViewGroup[{index}]')
            else:
                return xpath(f'//android.widget.FrameLayout[3]/*/*/*/*/android.view.ViewGroup')

        @staticmethod
        def history_prompt(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"tv_prompt")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"tv_prompt")]')

        @staticmethod
        def style_name(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemName")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemName")]')

    class ai_sketch:
        close = id('iv_close')
        continue_btn = id('tv_continue')
        dont_show_again = id('checkBox')
        crop = id('crop_button')
        title = id('tv_title')
        crop_close = id('cancel_btn')

        @staticmethod
        def style(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"materialCardView")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"materialCardView")]')

        @staticmethod
        def paid_style(index: int = 1):
            if index:
                return xpath(f'(//*[contains(@resource-id,"itemPremium")])[{index}]')
            else:
                return xpath(f'//*[contains(@resource-id,"itemPremium")]')





class Permission:
    gdpr_accept = id("gdpr_accept_button")
    loading_bar = id("splashWaitingProgress")
    file_ok = id("btn_remind_ok")
    photo_allow = installer_id("permission_allow_button")

class Created_project():
    edit = aid("[AID]SelectProject_Edit")


class Project:
    entry = xpath('//*[@text="Project"]')
    created = Created_project()
    empty = aid("[AID]Project_Create")
    select = id('project_item_border')
    new_project = id('layout_new_project')
    new_existed_created = id("btn_create_new_project")
    name = aid("[AID]Modify_ProjectName")
    btn_produced_videos = id("btn_produced_video")
    tutorials = id("btn_watch_tutorial")
    txt_project_title = id("item_title")
    btn_exit = id("btn_exit")
    shopping_cart = id("btn_shopping_cart")
    exit_toast = xpath('//android.widget.Toast')
    new_launcher_scroll = id("new_launcher_scrollview")
    btn_settings = id('btn_settings')
    ads = id('adMobUnifiedNativeAdView')
    header_exclusive_offer = id('header_exclusive_offer_for_you')
    # portrait_mode = id('portrait_mode')
    portrait_mode = id('radio_btn_portrait')
    # landscape_mode = id('landscape_mode')
    landscape_mode = id('radio_btn_landscape')
    autorotate_mode = id('radio_btn_auto')
    dont_ask_mode = id('dialog_checkbox')
    btn_ok = id('btn_remind_ok')
    dialog_ok = aid('[AID]ConfirmDialog_OK')

    ratio_16_9 = id('iv_project_16_9')
    ratio_9_16 = id('iv_project_9_16')
    ratio_1_1 = id('iv_project_1_1')
    ratio_21_9 = id('iv_project_21_9')
    ratio_4_5 = id('iv_project_4_5')

    @staticmethod
    def project_name(index=1):
        if index == 0:
            return xpath(f'//androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.TextView[contains(@resource-id,"tv_title")]')
        else:
            return xpath(f'(//androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.TextView[contains(@resource-id,"tv_title")])[{index}]')

class Project_Info():
    aspect_ratio = id("aspect_ratio_img")
    project_title = id("project_title")
    duration = id("item_duration")
    btn_edit_project = aid("[AID]SelectProject_Edit")
    btn_produce_video = aid("[AID]SelectProject_Produce")
    btn_save_as = id("btn_save_as_project")
    btn_delete_project = id("btn_delete_project")
    btn_back = aid('[AID]SelectProject_Back')


class AiEffect:
    ai_effect_entry = id("ai_template_entry")
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


class Menu:
    menu = id("iv_menu")
    back = id("iv_back")
    preference = id('btn_preference')
    display_file_name_switch = id('displayNameInMedia_switch')
    iap_banner = id("layout_premium")

class Tutorials():
    youtube_view = id('youtube_view')

    faq = xpath('//android.widget.TextView[contains(@text,"Frequently asked questions")]')
    trim_split = find_string('Trim & Split')
    # adjust_video_speed = find_string('Adjust Video Speed')
    stabilize_video = find_string('Stabilize Video')
    produce_video = find_string('Produce Video')
    apply_chroma_key = find_string('Apply Chroma Key')
    add_edit_title = find_string('Add & Edit a Title')
    adjust_video_speed = find_string('Adjust Video Speed')
    create_intro = find_string('Create Intro')
    download_music = find_string('Download Music')
    create_family_video = find_string('Create Family Video')
    record_voice_over = find_string('Record a Voice-over')
    add_custom_font = find_string('Add Custom Font')
    adjust_video_effect = find_string('Adjust Video Effects')
    extract_audio_from_video = find_string('Extract Audio from Video')
    create_manage_projects = find_string('Create & Manage Projects')
    add_pip_video = find_string('Add a PiP Video')
    expost_to_cyberlink_cloud = find_string('Export to CyberLink Cloud')
    pan_zoom_effect = find_string('Pan & Zoom (Ken Burns) Effect')
    shopping_cart = id("btn_shopping_cart")
    open_tutorial = id('fragment_open_tutorial')
    close_open_tutorial = id('cancel_button')

    
class Setting:

    default_image_duration = id("settings_default_image_duration")
    settings_default_video_quality = id('settings_default_video_quality')
    layout_premium = id('layout_premium')


class Subscribe:
    # v6.4-
    # one_month = id('subscribe_left_btn_layout')
    # three_month = id('subscribe_right_btn_layout')
    # one_year = id('subscribe_free_trial_btn_layout')
    # v6.5
    # one_month = id('subscribe_btn_left')
    # three_month = id('subscribe_btn_right')
    # one_year = id('free_trial')
    
    # new
    entry = id('layout_premium')
    iap_monthly = id('iap_radioBtn_monthly')
    iap_yearly = id('iap_radioBtn_yearly')
    continue_btn = id('continueBtn')
    password = xpath('//android.widget.EditText')
    verify = xpath('//android.widget.Button[@text="Verify"]')
    back_btn = aid('[AID]IAP_Back')
    feature_list = id('displayPool_weight_layout')
    feature_name = id('text_view')
    subscribe = xpath('//android.widget.Button[@text="Subscribe"]')
    highlight = id('highlight')
    complete = (None,)
    premium_tag = id('premium_features_used_bubble')
    premium_list = id("premium_list")
    iap_icon = id('iv_premium')



class CSE():
    login_entry = id('log_in_entry')
    login_page = id('loginPage')
    # email_field = xpath('//android.webkit.WebView[@content-desc="Cyberlink Member Login"]/android.view.View/android.view.View[2]/android.widget.EditText')
    # email_field = find_string('E-mail E-mail')
    email_field = xpath('//android.widget.EditText[@resource-id="id"]')
    # password_field = xpath('//android.webkit.WebView[@content-desc="Cyberlink Member Login"]/android.view.View/android.view.View[3]/android.widget.EditText')
    # password_field = find_string('Password Password')
    password_field = xpath('//android.widget.EditText[@resource-id="pw"]')
    btn_login = aid('Sign in')
    # btn_login = find_string('Log in')
    incorrect = find_string('The account or password is incorrect.')
    btn_logout = id('btnLogOut')
    login_back = aid('[AID]Log_In_Back')
    account_entry = id('cl_account_entry')
    btn_continue = aid('[AID]ConfirmDialog_OK')
    btn_cancel = aid('[AID]ConfirmDialog_Cancel')


class Sample_Projects():
    title = id('sample_project_list_title')
    list = id('sample_project_list_linear')
    project_thumbnail = id('thumbnail')
    project_video = id('video')
    project_title = id('title')


class Gamification():
    btn_entry = id('btn_quest_rewards_layout')
    tab_active = id('text_quest')
    tab_complete = id('text_history')
    scroller = id('scroller')
    quest_title = id('title')
    btn_claim = id('action')
    mission_description = id('description')
    text_countdown = id('action')
    no_cmoplete_text = find_string("You haven't completed any tasks yet. Get started now and claim your first reward.")
    produced_videos_progress = id('produced_videos_progress')
    produced_videos_progress_text = id('produced_videos_progress_text')
    class Claim_Dialog():
        description = id('reward_content')
        clock_img = id('reward_image')
        btn_use = id('use_it_button')
        title_not_complete = id('remind_title')
        btn_ok = id('ok_btn')
    claim_dialog = Claim_Dialog()
    btn_check_rewards = id('btn_check_rewards')
    btn_produce_page_claim = id('check_btn')
    check_in_later = id("later")

class Premium():
    btn_premium = id('btn_premium')
    dialog_title = id('dialog_title')
    iap_back = aid('[AID]IAP_Back')
    icon_tool_premium = id('tool_entry_premium')
    icon_library_lock = id('library_unit_lock')
    message = id('message')
    btn_remind_ok = id('btn_remind_ok')
    pdr_premium = id("header_pdr_premium")

#=======================================
class Interface:
    new_project = new_project
    ai_creation = AI_Creation
    shortcut = Shortcut
    permission = Permission()
    project = Project()
    project_info = Project_Info()
    launcher = Launcher
    menu = Menu()
    setting = Setting()
    tutorials = Tutorials()
    subscribe = Subscribe()
    cse = CSE()
    sample_projects = Sample_Projects()
    gamification = Gamification()
    premium = Premium()
    ai_effect = AiEffect
