from src.scene_manage_utils import *
from cnocr import CnOcr
import cv2

power_area = (1134, 175, 1211, 194)
guanqia_area = (0,550,1280,580)
class ocr_utils:
    def __init__(self):
        self.device = connect_device()

ocr_utils = ocr_utils()
image = get_screenshot(ocr_utils.device, area=guanqia_area)
cv2.imshow("Original Screenshot Image", image)
cv2.waitKey(0)
# 进行二值化处理
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Screenshot Image", binary_image)
cv2.waitKey(0)
# 进行形态学操作，去除噪点
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel, iterations=1)
# 进行轮廓检测
contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 识别数字区域
digit_contours = []
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    aspect_ratio = w / float(h)
    if 0.1 < aspect_ratio < 10:
        digit_contours.append(contour)
# 创建数字区域的掩码图像
mask = np.zeros_like(opening)
cv2.drawContours(mask, digit_contours, -1, (255), thickness=cv2.FILLED)
# 与原始图像进行位运算，过滤掉非数字部分
filtered_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)

ocr = CnOcr(det_model_name='densenet_lite_114-fc')
res = ocr.ocr(binary_image)
print("Predicted Chars:", res)