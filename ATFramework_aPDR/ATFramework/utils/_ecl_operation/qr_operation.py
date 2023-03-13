import os
import sys
import time
import datetime
import base64

from selenium.webdriver import Chrome, Edge
from selenium.webdriver import ChromeOptions, EdgeOptions
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from .password import Authorization

try:
    from ..log import logger
except:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    print(os.path.dirname(SCRIPT_DIR))
    from log import logger


# locator of TR/QR website
option_report_type = ("xpath", "//select[@name='QRtmpid']")
btn_create = ("xpath", "//select[@name='QRtmpid']/following-sibling::input[@type='submit']")
btn_create_qr = ("xpath", "//input[@value='Create' and @class='BTN']")
txt_short = ("xpath", "//input[@name='ShortDescription']")
txt_build_day = ("xpath", "//td[contains(text(), 'Build Day')]//input[@type='text']")
txt_test_result = ("xpath", "//td[contains(text(), 'Test Result(Ex: OK, Fail, Find Major Bugs)')]//input[@type='text']")
txt_test_detail = ("xpath", "//textarea")
btn_add_file = ("xpath", "//a[@onclick='addFile()']")
btn_file = ("xpath", "//input[@type='File']")
btn_save = ("xpath", "//input[@type='Submit']")
link_qr_from_tr = ("xpath", "(//*[text()='QA Report: ']/parent::*/parent::*/parent::*/parent::*/parent::*/tr//a)[last()-1]")
link_qr_from_qr = ("xpath", "//a[contains(text(), 'QR')]")

debug_mode = False


