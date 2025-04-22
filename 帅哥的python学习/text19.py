#encoding=gbk
#序列的相加和相乘
s1='hello'
s2='world'
s3='helloworld'

print(s1+s2)
print(s1*5)
print(s2*5)
print(s1 in s3)     #判断是否包含在里面
print(s3 in s1)
print(s1 in s1)
print('e在s1中存在吗?',( 'e' in s1))
print('v在s1中不存在吗?',('v' not in s1))
print(s1.index('o'))  #s.index() 找出其第一次出现的位置
print(s3.count('l'))  #s.count() 找出其出现的次数
print('max(s1)',max(s1))   #依据ASCII计算
print('min(s1)',min(s1))