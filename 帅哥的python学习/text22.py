#encoding=gbk
lst=[4,67,43,56,87,23,12]
print('ԭ�б�',lst)

lst.sort()   #���������б�
print('����',lst)

lst.sort(reverse=True)
print('����',lst)

print('-'*40)
lst2=['hello','world','happy','Rice','cat']
print('ԭ�б�',lst2)


lst2.sort()
print('����',lst2)

lst2.sort(reverse=True)
print('����',lst2)

print('-'*40)

#���Դ�Сд���бȽ�
lst2.sort(key=str.lower)
print(lst2)