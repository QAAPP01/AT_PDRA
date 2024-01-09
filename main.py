import platform
import os
import shutil
import subprocess
import sys

from multiprocessing import Process
import time

from ATFramework_aPDR.ATFramework.utils._ecl_operation import ecl_operation
from send_mail.send_report import send_report

# from ATFramework_aPDR.ATFramework.utils._ecl_operation.ecl_operation import Ecl_Operation
# import ecl_operation

# Local Mode Program
# Support Parallel Test on Local Mode (Windows/Android)

# [Configuration]
# ======================================================================================================================
# device_uudi - A list of the device uuid for testing, if no, program will arrange device(s) automatically
# parallel_device_count - the device number for parallel testing (default: 1)
# project_name - the target project for testing (e.g. aU, iPHD, aPDR)

deviceName = "R5CT32Q3WQN"
device_udid = [deviceName]  # A54
system_port_default = 8200  # for Android
parallel_device_count = 1
project_name = 'ATFramework_aPDR'
test_case_folder_name = 'SFT'
test_case_main_file = 'main.py'
report_list = []
package_name = 'com.cyberlink.powerdirector.DRA140225_01'


# [Auto Download parameters]
# auto_download = False
auto_download = False


sr_number = 'DRA231130-01'        # Please update build version info manually if didn't use auto download
tr_number = 'TR231218-017'
previous_tr_number = 'TR231208-045'  # Please update build version info manually
package_version = '13.1.0'        # Please update build version info manually if didn't use auto download
package_build_number = '1224180'  # Please update build version info manually if didn't use auto download


# [Report Mail Setting]
send = True
title_project = 'aPDR'
receiver = ["bally_hsu@cyberlink.com", "biaggi_li@cyberlink.com", "angol_huang@cyberlink.com", "hausen_lin@cyberlink.com", "AllenCW_Chen@cyberlink.com"]
# receiver = ['hausen_lin@cyberlink.com']

script_version = 'Testing'
# script_version = 'Debug'

# ======================================================================================================================

platform_type = platform.system()
print('Current OS:', platform_type)

# get connected devices udid
# if device_udid == []:
#     if platform_type == platform_type_windows:
#         obj_device = device_caps_android.DeviceCapability()
#         device_udid = obj_device.query_connected_device_list()
#     else:
#         obj_device = device_caps_ios.DeviceCapability()
#         device_udid = obj_device.query_connected_device_list()
#
# print('device=', device_udid)

# execute test
# def run_test(udid, system_port):


# generate path - test case, report
dir_path = os.path.dirname(os.path.realpath(__file__))
test_case_path = os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name))
app_path = os.path.normpath(os.path.join(dir_path, project_name, 'app'))
print('test_case_path=', test_case_path)


# execute
def __run_test(udid, system_port):
    start = 'pytest -s "%s" --color=yes --udid=%s --systemPort=%s' % (
    os.path.normpath(os.path.join(test_case_path, 'main.py')), udid, system_port)
    print(start)
    print('start to run test ---')
    try:
        os.system('color')
    except:
        pass
    stdout = os.popen(start).read()
    print(stdout)
    report_list.append(os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name,
                                                     'report/%s/%s' % (udid + '_' + tr_number, 'SFT_Report.html'))))


if __name__ == '__main__':
    procs = []
    deviceid_list = []

    # check version
    if sys.version_info < (3, 7):
        print("Please update Python to 3.7 +")
        sys.exit("Incorrect Python version.")

    # [auto download lasted build]
    if auto_download == True:
        sr_number = ''
        tr_number = ''
        previous_tr_number = ''
        package_version = ''
        package_build_number = ''

        # delete exist files in app folder
        for filename in os.listdir(app_path):
            file_path = os.path.join(app_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print('delete exist files in app folder...')
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        para_dict = {   'prod_name': 'PowerDirector Mobile for Android',
                        'sr_no': sr_number,
                        'tr_no': tr_number,
                        'prog_path_sub': '',
                        'dest_path': app_path,
                        'mail_list': receiver,
                        'is_md5_check': False}
        dict_result = ecl_operation.get_latest_build(para_dict)
        print(f'{dict_result=}')
        if not dict_result['build']:
            print(dict_result['error_log'])
            sys.exit(0)

        else:
            # [log tr info]
            tr_number = dict_result['tr_no']
            previous_tr_number = dict_result['prev_tr_no']

            version_numbers = dict_result['build'].split('.')
            package_version = version_numbers[0] + '.' + version_numbers[1] + '.' + version_numbers[2]
            package_build_number = version_numbers [3]
            print(f'package_version = {package_version}, package_build_number = {package_build_number}')

            with open('tr_info', 'w+') as file:
                file.write(f'tr_number={tr_number}\n')
                file.write(f'previous_tr_number={previous_tr_number}\n')
                file.write(f'package_version={package_version}\n')
                file.write(f'package_build_number={package_build_number}\n')

        # Rename apk
        fileExt = r".apk"
        new_name = os.path.join(app_path, 'PowerDirector.apk')
        for filename in os.listdir(app_path):
            if filename.endswith(fileExt):
                file_path = os.path.join(app_path, filename)
                os.rename(file_path, new_name)
                print('rename downloaded apk...')
                break

        # Install apk
        def install_apk(_apk_path, device_id=None):
            # 檢查目標資料夾是否存在，如果不存在，則創建它
            target_folder = os.path.dirname(_apk_path)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # 如果指定了設備ID，則添加“-s”選項
            adb_command = ["adb"]
            if device_id:
                adb_command.extend(["-s", device_id])

            # 添加安裝APK的命令
            adb_command.extend(["install", "-r", _apk_path])

            # 使用subprocess運行adb命令
            process = subprocess.Popen(adb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            # 檢查是否發生錯誤
            if process.returncode == 0:
                print(f"APK 安裝成功：{output.decode()}")
            else:
                print(f"APK 安裝失敗：{error.decode()}")


        def uninstall_apk(_package_name, device_id=None):
            # 如果指定了設備ID，則添加“-s”選項
            adb_command = ["adb"]
            if device_id:
                adb_command.extend(["-s", device_id])

            # 添加解除安裝APK的命令
            adb_command.extend(["uninstall", _package_name])

            # 使用subprocess運行adb命令
            process = subprocess.Popen(adb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            # 檢查是否發生錯誤
            if process.returncode == 0:
                print(f"APK 解除安裝成功：{output.decode()}")
            else:
                print(f"APK 解除安裝失敗：{error.decode()}")

        uninstall_apk(package_name, deviceName)
        install_apk(new_name, deviceName)

    # run test
    for device_idx in range(parallel_device_count):
        deviceid_list.append(device_udid[device_idx])
        cmd = ["%s" % device_udid[device_idx], "%s" % str(system_port_default + device_idx)]
        p = Process(target=__run_test, args=cmd)
        p.start()
        procs.append(p)
        print(report_list)

    for p in procs:
        p.join()
    print('test complete.')

    # [mail result]
    if send:
        send_report(title_project, deviceid_list, test_case_path, receiver, sr_number, tr_number, previous_tr_number,
                    package_version, package_build_number, script_version)
        print('send report complete.')
