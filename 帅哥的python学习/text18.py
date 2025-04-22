#encoding=gbk
s='helloworld'
#正向索引
for i in range(0,len(s)):
    print(i,s[i],end='\t')
print()

print('-------------------------------------------------------------------------------')

#逆向索引
for i in range(-len(s),0):
    print(i,s[i],end='\t')
print()

print(s[9],s[-1])
print('-----------------------------')

#切片操作
s1=s[0:5:1]
s2=s[0:5:]  #省略步长
s3=s[0:5:2] #2为步长
s4=s[:5:]   #省略开始以及步长
s5=s[0::1]

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print('-------------------------------')
#逆序输出
print(s[-1:-11:-1])
print(s[::-1])