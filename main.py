import platform
import os
import sys
#import device_caps_android
#import device_caps_ios
from multiprocessing import Process
import time

from send_mail.send_report import send_report
# from ATFramework_aPDR.ATFramework.utils._ecl_operation.ecl_operation import Ecl_Operation
# import ecl_operation

# Local Mode Program
# Support Parallel Test on Local Mode (Windows/Android)

# [Configuration]
# -----------------------------------------------------------
# device_uudi - it's a list to specified the device uuid for testing, if no, program will arrange device(s)
#               automatically
# parallel_device_count - the device number for parallel testing (default: 1)
# project_name - the target project for testing (e.g. aU, iPHD, aPDR)

#device_udid = ['ENU7N15B06006012'] # Samsung S6, S7:9886274c4131324644, Oppo:a886a7e6 P6: ENU7N15B09000259, 6P black: ENU7N15B06006012
# device_udid = ['ENU7N15B09000259'] # Samsung S6, S7:9886274c4131324644, Oppo:a886a7e6 P6: ENU7N15B09000259, 6P black: ENU7N15B06006012
deviceName = os.popen("adb devices").read().strip().split('\n')[1].split('\t')[0]
device_udid = [deviceName]  # Sony XZP
system_port_default = 8200 #for Android
parallel_device_count = 1
project_name = 'ATFramework_aPDR'
test_case_folder_name = 'SFT'
test_case_main_file = 'main.py'
platform_type_windows = 'Windows'
platform_type = platform_type_windows
report_list = []
package_name = 'com.cyberlink.powerdirector.DRA140225_01'
package_version = '10.3.0'              # Please update build version info manually if didn't use auto download
package_build_number = '117684'         # Please update build version info manually if didn't use auto download

# auto download paramenters
sr_number = 'DRA220601-01'             # Please update build version info manually if didn't use auto download
auto_download = False
#auto_download = True
tr_number = 'TR220711-018'
previous_tr_number = 'TR220629-011'              # Please update build version info manually

# mail report
title_project = 'aPDR'
# receiver_list = ["bally_hsu@cyberlink.com", "biaggi_li@cyberlink.com", "angol_huang@cyberlink.com", "Nicklous_Chen@cyberlink.com"]
receiver_list = ["hausen_lin@cyberlink.com"]

# script_version = 'Testing'
script_version = 'Debug'
# -----------------------------------------------------------

platform_type = platform.system()
print('Current OS:', platform_type)

#get connected devices udid
# if device_udid == []:
#     if platform_type == platform_type_windows:
#         obj_device = device_caps_android.DeviceCapability()
#         device_udid = obj_device.query_connected_device_list()
#     else:
#         obj_device = device_caps_ios.DeviceCapability()
#         device_udid = obj_device.query_connected_device_list()
#
# print('device=', device_udid)

#execute test
#def run_test(udid, system_port):


#generate path - test case, report
dir_path = os.path.dirname(os.path.realpath(__file__))
test_case_path = os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name))
app_path = os.path.normpath(os.path.join(dir_path, project_name, 'app'))
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
    report_list.append(os.path.normpath(os.path.join(dir_path, project_name, test_case_folder_name, 'report/%s/%s' % (udid+'_'+tr_number, 'SFT_Report.html'))))


if __name__ == '__main__':
    procs = []
    deviceid_list = []
    
    # check version
    if sys.version_info < (3,7):
        print ("Please update Python to 3.7 +")
        sys.exit("Incorrect Python version.")
    
    # auto download lasted build
    # if auto_download == True:
        
        # delete exist files in app folder
        # for filename in os.listdir(app_path):
        #     file_path = os.path.join(app_path, filename)
        #     try:
        #         if os.path.isfile(file_path) or os.path.islink(file_path):
        #             os.unlink(file_path)
        #         elif os.path.isdir(file_path):
        #             shutil.rmtree(file_path)
        #         print('delete exist files in app folder...')
        #     except Exception as e:
        #         print('Failed to delete %s. Reason: %s' % (file_path, e))
        #
        # para_dict = {   'prod_name': 'PowerDirector Mobile for Android',
        #                 'sr_no': sr_number,
        #                 'tr_no': tr_number,
        #                 'prog_path_sub': '',
        #                 'dest_path': app_path,
        #                 'mail_list': receiver_list,
        #                 'is_md5_check': False}
        # dict_result = ecl_operation.get_latest_build(para_dict)
        # print(f'{dict_result=}')
        # version_numbers = dict_result['build'].split('.')
        # package_version = version_numbers[0] + '.' + version_numbers[1] + '.' + version_numbers[2]
        # package_build_number = version_numbers [3]
        # print (f'package_version = {package_version}, package_build_number = {package_build_number}')
        #
        # fileExt = r".apk"
        # new_name = os.path.join(app_path, 'PowerDirector.apk')
        # for filename in os.listdir(app_path):
        #     if filename.endswith(fileExt):
        #         file_path = os.path.join(app_path, filename)
        #         os.rename(file_path, new_name)
        #         print('rename downloaded apk...')
    
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
    send_report(title_project, deviceid_list, test_case_path, receiver_list, sr_number, tr_number, previous_tr_number,package_version, package_build_number, script_version)
    print('send report complete.')
