import adbutils
import os

def connect_device():
    # 创建adb客户端连接到Android设备
    adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
    device = adb.device()
    return device

def click_position(device, x, y):
    # 发送点击命令到该位置
    adb_cmd = f"adb -s {device.serial} shell input tap {x} {y}"
    os.system(adb_cmd)

