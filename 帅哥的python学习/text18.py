#encoding=gbk
s='helloworld'
#��������
for i in range(0,len(s)):
    print(i,s[i],end='\t')
print()

print('-------------------------------------------------------------------------------')

#��������
for i in range(-len(s),0):
    print(i,s[i],end='\t')
print()

print(s[9],s[-1])
print('-----------------------------')

#��Ƭ����
s1=s[0:5:1]
s2=s[0:5:]  #ʡ�Բ���
s3=s[0:5:2] #2Ϊ����
s4=s[:5:]   #ʡ�Կ�ʼ�Լ�����
s5=s[0::1]

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print('-------------------------------')
#�������
print(s[-1:-11:-1])
print(s[::-1])