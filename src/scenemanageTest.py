from scenemanage_utils import *
import time
from adb_utils import *
from cv_utils import *


class scenemanageTest:
    def __init__(self):
        self.device = connect_device()

scenemanageTest = scenemanageTest()
transitions = load_scene_transitions('scene_transitions.json')
current_scene = get_current_scene(scenemanageTest.device,"../images/scene_markers")
print(current_scene)
time.sleep(0.5)
navigate_to_scene(scenemanageTest.device, current_scene, 'Material', '../images/scene_templates', transitions)
