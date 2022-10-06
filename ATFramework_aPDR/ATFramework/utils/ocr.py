import os
import pytesseract
from PIL import Image
from .log import logger

# ==================================================================================================================
# Class: OCR
# Description: optical character recognize
# functions:
#   - analyze():
#      | analyze()    , ex: OCR(photo_path, 'CyberLink').analyze()
#   - get_count():
#      | get_count()    , ex: OCR(photo_path, 'Version').get_count()
#   - get_pos(index):
#      | get_pos(index)    , ex: OCR(photo_path, 'SR').get_pos(1)
# Note: n/a
# Author: Terence
# ==================================================================================================================
class OCR(object):
    # initial
    def __init__(self, target_img_path, target_text, default_conf=70):
        # make sure target_text is text
        if type(target_text) is str:
            self.img = target_img_path
            self.text = target_text
            self.default_conf = default_conf
            self.conf = None
            self.im = None
            self.data = None
            self.count = 0
            self.result_dict = {}
            self.pos = None
        else:
            logger(f"target text isn't string. {target_text}")

    # in order to analyze and create dictionary
    # return value: False or Dict. (ex: {1: (200, 500), 2: (100, 400)}
    def analyze(self):
        try:
            # determine if img exists
            for y in range(3):  # for file handle(avoid getting fail)
                if os.path.isfile(self.img):
                    break
                else:
                    if y == 2:
                        logger(f"Can't find target_img_path. ({self.img})")
                        return False
            # read file as img
            self.im = Image.open(self.img)

            # transfer as data, arguments: dict/string(default)/bytes
            self.data = pytesseract.image_to_data(self.im, output_type='dict')
            logger(f'{self.data}')

            # analyze data and save as dict.
            self.count = 0
            self.result_dict = {}
            for x in range(len(self.data['level'])):
                if self.data['text'][x] == self.text:
                    self.conf = self.data['conf'][x]  # type of conf is int
                    if self.conf > self.default_conf:
                        self.count += 1
                        self.pos = (int((self.data['left'][x] + self.data['width'][x] / 2)/2), int((self.data['top'][x] + self.data['height'][x] / 2)/2))
                        self.result_dict.update({self.count: self.pos})
            # check if get string
            if len(self.result_dict) == 0:
                return 0
            else:
                return self.result_dict
        except Exception as e:
            logger(f'analyze:Exception: ({e})')
            return False

    # get count
    def get_count(self):
        try:
            result = self.analyze()
            if result == 0:
                logger(f"Can't find ['{self.text}'] in the image")
                return False
            return len(result) if not False else False
        except Exception as e:
            logger(f'get_count:Exception: ({e})')
            return False

    # get_position
    def get_pos(self, index):
        try:
            result = self.analyze()
            if result == 0:
                logger(f"Can't find ['{self.text}'] in the image")
                return False
            if index < 0:
                logger('incorrect parameter')
                return False
            if index > len(result):
                logger(f"only can find ['{self.text}']  {len(result)}-time . index is out of range")
                return False
            return result[index] if not False else False
        except Exception as e:
            logger(f'get_pos:Exception: ({e})')
            return False

# SAMPLE:
def sample():
    photo_path = os.path.dirname(os.getcwd()) + r'/SFT/material/snapshots/test/bbb.png'
    get_dict = OCR(photo_path, 'CyberLink').analyze()
    get_count = OCR(photo_path, 'Version').get_count()
    get_pos = OCR(photo_path, 'SR').get_pos(1)
    logger(f'dict: {get_dict}')
    logger(f'count: {get_count}')
    logger(f'pos: {get_pos}')





