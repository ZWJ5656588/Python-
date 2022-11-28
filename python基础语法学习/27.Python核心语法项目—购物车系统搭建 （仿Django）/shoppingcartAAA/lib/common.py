 # 写一些装饰器通用接口，用于判断是否在的登录状态

import time
from conf import setting

def log(msg):
     current_time=time.strftime('%Y-%m-%d %H:%M:%S')
     with open(setting.LOG_path,"at",encoding="utf-8") as f:
          f.write(current_time+"-"*6+msg+'\n')


import