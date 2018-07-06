#coding=utf-8
a=[1,2,3,4,5,6,7]
print(len(a))

print(sum(a))

def he(aa):
    '''求和的函数'''
    s=0
    for i in aa:
        s=s+i
    return s    #如果没有return 返回None
print(he(a))
b="中文"
print(type(b))

c=list(range(10))#0到9的列表
print(c)

import random
e=random.randint(1,10)#1到10随机输出
print(e)

h=[0,1,2,3,4,5,6,7,8,9]
k=["a","b","c","d","e","f"]

for i,j in zip(h,k):
    print(j+str(i))


