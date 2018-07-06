# coding:utf-8

def add(a):
    return a+1

def adddd(a,b):
    return a+b

# 匿名函数
d = lambda a: a+1#lambda是一个匿名函数的名称，其后面的a是参数
e = lambda a, b: a+b

if __name__ == "__main__":
    print(add(4))
    print(d(5))
    print(e(3, 4))
    print(e(a=3, b=4))