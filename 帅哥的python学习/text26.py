#encoding=gbk
t=('python','hello','world')

#������������Ԫ��
print(t[1])
t2=t[0:3:2]   #��Ƭ����
print(t2)

#����
for item in t:
    print(item)

print('-'*20)
#for+range()+len()
for i in range(len(t)):
    print(t[i])