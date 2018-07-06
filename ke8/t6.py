#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.find_elements()

def findElement(driver,by,value):#loctor是元祖类型
    '''
    args:
    loctor 传元祖，如("id","xx")
    '''
    element = WebDriverWait(driver,30,0.5).until(lambda x: x.find_element(by, value))
    return element

class find_element():
    def __init__(self,by,value):
        self.by=by
        self.value=value

    def __call__(self,driver):
        element = WebDriverWait(driver, 30, 0.5).until(lambda x: x.find_element(self.by, self.value))
        return element

driver.get("https://www.baidu.com")
ele=find_element("id","kw")#类实例化
ele(driver).send_keys(u"悠悠")  #实例化后变成函数了

from selenium.webdriver.support import expected_conditions as EC
# import time

# re=EC.title_is("期望的title")(driver)#传driver参数
# print(re)
res=WebDriverWait(driver, 10, 0.5).until(EC.title_is(u"悠悠"))
print(res)

res1=WebDriverWait(driver,10,0.5).until(EC.title_contains(u"悠悠"))
print(res1)

#判断元素存在不存在 只要在DOM就是存在的，即使不可见
loc2=("id","su")
res2=WebDriverWait(driver,30,0.5).until(EC.presence_of_element_located())
print("1111111")
print(res2) #存在的话，返回的是找到的这个元素

loc3=("id","xxx")
res3=WebDriverWait(driver,30,0.5).until(EC.presence_of_element_located())
print("222222")
print(res3)  #如果元素不存在了，那就会抛异常TimeoutException

