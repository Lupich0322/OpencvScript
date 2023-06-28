import cv2
import matplotlib.pyplot as plt
import numpy as np
from src.adb_utils import *
from src.cv_utils import *

level_area = (0, 550, 1280, 580)

class huidujiance:
    def __init__(self):
        self.device = connect_device()

hj = huidujiance()  # 创建一个 huidujiance 类的实例
image = get_screenshot(hj.device, area=level_area)  # 通过实例访问类的属性

# 显示图像并设置鼠标悬停事件
fig, ax = plt.subplots()

cax = ax.imshow(image, cmap='gray')

def format_coord(x, y):
    numrows, numcols = image.shape
    if x >= 0 and x < numcols and y >= 0 and y < numrows:
        return f'x={x:.4f}, y={y:.4f}, intensity={image[int(y), int(x)]}'
    else:
        return 'x={}, y={}'.format(x, y)

_, binary_image = cv2.threshold(image, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Screenshot Image", binary_image)

ax.format_coord = format_coord
plt.show()
