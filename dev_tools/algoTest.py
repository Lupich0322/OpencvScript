import time
from collections import deque

# 插入你的场景到下一级场景的映射
scene_navigation = {
    "Main": {
        "Chara": "Main_to_Chara.png",
        "Story": "Main_to_Story.png",
        "Summon": "Main_to_Summon.png",
        "Wild": "Main_to_Wild.png"
    },
    "Material": {
        "Beast": "Material_to_Beast.png",
        "Forest": "Material_to_Forest.png",
        "Main": "Material_to_Main.png",
        "Mountain": "Material_to_Mountain.png",
        "Somn": "Material_to_Somn.png",
        "Source": "Material_to_Source.png",
        "Star": "Material_to_Star.png",
        "Story": "Material_to_Story.png"
    },
    "Somn": {
        "Main": "Somn_to_Main.png"
    },
    "Source": {
        "Exp": "Source_to_Exp.png",
        "Gold": "Source_to_Gold.png",
        "Main": "Source_to_Main.png",
        "Material": "Source_to_Material .png",
        "Psy": "Source_to_Psy.png",
        "Sc": "Source_to_Sc.png",
        "Somn": "Source_to_Somn.png",
        "Story": "Source_to_Story.png"
    },
    "Story": {
        "Chapter1": "Story_to_Chapter1.png",
        "Chapter2": "Story_to_Chapter2.png",
        "Chapter3": "Story_to_Chapter3.png",
        "Chapter4": "Story_to_Chapter4.png",
        "Main": "Story_to_Main.png",
        "Material": "Story_to_Material.png",
        "Somn": "Story_to_Somn.png",
        "Source": "Story_to_Source.png"
    }
}

def dfs_navigation(current_scene, target_scene, path=[]):
    path = path + [current_scene]
    if current_scene == target_scene:
        return path

    next_steps = scene_navigation.get(current_scene, {})
    for next_scene in next_steps.keys():
        if next_scene not in path:
            new_path = dfs_navigation(next_scene, target_scene, path)
            if new_path:
                return new_path
    return None

def bfs_navigation(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        scene, path = queue.popleft()
        if scene == goal:
            return path

        if scene not in visited:
            visited.add(scene)
            next_steps = scene_navigation.get(scene, {})
            for next_scene in next_steps.keys():
                new_path = path + [next_scene]
                queue.append((next_scene, new_path))

    return None


def heuristic(scene, goal):
    return 0

def astar_navigation(start, goal):
    open_list = [(start, [], 0)]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[2])  # 按照代价排序
        scene, path, cost = open_list.pop(0)

        if scene == goal:
            return path

        if scene not in visited:
            visited.add(scene)
            next_steps = scene_navigation.get(scene, {})
            for next_scene in next_steps.keys():
                new_path = path + [next_scene]
                new_cost = cost + 1 + heuristic(next_scene, goal)
                open_list.append((next_scene, new_path, new_cost))

    return None


start = 'Main'
goal = 'Beast'

# 测试 DFS
start_time = time.time()
path_to_goal = dfs_navigation(start, goal)
print("DFS Path:", path_to_goal)
print("DFS Time:", time.time() - start_time)

# 测试 BFS
start_time = time.time()
path_to_goal = bfs_navigation(start, goal)
print("BFS Path:", path_to_goal)
print("BFS Time:", time.time() - start_time)

# 测试 A*
start_time = time.time()
path_to_goal = astar_navigation(start, goal)
print("A* Path:", path_to_goal)
print("A* Time:", time.time() - start_time)
