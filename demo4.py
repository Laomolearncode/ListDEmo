#整数类型
print('十进制',101)
print('二进制',0b101)
print('八进制',0o11)
print('十六进制',0x12)
#浮点数类型
n1=1.1
n2=2.2
print(n1+n2)  #有时浮点数运算打印结果会出现误差
              #解决方案：导入decimal模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
a1=3.3
a2=5.6
print(a1+a2)
from decimal import Decimal
print(Decimal('3.3')+Decimal('5.6'))
#布尔类型
f1=True     #在python中 True和 False是有整数类型的值的
f2=False    #True的值为 1，False的值为 0；严格区分大小写
print(f1,type(f1))
print(f1+f2)
#字符串类型
str1='对酒当歌，人生几何'
str2="对酒当歌，人生几何"
str3='''对酒当歌，
人生几何'''
print(str1,type(str1))
print(str2)
print(str3)
