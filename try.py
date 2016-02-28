from selenium import webdriver

filename = input('请输入文件名')
if filename=='hello':
    raise NameError('输入错误')
