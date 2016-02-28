#coding:utf-8
import time
print(time.time())

print(time.ctime())

print(time.localtime())

print(time.strftime('%Y%m%d%H%M%S'),time.localtime())

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
