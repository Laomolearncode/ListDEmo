#算数运算符
print(1+1)
print(5-3)
print(4*3)
print(11/5)  # 除法运算
print(11//5) #整除运算，结果取整数
print(9%4)
print(2**2)
print(10//-7) #整除运算，一正一负向下取整
print(7%-3)    #取余运算，一正一负要用公式：余数=被除数-除数*商
print(-7%3)
#赋值运算符
print('-------解包赋值-------')
a,b,c=10,20,30
print(a,b,c)
print('-------交换位置-------')
a,b,c=c,a,b
print(a,b,c)
#比较运算符
'''一个 = 称为赋值运算符，== 称为比较运算符
   一个变量由三个部分组成，标识，类型，值
   == 比较的是值； is 比较的是标识
   '''
a=10
b=10
print(a==b)   #True 说明 a与 b的value相等
print(a is b) #True 说明 a 与 b的id标识相等
#一下代码后面会学
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1 == lst2)    #value -->True
print(lst1 is lst2)    #id -->Flase
print(id(lst1))
print(id(lst2))
#位运算符
print(4&8)   #同时为 1，结果为 1
print(4|8)   #同时为 0，结果为 0
print(4<<1)  #向左移动一个位置，相当于乘以 2
print(8>>2)  #向右移动两个位置，相当于除以 4