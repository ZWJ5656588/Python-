#实例应用！！！
#一个学校，有三个办公室，现在有8位老师等待分配工位，请编写程序，完成随机分配
import  random
"""定义一个列表用来保存三个办公室"""
office=[[],[],[]]
"""定义一个列表储存八位老师的名字"""
names=["A","B","C","D","E",'F','G','H']
"""遍历所有老师，随机安排到0、1、2号办公室"""
for name in names:
    random_num=random.randint(0,2)
    office[random_num].append(name)
i=1
for office_names in office:#遍历外层列表，得到内层嵌套列表
    print(f"办公室{i}的人数为{len(office_names)}")#获取内层嵌套列表的元素个数
    i+=1
    for name in office_names:
        print(f"{name}",end=" ")#把老师的名字输出到一行
    print("\n")
    print("-"*20)
