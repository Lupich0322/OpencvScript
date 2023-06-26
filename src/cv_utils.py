import cv2
import numpy as np
import datetime
import re
from PIL import Image
import os
import re

MIN_MATCH_COUNT = 10

def get_screenshot(device, area=None):
    # 使用ADB获取屏幕截图
    screenshot_pil = device.screenshot()
    # 将PIL图像转换为OpenCV图像（灰度）
    screenshot_image = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2GRAY)
    # 如果指定了截取区域，截取指定的区域
    if area is not None:
        x1, y1, x2, y2 = area
        screenshot_image = screenshot_image[y1:y2, x1:x2]  # 注意：numpy的索引顺序是[y, x]
    return screenshot_image

def save_image(image, base_path):
    # 获取当前日期和时间，生成时间戳
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 生成带有时间戳的文件名
    filename = f'{base_path}_{timestamp}.png'
    # 保存图像到指定路径
    cv2.imwrite(filename, image)

def load_template(template_path):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    return template

def match_template(screenshot_image, template):
    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 计算模板的中心位置
    center_x = max_loc[0] + template.shape[1] // 2
    center_y = max_loc[1] + template.shape[0] // 2
    return center_x, center_y, max_val

def orb_match_template(screenshot_image, template):
    # 使用ORB算法进行模板匹配
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(screenshot_image, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    if len(matches) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        if M is not None:
            center_x = int(M[0, 2] + template.shape[1] / 2)
            center_y = int(M[1, 2] + template.shape[0] / 2)
            return center_x, center_y
    # 如果匹配失败，返回无效坐标
    return None, None
