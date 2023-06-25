import os
import cv2
import numpy as np
import subprocess

def get_screenshot(screen_img_path):
    # 使用adb获取当前屏幕的截图，并将截图保存到指定位置
    cmd_screencap = "adb shell screencap -p /sdcard/screenshot.png"
    os.system(cmd_screencap)
    cmd_pull = "adb pull /sdcard/screenshot.png " + screen_img_path
    os.system(cmd_pull)

def crop_button_images(button_config_path, screen_img_path, output_dir):
    # 加载屏幕截图
    screen_img = cv2.imread(screen_img_path)

    # 从 button_config.py 中读取按钮配置信息
    with open(button_config_path, 'r') as f:
        lines = f.readlines()

    # 根据按钮配置信息截取相应的区域并保存
    for line in lines:
        if "Button" not in line:
            continue
        button_name = line.split(" = ")[0]
        area_str = line.split("area=")[1].split(", button")[0].strip("()")
        x1, y1, x2, y2 = [int(num) for num in area_str.split(",")]
        button_img = screen_img[y1:y2, x1:x2]
        output_img_path = os.path.join(output_dir, button_name + ".png")
        cv2.imwrite(output_img_path, button_img)

button_config_path = '../src/configs/button_config.py'
screen_img_path = 'current_screen.png'  # 当前屏幕的截图路径
output_dir = '../logs/outputImages'

get_screenshot(screen_img_path)  # 获取当前屏幕的截图
crop_button_images(button_config_path, screen_img_path, output_dir)  # 根据按钮配置信息截取图片
