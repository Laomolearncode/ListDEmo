#类型转换
name='张三'
age=20
# print(name+'今年'+age+'岁') 报错，name与age的数据类型不同
print(name+'今年'+str(age)+'岁') # 把age转换为字符串类型就不会报错
a=10
b=6.6
c=True
d='9.9'
e='hello'
print(a,str(a),type(a),type(str(a)))
print(c,int(c),type(c),type(int(c)))
#print(d,int(d),type(d),type(int(d))) 报错，因为小数串和文字串不能转换为整数类型
#print(e,float(e),type(e),type(float(e))) 报错，非数字不能转换为浮点类型
print(a,float(a),type(a),type(float(a)))