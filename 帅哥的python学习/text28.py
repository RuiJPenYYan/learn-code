#encoding=gbk

#�ֵ�
d={'python':87,'math':89,'zhong':18,'math':22}

#ʹ��ӳ�亯��dict(lst1,lst2)�����ֵ�
#lst1��Ӧ�� lst2��Ӧֵ

lst1=['da','fa','fd','gf']
lst2=[78,54,67,75]

d2=zip(lst1,lst2)

print(d)
#����ͬʱ��ֵ�ᱻ����ĸ���
print(d2) #<zip object at 0x000002043BDDFCC0>
# print(list(d2)) #[('da', 78), ('fa', 54), ('fd', 67), ('gf', 75)]  Ԫ������
#ת�����ֵ�
dd=dict(d2)
print(dd)  #{'da': 78, 'fa': 54, 'fd': 67, 'gf': 75}
d=dict(kick=25,july=43,ins=98)  #���ú��������ֵ�
print(d)

t=(10,20,30)
print({t:10}) #{(10, 20, 30): 10}  Ԫ�����Ϊkey

list=[10,20,30]
# print({list:10}) #TypeError: unhashable type: 'list'
#�б��ǿɱ��������� ������Ϊ�ֵ��е�key

#�ֵ���������
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))

del d
print(d)