#encoding=gbk
d={1001:'��÷',1002:'������',1003:'����'}
print(d)

d[1004]='����'  #ֱ��ʹ�ø�ֵ��������Ԫ��
print(d)

#��ȡ�ֵ��е�����key
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

#��ȡ�ֵ��е�����value
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

print(d.pop(1005,'������'))

#���ɾ��
print(d.popitem())
print(d)

#�������Ԫ��
d.clear()
print(d)
print(bool(d))  #����ֵ