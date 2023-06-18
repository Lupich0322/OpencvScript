import numpy as np
from adb_utils import *
from cv_utils import *
import time


def psy_analysis(device):
    template_paths = [
        "../images/scene_templates/Main/Main_to_Select.png",
        "../images/scene_templates/Select/Select_to_source.png",
        "../images/scene_templates/Source/Source_to_Psy.png",
    ]
    # 遍历每个模板路径
    for template_path in template_paths:
        # 不断尝试获取屏幕截图并匹配模板，直到匹配度达到0.8
        while True:
            screenshot_image = get_screenshot(device)
            template = load_template(template_path)
            result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            print(max_val)
            # 当匹配度大于等于0.8时
            if max_val >= 0.8:
                center_x = max_loc[0] + template.shape[1] // 2
                center_y = max_loc[1] + template.shape[0] // 2
                click_position(device, center_x, center_y)
                break
            time.sleep(0.1)

