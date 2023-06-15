from adb_utils import *
from cv_utils import *
from game_actions import *

def main():
    # 连接设备
    device = connect_device()

    # 执行任务
    psy_analysis(device)

if __name__ == "__main__":
    main()


