from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time
import login # 导入登录文件

class Login (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url=('http://wiki.thinkjoy.cn')
        self.verificationErros =[]
        self.accept_next_alert = True

    #登录用例
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()


      #调用登录模块
        login.login(self)
        #调用退出模块
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErros)

if __name__=="__main__":
    unittest.main()