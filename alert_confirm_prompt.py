from selenium import   webdriver
import  time

driver =webdriver.Firefox()

driver.get("http://baidu.com")

#点击打开搜索设置
driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()
#点击保存设置

driver.find_element_by_link_text("保存设置").click()
#获取网页上的警告信息
alert = driver.switch_to_alert()

#接受警告信息
alert.accept()
#得到文本信息并打印
alert = driver.switch_to_alert()
print  (alert.text())
#取消对话框（如果有的话）
alert=driver.switch_to_alert()
alert.dismiss()
#输入值（如果有的话）
alert = driver.switch_to_alert()
alert.send_keys("xxx")
driver.quit()
