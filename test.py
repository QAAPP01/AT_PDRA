import time
from appium import webdriver




desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'device',
    "appPackage": "com.cyberlink.powerdirector.DRA140225_01",
    'autoGrantPermissions': False,
    "noReset": True,
    "autoLaunch": False,
    "waitForIdleTimeout": 0,
    "newCommandTimeout": 60000,
    'udid': 'R5CW31G76ST'
    # 'udid': '9596423546005V8'
    # 'udid': "R5CT32Q3WQN"
}
driver = webdriver.Remote('http://localhost:4727/wd/hub', desired_caps)

