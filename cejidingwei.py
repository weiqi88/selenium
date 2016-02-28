from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Firefox()
driver.get("http://wiki.thinkjoy.cn")

driver.find_element_by_id("os_username").send_keys("weiqi")
driver.find_element_by_id("os_password").send_keys("xubaojing@123")
driver.find_element_by_id("loginButton").click()
time.sleep(5)
driver.find_element_by_id("help-menu-link").click()
menu=driver.find_element_by_id("whats-new-menu-link")

ActionChains(driver).move_to_element(menu).perform()

