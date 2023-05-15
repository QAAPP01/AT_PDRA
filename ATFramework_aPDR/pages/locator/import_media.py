from .locator_type import *

class MediaLibrary:
    back = id("top_toolbar_back")
    back_landscape = id("library_menu_back")
    video_library = id("video_switch")
    photo_library = id("photo_switch")
    color_board = id("color_board_switch")
    search = id("searchText")
    waiting_cursor = id("waiting_cursor")  # waiting media refresh
    library_rooms = id('library_rooms')
    frame = id("pickerDeviceLibrary")
    library_recycler_gridview = id('library_recycler_gridview')
    first = ("xpath", '//*[contains(@resource-id,"select_view")][1]')
    last = ("xpath", '(//*[contains(@resource-id,"library_unit_thumbnail")])[last()]')
    first_caption = ("xpath", '//*[contains(@resource-id,"library_unit_caption")][1]')
    last_caption = ("xpath", '(//*[contains(@resource-id,"library_unit_caption")])[last()]')
    add = id("btn_add")
    apply = id('mediaPickerStoryboardOK')
    play = id("play")
    download = id('library_unit_download')  # for google drive
    cancel_download = id('library_unit_cancel')  # for google drive
    caption_media = id('library_unit_caption')
    # photo_capture = find_string('Photo Capture')
    photo_capture = id('btn_camera')
    # video_capture = find_string('Video Capture')
    video_capture = id('btn_camera')
    dialog_ok = aid('[AID]ConfirmDialog_OK')
    dialog_cancel = aid('[AID]ProjectProperties_Cancel')
    refresh = id('btn_refresh')
    first_duration = ("xpath", '//*[contains(@resource-id,"library_unit_duration")][1]')
    last_duration = ("xpath", '(//*[contains(@resource-id,"library_unit_duration")])[last()]')
    delete = id('top_delete')
    title_library_category_list = id('title_library_category_tab_list')
    template_library_category_list = id('overlay_library_category_tab_list')
    add_sticker = id('library_unit_frame')
    icon_try_sticker = id('library_unit_lock')
    btn_stock_filter = id('btn_sort_order')
    loading_circle = id('loading') # preview loading
    downloading = id("download_progress_bar")
    cancel = id("cancel_button")
    library_unit_sound_fx_icon = id('library_unit_sound_fx_icon')  # Sound Title
    library_unit_layout = id('library_unit_layout')
    library_tabs_content = id('library_tabs_content')
    creator_page = id("creatorWebsiteButton")
    next = id("mediaPickerClipSelectionOK")
    pexels_link = id("pexelsWebsiteBtn")
    pixabay_link = id("pixabayWebsiteBtn")
    sort_button = id("sort_button")


    @staticmethod
    def media(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"select_view")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"select_view")])[{index}]')

    @staticmethod
    def media_order(index=1):
        if index:
            return xpath(f'(//*[contains(@resource-id,"library_unit_order")])[{index}]')
        else:
            return xpath(f'//*[contains(@resource-id,"library_unit_order")]')

    @staticmethod
    def file_name(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"title_text")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"title_text")])[{index}]')

    @staticmethod
    def btn_preview(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"btn_preview")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"btn_preview")])[{index}]')

    @staticmethod
    def duration(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"duration_text")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"duration_text")])[{index}]')

    @staticmethod
    def orientation(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"ratio_image")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"ratio_image")])[{index}]')

    @staticmethod
    def stock(stock_name):
        stock = {"shutterstock": id('pickerShutter'),
                 "getty": id('pickerGetty'),
                 "getty_pro": id('pickerGettyPro'),
                 "giphy": id('pickerGIPHY'),
                 "pexels": id('pickerPexels'),
                 "pixabay": id('pickerPixabay'),
                 "google_drive": id('pickerGoogleDrive'),
                 }
        return stock[stock_name]

    @staticmethod
    def google_folder(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"library_unit_background")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"library_unit_background")])[{index}]')

    class Video:
        video_capture = id('btn_camera')
        start_recording = aid("Start recording")  # SS A53
        stop_recording = aid("Stop recording")  # SS A53
        camera_ok = aid("OK")  # SS A53
        shutter_stock = id('pickerShutter')
        getty = id('pickerGetty')
        getty_pro = id('pickerGettyPro')
        giphy = id('pickerGIPHY')
        pexels = id('pickerPexels')
        pixabay = id('pickerPixabay')
        display_preview = id('playerView')
        videoDisplay = id("videoDisplay")

    class Photo:
        photo_capture = id('btn_camera')
        take_picture = aid("Take picture")  # SS A53
        camera_ok = aid("OK")  # SS A53
        shutter_stock = id('pickerShutter')
        getty = id('pickerGetty')
        getty_pro = id('pickerGettyPro')
        pexels = id('pickerPexels')
        pixabay = id('pickerPixabay')
        display_preview = id('imageDisplay')


    video = Video
    photo = Photo


