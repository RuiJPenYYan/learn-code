#encoding=gbk
d={'hello':10,'math':20,'python':30}
#�����ֵ�Ԫ��
#(1)
print(d['hello'])
#(2)
print(d.get('hello'))

#���key������,d[]�ᱨ��,d.get()����ָ��Ĭ��ֵ
#print(d['java'])
#KeyError: 'java'
print(d.get('java'))
print(d.get('java','������'))

#�ֵ�ı���
for item in d.items():
    print(item)

for key,value in d.items():
    print(key,'--->',value)