#coding=utf-8
import unittest
from selenium import webdriver
import time

def login(driver,username="xiaoli",psw="Mt123456"):#这里的driver是形参
    '''登录函数'''
    #保证函数里面的每个参数都要定义
    driver.get("http://zentao.maotukeji.com/index.php?m=user&f=login")
    time.sleep(2)

    #登录
    driver.find_element_by_name("account").send_keys(username)
    driver.find_element_by_name("password").send_keys(psw)
    driver.find_element_by_id("submit").click()
    time.sleep(2)
    #获取用户名
    try:
       t=driver.find_element_by_css_selector("#userMenu>a").text
       #通过用户名判断是否登录成功
       return t
    except:
       return ""

if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Firefox()
    res=login(driver,"xiaoli","Mt123456")
    print(res)
