from main import package_name

id = lambda id: ("id", package_name + ":id/" + id)
installer_id = lambda id: ("id", "com.android.permissioncontroller:id/" + id)
aid = lambda id: ("accessibility id", id)
xpath = lambda id: ("xpath", id)
find_string = lambda id: ("xpath", '//*[contains(@text,"' + id + '")]')
class_name = lambda id: ("class name", id)
id_package = package_name + ":id/"
