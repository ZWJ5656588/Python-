 # 写一些装饰器通用接口，用于判断是否在的登录状态

import time
from conf import setting
from core import src

def log(msg):
     current_time=time.strftime('%Y-%m-%d %H:%M:%S')
     with open(setting.LOG_path,"at",encoding="utf-8") as f:
          f.write(current_time+"-"*6+msg+'\n')

# 之后的功能一定要在登录的前提下进行，所以要加装饰器
# 在src模块中放装饰器修饰任务函数

def login_intter(func):
     '''
     func就是它们
     '3':check_balance,
     查看余额添加装饰器
     十七.转账
     需要3个接口:用户查询，查看余额，转账
     get_userinfo_by_name，check_balance_interface，transfer_interface
     '4':transfer,
     '5':repay,
     '6':withdraw,
     '7':check_record,
     '8':shopping,
     '9':look_shoppingcart,
     都要在登录的情况下才能执行
     全部都写一个登录装饰器
     公用的在common里面写
     '''
     def wrapper():
          if not src.user_data['is_auth']:
               src.login()
               # 内层函数使用外层函数的参数
               return func()
          else:
             return func()
     # 外层函数返回内层函数的引用
     return wrapper
          # 登录状态在src模块的user_data字典中，先要导入模块

