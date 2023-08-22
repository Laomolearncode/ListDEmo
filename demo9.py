sum=0;
a=1;
while a<101:
    if not a%2:
        sum+=a;
    a+=1;
print('100内的偶数和为:',sum)
'''------------------------------------------'''
total=0;
for item in range(1,101):
    if item%2==0:
        total+=item
print('100内的偶数和为:',total)
'''------------------break---------------------'''
for item1 in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print("对不起，三次密码均输入错误")
'''-----使用continue输出5的倍数-----'''
for item2 in range(1,51):
    if item2%5 !=0:
        continue
    print(item2)