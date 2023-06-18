from scenemanage_utils import *
import time
from adb_utils import *
from cv_utils import *


class scenemanageTest:
    def __init__(self):
        self.device = connect_device()

scenemanageTest = scenemanageTest()
current_scene = get_current_scene(scenemanageTest.device,"../images/scene_markers")
print(current_scene)
time.sleep(0.5)
navigate_to_scene(scenemanageTest.device, 'Main', 'Beast')
