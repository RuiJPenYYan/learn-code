#encoding=gbk
import random
d={ item : random.randint(1,100) for item in range(4)}
print(d)
#字典生成式

#使用映射函数dict(lst1,lst2)创建字典
#lst1对应键 lst2对应值

lst1=['da','fa','fd','gf']
lst2=[78,54,67,75]

d={key:value for key,value in zip(lst1,lst2)}
print(d)