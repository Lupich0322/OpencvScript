import cv2
import numpy as np
import datetime


MIN_MATCH_COUNT = 10

def get_screenshot(device):
    # 使用ADB获取屏幕截图
    screenshot_pil = device.screenshot()
    # 将PIL图像转换为OpenCV图像彩色
    screenshot_image = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Save the image with timestamp
    cv2.imwrite(f'../logs/outputImages/screenshot_{timestamp}.png', screenshot_image)
    return screenshot_image

def load_template(template_path):
    # 加载模板（彩色）
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    return template

def match_template(screenshot_image, template):
    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 计算模板的中心位置
    center_x = max_loc[0] + template.shape[1] // 2
    center_y = max_loc[1] + template.shape[0] // 2
    return center_x, center_y, max_val

def sift_match_template(screenshot_image, template):
    # 使用SIFT进行模板匹配
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(template, None)
    kp2, des2 = sift.detectAndCompute(screenshot_image, None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m[0].queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m[0].trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        if M is not None:
            center_x = int(M[0, 2] + template.shape[1] / 2)
            center_y = int(M[1, 2] + template.shape[0] / 2)
            return center_x, center_y
    return None, None  # 返回无效坐标

def orb_match_template(screenshot_image, template):
    # Use the ORB algorithm to perform template matching
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(screenshot_image, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1,des2)
    # Sort matches by distance (i.e., quality of the match)
    matches = sorted(matches, key = lambda x:x.distance)
    if len(matches) > MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        if M is not None:
            center_x = int(M[0, 2] + template.shape[1] / 2)
            center_y = int(M[1, 2] + template.shape[0] / 2)
            return center_x, center_y
    return None, None  # Return invalid coordinates if match failed


def akaze_match_template(screenshot_image, template):
    # Use the AKAZE algorithm to perform template matching
    akaze = cv2.AKAZE_create()
    kp1, des1 = akaze.detectAndCompute(template, None)
    kp2, des2 = akaze.detectAndCompute(screenshot_image, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1,des2)
    # Sort matches by distance (i.e., quality of the match)
    matches = sorted(matches, key = lambda x:x.distance)
    if len(matches) > MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        if M is not None:
            center_x = int(M[0, 2] + template.shape[1] / 2)
            center_y = int(M[1, 2] + template.shape[0] / 2)
            return center_x, center_y
    return None, None  # Return invalid coordinatesif match failed

def brisk_match_template(screenshot_image, template):
    # Use the BRISK algorithm to perform template matching
    brisk = cv2.BRISK_create()
    kp1, des1 = brisk.detectAndCompute(template, None)
    kp2, des2 = brisk.detectAndCompute(screenshot_image, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1,des2)
    # Sort matches by distance (i.e., quality of the match)
    matches = sorted(matches, key = lambda x:x.distance)
    if len(matches) > MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        if M is not None:
            center_x = int(M[0, 2] + template.shape[1] / 2)
            center_y = int(M[1, 2] + template.shape[0] / 2)
            return center_x, center_y
    return None, None  # Return invalid coordinates if match failed
