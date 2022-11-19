#1  购物车
"""
1.启动程序 先登录，登陆成功打印商品列表，超过三次锁定三秒，sleep
2.允许用户选择商品编号购买商品，检测余额是否充足足够，足够扣款，不够提醒
3.结账时打印信息
"""

#用户信息
user_dic={
    "name":'大海',
    'password':'123a',
    'locked':False,
    'account':5200000,
    'shopping_cart':{}   #接收购买的商品字典
}

"""登录部分"""
import  time

def login():
    print("请登录,输入exit退出")
    count=0
    while True:
        # 最上面判断user_dict[]是否为锁定状态，类似安全门
        #print(user_dic['locked'])
        if user_dic['locked']:
            print('密码输入错误，休息五秒，请五秒后登录');
            time.sleep(5)
            """5秒后解锁，休息后再次运行下面的代码进行解锁"""
            user_dic['locked']=False
            count=0     #计算输入次数重新赋值为零
        global name
        name=input("输入用户名").strip()
        if name==user_dic['name']:
            pwd=input("输入密码").strip()
            if user_dic['password']==pwd and user_dic['locked']==False:
                print("登陆成功")
                break
            else:
                print("密码错误")
                count+=1
        elif name=='exit':
                return
        else:
            print("用户名不存在")
        if count==3:
            user_dic['locked']==True


#login()  当购物部分写完时，需要将登录机制装饰到购物函数中

def login_intter(func):
    def wrapper():
        login()
        if name=='exit':
            return
        func()
    return wrapper



#购物部分
@login_intter
def shopping():
    print("购物")
    goods_list=[
        ['coffee',30],
        ['chicken',20],
        ['iphone',10000],
        ['car',100000],
        ['building',5000000]
    ]
    shopping_cart={}    #购物列表
    cost_money=0
    """想要索引展示商品，想到枚举enumerate"""
    while True:
        for index,item in enumerate(goods_list):
            print(index,item)
        choice=input('输入商品对应的编号,按t键结账').strip()
        if choice.isdigit():
            #.isdigit()字符串方法，检测输入的字符串是否为数字类型
            #要将字符串的数字转换为整型
            int_choice=int(choice)
            if int_choice<0 or int_choice>=len(goods_list):
                print(f'请输入0-{len(goods_list)}范围内的编号')
                # 结束的是while循环的本层循环
                continue
                #可以打印出商品名和商品价格
            goods_name=goods_list[int_choice][0] #商品名
            goods_price=goods_list[int_choice][1] #商品价格
            if user_dic['account']>=goods_price:
                    #购买过这个商品 进入下面的if
                if goods_name in shopping_cart:
                    shopping_cart[goods_name]['count']+=1
                    shopping_cart[goods_name]['price']= shopping_cart[goods_name]['count']*goods_price
                else:   #第一次购买
                    shopping_cart[goods_name]= {'price':goods_price,'count':1}   #再造一个字典，储存商品价格和购买次数
                # print(shopping_cart) 等到结账部分打印
                # 账户金额-购买的商品价格
                user_dic['account']-=goods_price
                # 花费的金额
                cost_money+=goods_price
                # 提示用户这一次加入购物车的商品名字
                print(f'新的商品是{goods_name}')
                # print(user_dic['account'])
                # print(cost_money)
            else:
                print("钱不够")
        elif choice =='t':
            print('结账')
            print(shopping_cart)
            buy=input('买不买(y/n)>>>').strip()
            if buy=='y':
                if cost_money==0:
                    print("不买白看")  #购物车里是空的
                    break   #跳出while循环
                #把购物车的信息储存到用户信息中
                user_dic['shopping_cart']=shopping_cart
                print(f'{user_dic["name"]}花费了{cost_money}购买了{shopping_cart},余额{user_dic["account"]}')
                print("账号信息%s" % user_dic)
                break
            else:
                print('不买')

        else:
            print('非法输入')


shopping()
#登录装饰器,在被装饰的函数shopping()前写装饰器！！！
#用@login_intter在shopping前写



