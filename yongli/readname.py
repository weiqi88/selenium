from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get('http://pan.baidu.com/')

#登录百度云

driver.find_element_by_id('TANGRAM__PSP_4__userName').clear()
driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('weiqi8812')
driver.find_element_by_id('TANGRAM__PSP_4__password').clear()
driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('weiqi1234')
time.sleep(5)
driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
time.sleep(5)
#获取用户名
now_user = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/ul/li[3]/span').text

#用户名称是否等于weiqi8812，不等于将抛出异常

if now_user==u'weiqi8812':
    print('登录成功')

else:
    raise NameError('用户名不正确')
#判断当前文件个数


#重命名文件
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/dd[1]/span').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/a[9]/span/span').click()
time.sleep(3)
driver.find_element_by_xpath('//div/input').send_keys('文件1')
time.sleep(3)
driver.find_element_by_class_name('sure').click()




    #退出
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/ul/li[3]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/ul/li[3]/div/div/span[5]/a').click()
driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[1]/a[1]').click()
time.sleep(2)
driver.close()