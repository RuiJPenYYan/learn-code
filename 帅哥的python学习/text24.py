#encoding=gbk
import random
lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

lst=[random.randint(1,100) for item in range(10)]
print(lst)

lst=[i for i in range(10) if i%2==0]
print(lst)

print('-'*40)

lst=[
    ['城市','环比','同比'],
    ['北京','102','103'],
    ['上海','104','504'],
    ['深圳','100','39'],
]
print(lst)

#遍历二维列表使用双层for循环
for row in lst: #行
    for item in row: #列
        print(item,end='\t')
    print()

#四行五列二维列表
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)