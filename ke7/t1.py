#coding=utf-8
#object是所有类的一个基类

class Bird(object):#这里的括号可以要，也可以不要，object可以写，也可以不写，不写就默认继承object
    def zuiba(self):
        print("可以吃虫子")
    def chibang(self):
        print("翅膀可以飞")
    def jiao(self):
        print("爪子可以抓东西")
if __name__=="__main__":
   b=Bird() #创建一个实例
   b.zuiba()
   b.jiao()
   c=Bird() #创建另一个实例
   c.zuiba()
