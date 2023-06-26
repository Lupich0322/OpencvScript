from src.scene_manage_utils import *



class scenemanageTest:
    def __init__(self):
        self.device = connect_device()

scenemanageTest = scenemanageTest()
current_scene = get_current_scene(scenemanageTest.device,"../images/scene_markers")
print("调试信息: 当前场景"+current_scene)
navigate_to_scene(scenemanageTest.device, current_scene, 'Material')