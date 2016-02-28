from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://dapw-pro.thinkjoy.com.cn/#/app/auth/login")
driver.add_cookie({'access_token':"c5d2ffbc-d0ec-45eb-aae3-27603445bc82"})

driver.get("http://dapw-pro.thinkjoy.com.cn/#/app/auth/login")
print("xxxx")
print(driver.get_cookies())
