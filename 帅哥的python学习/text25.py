#encoding=gbk
#Ԫ��Ĵ���
t=('hello','python',[1,23,43],'world')
print(t)

#���ú���tuple
t=tuple('helloworld')
print(t)

t=tuple([23,12,12,11])
print(t)

print('10��Ԫ�����Ƿ����:',(10 in t))
print('10��Ԫ���в�����:',(10 not in t))
print('���ֵ:',max(t))
print('��Сֵ:',min(t))
print('len:',len(t))
print('t.index:',t.index(12))
print('t.count:',t.count(12))


t=(10)
print(t,type(t))

t=(10,)
print(t,type(t))

#Ԫ���ɾ��
del t
#print(t)