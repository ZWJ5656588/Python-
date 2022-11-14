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



# 2. 三级菜单
"""打印省、市、县三级菜单
可返回上一级
可随时退出程序
"""
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                '优酷':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '湖南':{
        '长沙':{
            "世界之窗":{
             '岳麓山':{}
            }
        },
        '岳阳':{
            '岳阳楼':{
            }
        },
        '衡阳':{

        },
    },
}

# 2.1 初级方式
tag=True
while tag:
    menu1=menu
    for key in menu1: # 打印第一层
        print(key)
    choice1=input('第一层>>: ').strip() # 选择第一层
    if choice1 == 'b': # 输入b，则返回上一级
        break
    if choice1 == 'q': # 输入q，则退出整体
        tag=False
        continue
    if choice1 not in menu1: # # 输入内容不在menu1内，则继续输入
        continue
    while tag:
        menu_2=menu1[choice1] # 拿到choice1对应的一层字典
        for key in menu_2:
            print(key)
        choice2 = input('第二层>>: ').strip()
        if choice2 == 'b':
            break
        if choice2 == 'q':
            tag = False
            continue
        if choice2 not in menu_2:
            continue
        while tag:
            menu_3=menu_2[choice2]
            for key in menu_3:
                print(key)
            choice3 = input('第三层>>: ').strip()
            if choice3 == 'b':
                break
            if choice3 == 'q':
                tag = False
                continue
            if choice3 not in menu_3:
                continue
            while tag:
                menu_4=menu_3[choice3]
                for key in menu_4:
                    print(key)
                choice4 = input('第四层>>: ').strip()
                if choice4 == 'b':
                    break
                if choice4 == 'q':
                    tag = False
                    continue
                if choice4 not in menu_4:
                    continue
                # 第四层内没数据了，无需进入下一层

print("-"*20)


# 2.2 方法改进，使用list[-1]的方法，永远指向列表最后元素！！
layers=[menu,]
while True:
    if layers==[]:
        break
    current_layer=layers[-1]
    for key in current_layer:
        print(key)
    choice=input('>>:').strip()
    if choice=='b':
        # 删除当前这一层,删多了会报错，索引
        layers.pop(-1)
        continue
    if choice=='q':
        break
    if choice not in current_layer:
        continue
    layers.append(current_layer[choice])
