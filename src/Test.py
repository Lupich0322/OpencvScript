import time
from adb_utils import connect_device, click_position
from cv_utils import get_screenshot, load_template, match_template, sift_match_template, akaze_match_template, \
    brisk_match_template, orb_match_template


class Test:
    def __init__(self):
        self.device = connect_device()

    def match_and_click_tm(self, template_path):
        # 加载模板
        template = load_template(template_path)
        # 获取屏幕截图
        screenshot = get_screenshot(self.device)
        # 开始计时
        start = time.time()
        # 进行模板匹配
        x, y, max_val = match_template(screenshot, template)
        # 结束计时
        end = time.time()
        print("模板匹配最大值：", max_val)
        click_position(self.device, x, y)
        print("模板匹配所用时间：", end - start)

    def match_and_click_sift(self, template_path):
        # 加载模板
        template = load_template(template_path)
        # 获取屏幕截图
        screenshot = get_screenshot(self.device)
        # 开始计时
        start = time.time()
        # 进行SIFT模板匹配
        x, y = sift_match_template(screenshot, template)
        # 结束计时
        end = time.time()
        # 如果匹配成功，则点击
        if x is not None and y is not None:
            click_position(self.device, x, y)
        else:
            print("SIFT模板匹配未找到匹配")
        print("SIFT模板匹配所用时间：", end - start)

    def match_and_click_akaze(self, template_path):
        # Load template
        template = load_template(template_path)
        # Get screenshot
        screenshot = get_screenshot(self.device)
        # Start timing
        start = time.time()
        # Perform AKAZE template matching
        x, y = akaze_match_template(screenshot, template)
        # End timing
        end = time.time()
        # If match was successful, click
        if x is not None and y is not None:
            click_position(self.device, x, y)
        print("AKAZE template matching time:", end - start)

    def match_and_click_brisk(self, template_path):
        # Load template
        template = load_template(template_path)
        # Get screenshot
        screenshot = get_screenshot(self.device)
        # Start timing
        start = time.time()
        # Perform BRISK template matching
        x, y = brisk_match_template(screenshot, template)
        # End timing
        end = time.time()
        # If match was successful, click
        if x is not None and y is not None:
            click_position(self.device, x, y)
        print("BRISK template matching time:", end - start)

    def match_and_click_orb(self, template_path):
        # Load template
        template = load_template(template_path)
        # Get screenshot
        screenshot = get_screenshot(self.device)
        # Start timing
        start = time.time()
        # Perform ORB template matching
        x, y = orb_match_template(screenshot, template)
        # End timing
        end = time.time()
        # If match was successful, click
        if x is not None and y is not None:
            click_position(self.device, x, y)
        print("ORB template matching time:", end - start)

test = Test()
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
# test.match_and_click_tm("../images/ui/btn/ui_enter.PNG")

for i in template_paths:
    test.match_and_click_orb(i)

# test.match_and_click_sift("../images/ui/btn/ui_enter.PNG")

# test.match_and_click_akaze("../images/ui/btn/ui_enter.PNG")

# test.match_and_click_brisk("../images/ui/btn/ui_enter.PNG")
