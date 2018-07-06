#coding=utf-8
#求a的平方-b的平方 （a+b）*（a-b）

a=1 #有等号就是实参
class Bird():

  def add(a=1,b=1): #如果参数有初始值，那参数是非必填的，后面可以不用传
    return a+b
  print(add())

  def jian(a,b):
     return a-b

  def cheng(a,b):
     return a*b
if __name__=="__main__":
    shili=Bird() #实例化过程,外部调用时需要实例化，self是类本身的实例参数
    print(type(shili))
    shili.add()

