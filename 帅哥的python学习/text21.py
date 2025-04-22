#encoding=gbk
lst=['hello','world','python','sone']
print('原列表',lst,id(lst))
#增加元素
lst.append('ovo')
print('增加后列表',lst,id(lst))

#使用insert(index,x)在指定的index位置上插入元素x
lst.insert(1,'xox')
print('插入后列表',lst,id(lst))

#列表元素的删除操作
lst.remove('hello')
print('删除后的列表',lst,id(lst))

#使用pop(index)根据索引取出元素，然后删除
print(lst.pop(1))
print(lst)

#清除列表中所有元素clear()
#lst.clear()
#print(lst,id(lst))

#列表的反向输出
lst.reverse() #不产生新列表，在原列表基础上进行
print(lst,id(lst))

#列表的拷贝
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素的修改
lst[1]='mysql'
print(lst)