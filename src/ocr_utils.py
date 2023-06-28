from src.scene_manage_utils import *
from cnocr import CnOcr
import cv2

power_area = (1132, 25, 1218, 45)
guanqia_area = (0,550,1280,580)
levelpower_area = (951, 631, 1028, 682)

class ocr_utils:
    def __init__(self):
        self.device = connect_device()

ocr_utils = ocr_utils()
image = get_screenshot(ocr_utils.device, area=levelpower_area)
cv2.imshow("Original Screenshot Image", image)
cv2.waitKey(0)
# 进行二值化处理
_, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Screenshot Image", binary_image)
cv2.waitKey(0)
ocr = CnOcr(det_model_name='densenet_lite_114-fc')
res = ocr.ocr(image)
print("Predicted Chars:", res)