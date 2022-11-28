# 导入日志
from lib import common
# 要用用户字典，所以要导入user模块
from interface import user

def check_balance_interface(name):
    """
    查看余额接口
    :param name:
    return:
    """
    print(f'{name}查看了余额')
    common.log(f"{name}查看余额")
    # 拿到用户字典
    user_dic=user.get_userinfo_by_name(name)
    return user_dic["account"]
