def func_1():
    yield 1
    yield from func_2()  # 切换,并且状态保存
    yield 2


def func_2():
    yield 3
    # yield from func_1()  不能写回调func_1() 会造成死递归
    yield 4
    # func_2执行完毕后自动跳转到func_1


f1=func_1()
for item in f1:
    print(item)

'''
yield关键字缺点：
    1.函数一切换到函数二之后不能手动的在函数二中切换到函数一
    2.不能实现自动切换
'''