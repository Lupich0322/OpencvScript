from src.adb_utils import *
from src.cv_utils import *


class CropTest:
    def __init__(self):
        self.device = connect_device()

CropTest = CropTest()
config_file = '../src/configs/button_config.py'
button_info = read_button_info_from_config(config_file)
screenshot_path = '../src/screenshot.png'
output_dir = '../logs/outputImages'
crop_and_save_images(button_info, screenshot_path, output_dir)
