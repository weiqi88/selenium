# coding=utf-8

import unittest
#把test_case目录添加到path路径下，这里用的相对路径
import sys
sys.path.append('\test_case')
from test_case import youdao
from test_case import baidu

# 这里导入需要测的文件

import HTMLTestRunner
import time

testunit = unittest.TestSuite()

# 将测试用例加入到测试容器中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
# 执行测试套件
# unner = unittest.TextTestRunner()
# unner.run(testunit)

# 获取前面时间
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
# 定义报告存放路径
filename = 'D:\\selenium\\report\\' + now + 'result2.html'

fp = file(filename, 'wb')
print(filename)
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索报告',
    description=u'用例执行情况'
)
# 执行测试用例
runner.run(testunit)
