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
from send_mail.send_report import send_report

deviceName = "R5CT32Q3WQN"
# deviceName = "R5CW31G76ST"
device_udid = [deviceName]
system_port_default = 8200  # for Android
parallel_device_count = 1
project_name = 'ATFramework_aPDR'
test_case_folder_name = 'ServerScan'
test_case_main_file = 'main.py'
report_list = []
package_name = 'com.cyberlink.powerdirector.DRA140225_01'

# ======================================================================================================================
# [Configuration]
send = True
tr_number = ''

# [Report Mail Setting]
title_project = 'aPDR'
receiver = ["bally_hsu@cyberlink.com", "biaggi_li@cyberlink.com", "angol_huang@cyberlink.com", "hausen_lin@cyberlink.com", "AllenCW_Chen@cyberlink.com"]
# receiver = ['hausen_lin@cyberlink.com']

script_version = 'Testing'

# ======================================================================================================================

platform_type = platform.system()

# generate path - test case, report
dir_path = os.path.dirname(os.path.realpath(__file__))
test_case_path = os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name))
print(f'{test_case_path=}')


# execute
def __run_test(udid, system_port):
    start = 'pytest -s "%s" --color=yes --udid=%s --systemPort=%s' % (
        os.path.normpath(os.path.join(test_case_path, 'main.py')), udid, system_port)
    print('start to run test ---')
    try:
        os.system('color')
    except:
        pass
    stdout = os.popen(start).read()
    print(stdout)
    report_list.append(os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name,
                                                     'report/%s/%s' % (udid + '_' + tr_number, 'SFT_Report.html'))))


def auto_server_scan():

    print("\n ======== Server Scan Test Start ========")
    procs = []
    deviceid_list = []

    sr_number = ''
    with open('tr_info', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            if key == 'tr_number':
                tr_number = value
            elif key == 'previous_tr_number':
                previous_tr_number = value
            elif key == 'package_version':
                package_version = value
            elif key == 'package_build_number':
                package_build_number = value

    # run test
    print(f'Test Info: TR = {tr_number}, Prev_TR = {previous_tr_number}, Build = {package_version}.{package_build_number}')
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
        send_report(title_project, deviceid_list, test_case_path, receiver, sr_number, tr_number, previous_tr_number, package_version, package_build_number, script_version)
        print('send report complete.')

    print("\n ======== Server Scan Test Finish ========")
    print_next_run_time()


def print_next_run_time():
    next_run = schedule.next_run()
    print(f"\nNext execution time: {next_run}")


if __name__ == '__main__':
    auto_server_scan()
    schedule.every().day.at("00:00").do(auto_server_scan)

    while True:
        schedule.run_pending()
        sleep = int(schedule.idle_seconds())
        time_delta = datetime.timedelta(seconds=sleep)
        print(f"Sleeping for {time_delta} until the next scheduled run...")
        time.sleep(sleep)
