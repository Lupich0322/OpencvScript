from utilss import *

import datetime

device = connect_device()

# 生成时间戳
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
click_matchposition('image/ui/dailysource/dailysource_psychgramanalysis.PNG',device, timestamp)
timestamp2 = time.strftime("%Y%m%d%H%M%S", time.localtime())
click_matchposition('image/ui/dailysource/dailysource_psy_level/dailysource_psy_level_666.PNG', device, timestamp2)