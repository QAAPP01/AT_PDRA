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
    # 'udid': 'R5CW31G76ST'
    'udid': '9596423546005V8'
    # 'udid': "R5CT32Q3WQN"
}
driver = webdriver.Remote('http://localhost:4727/wd/hub', desired_caps)

for i in range(0, 100):
    btn = driver.find_elements('id', 'com.cyberlink.powerdirector.DRA140225_01:id/btn_show_more')
    while btn[-1].get_attribute('enabled') == 'false':
        time.sleep(2)
    driver.find_elements('id', 'com.cyberlink.powerdirector.DRA140225_01:id/btn_show_more')[-1].click()
    print(len(btn)+1)
    time.sleep(3)