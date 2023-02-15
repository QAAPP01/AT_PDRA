from ATFramework_aPDR.SFT.conftest import PACKAGE_NAME

id = lambda id: ("id", PACKAGE_NAME + ":id/" + id)
installer_id = lambda id: ("id", "com.android.permissioncontroller:id/" + id)
aid = lambda id: ("accessibility id", id)
xpath = lambda id: ("xpath", id)
find_string = lambda id: ("xpath", '//*[contains(@text,"' + id + '")]')
class_name = lambda id: ("class name", id)
