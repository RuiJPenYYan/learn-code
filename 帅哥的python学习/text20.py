#encoding=gbk
#ֱ��ʹ��[]�����б�
'''lst=['hello','world',2004,98,100.5]
print(list)

#ʹ�����ú���list�����б�
lst2=list('helloworld')
print(lst2)
lst3=list(range(1,10,2))  # 2 Ϊ����
print(lst3)

#�б������е�һ�֣������еĲ����������������������ʹ��

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
del lst4    #ɾ���б�
print(lst4)
'''


#enumerate����      �б�ı���
#for index,item in enumerate(lst):
#    ���   Ԫ��

lst=['hello','world','python','sone']
#ʹ�ñ���ѭ��for�����б�Ԫ��
for item in lst:
    print(item,end='\t')
print()

#ʹ��forѭ����range()������������������
for i in range(0,len(lst)):
    print(i,'-->',lst[i],end='\t')
print()

#ʹ��enumerate��������
for index,item in enumerate(lst):
    print(index,item,end='\t') #index�����,��������
print()

#�ֶ��޸���ŵ���ʼֵ
for index,item in enumerate(lst,start=1):
    print(index,item,end='\t')
print()

for index,item in enumerate(lst,1):
    print(index,item,end='\t')
print()