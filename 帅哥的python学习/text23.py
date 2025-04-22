#encoding=gbk
lst=[4,67,43,56,87,23,12]
print('原列表',lst)

#升序
print('-'*40)
asc_lst=sorted(lst)
print('升序',asc_lst)
print('原列表',lst)

#降序
print('-'*40)
dasc_lst=sorted(lst,reverse=True)
print('降序',dasc_lst)
print('原列表',lst)