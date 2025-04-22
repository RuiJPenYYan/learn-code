#encoding=gbk
a,b=20,10
a/=b
print(a)
#交换两个变量的值
print(a,b)
a,b=b,a
print(a,b)
print('-'*40)
print('按位与计算',12&8)   #换为二进制后计算
print('按位或计算',4|8)
#按位异或 ^
#数位对齐 相同为0 不同为1
print('按位异或',33^22)
#按位取反 ~
print(~8)
print('-'*40)
#移位运算
print('左移位',2<<2)  # 2向左移动两位 高位溢出 后面补0
# 表示的是 2*2*2
print('左移位',2<<3)  #表示的是 2*2*2*2
print('右移位',8>>2)  # 高位端原来是0 就补0 是1 就补1
# 表示的是 8//2，4//2
print('右移位',-8>>2) # -8//2,-4//2
#左乘又除
print('-'*40)
a,b,c,d,e,f,g='sone131'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)