#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()


driver.get("https://www.baidu.com")
# class By(object):
#     """
#     Set of supported locator strategies.
#     """
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
#



driver.find_element(By.ID, "kw")

# 另外一种写法——参数化定位
driver.find_element("id", "kw")
driver.find_element("xpath", "//*[@id='kw']")
driver.find_element("css selector", "#kw")
driver.find_element("class name", "xxx")
driver.find_element("tag name","xxxxxx")





element = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_id("kw"))# 找到了就返回元素，10s之后找不到就抛异常：TimeoutException
element.send_keys("hehe")

element1 = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_id("su"))
element.click()

def element_is_disappeared(self, locator, timeout=30):
   is_disappeared = WebDriverWait(self.driver, timeout, 1).until_not(lambda x: x.find_element(*locator).is_displayed())
   return is_disappeared

def findElement(by, value):
    element = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element(by, value))
    return element