class Library_listview():
    # frame = id("library_listview")
    back = id("top_toolbar_back")
    frame = id("library_recycler_gridview")
    first = ("xpath", '//*[contains(@resource-id,"library_unit_thumbnail")][1]')
    last = ("xpath", '(//*[contains(@resource-id,"library_unit_thumbnail")])[last()]')
    first_caption = ("xpath", '//*[contains(@resource-id,"library_unit_caption")][1]')
    last_caption = ("xpath", '(//*[contains(@resource-id,"library_unit_caption")])[last()]')
    add = id("library_unit_add")
    play = id("play_icon")
    # play = aid("[AID]Libary_Play")
    stop = id('stop_icon')
    # stop = aid('[AID]Libary_Stop')
    frame_song = id('library_unit_background')  # for music server
    caption_song = id('library_unit_caption')  # for music server
    download_song = id('library_unit_download')  # for music server
    fav_icon = id('library_unit_favorite')


class Time_line():
    clip = ("xpath", '//android.widget.LinearLayout[contains(@content-desc,"[AID]TimeLineVideo_")]')
    clip_title = id("item_view_title")
    first_title = ("xpath", '//*[contains(@resource-id,"item_view_title")][1]')
    last_title = ("xpath", '(//*[contains(@resource-id,"item_view_title")])[last()]')
    last_photo = ("xpath", '(//*[contains(@resource-id,"item_view_thumbnail_host")])[last()]')


class Menu():
    # back = aid("[AID]Library_Back")
    # back = aid("[AID]TimeLine_Back")
    back = id("top_toolbar_back")
    # video_library = aid("[AID]Libary_Video")
    pip_video_library = id("library_menu_pip_video")
    # photo_library = aid("[AID]Library_Photo")
    video_library = id("video_switch")
    photo_library = id("photo_switch")
    pip_photo_library = id("library_menu_pip_photo")
    # music_library = aid("[AID]Library_Audio")
    music_library = id("library_menu_music")
    # close_and_play = aid("[AID]Library_CloseAndPlay")
    close_and_play = id("close_libraries_and_play")
    template_library = id('library_menu_template')
    add_as_intro = id('intro_text_view')
    add_as_outro = id('outro_text_view')
    add_as_premium_warning = id('header')
    # sticker_library = id('library_menu_sticker')
    sticker_library = id('library_menu_cms_sticker')
    overlay_library = id('library_menu_overlay')
    effect_layer_library = id('library_menu_fx_layer')
    sound_clips_library = id('library_menu_sound_clips')
    title_library = id('library_menu_title')

    @staticmethod
    def file_name(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"title_text")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"title_text")])[{index}]')


class SortMenu:
    sort_button = id("sort_button")
    by_name = id("by_name")
    by_date = id("by_date")
    by_duration = id("by_duration")
    by_resolution = id("by_resolution")
    by_file_size = id("by_file_size")
    ascending = id("order_asc")
    descending = id("order_des")
    best_match = aid('[AID]Sort_Best_Match')
    newest = aid('[AID]Sort_Newest')  # = Fresh content in SS
    random = aid('[AID]Sort_Random')  # = popular in SS
    most_popular = aid('[AID]Sort_Most_Popular')  # = random in SS
    by_all = aid('[AID]Filter_All')
    subscribed = aid('[AID]Filter_Subscribed')
    pay = aid('[AID]Filter_Pay')
    by_all_orientation = aid('[AID]Filter_All_Orientation')
    by_vertical = aid('[AID]Filter_Vertical')
    by_horizontal = aid('[AID]Filter_Horizontal')
    by_square = aid('[AID]Filter_Square')
    by_panoramic = aid('[AID]Filter_Panoramic_Horizontal')


class Video_Category():
    # txt_video_capture = xpath("//*[contains(@text,'Video Capture')]")
    txt_video_capture = id('btn_camera')


