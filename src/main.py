import time

from adb_utils import *
from cv_utils import *
from scene_manage_utils import *
from game_actions import *


def main():
    # 连接设备
    device = connect_device()

    # 执行任务
    # psy_analysis(device)
    while True:
        current_scene=get_current_scene(device, "../images/scene_markers")
        print("现在的场景:", current_scene)

if __name__ == "__main__":
    main()


