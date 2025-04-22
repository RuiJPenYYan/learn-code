#encoding=gbk
#元组的创建
t=('hello','python',[1,23,43],'world')
print(t)

#内置函数tuple
t=tuple('helloworld')
print(t)

t=tuple([23,12,12,11])
print(t)

print('10在元组中是否存在:',(10 in t))
print('10在元组中不存在:',(10 not in t))
print('最大值:',max(t))
print('最小值:',min(t))
print('len:',len(t))
print('t.index:',t.index(12))
print('t.count:',t.count(12))


t=(10)
print(t,type(t))

t=(10,)
print(t,type(t))

#元组的删除
del t
#print(t)