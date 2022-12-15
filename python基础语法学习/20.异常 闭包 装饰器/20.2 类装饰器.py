# 类装饰器要使用类作为装饰器实际上很简单，只要将某个类中多定义一个__call__方法
# 这样在类作为装饰器装饰函数时，函数运行时就会运行__call__方法中的内容，这就完成类作为函数装饰器的作用啦。

from functools import wraps

class animal:
    def __init__(self, func):
        self.func = func


    def __call__(self, *args, **kwargs):
        print('working here')
        res = self.func(*args, **kwargs)
        return res

@animal
def test(name, kind):
    word = f'{name} belongs to {kind}'
    return word

# test=animal(test)
A = test('cow', 'mammals')  # @animal相当于 A=animal(test), A('cow','mammals')调用了__call__方法
print(type(test))
print(A)

print("-"*20)

# 2. 带参数的类装饰器
import time

class Timer:
    def __init__(self,prefix):
        self.prefix=prefix

    def __call__(self, func):
        def wrapper(*args,**kwargs):
            start=time.time()
            ret=func(*args,**kwargs)
            print(f'{self.prefix}:{time.time()-start}')
            return ret
        return wrapper


@Timer(prefix='current_time:')
def add(a,b):
    time.sleep(1)
    return a+b

# 等价于 add=Timer(prefix='current_time')(add),  add(2,3)相当于wrapper(2,3)
print(add(2,3))