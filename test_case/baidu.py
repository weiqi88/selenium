#coding:utf-8
import unittest
import time
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import unittest,time,re
from selenium.webdriver.support.ui import Select


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.baidu.com'
        self.verificationErrors = []
        self.accept_next_alert = True

    # 百度搜索用例
    def test_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('kw').send_keys('java')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        driver.close()

    # 百度设置用例
    def test_baidu_set(self):
        driver = self.driver
        # 进入搜索设置页
        driver.get(self.base_url + '/gaoji/preferences.html')
        # 设置搜索结果每页为50条

        Select(driver.find_element_by_id("nr")).select_by_visible_text(u"每页显示50条")
        time.sleep(2)
        # 保存设置的信息
        driver.find_element_by_id('save').click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if  __name__ == "__main__":
    unittest.main()
