#encoding=gbk
s={20,30,40,50}
print(s)
#集合只能存储不可变数据类型
 
s=set()  #创建了一个空集合
print(s)
s={}  #创建的是字典
print(s,type(s))

s=set('helloworld')
print(s)  #集合无序 

s2=set([10,20,30])
print(s2)

s3=set(range(1,10))
print(s3)

print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合s3中存在吗?',(9 in s3))
print('9不在集合s3中存在吗?',(9 not in s3))

del s3
print(s3)