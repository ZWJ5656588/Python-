import os

# print(os.path.dirname(__file__))   拿到目录conf
# 获取shoppingcartAAA项目路径,是conf的上级目录
Source_path=os.path.dirname(os.path.dirname(__file__))

DB_path=os.path.join(Source_path,"db")
# print(DB_path)

# 日志路径
LOG_path=os.path.join(Source_path,"log","user1.log")
# print(LOG_path)