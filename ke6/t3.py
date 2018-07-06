#coding=utf-8
import unittest
from selenium import webdriver
import time

def login(driver,username="admin",psw="123456"):#这里的driver是形参
    '''登录函数'''
    #保证函数里面的每个参数都要定义
    driver.get("http://zentao.maotukeji.com/index.php?m=user&f=login")
    time.sleep(2)

    #登录
    driver.find_element_by_name("account").send_keys(username)
    driver.find_element_by_name("password").send_keys(psw)
    driver.find_element_by_id("submit").click()

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox() #全局的driver
    def test_01(self):
        login(self.driver)
if __name__=="__main__":
    #这里是自测的内容

    a=input("输入你的账号:") #直接在控制台输入账号
    b=input("输入你的密码：")#直接在控制台输入账号
    login(driver,username="addd",psw="1111")#调用登录