#ecoding=gbk
luck_number = 8

my_name = '钟磊'

print('luck_number的类型是:',type(luck_number))
print('my_name的类型是:',type(my_name))

#动态变量类型的转变
luck_number = '同栖彼女'
nice = '奈奈子'
print('luck_number的类型是:',type(luck_number))

#在python中支持多个变量指向同一个值
no=number=1024  #no和number都指向了1024这个整数值
print(no)
print(number)
print('---------------分割线-----------------')
print(id(no))
print(id(number))

pi = 3.1415926 #变量
PI = 3.1415926 #常量

#常量全用大写字母

#默认为十进制不需要引导符号
# 二进制 0b或0B(引导符号)
# 八进制 0o或0O
# 十六进制 0x或0X
num=978
num2=0b111101
num3=0o56771
num4=0x565A
print(num,num2,num3,num4)
print('---------------分割线-----------------')
print(0.1+0.2) #结果为0.30000000000000004    不确定的整数问题

print(round(0.1+0.2,1))   # 1 的意思是保留一位小数

x=123+456j #复数类型的表示方法 
print(x.real) #实数部分
print(x.imag) #虚数部分
print('-----------------------------')
print('三上悠亚')
print('\'三上悠亚\'')
print('三上\t悠亚')
print(r'三上\t悠亚')   # r或R可使转义字符失效

s='helloworld'
print(s[0],s[-10])  #序号 0 和 -10 是同一个字符、
m='山上有呀'
print(m[0],m[-4])
print(s[2:7])  #从2开始到7结束不包含7
print(m[0:4])

print(luck_number+nice)  #连接两个字符串
print(luck_number*10)   #对这个字符串复制10遍
print('奈奈子'in luck_number)
print('奈奈子'in nice)
# x in s
#如果x为s的子串 则为true否则为false

