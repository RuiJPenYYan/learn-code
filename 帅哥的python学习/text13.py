#encoding=gbk
s=0
i=1
while i<=100:
    if i%2==1:
        i+=1
        continue
    s+=i
    i+=1
print('1-100֮���ż����:',s)

print('-----------------------------')
s=0
for i in range(1,101):
    if i%2==0:
        continue
    s+=i
print('1-100֮���������Ϊ:',s)