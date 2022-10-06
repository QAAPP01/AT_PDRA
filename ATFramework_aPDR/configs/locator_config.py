from appium.webdriver.common.mobileby import MobileBy
import collections

locators = collections.defaultdict(list)
locators['tab_chats'].append((MobileBy.ACCESSIBILITY_ID, 'Chats'))
locators['tab_contacts'].append((MobileBy.ACCESSIBILITY_ID, 'Friends'))
print(locators)

# Sign in error msg
error_account = "The e-mail address or password is incorrect."
error_network = "The server or network is not currently available. Please try again later."
error_unknown = "Unknown error. Check your network connection and then try again."
error_email = "The e-mail address is invalid."
error_password = "The password needs to be at least 4 characters."

# Main page UI
tab_chats = (MobileBy.ACCESSIBILITY_ID, 'Chats')
tab_contacts = (MobileBy.ACCESSIBILITY_ID, 'Friends')
tab_meetings = (MobileBy.ACCESSIBILITY_ID, 'Meetings_And_Webinars')
tab_more = (MobileBy.ACCESSIBILITY_ID, 'More')
