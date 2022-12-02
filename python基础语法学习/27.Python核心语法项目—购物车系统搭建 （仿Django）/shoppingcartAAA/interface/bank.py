# 导入日志
from  db.db_handle import db_serialization
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


def transfer_interface(from_name, to_name, account): # 接收转账人，入账人，转账金额三个参数
    from_user_dic = user.get_userinfo_by_name(from_name)
    to_user_dic = user.get_userinfo_by_name(to_name)
    # 比较自己的钱和需要转入的钱
    if from_user_dic['account'] >= account :
        from_user_dic['account'] -= account  # 自己的余额减少
        to_user_dic["account"] += account    # 对方的余额增多
        # bankflow记录流水
        from_user_dic['bankflow'].extend(['%s转账%s元给%s' % (from_name,to_name,str(account))])
        to_user_dic['bankflow'].extend(['%s收到%s转来的%s元' % (to_name,from_name,str(account))])
        # 写入json更新用户数据
        db_serialization.update(from_user_dic)
        db_serialization.update(to_user_dic)
        # 写入日志
        common.log(f'{to_name}收到{from_name}的转账，金额{str(account)}元')
        print('%s 向 %s 转账 %s' % (from_name, to_name, str(account)))
    else:
        print("钱不够")


def repay_interface(name,account):
    """存款接口"""
    # 获取用户字典
    user_dic=user.get_userinfo_by_name(name)
    # 用户字典加上存款余额
    user_dic["account"]+=account
    user_dic["bankflow"].append(f'{name}存入了{str(account)}元')
    # 写入json
    db_serialization.update(user_dic)
    print('%s存款了%s' % (name, account)) # str强制类型转换可省略，%s进行转换
    common.log('%s存款了%s' % (name, account))


def withdraw_money(name,account):
    """取款接口"""
    user_dic=db_serialization.select(name)
    # 更改用户字典
    user_dic['account']-=account
    user_dic['bankoverflow'].append('%s取出%s元' % (name,account))
    # 写入json
    db_serialization.update(user_dic)
    print('%s取出了%s' % (name,account))
    common.log("%s取出了%s" % (name,account))


def check_bank_flow_interface(name):
    "银行流水接口"
    # 查询json用户获取用户字典
    user_dic=db_serialization.select(name)
    common.log('%s 查看银行流水' % name)
    return user_dic['bankflow']
