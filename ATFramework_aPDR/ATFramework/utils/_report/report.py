import base64
import os
import subprocess
import re
import webbrowser
import datetime
import platform
import inspect
import time
from datetime import timedelta
# import main

from .sendemail import send_mail as sendMail
from ..log import logger

class MyReport(object):
    uuid_queue = set()

    def __init__(self, udid=None, driver=None, tr_number=None, previous_tr_number=None):
        self.tr_number = tr_number
        self.previous_tr_number = previous_tr_number
        self.driver = driver
        self.udid = udid or "unknown_device"
        self.set_path()

        self.previous_checklist_name = str(f"SFT_Report_compare_base_{self.previous_tr_number}.html")

        # report data
        self.body = self.read("body.rep")
        self.css = self.read("sheet.rep")
        self.js = self.read("script.rep")
        self.replace_bft = self.read("rep_bft.rep")
        self.replace_bft2 = self.read("rep_bft2.rep")

        self.bft = self.read_custom("SFT.html")
        if os.path.isfile(self.compare_orig):
            self.bft_compare = self.read_custom("SFT_compare.html")
        else:
            self.bft_compare = None
        if os.path.isfile(self.compare_base):
            self.bft_compare_result = self.read_custom(self.previous_checklist_name)
        else:
            self.bft_compare_result = None
        self.ov = self.read_custom("ov.rep")
        self.cssDownload = self.read_custom("sheet.css")

        self.start_time = time.time()

        self.fail_number = 0
        now = datetime.datetime.now()
        self.ovInfo = {
            "title" : "",
            "date" : now.date().strftime("%Y-%m-%d"),
            "time" : now.time().strftime("%H:%M:%S"),
            "server" : os.getenv('COMPUTERNAME', "Windows"),
            "os" : "driver.capabilities['os']",
            "device" : "driver.capabilities['device']",
            "version" : "driver.capabilities['version']",
            "pass" : 0,
            "fail" : 0,
            "na" : 0,
            "skip" : 0,
            "duration" : "00:00:00"
            }
        self.passNumber = 0
        self.failNumber = 0
        self.pic_index = 0
    def set_path(self):
        # data path
        self.source_path = os.path.dirname(inspect.stack()[2].filename)
        self.base_path = os.path.dirname(__file__)
        self.sub_folder = self.source_path + "/check_list/"
        # report path
        self.compare_orig = self.sub_folder+ "SFT_compare.html"
        self.compare_base = self.sub_folder + "/SFT_Report_compare_base_" + self.previous_tr_number + ".html"
        self.output_path = self.source_path + "/report/" + self.udid + "_" + self.tr_number
        self.output_file = self.output_path +"/SFT_Report.html"
        self.output_file_compare_base = self.sub_folder +"/SFT_Report_compare_base_" + self.tr_number + ".html"
        if os.path.isfile(self.output_file_compare_base):
            count = 1
            while os.path.isfile(self.output_file_compare_base):
                self.output_file_compare_base = self.sub_folder + "/SFT_Report_compare_base_" + self.tr_number + "_" + str(count) + ".html"
                count += 1
        self.output_file_compare = self.output_path +"/SFT_Report_compare_" + self.previous_tr_number + '_' + self.tr_number + ".html"
    def set_driver(self,driver):
        self.driver =driver.driver
    def set_udid(self,udid):
        self.udid = udid
        self.set_path()
    def start_uuid(self,uuid):
        # checking format
        pattern_uuid = r"(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})"
        if not re.match(pattern_uuid,uuid):
            logger("[Error] Input uuid is incorrect: %s" % str(uuid) )
            return
        if uuid in self.uuid_queue:
            logger(f"[Warning] Duplicate UUID found. {uuid}")
        self.uuid_queue.add(uuid)
    def add_result(self, id, result, name, log="",fail_screenshot= True):
        if fail_screenshot: # dont show log if call from export()
            logger("Add Result = %s / %s / %s / %s" % (id,result,name,log))
        #remove from uuid_queue
        if id not in self.uuid_queue:
            logger("[Warning] UUID is not in running list. Do you forget start_uuid(%s)?" % id)
        else:
            self.uuid_queue.remove(id)

        if result == False and self.driver and fail_screenshot: # only screenshot if result == false and has self.driver (set_driver())
            os.makedirs(self.source_path + "/report/" + self.udid + "_" + self.tr_number, exist_ok=True)
            self.pic_index += 1
            file_name = "%s_%s.png" % (str(self.pic_index), name)
            log = "%s / %s" % (file_name, log)
            logger(f'Fail screenshot = {file_name}')
            file_path = "%s/%s" % (self.output_path, file_name)
            self.driver.get_screenshot_as_file(file_path)

            time.sleep(5)
            raw_data = self.driver.stop_recording_screen()
            video_name = "%s_%s.mp4" % (str(self.pic_index), name)
            video_path = "%s/%s" % (self.output_path, video_name)
            with open(video_path, "wb") as vd:
                vd.write(base64.b64decode(raw_data))

        # print ("args=", id,result, name, log)
        myPass = '<span id="myPass">Pass</span>'
        myFail = '<span id="myFail">Fail</span>'
        myBypass = '<span id="myNA">N/A</span>'
        # self.bft = self.bft.replace("&lt;" + id + "&gt;", myPass if result else myFail,1)
        p = r'<td class="(s\d+)"([^>]*?)>([^<]*)<\/td><td class="(s\d+)"([^>]*?)>('+id+r')\W*?<\/td>\W*<td class="(s\d+)"([^>]*?)>([^<>]*)<\/td>\W*<td class="(s\d+)"><\/td>'
        self.bft = re.sub( p , \
            r'<td class="\1"\2>{0}</td><td class="\4"\5>{1}</td><td class="\7"\8>{2}</td><td class="\10"></td>' \
            .format(name,myPass if result else myFail if result == False else myBypass ,log),self.bft, 1)
            #(myPass if result else myFail)+r'<\/td><td class="\2">'+log+r'<\/td><td class="\4"><\/td>',self.bft,1)

        if result:
            self.ovInfo["pass"] += 1
        elif result == None:
            self.ovInfo['na'] += 1
        elif result == False:
            self.ovInfo["fail"] += 1
            logger(f'[Fail] ID = {id} , Screenshot = {fail_screenshot} , fail number = {self.ovInfo["fail"]}')

        if os.path.isfile(self.compare_base):
            p = r'<td class="(s\d+)"([^>]*?)>('+id+r')\W*?<\/td>\W*<td class="(s\d+)"([^>]*?)>([^<>]*)<\/td>\W*<td class="(s\d+)"><\/td>'
            self.bft_compare_result = re.sub(p, r'<td class="\1"\2>{0}</td><td class="\4"\5>{1}</td><td class="\7"></td>'.format(myPass if result else myFail if result==False else myBypass, log), self.bft_compare_result, 1)

        p = r'<td class="(s\d+)"([^>]*?)>([^<]*)<\/td><td class="(s\d+)"([^>]*?)>(' + id + r')\W*?<\/td>\W*<td class="(s\d+)"([^>]*?)>(' + id + r')\W*?<\/td>\W*<td class="(s\d+)"([^>]*?)>([^<>]*)<\/td>\W*<td class="(s\d+)"><\/td>'
        if os.path.isfile(self.compare_orig):
            self.bft_compare = re.sub(p, \
                r'<td class="\1"\2>{0}</td><td class="\4"\5>{1}</td><td class="\4"\5>{2}</td><td class="\7"\8></td><td class="\10"></td>' \
                .format(name, myPass if result else myFail if result==False else myBypass, id), self.bft_compare, 1)
        return self

    def new_result(self,id,result,fail_log=None,log="",fail_screenshot= True):
        fail_log = "Fail Log is not set." if not fail_log else fail_log
        name = os.path.basename(inspect.stack()[1].function).replace("test_","") # remove extra strings
        if not result:
            log = "%s %s" % (str(fail_log),log)
        self.add_result(id,result,name,log,fail_screenshot)
    def add_ovinfo(self, key, value = ""):
        if  type(key) is dict:
            for x,y in key.items():
                self.ovInfo[x] = y
        else:
            self.ovInfo[key] = value
        return self
    def export(self,output_file = None):
        report_elapsed_time = int(time.time() - self.start_time)
        if output_file:
            self.output_file = output_file
        def repl(matchObj=None):
            try:
                repl.count += 1
            except:
                repl.count = 1
            return '<span id="mySkip">Skip</span>'
        #exist uuid change result to fail
        for uuid in self.uuid_queue.copy():
            self.new_result(uuid,False,"Exception",fail_screenshot=False)
        # self.bft = re.sub("(&lt;\d+\.+\d+\.+\d+\.+\d+\.+\d+\.+\d+&gt;)",mySkip,self.bft)
        repl.count = 0  # it won't intial if no skip case
        skip_cases = re.findall(r"(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})", self.bft)
        self.bft = re.sub(r"(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})", repl, self.bft)

        # self.bft_compare = re.sub(r"(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})", repl, self.bft_compare)
        self.ovInfo["skip"] = repl.count
        self.ovInfo["duration"] = str(timedelta(seconds=report_elapsed_time))
        # output summary.txt
        # os.makedirs(self.source_path + "/report/" + self.udid, exist_ok=True)
        os.makedirs(self.output_path, exist_ok=True)
        with open(os.path.join(os.path.dirname(self.output_file), "summary.txt"), 'w') as data:
            data.write(str(self.ovInfo))
        if self.ovInfo["fail"]:
            self.fail_number = self.ovInfo["fail"]
            self.ovInfo["fail"] = '<font color="red"><b>{}</b></font>'.format(self.ovInfo["fail"])
        self.bft = self.bft.replace("</style>",self.replace_bft)
        self.bft = self.bft.replace('<table class="waffle"',self.replace_bft2)
        self.body = self.body.replace("this_is_bft",self.bft)       # switch tab style
        for x,y in self.ovInfo.items():
            self.ov = self.ov.replace("#" + x + "#", str(y))
        self.body = self.body.replace("this_is_overview",self.ov)   # switch tab style
        self.body = self.ov + self.bft                              # all in one style
        # self.css = self.css.replace("this_is_css",self.cssDownload) #merge to below write
        self.html_final = self.css.replace("this_is_css",self.cssDownload)+self.body+self.js
        with open(self.output_file,"w", encoding="utf-8") as f:
            f.write(self.html_final)

        if os.path.isfile(self.compare_base):
            self.bft_compare_result = re.sub(r"(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})", repl, self.bft_compare_result)
            self.bft_compare_result = self.bft_compare_result.replace("</style>",self.replace_bft)
            self.bft_compare_result = self.bft_compare_result.replace('<table class="waffle"',self.replace_bft2)
            self.body = self.body.replace("this_is_bft",self.bft)       # switch tab style
            for x,y in self.ovInfo.items():
                self.ov = self.ov.replace("#" + x + "#", str(y))
            self.body = self.body.replace("this_is_overview",self.ov)   # switch tab style
            self.body = self.ov + self.bft_compare_result               # all in one style
            # self.css = self.css.replace("this_is_css",self.cssDownload) #merge to below write
            self.html_final = self.css.replace("this_is_css",self.cssDownload)+self.body+self.js
            with open(self.output_file_compare,"w", encoding="utf-8") as f:
                f.write(self.html_final)
        else:
            logger('compare base checklist not exist, skip making compare list...')

        if os.path.isfile(self.compare_orig):
            for x in skip_cases:
                self.bft_compare = re.sub(x, repl, self.bft_compare, 1)
            self.bft_compare = self.bft_compare.replace("</style>", self.replace_bft)
            self.bft_compare = self.bft_compare.replace('<table class="waffle"', self.replace_bft2)
            self.body = self.body.replace("this_is_bft", self.bft_compare)       # switch tab style
            for x, y in self.ovInfo.items():
                self.ov = self.ov.replace("#" + x + "#", str(y))
            self.body = self.body.replace("this_is_overview", self.ov)   # switch tab style
            self.body = self.ov + self.bft_compare                              # all in one style
            # self.css = self.css.replace("this_is_css",self.cssDownload) #merge to below write
            self.html_final = self.css.replace("this_is_css", self.cssDownload)+self.body+self.js
            with open(self.output_file_compare_base, "w", encoding="utf-8") as f:
                f.write(self.html_final)

        return self

    def show(self):
        if platform.system() == "Windows":
            win_chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(win_chrome_path).open(self.output_file)
        elif platform.system() == "Darwin":
            # Not working
            # mac_chrome_path = '/Applications/Google\ Chrome.app %s'
            webbrowser.open('file://' + self.output_file)
        else:
            return self
        return self
    def read(self,filename):
        with open(self.base_path+"/"+filename,"r") as f:
            return f.read()
    def read_custom(self,filename):
        with open(self.source_path+"/check_list/"+filename, "r", encoding='utf-8', errors='ignore') as f:
            return f.read()
    def send_mail(self,acc,pw,displayName,emailTo):
        if not isinstance(emailTo, (list,tuple)):
            print ("emailTo should be dictionary.")
            return False
        result = "PASS" if self.ovInfo["fail"] == 0 else str(self.fail_number)+ " FAIL"
        opts = {
            "account": acc
            ,"password": pw #"6uWHKTZpUK6Fmgm"
            ,"from": displayName+" <clsignupstress@gmail.com>"
            ,"to": emailTo
            ,"subject": "[UWeb AT] Report <{}> {} {}".format(result,self.ovInfo["date"],self.ovInfo["time"])
            ,"text": "this is UWeb BFT report"
            ,"html": self.css+self.ov
            ,"attachment": self.html_final
        }
        sendMail(opts)

    def exception_screenshot(self,func):
        def wrapper(*aug):
            try:
                return func(*aug)
            except Exception as e:
                file_full_path = self.output_path + "/[Exception]" + func.__name__ + ".png"
                os.makedirs(self.source_path + "/report/" + self.udid + "_" + self.tr_number, exist_ok=True)
                self.driver.get_screenshot_as_file(file_full_path)

                time.sleep(5)
                raw_data = self.driver.stop_recording_screen()
                video_path = self.output_path + "/[Exception]" + func.__name__ + ".mp4"
                with open(video_path, "wb") as vd:
                    vd.write(base64.b64decode(raw_data))

                logger("Exception screenshot: %s" % file_full_path)
                logger("Exception recording: %s" % video_path)
                logger("Exception: %s" % str(e))
                raise
        return wrapper
