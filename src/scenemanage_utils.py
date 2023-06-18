from adb_utils import *
from cv_utils import *
import time
import json


def load_scene_transitions(json_path):
    with open(json_path, 'r') as f:
        transitions = json.load(f)
    return transitions

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

def navigate_to_scene(device, current_scene, target_scene, scene_templates_dir, transitions):
    if current_scene == target_scene:
        return
    if current_scene not in transitions or target_scene not in transitions[current_scene]:
        print(f"从 {current_scene} 到 {target_scene} 的转换未定义。")
        return
    for transition in transitions[current_scene][target_scene]:
        navigation_button_template = transition + ".png"
        navigation_button_path = os.path.join(scene_templates_dir, current_scene, navigation_button_template)
        if os.path.isfile(navigation_button_path):
            while True:
                screenshot_image = get_screenshot(device)
                template = load_template(navigation_button_path)
                result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)
                if max_val > 0.8:
                    center_x = max_loc[0] + template.shape[1] // 2
                    center_y = max_loc[1] + template.shape[0] // 2
                    click_position(device, center_x, center_y)
                    time.sleep(1)  # 等待场景转换
                    current_scene = get_current_scene(device, scene_templates_dir)
                    if current_scene == target_scene:
                        return
                else:
                    print(f"在 {current_scene} 场景中未找到 {navigation_button_template} 模板。")
                    break  # 如果在当前场景中未找到转换模板，跳出循环并尝试下一个转换
        else:
            print(f"导航按钮模板 {navigation_button_template} 未找到。")


