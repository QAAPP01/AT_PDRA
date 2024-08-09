import json
import sys

from .sendemail import send_mail
import os
import shutil
import datetime
from ATFramework_aPDR.ATFramework.utils._google_api.google_api import GoogleApi
from ATFramework_aPDR.ATFramework.utils._ecl_operation import qr_operation

def summary_report_header():
    summary_report_header = '<div class=WordSection1>'
    summary_report_header += '<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0 style=\'border-collapse:collapse;border:none\'>'
    summary_report_header += '<tr style=\'height:19.75pt\'>'
    summary_report_header += '<td width=89 style=\'width:67.1pt;border:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Name<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=96 style=\'width:1.0in;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Date<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=78 style=\'width:58.5pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Time<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=114 style=\'width:85.5pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Server<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=84 style=\'width:63.0pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>OS<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=162 style=\'width:121.5pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Device<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=102 style=\'width:76.5pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Version<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=60 style=\'width:45.0pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Pass<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=60 style=\'width:45.0pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Fail<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=60 style=\'width:45.0pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>N/A<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=66 style=\'width:49.5pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Skip<o:p></o:p></span></b></p></td>'
    summary_report_header += '<td width=150 style=\'width:112.5pt;border:solid windowtext 1.0pt;border-left:none;padding:0in 5.4pt 0in 5.4pt;height:19.75pt\'><p class=MsoNormal align=center style=\'text-align:center\'><b><span style=\'font-size:12.0pt;color:#1F497D\'>Total Time<o:p></o:p></span></b></p></td></tr>'
    return summary_report_header


def summary_report_add_row(col_name, col_date, col_time, col_server, col_os, col_device, col_ver, col_pass, col_fail, col_na, col_skip, col_total_time):
    row_content = '<tr style=\'height:26.5pt\'>'
    row_content += '<td width=89 style=\'width:67.1pt;border:solid windowtext 1.0pt;border-top:none;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_name)
    row_content += '<td width=96 style=\'width:1.0in;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_date)
    row_content += '<td width=78 style=\'width:58.5pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_time)
    row_content += '<td width=114 style=\'width:85.5pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_server)
    row_content += '<td width=84 style=\'width:63.0pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_os)
    row_content += '<td width=162 style=\'width:121.5pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_device)
    row_content += '<td width=102 style=\'width:76.5pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_ver)
    row_content += '<td width=60 style=\'width:45.0pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_pass)
    row_content += '<td width=60 style=\'width:45.0pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_fail)
    row_content += '<td width=60 style=\'width:45.0pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_na)
    row_content += '<td width=66 style=\'width:49.5pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_skip)
    row_content += '<td width=150 style=\'width:112.5pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:0in 5.4pt 0in 5.4pt;height:26.5pt\'><p class=MsoNormal align=center style=\'text-align:center\'><span style=\'font-size:12.0pt;color:#1F497D\'>{}<o:p></o:p></span></p></td>'.format(col_total_time)
    return row_content


def summary_report_tail():
    summary_report_tail = '</tr></table><p class=MsoNormal><span style=\'color:#1F497D\'><o:p>&nbsp;</o:p></span></p></div>'
    return summary_report_tail


def copy_rename(old_file_name, new_file_name, test_case_path, device_id):
    print(os.curdir)
    src_dir = os.path.join(test_case_path, "report/{}".format(device_id))
    #dst_dir = os.path.join(os.curdir, "dest")
    dst_dir = os.path.dirname(__file__)
    src_file = os.path.join(src_dir, old_file_name)
    dst_file = os.path.join(dst_dir, old_file_name)
    try:
        os.remove(dst_file)
    except OSError as e:
        print(e)
    shutil.copy(src_file, dst_dir)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)
    try:
        os.remove(new_dst_file_name)
    except OSError as e:
        print(e)
    os.rename(dst_file, new_dst_file_name)
    return True


