import requests
from bs4 import BeautifulSoup
import sys
from os.path import dirname as _dir
sys.path.insert(0, _dir(__file__))
import re
import shutil
import browser_cookie3
import os
import inspect
import json
import hashlib
from configparser import ConfigParser
import subprocess
from password import Password
import getpass


class Ecl_Operation():
    def __init__(self, para_dict): # prod_name, sr_no, tr_no, prog_path_sub, dest_path, work_dir (for password and tr_db file), mail_list(list), is_md5_check
        try:
            self.user_name = ''
            self.password = ''
            if 'prod_name' in para_dict.keys():
                self.prod_name = para_dict['prod_name']
            if 'sr_no' in para_dict.keys():
                self.sr_no = para_dict['sr_no']
            if 'tr_no' in para_dict.keys():
                self.tr_no = para_dict['tr_no']
            self.program_path_subfolder = ''
            if 'prog_path_sub' in para_dict.keys():
                self.program_path_subfolder = para_dict['prog_path_sub']
            if 'mail_list' in para_dict.keys():
                self.mail_list = para_dict['mail_list']
            self.dest_path = para_dict['dest_path']
            self.cookies = browser_cookie3.chrome(domain_name='.cyberlink.com')
            self.password_file = 'password'
            self.tr_db_file = 'tr_db'
            self.work_dir = os.path.dirname(__file__)
            if 'work_dir' in para_dict.keys():
                self.work_dir = para_dict['work_dir']
            if 'is_md5_check' in para_dict.keys():
                self.is_md5_check = para_dict['is_md5_check']
            else:
                self.is_md5_check = True
            self.err_msg = ''
            # decrypt the username/ password
            obj_password = Password(self.work_dir)
            passwd_list = obj_password.decryption_vigenere()
            self.user_name = passwd_list[0]
            self.password = passwd_list[1]
        except Exception as e:
            err_msg = f'Exception occurs. Incorrect format of parameter or missing keys. ErrorLog={e}'
            print(err_msg)
            self.err_msg = err_msg

    def _send_email(self):
        try:
            from sendemail import send_mail
            opts = {
                "account": "cyberlinkqamc@gmail.com"
                , "password": "qamc1234"
                , "from": "QAATServer <cyberlinkqamc@gmail.com>"
                , "to": self.mail_list
                , "subject": "[AT] Auto TR Build Download Module Error"
                , "text": "text_content"
                , "html": self.err_msg
                , "attachment": []
            }
            send_mail(opts)
        except Exception as e:
            print(f'Exception occurs. Error={e}')
            raise Exception
        return True

    def _get_tr_info(self,  html_cleantext, head, tail): # html_cleantext: from BeautifulSoup(r.text, "lxml").text
        print('Calling _get_tr_info')
        try:
            pattern = rf'(?<={head})(.*)(?={tail})'
            result = re.search(pattern, html_cleantext, re.DOTALL)
        except Exception as e:
            print(f'Exception occurs. Error={e}')
            raise Exception
        return result

    def _md5(self, filename):
        try:
            md5_object = hashlib.md5()
            block_size = 128 * md5_object.block_size
            a_file = open(filename, 'rb')

            chunk = a_file.read(block_size)
            while chunk:
                md5_object.update(chunk)
                chunk = a_file.read(block_size)

            md5_hash = md5_object.hexdigest()
            print(f'{md5_hash=}')
        except Exception as e:
            print(f'Exception occurs. ErrLog={e}')
            raise Exception
        return md5_hash

    def _md5_check_folder(self, path_folder):
        try:
            file_md5 = 'Cyberlink.MD5'
            if os.name == 'nt':
                path_md5 = '\\'.join([path_folder, file_md5]) # for windows
            else: # mac
                path_md5 = '/'.join([path_folder, file_md5])
            if not os.path.isfile(path_md5):
                print('No Cyberlink.MD5 file')
                return False

            config = ConfigParser()
            config.read(path_md5)
            section_name = 'Info'
            file_count = int(config[section_name]['Count'])
            # print(f'{file_count=}')
            list_keys = config.items(section_name)
            # print(f'{list_keys=}')
            file_count_pass = 0
            for index in range(len(list_keys)):
                if index == 0:
                    continue
                if os.name == 'nt':
                    file = ''.join([path_folder, list_keys[index][0]])
                else: # mac
                    sub_path = list_keys[index][0].replace('\\', '/')
                    file = ''.join([path_folder, sub_path])
                # print(file)
                if list_keys[index][1] == '':
                    file_count_pass += 1
                    continue
                if not os.path.isfile(file):
                    print(f'{file} doesn\'t exist.')
                    continue
                value = self._md5(file)
                if not value:
                    print(f'Generate MD5 checksum of {file}')
                    continue
                if value.upper() == list_keys[index][1]:
                    file_count_pass += 1
                else:
                    print(f'[_md5_check_folder] MD5 check FAIL. {file=}, MD5_expected={list_keys[index][1]}, MD5_check={value.upper()}')

            if not file_count_pass == file_count:
                err_msg = f'[_md5_check_folder] MD5 check is FAIL. Expected={file_count}, Passed={file_count_pass}, folder_path={path_folder}'
                print(err_msg)
                self.error_msg = err_msg
                return False
            print(f'MD5 check is Done. Expected={file_count}, Passed={file_count_pass}')
        except Exception:
            return False
        return True

    def retrieve_tr_info(self):
        print('Calling retrieve_tr_info')
        try:
            dict_result = {'ver_type': '', 'build': '', 'prog_path': ''}
            if self.tr_no != '':
                url = f'https://ecl.cyberlink.com/TR/TRHandle/HandleMainTR.asp?IsFromMail=true&TRCode={self.tr_no}'
                r = requests.get(url, auth=(self.user_name, self.password), cookies=self.cookies)
                cleantext = BeautifulSoup(r.text, "lxml").text
                # TR Info. - Program Path
                head = 'Program Path'
                tail = 'Built by'
                result = self._get_tr_info(cleantext, head, tail)
                dict_result['prog_path'] = result[0].replace('(ex: Q:\PoweDVD\):', '').strip()
                # TR Info. - Build
                head = 'Build:'
                tail = 'Software Environment'
                result = self._get_tr_info(cleantext, head, tail)
                if 'Stage:' in result[0]:
                    dict_result['build'] = result[0].split('Stage:')[0].strip()
                else:
                    dict_result['build'] = result[0].strip()
                # TR Info. - Version Type
                head = 'Version Type:'
                tail = 'Build:'
                result = self._get_tr_info(cleantext, head, tail)
                dict_result['ver_type'] = result[0].strip()
        except Exception as e:
            err_msg = f'[retrieve_tr_info]Exception Occurs. ErrroLog={e}, Please check the if can reach TR page correctly.'
            print(err_msg)
            self.err_msg = err_msg
            raise Exception
        return dict_result

    def update_tr_to_db(self, tr_no, sr_no):
        print('Calling update_tr_to_db')
        try:
            tr_list = []
            # initial build_db file
            db_file_path = self.tr_db_file
            if self.work_dir != '':
                if os.name == 'nt':
                    db_file_path = self.work_dir + '\\' + self.tr_db_file
                else: # mac
                    db_file_path = self.work_dir + '/' + self.tr_db_file
            if not os.path.isfile(db_file_path):
                f = open(db_file_path, 'w')
                f.close()
            tr_db = ConfigParser()
            tr_db.optionxform = str  # make key as case sensitive
            tr_db.read(db_file_path)
            # check section - sr_no
            try:
                value = tr_db[sr_no][tr_no]
            except:
                tr_list.append(tr_no)
                if not tr_db.has_section(sr_no):
                    tr_db.add_section(sr_no)
                tr_db.set(sr_no, tr_no, '1')
                tr_db.write(open(db_file_path, 'w'))
        except Exception as e:
            err_msg = f'[update_tr_to_db]Exception occurs. ErrorLog={e}'
            print(err_msg)
            self.err_msg = err_msg
            raise Exception
        return tr_list

    def query_latest_tr_by_sr(self): # prod_name, sr_no
        # return latest valid TR (non-canceled and reject)
        print('Calling query_latest_tr_by_sr')
        try:
            tr_no = ''
            # Query SR/TR list by http request
            prod_name = self.prod_name
            prod_ver = ''
            prod_ver_type = ''
            r = requests.get(
                f'https://ecl.cyberlink.com/WebService/BusinessService/ProductDevelopment/SR/SRService.asmx/QuerySRByProductName?ProdName={prod_name}&ProdVer={prod_ver}&ProdVerType={prod_ver_type}',
                auth=(self.user_name, self.password))
            result = r.text.split('org/">')
            result = result[1].replace('</string>', '')
            # parse json
            ojson = json.loads(result)
            # get TR list
            amount_sr = len(ojson["SRForm"])
            index_target = -1
            if amount_sr > 0:
                for index in range(amount_sr):
                    if self.sr_no == ojson['SRForm'][index]['SRF_no']:
                        index_target = index
                        break
                if index_target == -1:
                    err_msg = f'[query_latest_tr_by_sr] No SR_Num is matched. {prod_name=}'
                    print(err_msg)
                    self.err_msg = err_msg
                    raise Exception
                ojson_tr_list = ojson['SRForm'][index_target]['TRList']
            else:
                err_msg = f'[query_latest_tr_by_sr] NO SR List is found. {prod_name=}'
                print(err_msg)
                self.err_msg = err_msg
                raise Exception
            # get latest valid TR
            if len(ojson_tr_list) > 0:
                for item_tr in ojson_tr_list[::-1]: # list tr from end
                    if 'Assigned' in item_tr['Status'] or 'NewCreated' in item_tr['Status']:
                        if 'Cancel' not in item_tr['Status'] and 'Rejected' not in item_tr['Status']:
                            self.tr_no = item_tr['TRCode']
                            break
                if self.tr_no == '':
                    self.err_msg = '[query_latest_tr_by_sr] No not tested valid TR is found.'
                    return False
            else:
                err_msg = f'[query_latest_tr_by_sr] NO TR List is found. SR_No={self.sr_no}'
                print(err_msg)
                self.err_msg = err_msg
                return False
        except Exception:
            raise Exception
        return True

    def download_tr_build(self, src_path, dest_path, is_md5_check=True):
        print('Calling get_tr_info')
        mount_local_folder = ''
        mount_server_path = r'//CLT-QASERVER/Testing'
        network_path = r'\\clt-qaserver'
        curr_user = ''
        try:
            # [0] check current os type
            curr_os = 'windows'
            if os.name != 'nt':
                curr_os = 'mac'
                curr_user = getpass.getuser()
                mount_local_folder = rf'/Users/{curr_user}/Desktop/my_mount'

            # [1] - Grant permission of clt-qaserver
            if curr_os == 'windows':
                if not os.path.exists(src_path):
                    print('Current OS: Windows')
                    cmd = 'NET USE ' + network_path + ' /User:' + self.user_name + ' ' + self.password
                    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                    stdout, stderr = process.communicate()
                    exit_code = process.wait()
                    print(stdout, stderr, exit_code)  # success - exit_code=0
            else:  # for mac
                print('Current OS: Mac')
                if not os.path.exists(mount_local_folder):
                    os.mkdir(mount_local_folder)
                if not os.path.ismount(mount_local_folder):
                    print('mount the local folder')
                    self.user_name = self.user_name.replace('clt\\', '')
                    os.system(f"mount_smbfs //{self.user_name}:{self.password}@clt-qaserver/Testing ~/Desktop/my_mount")
                print(f'Folder {mount_local_folder} is mounted.')

            # [2] Download build to local
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            if curr_os == 'mac':
                src_path = src_path.replace('\\', '/')
                src_path = src_path.replace(mount_server_path, mount_local_folder)
                print(f'{src_path=}')
            shutil.copytree(src_path, dest_path)
            # do the MD5 check
            if is_md5_check:
                result = self._md5_check_folder(dest_path)
                if not result:
                    self.err_msg = '[download_tr_build] MD5 check fail.'
                    return False

            # [3] Remove the permission/ unmount the folder
            if curr_os == 'mac':
                # for mac, unmount the folder and remove
                os.system(f'diskutil unmount {mount_local_folder}')
                os.rmdir(mount_local_folder)
        except Exception as e:
            print(f'Exception occurs. ErrorLog={e}')
            if self.err_msg == '':
                self.err_msg = f'[download_tr_build] Exception occurs. ErrorLog={e}'
            return False
        return True


