#coding=utf-8
#求a的平方-b的平方 （a+b）*（a-b）

a=1 #有等号就是实参
def add(a=1,b=1): #如果参数有初始值，那参数是非必填的，后面可以不用传
    return a+b
print(add())

def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
# a=10,b=5 初始化变量
c=add(a=10,b=5)#用一个参数去接收这个值
d=jian(a=10,b=5)
result=cheng(c,d)
print(result)
print(10**3)#10的3次方