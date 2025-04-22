#encoding=gbk
d={1001:'张梅',1002:'张丽丽',1003:'阿三'}
print(d)

d[1004]='李四'  #直接使用赋值运算符添加元素
print(d)

#获取字典中的所有key
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

#获取字典中的所有value
values=d.values()
print(values)
print(list(values))
print(tuple(values)) 

lst=list(d.items())
print(lst)

d=dict(lst)
print(d)

print(d.pop(1003))
print(d)

print(d.pop(1005,'不存在'))

#随机删除
print(d.popitem())
print(d)

#清空所有元素
d.clear()
print(d)
print(bool(d))  #布尔值