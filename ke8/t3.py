#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#driver.find_elements()

def findElement(driver,by, value):
    element = WebDriverWait(driver,10, 1).until(lambda x: x.find_element(by, value))
    return element

def findElements(driver,by,value):
    elements=WebDriverWait(driver,10,0.5).until(lambda x:x.find_elements(by,value))
    return elements

driver.get("https://www.baidu.com")

loc1=("id","kw")
ele1=findElement(driver,*loc1)
ele1.send_keys("haode")

loc2=("css selctor","#su")
ele2=findElement(driver,*loc2)#*号后面的参数是一个list或者是一个元祖
ele2.click()