import os

deviceName = "R5CT32Q3WQN"
os.system(f"adb -s {deviceName} shell pm uninstall io.appium.settings")
os.system(f"adb -s {deviceName} shell pm uninstall io.appium.uiautomator2.server")
