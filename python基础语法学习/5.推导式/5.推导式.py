for i in range(2,2):
    print(i)
print("ni")

print('-'*20)

a=[x*x for x in range(1,5) ]
print(a)


a=[]
for i in range (3):
    def fun(x):
        return x*i
    a.append(fun)
print(a)
print(a[0](2))   # a[0]是个函数地址，然后传入(2)进行调用

print('-'*20)

a=[lambda x:x*i for i in range(3)]  # lambda匿名函数返回的是函数的地址
print(a)
print(a[0](5))
print(a[1](5))
print(a[2](5))

print('-'*20)

# lambda函数返回值是函数地址！！
add=lambda x,y:x+y
print(type(add))