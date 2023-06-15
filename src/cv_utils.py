import cv2
import numpy as np
import time

def get_screenshot(device):
    # 使用ADB获取屏幕截图
    screenshot_pil = device.screenshot()
    # 将PIL图像转换为OpenCV图像彩色
    screenshot_image = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)
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
    return center_x, center_y

def wait_for_light_refresh(device, template_path):
    # 加载模板
    template = load_template(template_path)
    # 等待页面刷新
    while True:
        # 获取新的屏幕截图
        new_screenshot = get_screenshot(device)
        # 进行模板匹配
        x, y = match_template(new_screenshot, template)
        # 如果匹配成功，表示我们已经到达了期望的页面状态
        if x > 0 and y > 0:
            break
        # 如果页面还没有刷新，等待一段时间再重试
        time.sleep(0.5)

def wait_for_heavy_refresh(device, status_template_paths):
    # 等待页面切换
    while True:
        # 获取新的屏幕截图
        new_screenshot = get_screenshot(device)
        # 加载状态模板并进行匹配
        for status_template_path in status_template_paths:
            status_template = load_template(status_template_path)
            x, y = match_template(new_screenshot, status_template)
            # 如果匹配成功，表示我们已经到达了期望的页面状态
            if x > 0 and y > 0:
                break
        # 如果页面还没有切换，等待一段时间再重试
        time.sleep(0.5)
