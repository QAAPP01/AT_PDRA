import os, cv2, math, time, numpy
from os.path import exists
from os.path import dirname
from .log import logger, qa_log
from functools import reduce
from PIL import Image

# ==================================================================================================================
# Class: CompareImage
# Description: compare image
# functions:
#   - compare_image:
#      | compare_image()    , ex: CompareImage(img1, img2).compare_image()
# Return: True/False
# Note: n/a
# Author: Terence
# ==================================================================================================================


class CompareImage(object):

    def __init__(self, image_1_path, image_2_path, rate=7):
        self.minimum_image_diff = 1
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path
        self.rate = rate

    def compare_image(self):
        try:
            # check if file exists and five waiting time
            duration = 5
            for x in range(duration):
                if os.path.isfile(self.image_1_path) is True:
                    break
                else:
                    time.sleep(1)
                    logger(f"can't find image1 ({self.image_1_path})") if x == (duration - 1) else logger(f'finding...({x + 1}sec.)')
            for y in range(duration):
                if os.path.isfile(self.image_2_path) is True:
                    break
                else:
                    time.sleep(1)
                    logger(f"can't find image2 ({self.image_2_path})") if y == (duration - 1) else logger(f'finding...({y + 1}sec.)')

            # TODO: still need to testing all the flag compability to meet our AT project
            # if use 'cv2.IMREAD_COLOR' flag  => read all RGB(w/o transparent) and save to 3-dimention
            # if use 'cv2.IMREAD_GRAYSCALE' flag => read gray
            # if use 'cv2.IMREAD_UNCHANGED' flag => read all chanel , include transparent
            image_1 = cv2.imread(self.image_1_path, 0)
            image_2 = cv2.imread(self.image_2_path, 0)
            image_diff_final = self.get_image_difference(image_1, image_2)
            logger(f'Image1 resolution: {image_1.shape}  (file:{self.image_1_path})')
            logger(f'Image2 resolution: {image_2.shape}  (file:{self.image_2_path})')

            if image_diff_final < self.minimum_image_diff:
                if image_diff_final < math.pow(0.1, self.rate):  #!!: use < math.pow(0.1, 7) to check
                    logger(f'Diff. Rate: {image_diff_final}')
                    logger('compare pass')
                    return True
                else:
                    logger(f'Diff. Rate: {image_diff_final}')
                    logger('compare fail')
                    return False
            logger('totally diff')
            return False
        except Exception as e:
            logger(f'Exception. ({e})')

    def search_image(self, order=1):
        try:
            # check if file exists and five waiting time
            duration = 5
            for x in range(duration):
                if os.path.isfile(self.image_1_path) is True:
                    break
                else:
                    time.sleep(1)
                    logger(f"can't find image1 ({self.image_1_path})") if x == (duration - 1) else logger(
                        f'finding...({x + 1}sec.)')
            for y in range(duration):
                if os.path.isfile(self.image_2_path) is True:
                    break
                else:
                    time.sleep(1)
                    logger(f"can't find image2 ({self.image_2_path})") if y == (duration - 1) else logger(
                        f'finding...({y + 1}sec.)')

            # read image
            large_img = cv2.imread(self.image_1_path, 0)
            small_img = cv2.imread(self.image_2_path, 0)
            # get w & h
            w, h = small_img.shape
            logger(f'small img resolution:({w},{h})')
            # start to match
            result = cv2.matchTemplate(large_img, small_img, cv2.TM_CCOEFF_NORMED)
            # ========cv2.minMaxLoc(src)
            # @param src input single-channel array
            # return minVal, maxVal, minLoc, maxLoc
            # @param minVal pointer to the returned minimum value; NULL is used if not required.
            # @param maxVal pointer to the returned maximum value; NULL is used if not required.
            # @param minLoc pointer to the returned minimum location (in 2D case); NULL is used if not required.
            # @param maxLoc pointer to the returned maximum location (in 2D case); NULL is used if not required.
            minV, maxV, minLoc, maxLoc = cv2.minMaxLoc(result)
            logger(f'minV:{minV}, maxV:{maxV}, minLoc:{minLoc}, maxLoc:{maxLoc}')

            # determine if the diff. value is ok  (experience: below 0.5 is totally diff.)
            if maxV > 0.9:
                # add small img width/2 & height/2 to get mid-pos
                pos = (int(maxLoc[0] + w/2), int(maxLoc[1] + h/2))
                logger(f'MaxValue: {maxV}, MaxLoc: {maxLoc}')
                if order == 1:
                    # default: find 1st(best) match
                    logger(f'Return pos: {pos}')
                    return pos
                elif type(order) is int:
                    # analyze the order
                    result2 = numpy.reshape(result, result.shape[0] * result.shape[1])
                    sort = numpy.argsort(result2)
                    index = -order
                    logger(f'start to find {order}th(order) best match')
                    pos_y, pos_x = numpy.unravel_index(sort[index], result.shape)
                    pos = (int(pos_x), int(pos_y))
                    logger(f'Return pos: {pos}')
                    return pos
                else:
                    logger('incorrect parameter')
            else:
                logger(f"no similar area. maxValue: {maxV}")
            return False

            # for mark the result
            '''
            threshold = .8
            loc = numpy.where(res >= threshold)
            print(f'zip: {loc}, range:{zip(*loc[::-1])}')
            for pt in zip(*loc[::-1]):  # Switch collumns and rows
                cv2.rectangle(large_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            cv2.imwrite('result.png', large_img)
            '''
        except Exception as e:
            logger(f'Exception. ({e})')

    @staticmethod
    def get_image_difference(image_1, image_2):
        try:
            # parameter introduction:    (calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist)
              # [images]: format can be 'uint8' or 'float32', variable needs to be put in [] !!
              # channels: if gray =>  [0] , if RGB: R: [0], G: [1], B: [2],
              # mask:  mean area, None means all picture area
              # histSize: 畫出的直方圖數量(bins), usually use 256 , variable needs to be put in [] !!
              # ranges: all color , [0, 256]
            image1_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
            image2_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

            # compareHist introduction: (準確率比較低)
              # 1st-para: First compared histogram
              # 2nd-para: Second compared histogram of the same size as H1
              # method: 公式複雜....(please refer to 'https://docs.opencv.org/3.1.0/d6/dc7/group__imgproc__hist.html')
              #         usually use 'cv2.HISTCMP_BHATTACHARYYA'
            img_hist_diff = cv2.compareHist(image1_hist, image2_hist, cv2.HISTCMP_BHATTACHARYYA)

            # matchTemplate introduction:  (image, templ, method, result=None, mask=None) 用來search 比對
              # 1st-para: image1_hist
              # 2nd_para: image2 hist (尋找的target)
              # method: 一堆公式  (please refer to 'https://vovkos.github.io/doxyrest-showcase/opencv/sphinx_rtd_theme/enum_cv_TemplateMatchModes.html')
              # result: 想存的result, array
              # mask: area
            img_template_probability_match = cv2.matchTemplate(image1_hist, image2_hist, cv2.TM_CCOEFF_NORMED)[0][0]
            img_template_diff = 1 - img_template_probability_match

            # taking only 10% of histogram diff, since it's less accurate than template method
            # 根據經驗 from web
            commutative_image_diff = (img_hist_diff / 10) + img_template_diff
            return commutative_image_diff
        except Exception as e:
            logger(f'Exception. ({e})')

    # ==================================================================================================================
    # Function: h_total_compare
    # Description: Compare images with the same size and orientation
    # Parameters: image_1_path, image_2_path
    # Return: similarity or False
    # Note: N/A
    # Author: Hausen
    # ==================================================================================================================
    def h_total_compare(self):
        try:
            image_1 = cv2.imread(self.image_1_path)
            image_2 = cv2.imread(self.image_2_path)
            logger(f'Image1 resolution: {image_1.shape}  (file:{self.image_1_path})')
            logger(f'Image2 resolution: {image_2.shape}  (file:{self.image_2_path})')
            if image_1.shape[0] != image_2.shape[0] or image_1.shape[1] != image_2.shape[1]:
                logger('\n[Fail] Images size are different')
                return 0
            else:
                height = image_1.shape[0]
                width = image_1.shape[1]
                errorL2 = cv2.norm(image_1, image_2, cv2.NORM_L2)
                similarity = 1 - errorL2 / (height * width)
                logger(f'Similarity = {similarity}')
                return similarity
        except Exception as err:
            logger(f'[Error] {err}')


