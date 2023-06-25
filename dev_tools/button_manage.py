import os
import cv2
import numpy as np
import subprocess

# 定义按钮信息的模板字符串
button_template = "Button(area={0}, button={0}, file='{1}')"


def generate_button_configs(scene_dir, output_file_path, screen_img_path):
    # 加载屏幕截图
    screen_img = cv2.imread(screen_img_path, cv2.IMREAD_GRAYSCALE)

    # 遍历指定的页面文件夹里的所有模板图片
    for image_name in os.listdir(scene_dir):
        # 读取模板图片
        template_path = scene_dir + '/' + image_name  # 使用字符串拼接生成路径
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

        # 在屏幕截图中匹配模板图片的位置
        res = cv2.matchTemplate(screen_img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x1, y1 = max_loc  # 获取匹配位置的左上角坐标
        height, width = template.shape[:2]
        x2, y2 = x1 + width, y1 + height  # 计算匹配位置的右下角坐标

        button_area = (x1, y1, x2, y2)  # 按钮的点击区域即为模板图片在屏幕截图中的匹配位置

        # 将模板图片的名称转换为按钮的名称
        button_name = image_name.replace('.png', '').upper()

        # 将按钮信息写入到 output_file_path 指定的文件中
        with open(output_file_path, 'a') as f:
            button_info = button_template.format(button_area, template_path)
            f.write(f"{button_name} = {button_info}\n")
        print(f"{button_name}的信息已写入到{output_file_path}。")

    print("所有按钮信息已成功写入!")


def get_screenshot(screen_img_path):
    # 使用adb获取当前屏幕的截图，并将截图保存到指定位置
    cmd_screencap = "adb shell screencap -p /sdcard/screenshot.png"
    os.system(cmd_screencap)
    cmd_pull = "adb pull /sdcard/screenshot.png " + screen_img_path
    os.system(cmd_pull)


scene_dir = '../images/scene_templates/Material'
output_file_path = '../src/configs/button_config.py'
screen_img_path = 'current_screen.png'  # 当前屏幕的截图路径

get_screenshot(screen_img_path)  # 获取当前屏幕的截图
generate_button_configs(scene_dir, output_file_path, screen_img_path)  # 根据截图生成按钮配置
