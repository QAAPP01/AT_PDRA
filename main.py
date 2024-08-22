import platform
import os
import shutil
import subprocess
import sys
import datetime

from multiprocessing import Process
import schedule
import time

from ATFramework_aPDR.ATFramework.utils._ecl_operation import ecl_operation
from send_mail.send_report import generate_allure_report, remove_allure_result, move_allure_history, send_allure_report


# import ecl_operation

# Local Mode Program
# Support Parallel Test on Local Mode (Windows/Android)

# [Configuration]
# ======================================================================================================================
# device_uudi - A list of the device uuid for testing, if no, program will arrange device(s) automatically
# parallel_device_count - the device number for parallel testing (default: 1)
# project_name - the target project for testing (e.g. aU, iPHD, aPDR)

# deviceName = "R5CT32Q3WQN"
deviceName = "R5CW31G76ST"
# deviceName = "9596423546005V8"
device_udid = [deviceName]
system_port_default = 8200  # for Android
parallel_device_count = 1
project_name = 'ATFramework_aPDR'


test_case_main_file = 'main.py'
report_list = []
package_name = 'com.cyberlink.powerdirector.DRA140225_01'

# ======================================================================================================================
# [Configuration]
auto_download = False
send = False
test_apk_from_appPath = False

sr_number = 'DRA240110-04'  # for manual
manual_tr_number = 'TR240207-034'  # for manual


# [Report Mail Setting]
title_project = 'aPDR'
receiver = ["bally_hsu@cyberlink.com", "biaggi_li@cyberlink.com", "angol_huang@cyberlink.com", "hausen_lin@cyberlink.com", "AllenCW_Chen@cyberlink.com", "Amber_Mai@cyberlink.com"]
# receiver = ['hausen_lin@cyberlink.com', "biaggi_li@cyberlink.com"]

script_version = 'Testing'
# script_version = 'Debug'

# ======================================================================================================================

platform_type = platform.system()
print('Current OS:', platform_type)

# generate path - test case, report
dir_path = os.path.dirname(os.path.realpath(__file__))
app_path = os.path.normpath(os.path.join(dir_path, project_name, 'app'))

# execute
def __run_test(_test_case_path, _test_result_folder_name, _udid, _system_port, _test_file_name="main.py"):
    start = 'pytest -s --alluredir %s "%s" --color=yes --udid=%s --systemPort=%s --clean-alluredir' % (_test_result_folder_name, os.path.normpath(os.path.join(_test_case_path, _test_file_name)), _udid, _system_port)
    print('Start to run test >>>\n')
    try:
        os.system('color')
    except:
        pass
    stdout = os.popen(start).read()
    print(stdout)


