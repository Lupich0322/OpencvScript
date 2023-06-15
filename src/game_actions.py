import numpy as np

from adb_utils import connect_device, click_position
from cv_utils import load_template, get_screenshot, match_template
import time

def psy_analysis(device):
    # 定义模板的路径
    template_paths = ["../images/ui/ui_enter.PNG", "../images/ui/ui_dailysource.PNG", "../images/ui/dailysource/dailysource_psychgramanalysis.PNG","../images/ui/dailysource/dailysource_psy_level/dailysource_psy_level_666.PNG","../images/ui/ui_startaction.PNG","../images/ui/ui_countbtn.PNG","../images/ui/ui_x2.PNG","../images/ui/ui_autobtn.PNG"]
    # 对每个模板进行操作
    for i, template_path in enumerate(template_paths):
        template = load_template(template_path)
        screenshot = get_screenshot(device)
        x, y = match_template(screenshot, template)
        click_position(device, x, y)
        time.sleep(1)
        # 如果我们处于最后一个模板（也就是我们已经进行了最后一次点击），则跳出循环
        if i == len(template_paths) - 1:
            break
        # 等待页面切换
        while True:
            # 获取新的屏幕截图
            new_screenshot = get_screenshot(device)
            # 检查新页面是否已经加载完成，可以通过比较新旧截图来判断
            if not np.array_equal(screenshot, new_screenshot):
                break
            # 如果页面还没有切换，等待一段时间再重试
            time.sleep(0.5)