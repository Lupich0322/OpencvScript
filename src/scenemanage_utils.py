from adb_utils import *
from cv_utils import *
import time
import json
from queue import PriorityQueue

# 加载场景转换信息
with open('scene_transitions.json', 'r') as file:
    transitions = json.load(file)

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

# 生成邻接表
adjacency_list = {scene: list(transitions.keys()) for scene, transitions in transitions.items()}

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
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    print(path)
    return path

# 导航到目标场景
def navigate_to_scene(device, start_scene, end_scene):
    # 获取从起始场景到目标场景的最短路径
    path = get_shortest_path(start_scene, end_scene)

    for i in range(len(path) - 1):
        current_scene = path[i]
        next_scene = path[i + 1]
        transition = transitions[current_scene][next_scene]

        while True:
            # 获取屏幕截图
            screenshot_image = get_screenshot(device)
            # 加载场景转换模板
            template = load_template(os.path.join("../images/scene_templates", current_scene, transition))
            # 模板匹配
            result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > 0.8:
                # 计算点击位置
                center_x = max_loc[0] + template.shape[1] // 2
                center_y = max_loc[1] + template.shape[0] // 2
                # 点击
                click_position(device, center_x, center_y)
                time.sleep(1)  # 等待场景转换

                if get_current_scene(device, "../images/scene_markers") == next_scene:
                    break  # 如果已经到达下一个场景，则跳出循环

