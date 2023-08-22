

headers=['姓名','年龄','体重']
li=[('莫',21,121)]
import csv
with open('户口本.csv','w',encoding='utf-8',newline='')as f:
    write =csv.writer(f)
    write.writerow(headers)
    write.writerows(li)
