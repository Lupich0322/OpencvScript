import cv2
import numpy as np
import datetime

MIN_MATCH_COUNT = 10


def get_screenshot(device):
    # 使用ADB获取屏幕截图
    screenshot_pil = device.screenshot()
    # 将PIL图像转换为OpenCV图像（灰度）
    screenshot_image = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2GRAY)
    return screenshot_image


def save_image(image, base_path):
    # 获取当前日期和时间，生成时间戳
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 生成带有时间戳的文件名
    filename = f'{base_path}_{timestamp}.png'
    # 保存图像到指定路径
    cv2.imwrite(filename, image)


def crop_screenshot(screenshot_image, crop_area):
    # crop_area是一个元组，格式为(x, y, width, height)
    x, y, w, h = crop_area
    cropped_screenshot = screenshot_image[y:y + h, x:x + w]
    save_image(cropped_screenshot, '../logs/outputImages/cropped_screenshot')  # 保存裁剪后的图像
    return cropped_screenshot


def get_crop_area(screenshot_image, template):
    result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= 0.8:  # 如果匹配度达到0.8
        top_left = max_loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

        # 以下是扩大裁剪区域的逻辑，比如我们在原有模板周围各扩大10个像素点
        expansion_pixels = 10
        top_left_expanded = (max(0, top_left[0] - expansion_pixels), max(0, top_left[1] - expansion_pixels))
        bottom_right_expanded = (min(screenshot_image.shape[1], bottom_right[0] + expansion_pixels),
                                 min(screenshot_image.shape[0], bottom_right[1] + expansion_pixels))

        return top_left_expanded[0], top_left_expanded[1], bottom_right_expanded[0] - top_left_expanded[0], \
               bottom_right_expanded[1] - top_left_expanded[1]
    else:
        return None


def load_template(template_path):
    # 加载模板（彩色）
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    return template


def match_template(screenshot_image, template):
    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 计算模板的中心位置
    center_x = max_loc[0] + template.shape[1] // 2
    center_y = max_loc[1] + template.shape[0] // 2
    return center_x, center_y, max_val


def orb_match_template(screenshot_image, template):
    # 使用ORB算法进行模板匹配
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(screenshot_image, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    if len(matches) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        if M is not None:
            center_x = int(M[0, 2] + template.shape[1] / 2)
            center_y = int(M[1, 2] + template.shape[0] / 2)
            return center_x, center_y
    # 如果匹配失败，返回无效坐标
    return None, None
