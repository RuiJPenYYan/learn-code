#encoding=gbk
A={10,20,30,40,50}
B={30,40,50,60,70}

#����
print(A&B)

#����
print(A|B)

#�
print(A-B)

#����
print(A^B)

s={10,20,40,50}
s.add(30)
print(s)

s.remove(20)
print(s)

#s.clear()
#print(s)

#���ϵı���
for item in s:
    print(item)

for index,item in enumerate(s):
    print(index,'-->',item)

s={i for i in range(1,10)}
print(s)

s={i for i in range(1,10) if i%2==1}
print(s)