def auto_run():
    while True:
        print("\n ======== SFT Test Start ========")
        procs = []
        deviceid_list = []

        # check version
        if sys.version_info < (3, 7):
            print("Please update Python to 3.7 +")
            sys.exit("Incorrect Python version.")

        def rename_apk(name="PowerDirector.apk"):
            fileExt = r".apk"
            new_name = os.path.join(app_path, name)
            for filename in os.listdir(app_path):
                if filename.endswith(fileExt):
                    file_path = os.path.join(app_path, filename)
                    os.rename(file_path, new_name)
                    print('rename apk success!')
                    return new_name
            return False

        # Install apk
        def install_apk(_apk_path, device_id=None):
            if not os.path.exists(_apk_path):
                print("APK is not downloaded")
                return False

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
                return False

        def uninstall_apk(_package_name, device_id=None):
            try:
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
                    raise Exception(error.decode())
            except Exception as err:
                print(f"APK 解除安裝失敗：{err}")

        def delete_apk(_app_path):
            # delete exist files in app folder
            for filename in os.listdir(_app_path):
                file_path = os.path.join(_app_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    print('delete exist files in app folder...')
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))


        # [auto download lasted build]
        if auto_download:
            sr_number = ''
            tr_number = ''

            para_dict = {'prod_name': 'PowerDirector Mobile for Android',
                         'sr_no': sr_number,
                         'tr_no': tr_number,
                         'prog_path_sub': '',
                         'dest_path': app_path,
                         'mail_list': receiver,
                         'is_md5_check': False}
            dict_result = ecl_operation.get_untested_build(para_dict)
            print(f'{dict_result}')
            if not dict_result['build']:
                print(dict_result['error_log'])
                break

            else:
                # [log tr info]
                sr_number = dict_result['sr_no']
                tr_number = dict_result['tr_no']

                version_numbers = dict_result['build'].split('.')
                package_version = version_numbers[0].split('PowerDirector Mobile for Android: ')[1] + '.' + version_numbers[1] + '.' + version_numbers[2]
                package_build_number = version_numbers[3]
                print(f'package_version = {package_version}, package_build_number = {package_build_number}')

            apk = rename_apk()
            uninstall_apk(package_name, deviceName)
            install_apk(apk, deviceName)

        else:
            tr_number = manual_tr_number
            # Manual

            if test_apk_from_appPath:
                apk = rename_apk()
                if apk:
                    uninstall_apk(package_name, deviceName)
                    install_apk(apk, deviceName)
                else:
                    print("\nYou are in the non-auto-download mode")
                    print(f'**** Please put the apk file into {app_path}, or disable "test_apk_from_appPath"')
                    exit(1)

            def get_package_version(package_name, device_name):
                try:
                    version = os.popen(
                        f'adb -s {device_name} shell dumpsys package {package_name} | findstr  versionName').read().strip().split(
                        '=')[1]
                    build = os.popen(
                        f'adb -s {device_name} shell dumpsys package {package_name} | findstr  versionCode').read().strip().split(
                        '=')[1].split(' ')[0]
                    return version, build
                except Exception as e:
                    print(f"Error: {e}")
                    return "", ""

            package_version, package_build_number = get_package_version(package_name, deviceName)

        with open('tr_info', 'w+') as file:
            file.write(f'sr_number={sr_number}\n')
            file.write(f'tr_number={tr_number}\n')
            file.write(f'package_version={package_version}\n')
            file.write(f'package_build_number={package_build_number}\n')

        test_folder = 'SFT'
        test_result_title = 'SFT Test Result'
        result_folder = 'sft-allure-results'
        report_folder = 'sft-allure-report'
        test_case_path = os.path.normpath(os.path.join(dir_path, project_name, test_folder))

        # run test
        print(f'Test Info: TR = {tr_number}, Build = {package_version}.{package_build_number}')
        for device_idx in range(parallel_device_count):
            deviceid_list.append(device_udid[device_idx])
            cmd = ["%s" % test_case_path, "%s" % result_folder, "%s" % device_udid[device_idx], "%s" % str(system_port_default + device_idx)]
            p = Process(target=__run_test, args=cmd)
            p.start()
            procs.append(p)

        for p in procs:
            p.join()
        print('test complete.')

        move_allure_history(result_folder, report_folder)
        generate_allure_report(result_folder, report_folder)

        if send:
            send_allure_report(report_folder, test_result_title, deviceName, receiver, tr_number, package_version, package_build_number, sr_number)
            print('send report complete.')

        ecl_operation.manual_add_tr_to_db(sr_number, tr_number)
        delete_apk(app_path)

        print("\n ======== SFT Test Finish ========")


