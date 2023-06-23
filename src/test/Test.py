import time
from src.adb_utils import *
from src.cv_utils import *


class Test:
    def __init__(self):
        self.device = connect_device()

    def get_crop_area_from_template(self, template_path):
        screenshot_image = get_screenshot(self.device)
        template = load_template(template_path)
        crop_area = get_crop_area(screenshot_image, template)

        if crop_area is not None:
            print(f"Crop area for template {template_path} is {crop_area}")
            cropped_screenshot = crop_screenshot(screenshot_image, crop_area)
        else:
            print(f"No matching template found for {template_path}")

        return crop_area

test = Test()
template_path = "../../images/scene_templates/Main/Main_to_Select.png"
test.get_crop_area_from_template(template_path)
