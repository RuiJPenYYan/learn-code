#encoding=gbk
#输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print()
import random
rand=random.randint(1,100)  #产生1-100之间的随机数，包含1和100
count=1
while count<=10:
    number=eval(input('在我心中有一个数,1-100之间,让你猜一猜:'))
    if number==rand:
        break
    elif number>rand:
        print('大了,重新猜:')
    else:
        print('小了,重新猜:')
    count+=1
if count<=3:
    print('真聪明,一共猜了',count,'次')
elif count<=6:
    print('还可以,一共猜了',count,'次')
else:
    print('猜的次数有点多,一共猜了',count,'次')
