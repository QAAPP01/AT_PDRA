import os,re,glob
from os.path import exists
from os.path import basename
from os.path import dirname
from subprocess import getoutput
from subprocess import check_call
from .log import logger

howQ3_x86inx64 = 'C:\\Program Files (x86)\\CyberLink\\HowQ 3.0\\HowQ3.exe'
howQ3_x64 = 'C:\\Program Files\\CyberLink\\HowQ 3.0(x64)\\HowQ3_x64.exe'
howQ3_x86 = 'C:\\Program Files\\CyberLink\\HowQ 3.0\\HowQ3.exe'
temp = os.environ["temp"]


def compare_video(source,target):
    exist = lambda x,y,z : x if exists(x) else y if exists(y) else z if exists(z) else ""
    howQ3Path = exist(howQ3_x86inx64,howQ3_x64,howQ3_x86)
    fileName = basename(source)
    path = os.path.abspath(dirname(target))
    logName = '%s\\%s.info.txt'%(path,basename(target)) 

    
    if not howQ3Path:
        logger("[VerifyVideo] Can not find the HowQ3, please install in default path")
        return False
    if not exists(source):
        logger("[VerifyVideo] Sample file is not found. -> " + source)
        return False
    if not exists(target):
        logger("[VerifyVideo] Produced file is not found. -> " + target)
        return False
    
    params = ' /a evaluate /e autoclose /source "' + source + '" /output "' + target +'"'
    logger("[VerifyVideo] Runnning command: %s" % params)
    check_call('"%s" %s' % (howQ3Path,params), cwd=temp)
    
    with open(logName,"r") as f:
        file_data = f.read() 
    
    pattern = "Average PSNR=(-?\\d+\\.\\d*)[\\s\\S]*Average SSIM=(-?\\d+\\.\\d*)"
    result = re.search(pattern,file_data)
    PSNR ,SSIM = float(result.group(1)),float(result.group(2))
    
    logger("[VerifyVideo] PSNR: %s  SSIM: %s" % (PSNR,SSIM))

    if (PSNR > 40.0) & (SSIM > 0.9):
        logger("Video is the same.")
        logger("removing files")
        check_call(f'del "{os.path.abspath(logName)}"' , shell=True)
        check_call(f'del "{os.path.abspath(source)}"', shell=True)
        check_call(f'del "{path}\\*.csv"', shell=True)
        return True
    logger("Video is different.")
    return False
    

def compare_image(source,target):
    openCVTMPath = "c:\\ProgramData\\OpenCVTM\\OpenCVTM.exe"
    if not os.path.isfile(openCVTMPath):
        logger("[OpenCV] XXX OpenCVTM is not found. => {}" % openCVTMPath)
        exit(-1)
    output = getoutput("{} {} {}".format(openCVTMPath,source,target))
    result = re.search("\[(\\d*), (\\d*), (\\d*), (\\d*), (\\d*\\.\\d*)\]",output)
    if result:
        data = result.group(0)
        logger("[OpenCV] *** image is found: {!s}".format(data))
        return True
    else:
        logger("[OpenCV] --- image is not found: {!s}".format(output))
    return False

# a = r"D:\2011 Q1-2 video test files\MPEG-2\720p\inception-720p.mpg"
# b = r"D:\2011 Q1-2 video test files\MPEG-2\720p\beastly-720p.mpg"
# print (compare_video(a,b))

# a = r"C:\Users\Miti\Desktop\temp\Untitled.png"
# b = r"C:\Users\Miti\Desktop\temp\se.png"
# print (compare_video(a,b))