class HCompareImg(object):
    def __init__(self, image_1_path, image_2_path):
        """
        :param image_1_path
        :param image_2_path
        """
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path

    def full_compare(self):
        """
        :Function: full_compare
        :Description: Compare images with the same size and orientation
        :Parameters: image_1_path, image_2_path
        :Return: similarity or False
        :Note: N/A
        :Author: Hausen
        """
        try:
            image_1 = cv2.imread(self.image_1_path)
            image_2 = cv2.imread(self.image_2_path)
            logger(f'Image1 resolution: {image_1.shape}  (file:{self.image_1_path})')
            logger(f'Image2 resolution: {image_2.shape}  (file:{self.image_2_path})')
            if image_1.shape[0] != image_2.shape[0] or image_1.shape[1] != image_2.shape[1]:
                logger('\n[Fail] Images size are different')
                return 0
            else:
                height = image_1.shape[0]
                width = image_1.shape[1]
                errorL2 = cv2.norm(image_1, image_2, cv2.NORM_L2)
                similarity = 1 - errorL2 / (height * width)
                logger(f'Similarity = {similarity}')
                return similarity
        except Exception as err:
            logger(f'[Error] {err}')

    def keypoint_compare(self):
        try:
            """
            :Description: Use Keypoint detection to compare 2 images
            :return: similarity (0-1)
            :Note: No suitable for rotating cases
            :Author: Hausen
            """
            # 讀取圖片
            logger(f'img1 = {self.image_1_path}')
            logger(f'img2 = {self.image_2_path}')
            img1 = cv2.imread(self.image_1_path)
            img2 = cv2.imread(self.image_2_path)

            # 調整大小
            if img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]:
                # logger(f"{img1.shape[0]}, {img1.shape[1]}, {img2.shape[0]}, {img2.shape[1]}")
                size = min(img1.shape[0], img1.shape[1], img2.shape[0], img2.shape[1])
                img1 = cv2.resize(img1, (size, size))
                img2 = cv2.resize(img2, (size, size))

            # 將圖片轉換為灰階圖
            gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            # 建立ORB特徵檢測器
            orb = cv2.ORB_create()

            # 檢測特徵點並計算特徵描述子
            kp1, des1 = orb.detectAndCompute(gray_img1, None)
            kp2, des2 = orb.detectAndCompute(gray_img2, None)

            # 建立BFMatcher對象
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

            # 匹配特徵點
            matches = bf.match(des1, des2)

            # 將匹配結果按照特徵點之間的距離進行排序
            matches = sorted(matches, key=lambda x: x.distance)

            # 計算相似度
            similarity = 1 - (matches[0].distance / len(matches))
            logger(f'similarity = {similarity}')

            return similarity
        except Exception as err:
            logger(f'[Error] {err}')


