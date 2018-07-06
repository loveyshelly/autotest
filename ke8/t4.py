#coding=utf-8

#arg可以是list也可以是元祖
def add(*arg):
    for i in arg:
        print(i)
        return ""
arg=[1,2,4]
b=(1,6)
def addd(a,b):
    return a+b

if __name__=="__main__":
    can={"a":1,
         "b":2
         }
    print(addd(**can))#两个*号可以把字典里的每一个键值对挨个传过来
    print(add(*arg))

    #list和tuple用一个*号，字典用两个*号

