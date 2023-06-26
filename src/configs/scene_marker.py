class Button:
    instances = {}  # 用于存储所有的 Button 实例

    def __init__(self, name, area, button, file):
        self.name = name  # 添加一个 name 属性来保存 transition 名称
        self.area = area
        self.button = button
        self.file = file
        Button.instances[name] = self  # 将新创建的实例添加到 instances 字典中

MAIN1 = Button(name='Main1.png', area=(1114, 272, 1178, 328), button=(1114, 272, 1178, 328), file='..\images\scene_markers\Main\Main1.png')
CHARA1 = Button(name='Chara1.png', area=(1052, 31, 1168, 68), button=(1052, 31, 1168, 68), file='..\images\scene_markers\Chara\Chara1.png')
MATERIAL1 = Button(name='Material1.png', area=(186, 194, 476, 484), button=(186, 194, 476, 484), file='..\images\scene_markers\Material\Material1.png')
MATERIAL2 = Button(name='Material2.png', area=(299, 193, 589, 483), button=(299, 193, 589, 483), file='..\images\scene_markers\Material\Material2.png')
SOMN1 = Button(name='Somn1.png', area=(931, 300, 1088, 495), button=(931, 300, 1088, 495), file='..\images\scene_markers\Somn\Somn1.png')
SOURCE1 = Button(name='Source1.png', area=(727, 195, 1017, 485), button=(727, 195, 1017, 485), file='..\images\scene_markers\Source\Source1.png')
SOURCE2 = Button(name='Source2.png', area=(299, 194, 589, 484), button=(299, 194, 589, 484), file='..\images\scene_markers\Source\Source2.png')