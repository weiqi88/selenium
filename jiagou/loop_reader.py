import csv #导入csv包
import os

#读取本地CSV文件


my_file='D:\selenium\jiagou\\test.csv'

data = csv.reader(open(my_file,'r'))
#循环输入每一行信息
for user in data:
    print(user[0])
    print(user[1])
    print(user[2])
    print(user[3])