def auto_create_qr(param_dict, att_list):
    cwd = os.getcwd()
    file_dict = {}
    for i in range(len(att_list)):
        file_dict[f"upload_files_{i+1}"] = os.path.join(cwd, att_list[i])
    param_dict["browser"] = "edge"
    param_dict["qr_dict"].update(file_dict)
    qr_operation.create_qr(param_dict)


def remove_attachment_file(att_list):
    dst_dir = os.path.dirname(__file__)
    for f in att_list:
        try:
            os.remove(os.path.join(dst_dir, f))
        except OSError as e:
            print(e)
        else:
            print("File {} is deleted successfully".format(os.path.join(dst_dir, f)))


def read_summary_to_dict(proj_path, device_id):
    src_file = os.path.join(proj_path, "report/{}/summary.txt".format(device_id))
    f = open(src_file, 'r')
    content = f.read()
    f.close()
    d = eval(content)
    return d


def send_report(test_result_title, udid_list, test_case_path, receiver_list, sr_number, tr_number, previous_tr_number, package_version, package_build_number, script_version):

    fail_count = 0
    pass_count = 0
    na_count = 0
    result = '[PASS]'

    opts = {'account': 'cltest.qaapp1@gmail.com', 'password': 'izjysnzxhygofgns',
    # opts = {'account': 'cyberlinkqamc@gmail.com', 'password': 'qamc-1234',
    # opts = {'account': 'cltqaappatreport@gmail.com', 'password': 'cyberlinkqa',
            'to': '', 'subject': '',
            'from': 'ATServer', 'text': 'txt_content', 'html': 'html_content',
            'attachment': []}
    html_report_header = '<html><head><meta http-equiv=""Content-Type"" content=""text/html; charset=ANSI""></head><body style=font-family:Calibri>'
    html_report_tail = '</body></html>'

    mail_body = html_report_header + summary_report_header()
    for device_id in udid_list:
        if os.path.isfile('{}/report/{}/SFT_Report.html'.format(test_case_path, device_id + '_' + tr_number)):
            #backup and rename
            copy_rename("SFT_Report.html", "SFT_Report_{}.html".format(device_id), test_case_path, device_id + '_' + tr_number)
            #add to attachment list
            opts['attachment'].append("SFT_Report_{}.html".format(device_id))

        if os.path.isfile('{}/report/{}_{}/SFT_Report_compare_{}_{}.html'.format(test_case_path, device_id, tr_number, previous_tr_number, tr_number)):
            compare_file_name = "SFT_Report_compare_" + previous_tr_number + "_" + tr_number
            copy_rename('{}.html'.format(compare_file_name), 'SFT_Report_compare.html', test_case_path, device_id+'_'+tr_number)
            opts['attachment'].append('SFT_Report_compare.html')

        if os.path.isfile('{}/report/{}/summary.txt'.format(test_case_path, device_id + '_' + tr_number)):
            summary_dict = read_summary_to_dict(test_case_path, device_id + '_' + tr_number)
            pass_count += int(summary_dict['pass'])
            fail_count += int(summary_dict['fail'])
            na_count += int(summary_dict['na'])
            mail_body += summary_report_add_row(summary_dict['title'], summary_dict['date'], summary_dict['time'], summary_dict['server'], summary_dict['os'], summary_dict['device'], summary_dict['version'], summary_dict['pass'], summary_dict['fail'], summary_dict['na'], summary_dict['skip'], summary_dict['duration'])
        else:
            return False
    mail_body += summary_report_tail() + html_report_tail
    if fail_count > 0:
        result = '[FAIL]'
    if pass_count == 0 and fail_count == 0:
        result = '[SKIP]'
    opts['subject'] = f'QAAPP_{summary_dict["title"]} Auto Testing Report'
    opts['subject'] += result
    opts['to'] = receiver_list
    opts['html'] = mail_body
    send_mail(opts)

    tr_dict = {"browser": "Edge",
               "tr_no": tr_number,
               "qr_dict": {'short_description': opts['subject'],
                           'build_day': datetime.date.today().strftime('%m%d'),
                           'test_result': f'{test_result_title} - {result} [PASS: {summary_dict["pass"]}, FAIL: {summary_dict["fail"]}]',
                           'test_result_details': f'Pass: {summary_dict["pass"]}\nFail: {summary_dict["fail"]}\nSkip: {summary_dict["skip"]}\nN/A: {summary_dict["na"]}\nTotal time: {summary_dict["duration"]}',
                          }
               }
    auto_report = True
    if auto_report:
        auto_create_qr(tr_dict, opts['attachment'])
    # remove attachment files
    remove_attachment_file(opts['attachment'])
    print('compelte')
    
    # initial google_api object
    sheet_name = f"{summary_dict['title']}"
    #header = ['Date', 'Time', 'SR', 'Build_Ver', 'Build_No', 'Server', 'OS', 'Device', 'Version', 'Pass', 'Fail', 'Skip', 'N/A', 'Total time']
    header_custom = ['Pass', 'Fail', 'Skip', 'N/A', 'Total time']
    obj_google_api = GoogleApi(sheet_name, header_custom)
    # add new record
    new_record = {  'Date': summary_dict['date'], 
                    'Time': summary_dict['time'], 
                    'Script_Name': summary_dict['title'],
                    'Script_Ver': script_version,
                    'SR_No': sr_number, 
                    'TR_No': tr_number,
                    'Build_No': package_build_number,
                    'Prod_Ver': package_version,      
                    'Prod_Ver_Type': 'Prod',
                    'OS': summary_dict['os'],  
                    'OS_Ver': summary_dict['version'],
                    'Device_ID': summary_dict['device'] }
    obj_google_api.add_new_record(new_record)
    #print(f'current row={obj_google_api.row_prev_record}')

    # update columns of previous record
    data = {'Pass': summary_dict['pass'], 'Fail': summary_dict['fail'], 'Skip':  summary_dict['skip'], 'N/A': summary_dict['na'], 'Total time': summary_dict['duration']}
    obj_google_api.update_columns(data)
    #
    print(f'Done.')
    
    return True


