#coding=utf-8

class Father():
    def fangzi(self):
        print("父亲的房子")
    def chezi(self):
        print("父亲的车")
class Mother():
    def piaozi(self):
        print("妈妈的钱")
class son(Father,Mother):#同时继承两个类
    def quxifu(self):
        fang=self.fangzi()
        che=self.che()
        piao=self.piaozi()
if __name__=="__main__":
    s=son()
    s.quxifu()


