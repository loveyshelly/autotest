#coding=utf-8

a=1

class People():
    b=2 #整个类的变量,在整个类里全局，不用加self
    def __init__(self):#init里面通常放一些需要调用的参数
        self.c=3
        self.d=4
    def add(self):
        e=5
        print("a的值：%s" % a)
        print("b的值：%s" % self.b)
        print("c的值：%s" % self.c)
        print("d的值：%s" % self.d)
        print("e的值：%s" % e)
if __name__=="__main__":
    jia=People()
    jia.add()

