#encoding=gbk

#字典
d={'python':87,'math':89,'zhong':18,'math':22}

#使用映射函数dict(lst1,lst2)创建字典
#lst1对应键 lst2对应值

lst1=['da','fa','fd','gf']
lst2=[78,54,67,75]

d2=zip(lst1,lst2)

print(d)
#键相同时，值会被后面的覆盖
print(d2) #<zip object at 0x000002043BDDFCC0>
# print(list(d2)) #[('da', 78), ('fa', 54), ('fd', 67), ('gf', 75)]  元组类型
#转换成字典
dd=dict(d2)
print(dd)  #{'da': 78, 'fa': 54, 'fd': 67, 'gf': 75}
d=dict(kick=25,july=43,ins=98)  #内置函数创建字典
print(d)

t=(10,20,30)
print({t:10}) #{(10, 20, 30): 10}  元组可作为key

list=[10,20,30]
# print({list:10}) #TypeError: unhashable type: 'list'
#列表是可变数据类型 不可做为字典中的key

#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))

del d
print(d)