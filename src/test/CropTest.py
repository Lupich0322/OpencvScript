from src.scene_manage_utils import *

class CropTest:
    def __init__(self):
        self.device = connect_device()

CropTest = CropTest()
# swipe_left(CropTest.device, 195, 550, 1070, 560, duration=500)
# swipe_right(CropTest.device, 1070, 560, 195, 560, duration=500)
get_current_scene(CropTest.device, "../images/scene_markers")