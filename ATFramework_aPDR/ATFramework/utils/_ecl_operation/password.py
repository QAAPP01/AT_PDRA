import os
from configparser import ConfigParser
from tkinter import *
import tkinter.messagebox
import requests
import base64
import sys

try:
    from ..log import logger
except ImportError:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    from log import logger

class Authorization:
    def __init__(self, work_dir=''):
        self.key = 'testautomation'
        self.file_credential = 'credential'
        self.account = ''
        self.password = ''
        self.otp_code = ''
        self.work_dir = os.path.dirname(__file__) if not work_dir else work_dir
        self.file_credential = os.path.normpath(os.path.join(self.work_dir, self.file_credential))
        logger(f'file_credential = {self.file_credential}')

    def ensure_account_prefix(self, account):
        if not account.startswith('clt\\'):
            account = 'clt\\' + account
        return account

    def encryption_vigenere_clt_account(self, account, pw):
        try:
            account = self.ensure_account_prefix(account)
            ascii_key = [ord(c) for c in self.key]
            ascii_password = [ord(c) for c in pw]
            len_key = len(ascii_key)

            for index in range(len(ascii_password)):
                ascii_password[index] += ascii_key[index % len_key]

            config = ConfigParser()
            config.optionxform = str
            if not os.path.exists(self.file_credential):
                with open(self.file_credential, 'w'):
                    pass

            config.read(self.file_credential)
            section_name = 'CREDENTIAL'
            if not config.has_section(section_name):
                config.add_section(section_name)
            config.set(section_name, "ACCOUNT", account)
            config.set(section_name, "PASSWD", str(ascii_password))
            with open(self.file_credential, 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            logger(f'Exception occurs. Error={e}')
            raise
        return True

    def decryption_vigenere_clt_account(self):
        try:
            config = ConfigParser()
            config.read(self.file_credential)
            section_name = 'CREDENTIAL'
            account = config[section_name]['ACCOUNT']
            ascii_password = eval(config[section_name]['PASSWD'])

            ascii_key = [ord(c) for c in self.key]
            len_key = len(ascii_key)

            for index in range(len(ascii_password)):
                ascii_password[index] -= ascii_key[index % len_key]
            password = ''.join(map(chr, ascii_password))
            return [account, password]
        except Exception as e:
            logger(f'Exception occurs. Error={e}')
            raise

    def get_eclid_by_otp_code(self):
        try:
            url = f'https://ecl.cyberlink.com/ZFA/auth/OTOPVerify?U=https://cl-eportal.cyberlink.com&DC=ecl.cyberlink.com&C={self.otp_code}'
            r = requests.post(url, auth=(self.account, self.password))
            value = r.cookies["ECLID"]
            logger(f'ECLID={value}')
            return value
        except Exception as e:
            logger(f'Exception occurs. Error={e}')
            raise

    def create_eclid_file(self):
        try:
            if not self.otp_code:
                tkinter.messagebox.showwarning('Warning', 'Please provide OTP Code.')
                return False
            ecl_id = self.get_eclid_by_otp_code()
            file_name = os.path.normpath(os.path.join(self.work_dir, 'eclid'))
            with open(file_name, "wb") as f:
                encoded = base64.b64encode(ecl_id.encode('utf-8'))
                f.write(encoded)
            logger('create eclid file successfully')
        except Exception as e:
            logger(f'Exception occurs. Error={e}')
            raise
        return True

    def gui_save(self):
        self.account = self.ensure_account_prefix(name.get())
        self.password = password.get()
        self.otp_code = otp_code.get()
        tkinter.messagebox.showinfo(title='Save', message='Credentials saved successfully.')
        window.destroy()
        return True

if __name__ == '__main__':
    work_dir = sys.argv[1] if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else os.path.dirname(__file__)
    obj_authorization = Authorization(work_dir)

    # GUI
    window = Tk()
    window.title('Password + OTP code')
    window.geometry('300x150')
    window.resizable(0, 0)

    Label(window, text='Account: ').grid(row=0, column=0, padx=10, pady=5)
    name = StringVar()
    Entry(window, textvariable=name, font=('Arial', 11)).grid(row=0, column=1, padx=10, pady=5)

    Label(window, text='Password: ').grid(row=1, column=0, padx=10, pady=5)
    password = StringVar()
    Entry(window, show='*', textvariable=password, font=('Arial', 11)).grid(row=1, column=1, padx=10, pady=5)

    Label(window, text='OTP Code: ').grid(row=2, column=0, padx=10, pady=5)
    otp_code = StringVar()
    Entry(window, textvariable=otp_code, font=('Arial', 11)).grid(row=2, column=1, padx=10, pady=5)

    Button(window, text='Save', command=obj_authorization.gui_save).grid(row=3, column=1, padx=10, pady=10, sticky=E)

    window.mainloop()

    if obj_authorization.account and obj_authorization.password:
        obj_authorization.encryption_vigenere_clt_account(obj_authorization.account, obj_authorization.password)
        obj_authorization.create_eclid_file()
