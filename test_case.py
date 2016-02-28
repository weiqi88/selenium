import os
# 列出某个文件夹下的所有case，这里用的是python
# 所有py文件运行一次后会生成一个pyc的副本
caselist = os.listdir('D:\\selenium\\test_case')
d = len(caselist)
print(d)
for a in caselist:
    s = a.split('.')[1]  # 选取后缀名为py的文件
    print(s)
    if s == 'py':
        # 在次数执行DOS命令并将结果保存到log.txt
        os.system('D:\\selenium\\%s 1>>log.txt 2>&1'%a)
