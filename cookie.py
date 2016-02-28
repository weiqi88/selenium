from selenium import webdriver
import time

driver =webdriver.Firefox()
driver.get("http://www.youdao.com")
#获得cookie信息
cookie = driver.get_cookies()
#将获得cookie的信息打印
print(cookie)
#向cookie的name额value 添加回话信息。
driver.add_cookie({'name':'key-aaaa',"value":"value-bbb"})
#遍历cookie中的name和value信息打印
for cookie in driver.get_cookies():
    print((cookie['name'],cookie['value']))
# 下面可以通过两种方式删除cookie
# 删除特定cookie
driver.delete_cookie('key-aaaa')
print( "删除特定cookie")
for cookie in driver.get_cookies():
    print((cookie['name'],cookie['value']))
#删除指定cookie
driver.delete_all_cookies()
print("删除全部cookie")
for cookie in driver.get_cookies():
    print((cookie['name'],cookie['value']))
driver.quit()