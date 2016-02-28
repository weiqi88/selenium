from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.baidu.com/baidu?wd=%B7%D6%D2%B3&tn=monline_4_dg")
#获取所有分页方法并打印
s =len(driver.find_element_by_id("page").find_elements_by_class_name("pc"))
sleep(2)
print(s)
#再次获取分页并循环翻页操作
pages =driver.find_element_by_id("page").find_elements_by_class_name("pc")
length = len(pages)
print(length)
for i in range(length):
   print(i)
   pages = driver.pages =driver.find_element_by_id("page").find_elements_by_class_name("pc")
   pages[i].click()
   sleep(2)