class Video_Library():
    select_folder = id('album_arrow')
    folders = id('album_text')  # not unique
    sort_menu = SortMenu
    # back = aid("[AID]Library_Back")
    # back = aid("[AID]TimeLine_Back")
    back = id("library_menu_back")
    sort = id("btn_sort")
    # close_and_play = aid("[AID]Library_CloseAndPlay")
    close_and_play = id("close_libraries_and_play")
    tab_stock = id('tab_video_stock')
    tab_pixabay = id('tab_video_pixabay')
    tab_video_shutterstock = id('tab_video_shutterstock')
    tab_video_gettyimages = id('tab_video_gettyimages')
    tab_video_gettyimages_premium = id('tab_video_gettyimages_premium')
    searchText = id('searchText')
    shutterstock_ToU_OK = aid('[AID]ConfirmDialog_OK')
    searchClear = id('searchClear')


class Photo_Library():
    select_folder = id('album_arrow')
    folders = id('album_text')  # not unique
    sort_menu = SortMenu
    # back = aid("[AID]Library_Back")
    # back = aid("[AID]TimeLine_Back")
    back = id("library_menu_back")
    sort = id("btn_sort")
    # close_and_play = aid("[AID]Library_CloseAndPlay")
    close_and_play = id("close_libraries_and_play")
    photo_capture_text = ("xpath", '(//*[contains(@text,"Photo Capture")])')


class Music_Library:
    local = id("tab_music_local")
    meta = id("tab_meta_sound")
    sort = id("action_sort")
    by_name = id("by_name")
    by_duration = id("by_duration")
    by_file_size = id("by_file_size")
    by_ascending = id("order_asc")
    by_descending = id("order_des")
    file_name = id("library_unit_caption")          # not unique
    file_duration = id("library_unit_duration")     # not unique
    add = id("library_unit_add")                    # not unique
    stop = id("stop_icon")
    favorite = id("library_unit_favorite")
    download = id("library_unit_download")
    downloading = id("progress_bar_download")
    # back = aid("[AID]Library_Back")
    # back = aid("[AID]TimeLine_Back")
    back = id("action_back")
    # close_and_play = aid("[AID]Library_CloseAndPlay")
    close_and_play = id("close_libraries_and_play")
    # iap_back = aid("[AID]Upgrade_No")
    iap_back = aid("[AID]IAP_Back")
    shutterstock_tab = id('tab_music_shutterstock')
    pdr_tab = id('tab_bgm_sound_clip')
    filter_all = aid('[AID]Filter_All')
    filter_genres = id("stock_music_tab_genres")
    filter_moods = aid('[AID]Filter_Moods')
    category_name = id("library_unit_caption")
    search = id("searchText")

    @staticmethod
    def clip(index=1):
        if index == 0:
            return xpath(f'//*[contains(@resource-id,"library_unit_caption")]')
        else:
            return xpath(f'(//*[contains(@resource-id,"library_unit_caption")])[{index}]')


class Music_Server_Library():
    # back = aid("[AID]Library_Back")
    # back = aid("[AID]TimeLine_Back")
    back = id("library_menu_back")
    tab_background_music = id('tab_bgm_sound_clip')
    tab_sound_clip = id('tab_dz_sound_clip')


class Transition_List():
    no_transition = id('no_tx_item')
    category_list = id('category_list')
    category_name = id('category_name')
    transition_list = id('transition_list')
    tx_name = id('effect_name')


class Device_limit():
    limit_message = id('message')
    btn_remind_ok = id('btn_remind_ok')


class GettyImages_Premium():
    library_unit_purchasable = id('library_unit_purchasable')
    library_unit_purchased_media = id('library_unit_purchased_media')
    btn_preview_first = aid('[AID]Upgrade_No')
    dont_show_again = id('set_default')
    learn_more = find_string('Learn More')

    class Buy_Dialog():
        premium_list = id('premium_list')
        pay_stock_media_thumbnail = id('pay_stock_media_thumbnail')
        pay_stock_media_original_price = id('pay_stock_media_original_price')
        pay_stock_media_price = id('pay_stock_media_price')
        pay_stock_media_footer = id('pay_stock_media_footer')  # for PowerDirector subscribers
        total_price = id('total_price')
        btn_notnow = aid('[AID]Upgrade_No')
        btn_buy = aid('[AID]Subscribe_Unlock_All')

    buy_dialog = Buy_Dialog()
    btn_googlepay_buy = xpath('//android.widget.Button[@text="1-tap buy"]')


class Interface:
    media_library = MediaLibrary()
    library_listview = Library_listview()
    video_category = Video_Category()
    video_library = Video_Library()
    photo_library = Photo_Library()
    music_library = Music_Library()
    menu = Menu()
    sort_menu = SortMenu
    timeline = Time_line()
    music_server_library = Music_Server_Library()
    transition_list = Transition_List()
    device_limit = Device_limit()
    gettyimages_premium = GettyImages_Premium()
