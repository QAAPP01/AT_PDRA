import ecl_operation

# input dict. keys: prod_name, sr_no, tr_no, prog_path_sub, dest_path, work_dir, is_md5_check
# output dict. keys: result, err_msg, ver_type, build
para_dict = {'prod_name': 'PhotoDirector Mobile for Android', 'sr_no': 'PHA201130-01', 'tr_no': '', 'prog_path_sub': '', 'dest_path': 'D:\\test_build',
             'mail_list': ['jim_huang@cyberlink.com'], 'is_md5_check': True}
result = ecl_operation.get_latest_build(para_dict)
print(f'{result=}')
print('complete')