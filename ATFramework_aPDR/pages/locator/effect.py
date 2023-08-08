from .locator_type import *


# ======================================================
class Menu():
    title = aid("[AID]FloatingMenu_Title")
    video = aid("[AID]FloatingMenu_Video")
    image = aid("[AID]FloatingMenu_Image")
    sticker = aid("[AID]FloatingMenu_Sticker")


# ======================================================
class SubMenu:
    add = id('library_unit_add')
    text = ("",)
    video = ("",)
    image = ("",)
    sticker = ("",)
    play = ("",)


class Title:

    add = id('library_unit_add')
    play = ("",)

    get_more = ("",)
    assembly_line = ("xpath", '(//*[contains(@resource-id,"library_unit_thumbnail")])[2]')
    clover_01 = ("",)
    default_with_fade = ("",)
    ending_credits_002 = ("",)
    flip = ("",)
    amplify_vertical = ("",)
    balloon = ("",)
    default = ("",)
    ending_credits_001 = ("",)
    fashion_glitter = ("",)
    flocking = ("",)


class Video():


    video_capture = ("",)
    google_drive = ("",)
    color_board = ("",)


class Image():


    photo_capture = ("",)
    google_drive = ("",)
    color_board = ("",)


class Sticker():


    get_more = ("",)
    like = ("",)
    road_trip = ("",)
    camera_focus = ("",)
    photoframe_05 = ("",)
    tropical_island = ("",)


# =========================================
class Font_face():
    rgb = ("accessibility id", "[AID]TextEdit_Color")
    saturation = ("accessibility id", "[AID]TextEdit_Pick")
    transparent = ("accessibility id", "[AID]TextEdit_Opcity_Pick")
    type = ("accessibility id", "[AID]Item_InputText")
    type_5th = ("xpath", '(//android.widget.TextView[@content-desc="[AID]Item_InputText"])[5]')


class Border():
    rgb = ("",)


class Shadow():
    rgb = ("",)


class Font():
    font_face = Font_face()
    border = Border()
    shadow = Shadow()


# ========================================
class Interface():
    sub_menu = SubMenu
    font = Font()
    menu = Menu()
    title = Title()
    video = Video()
    image = Image()
    sticker = Sticker()
