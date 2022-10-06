from .locator_type import *

class Tab():
    gallery = id('produce_panel_movie')
    facebook = id('produce_panel_facebook')
    youtube = id('produce_panel_youtube')
    share = id('produce_panel_share')
    cloud = id('produce_panel_export')
    ig = id('produce_panel_instagram')
    tiktok = id('produce_panel_tiktok')
    
class Cloud():
    export = id('btn_produce')
    email = xpath('//*[@resource-id="id"]')
    pw = xpath('//*[@resource-id="pw"]')
    signin = xpath('//*[@resource-id="signinBt"]')
    signout = id('btn_sign_out')
    
class Produce_setting_page():
    class Setting_page():
        save_location = id('settings_save_location_value')
        bitrate = id('settings_bitrate_value')
        framerate = id('settings_frame_rate_value')
        better_quality = xpath('//*[@text="Better Quality"]')
        standard = xpath('//*[@text="Standard"]')
        smaller_size = xpath('//*[@text="Smaller Size"]')
        fps_24 = xpath('//*[@text="24 FPS(Film)"]')
        fps_30 = xpath('//*[@text="30 FPS"]')
        fps_60 = xpath('//*[@text="60 FPS"]')
        fps_25 = xpath('//*[@text="25 FPS"]')
        fps_50 = xpath('//*[@text="50 FPS"]')
        ok = id('btn_ok')
        cancel = id('btn_cancel')
    class Ad():
        close = aid('Interstitial close button')
        close_btn2 = xpath('//android.widget.ImageButton[@content-desc="Interstitial close button"]')
        open = xpath('//android.widget.Button[@resource-id="google-cta-button"]')
        no_thanks = xpath('//android.widget.Button[@resource-id="google-close-button"]')
        cancel = id('btnCancel')
    class Tooltip():
        show_next_time = id('help_enable_tip')
        ok = id('btn_ok')
    class Produce_page():
        progress_bar = id('progress_bar')
        file_name = id('progress_message')
        cancel = aid('[AID]ProjectProperties_Cancel')   # same item as open, different text
        open = aid('[AID]ProjectProperties_Cancel')     # same item as cancel, different text
        to_facebook = aid('[AID]ProjectProperties_Ok')
        share_video_to = ('id','android:id/title')
        btn_cancel = aid('[AID]ProjectProperties_Cancel')
        btn_back = aid('[AID]Produce_Back')
        ad_frame = id('native_ad_container')
        btn_play = id('btn_produce_preview')
        full_screen_preview = id('movie_view')
        save_to_camera_roll = id('btn_save_to_camera_roll')
        btn_file_location = id('btn_file_location')
        btn_share_to = aid('[AID]ProjectProperties_Ok')
        project_thumbnail = id('produce_loading_area')
        ig_share_menu = ('id', 'android:id/resolver_list')
    setting_page = Setting_page()
    ad = Ad()
    tooltip = Tooltip()
    produce_page = Produce_page()
    
    ultra_hd = id('produce_profile_2160p')  # enabled / displayed
    ultra_lock = id('uhd_lock')
    full_hd = id('produce_profile_1080p')
    fhd_lock = id('fhd_lock')
    hd = id('produce_profile_720p')
    sd = id('produce_profile_360p')
    setting = id('btn_settings')
    next = id('btn_next')
    btn_next = id('btn_next')
    rate_us = find_string('Not Now')
    btnPurchase = id('btnPurchase')
    btnCancel = id('btnCancel')
    file_name = id('edit_filename')
    fhd1080p = xpath('//*[@text="Full HD 1080p"]')
    hd720p = xpath('//*[@text="HD 720p"]')
    hd540p = xpath('//*[@text="HD 540p"]')
    sd360p = xpath('//*[@text="SD 360p"]')
    uhd_4k = xpath('//*[@text="Ultra HD (4K)"]')

#=======================================
class Interface():
    back = id('back_button')
    iap_back = aid('[AID]IAP_Back')
    tab = Tab()
    facebook = Produce_setting_page()
    gallery = Produce_setting_page()
    youtube = Produce_setting_page()
    cloud = Cloud()
    