from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.baidu.com/baidu?wd=%B7%D6%D2%B3&tn=monline_4_dg")

span = driver.find_element_by_tag_name("span")

for spans in span:
    if spans.grt_sttribute('data-node')=='2':
        spans.click()