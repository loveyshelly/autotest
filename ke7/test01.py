#coding=utf-8
from selenium import webdriver
import unittest
from ke7.loginpage import LoginPage
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.loginpage = LoginPage(self.driver)

    def test01(self):
        res=self.loginpage.login()#登录
        print(res)#获取登录结果
        time.sleep(2)
        self.assertTrue(self,"肖俐"==res)
        #self.assertTrue("肖俐"==res)

    def tearDown(self):
        self.loginpage.logout()
        self.driver.quit()

if __name__=="__main__":
    unittest.main()