def remove_allure_result(result_folder):
    if os.path.exists(result_folder):
        try:
            shutil.rmtree(result_folder)
            print(f"Successfully removed {result_folder}")
        except OSError as e:
            print(f"An error occurred while removing {result_folder}: {e}")
    else:
        print(f"Directory does not exist: {result_folder}")


def move_allure_history(result_folder, report_folder):
    history_path = os.path.join(report_folder, 'history')
    destination_path = os.path.join(result_folder, 'history')

    if os.path.exists(history_path):
        try:
            if os.path.exists(destination_path):
                print(f"Destination already exists: {destination_path}")
                shutil.rmtree(destination_path)
                print("Destination removed")
            shutil.move(history_path, destination_path)
            print(f"Successfully moved history from {history_path} to {destination_path}")
        except OSError as e:
            print(f"An error occurred while moving history: {e}")
    else:
        print(f"No history directory found at {history_path}")


def generate_allure_report(result_folder, report_folder):
    os.system(f'allure generate {result_folder} --clean -o {report_folder}')
    os.system(f'allure generate --single-file {result_folder} --clean -o {report_folder}-html')
    return True


def send_allure_report(report_folder, test_result_title, device_id, receiver_list, tr_number, package_version, package_build_number, sr_number=None):

    opts = {'account': 'cltest.qaapp1@gmail.com', 'password': 'izjysnzxhygofgns',
            'to': '', 'subject': '',
            'from': 'ATServer', 'text': 'txt_content', 'html': 'html_content',
            'attachment': []}

    with open('summary.json', 'r') as f:
        summary_info = json.load(f)

    if summary_info["failed"] > 0:
        result = '[FAIL]'
    elif summary_info["passed"] == 0 and summary_info["failed"] == 0:
        result = '[SKIP]'
    else:
        result = '[PASS]'

    html_report_header = '<html><head><meta http-equiv=""Content-Type"" content=""text/html; charset=ANSI""></head><body style=font-family:Calibri>'
    html_report_tail = '</body></html>'
    mail_body = html_report_header
    mail_body += f'<h1>{test_result_title} {result}</h1>'
    mail_body += f'<p>device: {device_id}</p>'
    mail_body += f'<p>TR: {tr_number}</p>'
    mail_body += f'<p>Build: {package_version}.{package_build_number}</p>'
    mail_body += f'<h2>Test Summary:</h2>'
    mail_body += f'<p>Total: {summary_info["num_collected"]}</p>'
    mail_body += f'<p>Passed: {summary_info["passed"]}</p>'
    mail_body += f'<p>Failed: {summary_info["failed"]}</p>'
    mail_body += f'<p>Errors: {summary_info["errors"]}</p>'
    mail_body += f'<p>Skipped: {summary_info["skipped"]}</p>'
    mail_body += f'<p>Duration: {summary_info["duration"]}</p>'
    mail_body += html_report_tail

    opts['attachment'].append(f'{report_folder}-html\\index.html')

    opts['subject'] = f'[PDRA AT] {test_result_title} - {package_version}.{package_build_number}'
    opts['subject'] += result
    opts['to'] = receiver_list
    opts['html'] = mail_body
    send_mail(opts)


    # Create QA Report
    auto_report = True
    if auto_report:
        fail_count = int(summary_info["failed"]) + int(summary_info["errors"])
        na_count = summary_info["num_collected"] - summary_info["passed"] - summary_info["failed"] - summary_info["skipped"] - summary_info["errors"]
        tr_dict = {"browser": "Edge",
                   "tr_no": tr_number,
                   "qr_dict": {'short_description': opts['subject'],
                               'build_day': datetime.date.today().strftime('%m%d'),
                               'test_result': f'{test_result_title} - {result} [PASS: {summary_info["passed"]}, FAIL: {fail_count}]',
                               'test_result_details': f'Pass: {summary_info["passed"]}\nFail: {fail_count}\nSkip: {summary_info["skipped"]}\nN/A: {na_count}\nTotal time: {summary_info["duration"]}',
                               }
                   }
        auto_create_qr(tr_dict, opts['attachment'])
        print('compelte')

        # Add to Google Sheet
        # initial google_api object
        sheet_name = f"aPDR_SFT"
        # header = ['Date', 'Time', 'SR', 'Build_Ver', 'Build_No', 'Server', 'OS', 'Device', 'Version', 'Pass', 'Fail', 'Skip', 'N/A', 'Total time']
        header_custom = ['Pass', 'Fail', 'Skip', 'N/A', 'Total time']
        obj_google_api = GoogleApi(sheet_name, header_custom)
        # add new record
        new_record = {'Date': datetime.date.today(),
                      'Time': datetime.datetime.now().strftime("%I:%M %p"),
                      'Script_Name': test_result_title,
                      'Script_Ver': "Testing",
                      'SR_No': sr_number,
                      'TR_No': tr_number,
                      'Build_No': package_build_number,
                      'Prod_Ver': package_version,
                      'Prod_Ver_Type': 'Prod',
                      'OS': 'Android',
                      'OS_Ver': "12",
                      'Device_ID': 'Samsung A53'}
        obj_google_api.add_new_record(new_record)
        # print(f'current row={obj_google_api.row_prev_record}')

        # update columns of previous record
        data = {'Pass': summary_info["passed"], 'Fail': fail_count, 'Skip': summary_info["skipped"],
                'N/A': na_count, 'Total time': summary_info["duration"]}
        obj_google_api.update_columns(data)
        #
        print(f'Done.')

    return True