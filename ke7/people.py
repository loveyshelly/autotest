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

if __name__=="__main__":
    a=People("girl","活的")#实例化的时候调用参数
    a.zhaoduixiang(18)
    a.fangzi()
    a.chezi()


