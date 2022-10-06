from .locator_type import *

#=======================================
class Ad():
    shopping_cart = id('btn_shopping_cart')
    x_button = aid('[AID]AdRemoveButton')
    frame = id('native_ad_container')
    frame_promote = id('cross_promotion')
    #frame_install_app = id('native_ad_call_to_action')
    frame_install_app = id('ad_container')
    frame_leave_app = id('leave_app_dialog_ad_container')
    frame_full_ad = xpath('/hierarchy/*[1]')
    frame_phd_promote = id('ad_container')
    watch_ad_to_unlock = id('btnOk')
    count_down = ('id', "count-down")
    progress_bar = id('progress_bar')
    dialog_title = id('dialog_title')
    countdown_close = ('id', 'countdown-close-container')
    close_btn = ('id', 'close-button-container')	
    close_btn3 = ('id', 'close-button-icon')	
    close_btn2 = xpath('//android.widget.ImageButton[@content-desc="Interstitial close button"]')
    continue_to_app_btn = ('id', 'close-button')
    exclusive_offer = id('header_exclusive_offer_for_you')
    iap_back_btn = aid('[AID]IAP_Back')