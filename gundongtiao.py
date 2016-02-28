from  selenium import  webdriver
import  time
#访问百度
driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将页面混动条拖到最底部
js ="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

#将滚动条移到页面顶部
js ="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

driver.quit()