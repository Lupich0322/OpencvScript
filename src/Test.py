import time
from adb_utils import connect_device, click_position
from cv_utils import get_screenshot, load_template,orb_match_template


class Test:
    def __init__(self):
        self.device = connect_device()

    def match_and_click_orb(self, template_path):
        # Load template
        template = load_template(template_path)
        # Get screenshot
        screenshot = get_screenshot(self.device)
        # Start timing
        start = time.time()
        # Perform ORB template matching
        x, y = orb_match_template(screenshot, template)
        # End timing
        end = time.time()
        # If match was successful, click
        if x is not None and y is not None:
            click_position(self.device, x, y)
        print("ORB template matching time:", end - start)

test = Test()
template_paths = [
        "../images/scene_templates/Main/Main_to_Select.png",
        "../images/scene_templates/Select/Select_to_source.png",
        "../images/scene_templates/Source/Source_to_Psy.png",
    ]

for i in template_paths:
    test.match_and_click_orb(i)