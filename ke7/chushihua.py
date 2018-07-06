#coding=utf-8

class Son():
    def __init__(self):#子类初始化方法（一出生就含着金钥匙）
        self.jinyaoshi="金钥匙"#加self就是全局变量了
        print(self.jinyaoshi)
    def zhaoduixiang(self):
        print(self.jinyaoshi)
        print("开始找对象")
if __name__=="__main__":
    aa=Son()#实例化的时候，默认执行init里面的内容
    aa.zhaoduixiang()