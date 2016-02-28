#coding:utf-8
#引入 ActionChains
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#打开浏览器
browser=webdriver.Firefox()
#浏览器输入网址
browser.get('http:www.baidu.com')

#定位元素
#right=browser.find_element_by_id("kw")
#定位到元素右击
#ActionChains(browser).context_click(right).perform()
#找到元素并输入 值
#browser.find_element_by_id("kw").send_keys("selenium")
#找到 属性并赋予 变量
#double = browser.find_element_by_id("su")
#把该变量放入双击的方法中
#ActionChains(browser).double_click(double).perform()

#定位到鼠标要移动的元素上 并点击
above=browser.find_element_by_id("su").click()
#对定位到的元素执行鼠标移动到上面 的操作
ActionChains(browser).move_to_element(above).perform()
#定位到鼠标按下左键的元素


#left =browser.find_element_by_id("su")
#对定位到的元素执行鼠标左键按下的操作
#ActionChains(browser).click_and_hold(left).perform()