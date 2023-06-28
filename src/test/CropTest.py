from src.adb_utils import *

class CropTest:
    def __init__(self):
        self.device = connect_device()

CropTest = CropTest()
# swipe_left(CropTest.device, 195, 550, 1070, 560, duration=300)
swipe_right(CropTest.device, 1070, 560, 195, 560, duration=300)
