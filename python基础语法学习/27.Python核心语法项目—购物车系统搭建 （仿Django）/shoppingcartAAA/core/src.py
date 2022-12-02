import time

from interface import bank
from interface import user
from lib import common

# 设置一个用户的信息，登录的状态

user_data = {'name': '',
             'is_auth': False, }


# 这里相当于把name 作为全局变量储存在user_data中 方便调用

def login():
    '''
    登录函数，密码输错三次锁定，用户名输错可以一直输入
    :return:
    '''
    if user_data["is_auth"]:
        print("已登录")
        return
    print("登录")
    count = 0
    while True:
        name = input("输入用户名").strip()
        # 查询用户是否存在
        user_dic = user.get_userinfo_by_name(name)
        # 判断是否锁定
        # 锁定状态
        if user_dic:
            if user_dic["locked"]:
                time.sleep(5)
                count = 0
                # 这时需要解锁定，写入user_dic，s使得locked边Flase，并写入Json
                user.unlock_user(name)
            pwd = input("输入密码").strip()
            if pwd == user_dic["password"] and user_dic["locked"] == False:
                # 用户状态
                user_data["name"] = name
                user_data["is_auth"] = True
                print("登录成功")
                break
            else:
                # 密码错误时，计数器加1，
                print("密码错误")
                count += 1
            if count == 3:
                # user中写一个锁定接口，更新json里的数据
                user.lock_user(name)
        else:
            # 没有查询到用户的json文件信息
            print("用户不存在")


def register():
    if user_data["is_auth"]:
        print("已登录")
        return
    while True:
        name = input("请输入用户名").strip()
        user_dic = user.get_userinfo_by_name(name)
        # print(user_dic)
        # 有值的字典传过来返回True
        while not user_dic:
            pwd = input("输入密码:").strip()
            pwd1 = input("确认密码:").strip()
            if pwd == pwd1:
                user.register_user(name, pwd)
                break
            else:
                # 不再输入用户名，重新输入密码确认密码即可
                print("2次密码不一致，请再次输入")
        else:
            print("用户名存在")
            break
        break


@common.login_intter
def check_balance():
    print('查看余额')
    # 需要interface接口 bank.py模块 check_balance_interface方法
    # # 取登录状态的name 从字典中取
    balance = bank.check_balance_interface(user_data["name"])
    print('你的余额是%s' % balance)


@common.login_intter
def transfer():
    # 用户查询，查看余额，转账
    # 要调用3个接口 get userinfo_by_name,check_balance_interface,transfer_interface
    while True:
        trans_name = input('请输入转入用户名，q返回退出转账').strip()
        if trans_name == user_data['name'] or trans_name == user_data['name'].upper():
            print('不能给自己转账')
            continue
        if 'q' == trans_name:
            break
        # 查看账户是否存在
        trans_dic = user.get_userinfo_by_name(trans_name)
        if trans_dic:
            trans_money = input("请输入转账金额").strip()
            if trans_money.isdigit():
                int_trans_money = int(trans_money)
                if int_trans_money > 0:
                    # 调用查看余额的接口,根据登录名拿到余额
                    user_balance = bank.check_balance_interface(user_data['name'])
                    # 用户余额必须大于转入的钱
                    if user_balance >= int_trans_money:
                        # 写转账接口 user_data['name'],trans_name,trans_money
                        bank.transfer_interface(user_data['name'], trans_name, int_trans_money)
                        break
                    else:
                        print("钱不够")
            else:
                print("不是数字，重新键入")
        else:
            print('用户不存在')




@common.login_intter
def repay():
    print('存款')
    # 调用存款的接口
    while True:
        account=input("请输入存款金额").strip()
        if account=='q':
           break
        if account.isdecimal():
            account=int(account)
            if account > 0:
                # 调用存款接口执行存款业务逻辑
                bank.repay_interface(user_data['name'],account)
                break
            else:
                print("存款应大于0")
        else:
            print("请输入数字")






@common.login_intter
def withdraw():
    print('取款')
    while True:
        withdraw_money=input('请输入取款金额:').strip()
        if 'q'==withdraw_money:
            break
        if withdraw_money.isdigit():
            withdraw_money=int(withdraw_money)
            if withdraw_money>0:
                # 调用查询余额接口，根据登录名拿到余额
                user_account=bank.check_balance_interface(user_data['name'])
                # 取款
                if user_account>= withdraw_money:
                    # 调用取款接口
                    bank.withdraw_money(user_data['name'],withdraw_money)
                    print("%s取款%s成功" % (user_data['name'],withdraw_money))
                    break
                else:
                    print("钱不够")
            else:
                print("取款金额需要大于0")
        else:
            print("请输入数字")



@common.login_intter
def check_record():
    print('查看流水')
    # 调用查看流水接口执行查看流水的业务逻辑，传入用户名
    bankflow=bank.check_bank_flow_interface(user_data["name"])
    # print(bankflow)
    for record in bankflow:
        print(record)



@common.login_intter
def shopping():
    print('购物')


@common.login_intter
def look_shoppingcart():
    print('查看购物车')


@common.login_intter
def loginout():
    user_data["is_auth"]=False
    print("注销")

# 定义一个字典，把要执行的函数地址放在字典的值中
fun_dic = {'1': login,
           '2': register,
           '3': check_balance,
           '4': transfer,
           '5': repay,
           '6': withdraw,
           '7': check_record,
           '8': shopping,
           '9': look_shoppingcart,
           '10': loginout,
           }


def run():
    while True:
        print("""
    "1":登录
    "2":注册
    "3":查看余额
    "4":转账
    "5":还款
    "6":取款
    "7":查看流水
    "8":购物
    "9":查看购买商品
    "10":注销

        """)
        choice = input('输入操作编号').strip()
        if choice not in fun_dic:
            continue
        # fun_dic[choice]拿到函数内存地址，加括号调用
        # print(fun_dic[choice])
        fun_dic[choice]()
