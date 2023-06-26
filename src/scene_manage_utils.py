from adb_utils import *
from cv_utils import *
import time
import json
from queue import PriorityQueue
from collections import deque
from src.configs.button_config import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# 加载场景转换信息
with open('../configs/scene_transitions.json', 'r') as file:
    transitions = json.load(file)
# 生成邻接表
adjacency_list = {scene: list(transitions.keys()) for scene, transitions in transitions.items()}

def load_scene_transitions(json_path):
    with open(json_path, 'r') as f:
        transitions = json.load(f)
    return transitions

def get_current_scene(device, scene_templates_dir, max_attempts=5):
    attempt = 0  # 当前尝试次数
    while attempt < max_attempts:
        screenshot_image = get_screenshot(device)
        # DEBUG: 记录获取到的屏幕截图
        print("调试信息: 已获取屏幕截图")

        # 遍历所有场景模板
        for scene in os.listdir(scene_templates_dir):
            scene_dir = os.path.join(scene_templates_dir, scene)
            if os.path.isdir(scene_dir):
                for file_name in os.listdir(scene_dir):
                    if file_name.endswith(('.jpg', '.jpeg', '.png')):
                        template_path = os.path.join(scene_dir, file_name)
                        template = load_template(template_path)
                        result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
                        _, max_val, _, max_loc = cv2.minMaxLoc(result)
                        if max_val > 0.8:
                            print("调试信息: 已在场景 '{}' 中找到模板 '{}'".format(scene, file_name))
                            return scene
        attempt += 1  # 增加尝试次数
        print("警告: 无法识别当前场景，尝试再次获取屏幕截图")
        time.sleep(1)  # 等待一段时间后再次尝试获取屏幕截图
    print("警告: 经过多次尝试后仍无法识别当前场景")
    return None


def get_button_area(button, expand_pixels=10):
    x1, y1, x2, y2 = button.area
    # 确保截取区域不超过屏幕边界
    x1 = max(0, x1 - expand_pixels)
    y1 = max(0, y1 - expand_pixels)
    x2 = min(x2 + expand_pixels, SCREEN_WIDTH)
    y2 = min(y2 + expand_pixels, SCREEN_HEIGHT)
    return (x1, y1, x2, y2)

# A* 搜索算法
def a_star_search(start, end):
    # 创建优先队列
    frontier = PriorityQueue()
    frontier.put((0, start))

    # 来自哪里，当前场景是从哪个场景转换来的
    came_from = {start: None}
    # 到目前为止的成本，从起始场景到当前场景的总成本
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == end:
            break

        for next in adjacency_list[current]:
            new_cost = cost_so_far[current] + 1  # 所有的转换成本都是1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # 使用启发式函数估计的总成本：到目前为止的成本 + 从当前场景到目标场景的估计成本
                priority = new_cost + heuristic(end, next)  # 假设启发式成本为1（如果 next != end），否则为0
                frontier.put((priority, next))
                came_from[next] = current

    return came_from, cost_so_far

# 启发式函数
def heuristic(end, next):
    return 0 if next == end else 1

# 获取从起始场景到目标场景的最短路径
def get_shortest_path(start, end):
    came_from, cost_so_far = a_star_search(start, end)
    path = deque()
    current = end

    while current is not None:
        path.appendleft(current)  # 在路径的左端添加当前场景
        current = came_from[current]

    print(list(path))  # 如果你希望路径仍然是一个列表，你可以将其转换为列表
    return path

# 导航到目标场景
def navigate_to_scene(device, start_scene, end_scene):
    # 获取从起始场景到目标场景的最短路径
    path = get_shortest_path(start_scene, end_scene)

    for i in range(len(path) - 1):
        current_scene = path[i]
        next_scene = path[i + 1]
        transitions_sequence = transitions[current_scene][next_scene]  # 获取转换步骤列表

        print("调试信息: 从场景 '{}' 切换到场景 '{}'".format(current_scene, next_scene))

        for transition in transitions_sequence:
            max_attempts = 2  # 设定最大尝试次数
            attempt = 0  # 当前尝试次数

            while attempt < max_attempts:
                button = Button.instances[transition]
                area = get_button_area(button)
                print("调试信息: 获取按钮 '{}' 的区域 {}".format(transition, area))

                screenshot_image = get_screenshot(device, area)

                # 显示截取的屏幕图片
                cv2.imshow("Screenshot Image", screenshot_image)
                cv2.waitKey(0)

                template = load_template(os.path.join("../images/scene_templates", current_scene, transition))
                result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)

                if max_val > 0.8:
                    print("调试信息: 匹配到模板 '{}'".format(transition))
                    center_x = max_loc[0] + template.shape[1] // 2
                    center_y = max_loc[1] + template.shape[0] // 2
                    # 将区域的起始点坐标加到中心点上
                    center_x += area[0]
                    center_y += area[1]
                    click_position(device, center_x, center_y)
                    time.sleep(0.5)  # 等待场景转换

                    if get_current_scene(device, "../images/scene_markers") == next_scene:
                        print("调试信息: 到达场景 '{}'".format(next_scene))
                        break  # 如果已经到达下一个场景，则跳出循环
                else:
                    print("警告: 未能匹配到模板 '{}'，尝试再次匹配".format(transition))
                    attempt += 1
                    time.sleep(0.5)