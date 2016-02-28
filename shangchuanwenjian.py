from selenium import webdriver
import  time
driver = webdriver.Firefox()
driver.get("http://jira.thinkjoy.cn/browse/JJWAPP-336?jql=project%20%3D%20JJWAPP")
driver.find_element_by_id("login-form-username").clear()
driver.find_element_by_id("login-form-username").send_keys("weiqi")
driver.find_element_by_id("login-form-password").clear()
driver.find_element_by_id("login-form-password").send_keys("xubaojing@123")
driver.find_element_by_id("login-form-submit").click()
time.sleep(5)
print(driver.get_cookies())
driver.find_element_by_id("edit-issue").click()

button =driver.find_element_by_class_name("issue-drop-zone__button aui-button")
driver.execute_script("$(arguments[0]).fadeOut()",button)
