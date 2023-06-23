import cv2
import os
import adbutils
import numpy as np
import time

def connect_device():
    adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
    device = adb.device()
    return device


def click_matchposition(template_path, device, timestamp):
    # 加载模板（灰度图像）
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    # 使用ADB获取屏幕截图
    screenshot_pil = device.screenshot()
    # 将PIL图像转换为灰度图像
    screenshot_image = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2GRAY)
    # 保存屏幕截图到指定路径
    output_path = f"../logs/outputImages/screenshot_{timestamp}.png"
    cv2.imwrite(output_path, screenshot_image)
    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 计算模板的中心位置
    center_x = max_loc[0] + template.shape[1] // 2
    center_y = max_loc[1] + template.shape[0] // 2
    # 发送点击命令到该位置
    adb_cmd = f"adb -s {device.serial} shell input tap {center_x} {center_y}"
    os.system(adb_cmd)
    time.sleep(1)
