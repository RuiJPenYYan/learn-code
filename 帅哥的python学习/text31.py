#encoding=gbk
import random
d={ item : random.randint(1,100) for item in range(4)}
print(d)
#�ֵ�����ʽ

#ʹ��ӳ�亯��dict(lst1,lst2)�����ֵ�
#lst1��Ӧ�� lst2��Ӧֵ

lst1=['da','fa','fd','gf']
lst2=[78,54,67,75]

d={key:value for key,value in zip(lst1,lst2)}
print(d)