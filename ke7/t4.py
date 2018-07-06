#coding=utf-8
from ke7.t3 import Father,Mother #导入这两个父类，私生子也可以继承这两个类

class Sunnew(Father,Mother):
    def fangzi(self):#方法重写
        print("儿子把父亲的房子拆了，重新建房子")
    def quxifu(self):
        self.piaozi()
        self.chezi()
        self.fangzi()
if __name__=="__main__":
    s=Sunnew()
    s.quxifu()

