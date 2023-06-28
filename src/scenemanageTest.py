from src.scene_manage_utils import *
from level_utils import *

class scenemanageTest:
    def __init__(self):
        self.device = connect_device()

scenemanageTest = scenemanageTest()
current_scene = get_current_scene(scenemanageTest.device,"../images/scene_markers")
print("调试信息: 当前场景"+current_scene)
# navigate_to_scene(scenemanageTest.device, current_scene, 'Psy')
# select_level(scenemanageTest.device, '06')
# match_click(scenemanageTest.device,'../images/others/start_action.png',area = (1015, 592, 1135, 620))
# current_scene = get_current_scene(scenemanageTest.device,"../images/scene_markers")