def get_latest_build(para_dict):
    print('enter get_latest_build func.')
    dict_result = {'result': True, 'error_log': '', 'ver_type': '', 'build': ''}
    oecl = ''
    try:
        # Initial object
        oecl = Ecl_Operation(para_dict)
        # print(f'user_name={oecl.user_name}, password={oecl.password}')
        # Query Latest TR by SR
        if oecl.tr_no == '':
            oecl.query_latest_tr_by_sr()
            # Check if TR is tested from db, if yes, skip it
            if oecl.tr_no != '':
                if len(oecl.update_tr_to_db(oecl.tr_no, oecl.sr_no)) == 0:
                    print('No new TR for testing.')
                    dict_result['result'] = False
                    dict_result['error_log'] = f'Latest TR {oecl.tr_no} is already tested'
                    return dict_result # query a tr but it's already tested
            else:
                dict_result['result'] = False
                dict_result['error_log'] = oecl.err_msg
                return dict_result # query no tr from sr
        # Retrieve TR Info.
        dict_tr_info = oecl.retrieve_tr_info()
        dict_result['ver_type'] = dict_tr_info['ver_type']
        dict_result['build'] = dict_tr_info['build']
        print(f'{dict_tr_info=}')
        # Download TR Build to Destination
        src_path = dict_tr_info['prog_path']
        if oecl.program_path_subfolder != '':
            src_path += '\\' + oecl.program_path_subfolder
        retry = 0
        result_download = False
        while retry < 3:
            if oecl.download_tr_build(src_path, oecl.dest_path, oecl.is_md5_check):
                result_download = True
                break
            retry += 1
        if not result_download:
            raise Exception
    except Exception as e:
        print(f'Exception occurs. ErrorLog={e}')
        dict_result['result'] = False
        dict_result['error_log'] = oecl.err_msg
        oecl._send_email()
    return dict_result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(f'parameter={sys.argv[1]}')
        print(f'type(sys.argv[1])={type(sys.argv[1])}')
        para_dict = eval(sys.argv[1])
        print(f'type(para_dict)={type(para_dict)}')
        result_dict = get_latest_build(para_dict)
        # output to return INI file
        print(f'{result_dict=}')
        conf = ConfigParser()
        cfgpath = '\\'.join([para_dict['work_dir'], 'result'])
        conf.add_section('RETURN')
        conf.set('RETURN', 'result', str(result_dict['result']))
        conf.set('RETURN', 'error_log', result_dict['error_log'])
        conf.set('RETURN', 'ver_type', result_dict['ver_type'])
        conf.set('RETURN', 'build', result_dict['build'])
        conf.write(open(cfgpath, "w"))
        sys.exit(0)
    else:
        print(f'Error parameter format. E.g. main.py str_in_dict_format. len(sys.argv[1])={len(sys.argv[1])}')
        sys.exit(1)