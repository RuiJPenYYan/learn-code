#encoding=gbk
t=('python','hello','world')

#根据索引访问元组
print(t[1])
t2=t[0:3:2]   #切片操作
print(t2)

#遍历
for item in t:
    print(item)

print('-'*20)
#for+range()+len()
for i in range(len(t)):
    print(t[i])