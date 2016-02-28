#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest,time,re

class Youdao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.youdao.com'
        self.verificationErrors=[]
        self.accept_next_alert=True

        #有道搜索用例
    def test_youdao_search(self):
        driver =self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id('query').send_keys(u'魏琪')
        driver.find_element_by_id('qb').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertAlmostEqual([],self.verificationErrors)
if __name__=='__main__':
    unittest.main()
