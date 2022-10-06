
import os
from configparser import ConfigParser
from tkinter import *
import tkinter.messagebox

# from distutils.core import setup
# import PyInstaller
# setup (windows = ['password.exe'],
#        options = { 'PyInstaller' : {'packages':['Tkinter']}})

window = ''

class Password():
    def __init__(self, work_dir=''):
        self.key = 'testautomation'
        self.file_credential = 'credential'
        self.account = ''
        self.password = ''
        if work_dir != '':
            if os.name == 'nt':
                self.file_credential = work_dir + '\\' + self.file_credential
            else:
                self.file_credential = work_dir + '/' + self.file_credential

    def encryption_vigenere(self, account, pw):
        try:
            # encryption
            ascii_key = [ord(c) for c in self.key]
            ascii_password = [ord(c) for c in pw]
            len_key = len(ascii_key)
            for index in range(len(ascii_password)):
                ascii_password[index] = ascii_password[index] + ascii_key[index % len_key]

            if not os.path.exists(self.file_credential):
                fo = open(self.file_credential, 'w')
                fo.close()
            config = ConfigParser()
            config.optionxform = str  # reference: http://docs.python.org/library/configparser.html
            config.read(self.file_credential)
            section_name = 'CREDENTIAL'
            if not config.has_section(section_name):
                config.add_section(section_name)
            config.set(section_name, "ACCOUNT", account)
            config.set(section_name, "PASSWD", str(ascii_password))
            config.write(open(self.file_credential, 'w'))
        except Exception as e:
            print(f'Exception occurs. Error={e}')
            raise Exception
        return True

    def decryption_vigenere(self):
        result = []
        try:
            config = ConfigParser()
            config.read(self.file_credential)
            section_name = 'CREDENTIAL'
            account = config[section_name]['ACCOUNT']
            ascii_password = eval(config[section_name]['PASSWD'])

            # decryption
            ascii_key = [ord(c) for c in self.key]
            len_key = len(ascii_key)

            for index in range(len(ascii_password)):
                ascii_password[index] = ascii_password[index] - ascii_key[index % len_key]
            password = ''.join(map(chr, ascii_password))
            result.append(account)
            result.append(password)
            # print(f'{account=}, {password=}')
        except Exception as e:
            print(f'Exception occurs. Error={e}')
            raise Exception
        return result

    def gui_save(self):
        self.account = name.get()
        self.password = password.get()
        print(f'name={self.account}, password={self.password}')
        tkinter.messagebox.showinfo(title='Save', message='Complete')
        window.destroy()
        return True


if __name__ == '__main__':
    account = ''
    pw = ''
    obj_password = Password()
    # GUI
    window = Tk()
    window.title('Password')
    window.geometry('300x200')
    window.maxsize(300, 100)  # int
    window.resizable(0, 0)  # cannot resize

    label1 = Label(window, text='account: ')
    name = StringVar()
    password = StringVar()
    btn = Button(window, text='Save', command=obj_password.gui_save)
    nameEntry = Entry(window, textvariable=name)
    nameEntry.config(font=('Arial', 11))
    label2 = Label(window, text='password: ')
    passwordEntry = Entry(window, show='*', textvariable=password)
    passwordEntry.config(font=('Arial', 11))
    label1.grid(row=0, column=0)
    nameEntry.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    passwordEntry.grid(row=1, column=1)
    btn.place(x=250, y=60)
    window.mainloop()

    obj_password.encryption_vigenere(obj_password.account, obj_password.password)
    value = obj_password.decryption_vigenere()