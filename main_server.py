
import platform
import os
import sys
#import device_caps_android
#import device_caps_ios
from multiprocessing import Process
import time
from send_mail.send_report import send_report

# Local Mode Program
# Support Parallel Test on Local Mode (Windows/Android)

# [Configuration]
# -----------------------------------------------------------
# device_uudi - it's a list to specified the device uuid for testing, if no, program will arrange device(s)
#               automatically
# parallel_device_count - the device number for parallel testing (default: 1)
# project_name - the target project for testing (e.g. aU, iPHD, aPDR)

#device_udid = ['ENU7N15B06006012'] # Samsung S6, S7:9886274c4131324644, Oppo:a886a7e6 P6: ENU7N15B09000259, 6P black: ENU7N15B06006012
#device_udid = ['ENU7N15B09000259'] # Samsung S6, S7:9886274c4131324644, Oppo:a886a7e6 P6: ENU7N15B09000259, 6P black: ENU7N15B06006012
device_udid = ['R58M93BNL2Y'] #A30
system_port_default = 8200 #for Android
parallel_device_count = 1
project_name = 'ATFramework_aPDR'
test_case_folder_name = 'ServerMonitoring'
test_case_main_file = 'main.py'
platform_type_windows = 'Windows'
platform_type = platform_type_windows
report_list = []
package_name = 'com.cyberlink.powerdirector.DRA140225_01'
# mail report
title_project = 'aPDR'

package_version = '10.2.2'
package_build_number = '116856'
sr_number = 'DRA220425-01'
tr_number = 'TR220623-008'
previous_tr_number = 'TR220623-008'
# script_version = 'Testing'
script_version = 'Debug'

receiver_list = [ "bally_hsu@cyberlink.com", "biaggi_li@cyberlink.com", "angol_huang@cyberlink.com", "nicklous_chen@cyberlink.com" ]

# -----------------------------------------------------------

platform_type = platform.system()
print('Current OS:', platform_type)


#generate path - test case, report
dir_path = os.path.dirname(os.path.realpath(__file__))
test_case_path = os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name))
print('test_case_path=', test_case_path)

#execute
def __run_test(udid, system_port):
    cmd = 'pytest -s "%s" --color=yes --udid=%s --systemPort=%s' % (os.path.normpath(os.path.join(test_case_path, 'main.py')), udid, system_port)
    print(cmd)
    print('start to run test ---')
    try:
        os.system('color')
    except:
        pass
    stdout = os.popen(cmd).read()
    print(stdout)
    report_list.append(os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name, 'report/%s/%s' % (udid, 'SFT_Report.html'))))


if __name__ == '__main__':
    procs = []
    deviceid_list = []
    
    # check version
    if sys.version_info < (3,7):
        print ("Please update Python to 3.7 +")
        sys.exit("Incorrect Python version.")
    
    #run test
    for device_idx in range(parallel_device_count):
        deviceid_list.append(device_udid[device_idx])
        cmd = ["%s" % device_udid[device_idx], "%s" % str(system_port_default+device_idx)]
        p = Process(target=__run_test, args=cmd)
        p.start()
        procs.append(p)
        print(report_list)

    for p in procs:
        p.join()
    print('test complete.')

    #mail result

    send_report(title_project, deviceid_list, test_case_path, receiver_list, sr_number, tr_number, previous_tr_number, package_version, package_build_number, script_version)
    print('send report complete.')