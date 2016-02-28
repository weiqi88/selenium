from selenium import  webdriver
import  os,time

driver =webdriver.Firefox()
file_path ="file:///"+os.path.abspath("xialakuang.html")
driver.get(file_path)
time.sleep(2)

#先定位到下拉框
driver.find_element_by_xpath("/html/body/select").click()
driver.find_element_by_xpath("/html/body/select/option[3]").click()
time.sleep(3)
driver.quit()