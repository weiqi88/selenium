from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#获得当前窗口
dangqianwin =driver.current_window_handle

#打开注册新窗口
driver.find_element_by_id("setf").click()

#获得所有窗口
allhandles =driver.window_handles

for handle in allhandles:
    if handle !=dangqianwin:
        driver.switch_to_window(handle)
        print("百度设为主页")
        #切换到百度这位主页标签
        driver.find_element_by_link_text("百度首页") .click()
        time.sleep(5)
        driver.close()
#回到原先的窗口
driver.switch_to_window(dangqianwin)

driver.find_element_by_id("kw").send_keys(u"注册邮箱")
time.sleep(3)
driver.quit()