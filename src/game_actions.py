import numpy as np
from adb_utils import *
from cv_utils import *
import time


def psy_analysis(device):
    template_paths = [
        "../images/ui/btn/ui_enter.PNG",
        "../images/ui/btn/ui_dailysource.PNG",
        "../images/ui/dailysource/dailysource_psychgramanalysis.PNG",
        "../images/ui/dailysource/dailysource_psy_level/dailysource_psy_level_666.PNG",
        "../images/ui/btn/ui_startaction.PNG",
        "../images/ui/btn/ui_countbtn.PNG",
        "../images/ui/btn/ui_x1w.PNG",
        "../images/ui/btn/ui_x2.PNG",
        "../images/ui/btn/ui_autobtn.PNG"
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
