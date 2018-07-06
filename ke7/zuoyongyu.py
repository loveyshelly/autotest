#coding=utf-8

a=1#全局的

def add():
    b=4 #局部变量，只在这一个函数下生效
    c=a+3+b
    return c
for i in range(10):
    a=a+i
    print(a)

if __name__=="__main__":
    print(add())