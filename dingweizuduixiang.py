from  selenium import  webdriver
import  os
import time
driver = webdriver.Firefox()
file_path =('file:///') + os.path.abspath('checkbox.html')
driver.get(file_path)
#选择页面上所有的 tag name 为 input 的元素
inputs =driver.find_elements_by_name("hrong")
#然后从中过滤出type为 checkbox的元素，danjigouxuan
for input in  inputs:
   if input.get_attribute('type')=="checkbox":
    print("ok")
else :
    print("no")
time.sleep(10)
driver.quit()
