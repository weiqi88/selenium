from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException
import  unittest,time
import userinfo  #导入函数

#通过两个变量，来接收调用函数获得用户名&密码
us,pw=userinfo.fun()
#打印两个变量
print(us,pw)
#登录模块(函数)

def login(self):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_id("os_username").clear()
    driver.find_element_by_id("os_username").send_keys(us)
    driver.find_element_by_id('os_password').clear()
    driver.find_element_by_id('os_password').send_keys(pw)
    driver.find_element_by_id('loginButton').click()
    time.sleep(3)
def logout(self):
    driver = self.driver
    driver.find_element_by_id('user-menu-link').click()
    time.sleep(2)
    driver.find_element_by_id('logout-link').click()
    time.sleep(2)