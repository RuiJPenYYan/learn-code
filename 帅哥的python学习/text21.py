#encoding=gbk
lst=['hello','world','python','sone']
print('ԭ�б�',lst,id(lst))
#����Ԫ��
lst.append('ovo')
print('���Ӻ��б�',lst,id(lst))

#ʹ��insert(index,x)��ָ����indexλ���ϲ���Ԫ��x
lst.insert(1,'xox')
print('������б�',lst,id(lst))

#�б�Ԫ�ص�ɾ������
lst.remove('hello')
print('ɾ������б�',lst,id(lst))

#ʹ��pop(index)��������ȡ��Ԫ�أ�Ȼ��ɾ��
print(lst.pop(1))
print(lst)

#����б�������Ԫ��clear()
#lst.clear()
#print(lst,id(lst))

#�б�ķ������
lst.reverse() #���������б���ԭ�б�����Ͻ���
print(lst,id(lst))

#�б�Ŀ���
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#�б�Ԫ�ص��޸�
lst[1]='mysql'
print(lst)