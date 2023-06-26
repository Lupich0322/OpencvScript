class Button:
    instances = {}  # 用于存储所有的 Button 实例

    def __init__(self, name, area, button, file):
        self.name = name  # 添加一个 name 属性来保存 transition 名称
        self.area = area
        self.button = button
        self.file = file
        Button.instances[name] = self  # 将新创建的实例添加到 instances 字典中


MAIN_TO_CHARA = Button(name='Main_to_Chara.png', area=(1098, 369, 1187, 446), button=(1098, 369, 1187, 446), file='../images/scene_templates/Main/Main_to_Chara.png')
MAIN_TO_STORY = Button(name='Main_to_Story.png',area=(1114, 272, 1178, 328), button=(1114, 272, 1178, 328), file='../images/scene_templates/Main/Main_to_Story.png')
MAIN_TO_SUMMON = Button(name='Main_to_Summon.png',area=(949, 465, 1171, 538), button=(949, 465, 1171, 538), file='../images/scene_templates/Main/Main_to_Summon.png')
MAIN_TO_WILD = Button(name='Main_to_Wild.png',area=(938, 369, 1078, 432), button=(938, 369, 1078, 432), file='../images/scene_templates/Main/Main_to_Wild.png')
CHARA_TO_MAIN = Button(name='Chara_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Chara/Chara_to_Main.png')
BEAST_TO_MAIN = Button(name='Beast_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Beast/Beast_to_Main.png')
CHAPTER1_TO_MAIN = Button(name='Chapter1_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Chapter1/Chapter1_to_Main.png')
CHAPTER2_TO_MAIN = Button(name='Chapter2_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Chapter2/Chapter2_to_Main.png')
CHAPTER3_TO_MAIN = Button(name='Chapter3_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Chapter3/Chapter3_to_Main.png')
CHAPTER4_TO_MAIN = Button(name='Chapter4_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Chapter4/Chapter4_to_Main.png')
FOREST_TO_MAIN = Button(name='Forest_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Forest/Forest_to_Main.png')
MOUNTAIN_TO_MAIN = Button(name='Mountain_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Mountain/Mountain_to_Main.png')
SOMN_TO_MAIN = Button(name='Somn_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Somn/Somn_to_Main.png')
STAR_TO_MAIN = Button(name='Star_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Star/Star_to_Main.png')
STORY_TO_CHAPTER1 = Button(name='Story_to_Chapter1.png',area=(110, 143, 336, 545), button=(110, 143, 336, 545), file='../images/scene_templates/Story/Story_to_Chapter1.png')
STORY_TO_CHAPTER2 = Button(name='Story_to_Chapter2.png',area=(384, 144, 610, 546), button=(384, 144, 610, 546), file='../images/scene_templates/Story/Story_to_Chapter2.png')
STORY_TO_CHAPTER3 = Button(name='Story_to_Chapter3.png',area=(664, 143, 890, 545), button=(664, 143, 890, 545), file='../images/scene_templates/Story/Story_to_Chapter3.png')
STORY_TO_CHAPTER4 = Button(name='Story_to_Chapter4.png',area=(940, 143, 1166, 545), button=(940, 143, 1166, 545), file='../images/scene_templates/Story/Story_to_Chapter4.png')
STORY_TO_MAIN = Button(name='Story_to_Main.png',area=(125, 30, 158, 63), button=(125, 30, 158, 63), file='../images/scene_templates/Story/Story_to_Main.png')
STORY_TO_MATERIAL = Button(name='Story_to_Material.png',area=(440, 629, 492, 664), button=(440, 629, 492, 664), file='../images/scene_templates/Story/Story_to_Material.png')
STORY_TO_SOMN = Button(name='Story_to_Somn.png',area=(597, 627, 655, 665), button=(597, 627, 655, 665), file='../images/scene_templates/Story/Story_to_Somn.png')
STORY_TO_SOURCE = Button(name='Story_to_Source.png',area=(284, 628, 324, 664), button=(284, 628, 324, 664), file='../images/scene_templates/Story/Story_to_Source.png')
SUMMON_TO_MAIN = Button(name='Summon_to_Main.png',area=(29, 30, 56, 62), button=(29, 30, 56, 62), file='../images/scene_templates/Summon/Summon_to_Main.png')
SOURCE_TO_GOLD = Button(name='Source_to_Gold.png',area=(299, 194, 589, 484), button=(299, 194, 589, 484), file='../images/scene_templates/Source/Source_to_Gold.png')
SOURCE_TO_MAIN = Button(name='Source_to_Main.png',area=(138, 661, 171, 694), button=(138, 661, 171, 694), file='../images/scene_templates/Source/Source_to_Main.png')
SOURCE_TO_MATERIAL = Button(name='Source_to_Material.png',area=(440, 629, 492, 664), button=(440, 629, 492, 664), file='../images/scene_templates/Source/Source_to_Material.png')
SOURCE_TO_SC = Button(name='Source_to_Sc.png',area=(847, 194, 1137, 484), button=(847, 194, 1137, 484), file='../images/scene_templates/Source/Source_to_Sc.png')
SOURCE_TO_SOMN = Button(name='Source_to_Somn.png',area=(597, 627, 655, 665), button=(597, 627, 655, 665), file='../images/scene_templates/Source/Source_to_Somn.png')
SOURCE_TO_STORY = Button(name='Source_to_Story.png',area=(114, 628, 173, 664), button=(114, 628, 173, 664), file='../images/scene_templates/Source/Source_to_Story.png')
SOURCE_TO_EXP = Button(name='Source_to_Exp.png',area=(727, 195, 1017, 485), button=(727, 195, 1017, 485), file='../images/scene_templates/Source/Source_to_Exp.png')
SOURCE_TO_PSY = Button(name='Source_to_Psy.png',area=(187, 195, 477, 485), button=(187, 195, 477, 485), file='../images/scene_templates/Source/Source_to_Psy.png')
MATERIAL_TO_MAIN = Button(name='Material_to_Main.png',area=(337, 304, 370, 337), button=(337, 304, 370, 337), file='../images/scene_templates/Material/Material_to_Main.png')
MATERIAL_TO_MOUNTAIN = Button(name='Material_to_Mountain.png',area=(186, 194, 476, 484), button=(186, 194, 476, 484), file='../images/scene_templates/Material/Material_to_Mountain.png')
MATERIAL_TO_SOMN = Button(name='Material_to_Somn.png',area=(597, 627, 655, 665), button=(597, 627, 655, 665), file='../images/scene_templates/Material/Material_to_Somn.png')
MATERIAL_TO_SOURCE = Button(name='Material_to_Source.png',area=(284, 628, 324, 664), button=(284, 628, 324, 664), file='../images/scene_templates/Material/Material_to_Source.png')
MATERIAL_TO_STAR = Button(name='Material_to_Star.png',area=(728, 196, 1018, 486), button=(728, 196, 1018, 486), file='../images/scene_templates/Material/Material_to_Star.png')
MATERIAL_TO_STORY = Button(name='Material_to_Story.png',area=(114, 628, 173, 664), button=(114, 628, 173, 664), file='../images/scene_templates/Material/Material_to_Story.png')
MATERIAL_TO_BEAST = Button(name='Material_to_Beast.png',area=(839, 193, 1129, 483), button=(839, 193, 1129, 483), file='../images/scene_templates/Material/Material_to_Beast.png')
MATERIAL_TO_FOREST = Button(name='Material_to_Forest.png',area=(298, 193, 588, 483), button=(298, 193, 588, 483), file='../images/scene_templates/Material/Material_to_Forest.png')
