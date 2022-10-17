"""需求：用类和对象实现银行账户的资金交易管理，
包括存取款、打印交易详情，交易详情包含交易的时间，
存款额或者取款金额，每次交易后的余额"""

import time

class MoneyExhcange:
    money=0
    abstract=[]
    singe_bill_list=[]
    bill_list=[]
    transcation_num=0
    currency_type="人民币"
    service_option_num=[]
    service_option=[]
    service_menu={
        1:"1,存款",
        2:"2,取款",
        3:"3,查看明细",
        4:"4,查看余额",
        0:"0,退出系统"
    }
    for key,value in service_menu.items():
        service_option_num.append(key)
        service_option.append(value)


    def welcome_menu(self):
        print('*'*20+'欢迎使用资金交易管理系统'+'*'*20)
        for i in range(0,len(self.service_option_num)):   #注意调用类属性时一定要加上self.
            print(self.service_option[i])
        print('*'*60)


    def save_money(self):
        self.money_to_be_save=float(input('请输入存钱金额'))
        self.abstract="转入"
        self.time=time.strptime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.money+=self.money_to_be_save
        self.singe_bill_list.append(self.time)
        self.singe_bill_list.append(self.abstract)
        self.singe_bill_list.append(self.money_to_be_save)
        self.singe_bill_list.append(self.currency_type)
        self.singe_bill_list.append(self.money)
        self.singe_bill_list.append(self.singe_bill_list)
        self.singe_bill_list=[]
        self.transcation_num+=1
        print(f'已经存入{self.money_to_be_save}元！当前余额{self.money}元')
        input("请点击任意键继续...")


    def withdraw_money(self):
        self.money_to_be_withdraw = float(input('请输入取出金额'))
        if self.money_to_be_withdraw <= self.money:
            self.abstract="取出"
            self.time=time.strptime("%Y-%m-%d %H:%M:%S",time.localtime())
            self.money-=self.money_to_be_withdraw
            self.singe_bill_list.append(self.time)
            self.singe_bill_list.append(self.abstract)
            self.singe_bill_list.append(self.money_to_be_save)
            self.singe_bill_list.append(self.currency_type)
            self.singe_bill_list.append(self.money)
            self.singe_bill_list.append(self.singe_bill_list)
            self.singe_bill_list=[]  #再次赋值成空列表
            self.transcation_num+=1
            print(f'已经取出{self.money_to_be_withdraw}元！当前余额{self.money}元')
            input("请点击任意键继续...")
        else:
            print("您输入的金额超过余额，无法去除，请重新输入")
            input("请点击任意键继续...")


    def chek_bill_list(self):
        print("\t\t交易日期\t\t摘要\t\t金额\t\t币种\t\t余额\t\t")
        for i in range(0,self.transcation_num):
            print("\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t "%(
                  self.bill_list[i][0],
                  self.bill_list[i][1],
                  self.bill_list[i][2],
                  self.bill_list[i][3],
                  self.bill_list[i][4],
            ))
        input("请点击任意键继续...")


    def check_money(self):
        print("账户余额为：%s元" % self.money)
        input("请点击任意键继续...")


    def user_input(self):
        option=float(input("请输入选项 "))
        if option in self.service_option_num:
            if option == 1:
                self.save_money()
            if option == 2:
                self.withdraw_money()
            if option == 3:
                self.chek_bill_list()
            if option == 4:
                self.check_money()
            if option == 0:
                print("您已退出程序")
                exit()
        else:
            print("您的输入有误，请重新输入")
            input("请点击任意键继续...")


money_exchange=MoneyExhcange()
while True:
    money_exchange.welcome_menu()
    money_exchange.user_input()