class Qr_Operation():
    def __init__(self, para_dict): # prod_name, sr_no, tr_no, prog_path_sub, dest_path, work_dir (for password and tr_db file), mail_list(list)
        try:
            self.user_name = ''
            self.password = ''
            self.tr_no = ''
            if 'tr_no' in para_dict.keys():
                self.tr_no = para_dict['tr_no']
            self.qr_dict = {'short_description': 'AutoTest Report',
                            'build_day': datetime.date.today().strftime('%m%d'),
                            'test_result': 'AutoTest Report Result',
                            'test_result_details': 'AutoTest Report Result Detail',
                            'upload_files_1': '',
                            'upload_files_2': '',
                            'upload_files_3': '', }
            if 'qr_dict' in para_dict.keys():
                self.qr_dict = para_dict['qr_dict']
            self.work_dir = os.path.dirname(__file__)
            if 'work_dir' in para_dict.keys() and para_dict['work_dir']:
                self.work_dir = para_dict['work_dir']
            if debug_mode: print(f'Init - work_dir={self.work_dir}')
            self.webdriver_download_path = os.path.dirname(os.path.dirname(__file__))
            self.webdriver = self.set_webdriver(para_dict['browser'])
            self.cookies = {'domain': '.cyberlink.com', 'httpOnly': True, 'name': 'ECLID', 'path': '/', 'secure': True,
                            'value': self.read_eclid_file()}
            self.password_file = 'password'
            self.err_msg = ''
            # decrypt the username/ password
            obj_authorization = Authorization(self.work_dir)
            passwd_list = obj_authorization.decryption_vigenere_clt_account()
            self.user_name = passwd_list[0]
            self.password = passwd_list[1]
            # initial browser
            self.driver = Edge() if para_dict["browser"] == 'edge' else Chrome()
            self.driver.implicitly_wait(1)
            self.options = EdgeOptions if para_dict["browser"] == 'edge' else ChromeOptions()
            self.options.add_experimental_option("excludeSwitches", ['enable-automation', 'ignore-certificate-errors', 'enable-logging'])  # 新版本關閉“chrome正受到自動測試軟件的控製”信息
            self.options.add_argument("--no-first-run")
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--allow-insecure-localhost')
            self.options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        except Exception as e:
            err_msg = f'Exception occurs. Incorrect format of parameter or missing keys. ErrorLog={e}'
            logger(err_msg)
            self.err_msg = err_msg

    def set_webdriver(self, browser='chrome'):
        driver_path = os.path.join(self.webdriver_download_path, f'{browser}_driver')
        os.makedirs(driver_path, exist_ok=True)
        return chromedriver_autoinstaller.install(False, driver_path)

    def read_eclid_file(self):
        # file_name = 'eclid'
        file_name = os.path.normpath(os.path.join(self.work_dir, 'eclid'))
        logger(f'eclid file path={file_name}')
        if debug_mode: print(f'eclid file path={file_name}')
        ECL_ID = ''
        if not os.path.exists(file_name):
            if debug_mode: print('eclid file does not exist')
            logger('eclid file does not exist')
        else:
            # read ECLID from file
            if debug_mode: print('read eclid file')
            f = open(file_name, "rb")
            encoded = f.read()
            bytes_content = base64.b64decode(encoded)
            ECL_ID = bytes_content.decode('utf-8')
            logger('read eclid file successfully')
        if debug_mode: print(f'ECLID: {ECL_ID}')
        return ECL_ID

    def el(self, locator):
        if debug_mode: print(locator)
        return self.driver.find_element(*locator)

    def els(self, locator):
        if debug_mode: print(locator)
        return self.driver.find_elements(*locator)

    def is_el(self, locator):
        try:
            self.el(locator)
        except Exception as e:
            self.err_msg = e
            if debug_mode: print(e)
            return False
        return True

    def click(self, locator):
        try:
            self.el(locator).click()
        except Exception as e:
            self.err_msg = e
            if debug_mode: print(e)
            raise Exception
        return True

    def select_by_visible_text(self, locator, value):
        try:
            s = Select(self.el(locator))
            s.select_by_visible_text(value)
            return True
        except Exception as e:
            self.err_msg = e
            if debug_mode: print(e)
            return False

    def set_text(self, locator, text, clear_flag=True):
        try:
            text_area = self.el(locator)
            if clear_flag is True:
                try:
                    text_area.clear()
                except Exception as e:
                    self.err_msg = e
                    if debug_mode: print("ERROR: %s page cannot clear the text field: %s" % (self, locator))
                    raise Exception
            try:
                return text_area.send_keys(text)
            except Exception as e:
                self.err_msg = e
                if debug_mode: print("ERROR: %s page cannot set the text field: %s" % (self, locator))
                raise Exception
        except Exception as e:
            self.err_msg = e
            if debug_mode: print("ERROR: %s page cannot find the text field: %s" % (self, locator))
            raise Exception

    def add_file(self, locator, file_path):
        try:
            if not os.path.isfile(file_path):
                logger('File is missing')
                return False
            file_locator = self.el(locator)
            file_locator.send_keys(file_path)
            return True
        except Exception as e:
            self.err_msg = e
            if debug_mode: print(e)
            return False

    def select_qr_type(self, text='Standard Report'):
        return self.select_by_visible_text(option_report_type, text)

    def click_btn_create(self):
        return self.click(btn_create)

    def input_short_description(self, text):
        return self.set_text(txt_short, text)

    def input_build_day(self, text):
        if not self.is_el(txt_build_day):
            return False
        return self.set_text(txt_build_day, text)

    def input_test_result(self, text):
        return self.set_text(txt_test_result, text)

    def input_test_detail(self, text):
        return self.set_text(txt_test_detail, text)

    def input_file(self, index, file_path):
        locator_file = (btn_file[0], f'({btn_file[1]})[{index}]')
        return self.add_file(locator_file, file_path)

    def click_btn_save(self):
        return self.click(btn_save)

    def get_qr_link(self, from_qr=True, timeout=30):
        current_time = time.time()
        result = ''
        while current_time - time.time() < timeout:
            if from_qr:
                try:
                    link_locator = self.el(link_qr_from_qr)
                    result = link_locator.get_attribute("href")
                except:
                    pass
                if result:
                    break
                time.sleep(1)
            else:
                try:
                    link_locator_list = self.els(link_qr_from_qr)
                    result = link_locator_list[-2].get_attribute("href")
                except:
                    pass
                if result:
                    break
                time.sleep(1)
        return result

    def refresh_webpage(self):
        self.driver.refresh()
        result = True
        time.sleep(1)
        return result

    def close_browser(self):
        return self.driver.close()

    def qr_operation(self):
        try:
            self.user_name = self.user_name.replace('clt\\', '')
            url_authorize = f'https://{self.user_name}:{self.password}@ecl.cyberlink.com/TR/TRHandle/HandleMainTR.asp?IsFromMail=true&TRCode={self.tr_no}'
            url_tr = f'https://ecl.cyberlink.com/TR/TRHandle/HandleMainTR.asp?IsFromMail=true&TRCode={self.tr_no}'
            self.driver.get(url_authorize)
            self.driver.add_cookie(self.cookies)
            time.sleep(1)
            self.driver.get(url_tr)
            main_page = self.driver.current_window_handle
            time.sleep(2)
            self.select_qr_type('Standard Report')
            self.click_btn_create()
            time.sleep(5)
            browser_tabs = self.driver.window_handles
            self.driver.switch_to.window(browser_tabs[1])
            time.sleep(1)
            self.input_short_description(self.qr_dict['short_description'])
            self.input_build_day(self.qr_dict['build_day'])
            self.input_test_result(self.qr_dict['test_result'])
            self.input_test_detail(self.qr_dict['test_result_details'])
            if self.qr_dict.get('upload_files_1'):
                self.input_file(1, self.qr_dict['upload_files_1'])
            if self.qr_dict.get('upload_files_2'):
                self.input_file(2, self.qr_dict['upload_files_2'])
            if self.qr_dict.get('upload_files_3'):
                self.input_file(3, self.qr_dict['upload_files_3'])
            print(f'Save Report') if debug_mode else self.click_btn_save()
            time.sleep(30) if debug_mode else time.sleep(10)
            # self.driver.switch_to.window(main_page)
            # self.refresh_webpage()
            qr_link = self.get_qr_link(from_qr=True)
            return qr_link
        except Exception as e:
            self.err_msg = e
            logger(f'Exception occurs. ErrorLog={e}')


def create_qr(para_dict):
    dict_result = {'result': True, 'error_log': '', 'qr_link': ''}
    oqr = ''
    try:
        oqr = Qr_Operation(para_dict)
        dict_result['qr_link'] = oqr.qr_operation()
        oqr.close_browser()
        if not dict_result['qr_link']:
            dict_result['result'] = False
            dict_result['error_log'] = 'Get QR link failed'
    except Exception as e:
        oqr.err_msg = e
        dict_result['result'] = False
        dict_result['error_log'] = oqr.err_msg
    logger(f'{dict_result=}')
    return dict_result


if __name__ == '__main__':
    print('Start QR Creation')
    para_dict = {'browser': 'chrome',
                 'tr_no': 'TR221116-028',
                 'qr_dict': {'short_description': 'AutoTest Report 111',
                             'build_day': datetime.date.today().strftime('%m%d'),
                             'test_result': 'AutoTest Report Result 111',
                             'test_result_details': 'AutoTest Report Result Detail 111',
                             'upload_files_1': r"C:\Users\QAAT\Downloads\test1.txt",
                             'upload_files_2': r"C:\Users\QAAT\Downloads\test2.txt",
                             'upload_files_3': "", },
                 'work_dir': os.path.dirname(__file__),
                 }
    print(create_qr(para_dict))
