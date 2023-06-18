import adbutils
import os

def connect_device():
    # 创建adb客户端连接到Android设备
    adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
    device = adb.device()
    return device

def click_position(device, x, y):
    # 使用adbutils库的接口直接在设备上执行点击操作
    device.shell(f"input tap {x} {y}")

def swipe_left(device, start_x, start_y, end_x, end_y, duration=500):
    # 使用adbutils库的接口直接在设备上执行滑动操作
    device.shell(f"input swipe {start_x} {start_y} {end_x} {end_y} {duration}")

def swipe_right(device, start_x, start_y, end_x, end_y, duration=500):
    # 使用adbutils库的接口直接在设备上执行滑动操作
    device.shell(f"input swipe {start_x} {start_y} {end_x} {end_y} {duration}")

