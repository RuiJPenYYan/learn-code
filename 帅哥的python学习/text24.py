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
    ['����','����','ͬ��'],
    ['����','102','103'],
    ['�Ϻ�','104','504'],
    ['����','100','39'],
]
print(lst)

#������ά�б�ʹ��˫��forѭ��
for row in lst: #��
    for item in row: #��
        print(item,end='\t')
    print()

#�������ж�ά�б�
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)