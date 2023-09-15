import platform
import os
import sys
from glob import glob
import subprocess

from ATFramework_aPDR.ATFramework.utils.log import logger
from multiprocessing import Process

from send_mail.send_report import send_report

# Local Mode Program
# Support Parallel Test on Local Mode (Windows/Android)

# [Configuration]
# ======================================================================================================================
# device_uudi - A list of the device uuid for testing, if no, program will arrange device(s) automatically
# parallel_device_count - the device number for parallel testing (default: 1)

# [TR Setting]
tr_number = "TR230914-016"
previous_tr_number = "TR230911-018"  # Please update build version info manually
sr_number = 'DRA230607-01'  # Please update build version info manually if didn't use auto download

# [Device Setting]
# deviceName = os.popen("adb devices").read().strip().split('\n')[1].split('\t')[0]  # Auto query connected device
deviceName = "R5CT32Q3WQN"
# deviceName = "RFCW2198L7B"
device_udid = [deviceName]
system_port_default = 8200  # for Android
parallel_device_count = 1
project_name = 'ATFramework_aPDR'
test_case_folder_name = 'SFT'
test_case_main_file = 'main.py'
report_list = []

# [Auto Download The Newest Build]
auto_download = False
package_name = 'com.cyberlink.powerdirector.DRA140225_01'
try:
    package_version = os.popen(f'adb -s {deviceName} shell dumpsys package {package_name} | findstr  versionName').read().strip().split('=')[1]
except IndexError:
    package_version = os.popen(f'adb shell dumpsys package {package_name} | findstr  versionName').read().strip().split('=')[1]
try:
    package_build_number = os.popen(f'adb -s {deviceName} shell dumpsys package {package_name} | findstr  versionCode').read().strip().split('=')[1].split(' ')[0]
except IndexError:
    package_build_number = os.popen(f'adb shell dumpsys package {package_name} | findstr  versionCode').read().strip().split('=')[1].split(' ')[0]

# [Report Mail Setting]
send = True
title_project = 'aPDR'
receiver = ["bally_hsu@cyberlink.com", "biaggi_li@cyberlink.com", "angol_huang@cyberlink.com",
            "hausen_lin@cyberlink.com", "AllenCW_Chen@cyberlink.com"]
# receiver = ['hausen_lin@cyberlink.com']
script_version = 'Testing'
# script_version = 'Debug'

# ======================================================================================================================

platform_type = platform.system()
print('Current OS:', platform_type)

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
    package_version = \
    os.popen(f'adb -s {deviceName} shell dumpsys package {package_name} | findstr  versionName').read().strip().split('=')[
        1]
    package_build_number = \
    os.popen(f'adb -s {deviceName} shell dumpsys package {package_name} | findstr  versionCode').read().strip().split('=')[
        1].split(' ')[0]

    if auto_download:
        path = r'\\clt-qaserver\Testing\_RD_Build\PowerDirector_Android\PowerDirector*\PowerDirector*.apk'
        latest = 0
        for file in glob(path):
            string = file.split("\\")[7].split("-")[2].split(".apk")[0].split(".")
            apk_build = string[3]
            if int(apk_build) > latest:
                install = file
                latest = int(apk_build)
        if latest:
            logger(f'[Info] Newest Build {latest}')
            try:
                your_build = int(
                    os.popen(
                        f'adb -s {deviceName} shell dumpsys package {package_name} | findstr  versionCode').read().strip().split(
                        '=')[
                        1].split(' ')[0])
            except IndexError:
                your_build = 0
            if latest > your_build:
                if your_build:
                    if not subprocess.call(['adb', '-s', deviceName, 'shell', 'pm', 'uninstall', package_name],
                                           stdout=subprocess.DEVNULL,
                                           stderr=subprocess.STDOUT):
                        logger(f'[Info] Remove old build {your_build}')
                    else:
                        logger(f'[Info] Remove Fail')
                if not subprocess.call(['adb', '-s', deviceName, 'install', install], stdout=subprocess.DEVNULL,
                                       stderr=subprocess.STDOUT):
                    logger(f"[Info] Installed success!")
                else:
                    logger(f"[Info] Installed fail!")

                # Copy file
                build_path = f'storage/emulated/0/Build/PDR/'
                no_dir = subprocess.call(['adb', '-s', deviceName, 'shell', 'ls', build_path],
                                         stdout=subprocess.DEVNULL,
                                         stderr=subprocess.STDOUT)
                if no_dir:
                    subprocess.call(['adb', '-s', deviceName, 'shell', 'mkdir', build_path])

                apk_name = install.split("\\")
                apk_name = apk_name[len(apk_name) - 1]
                no_apk = subprocess.call(['adb', '-s', deviceName, 'shell', 'ls', os.path.join(build_path, apk_name)],
                                         stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

                if no_apk:
                    print('Start copying file...')
                    copy = subprocess.call(['adb', '-s', deviceName, 'push', install, build_path])
                    if not copy:
                        print(f'Copy apk to {build_path} completed！')
                    else:
                        print(f'Copy apk to {build_path} failed！')

            else:
                logger(f'[Info] Your build is newest {your_build}')
        else:
            logger('[Info] Cannot find apk from server')



    # check version
    if sys.version_info < (3, 7):
        print("Please update Python to 3.7 +")
        sys.exit("Incorrect Python version.")

    # run test
    for device_idx in range(parallel_device_count):
        deviceid_list.append(device_udid[device_idx])
        cmd = ("%s" % device_udid[device_idx], "%s" % str(system_port_default + device_idx))
        p = Process(target=__run_test, args=cmd)
        p.start()
        procs.append(p)
        print(report_list)

    for p in procs:
        p.join()
    print('test complete.')

    # mail result
    if send:
        send_report(title_project, deviceid_list, test_case_path, receiver, sr_number, tr_number, previous_tr_number,
                    package_version, package_build_number, script_version)
        print('send report complete.')
