from selenium import webdriver
import  time
browser = webdriver.Firefox()
browser.get('http://www.baidu.com')

#捕捉报读输入异常

try:
    browser.find_element_by_id('kwss').send_keys('selenium')
    browser.find_element_by_id('su').click()
    time.sleep(5)
except:
    browser.get_screenshot_as_file('D:\jietu\error.png')
browser.quit()