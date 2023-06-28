from cv_utils import *
from adb_utils import *
from src.scene_manage_utils import get_current_scene

LEVEL_TEMPLATES_DIR = '../images/level_templates'
level_area = (0,550,1280,580)
max_attempts = 5
level_templates = {}
for file_name in os.listdir(LEVEL_TEMPLATES_DIR):
    if file_name.endswith(('.jpg', '.jpeg', '.png')):
        level_number = os.path.splitext(file_name)[0]  # 提取关卡编号
        level_templates[level_number] = cv2.imread(os.path.join(LEVEL_TEMPLATES_DIR, file_name), 0)

def select_level(device, target_level):
    target_level = str(target_level)  # 确保目标关卡是字符串形式
    assert target_level in level_templates, "目标关卡不存在"
    for _ in range(max_attempts):
        screenshot_image = get_screenshot(device, area=level_area)
        _, binary_image = cv2.threshold(screenshot_image, 230, 255, cv2.THRESH_BINARY)

        # cv2.imshow("Binary Screenshot Image", screenshot_image)
        # cv2.waitKey(0)
        # cv2.imshow("Binary Screenshot Image", binary_image)
        # cv2.waitKey(0)

        matched_levels = {}  # 存储找到的所有关卡和其匹配度
        matched_locs = {}  # 存储找到的所有关卡的匹配位置

        for level_number, template in level_templates.items():
            result = cv2.matchTemplate(binary_image, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, max_loc, _ = cv2.minMaxLoc(result)
            if max_val > 0.8:  # 成功匹配到了关卡
                matched_levels[level_number] = max_val
                matched_locs[level_number] = max_loc

        if target_level in matched_levels:  # 如果匹配到的关卡中包含目标关卡
            print("调试信息: 成功选择了关卡 '{}'".format(target_level))
            # 计算模板的中心位置并点击
            center_x = matched_locs[target_level][0] + level_templates[target_level].shape[1] // 2 + level_area[0]
            center_y = matched_locs[target_level][1] + level_templates[target_level].shape[0] // 2 + level_area[1]
            click_position(device, center_x, center_y)
            return True
        else:
            # 获取匹配到的最高和最低关卡号，以判断滑动方向
            min_matched_level = min(matched_levels.keys(), key=int)
            max_matched_level = max(matched_levels.keys(), key=int)
            print("警告: 匹配到关卡范围 '{}-{}'，但没有找到目标关卡".format(min_matched_level, max_matched_level))

            if int(max_matched_level) < int(target_level):  # 目标关卡在右边，需要向左滑动
                swipe_right(device, 1070, 560, 195, 560, duration=500)
            else:  # 目标关卡在左边，需要向右滑动
                swipe_left(device, 195, 550, 1070, 560, duration=500)
            time.sleep(2)

    print("警告: 经过多次尝试后仍无法选择关卡 '{}'".format(target_level))
    return False  # 在尝试了多次后仍然没有找到目标关卡

def prepare_level(device, mode,at_times):
    at_times=str(at_times)
    current_scene = get_current_scene(device, "../images/scene_markers")
    if current_scene == 'Preparelevel':
        if mode == 'manual':
            print("警告: 手动模式正在开发中，暂时不可用。")
        elif mode == 'auto':
            print("信息: 自动模式已启动。")
            match_click(device, '../images/auto_templates/auto_select.png', area=(833, 630, 877, 682))
            match_click(device, '../images/auto_templates/auto_times.png', area=(798, 647, 857, 667))
            if at_times == 1:
                match_click(device, '../images/auto_templates/start_action.png.png', area=(1002, 639, 1122, 667))
            elif at_times == 2:
                match_click(device, '../images/auto_templates/auto_x2.png', area=(812, 528, 838, 545))
                match_click(device, '../images/auto_templates/auto_start.png', area=(1063, 640, 1121, 668))
            elif at_times == 3:
                match_click(device, '../images/auto_templates/auto_x3.png', area=(812, 466, 838, 483))
                match_click(device, '../images/auto_templates/auto_start.png', area=(1063, 640, 1121, 668))
            elif at_times == 4:
                match_click(device, '../images/auto_templates/auto_x4.png', area=(812, 406, 838, 422))
                match_click(device, '../images/auto_templates/auto_start.png', area=(1063, 640, 1121, 668))
            else:
                print("错误: 自动次数不存在")
        else:
            print("错误: 不支持的模式。")
    else:
        print("错误: 当前场景不是 'Preparelevel'。")

