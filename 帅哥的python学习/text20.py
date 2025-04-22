#encoding=gbk
#直接使用[]创建列表
'''lst=['hello','world',2004,98,100.5]
print(list)

#使用内置函数list创建列表
lst2=list('helloworld')
print(lst2)
lst3=list(range(1,10,2))  # 2 为步长
print(lst3)

#列表是序列的一种，对序列的操作符，运算符，函数均可使用

print(lst+lst2+lst3)
print(lst2 in lst)
print(lst*3)
print(len(lst))
print(max(lst3))
print(min(lst2))
print(lst2.count('o'))
print(lst2.index('o'))
print('-'*40)
lst4=[10,20,40]
print(lst4)
del lst4    #删除列表
print(lst4)
'''


#enumerate函数      列表的遍历
#for index,item in enumerate(lst):
#    序号   元素

lst=['hello','world','python','sone']
#使用遍历循环for遍历列表元素
for item in lst:
    print(item,end='\t')
print()

#使用for循环，range()函数，根据索引遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i],end='\t')
print()

#使用enumerate函数遍历
for index,item in enumerate(lst):
    print(index,item,end='\t') #index是序号,不是索引
print()

#手动修改序号的起始值
for index,item in enumerate(lst,start=1):
    print(index,item,end='\t')
print()

for index,item in enumerate(lst,1):
    print(index,item,end='\t')
print()