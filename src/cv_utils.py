import cv2
import numpy as np
import datetime
import os

MIN_MATCH_COUNT = 5

def get_screenshot(device):
    # 使用ADB获取屏幕截图
    screenshot_pil = device.screenshot()
    # 将PIL图像转换为OpenCV图像（灰度）
    screenshot_image = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2GRAY)
    # 获取当前日期和时间
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 保存带时间戳的图像
    cv2.imwrite(f'../logs/outputImages/screenshot_{timestamp}.png', screenshot_image)
    return screenshot_image

def load_template(template_path):
    # 加载模板（彩色）
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
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    if len(matches) > MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        if M is not None:
            center_x = int(M[0, 2] + template.shape[1] / 2)
            center_y = int(M[1, 2] + template.shape[0] / 2)
            return center_x, center_y
    # 如果匹配失败，返回无效坐标
    return None, None


def get_current_scene(device, scene_templates_dir):
    # 获取当前屏幕截图
    screenshot_image = get_screenshot(device)
    # 遍历所有场景模板
    for scene in os.listdir(scene_templates_dir):
        scene_dir = os.path.join(scene_templates_dir, scene)
        if os.path.isdir(scene_dir):
            # 读取场景文件夹下的图片
            for file_name in os.listdir(scene_dir):
                if file_name.endswith(('.jpg', '.jpeg', '.png')):
                    template_path = os.path.join(scene_dir, file_name)
                    # 加载模板
                    template = load_template(template_path)
                    # 执行模板匹配
                    result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
                    _, max_val, _, max_loc = cv2.minMaxLoc(result)
                    # 如果匹配度大于阈值，例如0.8，则认为当前场景是这个场景
                    if max_val > 0.8:
                        return scene
    # 如果没有匹配到任何场景，返回None
    return None

