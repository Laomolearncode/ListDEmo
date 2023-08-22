# 函数print

#可以输出数字
print(520)
print(99.1)

#可以输出字符串
print('helloworld')
print("helloworld")

#可以输出运算符的表达式，直接得出结果
print(3+4)
print(3*3)

#以上是将内容输出到显示器，接下来将数据输出到文件中
fp=open('C:/Users/86184/Desktop/pythontext.txt','a+')   #a+如果文件不存在就自动创建，存在就在文件内容后面继续追加要输出的内容
print('helloworld',file=fp)    #注意：file=fp
fp.close()

#不进行换行输出
print('hello','world','Python')
