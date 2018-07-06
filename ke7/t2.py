#coding=utf-8

#打开两个浏览器
from selenium import webdriver

driver1=webdriver.Firefox() #浏览器1
driver1.get("https://www.baidu.com")

driver2=webdriver.Firefox() #浏览器1
driver2.get("https://www.baidu.com")

driver1.find_element_by_id("kw").send_keys("haode")
driver2.find_element_by_id("kw").send_keys("byebye")

driver1.quit()
driver2.quit()
