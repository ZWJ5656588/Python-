from db.db_handle import db_serialization
from lib import common

# 查询用户字典
def get_userinfo_by_name(name):
    # print(name)
    '''
     写一个查询用户信息的接口
     :param name:
     :return:
     '''
    # 这里需要用到一个db 下面的 db_handle 数据管理的方法在这个文件夹下
    # 这里需要返回用户信息
    return db_serialization.select(name)


def register_user(name,pwd,balance=15000):
    '''
    注册用户接口
    :param name:
    :param password:
    :param balance:
    :return:
    '''
    # 下面这个用户字典要传入db_handle文件中的函数
    user_dic = {"name": name, "password": pwd
        , "locked": False, "account":balance,
                "shopping_cart": {}, "bankflow": []}

    # 这个字典到时候会存储成json文件
    # 需要通过谁写入    ？？？
    # db包  db_handle模块 的 db_serialization 对象的方法
    # db_serialization
    # 向db_handle下的实例对象传入user模块中定义好的user_dict
    db_serialization.update(user_dic)

    # 存储一个日志
    # 日志是公用的 在lib 文件夹 common 写方法 数据存储到 log 文件夹里面
    # 需要添加log 下面日志文件的路径到 setting 里面
    common.log(f'{name}注册了')


# 锁定接口
def lock_user(name):

    # 拿到用户信息，内存中先更改
    user_dic=get_userinfo_by_name(name)
    user_dic["locked"]=True
    # 写入到json文件，放入硬盘
    db_serialization.update(user_dic)
    print(f"{name}已经锁定")

    # 记录日志
    common.log(f'{name}锁定')


# 解除锁定接口
def unlock_user(name):

    # 拿到用户信息，内存中先更改
    user_dic=get_userinfo_by_name(name)
    user_dic["locked"]=False
    # 写入到json文件，放入硬盘
    db_serialization.update(user_dic)
    print(f"{name}已经解锁定")

    # 记录日志
    common.log(f"{name}解锁定")