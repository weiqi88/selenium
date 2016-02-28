from  selenium import  webdriver
import  time
values =['abc','def','selenium']
#执行循环

for serch in values:
    driver=webdriver.Firefox()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(serch)
    time.sleep(3)
    driver.quit()
