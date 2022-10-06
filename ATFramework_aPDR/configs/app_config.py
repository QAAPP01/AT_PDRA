from SFT.conftest import PACKAGE_NAME
import os
root_path = os.path.dirname(os.path.dirname(__file__))


prod_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "noReset": "true",
    "autoLaunch": "false",
    "newCommandTimeout": "0",  # for installation
    'appPackage': PACKAGE_NAME,
    'appActivity': 'com.cyberlink.powerdirector.splash.SplashActivity',
    'NoSign' : True
}

prod_install_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "noReset": "true",
    "autoLaunch": "false",
    "newCommandTimeout": "600",  # for installation
    "app": root_path +r"\app\PowerDirector.apk"
}

prod_fullreset_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "noReset": "false",
    "fullReset": "true",
    "autoLaunch": "false",
    "newCommandTimeout": "600",  # for installation
    "app": root_path +r"\app\PowerDirector.apk"
}

prod_fastreset_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "noReset": "false",
    "fastReset": "true",
    "autoLaunch": "false",
    "newCommandTimeout": "600",  # for installation
    "app": root_path +r"\app\PowerDirector.apk"
}

OPPO_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "noReset": "true",
    "autoLaunch": "false",
    "newCommandTimeout": "600",  # for installation
    "app": root_path +r"\app\PowerDirector-DRA140225_01-6.0.0.68420.apk"
}

native_settings_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "noReset": "true",
    "autoLaunch": "false",
    "newCommandTimeout": "600",  # for installation
    'appPackage': 'com.android.settings'
}


# for install app cap  ,master session: safari(TBD)
native_cap = {
    "platformName": "iOS",
    "deviceName": "WorkiPhone",
    "udid": "e7bacca54da29caa9e3caf59a0672818f8ce0cff",
    "platformVersion": "11.2.6",
    "automationName": "XCUITest",
    "noReset": "true",
    "autoLaunch": "false",
    "newCommandTimeout": "600",  # for installation
    # "derivedDataPath": "~/Documents/DerivedData",
    "bundleId": "com.apple.mobilesafari",
    "webDriverAgentUrl": "http://192.168.2.120:8100"
}

# for trust app cap  ,master session: settings
trustapp_cap = {
    "platformName": "iOS",
    "deviceName": "WorkiPhone",
    "udid": "e7bacca54da29caa9e3caf59a0672818f8ce0cff",
    "platformVersion": "11.2.6",
    "automationName": "XCUITest",
    "noReset": "true",
    "autoLaunch": "false",
    # "derivedDataPath": "~/Documents/DerivedData",
    "app": "Settings",
    "webDriverAgentUrl": "http://192.168.2.120:8100"
}


# cap for already installed
launch_cap = {
    "platformName": "iOS",
    "deviceName": "WorkiPhone",
    "udid": "e7bacca54da29caa9e3caf59a0672818f8ce0cff",
    "platformVersion": "11.2.6",
    "automationName": "XCUITest",
    "app": "com.cyberlink.U-beta2",  # will be changed in function
    "noReset": "true",
    # "derivedDataPath": "~/Documents/DerivedData",
    "autoLaunch": "false"
}

# cap for already installed
launch_phd_cap = {
    "platformName": "iOS",
    "deviceName": "WorkiPhone",
    "udid": "e7bacca54da29caa9e3caf59a0672818f8ce0cff",
    "platformVersion": "11.2.6",
    "automationName": "XCUITest",
    "app": "com.cyberlink.photodirector",  # will be changed in function
    "noReset": True,
    # "derivedDataPath": "~/Documents/DerivedData",
    "autoLaunch": False,
    "derivedDataPath": '~/Downloads/xcode_temp_log',
    # "newCommandTimeout": 1800,   # for testing (avoid create another session while test-run)
    # "nativeWebTap": True,  # recommend not to use, affect the APPIUM efficience
    "webDriverAgentUrl": "http://192.168.2.120:8100"
}

# cap for 1st time to install
install_phd_cap = {
    "platformName": "iOS",
    "deviceName": "WorkiPhone",
    "udid": "e7bacca54da29caa9e3caf59a0672818f8ce0cff",
    "platformVersion": "11.2.6",
    "automationName": "XCUITest",
    "app": 'n/a',  # will be changed in function
    "noReset": True,
    # "derivedDataPath": "~/Documents/DerivedData",
    "autoLaunch": False,
    "derivedDataPath": '~/Downloads/xcode_temp_log',
    # "newCommandTimeout": 1800,   # for testing (avoid create another session while test-run)
    # "nativeWebTap": True,  # recommend not to use, affect the APPIUM efficience
    "webDriverAgentUrl": "http://192.168.2.120:8100"
}