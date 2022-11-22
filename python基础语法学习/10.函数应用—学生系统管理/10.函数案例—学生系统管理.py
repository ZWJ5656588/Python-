"""学生管理系统
        通过函数方式实现
1.系统功能菜单
2.添加学生
3.删除功能
4.修改功能
5.查询功能
6.显示所有学生信息
"""

#创建全局变量，列表类型
info_list=[]


#创建系统的功能菜单函数
def print_menu():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")


#添加学生
def add_new_info():
    while True:
        """添加学生信息
        :return
        """
        new_name=input("请输入姓名：")
        new_tel=input("请输入手机号：")
        new_qq=input("请输入QQ号：")
        """此时需要创建一个列表接收信息
           使用全局变量，其他函数也要用
        """
        for temp_info in info_list: #temp_info为字典
            #添加之前检测学生信息是否重复
            if temp_info["name"]==new_name:
                print("此用户名被占用，请输入...")
                return 0 #结束函数
        #若没有重复，则定义字典，使用字典保存学生详细信息
        info=dict()
        info["name"] = new_name
        info["tel"] = new_tel
        info["qq"] = new_qq

        #将字典传入列表
        info_list.append(info)
        feedback1 = input("是否继续添加？yes or other:")
        if feedback1 == "yes":
            continue
        else:
            print("已键入的学生信息是")
            print(info_list)
            break


#删除学生
def del_info():
    while True:
        del_num=input("请输入要删除的学生序号：")
        if 0 <= del_num <= len(info_list):
            del_flag=input("确定要删除吗，yes or no:")
            if del_flag=="yes":
                del info_list[del_num]
            break
        else:
            print("序号输入有误，返回重新输入")
            continue



#修改学生信息
def revise_info():
    while True:
        revise_num=int(input(f"请输入要更改的学生序号0—{len(info_list)-1}："))
        if 0 <= revise_num <len(info_list):
            revise_flag1=input(f"确定修改{revise_num}号学生吗？，yes or no")
            if revise_flag1=="yes":
                info_list[revise_num]["name"]=input(f"序号为{revise_num}的学生姓名为{ info_list[revise_num]['name']}修改为：")
                info_list[revise_num]["tel"]=input(f"序号为{revise_num}的学生电话为{ info_list[revise_num]['tel']}修改为：")
                info_list[revise_num]["qq"]=input(f"序号为{revise_num}的学生QQ为{ info_list[revise_num]['qq']}修改为：")
                break
            else:
                print("主动放弃修改该学生，返回上一步重新键入")
                continue
        else:
            print("错误的学生序号，退出修改")
            break


#查询学生信息
def query_info():
    index=0 #定义初始化索引序号i,遍历列表中所有的字典，再用字典的值判断
    while True:
        query_name=(input(f"请输入要查询的学生的名字："))
        for index in range(0,len(info_list)):      #这里可以直接用列表中的字典进行遍历，比索引方便，建def print_info()
            if  query_name == info_list[index]["name"]:
                print(f"找到该学生，序号:\t\t{index}\t\t"
                      f"姓名:\t\t{query_name}\t\t"
                      f"电话:\t\t{info_list[index]['tel']}\t\t"
                      f"QQ号:\t\t{info_list[index]['qq']}\t\t")
        else:
            print("没有找到该学生，请重新键入查询")
        feedback2=input("是否继续查询？yes or other:")
        if feedback2=="yes":
            continue
        else:
            break


#打印学生信息
def print_info():
    print("序号\t\t姓名\t\t手机号\t\tQQ")
    for temp in info_list:
        print(f"{info_list.index(temp)}\t\t{temp['name']}\t\t{temp['tel']}\t\t{temp['qq']}")




#创建一个函数负责调度当前这个系统的小功能
def main():
    Flag=True
    while Flag:
        #1.打印当前系统的功能模块
        #当前代码执行顺序是从上到下
        print_menu()

        #2.根据用户选择进行功能模块的调用
        num=input("请输入您要进行的操作（输入序号即可）：")

        #3.根据用户输入的序号进行判断并调用对应的函数
        if num=="1":
        #添加学生信息
            add_new_info()
        if num=="2":
        #删除学生信息
            del_info()
        if num=="3":
        #修改学生信息：
            revise_info()
        if num=="4":
        #查询学生信息
            query_info()
        if num=="5":
            print_info()
        if num=="6":
            print("退出系统，谢谢使用，再见")
            break
        question=input("是否要再次进入界面，yes or no")
        if question!="yes":
            print("退出系统，谢谢使用，再见")
            break


main()