def auto_server_scan():
    print("\n ======== Server Scan Test Start ========")
    test_folder = 'ServerScan'
    test_result_title = 'Server Scan Test Result'
    result_folder = 'server-scan-allure-results'
    report_folder = 'server-scan-allure-report'
    test_case_path = os.path.normpath(os.path.join(dir_path, project_name, test_folder))

    remove_allure_result(result_folder)

    procs = []
    with open('tr_info', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            if key == 'tr_number':
                tr_number = value
            elif key == 'sr_number':
                sr_number = value
            elif key == 'package_version':
                package_version = value
            elif key == 'package_build_number':
                package_build_number = value

    # run test
    print(f'Test Info: TR = {tr_number}, Build = {package_version}.{package_build_number}')
    cmd = ["%s" % test_case_path, "%s" % result_folder, "%s" % deviceName, "%s" % str(system_port_default)]
    p = Process(target=__run_test, args=cmd)
    p.start()
    procs.append(p)

    for p in procs:
        p.join()
    print('test complete.')

    move_allure_history(result_folder, report_folder)
    generate_allure_report(result_folder, report_folder)

    if send:
        send_allure_report(report_folder, test_result_title, deviceName, receiver, tr_number, package_version, package_build_number, sr_number)
        print('send report complete.')

    print("\n ======== Server Scan Test Finish ========")
    auto_ai_style_scan()


def auto_ai_style_scan():
    print("\n ======== AI Style Scan Test Start ========")
    test_folder = 'ServerScan'
    test_result_title = 'AI Style Scan Test Result'
    result_folder = 'ai-style-scan-allure-results'
    report_folder = 'ai-style-scan-allure-report'
    test_case_path = os.path.normpath(os.path.join(dir_path, project_name, test_folder))

    remove_allure_result(result_folder)

    procs = []
    with open('tr_info', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            if key == 'tr_number':
                tr_number = value
            elif key == 'package_version':
                package_version = value
            elif key == 'package_build_number':
                package_build_number = value

    # run test
    print(f'Test Info: TR = {tr_number}, Build = {package_version}.{package_build_number}')
    cmd = ["%s" % test_case_path, "%s" % result_folder, "%s" % deviceName, "%s" % str(system_port_default), "main_scan_ai_style.py"]
    p = Process(target=__run_test, args=cmd)
    p.start()
    procs.append(p)

    for p in procs:
        p.join()
    print('test complete.')

    move_allure_history(result_folder, report_folder)
    generate_allure_report(result_folder, report_folder)

    if send:
        send_allure_report(report_folder, test_result_title, deviceName, receiver, tr_number, package_version, package_build_number)
        print('send report complete.')

    print("\n ======== AI Style Scan Test Finish ========")


def print_next_run_time():
    next_run = schedule.next_run()
    print(f"\nNext execution time: {next_run}")


if __name__ == '__main__':
    auto_run()

    schedule.every().monday.at("07:00").do(auto_run)
    schedule.every().monday.at("10:00").do(auto_run)
    schedule.every().monday.at("13:00").do(auto_run)
    schedule.every().monday.at("16:00").do(auto_run)
    schedule.every().monday.at("19:00").do(auto_run)

    schedule.every().tuesday.at("07:00").do(auto_run)
    schedule.every().tuesday.at("10:00").do(auto_run)
    schedule.every().tuesday.at("13:00").do(auto_run)
    schedule.every().tuesday.at("16:00").do(auto_run)
    schedule.every().tuesday.at("19:00").do(auto_run)

    schedule.every().wednesday.at("07:00").do(auto_run)
    schedule.every().wednesday.at("10:00").do(auto_run)
    schedule.every().wednesday.at("13:00").do(auto_run)
    schedule.every().wednesday.at("16:00").do(auto_run)
    schedule.every().wednesday.at("19:00").do(auto_run)

    schedule.every().thursday.at("07:00").do(auto_run)
    schedule.every().thursday.at("10:00").do(auto_run)
    schedule.every().thursday.at("13:00").do(auto_run)
    schedule.every().thursday.at("16:00").do(auto_run)
    schedule.every().thursday.at("19:00").do(auto_run)

    schedule.every().friday.at("07:00").do(auto_run)
    schedule.every().friday.at("10:00").do(auto_run)
    schedule.every().friday.at("13:00").do(auto_run)
    schedule.every().friday.at("16:00").do(auto_run)
    schedule.every().friday.at("19:00").do(auto_run)

    schedule.every().day.at("00:05").do(auto_server_scan)

    while True:
        schedule.run_pending()
        time.sleep(1)
        sleep = int(schedule.idle_seconds())
        time_delta = datetime.timedelta(seconds=sleep)
        print(f"Sleeping for {time_delta} until the next scheduled run...")
        print_next_run_time()
        if sleep < 0:
            sleep = 0
        time.sleep(sleep)
