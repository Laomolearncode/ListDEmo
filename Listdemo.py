lst=[54,13,4.13,80,22]
print(lst[-2])
print(lst.index(13))
print(lst.index(13,0,3))
print(lst[4:0:-2])
print('-----------------------')
for item in lst:
    print(item)
lst.append(100)
print(lst)
lst1=[True,False,'hh']
lst.extend(lst1)
print(lst)
lst.insert(2,True)
print(lst)