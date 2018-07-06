#coding=utf-8
from ke6.loginfuc import login
from selenium import webdriver
import unittest
import time


def dyb(self):
    print("1")

def deb(self):
    print("2")
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.result=login(cls.driver) #只登录一次，且获取登录结果

    def test_01(self):  #用例
        print("登录之后，测试用例1")
        self.assertTrue(self.result == "肖俐")

    def test_02(self):  #用例
        print("登录之后，测试用例2")
        canshu=self.result #调用第一个用例的返回参数
        print(canshu)


    def test_03(self):
        dyb()
        deb()


if __name__=="__main__":
    unittest.main()