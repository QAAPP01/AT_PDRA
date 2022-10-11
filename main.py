import platform
import os
import sys
from multiprocessing import Process

from send_mail.send_report import send_report

# Local Mode Program
# Support Parallel Test on Local Mode (Windows/Android)

# [Configuration]
# ======================================================================================================================
# device_uudi - A list of the device uuid for testing, if no, program will arrange device(s) automatically
# parallel_device_count - the device number for parallel testing (default: 1)


# [TR Setting]
package_version = '10.3.0'  # Please update build version info manually if didn't use auto download
package_build_number = '117684'  # Please update build version info manually if didn't use auto download
sr_number = 'DRA220601-01'  # Please update build version info manually if didn't use auto download
tr_number = 'TR220711-018'
previous_tr_number = 'TR220629-011'  # Please update build version info manually


# [Report Mail Setting]
send = False
title_project = 'aPDR'
# receiver = ["bally_hsu@cyberlink.com", "biaggi_li@cyberlink.com", "angol_huang@cyberlink.com",
#             "hausen_lin@cyberlink.com"]
receiver = ['hausen_lin@cyberlink.com']
# script_version = 'Testing'
script_version = 'Debug'


# [Device Setting]
deviceName = os.popen("adb devices").read().strip().split('\n')[1].split('\t')[0]  # Auto query connected device
device_udid = [deviceName]
system_port_default = 8200  # for Android
parallel_device_count = 1
project_name = 'ATFramework_aPDR'
test_case_folder_name = 'SFT'
test_case_main_file = 'main.py'
report_list = []
package_name = 'com.cyberlink.powerdirector.DRA140225_01'

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
    start = 'pytest -s "%s" --color=yes --udid=%s --systemPort=%s' % (os.path.normpath(os.path.join(test_case_path, 'main.py')), udid, system_port)
    print(start)
    print('start to run test ---')
    try:
        os.system('color')
    except:
        pass
    stdout = os.popen(start).read()
    print(stdout)
    report_list.append(os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name, 'report/%s/%s' % (udid + '_' + tr_number, 'SFT_Report.html'))))


if __name__ == '__main__':
    procs = []
    deviceid_list = []

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
