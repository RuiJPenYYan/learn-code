#encoding=gbk
lst=[4,67,43,56,87,23,12]
print('原列表',lst)

lst.sort()   #不产生新列表
print('升序',lst)

lst.sort(reverse=True)
print('降序',lst)

print('-'*40)
lst2=['hello','world','happy','Rice','cat']
print('原列表',lst2)


lst2.sort()
print('升序',lst2)

lst2.sort(reverse=True)
print('降序',lst2)

print('-'*40)

#忽略大小写进行比较
lst2.sort(key=str.lower)
print(lst2)