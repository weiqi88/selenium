import  os
from selenium import  webdriver
import time
fp =webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

browser =webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
time.sleep(10)
browser.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[3]/table/tbody/tr[2]/td[1]/span/a[1]").click()