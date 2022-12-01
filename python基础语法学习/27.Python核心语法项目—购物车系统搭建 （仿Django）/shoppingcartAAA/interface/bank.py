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
    # 放到日志中
    common.log(f"{name}查看余额")
    # 拿到用户字典，反序列化
    user_dic = user.get_userinfo_by_name(name)
    # 返回给用户
    return user_dic["account"]


def transfer_interface(from_name, to_name, account):
    from_user_dic = user.get_userinfo_by_name(from_name)
    to_user_dic = user.register_user(to_name)
    # 比较自己的钱和需要转入的钱
    if from_user_dic['account'] >= account :
        from_user_dic['account']-=account

