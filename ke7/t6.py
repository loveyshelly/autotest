#coding=utf-8
from ke7.t3 import Father,Mother
class People(Father,Mother):
    def __init__(self,xingbie):#参数
        self.sex=xingbie
        self.live="live"
    def zhaoduixiang(self):
        print("找对象的要求1：%s" % self.sex)
        print("找对象的要求2：%s" % self.live)
        print("找对象的要求3：%s" % self.age)
        #实例化方法可以调用静态方法
        self.jingtai()
    @staticmethod
    def jingtai():#静态方法 跟函数功能是一样的,类里面的函数叫静态方法
        print("hello world")

