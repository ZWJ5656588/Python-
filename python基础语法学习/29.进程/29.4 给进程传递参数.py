from multiprocessing import Process


def test(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(*args)
    print(args)
    print(*kwargs.items())
    print(kwargs.items())
    print(kwargs)


def main():
    p=Process(target=test,args=(11,22,33,44,55),kwargs={"name":"zwj"})
    p.start()


if __name__ == '__main__':
    main()