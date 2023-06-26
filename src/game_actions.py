import numpy as np
from adb_utils import *
from cv_utils import *
from scene_manage_utils import *
import time


def psy_analysis(device):
    current_scene = get_current_scene(device, "../images/scene_markers")
    print("调试信息: 当前场景" + current_scene)
    navigate_to_scene(device, current_scene, 'psy')
